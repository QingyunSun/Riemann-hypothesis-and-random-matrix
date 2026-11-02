"""Exact finite Boolean encoding of minimal admissible tuple diameter.
No floating-point arithmetic. z3 unsat establishes the encoded finite question;
we save SMT-LIB and a proof term, but do not claim an independent proof replay.
"""
from pathlib import Path
import time,json,z3
BASE=Path(__file__).parent
z3.set_param(proof=True)
def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
def run(k,d):
    t=time.monotonic();s=z3.Solver();s.set(timeout=240000)
    n=d//2+1;x=[z3.Bool(f'x_{i}') for i in range(n)]
    s.add(z3.PbGe([(v,1) for v in x],k))
    for p in primes(k):
        if p==2: continue
        y=[z3.Bool(f'omit_{p}_{r}') for r in range(p)]
        s.add(z3.PbEq([(v,1) for v in y],1))
        for i in range(n): s.add(z3.Or(z3.Not(x[i]),z3.Not(y[i%p])))
    tag=f'tuple_k{k}_d{d}'
    (BASE/f'{tag}.smt2').write_text(s.to_smt2())
    ans=s.check();out={'k':k,'diameter':d,'status':str(ans),'seconds':time.monotonic()-t,'z3_version':z3.get_version_string()}
    if ans==z3.unsat:
        p=s.proof().sexpr();(BASE/f'{tag}.proof.sexp').write_text(p);out['proof_chars']=len(p)
    elif ans==z3.sat:
        model=s.model();a=[2*i for i,v in enumerate(x) if z3.is_true(model.eval(v))];out['tuple']=a
    else:out['reason']=s.reason_unknown()
    print(json.dumps(out),flush=True);(BASE/f'{tag}.result.json').write_text(json.dumps(out,indent=2))
for k,d in [(40,184),(39,180)]:run(k,d)
