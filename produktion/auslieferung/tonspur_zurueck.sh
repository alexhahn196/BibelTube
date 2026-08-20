#!/usr/bin/env bash
#
# tonspur_zurueck.sh - die gesicherte Tonspur aus dem Release holen,
# pruefen und bis zurueck zu produktion/arbeit/video-NN/stimme.wav
# dekodieren.
#
#     produktion/auslieferung/tonspur_zurueck.sh V4
#
# Danach laufen Schritt 3 (Mischung) und Schritt 5 (Montage) ohne
# TTS-Kosten:
#     python3 produktion/pipeline/render.py V4 --nur 3 5
set -euo pipefail
source "$(dirname "${BASH_SOURCE[0]}")/gemeinsam.sh"

[ $# -ge 1 ] || { echo "Aufruf: $0 <V1…V8>" >&2; exit 2; }
video="$1"; nr="$(nummer "$video")"; tag="$(marke "$video")"
werkzeug_pruefen ffmpeg ffprobe sha256sum md5sum

name="stimme-video-$nr.flac"
man="$(manifest "$video")"
[ -f "$man" ] || fehler "Kein Manifest: $man
Fuer dieses Video wurde nie eine Tonspur gesichert."

soll_groesse="$(manifest_holen "$man" "$name" groesse)" || true
soll_sha="$(manifest_holen "$man" "$name" sha256)" || true
soll_pcm="$(manifest_holen "$man" "$name" pcm_md5)" || true
[ -n "$soll_sha" ] || fehler "Im Manifest steht keine sha256 fuer $name."

arbeit="$WURZEL/produktion/arbeit/video-$nr"
mkdir -p "$arbeit"
flac="$arbeit/$name"
wav="$arbeit/stimme.wav"

# --- 1. Holen ----------------------------------------------------------
gh_pruefen
echo "[1/4] Hole $name aus Release $tag …"
rm -f "$flac"
gh release download "$tag" --pattern "$name" --dir "$arbeit"
[ -f "$flac" ] || fehler "Release $tag enthaelt kein Asset $name."

# --- 2. FLAC gegen das Manifest ----------------------------------------
ist_groesse=$(stat -c%s "$flac")
[ "$ist_groesse" = "$soll_groesse" ] || fehler "$ist_groesse B statt $soll_groesse B."
ist_sha="$(sha "$flac")"
[ "$ist_sha" = "$soll_sha" ] || fehler "SHA-256 $ist_sha statt $soll_sha."
echo "[2/4] FLAC unversehrt  ($ist_groesse B, sha256 stimmt)"

# --- 3. Dekodieren -----------------------------------------------------
# -bitexact: kein Encoder-Namensfeld im Kopf, damit die WAV reproduzierbar
# bleibt und nicht bei jeder ffmpeg-Fassung anders aussieht.
# Format wie schritt2_tts.py es schreibt: 44100 Hz, mono, PCM_16.
echo "[3/4] Dekodiere nach $wav …"
ffmpeg -y -loglevel error -bitexact -i "$flac" -c:a pcm_s16le -ar 44100 -ac 1 "$wav"
rm -f "$flac"

sr=$(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of default=nw=1:nk=1 "$wav")
ka=$(ffprobe -v error -select_streams a:0 -show_entries stream=channels    -of default=nw=1:nk=1 "$wav")
[ "$sr" = "44100" ] && [ "$ka" = "1" ] || fehler "$wav ist $sr Hz / $ka Kanal, erwartet 44100 Hz / mono."

# --- 4. Audiodaten gegen die Vertonung ---------------------------------
# Ein Byte-Vergleich der ganzen WAV taugt hier nicht: der Kopf traegt je
# nach Schreiber unterschiedliche Zusatzfelder. Geprueft werden die
# Samples selbst.
if [ -n "$soll_pcm" ]; then
    ist_pcm="$(pcm "$wav")"
    [ "$ist_pcm" = "$soll_pcm" ] || fehler "Audiodaten weichen ab ($ist_pcm != $soll_pcm)."
    echo "[4/4] Audiodaten bitgleich zur Vertonung ✓  PCM-MD5 $ist_pcm"
else
    echo "[4/4] HINWEIS: kein pcm_md5 im Manifest — vor dieser Fassung gesichert." >&2
fi

echo
echo "Fertig: $wav  ($(stat -c%s "$wav") B, $sr Hz, mono)"
echo
echo "Weiter ohne TTS-Kosten:"
echo "  python3 produktion/pipeline/render.py $video --nur 3 5"
