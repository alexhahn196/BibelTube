#!/usr/bin/env bash
#
# zusammensetzen.sh - ein zerlegtes Video aus den Teilen im Repo
# wiederherstellen, mit Pruefsummenkontrolle vor und nach dem Fuegen.
#
#     produktion/auslieferung/zusammensetzen.sh video-04
#     produktion/auslieferung/zusammensetzen.sh video-04 /pfad/ziel.mp4
#
# Prueft in dieser Reihenfolge:
#   1. sind alle im manifest.txt gemeldeten Teile da,
#   2. stimmt jeder Teil gegen pruefsummen.sha256,
#   3. stimmt Groesse, SHA-256 und MD5 der gefuegten Datei gegen manifest.txt.
# Jeder Fehlschlag bricht ab; eine halbfertige Datei bleibt nicht liegen.
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Aufruf: $0 <video-04|verzeichnis> [zieldatei]" >&2
    exit 2
fi

HIER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Argument darf ein Name (video-04) oder ein Pfad sein.
if [ -d "$1" ]; then
    quelle="$(cd "$1" && pwd)"
elif [ -d "$HIER/$1" ]; then
    quelle="$HIER/$1"
else
    echo "FEHLER: kein Verzeichnis $1 und kein $HIER/$1" >&2
    exit 1
fi

manifest="$quelle/manifest.txt"
pruef="$quelle/pruefsummen.sha256"
for f in "$manifest" "$pruef"; do
    [ -f "$f" ] || { echo "FEHLER: $f fehlt." >&2; exit 1; }
done

hole() { awk -v k="$1" '$1==k {print $2}' "$manifest"; }
name=$(hole datei)
soll_groesse=$(hole groesse)
soll_md5=$(hole md5)
soll_sha=$(hole sha256)
soll_teile=$(hole teile)

ziel="${2:-$quelle/$name}"

echo "Video        $name"
echo "erwartet     $soll_teile Teile, $soll_groesse B"
echo

# --- 1. Vollzaehligkeit ------------------------------------------------
ist_teile=$(find "$quelle" -maxdepth 1 -name '*.part' | wc -l)
if [ "$ist_teile" -ne "$soll_teile" ]; then
    echo "FEHLER: $ist_teile Teile gefunden, $soll_teile erwartet." >&2
    echo "Fehlt etwas, ist der Klon unvollstaendig — git lfs/partial clone pruefen." >&2
    exit 1
fi
echo "[1/3] Vollzaehligkeit  $ist_teile/$soll_teile Teile"

# --- 2. Pruefsumme je Teil ---------------------------------------------
if ! ( cd "$quelle" && sha256sum --quiet -c pruefsummen.sha256 ); then
    echo "FEHLER: mindestens ein Teil ist beschaedigt." >&2
    exit 1
fi
echo "[2/3] Teil-Pruefsummen alle korrekt"

# --- 3. Fuegen und Gesamtdatei pruefen ---------------------------------
tmp="$(mktemp "${ziel}.XXXXXX.unfertig")"
aufraeumen() { rm -f "$tmp"; }
trap aufraeumen EXIT

# Nullgepolsterte Suffixe: die Glob-Sortierung ist die Teilereihenfolge.
cat "$quelle"/*.part > "$tmp"

ist_groesse=$(stat -c%s "$tmp")
if [ "$ist_groesse" -ne "$soll_groesse" ]; then
    echo "FEHLER: $ist_groesse B statt $soll_groesse B." >&2
    exit 1
fi

ist_sha=$(sha256sum "$tmp" | cut -d' ' -f1)
if [ "$ist_sha" != "$soll_sha" ]; then
    echo "FEHLER: SHA-256 $ist_sha statt $soll_sha." >&2
    exit 1
fi

ist_md5=$(md5sum "$tmp" | cut -d' ' -f1)
if [ "$ist_md5" != "$soll_md5" ]; then
    echo "FEHLER: MD5 $ist_md5 statt $soll_md5." >&2
    exit 1
fi

mv "$tmp" "$ziel"
trap - EXIT

echo "[3/3] Gesamtdatei      Groesse, SHA-256 und MD5 stimmen"
echo
echo "Fertig: $ziel"
echo "  $ist_groesse B"
echo "  MD5     $ist_md5"
echo "  SHA-256 $ist_sha"
