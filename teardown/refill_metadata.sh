#!/usr/bin/env bash
# ---------------------------------------------------------------
# refill_metadata.sh - holt die Metadaten der Videos nach, die
# teardown_batch.sh wegen YouTube-Ratelimit (429 -> Bot-Check)
# nicht vermessen konnte.
#
# Gleiche Feldlogik wie analyse_video() im Originalskript, aber
# mit Pacing + Backoff statt Schnellfeuer.
#
# Aufruf: ./refill_metadata.sh <matrix.csv> <ids.txt>
#         ids.txt: "kanal rolle video_id" pro Zeile
# ---------------------------------------------------------------
set -uo pipefail

MATRIX="${1:?matrix.csv}"
IDS="${2:?ids.txt}"
WORKROOT="$(dirname "$MATRIX")/refill"
mkdir -p "$WORKROOT"

extract() {
  python3 -c "
import json,glob,sys
try: d=json.load(open(glob.glob('$1/m*.info.json')[0]))
except: sys.exit(1)
t=(d.get('title') or '').replace(',',';').replace('\"','')[:70]
if not t: sys.exit(1)
views=d.get('view_count') or 0
likes=d.get('like_count') or 0
rate=round(likes*100/views,2) if views else 0
tags='JA' if d.get('tags') else 'NEIN'
caps='JA' if d.get('subtitles') else 'NEIN'
cat=(d.get('categories') or ['?'])[0]
print(f\"{t},{views},{likes},{rate},{d.get('duration') or 0},{d.get('width')}x{d.get('height')},{d.get('fps')},{tags},{caps},{cat}\")
"
}

while read -r CHAN ROLE VID; do
  [ -z "${VID:-}" ] && continue
  grep -q ",$VID," "$MATRIX" && { echo "  [skip] $VID schon vorhanden"; continue; }

  OK=0
  for ATTEMPT in 1 2 3 4 5; do
    WORK="$WORKROOT/$VID"; rm -rf "$WORK"; mkdir -p "$WORK"

    timeout 150 /usr/local/bin/yt-dlp --js-runtimes node --skip-download \
      --write-info-json --retries 2 --socket-timeout 30 --no-warnings \
      -o "$WORK/m" "https://www.youtube.com/watch?v=$VID" >/dev/null 2>&1

    if INFO=$(extract "$WORK"); then
      DUR=$(echo "$INFO" | cut -d, -f5)
      if [ "${DUR:-0}" -ge 60 ]; then
        # sprache_bis_pct + visuell bleiben leer: Medien-Download ist in
        # dieser Umgebung blockiert (403). Werte kommen aus separater Quelle.
        echo "$CHAN,$ROLE,$VID,$INFO,NA,NA" >> "$MATRIX"
        echo "  [ok $ATTEMPT] $ROLE $VID"
        OK=1
      fi
    fi
    rm -rf "$WORK"
    [ "$OK" = "1" ] && break

    BACK=$(( ATTEMPT * 45 ))
    echo "  [retry $ATTEMPT] $VID -> warte ${BACK}s"
    sleep "$BACK"
  done

  [ "$OK" = "0" ] && echo "  [FEHLGESCHLAGEN] $ROLE $VID"
  sleep 20
done < "$IDS"

echo "REFILL FERTIG"
