#!/usr/bin/env bash
#
# tonspur_sichern.sh - die Tonspur eines Videos verlustfrei als FLAC
# sichern und in repo-taugliche Teile zerlegen.
#
#     produktion/auslieferung/tonspur_sichern.sh V4
#
# Warum die Tonspur und nicht das fertige MP4:
# stimme.wav ist das einzige Zwischenergebnis der Pipeline, das Geld
# kostet (Fish-Audio-TTS, rund 160.000 Zeichen je Video) und das sich
# nicht aus dem Repo neu erzeugen laesst. Text, Standbild, Bildkette,
# Klangbett und SRT liegen alle im Repo. Aus stimme.wav sind Schritt 3
# (Mischung) und Schritt 5 (Montage) jederzeit kostenlos wiederholbar —
# das MP4 ist also reproduzierbar, die TTS-Ausgabe nicht.
#
# FLAC ist verlustfrei: das Ergebnis ist bitgleich zur WAV, nur rund
# halb so gross. Das Skript weist das nach, bevor es fertig meldet.
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Aufruf: $0 <V1…V8>" >&2
    exit 2
fi

video="$1"
case "$video" in
    V[0-9]|V[0-9][0-9]) ;;
    *) echo "FEHLER: Video als V1 … V8 angeben, nicht '$video'." >&2; exit 2 ;;
esac

HIER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WURZEL="$(cd "$HIER/../.." && pwd)"
nr=$(printf '%02d' "${video#V}")

quelle="$WURZEL/produktion/arbeit/video-$nr/stimme.wav"
if [ ! -f "$quelle" ]; then
    echo "FEHLER: Tonspur fehlt: $quelle" >&2
    echo "Sie entsteht in Schritt 2 (TTS) und braucht FISH_KEY." >&2
    exit 1
fi

for t in ffmpeg ffprobe; do
    command -v "$t" >/dev/null || { echo "FEHLER: $t fehlt." >&2; exit 1; }
done

flac="$WURZEL/produktion/arbeit/video-$nr/stimme-video-$nr.flac"

echo "Quelle   $quelle  ($(stat -c%s "$quelle") B)"
echo "Wandle nach FLAC (-compression_level 8) …"
ffmpeg -y -loglevel error -i "$quelle" -c:a flac -compression_level 8 "$flac"

# --- Nachweis: FLAC ist bitgleich zur WAV -----------------------------
# Beide Seiten als roher PCM-Strom, Pruefsumme vergleichen. Erst wenn
# die stimmt, darf die WAV als entbehrlich gelten.
echo "Pruefe Verlustfreiheit …"
roh_wav=$(ffmpeg -v error -i "$quelle" -f s16le -c:a pcm_s16le - | md5sum | cut -d' ' -f1)
roh_flac=$(ffmpeg -v error -i "$flac"   -f s16le -c:a pcm_s16le - | md5sum | cut -d' ' -f1)
if [ "$roh_wav" != "$roh_flac" ]; then
    echo "FEHLER: FLAC ist NICHT bitgleich ($roh_wav != $roh_flac)." >&2
    rm -f "$flac"
    exit 1
fi

w=$(stat -c%s "$quelle"); f=$(stat -c%s "$flac")
echo "  bitgleich ✓  PCM-MD5 $roh_wav"
echo "  $((w/1000000)) MB WAV -> $((f/1000000)) MB FLAC  ($((f*100/w)) %)"
echo

"$HIER/zerlegen.sh" "$flac"

# Die PCM-Pruefsumme mit ins manifest: sie ueberlebt den Umweg ueber FLAC
# und ueber den WAV-Header und ist damit der einzige Wert, an dem sich
# der Rueckweg wirklich messen laesst. tonspur_zurueck.sh prueft ihn.
echo "pcm_md5     $roh_wav" >> "$HIER/stimme-video-$nr/manifest.txt"

echo
echo "Zurueck kommt die Tonspur mit:"
echo "  produktion/auslieferung/tonspur_zurueck.sh $video"
echo "Danach Schritt 3 und 5 neu laufen lassen — ohne TTS-Kosten."
