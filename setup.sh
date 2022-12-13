#!/bin/zsh

set -x
src_dir="$(dirname $0)"
dst_dir="${src_dir}/$1"
mkdir "${dst_dir}"
cp "${src_dir}/template.py" "${dst_dir}/problem.py"
touch "${dst_dir}/big.in"
touch "${dst_dir}/tiny.in"
