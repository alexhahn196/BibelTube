#!/usr/bin/env bash
# ---------------------------------------------------------------
# teardown_batch.sh - Kontrast-Analyse mehrerer Konkurrenzkanaele
#
# Waehlt pro Kanal automatisch DREI Videos aus:
#   TOP    = meistgesehenes Video
#   MEDIAN = typisches Video (mittlere Views)
#   FLOP   = schwaechstes Video mit >2 Wochen Standzeit
#
# Damit entsteht Kontrast INNERHALB jedes Kanals (Produktion konstant,
# nur Titel/Thumbnail/Thema variieren) und ZWISCHEN den Kanaelen
# (unterschiedliche Produktionsqualitaet bei gleichem Format).
#
# Alle Ergebnisse landen in EINER Vergleichsmatrix: matrix.csv
#
# Aufruf:  ./teardown_batch.sh kanaele.txt
#          (eine Kanal-URL pro Zeile, # = Kommentar)
#
# Voraussetzungen: yt-dlp, ffmpeg, ffprobe, python3, bc
# ---------------------------------------------------------------

set -uo pipefail

LIST="${1:?Bitte Datei mit Kanal-URLs uebergeben}"
OUT="teardown_batch_$(date +%Y%m%d_%H%M%S)"
MATRIX="$OUT/matrix.csv"
mkdir -p "$OUT/frames"

echo "kanal,rolle,video_id,titel,views,likes,like_rate_pct,dauer_s,aufloesung,fps,tags_gesetzt,captions,kategorie,sprache_bis_pct,visuell" > "$MATRIX"

