#!/usr/bin/env bash
# Two tiers of checking for the extracted snippets.
#
#   tier 1  ruby -c        syntax only, needs nothing installed, runs in CI
#   tier 2  sonic-pi-tool  catches undefined methods and bad arguments,
#                          needs Sonic Pi running on this machine
#
# Usage: scripts/check-code.sh [--deep]
set -uo pipefail
cd "$(dirname "$0")/.."

[ -d code ] || scripts/extract-code.sh >/dev/null

fail=0
total=0

for f in code/*/*.rb; do
  [ -e "$f" ] || continue
  total=$((total + 1))
  if ! out=$(ruby -c "$f" 2>&1); then
    echo "SYNTAX  $f"
    echo "$out" | sed 's/^/        /'
    fail=$((fail + 1))
  fi
done

echo "Checked $total snippets, $fail syntax failures."

if [ "${1:-}" = "--deep" ]; then
  if ! command -v sonic-pi-tool >/dev/null; then
    echo "sonic-pi-tool not installed; skipping evaluation pass."
    exit $((fail > 0))
  fi
  echo "Evaluating against a running Sonic Pi. Turn your volume down."
  for f in code/*/*.rb; do
    sonic-pi-tool eval-file "$f" || { echo "EVAL    $f"; fail=$((fail + 1)); }
    sleep 1
  done
  sonic-pi-tool stop || true
fi

exit $((fail > 0))
