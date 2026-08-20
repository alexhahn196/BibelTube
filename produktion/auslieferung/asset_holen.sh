#!/usr/bin/env bash
#
# asset_holen.sh - ein Release-Asset holen und gegen das Manifest pruefen.
#
#     produktion/auslieferung/asset_holen.sh V4 video-04.mp4
#     produktion/auslieferung/asset_holen.sh V4 video-04.mp4 /pfad/ziel.mp4
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/gemeinsam.sh"

[ $# -ge 2 ] || { echo "Aufruf: $0 <V1…V8> <assetname> [zieldatei]" >&2; exit 2; }
video="$1"; name="$2"; nr="$(nummer "$video")"; tag="$(marke "$video")"
werkzeug_pruefen sha256sum

man="$(manifest "$video")"
[ -f "$man" ] || fehler "Kein Manifest: $man"
soll_g="$(manifest_holen "$man" "$name" groesse)" || true
soll_s="$(manifest_holen "$man" "$name" sha256)" || true
[ -n "$soll_s" ] || fehler "Im Manifest steht keine sha256 fuer $name.
Bekannte Assets fuer $video:
$(awk '{print "  " $1}' "$man" | sort -u)"

ziel="${3:-$WURZEL/produktion/arbeit/video-$nr/$name}"
mkdir -p "$(dirname "$ziel")"

gh_pruefen
echo "[1/2] Hole $name aus Release $tag …"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
gh release download "$tag" --pattern "$name" --dir "$tmp"
[ -f "$tmp/$name" ] || fehler "Release $tag enthaelt kein Asset $name."

ist_g=$(stat -c%s "$tmp/$name")
[ "$ist_g" = "$soll_g" ] || fehler "$ist_g B statt $soll_g B."
ist_s="$(sha "$tmp/$name")"
[ "$ist_s" = "$soll_s" ] || fehler "SHA-256 $ist_s statt $soll_s."
echo "[2/2] Groesse und sha256 stimmen ✓"

mv "$tmp/$name" "$ziel"
echo
echo "Fertig: $ziel  ($ist_g B)"
