#!/usr/bin/env python3
"""Read-only post-audit of computed radial-residual outputs; no new integrations."""
from pathlib import Path
import hashlib,json,os
import numpy as np
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
records=[]
for source in sorted(HERE.glob('radial_residual_n*.json')):
    d=json.loads(source.read_text())
    witness=source.with_suffix('.npz')
    if not witness.exists():witness=source.with_name(source.stem+'_compact.npz')
    a=np.load(witness)
    trial_root=Path(os.environ.get("PRIME186_TRIAL_ROOT",str(BASE/"research-round4/k39-trial")))
    old=trial_root/f"ritz_k39_n{d['N']}"
    meta=json.loads(old.with_suffix('.json').read_text());mat=np.load(old.with_suffix('.npz'))
    c=np.asarray(meta['trials'][-1]['coefficients_float']);G,B=mat['gram'],mat['numerator']
    normf=float(c@G@c);lam=float(c@B@c/normf)
    gamma=d['outside_77_norm_squared'];b=float(a['K'][-1,-1])
    beta=d['coupling_f_Tz']/(normf*gamma)**.5
    pair=np.array([[lam,beta],[beta,b]])
    top=float(np.linalg.eigvalsh(pair)[-1]);e=a['projected']-lam*c
    defect_sq=float(e@G@e)
    # Do not call a negative rounded quadratic form a norm.
    record={'source':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'N':d['N'],'tilt':d['tilt'],'density_cutoff':d['density_cutoff'],
        'norm_f_squared':normf,'two_by_two_matrix':pair.tolist(),
        'two_by_two_largest_eigenvalue':top,'two_by_two_gain':top-lam,
        'full_78_largest_eigenvalue':d['new_78_matrix_quotient'],
        'extra_gain_from_full_78_reoptimization':d['new_78_matrix_quotient']-top,
        'ritz_defect_squared_computed':defect_sq,
        'ritz_defect_norm_computed':defect_sq**.5 if defect_sq>=0 else None,
        'compressed_norm_squared':d['radial_norm_squared'],
        'orthogonal_norm_squared':gamma,
        'coupling_squared':beta*beta,
        'two_by_two_crossing_coupling_squared_threshold':(1-lam)*(1-b),
        'fraction_of_crossing_coupling_squared':beta*beta/((1-lam)*(1-b)),
        'normalized_new_vector_mass_check':float((a['newc']@G@a['newc'])+
                2*d['new_vector_beta']*a['newc']@a['mass_cross']+
                d['new_vector_beta']**2*d['radial_norm_squared'])}
    records.append(record)
(HERE/'projection_audit.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
