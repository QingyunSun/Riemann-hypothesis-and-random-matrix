"""Six independent saved-array transpose checks; no new frequency or prime work."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np

HERE=Path(__file__).resolve().parent
AUTHOR=HERE.parent/'actual-prime-matrix-test'


def info(path):
    b=path.read_bytes()
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}


receipt=json.loads((AUTHOR/'FOLLOWUP_TRANSPOSE_RECEIPT.json').read_text())
pins=[]
for kind in ['new_files','unchanged_source_files']:
    for entry in receipt[kind]:
        got=info(AUTHOR/entry['path'])
        assert all(got[k]==entry[k] for k in ['bytes','sha256'])
        pins.append({'kind':kind,'path':entry['path'],**got,'matches':True})
reports=json.loads((AUTHOR/'transpose_pairing_results.json').read_text())
cases=[]
for report in reports['cases']:
    X=report['X']
    raw=np.load(AUTHOR/f'arrays/case_{X}.npz')
    saved=np.load(AUTHOR/f'arrays/transpose_pairing_{X}.npz')
    C,rows=raw['C'],raw['row_integers'];n=len(rows)
    ev,V=raw['eigenvalues'],raw['eigenvectors'];op=abs(float(ev[0]))
    evaluations=[]
    for j,t in enumerate(saved['frequencies']):
        # Scalar trigonometry gives an independent phase evaluation route.
        c=np.array([math.cos(float(t)*math.log(int(d))) for d in rows])/math.sqrt(n)
        s=np.array([math.sin(float(t)*math.log(int(d))) for d in rows])/math.sqrt(n)
        w=c+1j*s
        pair=float(c@C@c-s@C@s)+2j*float(c@C@s)
        coordinates=V.T@w
        # The squares below are deliberately unconjugated, not abs()**2.
        terms=ev*coordinates**2
        spectral=complex(math.fsum(terms.real),math.fsum(terms.imag))
        original=complex(saved['transpose_pairings'][j])
        assert abs(pair-original)<2e-8
        assert abs(spectral-original)<2e-8
        assert abs(pair)<=op*(1+1e-12)
        features=c[:,None] if t==0 else np.column_stack((c,s))
        Q,_=np.linalg.qr(features,mode='reduced')
        compressed=Q.T@C@Q
        compressed_eigs=np.linalg.eigvalsh(compressed)
        old=report['evaluations'][j]
        assert np.max(abs(compressed_eigs-np.array(old['compression_eigenvalues'])))<2e-8
        qcoords=Q.T@w
        compression_pair=qcoords.T@compressed@qcoords
        assert abs(compression_pair-pair)<2e-9
        hermitian=np.vdot(w,C@w)
        evaluations.append({'frequency':float(t),'independent_pair_real':pair.real,
            'independent_pair_imaginary':pair.imag,'absolute_over_op':abs(pair)/op,
            'scalar_phase_pair_error':abs(pair-original),
            'all_eigenmodes_unconjugated_expansion_error':abs(spectral-original),
            'plane_compression_pair_error':abs(compression_pair-pair),
            'compression_eigenvalues':compressed_eigs.tolist(),
            'compression_norm_over_op':float(np.max(abs(compressed_eigs))/op),
            'hermitian_control_real':float(hermitian.real),
            'transpose_minus_Hermitian_absolute':abs(pair-hermitian),
            'stored_vector_scalar_phase_max_difference':float(np.max(abs(w-saved['w_vectors'][:,j])))})
    cases.append({'X':X,'evaluations':evaluations})
out={'status':'PASS','scope':'Exactly six previously selected frequencies. Floating diagnostics, no interval enclosure or asymptotic estimate. Main input bytes unchanged.',
     'pins':pins,'cases':cases}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
(HERE/'independent_transpose_checks.json').write_text(s)
print(s,end='')
