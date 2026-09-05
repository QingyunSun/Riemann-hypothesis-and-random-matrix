#!/usr/bin/env python3
"""Exact final scalar replay: one new rectangle + printed original endpoints."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parent
certificate=OUT/'alpha_rectangle_certificate.json'
d=json.loads(certificate.read_text())
assert d['status']=='certified positive alpha lower endpoint' and d['signed_regression_passed']
alpha=F(d['alpha_rectangle_normalized_interval']['lower'])
rho=F(2624989,10**7);bh=F(-843183,10**9);ca=1-4*rho*abs(bh)
Ilow=F(23685317816,10**24);Ihigh=F(23685317890,10**24);Jlow=F(90248755123,10**24)
loss=Ilow*F(696075110,10**12)
original=rho*(Jlow-loss)/Ihigh-1
credit=ca*alpha/Ihigh
new=original+credit
assert credit==F(d['credit_over_published_I_upper_lower'])
assert alpha>0 and credit>F(15058,10**10) and new>F(248662,10**10)
def record(v):return {'exact':str(v),'decimal_diagnostic':float(v)}
result={'status':'exact scalar replay using new outward alpha and source-inherited original bounds',
        'rectangle_certificate_sha256':hashlib.sha256(certificate.read_bytes()).hexdigest(),
        'old_margin_lower':record(original),'new_credit_lower':record(credit),'new_margin_lower':record(new),
        'relative_margin_increase_lower':record(credit/original),
        'scope':'Original I,J,97 loss component endpoints are printed source bounds, not freshly re-certified in this task. k40/diameter186 unchanged.'}
(OUT/'alpha_credit_margin_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
