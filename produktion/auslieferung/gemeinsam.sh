#!/usr/bin/env bash
#
# gemeinsam.sh - geteilte Hilfen der Auslieferungsskripte.
# Wird per `source` eingebunden, nicht direkt aufgerufen.
#
# Aufteilung: die BYTES liegen als Release-Asset (2 GB je Datei, zaehlen
# nicht gegen die Repo-Groesse, Loeschen gibt den Platz wirklich frei).
# Die PRUEFSUMMEN liegen im Repo, je Video eine kleine Manifestdatei.
# Damit ist die Historie klein und trotzdem nachvollziehbar, welches
# Release welche Datei mit welcher Pruefsumme haelt.

AUSL="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WURZEL="$(cd "$AUSL/../.." && pwd)"

fehler() { echo "FEHLER: $*" >&2; exit 1; }

# V4 -> 04
nummer() {
    case "$1" in
        V[0-9]|V[0-9][0-9]) printf '%02d' "${1#V}" ;;
        *) fehler "Video als V1 … V8 angeben, nicht '$1'." ;;
    esac
}

# V4 -> v04
marke() { echo "v$(nummer "$1")"; }

manifest() { echo "$AUSL/video-$(nummer "$1").manifest"; }

werkzeug_pruefen() {
    for t in "$@"; do
        command -v "$t" >/dev/null || fehler "$t fehlt."
    done
}

gh_pruefen() {
    command -v gh >/dev/null || fehler \
"gh fehlt. Die Bytes liegen als Release-Asset, und nur die GitHub-CLI
kann sie hoch- und herunterladen.
  Installieren : https://cli.github.com
  Anmelden     : gh auth login
Ohne gh laufen die Pruefungen dieses Skripts, aber kein Upload."
    gh auth status >/dev/null 2>&1 || fehler "gh ist nicht angemeldet — 'gh auth login'."
}

# Release anlegen, falls es noch keins gibt. Idempotent.
release_sichern() {
    local tag="$1" video="$2"
    if gh release view "$tag" >/dev/null 2>&1; then
        echo "  Release $tag besteht bereits"
    else
        echo "  Release $tag wird angelegt …"
        gh release create "$tag" \
            --title "Video ${video#V} — Tonspur und Video" \
            --notes "Auslieferung Video ${video#V}.

Assets:
- \`stimme-video-$(nummer "$video").flac\` — Tonspur der TTS, verlustfrei.
  Aus ihr sind Mischung und Montage kostenlos wiederholbar.
- \`video-$(nummer "$video").mp4\` — fertige Montage, nur solange zum
  Upload gebraucht. Danach loeschbar; die Tonspur bleibt.

Pruefsummen: \`produktion/auslieferung/video-$(nummer "$video").manifest\`
Zurueckholen: \`produktion/auslieferung/tonspur_zurueck.sh $video\`"
    fi
}

# manifest_setzen <manifestdatei> <assetname> <schluessel> <wert>
manifest_setzen() {
    local d="$1" a="$2" k="$3" w="$4"
    touch "$d"
    # bestehende Zeile fuer (asset, schluessel) entfernen, dann neu anhaengen
    local tmp; tmp="$(mktemp)"
    awk -v a="$a" -v k="$k" '!($1==a && $2==k)' "$d" > "$tmp"
    printf '%-26s %-10s %s\n' "$a" "$k" "$w" >> "$tmp"
    sort -k1,1 -k2,2 "$tmp" > "$d"
    rm -f "$tmp"
}

# manifest_holen <manifestdatei> <assetname> <schluessel>
manifest_holen() {
    [ -f "$1" ] || return 1
    awk -v a="$2" -v k="$3" '$1==a && $2==k {print $3}' "$1"
}

# sha256 einer Datei
sha() { sha256sum "$1" | cut -d' ' -f1; }

# Pruefsumme der rohen PCM-Daten, ohne Containerkopf. Der einzige Wert,
# an dem sich eine Tonspur ueber WAV/FLAC hinweg messen laesst: ffmpeg
# schreibt ein LIST/INFO/ISFT-Feld in den WAV-Kopf, die Samples bleiben
# davon unberuehrt.
pcm() { ffmpeg -v error -i "$1" -f s16le -c:a pcm_s16le - | md5sum | cut -d' ' -f1; }
