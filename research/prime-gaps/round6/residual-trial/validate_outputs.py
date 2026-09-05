#!/usr/bin/env python3
"""Numerical structural regressions, not rigorous error enclosures."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
cases=[]
for path in sorted(HERE.glob('radial_residual_n*.json')):
    d=json.loads(path.read_text())
    assert 0<d['outside_77_norm_squared']<=d['radial_norm_squared']*(1+1e-8)
    assert abs(d['coupling_identity_relative_error'])<1e-6
    assert abs(d['mixed_adjoint_relative_check'])<1e-6
    assert abs(d['matrix_direct_difference'])<1e-8
    assert d['new_78_matrix_quotient']>d['original_77_quotient']
    cases.append({'file':path.name,'coupling_identity_relative_error':d['coupling_identity_relative_error'],
                  'matrix_direct_difference':d['matrix_direct_difference'],'passed':True})
for d in json.loads((HERE/'projection_audit.json').read_text()):
    assert d['two_by_two_gain']>0
    assert d['extra_gain_from_full_78_reoptimization']>=-1e-8
    assert abs(d['normalized_new_vector_mass_check']-1)<1e-6
fine=[json.loads(p.read_text()) for p in HERE.glob('radial_residual_n98304*.json')]
a=next(d for d in fine if d['tilt']==20 and d['density_cutoff']==1e-9)
b=next(d for d in fine if d['tilt']==25 and d['density_cutoff']==1e-9)
assert abs(a['new_78_matrix_quotient']-b['new_78_matrix_quotient'])<1e-9
out={'status':'numerical structural regressions pass; not interval certificates','cases':cases,
     'tilt_matrix_difference':a['new_78_matrix_quotient']-b['new_78_matrix_quotient']}
(HERE/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'])
