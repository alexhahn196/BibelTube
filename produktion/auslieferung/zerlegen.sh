#!/usr/bin/env bash
#
# zerlegen.sh - ein fertiges Video in repo-taugliche Teile zerlegen.
#
#     produktion/auslieferung/zerlegen.sh produktion/video-04/video-04.mp4
#
# Ergebnis: produktion/auslieferung/video-04/ mit
#   video-04.mp4.00.part … video-04.mp4.NN.part
#   pruefsummen.sha256   je Teil, fuer zusammensetzen.sh
#   manifest.txt         Groesse, MD5 und SHA-256 der GANZEN Datei
#
# Warum nach Groesse (-b) und nicht nach fester Teilezahl (-n 20):
# GitHub weist einzelne Blobs ab 100 MiB hart zurueck. Bei 1825 MB
# (Video 04) ergeben 20 Teile 87 MiB und passen; bei 2415 MB (Video 02)
# ergaeben dieselben 20 Teile 115 MiB und der Push wuerde abgewiesen.
# 90 MiB je Teil haelt die Grenze fuer jede Dateigroesse ein und liefert
# fuer Video 04 genau die erwarteten 20 Teile.
set -euo pipefail

TEILGROESSE="${TEILGROESSE:-90M}"   # 90 MiB
GRENZE=104857600                    # 100 MiB, GitHubs harte Blob-Grenze

if [ $# -lt 1 ]; then
    echo "Aufruf: $0 <video.mp4>" >&2
    exit 2
fi

quelle="$1"
if [ ! -f "$quelle" ]; then
    echo "FEHLER: Datei fehlt: $quelle" >&2
    exit 1
fi

HIER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
name="$(basename "$quelle")"
ziel="$HIER/${name%.*}"

mkdir -p "$ziel"
rm -f "$ziel"/*.part "$ziel/pruefsummen.sha256" "$ziel/manifest.txt"

echo "Zerlege $quelle …"
split -b "$TEILGROESSE" -d -a 2 --additional-suffix=.part "$quelle" "$ziel/$name."

teile=$(find "$ziel" -maxdepth 1 -name '*.part' | wc -l)
if [ "$teile" -eq 0 ]; then
    echo "FEHLER: split hat keine Teile erzeugt." >&2
    exit 1
fi
if [ "$teile" -gt 99 ]; then
    echo "FEHLER: $teile Teile — zweistellige Suffixe (-a 2) reichen nicht." >&2
    exit 1
fi

# Kein Teil darf die Blob-Grenze reissen, sonst scheitert erst der Push.
groesster=$(find "$ziel" -maxdepth 1 -name '*.part' -printf '%s\n' | sort -n | tail -1)
if [ "$groesster" -ge "$GRENZE" ]; then
    echo "FEHLER: groesster Teil $groesster B >= 100 MiB. TEILGROESSE kleiner setzen." >&2
    exit 1
fi

( cd "$ziel" && sha256sum ./*.part > pruefsummen.sha256 )

groesse=$(stat -c%s "$quelle")
md5=$(md5sum "$quelle" | cut -d' ' -f1)
sha=$(sha256sum "$quelle" | cut -d' ' -f1)

{
    echo "datei       $name"
    echo "groesse     $groesse"
    echo "md5         $md5"
    echo "sha256      $sha"
    echo "teile       $teile"
    echo "teilgroesse $TEILGROESSE"
} > "$ziel/manifest.txt"

echo
echo "Teile         $teile à höchstens $((groesster/1024/1024)) MiB  →  $ziel"
echo "Gesamtgroesse $groesse B"
echo "MD5           $md5"
echo "SHA-256       $sha"
echo
echo "Jetzt einchecken:  git add $ziel && git commit && git push -u origin <branch>"
