#!/usr/bin/env python3
"""Three finite actual-prime diagnostics; analytic errors are not float enclosures.

The fixed T values are 100, 300, 1000. Every prime power has Lambda(p**k)=log(p).
The main output uses positive interval-event geometry and exact seed definitions.
Only --output-dir varies. No zeta zeros or asymptotic hypothesis is evaluated.
"""
from __future__ import annotations
import argparse
import csv
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import mpmath as mp
import numpy as np

T_VALUES = (100, 300, 1000)
EPSILON = Fraction(1, 4)
ALPHA_BINS = 16384
SIMPSON_FINE = 4096
SIMPSON_CONTROL = 2048
SERIES_DEGREE = 12


def file_record(path: Path) -> dict:
    raw = path.read_bytes()
    return {'name': path.name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def seed(x: np.ndarray) -> np.ndarray:
    y = 1 - 4*x*x
    result = np.zeros_like(x)
    mask = y > 0
    result[mask] = np.exp(-1/y[mask])
    return result


def simpson_weights(n: int) -> np.ndarray:
    assert n % 2 == 0
    w = np.full(n+1, 2.0)
    w[1:n:2] = 4.0
    w[0] = w[-1] = 1.0
    return w / (3*n)


def seed_table(n: int, v: np.ndarray) -> tuple[np.ndarray, float, float]:
    z = np.linspace(0, 1, n+1)
    w = simpson_weights(n)
    f = seed(z-.5)
    integral = float(w @ f)
    s2 = float(w @ (f*f))
    result = np.empty_like(v)
    for left in range(0, len(v), 128):
        values = v[left:left+128]
        length = 1-values
        x = values[:,None]-.5+length[:,None]*z[None,:]
        numerator = length*((seed(x)*seed(x-values[:,None])) @ w)
        result[left:left+128] = numerator/s2
    return result, integral, s2


def analytic_constants() -> dict:
    # f^(j)(x)=2^j exp(-1/y) P_j(2x)/y^(2j), y=1-4x^2.
    # Coefficient l1 norms of P_0,...,P_4, proved in the independent checker.
    norms = [1, 2, 8, 88, 1096]
    c = [Fraction(3,8)]
    for j in range(1,5):
        c.append(Fraction(2**j*norms[j]) * Fraction(3*j,4)**(2*j))
    product4 = sum(Fraction(math.comb(4,j))*c[j]*c[4-j] for j in range(5))
    s2_lower = Fraction(1,54)
    error_s2 = product4 / (180*SIMPSON_FINE**4)
    error_f = c[4] / (180*SIMPSON_FINE**4)
    error_psi = 2*error_s2/(s2_lower-error_s2)
    error_m0 = (Fraction(3,4)*error_f+error_f**2+error_s2)/(s2_lower-error_s2)
    # |(v psi(v))''''| <= (3/8)/(1/54) * (C4+4C3).
    moment4 = Fraction(81,4)*(c[4]+4*c[3])
    j = ALPHA_BINS//2
    error_m1 = error_psi + 2*moment4/(180*j**4)
    return {'derivative_upper_f_0_to_4':[str(x) for x in c],
            'derivative_upper_product4':str(product4), 's2_lower':str(s2_lower),
            'ideal_simpson_error_s2':str(error_s2),
            'ideal_simpson_error_seed_integral':str(error_f),
            'ideal_simpson_error_psi_uniform':str(error_psi),
            'ideal_simpson_error_m0':str(error_m0),
            'ideal_simpson_error_m1':str(error_m1),
            'scope':'Rational analytic truncation bounds for exact evaluations and sums. Machine rounding is not enclosed.'}


def floor_fourth_root(n: int) -> int:
    return math.isqrt(math.isqrt(n))


def ceil_fourth_root(n: int) -> int:
    a=floor_fourth_root(n)
    return a if a**4==n else a+1


def prime_powers(limit: int) -> tuple[np.ndarray,np.ndarray,np.ndarray]:
    sieve = np.ones(limit+1,dtype=bool)
    sieve[:2] = False
    for p in range(2, math.isqrt(limit)+1):
        if sieve[p]:
            sieve[p*p::p] = False
    primes = np.flatnonzero(sieve)
    base = np.zeros(limit+1,dtype=np.int32)
    exponent = np.zeros(limit+1,dtype=np.uint8)
    base[primes] = primes
    exponent[primes] = 1
    for p in primes[primes <= math.isqrt(limit)]:
        power = int(p)*int(p)
        e = 2
        while power <= limit:
            assert base[power] == 0
            base[power] = p
            exponent[power] = e
            power *= int(p)
            e += 1
    positions = np.flatnonzero(base).astype(np.int32)
    return positions,base[positions],exponent[positions]


def kahan_prefix(values: np.ndarray, initial: float) -> np.ndarray:
    result = np.empty(len(values)+1)
    result[0] = initial
    total = initial
    correction = 0.0
    for i,value in enumerate(values):
        adjusted = float(value)-correction
        updated = total+adjusted
        correction = (updated-total)-adjusted
        total = updated
        result[i+1] = total
    return result


def stable_integral(left: np.ndarray,right: np.ndarray,total: np.ndarray,T: int):
    u = (right-left)/left
    assert np.max(u) < .01
    i0 = u/(1+u)
    # I1=int_0^u z/(1+z)^2 dz; I2=int_0^u z^2/(1+z)^2 dz.
    p1 = np.zeros_like(u)
    p2 = np.zeros_like(u)
    for k in range(SERIES_DEGREE,1,-1):
        p1 = p1*u + ((-1)**k)*(k-1)/k
    for k in range(SERIES_DEGREE,2,-1):
        p2 = p2*u + ((-1)**(k+1))*(k-2)/k
    i1 = u*u*p1
    i2 = u*u*u*p2
    b = total-left/T
    centered = b*b/left*i0-2*b/T*i1+left/T**2*i2
    assert np.min(centered) >= 0
    prime_square = total*total/left*i0
    mixed = -2*total/T*np.log1p(u)
    mean_square = left/T**2*u
    return centered,prime_square,mixed,mean_square,u


def compute_one(T: int,pp: np.ndarray,bases: np.ndarray,exponents: np.ndarray,
                psi: np.ndarray,delta_psi: float,out: Path) -> dict:
    started = time.perf_counter()
    mp.mp.dps = 80
    low_mp = mp.mpf(T)**mp.mpf('1.75')
    high_mp = mp.mpf(T)**mp.mpf('2.25')
    upper_mp = (1+mp.mpf(1)/T)*high_mp
    low,high = float(low_mp),float(high_mp)
    max_n = floor_fourth_root(T**5*(T+1)**4)
    low_integer = floor_fourth_root(T**7)
    use = (pp > low_integer) & (pp <= max_n)
    positions = pp[use].astype(np.int64)
    base = bases[use]
    logs = np.log(base.astype(float))
    q = (T+1)/T
    initial_cutoff = floor_fourth_root(T**3*(T+1)**4)
    initial = math.fsum(float(v) for v in logs[positions <= initial_cutoff])
    # The event order is exact integer arithmetic in y=(T+1)x.
    keys = np.concatenate((positions*T,positions*(T+1)))
    jumps = np.concatenate((logs,-logs))
    lower_key_floor = floor_fourth_root((T+1)**4*T**7)
    upper_key_strict = ceil_fourth_root((T+1)**4*T**9)-1
    keep = (keys > lower_key_floor) & (keys <= upper_key_strict)
    keys,jumps = keys[keep],jumps[keep]
    order = np.argsort(keys,kind='stable')
    keys,jumps = keys[order],jumps[order]
    unique,start = np.unique(keys,return_index=True)
    changes = np.add.reduceat(jumps,start)
    event_x = unique/(T+1)
    totals = kahan_prefix(changes,initial)
    alpha = np.linspace(1.75,2.25,ALPHA_BINS+1)
    boundaries = np.exp(alpha*math.log(T))
    boundaries[0],boundaries[-1] = low,high
    all_points = np.unique(np.concatenate((boundaries,event_x)))
    left,right = all_points[:-1],all_points[1:]
    active_index = np.searchsorted(event_x,left,side='right')
    active_total = totals[active_index]
    centered,prime_sq,mixed,mean_sq,u = stable_integral(left,right,active_total,T)
    scale = T/math.log(T)**2
    bins = np.searchsorted(boundaries,left,side='right')-1
    assert np.min(bins)==0 and np.max(bins)==ALPHA_BINS-1
    mass = np.bincount(bins,weights=scale*centered,minlength=ALPHA_BINS)
    parts = [np.bincount(bins,weights=scale*a,minlength=ALPHA_BINS) for a in (prime_sq,mixed,mean_sq)]
    counts = np.bincount(bins,minlength=ALPHA_BINS)
    # psi is increasing to v=0 and decreasing thereafter; exact endpoint Darboux rule.
    psi_min = np.minimum(psi[:-1],psi[1:])
    psi_max = np.maximum(psi[:-1],psi[1:])
    psi_center = .5*(psi_min+psi_max)
    lower = np.maximum(0,psi_min-delta_psi)
    upper = np.minimum(1,psi_max+delta_psi)
    approximate = math.fsum(float(v) for v in mass*psi_center)
    low_value = math.fsum(float(v) for v in mass*lower)
    high_value = math.fsum(float(v) for v in mass*upper)
    dar_low = math.fsum(float(v) for v in mass*psi_min)
    dar_high = math.fsum(float(v) for v in mass*psi_max)
    # Independent direct sums on a fixed set of 33 actual event cells.
    sample_indices = np.linspace(0,len(left)-1,33,dtype=np.int64)
    checks=[]
    for j in sample_indices:
        mid=(left[j]+right[j])/2
        mask=(positions>mid)&(positions<=q*mid)
        direct=math.fsum(math.log(int(p)) for p in base[mask])
        checks.append({'cell':int(j),'x_mid':mid,'event_total':float(active_total[j]),
                       'direct_fsum':direct,'absolute_difference':abs(float(active_total[j])-direct)})
    assert max(x['absolute_difference'] for x in checks)<1e-8
    raw_recombination = math.fsum(float(v) for v in parts[0])+math.fsum(float(v) for v in parts[1])+math.fsum(float(v) for v in parts[2])
    unweighted=math.fsum(float(v) for v in mass)
    # Alternating-series remainders satisfy |R1|,|R2| <= u^13 for u<.01.
    # Bound the exact event total by the number of possible integers times log(max_n).
    high_integer = ceil_fourth_root(T**9)
    b_max = (Fraction(high_integer,T)+1)*16+Fraction(high_integer,T)
    # log(T)<7, exp(7/32768)-1<7/32761; log(max_n)<16.
    cell_bound = 2*(max_n-low_integer)+ALPHA_BINS
    series_error = cell_bound*T*(2*b_max/T+Fraction(high_integer,T*T))*Fraction(7,32761)**(SERIES_DEGREE+1)
    csv_path=out/f'variance_T{T}_bins.csv'
    with csv_path.open('w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['bin','alpha_left','alpha_right','x_left','x_right','event_cells','unweighted_positive_mass',
                         'prime_square_mass','mixed_center_mass','continuous_center_mass','psi_left_simpson','psi_right_simpson',
                         'weight_lower_analytic_only','weight_upper_analytic_only','weighted_midpoint','weighted_lower_analytic_only','weighted_upper_analytic_only'])
        for j in range(ALPHA_BINS):
            writer.writerow([j,alpha[j],alpha[j+1],boundaries[j],boundaries[j+1],int(counts[j]),mass[j],
                             parts[0][j],parts[1][j],parts[2][j],psi[j],psi[j+1],lower[j],upper[j],mass[j]*psi_center[j],mass[j]*lower[j],mass[j]*upper[j]])
    return {'T':T,'epsilon':'1/4','q':f'{T+1}/{T}','alpha_support':['7/4','9/4'],
            'x_low_80digit':str(low_mp),'x_high_80digit':str(high_mp),'integer_prime_power_cutoff':max_n,
            'largest_included_prime_power':int(positions[-1]),'initial_integer_cutoff':initial_cutoff,
            'prime_power_entries_in_supported_interval':len(positions),
            'higher_prime_power_entries_in_supported_interval':int(np.sum(exponents[use]>1)),
            'unique_integer_events':len(unique),'integration_cells':len(left),'alpha_bins':ALPHA_BINS,
            'positive_variance_midpoint_diagnostic':approximate,
            'analytic_only_lower':low_value,'analytic_only_upper':high_value,
            'darboux_only_lower':dar_low,'darboux_only_upper':dar_high,
            'ideal_seed_quadrature_error_allowance':delta_psi*unweighted,
            'unweighted_positive_variance':unweighted,
            'weighted_prime_square':math.fsum(float(v) for v in parts[0]*psi_center),
            'weighted_mixed_center':math.fsum(float(v) for v in parts[1]*psi_center),
            'weighted_continuous_center':math.fsum(float(v) for v in parts[2]*psi_center),
            'raw_component_recombination_disagreement':raw_recombination-unweighted,
            'max_cell_relative_width':float(np.max(u)),
            'ideal_event_series_error_upper_rational':str(series_error),
            'ideal_event_series_error_upper_decimal':float(series_error),
            'direct_active_sum_controls':checks,
            'per_bin_output':file_record(csv_path),
            'scope':'Finite actual-prime diagnostic. Analytic-only bounds exclude all machine rounding; not certified numerical intervals or asymptotic evidence.',
            'elapsed_seconds':time.perf_counter()-started}


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args();out=args.output_dir;out.mkdir(parents=True,exist_ok=True)
    began=time.perf_counter()
    positive_v=np.linspace(0,1,ALPHA_BINS//2+1)
    fine,I,s2=seed_table(SIMPSON_FINE,positive_v)
    control,Ic,s2c=seed_table(SIMPSON_CONTROL,positive_v)
    assert abs(fine[0]-1)<1e-13 and fine[-1]==0
    assert np.max(np.diff(fine))<1e-12
    psi=np.concatenate((fine[:0:-1],fine))
    constants=analytic_constants()
    delta=float(Fraction(constants['ideal_simpson_error_psi_uniform']))
    seed_error=float(np.max(np.abs(fine-control)))
    m0=I*I/s2
    m1=float(2*(simpson_weights(ALPHA_BINS//2) @ (positive_v*fine)))
    moments={'seed':'exp(-1/(1-4x^2)) for |x|<1/2, otherwise 0',
             'autocorrelation':'psi(v)=integral f(x)f(x-v) dx / integral f(x)^2 dx',
             'simpson_fine':SIMPSON_FINE,'simpson_control':SIMPSON_CONTROL,'v_grid_count':len(positive_v),
             'seed_integral':I,'s2':s2,'m0':m0,'m1':m1,
             'AH_limit_A':1+m1/16,'sine_limit':m0/4,
             'simpson_control_max_psi_difference':seed_error,
             'simpson_control_seed_integral_difference':abs(I-Ic),'simpson_control_s2_difference':abs(s2-s2c),
             'analytic_constants':constants,
             'scope':'Finite quadrature diagnostic with separately proved analytic truncation bounds. Rounding not enclosed.'}
    (out/'seed_quadrature.json').write_text(json.dumps(moments,indent=2,sort_keys=True)+'\n')
    with (out/'seed_autocorrelation.csv').open('w',newline='') as f:
        writer=csv.writer(f);writer.writerow(['v','psi_fine','psi_control'])
        writer.writerows(zip(positive_v,fine,control))
    mp.mp.dps=80
    max_T=max(T_VALUES)
    limit=ceil_fourth_root(max_T**5*(max_T+1)**4)
    pp,bases,exponents=prime_powers(limit)
    np.savez_compressed(out/'prime_powers.npz',n=pp,prime_base=bases,exponent=exponents)
    results=[]
    for T in T_VALUES:
        value=compute_one(T,pp,bases,exponents,psi,delta,out)
        value['difference_from_AH_limit']=value['positive_variance_midpoint_diagnostic']-moments['AH_limit_A']
        value['difference_from_sine_limit']=value['positive_variance_midpoint_diagnostic']-moments['sine_limit']
        results.append(value)
        print(json.dumps({k:value[k] for k in ('T','positive_variance_midpoint_diagnostic','analytic_only_lower','analytic_only_upper','difference_from_AH_limit','elapsed_seconds')},sort_keys=True),flush=True)
    output={'status':'PASS','scope':'Three finite actual-prime variances; no RH/AH/asymptotic conclusion and no floating-point enclosure.',
            'T_values':list(T_VALUES),'numpy_version':np.__version__,'python_version':sys.version,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'prime_power_limit':limit,'prime_power_count':len(pp),'higher_power_count':int(np.sum(exponents>1)),
            'prime_power_array_sha256':hashlib.sha256(pp.tobytes()+bases.tobytes()+exponents.tobytes()).hexdigest(),
            'moments':moments,'results':results,'elapsed_seconds':time.perf_counter()-began}
    (out/'actual_prime_variance.json').write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print('PASS: only the three requested T values; full per-bin CSV data and all prime powers retained.',flush=True)

if __name__=='__main__':
    main()
