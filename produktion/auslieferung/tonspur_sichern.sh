#!/usr/bin/env bash
#
# tonspur_sichern.sh - die Tonspur eines Videos verlustfrei als FLAC
# sichern und als Release-Asset ablegen.
#
#     produktion/auslieferung/tonspur_sichern.sh V4
#
# Warum die Tonspur und nicht das fertige MP4:
# stimme.wav ist das einzige Zwischenergebnis der Pipeline, das Geld
# kostet (Fish-Audio-TTS, rund 160.000 Zeichen je Video) und sich nicht
# aus dem Repo neu erzeugen laesst. Text, Standbild, Bildkette, Klangbett
# und SRT liegen alle im Repo. Aus stimme.wav sind Schritt 3 (Mischung)
# und Schritt 5 (Montage) jederzeit kostenlos wiederholbar — das MP4 ist
# reproduzierbar, die TTS-Ausgabe nicht.
#
# Warum als Release-Asset und nicht ins Repo:
# Git gibt Platz nie wieder frei. Acht Tonspuren waeren 4,1-5,5 GB
# dauerhaft in der Historie, gegen eine harte Grenze von 5,0 GB — das
# traegt die Serie nicht zu Ende. Ein Release-Asset erlaubt 2 GB je Datei,
# zaehlt nicht gegen die Repo-Groesse, und Loeschen wirkt wirklich.
# Im Repo bleibt nur die Manifestdatei mit den Pruefsummen.
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/gemeinsam.sh"

[ $# -ge 1 ] || { echo "Aufruf: $0 <V1…V8>" >&2; exit 2; }
video="$1"; nr="$(nummer "$video")"; tag="$(marke "$video")"
werkzeug_pruefen ffmpeg ffprobe sha256sum md5sum

quelle="$WURZEL/produktion/arbeit/video-$nr/stimme.wav"
[ -f "$quelle" ] || fehler "Tonspur fehlt: $quelle
Sie entsteht in Schritt 2 (TTS) und braucht FISH_KEY."

name="stimme-video-$nr.flac"
flac="$WURZEL/produktion/arbeit/video-$nr/$name"
man="$(manifest "$video")"

echo "Quelle   $quelle  ($(stat -c%s "$quelle") B)"
echo "Wandle nach FLAC (-compression_level 8) …"
ffmpeg -y -loglevel error -i "$quelle" -c:a flac -compression_level 8 "$flac"

# --- Nachweis: FLAC ist bitgleich zur WAV -----------------------------
echo "Pruefe Verlustfreiheit …"
roh_wav="$(pcm "$quelle")"
roh_flac="$(pcm "$flac")"
[ "$roh_wav" = "$roh_flac" ] || { rm -f "$flac"; fehler "FLAC ist NICHT bitgleich ($roh_wav != $roh_flac)."; }

w=$(stat -c%s "$quelle"); f=$(stat -c%s "$flac")
echo "  bitgleich ✓  PCM-MD5 $roh_wav"
echo "  $((w/1000000)) MB WAV -> $((f/1000000)) MB FLAC  ($((f*100/w)) %)"

GRENZE=$((2*1024*1024*1024))
[ "$f" -lt "$GRENZE" ] || fehler "FLAC ist $f B — ueber der 2-GB-Grenze je Release-Asset."

# --- Pruefsummen ins Repo ---------------------------------------------
manifest_setzen "$man" "$name" groesse "$f"
manifest_setzen "$man" "$name" sha256  "$(sha "$flac")"
manifest_setzen "$man" "$name" pcm_md5 "$roh_wav"
manifest_setzen "$man" "$name" tag     "$tag"
echo
echo "Manifest $man"
sed 's/^/  /' "$man"

# --- Hochladen ---------------------------------------------------------
echo
gh_pruefen
release_sichern "$tag" "$video"
echo "  Lade $name hoch ($((f/1000000)) MB) …"
gh release upload "$tag" "$flac" --clobber

# Gegenprobe: liegt das Asset mit der erwarteten Groesse im Release?
ist=$(gh release view "$tag" --json assets \
      --jq ".assets[] | select(.name==\"$name\") | .size" 2>/dev/null || true)
[ "$ist" = "$f" ] || fehler "Asset im Release meldet '$ist' B statt $f B."
echo "  im Release bestaetigt: $ist B ✓"
rm -f "$flac"

echo
echo "Fertig. Jetzt das Manifest einchecken:"
echo "  git add $man && git commit -m 'Tonspur Video $nr gesichert' && git push"
echo
echo "Zurueck kommt die Tonspur mit:"
echo "  produktion/auslieferung/tonspur_zurueck.sh $video"
