#!/usr/bin/env python3
"""Exact-parameter and actual-grid nesting checks for the bounded geometry screen."""
from pathlib import Path
from fractions import Fraction as Q
import json
import numpy as np
from cap_trial import geometry,Trial

records=[]
for path in sorted(Path(__file__).parent.glob("*.config.json")):
    config=json.loads(path.read_text()); g=geometry(config)
    assert g["rho_star"]*(g["S"]+g["T1"])==Q(".5252997")
    assert g["S"]+g["T0"]==Q("1.997")
    records_at_grids=[]
    for N in (16384,98304):
        trial=Trial(39,N,20,config=config)
        for cap in trial.caps:
            masks={}
            for role in ("base","enlarged","full"):
                mask=np.zeros(trial.n,dtype=bool)
                for c,radial in trial.shells[role]:
                    if cap<=c: mask |= radial
                masks[role]=mask
            assert not np.any(masks["base"] & ~masks["enlarged"])
            assert not np.any(masks["enlarged"] & ~masks["full"])
        shell_record={}
        for role,rows in trial.shells.items():
            shell_record[role]=[]
            for cap,mask in rows:
                idx=np.flatnonzero(mask)
                shell_record[role].append({"cap_index":cap,"nonempty":bool(len(idx)),
                    "radial_integer_min":int(idx[0]) if len(idx) else None,
                    "radial_integer_max":int(idx[-1]) if len(idx) else None})
        records_at_grids.append({"N":N,"shells":shell_record,"nested":True})
    records.append({"config":config,"exact_geometry":g["metadata"],"grids":records_at_grids})
Path(__file__).with_name("geometry_checks.json").write_text(json.dumps(records,indent=2)+"\n")
print("PASS: fixed sums, exact plateau frontier and 20 grid nestings")
