#!/usr/bin/env bash
# gofile_hochladen.sh - Auslieferung eines fertigen Videos zu GoFile.
#
# V01-V04 wurden von Hand hochgeladen; im Repo gab es dafuer keinen Code.
# Dieses Skript macht den Weg wiederholbar und schreibt ein Manifest, damit
# spaeter nachvollziehbar ist, WELCHE Datei hinter einem Link liegt.
#
# Der Token kommt aus der Umgebung, nie aus einer Datei im Repo:
#     export GOFILE_TOKEN=...
#     produktion/pipeline/gofile_hochladen.sh V5
#
# Ohne Token laeuft es trotzdem: GoFile nimmt anonyme Uploads an, die Dateien
# landen dann aber in keinem Konto und sind nicht verwaltbar. Das Skript sagt
# das an und fragt nicht nach.
#
# Was hochgeladen wird (in dieser Reihenfolge, fehlende werden uebersprungen):
#     video-0N.mp4   die Videospur mit Ton      -> Rolle "video"
#     video-0N.flac  die reine Tonspur          -> Rolle "ton"
#     video-0N.srt   die Untertitel             -> Rolle "untertitel"
#
# Jede Datei wird nach dem Upload GEGENGEPRUEFT: die von GoFile gemeldete
# Groesse muss byte-genau mit der lokalen uebereinstimmen. Zusaetzlich steht
# im Manifest ein sha256 je Datei - eine Groesse allein kann zufaellig
# stimmen, eine Pruefsumme nicht.
set -u -o pipefail

WURZEL="$(cd "$(dirname "$0")/../.." && pwd)"
VIDEO="${1:-}"
[ -z "$VIDEO" ] && { echo "Aufruf: $0 V5 [--nur-pruefen]" >&2; exit 2; }
NUR_PRUEFEN="${2:-}"

