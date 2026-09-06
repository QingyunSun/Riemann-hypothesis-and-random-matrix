#!/usr/bin/env python3
"""Export exact witness arrays, omitting only regenerable radial mass cache D."""
from pathlib import Path
import hashlib,json
import numpy as np
HERE=Path(__file__).resolve().parent
records=[]
for full in sorted(HERE.glob('radial_residual_n*.npz')):
    if full.stem.endswith('_compact'):continue
    data=np.load(full)
    arrays={key:data[key] for key in data.files if key!='D'}
    compact=full.with_name(full.stem+'_compact.npz')
    np.savez_compressed(compact,**arrays)
    check=np.load(compact)
    assert set(check.files)==set(arrays)
    for key in arrays:
        assert check[key].dtype==arrays[key].dtype
        assert check[key].shape==arrays[key].shape
        assert check[key].tobytes()==arrays[key].tobytes()
    records.append({'full_file':full.name,'full_sha256':hashlib.sha256(full.read_bytes()).hexdigest(),
      'full_bytes':full.stat().st_size,'compact_file':compact.name,
      'compact_sha256':hashlib.sha256(compact.read_bytes()).hexdigest(),
      'compact_bytes':compact.stat().st_size,'omitted_arrays':['D'],
      'omitted_D_shape':list(data['D'].shape),'omitted_D_dtype':str(data['D'].dtype),
      'omitted_D_sha256_C_bytes':hashlib.sha256(data['D'].tobytes()).hexdigest(),
      'retained_array_sha256_C_bytes':{key:hashlib.sha256(a.tobytes()).hexdigest() for key,a in arrays.items()},
      'verification':'all retained array shapes, dtypes and raw bytes identical',
      'rebuild':'run radial_residual.py with the N, tilt and density cutoff of the matching JSON; radial_mass reconstructs D'})
(HERE/'compaction_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps([{'full_bytes':r['full_bytes'],'compact_bytes':r['compact_bytes']} for r in records]))
