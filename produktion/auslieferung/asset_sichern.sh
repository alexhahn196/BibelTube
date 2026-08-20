#!/usr/bin/env bash
#
# asset_sichern.sh - eine beliebige Datei als Release-Asset eines Videos
# ablegen und ihre Pruefsumme ins Manifest schreiben.
#
#     produktion/auslieferung/asset_sichern.sh V4 produktion/video-04/video-04.mp4
#     produktion/auslieferung/asset_sichern.sh V4 produktion/arbeit/video-04/mix.wav
#
# Fuer die Tonspur gibt es tonspur_sichern.sh — das wandelt zusaetzlich
# nach FLAC und weist die Verlustfreiheit nach. Dieses Skript legt die
# Datei so ab, wie sie ist.
#
# Das MP4 gehoert hierher, solange es zum Upload gebraucht wird, und darf
# danach aus dem Release geloescht werden:
#     gh release delete-asset v04 video-04.mp4
# Die Tonspur bleibt und macht die Montage jederzeit wiederholbar.
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/gemeinsam.sh"

[ $# -ge 2 ] || { echo "Aufruf: $0 <V1…V8> <datei>" >&2; exit 2; }
video="$1"; datei="$2"; nr="$(nummer "$video")"; tag="$(marke "$video")"
werkzeug_pruefen sha256sum
[ -f "$datei" ] || fehler "Datei fehlt: $datei"

name="$(basename "$datei")"
man="$(manifest "$video")"
g=$(stat -c%s "$datei")

GRENZE=$((2*1024*1024*1024))
[ "$g" -lt "$GRENZE" ] || fehler "$name ist $g B — ueber der 2-GB-Grenze je Release-Asset."

echo "Datei    $datei  ($((g/1000000)) MB)"
echo "Bilde sha256 …"
s="$(sha "$datei")"

manifest_setzen "$man" "$name" groesse "$g"
manifest_setzen "$man" "$name" sha256  "$s"
manifest_setzen "$man" "$name" tag     "$tag"

# Bei Tondateien zusaetzlich die PCM-Pruefsumme: nur sie ueberlebt einen
# Wechsel des Containers oder des Kopfes.
case "${name,,}" in
    *.wav|*.flac)
        if command -v ffmpeg >/dev/null; then
            manifest_setzen "$man" "$name" pcm_md5 "$(pcm "$datei")"
        fi ;;
esac

echo
echo "Manifest $man"
sed 's/^/  /' "$man"

echo
gh_pruefen
release_sichern "$tag" "$video"
echo "  Lade $name hoch ($((g/1000000)) MB) …"
gh release upload "$tag" "$datei" --clobber

ist=$(gh release view "$tag" --json assets \
      --jq ".assets[] | select(.name==\"$name\") | .size" 2>/dev/null || true)
[ "$ist" = "$g" ] || fehler "Asset im Release meldet '$ist' B statt $g B."
echo "  im Release bestaetigt: $ist B ✓"

echo
echo "Manifest einchecken:"
echo "  git add $man && git commit -m 'Asset $name zu Release $tag' && git push"
