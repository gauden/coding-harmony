#!/usr/bin/env bash
# Convert a Sonic Pi recording into the mp3 the site ships, plus the QR code
# the printed book uses.
#
# Record in Sonic Pi with the Rec button, save as assets/audio/L07-1.wav, then:
#     scripts/make-audio.sh L07-1
# or run with no arguments to process every wav that has no mp3 yet.
set -euo pipefail
cd "$(dirname "$0")/.."

BASE_URL=$(grep '^audio-base-url:' _quarto.yml | sed 's/.*"\(.*\)"/\1/')
AUDIO=assets/audio

convert() {
  local name="$1"
  local wav="$AUDIO/$name.wav"
  [ -f "$wav" ] || { echo "No such recording: $wav" >&2; return 1; }

  # Trim the silence before the first note, then normalise so no example is
  # twice as loud as its neighbour.
  ffmpeg -loglevel error -y -i "$wav" \
    -af "silenceremove=1:0:-50dB,loudnorm=I=-16:TP=-1.5:LRA=11" \
    -codec:a libmp3lame -q:a 4 "$AUDIO/$name.mp3"

  if command -v qrencode >/dev/null; then
    mkdir -p "$AUDIO/qr"
    qrencode -o "$AUDIO/qr/$name.png" -s 6 -m 1 "${BASE_URL}${name}.mp3"
  fi

  echo "$name.mp3  $(du -h "$AUDIO/$name.mp3" | cut -f1)"
}

if [ $# -gt 0 ]; then
  for n in "$@"; do convert "${n%.wav}"; done
else
  shopt -s nullglob
  for wav in "$AUDIO"/*.wav; do
    name=$(basename "$wav" .wav)
    [ -f "$AUDIO/$name.mp3" ] && continue
    convert "$name"
  done
fi
