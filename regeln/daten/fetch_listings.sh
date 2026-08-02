#!/usr/bin/env bash
# Kanal-Listings (flach, ohne Download) mit Pausen gegen 429.
set -u
cd "$(dirname "$0")/listings"
declare -A CH=(
  [A_HushLittleLamb]=UCBnoLXdJ9tIR-8vjSdgiYAw
  [B_RestInGrace]=UCiolk5zOhJjJta3iS6HJDCw
  [C_TheBibleSacred]=UC0cy4w3yoMAFirr2-T8SO6w
  [D_GodMessageToday]=UCUiIE3C3I3bUX0Tlg80bsVQ
  [E_QuietMind]=UCR1FgO0Oycryt1WWp8oi4Uw
  [F_GodsPeacefulSleep]=UC-5_ygyeDFcaNX8EOP72dKA
  [G_TheSilentShepherd]=UCMGv7-T-3VC8ABo711wiPzw
  [H_TimeForGod]=UC-pEU9jgYXwic0fA1Q6U0GQ
  [I_DeepRestBible]=UCAz3nyKbrOFqaETDSqTTyHg
  [J_JesusLovesYou]=UCY9b-no-diXY4sVkU2G9CHA
)
for K in "${!CH[@]}"; do
  ID="${CH[$K]}"
  for TAB in videos shorts; do
    OUT="${K}_${TAB}.jsonl"
    [ -s "$OUT" ] && continue
    timeout 180 /usr/local/bin/yt-dlp --js-runtimes node --flat-playlist --dump-json \
      "https://www.youtube.com/channel/${ID}/${TAB}" > "$OUT" 2>"${OUT}.err" \
      && echo "OK  $K $TAB $(wc -l < "$OUT")" \
      || echo "ERR $K $TAB $(tail -c 120 "${OUT}.err" | tr '\n' ' ')"
    sleep 8
  done
done
echo "LISTINGS FERTIG"