# ---------------------------------------------------------------
# Ein einzelnes Video vermessen -> eine CSV-Zeile
# ---------------------------------------------------------------
analyse_video() {
  local CHAN="$1" ROLE="$2" VID="$3"
  local URL="https://www.youtube.com/watch?v=$VID"
  local WORK="$OUT/tmp_$VID"
  mkdir -p "$WORK"

  echo "    [$ROLE] $VID"

  yt-dlp --skip-download --write-info-json -o "$WORK/m" "$URL" >/dev/null 2>&1 || return

  local INFO
  INFO=$(python3 -c "
import json,glob,sys
try: d=json.load(open(glob.glob('$WORK/m*.info.json')[0]))
except: sys.exit(1)
t=(d.get('title') or '').replace(',',';').replace('\"','')[:70]
views=d.get('view_count') or 0
likes=d.get('like_count') or 0
rate=round(likes*100/views,2) if views else 0
tags='JA' if d.get('tags') else 'NEIN'
caps='JA' if d.get('subtitles') else 'NEIN'
cat=(d.get('categories') or ['?'])[0]
print(f\"{t},{views},{likes},{rate},{d.get('duration') or 0},{d.get('width')}x{d.get('height')},{d.get('fps')},{tags},{caps},{cat}\")
") || { rm -rf "$WORK"; return; }

  local DUR
  DUR=$(echo "$INFO" | cut -d, -f5)
  [ "${DUR:-0}" -lt 60 ] && { rm -rf "$WORK"; return; }

  # ---- Fuenf Stichproben ueber die Laufzeit -------------------
  local VOICE_LAST=0 PREV_FRAME="" VIS="statisch"
  for i in 1 2 3 4 5; do
    local T=$(( DUR * i / 6 ))
    local HMS
    HMS=$(printf '%02d:%02d:%02d' $((T/3600)) $(((T%3600)/60)) $((T%60)))
    local END
    END=$(printf '%02d:%02d:%02d' $(((T+15)/3600)) $((((T+15)%3600)/60)) $(((T+15)%60)))

    yt-dlp -f "bv*[height<=720]+ba/b" \
           --download-sections "*${HMS}-${END}" --force-keyframes-at-cuts \
           -o "$WORK/c$i.%(ext)s" "$URL" >/dev/null 2>&1 || continue
    local CLIP
    CLIP=$(ls "$WORK/c$i."* 2>/dev/null | head -1); [ -z "$CLIP" ] && continue

    # Frame sichern (nur fuer TOP-Videos, spart Platz)
    if [ "$ROLE" = "TOP" ]; then
      ffmpeg -y -loglevel error -i "$CLIP" -vframes 1 -vf scale=800:-1 \
             "$OUT/frames/${CHAN}_${VID}_$i.png" 2>/dev/null
    fi

    # Frame fuer Bildvergleich
    ffmpeg -y -loglevel error -i "$CLIP" -vframes 1 -vf scale=480:-1 \
           "$WORK/f$i.png" 2>/dev/null
    if [ -n "$PREV_FRAME" ] && [ -f "$WORK/f$i.png" ]; then
      local D
      D=$(ffmpeg -hide_banner -i "$PREV_FRAME" -i "$WORK/f$i.png" \
            -lavfi "[0:v][1:v]scale2ref[a][b];[a][b]psnr" -f null - 2>&1 \
          | grep -o 'average:[0-9.]*' | cut -d: -f2 | head -1)
      if [ -n "$D" ]; then
        awk -v d="$D" 'BEGIN{exit !(d<25)}' && VIS="szenenwechsel"
        awk -v d="$D" -v v="$VIS" 'BEGIN{exit !(d>=25 && d<38 && v=="statisch")}' && VIS="langsame_bewegung"
      fi
    fi
    PREV_FRAME="$WORK/f$i.png"

    # Sprache aktiv? Dynamik = Peak - RMS
    ffmpeg -y -loglevel error -i "$CLIP" -vn -ac 1 -ar 22050 "$WORK/a$i.wav" 2>/dev/null
    if [ -f "$WORK/a$i.wav" ]; then
      local ST RMS PK
      ST=$(ffmpeg -hide_banner -i "$WORK/a$i.wav" -af astats=metadata=1 -f null - 2>&1)
      RMS=$(echo "$ST" | grep -m1 "RMS level dB"  | awk '{print $NF}')
      PK=$(echo  "$ST" | grep -m1 "Peak level dB" | awk '{print $NF}')
      if [ -n "$RMS" ] && [ -n "$PK" ]; then
        awk -v p="$PK" -v r="$RMS" 'BEGIN{exit !((p-r)>12)}' && VOICE_LAST=$(( i * 100 / 6 ))
      fi
    fi
    rm -f "$CLIP"
  done

  echo "$CHAN,$ROLE,$VID,$INFO,$VOICE_LAST,$VIS" >> "$MATRIX"
  rm -rf "$WORK"
}

# ---------------------------------------------------------------
# Hauptschleife ueber alle Kanaele
# ---------------------------------------------------------------
while IFS= read -r CHANNEL_URL; do
  [[ -z "$CHANNEL_URL" || "$CHANNEL_URL" =~ ^# ]] && continue
  CHAN=$(echo "$CHANNEL_URL" | sed 's#.*/##; s/@//' | tr -cd '[:alnum:]_-')
  echo "==> Kanal: $CHAN"

  # Videoliste mit Viewcounts holen (flach, ohne Download)
  yt-dlp --flat-playlist --dump-json "${CHANNEL_URL%/}/videos" 2>/dev/null \
    > "$OUT/${CHAN}_videos.jsonl" || { echo "    Fehler"; continue; }

  # Top / Median / Flop bestimmen
  PICKS=$(python3 -c "
import json,sys
rows=[]
for line in open('$OUT/${CHAN}_videos.jsonl'):
    try:
        d=json.loads(line)
        if d.get('view_count') and (d.get('duration') or 0)>300:
            rows.append((d['view_count'], d['id']))
    except: pass
if len(rows)<3: sys.exit(1)
rows.sort()
print(rows[-1][1], rows[len(rows)//2][1], rows[0][1])
") || { echo "    zu wenige Videos"; continue; }

  read -r TOP MED FLOP <<< "$PICKS"
  analyse_video "$CHAN" "TOP"    "$TOP"
  analyse_video "$CHAN" "MEDIAN" "$MED"
  analyse_video "$CHAN" "FLOP"   "$FLOP"
done < "$LIST"

# ---------------------------------------------------------------
# Auswertung
# ---------------------------------------------------------------
echo ""
echo "=============================================="
column -s, -t < "$MATRIX"
echo "=============================================="
echo "Matrix:  $MATRIX"
echo "Frames:  $OUT/frames/  (nur TOP-Videos)"
echo ""
echo "Naechster Schritt in Claude Code:"
echo "  1. Welche Werte sind bei ALLEN TOP-Videos gleich und bei den"
echo "     FLOPs anders?  -> das sind die echten Stellschrauben."
echo "  2. Welche Werte sind ueberall gleich?  -> irrelevant, ignorieren."
echo "  3. Frames ansehen: Bildaufbau, Farbpalette, Typografie."
