"""Six requested transpose pairings on frozen arrays; no search or prime work."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np

HERE = Path(__file__).resolve().parent


def complex_json(z):
    return {'real':float(np.real(z)), 'imaginary':float(np.imag(z)), 'absolute':float(abs(z))}


def main():
    selection_file = HERE/'mellin_results.json'
    selected = json.loads(selection_file.read_text())
    result = {'scope':'Post-initial-data selected frequencies and t=0 only; complex transpose w^T C w, never w* C w. Existing frozen matrices, no new grid or primes.', 'selection_source_sha256':hashlib.sha256(selection_file.read_bytes()).hexdigest(), 'cases':[]}
    for old in selected['cases']:
        X = old['X']
        source = HERE/'arrays'/f'case_{X}.npz'
        assert hashlib.sha256(source.read_bytes()).hexdigest()==old['source_array_sha256']
        data = np.load(source)
        C, rows = data['C'], data['row_integers']
        n = len(rows)
        sigma = float(abs(data['eigenvalues'][0]))
        products, f_values = data['unique_products'], data['f_values']
        counts = np.bincount(data['inverse_product_index'],minlength=len(products))
        frequencies = np.array([0.,old['winning_frequency']])
        vectors, pairings, compressions, checks = [], [], [], []
        for t in frequencies:
            w = np.exp(1j*t*np.log(rows))/math.sqrt(n)
            pairing = w @ (C @ w)  # Deliberately no conjugation.
            assert abs(float(np.vdot(w,w).real)-1)<1e-13
            c, s = w.real, w.imag
            expanded = c@C@c-s@C@s+2j*(c@C@s)
            grouped = np.sum(counts*f_values*np.exp(1j*t*np.log(products)))/n
            center = float(rows[n//2])
            rotated = np.exp(1j*t*np.log(rows/center))/math.sqrt(n)
            restored = np.exp(2j*t*math.log(center))*(rotated@(C@rotated))
            assert abs(pairing)<=sigma*(1+1e-12)
            assert abs(pairing-expanded)<1e-11*max(1,sigma)
            # Distinct equivalent phase reductions need not be bit-identical.
            assert abs(pairing-grouped)<1e-9*max(1,sigma)
            assert abs(pairing-restored)<1e-9*max(1,sigma)
            features = c[:,None] if t==0 else np.column_stack((c,s))
            Q,_ = np.linalg.qr(features,mode='reduced')
            compressed = Q.T@C@Q
            compressed_values = np.linalg.eigvalsh(compressed)
            record = {'frequency':float(t),'frequency_over_T':float(t/math.sqrt(X)),'transpose_pairing':complex_json(pairing),'absolute_over_operator_norm':float(abs(pairing)/sigma),'cos_sin_expansion':complex_json(expanded),'checks':{'unit_norm_error':abs(float(np.vdot(w,w).real)-1),'cos_sin_absolute_error':float(abs(pairing-expanded)),'grouped_product_absolute_error':float(abs(pairing-grouped)),'centered_phase_absolute_error':float(abs(pairing-restored))},'orthonormal_compression':compressed.tolist(),'compression_eigenvalues':compressed_values.tolist(),'compression_op_over_full_op':float(np.max(np.abs(compressed_values))/sigma)}
            pairings.append(pairing);vectors.append(w);compressions.append(compressed);checks.append(record)
        np.savez_compressed(HERE/'arrays'/f'transpose_pairing_{X}.npz',frequencies=frequencies,w_vectors=np.column_stack(vectors),transpose_pairings=np.array(pairings),compression_zero=compressions[0],compression_selected=compressions[1])
        case = {'X':X,'dimension':n,'operator_norm':sigma,'array_source_sha256':old['source_array_sha256'],'selected_by':'Prior maximum top-vector Mellin-plane projection; post-initial-data, not selected to maximize this transpose pairing.','prior_maximum_squared_plane_projection':old['maximum_squared_projection'],'evaluations':checks}
        result['cases'].append(case)
        print(json.dumps(case,sort_keys=True),flush=True)
    (HERE/'transpose_pairing_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
