#!/usr/bin/env python3
"""Small structural checks; does not run the full cap computation."""
import itertools
import json
import math

import numpy as np
from scipy.integrate import quad

from cap_trial import HERE, Trial, block_partitions, dickman_under_three, fiber_splits, read_coefficients

signatures,_=read_coefficients()
weights=np.array([.1,.2,.3,.4])
locations=np.array([.05,.15,.25,.35])
count=3
checks=[]
for signature in signatures:
    exact=np.zeros(count*(len(weights)-1)+1)
    for indices in itertools.product(range(len(weights)),repeat=count):
        points=locations[list(indices)]
        polynomial=math.prod(float(np.sum(points**q)) for q in signature)
        exact[sum(indices)]+=math.prod(weights[list(indices)])*polynomial
    reconstructed=np.zeros_like(exact)
    for blocks,mult in block_partitions(signature):
        conv=np.ones(1)
        for exponent in blocks+(0,)*(count-len(blocks)):
            conv=np.convolve(conv,weights*locations**exponent)
        reconstructed+=mult*math.prod(range(count-len(blocks)+1,count+1))*conv
    assert np.max(abs(exact-reconstructed))<1e-14
    other=np.array([.02,.13,.27])
    inserted=.19
    left=math.prod(float(np.sum(np.append(other,inserted)**q)) for q in signature)
    right=sum(mult*inserted**exponent*math.prod(float(np.sum(other**q)) for q in remaining)
              for remaining,exponent,mult in fiber_splits(signature))
    assert abs(left-right)<1e-14
    checks.append({"signature":list(signature),"moment_max_error":float(np.max(abs(exact-reconstructed))),
                   "fiber_error":abs(left-right)})
expected={
    "outer":[(0,89196,68225),(89197,95598,49152),(95599,98263,46580)],
    "base":[(0,84930,68225),(84931,87194,44781),(87195,89524,35265)],
    "enlarged":[(0,85161,68225),(85162,87249,44976),(87250,89914,35419)],
    "full":[(0,98263,68225)],
}
actual={}
trial=Trial(40,98304,20)
for role,rows in trial.shells.items():
    values=[]
    for cap,mask in rows:
        idx=np.flatnonzero(mask)
        values.append((int(idx[0]),int(idx[-1]),cap))
    assert values==expected[role]
    actual[role]=values
rho3=float(dickman_under_three(np.array([3.0]))[0])
independent=1-math.log(3)+quad(lambda t:math.log(t-1)/t,2,3,epsabs=1e-14)[0]
assert abs(rho3-independent)<1e-14
out={"status":"structural floating checks, not interval certification",
     "moment_and_fiber_checks":checks,"official_k40_shells_exact":actual,
     "dickman_at_3":rho3,"independent_integral_difference":rho3-independent}
(HERE/"structural_check_results.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
