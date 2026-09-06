"""Predeclared deterministic R28 actual-prime matrix diagnostic; float64 only."""
from __future__ import annotations

import hashlib
import io
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.special import roots_laguerre, roots_legendre

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
ARRAYS = HERE / 'arrays'
XS = (1_000_000, 4_000_000, 16_000_000)


def emit(value: dict) -> None:
    print(json.dumps(value, sort_keys=True), flush=True)


def bump(t: np.ndarray | float) -> np.ndarray:
    t = np.asarray(t, dtype=np.float64)
    z = (t - 1.5) / .45
    out = np.zeros_like(z)
    inside = np.abs(z) < 1
    out[inside] = np.exp(1 - 1/(1-z[inside]**2))
    return out


def seed(t: np.ndarray) -> np.ndarray:
    out = np.zeros_like(t)
    inside = np.abs(t) < .5
    out[inside] = np.exp(-1/(1-4*t[inside]**2))
    return out


class Omega:
    def __init__(self, size: int, order: int):
        nodes, weights = roots_legendre(order)
        self.nodes, self.weights = nodes, weights
        self.s2 = float(np.dot(weights, seed(nodes/2)**2)/2)
        self.grid = np.linspace(0, 1, size)
        values = self.direct_psi(self.grid)
        self.values = values
        self.spline = CubicSpline(self.grid, values, bc_type=((1, 0.), (1, 0.)))

    def direct_psi(self, v: np.ndarray | float) -> np.ndarray:
        v = np.abs(np.asarray(v, dtype=np.float64))
        out = np.zeros_like(v)
        inside = v < 1
        z = v[inside]
        # Intersection of [-1/2,1/2] with [v-1/2,v+1/2].
        width = (1-z)/2
        x = z[:, None]/2 + width[:, None]*self.nodes
        out[inside] = width*np.sum(self.weights*seed(x)*seed(x-z[:, None]), axis=1)/self.s2
        return out

    def __call__(self, u: np.ndarray) -> np.ndarray:
        v = np.abs(4*(u-2))
        out = np.zeros_like(v)
        inside = v < 1
        out[inside] = self.spline(v[inside])
        return out

    def direct(self, u: float) -> float:
        return float(self.direct_psi(np.asarray([4*(u-2)]))[0])


def lambda_sieve(limit: int) -> tuple[np.ndarray, np.ndarray]:
    primal = np.ones(limit+1, dtype=np.bool_)
    primal[:2] = False
    primal[4::2] = False
    for p in range(3, math.isqrt(limit)+1, 2):
        if primal[p]:
            primal[p*p::p] = False
    primes = np.flatnonzero(primal)
    values = np.zeros(limit+1, dtype=np.float64)
    values[primes] = np.log(primes)
    for p in primes[primes <= math.isqrt(limit)]:
        p = int(p)
        power = p*p
        while power <= limit:
            values[power] = math.log(p)
            power *= p
    del primal
    return values, primes


def mobius_sieve(limit: int, primes: np.ndarray) -> np.ndarray:
    mu = np.ones(limit+1, dtype=np.int8)
    mu[0] = 0
    for p in primes[primes <= limit]:
        p = int(p)
        mu[p::p] *= -1
        mu[p*p::p*p] = 0
    return mu


def b_prefactor(products: np.ndarray, X: int, T: int, omega: Omega, order: int) -> np.ndarray:
    nodes, weights = roots_laguerre(order)
    ell = math.log(T)
    out = np.empty(len(products))
    for start in range(0, len(products), 8192):
        m = products[start:start+8192].astype(np.float64)
        u = np.log(m)[:, None]/ell - nodes/((T-1)*ell)
        out[start:start+len(m)] = X/m*T/(T-1)*(omega(u) @ weights)
    return out


def orthonormal_span(features: np.ndarray) -> np.ndarray:
    u, s, _ = np.linalg.svd(features, full_matrices=False)
    return u[:, s > s[0]*1e-12]


def overlap(u: np.ndarray, v: np.ndarray) -> float:
    return float(np.dot(u, v)**2 / np.dot(v, v))


