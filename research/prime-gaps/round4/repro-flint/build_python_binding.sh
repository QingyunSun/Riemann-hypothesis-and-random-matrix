#!/usr/bin/env bash
# Isolated binding build for the already-tested prefix. No system FLINT replacement.
set -euo pipefail
if [[ $# != 2 ]]; then
  echo 'Usage: build_python_binding.sh BUILD_DIRECTORY PYTHON_EXECUTABLE' >&2
  exit 2
fi
build_root=$1
python_executable=$2
install_prefix="$build_root/prefix"
test -f "$install_prefix/lib/pkgconfig/flint.pc"
if [[ -e "$build_root/venv" ]]; then
  echo 'Refusing to replace an existing virtual environment.' >&2
  exit 2
fi
uv venv --python "$python_executable" "$build_root/venv"
PKG_CONFIG_PATH="$install_prefix/lib/pkgconfig:/opt/homebrew/opt/gmp/lib/pkgconfig:/opt/homebrew/opt/mpfr/lib/pkgconfig" \
  LDFLAGS=-L/opt/homebrew/opt/gmp/lib \
  uv pip install --python "$build_root/venv/bin/python" --no-binary python-flint \
  python-flint==0.9.0 numpy==2.2.6

# Meson embeds the library's absolute install name on this macOS build. Its
# optional add_flint_rpath flag emits a Linux-style linker flag and is omitted.
"$build_root/venv/bin/python" -c 'import flint; print(flint.__version__, flint.__FLINT_VERSION__)'
