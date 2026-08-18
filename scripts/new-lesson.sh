#!/usr/bin/env bash
# Lessons are generated from the syllabus, not created by hand. Add the lesson
# to curriculum/music_theory_through_sonic_pi.html, then run the generator.
set -euo pipefail
cd "$(dirname "$0")/.."
echo "Add the lesson to curriculum/music_theory_through_sonic_pi.html, then:"
echo
echo "    python3 scripts/gen_book.py"
echo
echo "Existing lessons are never overwritten. Only missing files are created."
exec python3 scripts/gen_book.py --dry-run
