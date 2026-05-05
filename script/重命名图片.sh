#!/usr/bin/env bash

set -euo pipefail

cd "/Users/a86198/Desktop/质量管理/notes/源哥"

shopt -s nullglob
files=( *.JPG )

i=1
for f in "${files[@]}"; do
	tmp=$(printf "__tmp__%02d.JPG" "$i")
	mv "$f" "$tmp"
	((i++))
done

i=1
for f in __tmp__*.JPG; do
	final=$(printf "%02d.JPG" "$i")
	mv "$f" "$final"
	((i++))
done

ls -1