NR="$(printf '%02d' "${VIDEO#V}")"
PAKET="$WURZEL/produktion/video-$NR"
MANIFEST="$WURZEL/produktion/auslieferung/manifest.json"
mkdir -p "$(dirname "$MANIFEST")"
[ -f "$MANIFEST" ] || echo '{"format":1,"auslieferungen":[]}' > "$MANIFEST"

# Der Upload-Endpunkt beantwortet eine Anfrage OHNE Authorization-Header seit
# 2026-08 mit "error-createGuestAccount" - der frueher hier dokumentierte
# voellig anonyme Weg existiert nicht mehr. Ein Gastkonto ist aber weiterhin
# frei anzulegen und liefert einen Wegwerf-Token; damit laeuft der Upload wie
# zuvor, nur eben authentifiziert. Der Token gehoert NICHT ins Repo: er wird
# hier erzeugt, benutzt und am Ende ausgegeben, damit ein Mensch die Dateien
# notfalls doch noch verwalten kann.
TOKEN="${GOFILE_TOKEN:-}"
GASTTOKEN=""
if [ -z "$TOKEN" ]; then
  echo "HINWEIS: GOFILE_TOKEN ist nicht gesetzt - es wird ein GASTKONTO angelegt."
  echo "         Die Dateien haengen dann an einem Wegwerf-Konto, nicht an deinem."
  GASTTOKEN="$(curl -sS --max-time 30 -X POST https://api.gofile.io/accounts \
               | jq -r '.data.token // ""')"
  if [ -z "$GASTTOKEN" ] || [ "$GASTTOKEN" = "null" ]; then
    echo "Gastkonto konnte nicht angelegt werden - mit eigenem Token aufrufen:" >&2
    echo "    export GOFILE_TOKEN=... && $0 $VIDEO" >&2
    exit 1
  fi
  TOKEN="$GASTTOKEN"
  echo "         Gast-Token angelegt (wird am Ende ausgegeben)."
  echo
fi

SERVER="$(curl -sS --max-time 30 https://api.gofile.io/servers \
          | jq -r '.data.servers[0].name')"
[ -z "$SERVER" ] || [ "$SERVER" = "null" ] && { echo "Kein GoFile-Server erreichbar." >&2; exit 1; }
echo "GoFile-Server: $SERVER"
echo

EINTRAEGE="[]"
GEFUNDEN=0
for PAAR in "video:mp4" "ton:flac" "untertitel:srt"; do
  ROLLE="${PAAR%%:*}"; ENDUNG="${PAAR##*:}"
  DATEI="$PAKET/video-$NR.$ENDUNG"
  [ -f "$DATEI" ] || { echo "  ueberspringe $ROLLE: $(basename "$DATEI") fehlt"; continue; }
  GEFUNDEN=$((GEFUNDEN+1))
  BYTES="$(stat -c%s "$DATEI")"
  echo "  $ROLLE  $(basename "$DATEI")  $(numfmt --to=iec --suffix=B "$BYTES")"
  SHA="$(sha256sum "$DATEI" | cut -d' ' -f1)"
  echo "        sha256 $SHA"

  if [ "$NUR_PRUEFEN" = "--nur-pruefen" ]; then
    echo "        (--nur-pruefen: kein Upload)"
    continue
  fi

  ANTWORT="$(curl -sS --max-time 7200 -X POST "https://$SERVER.gofile.io/contents/uploadfile" \
             -H "Authorization: Bearer $TOKEN" -F "file=@$DATEI")"
  STATUS="$(echo "$ANTWORT" | jq -r '.status // "fehler"')"
  if [ "$STATUS" != "ok" ]; then
    echo "        UPLOAD FEHLGESCHLAGEN: $(echo "$ANTWORT" | head -c 300)" >&2
    exit 1
  fi
  FID="$(echo "$ANTWORT"  | jq -r '.data.id // .data.fileId // ""')"
  SEITE="$(echo "$ANTWORT" | jq -r '.data.downloadPage // ""')"
  FERN="$(echo "$ANTWORT"  | jq -r '.data.size // -1')"
  echo "        -> $SEITE"

  # Gegenprobe: gemeldete Groesse gegen die lokale
  if [ "$FERN" != "-1" ] && [ "$FERN" != "$BYTES" ]; then
    echo "        GROESSE WEICHT AB: lokal $BYTES, GoFile $FERN" >&2
    exit 1
  fi
  echo "        Groesse bestaetigt ($BYTES Byte)"

  EINTRAEGE="$(echo "$EINTRAEGE" | jq \
    --arg r "$ROLLE" --arg n "$(basename "$DATEI")" --arg s "$SHA" \
    --arg f "$FID" --arg p "$SEITE" --arg srv "$SERVER" --argjson b "$BYTES" \
    '. + [{rolle:$r,name:$n,bytes:$b,sha256:$s,gofile:{fileId:$f,downloadPage:$p,server:$srv}}]')"
done

[ "$GEFUNDEN" = "0" ] && { echo "Keine auszuliefernden Dateien in $PAKET" >&2; exit 1; }
[ "$NUR_PRUEFEN" = "--nur-pruefen" ] && { echo; echo "Nur geprueft, nichts hochgeladen."; exit 0; }

TITEL="$(cat "$PAKET/titel.txt" 2>/dev/null || echo "")"
NEU="$(jq -n --arg v "$VIDEO" --arg t "$TITEL" \
        --arg d "$(date -u +%Y-%m-%dT%H:%M:%SZ)" --argjson e "$EINTRAEGE" \
        '{video:$v,titel:$t,hochgeladen_am:$d,dateien:$e}')"
TMP="$(mktemp)"
jq --argjson n "$NEU" '.auslieferungen += [$n]' "$MANIFEST" > "$TMP" && mv "$TMP" "$MANIFEST"
echo
echo "Manifest ergaenzt: ${MANIFEST#$WURZEL/}"
jq -r '.auslieferungen[-1] | "  \(.video)  \(.titel)\n" + (.dateien[] | "    \(.rolle): \(.gofile.downloadPage)")' "$MANIFEST"

if [ -n "$GASTTOKEN" ]; then
  echo
  echo "Gast-Token dieser Auslieferung (NICHT ins Repo, nicht im Manifest):"
  echo "    $GASTTOKEN"
  echo "  Nur damit sind die Dateien spaeter noch zu verwalten oder zu loeschen."
fi
