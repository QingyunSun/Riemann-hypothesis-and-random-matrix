"""Reproduce the round-two full arithmetic operator values without rewriting round one."""
import argparse,json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parents[2]/'research/residual-gram'))
from arithmetic_operator import solve
p=argparse.ArgumentParser();p.add_argument('--save-largest',action='store_true');p.add_argument('--lengths',default='3000000,10000000');a=p.parse_args();rows=[]
for L in map(int,a.lengths.split(',')):
    row,x=solve(L);rows.append(row);print(json.dumps(row),flush=True)
if a.save_largest:np.savez_compressed(Path(__file__).with_name('extended-arithmetic-eigenvector.npz'),L=L,theta=1.,x=x)
Path(__file__).with_name('extended-arithmetic-results.json').write_text(json.dumps(rows,indent=2))
