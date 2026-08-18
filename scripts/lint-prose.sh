#!/usr/bin/env bash
# Report banned vocabulary and constructions from STYLE.md.
# Exits 1 if anything is found, so it can gate a commit or a build.
set -uo pipefail
cd "$(dirname "$0")/.."

WORDS='delve|crucial|journey|unlock|robust|seamless|powerful|game-changer|deep dive|dive in|at its core|it'"'"'s worth noting|obviously|of course'
PHRASES='harness the|leverage the|not just|not only.*but also'

status=0
files=$(git ls-files '*.qmd' '*.md' 2>/dev/null | grep -v -e '^STYLE.md$' -e '^notes/')

for pattern in "$WORDS" "$PHRASES"; do
  # -n line numbers, -I skip binaries, -E extended regex, -i case-insensitive
  if hits=$(grep -nIEi -- "$pattern" $files 2>/dev/null); then
    echo "$hits"
    status=1
  fi
done

# Em dashes get their own pass so the message can explain itself.
if hits=$(grep -nI -- '—' $files 2>/dev/null); then
  echo "$hits" | sed 's/$/   <- em dash, prefer a full stop or comma/'
  status=1
fi

[ $status -eq 0 ] && echo "Prose clean."
exit $status
