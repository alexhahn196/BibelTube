#!/usr/bin/env bash
#
# tonspur_zurueck.sh - die gesicherte Tonspur aus den Teilen im Repo
# wiederherstellen, bis zurueck zu produktion/arbeit/video-NN/stimme.wav.
#
#     produktion/auslieferung/tonspur_zurueck.sh V4
#
# Danach laufen Schritt 3 (Mischung) und Schritt 5 (Montage) ohne
# TTS-Kosten:
#     python3 produktion/pipeline/render.py V4 --nur 3 5
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

teileordner="$HIER/stimme-video-$nr"
if [ ! -d "$teileordner" ]; then
    echo "FEHLER: keine gesicherte Tonspur unter $teileordner" >&2
    exit 1
fi
command -v ffmpeg >/dev/null || { echo "FEHLER: ffmpeg fehlt." >&2; exit 1; }

arbeit="$WURZEL/produktion/arbeit/video-$nr"
mkdir -p "$arbeit"
flac="$arbeit/stimme-video-$nr.flac"
wav="$arbeit/stimme.wav"

# 1. Teile pruefen und fuegen (Pruefsummenkontrolle steckt im Skript).
"$HIER/zusammensetzen.sh" "stimme-video-$nr" "$flac"

# 2. FLAC nach WAV zurueck — genau das Format, das Schritt 3 erwartet:
#    44100 Hz, mono, PCM_16 (siehe schritt2_tts.py).
echo
echo "Dekodiere nach $wav …"
# -bitexact: kein Encoder-Namensfeld im Header, damit der Kopf
# reproduzierbar bleibt und nicht bei jeder ffmpeg-Version anders aussieht.
ffmpeg -y -loglevel error -bitexact -i "$flac" -c:a pcm_s16le -ar 44100 -ac 1 "$wav"
rm -f "$flac"

# Der eigentliche Nachweis: die Audiodaten selbst, ohne WAV-Kopf. Ein
# Byte-Vergleich der ganzen Datei taugt nicht — der Kopf traegt je nach
# Schreiber unterschiedliche Zusatzfelder, die Samples sind trotzdem gleich.
soll_pcm=$(awk '$1=="pcm_md5" {print $2}' "$HIER/stimme-video-$nr/manifest.txt")
if [ -n "$soll_pcm" ]; then
    ist_pcm=$(ffmpeg -v error -i "$wav" -f s16le -c:a pcm_s16le - | md5sum | cut -d' ' -f1)
    if [ "$ist_pcm" != "$soll_pcm" ]; then
        echo "FEHLER: Audiodaten weichen ab ($ist_pcm != $soll_pcm)." >&2
        exit 1
    fi
    echo "  Audiodaten bitgleich zur Vertonung ✓  PCM-MD5 $ist_pcm"
else
    echo "  HINWEIS: kein pcm_md5 im manifest — vor dieser Skriptfassung gesichert." >&2
fi

sr=$(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of default=nw=1:nk=1 "$wav")
ka=$(ffprobe -v error -select_streams a:0 -show_entries stream=channels    -of default=nw=1:nk=1 "$wav")
if [ "$sr" != "44100" ] || [ "$ka" != "1" ]; then
    echo "FEHLER: $wav ist $sr Hz / $ka Kanal, erwartet 44100 Hz / 1 Kanal." >&2
    exit 1
fi

echo "Fertig: $wav  ($(stat -c%s "$wav") B, $sr Hz, mono)"
echo
echo "Weiter ohne TTS-Kosten:"
echo "  python3 produktion/pipeline/render.py $video --nur 3 5"
