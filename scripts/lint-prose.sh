#!/usr/bin/env bash
# Report banned vocabulary, constructions, and voice slips from STYLE.md.
# Patterns live in scripts/prose-banned.txt, one extended regex per line.
# Exits 1 if anything is found, so it can gate a commit or a build.
set -uo pipefail
cd "$(dirname "$0")/.."

PATTERNS=scripts/prose-banned.txt
status=0

# STYLE.md quotes the banned words in order to ban them, and the field notes
# are private working text, so neither is linted.
# git ls-files still lists files deleted but not yet staged, so keep only the
# ones on disk. Untracked new lessons get linted too.
files=$({ git ls-files '*.qmd' '*.md'; git ls-files -o --exclude-standard '*.qmd' '*.md'; } 2>/dev/null \
        | sort -u \
        | grep -v -e '^STYLE.md$' -e '^notes/' -e '^scripts/prose-banned.txt$' -e '^graphify-out/' \
        | while IFS= read -r f; do [ -f "$f" ] && printf '%s\n' "$f"; done)

[ -n "$files" ] || { echo "No tracked prose files."; exit 0; }

# Strip comments and blank lines before handing the list to grep.
active=$(grep -vE '^\s*(#|$)' "$PATTERNS")

if hits=$(printf '%s\n' "$active" | grep -nIEi -f /dev/stdin -- $files); then
  echo "$hits"
  status=1
fi

# Em dashes get their own pass so the message can explain itself.
if hits=$(grep -nI -- '—' $files); then
  echo "$hits" | sed 's/$/   <- em dash, prefer a full stop or comma/'
  status=1
fi

if [ $status -eq 0 ]; then
  echo "Prose clean: $(printf '%s\n' $files | wc -l | tr -d ' ') files, $(printf '%s\n' "$active" | wc -l | tr -d ' ') patterns."
fi
exit $status
