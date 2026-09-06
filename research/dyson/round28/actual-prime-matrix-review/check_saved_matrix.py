"""Independent bounded audit of saved matrices; no full prime sieve or new height."""
from __future__ import annotations
import hashlib
import json
import math
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'actual-prime-matrix-test'


def file_info(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def seed(x):
    if abs(x) >= .5:
        return 0.
    return math.exp(-1 / (1 - 4*x*x))


def profile(x):
    z = (x - 1.5) / .45
    return math.exp(1 - 1/(1-z*z)) if abs(z) < 1 else 0.


denom, denom_error = quad(lambda x: seed(x)**2, -.5, .5,
                         epsabs=2e-14, epsrel=2e-13, limit=120)
inner_errors = []


def omega(u):
    v = abs(4*(u-2))
    if v >= 1:
        return 0.
    integral, err = quad(lambda x: seed(x)*seed(x-v), v-.5, .5,
                         epsabs=2e-14, epsrel=2e-13, limit=120)
    inner_errors.append(err / denom)
    return integral / denom


# Small independent trial-prime list only; no re-sieving of the 29M endpoint.
primes = []
for n in range(2, 5500):
    if all(n % p for p in primes if p*p <= n):
        primes.append(n)


def factor(n):
    factors = []
    for p in primes:
        if p*p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            factors.append((p, e))
    if n > 1:
        factors.append((n, 1))
    return factors


def mangoldt(n):
    fs = factor(n)
    return math.log(fs[0][0]) if len(fs) == 1 else 0.


def mobius(n):
    fs = factor(n)
    return 0 if any(e > 1 for _, e in fs) else (-1)**len(fs)


manifest = json.loads((AUTHOR/'AUTHOR_RECEIPT.json').read_text())
source_manifest = json.loads((AUTHOR/'source_receipt.json').read_text())
pins = []
for kind, entries, base in [('author', manifest['files'], AUTHOR),
                            ('source', source_manifest['files'], None)]:
    for entry in entries:
        path = base / entry['path'] if base else Path(entry['path'])
        actual = file_info(path)
        assert all(actual[k] == entry[k] for k in ('bytes', 'sha256'))
        pins.append({'kind': kind, 'path': entry['path'], **actual, 'matches': True})

coeff = np.load(AUTHOR/'arrays/lambda_coefficients.npz')
indices, lambda_values = coeff['indices'], coeff['values']
assert np.all(np.diff(indices.astype(np.int64)) > 0)
assert np.all(lambda_values > 0) and indices[-1] <= coeff['limit'][0]


def saved_lambda(n):
    at = int(np.searchsorted(indices, n))
    return float(lambda_values[at]) if at < len(indices) and indices[at] == n else 0.


fixture_errors = {}
for n in [1,2,3,4,6,8,9,25,27,45,49,125,10201,59049,29157201]:
    error = abs(mangoldt(n)-saved_lambda(n))
    assert error < 2e-14
    fixture_errors[str(n)] = error

reported = {c['X']: c for c in json.loads((AUTHOR/'results.json').read_text())['cases']}
mellin_reported = {c['X']: c for c in json.loads((AUTHOR/'mellin_results.json').read_text())['cases']}
cases = []
for X in (1_000_000,4_000_000,16_000_000):
    z = np.load(AUTHOR/f'arrays/case_{X}.npz')
    C, rows, products = z['C'], z['row_integers'], z['unique_products']
    inverse = z['inverse_product_index']
    T = math.isqrt(X); ell = math.log(T); n = len(rows)
    expected_rows = np.arange(21*T//20+1,27*T//20+1,dtype=np.int64)
    expected_rows = expected_rows[expected_rows%2 == 1]
    assert np.array_equal(rows,expected_rows)
    assert np.array_equal(products[inverse].reshape(n,n),rows[:,None]*rows[None,:])
    assert np.array_equal(C,C.T)
    assert np.array_equal(C,z['f_values'][inverse].reshape(n,n))
    assert np.array_equal(z['f_values'],z['b64']*z['chi_product']*z['centered_window_sum'])
    expected_shifts = np.array([h for h in range(2,2*T+1,2) if profile(h/T)>0])
    assert np.array_equal(expected_shifts,z['shifts'])
    assert np.max(abs(np.array([profile(h/T) for h in expected_shifts])-z['V_shift'])) < 1e-14
    assert np.max(abs(z['centered_window_sum']-(z['prime_window_sum']-z['flat2_window_sum']))) < 1e-9
    a = np.array([mobius(int(d)) for d in rows],dtype=float)
    assert np.array_equal(a,z['mobius'])
    assert np.array_equal(a,coeff['mobius_prefix'][rows])
    b = np.log(rows)
    assert np.array_equal(b,z['log_vector'])
    eig, vec = z['eigenvalues'],z['eigenvectors']
    frob = float(np.linalg.norm(C)); op = abs(float(eig[0]))
    assert np.all(np.abs(eig[:-1]) >= np.abs(eig[1:]))
    residual = float(np.linalg.norm(C@vec-vec*eig))/frob
    orth_error = float(np.max(np.abs(vec.T@vec-np.eye(n))))
    assert residual < 2e-12 and orth_error < 2e-12
    reconstructed = (vec*eig)@vec.T
    reconstruction_error = float(np.linalg.norm(C-reconstructed))/frob
    assert reconstruction_error < 2e-12
    normalized_Z = float(2*(a@C@b)/(X*ell**2))
    cauchy = float(2*np.linalg.norm(a)*op*np.linalg.norm(b)/(X*ell**2))
    assert abs(normalized_Z-reported[X]['normalized_Z_block']) < 1e-13
    assert abs(cauchy-reported[X]['normalized_operator_Cauchy_bound']) < 1e-13
    normalized = {'op_norm':op,'frobenius_norm':frob,
        'top_energy_fraction':op**2/frob**2,'stable_rank':frob**2/op**2,
        'sigma2_over_sigma1':abs(float(eig[1]))/op,
        'op_squared_over_X_logX_squared':op**2/(X*math.log(X)**2),
        'op_squared_over_X_logX':op**2/(X*math.log(X)),
        'normalized_Z_block':normalized_Z,'normalized_operator_Cauchy_bound':cauchy}
    assert all(abs(v-reported[X][k]) < 2e-11*max(1,abs(v)) for k,v in normalized.items())

    # Three predetermined sample types: lower corner, non-diagonal interior,
    # and the first product interval containing a square of the first prime >=1.2T.
    p = next(p for p in primes if p >= 6*T//5)
    at = int(np.searchsorted(products,p*p-int(expected_shifts[-1])))
    assert at < len(products) and p*p-int(products[at]) in expected_shifts
    loc = int(np.flatnonzero(inverse==at)[0])
    locations = [(0,0),(n//3,2*n//3),divmod(loc,n)]
    direct = []
    for i,j in locations:
        m = int(rows[i]*rows[j]); pos=int(np.searchsorted(products,m))
        hs = [int(h) for h in expected_shifts]
        lams = [mangoldt(m+h) for h in hs]
        lambda_error=max(abs(value-saved_lambda(m+h)) for h,value in zip(hs,lams))
        assert lambda_error < 2e-14
        weights=[profile(h/T)*math.exp(-T*math.log1p(h/m)) for h in hs]
        center=math.fsum(w*(value-2) for w,value in zip(weights,lams))
        prime=math.fsum(w*value for w,value in zip(weights,lams))
        flat=2*math.fsum(weights)
        integral,qerr=quad(lambda r:math.exp(-r)*omega(math.log(m)/ell-r/((T-1)*ell)),
                           0,48,epsabs=3e-12,epsrel=3e-12,limit=100)
        prefactor=X/m*T/(T-1)*integral
        entry=prefactor*profile(m/X)*center
        entry_error=abs(entry-float(C[i,j]))
        assert entry_error < 2e-9*max(1,abs(entry))
        power_hits=[{'n':m+h,'factorization':factor(m+h)} for h,value in zip(hs,lams)
                    if value and factor(m+h)[0][1]>1]
        direct.append({'i':int(i),'j':int(j),'m':m,'terms':len(hs),
            'stored_entry':float(C[i,j]),'independent_entry':entry,'absolute_error':entry_error,
            'max_saved_lambda_error':lambda_error,'higher_prime_powers':power_hits,
            'window_sum_abs_error':abs(center-float(z['centered_window_sum'][pos])),
            'prime_sum_abs_error':abs(prime-float(z['prime_window_sum'][pos])),
            'flat2_sum_abs_error':abs(flat-float(z['flat2_window_sum'][pos])),
            'prefactor_abs_error':abs(prefactor-float(z['b64'][pos])),
            'outer_quad_reported_error':qerr,
            'analytic_prefactor_tail_bound':X/m*T/(T-1)*math.exp(-48)})
    assert direct[-1]['higher_prime_powers']

    mm=np.load(AUTHOR/f'arrays/mellin_{X}.npz')
    freq=mm['frequencies']; winner=int(np.argmax(mm['right_projection']))
    logcoord=np.log(rows/float(rows[n//2])); top=vec[:,0]
    assert len(freq)==4*n
    assert np.array_equal(freq,np.linspace(0,np.pi/np.min(np.diff(np.log(rows.astype(float)))),4*n))
    sample_indices=sorted({0,1,n,2*n,len(freq)-1,winner})
    mellin_checks=[]
    for index in sample_indices:
        t=float(freq[index])
        basis=np.ones((n,1)) if index==0 else np.column_stack((np.cos(t*logcoord),np.sin(t*logcoord)))
        q,_=np.linalg.qr(basis,mode='reduced')
        projection=float(np.linalg.norm(q.T@top)**2)
        error=abs(projection-float(mm['right_projection'][index]))
        assert error<2e-12
        mellin_checks.append({'index':index,'frequency':t,'independent_QR_projection':projection,'absolute_error':error})
    assert abs(float(mm['right_projection'][winner])-mellin_reported[X]['maximum_squared_projection'])<1e-14
    cases.append({'X':X,'dimension':n,'all_support_and_array_identities_pass':True,
        'all_eigenpair_residual_over_frobenius':residual,'eigenvector_max_orthogonality_error':orth_error,
        'spectral_reconstruction_relative_frobenius_error':reconstruction_error,
        'normalizations':normalized,'direct_entries':direct,
        'stored_b32_b64_max_relative':float(np.max(abs(z['b32']-z['b64'])/abs(z['b64']))),
        'mellin_selected_QR_checks':mellin_checks})

out={'status':'PASS','scope':'Saved-array algebra, all stored eigenpairs, nine independently factored direct entries and selected Mellin QR checks. No broad prime scan, new height, eigensolver, or interval certificate.',
     'software':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
     'pins':pins,'coefficient_fixture_errors':fixture_errors,
     'independent_autocorrelation_denominator':denom,'denominator_quad_reported_error':denom_error,
     'maximum_inner_normalized_quad_reported_error':max(inner_errors),'cases':cases}
encoded=json.dumps(out,indent=2,sort_keys=True)+'\n'
(HERE/'independent_matrix_checks.json').write_text(encoded)
print(encoded,end='')
