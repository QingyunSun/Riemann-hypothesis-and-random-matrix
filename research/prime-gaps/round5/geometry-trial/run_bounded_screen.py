#!/usr/bin/env python3
"""Reproduce only the declared ten-point screen and two-point refinement."""
import argparse
import os
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
SCREEN=("baseline","r272_min","r272_original","r274_original","r274_max",
        "r275_max","r276_min","r276_max","r278_min","r278_max")
REFINE=("r274_max","r275_max")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--refine",action="store_true")
    args=ap.parse_args();env=os.environ.copy();env["OPENBLAS_NUM_THREADS"]="1"
    for tag in REFINE if args.refine else SCREEN:
        N=98304 if args.refine else 16384
        with (HERE/f"{tag}_n{N}.log").open("w") as log:
            subprocess.run([sys.executable,str(HERE/"optimize_cap.py"),"--config",
                            str(HERE/f"{tag}.config.json"),"--intervals",str(N),"--validate"],
                           cwd=HERE,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
if __name__=="__main__":main()