def run_case(X: int, lam: np.ndarray, mu: np.ndarray, coarse: Omega, fine: Omega) -> dict:
    started = time.perf_counter()
    T = math.isqrt(X)
    assert T*T == X
    ell = math.log(T)
    rows = np.arange(21*T//20+1, 27*T//20+1, dtype=np.int64)
    rows = rows[rows % 2 == 1]
    n = len(rows)
    matrix_products = rows[:, None]*rows[None, :]
    assert np.all((matrix_products > X) & (matrix_products < 2*X))
    products, inverse = np.unique(matrix_products, return_inverse=True)
    inverse = inverse.ravel()
    shifts = np.arange(2, 2*T+1, 2, dtype=np.int64)
    weights_v = bump(shifts/T)
    keep = weights_v > 0
    shifts, weights_v = shifts[keep], weights_v[keep]
    assert np.all(shifts % 2 == 0)
    assert products[-1]+shifts[-1] < len(lam)
    emit({'stage':'case_start', 'X':X, 'T':T, 'dimension':n, 'unique_products':len(products), 'even_shifts':len(shifts), 'direct_terms':int(len(products)*len(shifts))})

    b32 = b_prefactor(products, X, T, coarse, 32)
    b64 = b_prefactor(products, X, T, fine, 64)
    b_abs = float(np.max(np.abs(b64-b32)))
    b_rel = float(np.max(np.abs(b64-b32)/np.maximum(np.abs(b64), 1e-300)))
    assert b_rel < 1e-9
    window = np.empty(len(products))
    prime_part, flat_part = np.empty_like(window), np.empty_like(window)
    for start in range(0, len(products), 1024):
        m = products[start:start+1024]
        weights = np.exp(-T*np.log1p(shifts[None, :]/m[:, None]))*weights_v
        coefficients = lam[m[:, None]+shifts]
        prime_part[start:start+len(m)] = np.sum(weights*coefficients, axis=1)
        flat_part[start:start+len(m)] = 2*np.sum(weights, axis=1)
        window[start:start+len(m)] = np.sum(weights*(coefficients-2), axis=1)
    assert np.max(np.abs(window-(prime_part-flat_part))) < 1e-9
    profile = bump(products/X)
    f_values = b64*profile*window
    C = f_values[inverse].reshape((n, n))
    C32 = (b32*profile*window)[inverse].reshape((n, n))
    assert np.array_equal(C, C.T)
    quadrature_matrix_frobenius_difference = float(np.linalg.norm(C-C32))
    del C32
    values, vectors = np.linalg.eigh(C)
    order = np.argsort(-np.abs(values), kind='stable')
    values, vectors = values[order], vectors[:, order]
    for j in range(n):
        if np.sum(vectors[:, j]) < 0:
            vectors[:, j] *= -1
    sigma = abs(float(values[0]))
    frob = float(np.linalg.norm(C))
    norm_identity_error = abs(float(np.dot(values, values))-frob**2)/(frob**2)
    eigen_residual = float(np.linalg.norm(C@vectors[:, :8]-vectors[:, :8]*values[:8]))/frob
    assert norm_identity_error < 1e-11 and eigen_residual < 1e-11

    a = mu[rows].astype(np.float64)
    b = np.log(rows)
    contraction = float(a@C@b)
    grouped_weights = np.bincount(inverse, weights=(a[:, None]*b[None, :]).ravel(), minlength=len(products))
    grouped_contraction = float(grouped_weights@f_values)
    contraction_check = abs(contraction-grouped_contraction)/max(1., abs(contraction))
    assert contraction_check < 1e-10
    bound = float(np.linalg.norm(a)*sigma*np.linalg.norm(b))
    constant = np.ones(n)
    centered_log = b-np.mean(b)
    coord = (rows/T-1.05)/.3
    smooth_features = np.column_stack([constant]+[fun(2*np.pi*j*coord) for j in range(1, 5) for fun in (np.cos, np.sin)])
    arith_features = np.column_stack([(rows % p == r).astype(float) for p in (3,5,7) for r in range(p)])
    smooth_Q, arith_Q = orthonormal_span(smooth_features), orthonormal_span(arith_features)
    top = vectors[:, 0]
    overlaps = {'constant':overlap(top, constant), 'log':overlap(top, b), 'centered_log':overlap(top, centered_log), 'mobius':overlap(top, a), 'smooth_9dim':float(np.linalg.norm(smooth_Q.T@top)**2), 'residues_mod_3_5_7':float(np.linalg.norm(arith_Q.T@top)**2)}
    subspace_gains = {'smooth':float(np.linalg.svd(C@smooth_Q, compute_uv=False)[0]/sigma), 'arithmetic':float(np.linalg.svd(C@arith_Q, compute_uv=False)[0]/sigma)}

    locations = [(0,0),(0,n//2),(0,n-1),(n//4,n//4),(n//2,n//2),(n//4,3*n//4),(n-1,0),(n-1,n//2),(n-1,n-1)]
    direct_checks = []
    for i,j in locations:
        m = int(rows[i]*rows[j])
        full = math.fsum(float(v)*math.exp(-T*math.log1p(int(h)/m))*(float(lam[m+int(h)])-2) for h,v in zip(shifts, weights_v))
        integral, quad_error = quad(lambda r:math.exp(-r)*fine.direct(math.log(m)/ell-r/((T-1)*ell)), 0, 48, epsabs=2e-12, epsrel=2e-12, limit=100)
        direct_b = X/m*T/(T-1)*integral
        direct_C = direct_b*float(bump(m/X))*full
        error = abs(direct_C-C[i,j])
        assert error < 1e-8*max(1., abs(C[i,j]))
        direct_checks.append({'i':i,'j':j,'m':m,'matrix_value':float(C[i,j]),'direct_value':direct_C,'absolute_error':error,'adaptive_quad_reported_error':quad_error,'omitted_r_tail_upper':X/m*T/(T-1)*math.exp(-48)})

    np.savez_compressed(ARRAYS/f'case_{X}.npz', C=C, row_integers=rows, unique_products=products, inverse_product_index=inverse, shifts=shifts, V_shift=weights_v, b32=b32, b64=b64, chi_product=profile, centered_window_sum=window, prime_window_sum=prime_part, flat2_window_sum=flat_part, f_values=f_values, mobius=a, log_vector=b, eigenvalues=values, eigenvectors=vectors, grouped_coefficient=grouped_weights, smooth_basis=smooth_Q, arithmetic_basis=arith_Q)
    result = {'X':X,'T':T,'ell':ell,'dimension':n,'row_min':int(rows[0]),'row_max':int(rows[-1]),'product_min':int(products[0]),'product_max':int(products[-1]),'unique_products':len(products),'even_shift_count':len(shifts),'shift_min':int(shifts[0]),'shift_max':int(shifts[-1]),'direct_terms':int(len(products)*len(shifts)), 'op_norm':sigma,'frobenius_norm':frob,'top_eigenvalue':float(values[0]),'top_eigenvalues':values[:8].tolist(),'top_energy_fraction':sigma**2/frob**2,'stable_rank':frob**2/sigma**2,'sigma2_over_sigma1':float(abs(values[1])/sigma),'matrix_mean':float(np.mean(C)),'constant_rayleigh_over_op':float(abs(constant@C@constant)/n/sigma),'op_squared_over_X_logX_squared':sigma**2/(X*math.log(X)**2),'op_squared_over_X_logX':sigma**2/(X*math.log(X)),'raw_mu_log_contraction':contraction,'normalized_Z_block':2*contraction/(X*ell**2),'normalized_operator_Cauchy_bound':2*bound/(X*ell**2),'contraction_fraction_of_operator_bound':contraction/bound,'top_mode_fraction_of_contraction':float(values[0]*np.dot(a,top)*np.dot(top,b)/contraction) if contraction else None,'top_vector_squared_overlaps':overlaps,'test_subspace_dimensions':{'smooth':smooth_Q.shape[1],'arithmetic':arith_Q.shape[1]},'restricted_input_op_over_full_op':subspace_gains,'checks':{'b32_b64_max_absolute':b_abs,'b32_b64_max_relative':b_rel,'matrix_quadrature_frobenius_difference':quadrature_matrix_frobenius_difference,'eigen_residual_over_frobenius':eigen_residual,'frobenius_eigenvalue_relative_error':norm_identity_error,'grouped_contraction_relative_error':contraction_check,'direct_entries':direct_checks},'seconds':time.perf_counter()-started}
    emit({'stage':'case_complete',**{k:result[k] for k in ['X','dimension','op_norm','frobenius_norm','normalized_Z_block','top_energy_fraction','sigma2_over_sigma1','top_vector_squared_overlaps','seconds']}})
    return result


def main() -> None:
    ARRAYS.mkdir(exist_ok=True)
    start = time.perf_counter()
    coarse, fine = Omega(8193, 128), Omega(16385, 256)
    np.savez_compressed(ARRAYS/'omega_quadrature.npz', coarse_grid=coarse.grid,coarse_psi=coarse.values,fine_grid=fine.grid,fine_psi=fine.values,coarse_nodes=coarse.nodes,coarse_weights=coarse.weights,fine_nodes=fine.nodes,fine_weights=fine.weights,s2=np.array([coarse.s2,fine.s2]))
    largest_T = math.isqrt(XS[-1])
    largest_d = 27*largest_T//20
    if largest_d % 2 == 0: largest_d -= 1
    limit = largest_d**2+2*largest_T
    emit({'stage':'sieve_start','limit':limit})
    lam, primes = lambda_sieve(limit)
    mu = mobius_sieve(largest_d, primes)
    fixtures = {1:0.,2:math.log(2),3:math.log(3),4:math.log(2),8:math.log(2),9:math.log(3),25:math.log(5),27:math.log(3),49:math.log(7),125:math.log(5),6:0.,45:0.}
    assert all(abs(lam[n]-x)<1e-14 for n,x in fixtures.items())
    support = np.flatnonzero(lam).astype(np.uint32)
    np.savez_compressed(ARRAYS/'lambda_coefficients.npz', indices=support,values=lam[support],limit=np.array([limit],dtype=np.int64),mobius_prefix=mu)
    emit({'stage':'sieve_complete','nonzero_lambda_coefficients':len(support),'seconds':time.perf_counter()-start})
    results, omitted = [], []
    for X in XS:
        if len(results)==2 and results[-1]['seconds']*8>600:
            omitted.append({'X':X,'reason':'Predeclared resource guard: second-case time times eight exceeds 600 seconds.'})
            break
        result = run_case(X,lam,mu,coarse,fine)
        results.append(result)
        (HERE/'results.partial.json').write_text(json.dumps(results,indent=2)+'\n')
    final={'scope':'Deterministic float64 actual Lambda matrix diagnostic; no interval certificate or asymptotic inference. No mode subtraction.','predeclared_X':list(XS),'omitted':omitted,'software':{'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'platform':platform.platform(),'threads':{key:os.environ.get(key) for key in ('OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','OMP_NUM_THREADS')}},'sieve':{'limit':limit,'nonzero_coefficients':len(support),'fixtures':fixtures},'profile':{'chi_and_V':'exp(1-1/(1-((t-1.5)/0.45)^2)) for abs(t-1.5)<0.45; zero elsewhere','omega':'Actual R16 psi(4(u-2)); fixed flat-seed normalized autocorrelation','row_interval':'1.05T<d,k<=1.35T, all odd integers','b_integral':'Gauss-Laguerre stable transformed exact b_T integral; 32/64 comparison'},'cases':results,'total_seconds':time.perf_counter()-start}
    (HERE/'results.json').write_text(json.dumps(final,indent=2)+'\n')
    emit({'stage':'complete','cases':len(results),'omitted':omitted,'total_seconds':final['total_seconds']})


if __name__ == '__main__':
    main()
