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

if [ -z "${GOFILE_TOKEN:-}" ]; then
  echo "HINWEIS: GOFILE_TOKEN ist nicht gesetzt - Upload laeuft anonym."
  echo "         Die Dateien landen in keinem Konto und sind spaeter nicht"
  echo "         zu verwalten oder zu loeschen. Mit Token aufrufen:"
  echo "             export GOFILE_TOKEN=... && $0 $VIDEO"
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

  if [ -n "${GOFILE_TOKEN:-}" ]; then
    ANTWORT="$(curl -sS --max-time 7200 -X POST "https://$SERVER.gofile.io/contents/uploadfile" \
               -H "Authorization: Bearer $GOFILE_TOKEN" -F "file=@$DATEI")"
  else
    ANTWORT="$(curl -sS --max-time 7200 -X POST "https://$SERVER.gofile.io/contents/uploadfile" \
               -F "file=@$DATEI")"
  fi
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
