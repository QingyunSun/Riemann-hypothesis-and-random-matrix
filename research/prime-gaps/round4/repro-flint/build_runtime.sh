#!/usr/bin/env bash
# Build FLINT 3.6.0 with upstream's signed FFT fix in an isolated prefix.
# Prerequisites on this host: GMP, MPFR, autoconf, automake, libtool, clang.
set -euo pipefail

if [[ $# != 2 ]]; then
  echo 'Usage: build_runtime.sh DOWNLOAD_DIRECTORY BUILD_DIRECTORY' >&2
  exit 2
fi
downloads=$1
build_root=$2
source_dir="$build_root/flint-3.6.0"
install_prefix="$build_root/prefix"
mkdir -p "$build_root"

python3 - "$downloads" <<'PY'
from hashlib import sha256
from pathlib import Path
import sys
p = Path(sys.argv[1])
expected = {
    'flint-v3.6.0.tar.gz': '4307a504622702bf0be6d8969791f7d7ff378645cf2ae3bb5a7a2b56653d97f1',
    'flint-7ad753d.patch': '333788fe3d7fe1c24ca10e5ef33f492eae68de6202568e75e18e1bcd7bfb71ff',
}
for name, digest in expected.items():
    actual = sha256((p / name).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit(f'Hash mismatch for {name}: {actual}')
    print(f'Verified {name}: {actual}', flush=True)
PY

if [[ -e "$source_dir" ]]; then
  echo "Refusing to overwrite existing source: $source_dir" >&2
  exit 2
fi
tar -xzf "$downloads/flint-v3.6.0.tar.gz" -C "$build_root"
cd "$source_dir"
patch -p1 < "$downloads/flint-7ad753d.patch"
./bootstrap.sh
./configure --prefix="$install_prefix" --with-gmp=/opt/homebrew/opt/gmp \
  --with-mpfr=/opt/homebrew/opt/mpfr --disable-static --enable-assert
make -j4
make -j4 check MOD='fmpz_vec fmpz_poly arb arb_poly'
make install
echo "Built and tested corrected library at $install_prefix"
