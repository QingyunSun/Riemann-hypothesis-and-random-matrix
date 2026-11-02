#!/usr/bin/env python3
"""Fixed two-distinct-large-prime interaction; floating quadrature, not enclosures."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from functools import lru_cache
import numpy as np
from numpy.polynomial.legendre import legval

HERE = Path(__file__).resolve().parent
PRIOR = Path(os.environ.get('ASTRA_LARGE_PRIME_SOURCE', '/Users/qingyunsun/Library/CloudStorage/Dropbox/Code/Riemann zeta RMT/Astra-Research/research/dyson/round7/arithmetic-resonator/large_prime_sector.py'))
PRIOR_SHA = '255ad9a2f29e086eca01b3823bd9ece3ecbfa47b431259a6af3fee260c9afa8d'
assert hashlib.sha256(PRIOR.read_bytes()).hexdigest() == PRIOR_SHA
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('prior_fixed_moments', PRIOR)
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
moment, expand, gauss, solve = prior.moment, prior.expand, prior.gauss, prior.solve
BASE_GROUPS, MARK_GROUPS = prior.BASE_GROUPS, prior.MARK_GROUPS
TAU = 1/3


@lru_cache(maxsize=2048)
def marked_values(a, ks, values, mode, order):
    """E[C P]/(v-tau)^a or E[D P]/(v-2tau)^(a+1)."""
    v = np.asarray(values)
    z, wz = gauss(order, a-1)
    if mode == 1:
        delta = v-TAU
        p = v[:, None]-delta[:, None]*z
        inserted = [p]
        rem = delta[:, None]*z
        weight = wz[None, :]/p
    else:
        assert mode == 2
        delta = v-2*TAU
        s, ws = gauss(order, 0)
        z, s = np.meshgrid(z, s, indexing='ij')
        wz, ws = np.meshgrid(wz, ws, indexing='ij')
        z, s, wz, ws = z.ravel(), s.ravel(), wz.ravel(), ws.ravel()
        p = TAU+delta[:, None]*(1-z)*s
        q = TAU+delta[:, None]*(1-z)*(1-s)
        inserted = [p, q]
        rem = delta[:, None]*z
        weight = (wz*ws*(1-z))[None, :]/(p*q)
    out = np.zeros(len(v))
    for bits in range(1 << len(ks)):
        remaining = tuple(k for j, k in enumerate(ks) if not (bits >> j) & 1)
        factor = rem**sum(remaining)
        for j, k in enumerate(ks):
            if (bits >> j) & 1:
                factor = factor*sum(u**k for u in inserted)
        out += moment(a, remaining)*np.sum(weight*factor, axis=1)
    coefficient = a if mode == 1 else a*a/2
    return coefficient*v**(1-a)*out


def background_moment(a, ks, v, mode, order):
    if mode == 0:
        return moment(a, ks)*v**sum(ks)
    unique, inverse = np.unique(v, return_inverse=True)
    return marked_values(a, ks, tuple(unique), mode, order)[inverse]


def choose_two(c):
    return c*(c-1)/2


class FormBuilder:
    def __init__(self, ell, degree, order):
        self.ell, self.a, self.degree, self.order = ell, ell*ell, degree, order
        self.groups = [(ks, 0) for ks in BASE_GROUPS]+[(ks, 1) for ks in MARK_GROUPS]
        self.features = [(d, ks, mark) for ks, mark in self.groups for d in range(degree+1)]
        self.mark_order = max(28, order)

    def cross(self, v, left, right, weight, mode):
        v = np.ravel(v)
        left, right = [np.ravel(u) for u in left], [np.ravel(u) for u in right]
        weight, n, d = np.ravel(weight), len(v), self.degree+1
        ml, mr = v+sum(left), v+sum(right)
        dl = sum((u > TAU).astype(float) for u in left) if left else np.zeros(n)
        dr = sum((u > TAU).astype(float) for u in right) if right else np.zeros(n)
        rl = {c: np.array([legval(2*ml-1 if c == 0 else 6*ml-5, [0]*j+[1]) for j in range(d)]).T for c in (0, 1)}
        rr = {c: np.array([legval(2*mr-1 if c == 0 else 6*mr-5, [0]*j+[1]) for j in range(d)]).T for c in (0, 1)}
        xl = {ks: expand(ks, left, n) for ks, _ in self.groups}
        xr = {ks: expand(ks, right, n) for ks, _ in self.groups}
        cache, out = {}, np.zeros((len(self.features), len(self.features)))
        for i, (ks, ci) in enumerate(self.groups):
            for j, (eta, cj) in enumerate(self.groups):
                q = []
                for count in (0, 1, 2):
                    q.append((choose_two(count+dl) if ci else np.ones(n))*(choose_two(count+dr) if cj else np.ones(n)))
                coefficient = (q[0], q[1]-q[0], q[2]-2*q[1]+q[0])[mode]
                if not np.any(coefficient):
                    continue
                value = np.zeros(n)
                for kl, cl in xl[ks].items():
                    for kr, cr in xr[eta].items():
                        key = tuple(sorted(kl+kr))
                        if key not in cache:
                            cache[key] = background_moment(self.a, key, v, mode, self.mark_order)
                        value += cl*cr*cache[key]
                out[i*d:(i+1)*d, j*d:(j+1)*d] = rl[ci].T@((weight*coefficient*value)[:, None]*rr[cj])
        return out

    def v_slabs(self, mode):
        offset = mode*TAU
        power = (self.a-1, self.a, self.a+1)[mode]
        endpoints = [x for x in (0., TAU, 2*TAU, 1.) if x >= offset]
        for lo, hi in zip(endpoints[:-1], endpoints[1:]):
            if lo == offset:
                v, w = gauss(self.order, power, lo, hi)
            else:
                v, w = gauss(self.order, 0, lo, hi)
                w *= (v-offset)**power
            if mode:
                w *= v**(self.a-1)
            yield v, w

    def m2(self, V, U, W, weights, mode):
        weights = weights*(self.ell**2/2)*np.sinc(U/2)*np.sinc(W/2)
        return self.cross(V, [], [U, W], weights, mode)+self.cross(V, [U], [W], weights, mode)

    def forms(self):
        size = len(self.features)
        G, M = np.zeros((size, size)), np.zeros((size, size))
        z, wz = gauss(self.order, 0)
        for mode in (0, 1, 2):
            for v, vw in self.v_slabs(mode):
                G += self.cross(v, [], [], vw, mode)
                V, Z = np.meshgrid(v, z, indexing='ij')
                Wv, Wz = np.meshgrid(vw, wz, indexing='ij')
                U = (1-V)*Z
                # Same-prime A*A: H0^2, never an inserted D or g(u)^2.
                weights = Wv*Wz*(1-V)*U*np.sinc(U/2)**2/2
                M += self.cross(V, [], [], weights, mode)
                # Slice every u,w threshold plane; no discontinuous masks are
                # left in the interior of a quadrature box.
                if v.max() < TAU:
                    bounds = [np.zeros_like(v), np.full_like(v, TAU), 1-v-TAU, 1-v]
                elif v.max() < 2*TAU:
                    bounds = [np.zeros_like(v), 1-v-TAU, np.full_like(v, TAU), 1-v]
                else:
                    bounds = [np.zeros_like(v), 1-v]
                for ulo, uhi in zip(bounds[:-1], bounds[1:]):
                    U = ulo[:, None]+(uhi-ulo)[:, None]*z
                    uw = (uhi-ulo)[:, None]*wz
                    V = np.broadcast_to(v[:, None], U.shape)
                    Wv = np.broadcast_to(vw[:, None], U.shape)
                    end = 1-V-U
                    cut = np.minimum(end, TAU)
                    for wlo, whi in [(np.zeros_like(end), cut), (cut, end)]:
                        W = wlo[:, :, None]+(whi-wlo)[:, :, None]*z
                        weights = (Wv*uw)[:, :, None]*(whi-wlo)[:, :, None]*wz
                        VB, UB = np.broadcast_to(V[:, :, None], W.shape), np.broadcast_to(U[:, :, None], W.shape)
                        if np.any(weights):
                            M += self.m2(VB, UB, W, weights, mode)
        return (M+M.T)/2, (G+G.T)/2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--order', type=int, default=20)
    ap.add_argument('--degree', type=int, default=4)
    args = ap.parse_args()
    started = time.monotonic()
    builder = FormBuilder(27/25, args.degree, args.order)
    M, G = builder.forms()
    count = len(BASE_GROUPS)*(args.degree+1)
    result = {
        'status': 'fixed arithmetic two-large-prime interaction; floating integration, not interval certified',
        'ell_exact': '27/25', 'threshold_exact': '1/3', 'degree': args.degree, 'order': args.order,
        'mark': 'D_L(n)=choose(count of DISTINCT prime divisors p>L^(1/3),2), n<=L',
        'features': builder.features,
        'radial_basis': 'Legendre_d(2v-1) unmarked; Legendre_d(6v-5) D marked',
        'base': solve(M, G, np.arange(count)), 'enlarged': solve(M, G),
        'seconds': time.monotonic()-started,
        'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'prior_source_sha256': PRIOR_SHA,
    }
    prefix = HERE/f'two_large_prime_d{args.degree}_q{args.order}'
    prefix.with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    np.savez_compressed(prefix.with_suffix('.npz'), M=M, G=G)
    print(json.dumps({key: {k: v for k, v in result[key].items() if k not in ('coefficients', 'gram_scaled_eigenvalues')} for key in ('base', 'enlarged')}, indent=2))
    print('seconds', result['seconds'], flush=True)


if __name__ == '__main__':
    main()
