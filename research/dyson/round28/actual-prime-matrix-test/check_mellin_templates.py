"""One coordinator-requested Mellin grid check of saved R28 arrays only."""
from pathlib import Path
import hashlib
import json
import math
import numpy as np

HERE = Path(__file__).resolve().parent


def main():
    result = {'scope':'Post-initial-result fixed Mellin template grid; existing matrices only. No new prime computation or mode subtraction.','cases':[]}
    for X in (1_000_000,4_000_000,16_000_000):
        source = HERE/'arrays'/f'case_{X}.npz'
        if not source.exists():
            continue
        z = np.load(source)
        rows = z['row_integers']
        n = len(rows)
        u = z['eigenvectors'][:,0]
        left = np.sign(z['eigenvalues'][0])*u
        log_d = np.log(rows.astype(float))
        step = np.diff(log_d)
        nyquist = {'minimum_local':float(np.pi/np.max(step)), 'mean_spacing':float(np.pi/np.mean(step)), 'maximum_local':float(np.pi/np.min(step))}
        frequencies = np.linspace(0,nyquist['maximum_local'],4*n)
        coordinate = np.log(rows/float(rows[n//2]))
        cosine = np.cos(coordinate[:,None]*frequencies)
        sine = np.sin(coordinate[:,None]*frequencies)
        cc = np.sum(cosine*cosine,axis=0)
        ss = np.sum(sine*sine,axis=0)
        cs = np.sum(cosine*sine,axis=0)
        determinant = cc*ss-cs*cs
        trace = cc+ss
        minimum_eigenvalue = (trace-np.sqrt((cc-ss)**2+4*cs**2))/2
        assert np.all(minimum_eigenvalue[1:]>1e-9)
        uc, us = u@cosine, u@sine
        lc, ls = left@cosine, left@sine
        projection = np.empty(len(frequencies)); projection[0]=uc[0]**2/cc[0]
        projection[1:] = (ss[1:]*uc[1:]**2-2*cs[1:]*uc[1:]*us[1:]+cc[1:]*us[1:]**2)/determinant[1:]
        left_projection = np.empty_like(projection);left_projection[0]=lc[0]**2/cc[0]
        left_projection[1:] = (ss[1:]*lc[1:]**2-2*cs[1:]*lc[1:]*ls[1:]+cc[1:]*ls[1:]**2)/determinant[1:]
        assert np.allclose(projection,left_projection,atol=1e-14,rtol=1e-14)
        assert np.min(projection)>-1e-12 and np.max(projection)<1+1e-12
        best = int(np.argmax(projection))
        basis = cosine[:,best,None] if best==0 else np.column_stack((cosine[:,best],sine[:,best]))
        q,_ = np.linalg.qr(basis,mode='reduced')
        qr_value = float(np.linalg.norm(q.T@u)**2)
        assert abs(qr_value-projection[best])<1e-12
        order = np.argsort(-projection,kind='stable')[:10]
        case = {'X':X,'dimension':n,'grid_count':len(frequencies),'frequency_step':float(frequencies[1]),'nyquist_conventions':nyquist,'maximum_squared_projection':float(projection[best]),'winning_frequency':float(frequencies[best]),'winning_frequency_over_T':float(frequencies[best]/math.sqrt(X)),'winning_index':best,'winning_QR_projection':qr_value,'minimum_positive_frequency_Gram_eigenvalue':float(np.min(minimum_eigenvalue[1:])),'left_right_max_difference':float(np.max(np.abs(projection-left_projection))),'top_ten_grid_points':[{'index':int(i),'frequency':float(frequencies[i]),'squared_projection':float(projection[i])} for i in order],'source_array_sha256':hashlib.sha256(source.read_bytes()).hexdigest()}
        np.savez_compressed(HERE/'arrays'/f'mellin_{X}.npz',frequencies=frequencies,right_projection=projection,left_projection=left_projection,gram_cc=cc,gram_ss=ss,gram_cs=cs,gram_minimum_eigenvalue=minimum_eigenvalue,winning_basis=q,row_log_coordinate=coordinate)
        result['cases'].append(case)
        print(json.dumps(case,sort_keys=True),flush=True)
    (HERE/'mellin_results.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':
    main()
