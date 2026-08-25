# Workflow-Gates

Zwei Haltepunkte im Produktionsablauf. Gate 1 vor jedem Rendering, Gate 2
einmalig nach Video 4. Sie fassen zusammen, was ohnehin in
`produktion/pipeline/` geprüft wird — hier steht es an einer Stelle und mit
Begründung, damit kein Lauf startet, dessen Ergebnis danach ohnehin
verworfen werden müsste.

Bindende Quellen: [`formel/video-formel.md`](../formel/video-formel.md) ·
[`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md) ·
[`formel/thumbnail-checkliste.md`](../formel/thumbnail-checkliste.md)

---

## Gate 1 — vor dem Rendern

> **Kernregel: Kein Rendering, bevor Titel und Thumbnail stehen.**
>
> Ein Renderlauf kostet rund 35 Minuten Rechenzeit und ~160.000 TTS-Zeichen.
> Titel und Thumbnail entscheiden, ob das Video überhaupt geklickt wird — sie
> sind der billigste Teil und müssen zuerst fertig sein. Wer erst rendert und
> dann den Titel sucht, hat den Anreiz, einen schlechten Titel zu behalten,
> weil das Video schon da ist.

| # | Prüfung | Grenze | Woher | Womit |
|---|---|---|---|---|
| 1.1 | **Korpuslänge** | ≥ 3,0 h; Ziel 3,4–3,8 h | Formel §2: kein Video unter 3 h je über 2.500 Views (n=6), alle 10 Treffer ≥ 3,2 h | `schritt1_text.py` meldet die erwartete Laufzeit |
| 1.2 | **Titelähnlichkeit** | < 50 % gemeinsame inhaltstragende Wörter mit **jedem** Gewinnertitel | Formel §1: Kanal F kopierte wörtlich → 18 Views | `produktion/titel_pruefung.py` |
| 1.3 | **Titelanker** | einer der 13 belegten Anker | Formel §10 („diese zuerst verwenden"); die 7 abgeleiteten sind ausdrücklich ungeprüft | von Hand gegen §10 |
| 1.4 | **Thumbnail: Wörter** | höchstens 4 | Checkliste | `thumbnail.py` |
| 1.5 | **Thumbnail: Versalhöhe** | ≥ 11,5 % der Bildhöhe (≥ 125 px bei 1080p) | Checkliste | `thumbnail.py` |
| 1.6 | **Thumbnail: Kontrast** | ≥ 10 : 1 zum direkten Hintergrund | Checkliste | `thumbnail.py` |
| 1.7 | **Thumbnail: Serienmotiv** | gleiches Motiv wie die letzten Uploads | Formel §5 (B: 13/13); trägt die Kanalidentität, nicht den Einzeltreffer | Sichtprüfung |
| 1.8 | **160×90-Kontrolle** | Text in einer Sekunde erfassbar, Lichtquelle erkennbar | Checkliste | Sichtprüfung am Handy |
| 1.9 | **Sprechbeginn** | Sekunde 0–3, kein Musikintro | Formel §3 PFLICHT (n=24; Gewinner 0,1–3,1 s) | `vorlauf_s` in `config.md`, nachgemessen in `schritt6_srt.py` (erste Kachel) |
| 1.10 | **CTA** | höchstens 2, beide in den ersten 60 s | Formel §3 (Gewinner 0–2, tote Kanäle 4–7) | `schritt1_text.py` zählt sie; Zeitpunkt aus der Rahmen-Wortzahl |
| 1.11 | **Pegelabstand** | Stimme 12 dB über dem Bett, über Sprachabschnitte gemessen — **in beiden Wiedergabefällen** | Formel §5b: „Stimme in 6/6 Fällen klar über dem Bett" — **qualitativ belegt, die Zahl 12 ist abgeleitet** | `schritt3_bett.py` (nur Mono) · `pegel_wiedergabe.py` (Mono **und** Stereo) |
| 1.12 | **Übersetzung** | WEBBE, kein „Yahweh" im Text | Formel §4 | `schritt1_text.py` bricht sonst ab |

**1.1 und 1.11 sind Sonderfälle:** Die Korpuslänge lässt sich erst nach dem
Textbau prüfen (Schritt 1), der Pegelabstand erst nach der Mischung
(Schritt 3). Beide liegen aber **vor** dem teuren Teil — TTS und Montage —
und beide brechen die Pipeline hart ab, wenn sie reißen.

**1.11 hat zwei Werte, nicht einen.** `schritt3_bett.py` mischt stereo, misst
aber mono: `rahmen_datei()` und `rms_db(bett.mean(axis=1))` summieren vorher
L und R. Der Wert in `qa_mix.json` beschreibt deshalb nur die Wiedergabe über
**einen** Lautsprecher. Das Bett hat Stereobreite (`stimmtest/musikbett.py`:
`np.stack([sig, np.roll(sig, 240)])`), L und R sind negativ korreliert, und
die Monosumme löscht einen Teil davon aus — die Stimme dagegen liegt identisch
in beiden Kanälen und summiert verlustfrei. Gemessen
(`produktion/pipeline/qa/pegel_wiedergabe.json`, 2026-08-25):

| Wiedergabefall | Bett | Abstand | gegen Soll 12 dB |
|---|---|---|---|
| **Mono** — Handy, Bluetooth-Box, Smart Speaker | −31,00 dBFS | **12,00 dB** | hält |
| **Stereo** — Kopfhörer | −25,80 dBFS je Kanal | **6,80 dB** | **reißt um 5,20 dB** |

Der Unterschied hängt allein am Bett (Downmix-Verlust +5,20 dB, Korrelation
L/R −0,396) und ist damit für alle Videos gleich, solange `bett_datei`
dieselbe ist. Die vier gerenderten Videos 01–04 sind betroffen. Was daraus
folgt — Bett um 5,2 dB absenken, Bett mono machen, oder 6,8 dB auf Kopfhörern
akzeptieren — ist **nicht entschieden**; `abstand_soll_db` in `config.md`
bleibt bis dahin bei 12,0.

**Wenn eine Prüfung reißt:** anhalten und entscheiden, nicht umgehen. Die
einzige Prüfung mit Ermessensspielraum ist 1.3 (SOLL, nicht MUSS) — ein
ungeprüfter Anker ist erlaubt, kostet aber bewusst einen belegten.

---

## Gate 2 — Feedback-Schleife nach Video 4

**Auslöser:** Video 4 ist veröffentlicht **und** das älteste Video ist
mindestens **14 Tage** alt. Nicht früher: YouTube braucht Zeit, bis
Impressionen und CTR stabil sind, und die ersten Tage werden von der
Abo-Startverteilung verzerrt.

> **Kernregel: Eigene Daten schlagen Fremddaten.**
>
> Alles in `formel/video-formel.md` stammt aus 10 fremden Kanälen — mit
> allen Verzerrungen, die dabei entstehen: nur Views sichtbar, keine
> Impressionen, keine CTR, keine Retention, und die Treffer stammen aus
> genau 2 Kanälen. Sobald eigene Zahlen vorliegen, ersetzen sie die
> Fremdbefunde an jeder Stelle, wo sie sich widersprechen.

### Was gelesen wird (YouTube Studio, je Video)

| Kennzahl | Wo | Wofür |
|---|---|---|
| **Impressionen und Klickrate (CTR)** | Reichweite | Die Größe, die dem ganzen Fremddatensatz fehlt. Erst hier lässt sich Titel und Thumbnail überhaupt bewerten. |
| **Absprungstelle** (Zuschauerbindung) | Interaktion | Wo die Kurve zuerst kippt: in den ersten 30 s (Hook/Stimme) oder im Verlauf (Länge/Monotonie)? |
| **Durchschnittliche Wiedergabedauer** | Interaktion | Bei 3,5 h Laufzeit ist die absolute Minutenzahl aussagekräftiger als der Prozentwert. |
| **Traffic-Quellen** | Reichweite | Vorgeschlagene Videos vs. Suche vs. Startseite — entscheidet, ob Titel-Keywords oder Thumbnail wichtiger sind. |
| **Zuschauer nach Uhrzeit** | Publikum | Für den Upload-Zeitpunkt; im Fremddatensatz nicht ermittelbar. |

### Was daraus entschieden wird

1. **CTR-Vergleich der 4 Titel** — welcher Anker trägt bei *diesem* Kanal?
   Fremdbelegte Anker gegen die eigene CTR stellen. Bei klarem Unterschied:
   §10 um eine eigene Spalte ergänzen.
2. **Thumbnail A gegen B** — falls beide Varianten im Einsatz waren.
   Erst hier ist die offene Frage aus `thumbnail-motive.md` beantwortbar,
   ob das Motiv überhaupt CTR bewegt.
3. **Absprungstelle in den ersten 60 s** — testet Hook-Variante (a) gegen (b)
   und die Stimme. Formel §3 hält ausdrücklich fest, dass ein festes Schema
   **nicht** belegt ist; hier entstehen die ersten echten Daten dazu.
4. **Laufzeit** — bricht die Kurve regelmäßig weit vor Ende ab, ist das
   Zielband 3,4–3,8 h für diesen Kanal zu lang, und §2 wird korrigiert.

### Was danach passiert

- Jede Korrektur wird **in die Dokumente geschrieben**, mit eigener Fallzahl
  und Datum, und markiert, welcher Fremdbefund sie ersetzt.
- Erst danach werden Videos 5–8 gerendert. Vier Videos sind die kleinste
  Menge, aus der sich überhaupt ein Vergleich ziehen lässt — und n=4 bleibt
  eine schwache Grundlage. Was nicht deutlich ist, bleibt unverändert.

---

## Prozessbefund 2026-08-25 — was als „gemessen" gilt

> **Kernregel: Eine Kennzahl gilt erst als gemessen, wenn sie aus einer
> eingecheckten Messdatei stammt — nicht aus einem Bericht.**
>
> Steht ein Wert in einem Sitzungsbericht, aber in keiner Messdatei, ist er
> eine **Absicht**, kein **Ergebnis**. Er wird nicht als Vorgabe
> weitergegeben und nicht in ein Dokument geschrieben.

Dieser Befund steht bei Gate 2, weil er dieselbe Frage beantwortet wie die
Gate-2-Kernregel — *welche Zahl gilt?* — nur eine Stufe davor: „Eigene Daten
schlagen Fremddaten" hilft nicht, solange unklar ist, ob die eigene Zahl
überhaupt eine Messung war.

### Der Fall

Der Sitzungsbericht zu Video 04 meldete eine Thumbnail-Versalhöhe von
**„129 px = 11,94 %"** — als Ergebnis einer Schriftvergrößerung. Die
Vergrößerung hat es nie gegeben.
`produktion/video-04/thumbnail_messung.json` steht seit seinem einzigen
Commit (`9fcb2a0`) auf `fontgroesse_px 184` · `versalhoehe_px 125` ·
`versalhoehe_pct 11.57` — identisch zu allen vier anderen
Thumbnail-Messungen des Kanals. Die Zahlen 129 und 11,94 kommen in keiner
Datei und in keiner Version der Historie vor.

Der Wert wurde ungeprüft übernommen und **zwei Runden lang als Ausgangslage
weiterverwendet**. Der Schaden waren nicht die 4 Pixel. Der Schaden war,
dass zwei Runden auf einer Zahl aufbauten, die nie existiert hat.

### Das Prüfverfahren gehört vor die Meldung, nicht in die Rückfrage

Bevor eine Kennzahl in einen Bericht oder in ein Dokument geht:

1. `git log --oneline -- <messdatei>` — gibt es die Datei, und wie oft
   wurde sie geschrieben?
2. `git show <commit>:<messdatei>` für **jede** Version — stand der Wert je
   drin?
3. `git log -S"<wert>"` über das ganze Repo — taucht die Zahl überhaupt
   irgendwo auf?
4. Dieselbe Kennzahl in **allen** gleichartigen Messdateien nebeneinander
   halten (alle fünf `thumbnail*_messung.json`, alle `qa-V*.json`, alle
   `*_messung.json` unter `produktion/motive/`). Ein Wert, der aus der
   Reihe fällt, ist zuerst verdächtig, nicht zuerst wahr.

Findet dieser Schritt nichts, wird der Wert **als ungemessen gemeldet** —
zusammen mit dem Satz, was fehlt, damit er gemessen werden könnte. Eine
Rückfrage ersetzt die Prüfung nicht; sie kommt erst danach.

### Herkunft mitschreiben

Jede Kennzahl in einem Dokument bekommt die Datei dazu, aus der sie stammt.
Eine Zahl ohne Dateiangabe ist ab hier eine Absicht — egal, wie sicher sie
klingt und wie oft sie schon zitiert wurde.

### Bekannte Lücke: die Renderwerte sind nicht eingecheckt

`produktion/arbeit/` steht in `.gitignore`. Alle QA-Dateien eines
Renderlaufs — `qa_stimme.json`, `qa_mix.json`, `qa_video.json`,
`qa_srt.json`, `qa_bild.json`, `skript.json` — landen dort und sind nie im
Repository. Damit ist **jeder** Messwert in `produktion/video-0*/upload.md`
und in `produktion/video-01/upload-checkliste.md` maschinell erzeugt, aber
im Repo nicht nachprüfbar.

Diese Werte sind nicht erfunden — sie sind unbelegbar, und nach der Regel
oben gelten sie damit nicht als gemessen. Solange die Lücke offen ist, wird
in einem Bericht dazugesagt, dass die Quelle nicht eingecheckt ist. Die
saubere Auflösung wäre, die QA-Dateien eines abgeschlossenen Renderlaufs
neben `upload.md` in `produktion/video-0*/` zu legen; das ist noch nicht
entschieden.
