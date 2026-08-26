# Workflow-Gates

Zwei Haltepunkte im Produktionsablauf. Gate 1 vor jedem Rendering, Gate 2
einmalig nach Video 4. Sie fassen zusammen, was ohnehin in
`produktion/pipeline/` geprüft wird — hier steht es an einer Stelle und mit
Begründung, damit kein Lauf startet, dessen Ergebnis danach ohnehin
verworfen werden müsste.

Bindende Quellen: [`formel/video-formel.md`](../formel/video-formel.md) (v2.2) ·
[`regeln/erfolgsregeln.md`](../regeln/erfolgsregeln.md) ·
[`formel/thumbnail-checkliste.md`](../formel/thumbnail-checkliste.md)

> **Stand 2026-08-23: Gate 2 ist gelaufen.** Die Ergebnisse stehen unten und sind in
> die drei bindenden Quellen eingearbeitet. **Gate 1 hat dadurch zwei neue Prüfungen
> bekommen (1.13 Korpusart, 1.14 Eigenname im Titel)** — beide gelten ab V05.

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
| 1.2 | **Titelähnlichkeit** | < 50 % gemeinsame inhaltstragende Wörter mit **jedem** Gewinnertitel — **und nicht näher an einem Kopisten-Titel als am nächsten Gewinner** | Formel §1: Kanal F kopierte wörtlich → 18 Views; Kanal C baute Mashups → 17 Views | `produktion/titel_pruefung.py` (Bestand), `produktion/titel_kandidaten.py` (neue Titel, misst zusätzlich gegen Kopisten und den eigenen Katalog). **Auflösung beachten:** ein Wort wiegt 9–33 Prozentpunkte, Unterschiede darunter sind kein Signal — siehe §10 „Auflösungsgrenze". |
| 1.3 | **Titelanker** | einer der 13 belegten Anker | Formel §10 („diese zuerst verwenden"); die 7 abgeleiteten sind ausdrücklich ungeprüft | von Hand gegen §10 |
| 1.4 | **Thumbnail: Wörter** | höchstens 4 | Checkliste — **gesetzter Spielraum, nicht gemessen**: keine Messdatei führt eine Wortzahl je Feld-Thumbnail; beobachtet sind bei A und B nur 2- und 3-Wort-**Zeilen** (`thumbnail_forensik.json`). Eine Zeile ist kein Bild — 2 + 2 sind vier Wörter. | `thumbnail.py` |
| 1.5 | **Thumbnail: Versalhöhe** | ≥ 11,5 % der Bildhöhe (≥ 125 px bei 1080p) | Checkliste | `thumbnail.py` |
| 1.6 | **Thumbnail: Kontrast** | ≥ 10 : 1 zum direkten Hintergrund | Checkliste | `thumbnail.py` |
| 1.7 | **Thumbnail: Serienmotiv** | gleiches Motiv wie die letzten Uploads | Formel §5 (B: 13/13); trägt die Kanalidentität, nicht den Einzeltreffer | Sichtprüfung |
| 1.8 | **160×90-Kontrolle** | Text in einer Sekunde erfassbar, Lichtquelle erkennbar | Checkliste | Sichtprüfung am Handy |
| 1.9 | **Sprechbeginn** | Sekunde 0–3, kein Musikintro | Formel §3 PFLICHT (n=24; Gewinner 0,1–3,1 s) | `vorlauf_s` in `config.md`, nachgemessen in `schritt6_srt.py` (erste Kachel) |
| 1.10 | **CTA** | höchstens 2, beide in den ersten 60 s | Formel §3 (Gewinner 0–2, tote Kanäle 4–7) | `schritt1_text.py` zählt sie; Zeitpunkt aus der Rahmen-Wortzahl |
| 1.11 | **Pegelabstand** | Stimme ≥ 12 dB über dem Bett, über Sprachabschnitte gemessen — **in der Mono-Summe UND je Kanal, beide Werte** | Formel §5b: „Stimme in 6/6 Fällen klar über dem Bett" — **qualitativ belegt, die Zahl 12 ist abgeleitet**. Zwei Werte statt einem seit 2026-08-23: `qa_mix.json` maß nur den Mono-Downmix und meldete 12,0 dB, wo am Kopfhörer 6,8 dB standen (V01–V04). | `schritt3_bett.py`, meldet `abstand_eingehalten_mono` und `abstand_eingehalten_je_kanal` |
| 1.12 | **Übersetzung** | WEBBE, kein „Yahweh" im Text | Formel §4 | `schritt1_text.py` bricht sonst ab |
| 1.13 | **Korpusart** | Erzählanteil ≥ 80 %, und der größte Block ist selbst Erzählung | **M8** (eigene Kanaldaten Gate 2, 2026-08-23: Endretention V3 14,4 % gegen V2 2,4 %, Faktor 6) | `produktion/korpus_pruefung.py` |
| 1.14 | **Eigenname im Titel** | Pflicht, in **jedem** Video (Buch- oder Evangelienname) | Formel §1. **Konvention, kein belegter Hebel** — der Wirkmechanismus ist ungeklärt, siehe §1 „die sparsamere Erklärung". Die Prüfung steht hier, weil sie nichts kostet und die Serie einheitlich hält. | von Hand gegen §1 |

| 1.15 | **Titellänge** | unter **70 Zeichen**, und der Eigenname beginnt vor Zeichen **60** | **Gesetzte Grenze, nicht gemessen.** Belegt ist nur der Anlass: Gate 2 (2026-08-23) hat **68 % der Aufrufe am Handy** gemessen, TV und Handy zusammen 80 %. In der Vorschlagsleiste am Handy bricht der Titel bei rund 60 Zeichen ab — *wo genau*, ist nicht gemessen und hängt an Gerät und Schriftgröße. Steht der Eigenname jenseits der Kante, trägt er die kontextliche Zuordnung nicht mehr, auf der 1.14 beruht. SOLL, nicht MUSS. | `produktion/titel_kandidaten.py` meldet Länge und Position |
**1.1 und 1.11 sind Sonderfälle:** Die Korpuslänge lässt sich erst nach dem
Textbau prüfen (Schritt 1), der Pegelabstand erst nach der Mischung
(Schritt 3). Beide liegen aber **vor** dem teuren Teil — TTS und Montage —
und beide brechen die Pipeline hart ab, wenn sie reißen.

### Audit 2026-08-23: welche Prüfung deckt nur einen Wiedergabefall ab?

Anlass war 1.11 — die Prüfung maß den Mono-Downmix und meldete 12,0 dB, wo am
Kopfhörer 6,8 dB standen. Die Frage dahinter gilt für jede Prüfung: **wir messen den
Master, der Zuschauer bekommt etwas Umgerechnetes.** Alle Prüfungen daraufhin
durchgegangen:

| # | misst | was beim Zuschauer ankommt | Befund |
|---|---|---|---|
| **1.11** | Mono-Downmix des Betts | Mono (80 %) **und** je Kanal (20 %) | **Echte Lücke. Behoben** — prüft jetzt beide, beide ≥ 12 dB. |
| 1.5 | Versalhöhe in % der Bildhöhe | jede Anzeigegröße | Keine Lücke: ein Prozentwert skaliert mit. |
| 1.6 | Kontrast im 1920×1080-Master | Feed-Größe 160×90 | **Geprüft, keine Lücke.** Gemessen an allen fünf gebauten Thumbnails: 0,9–3,2 % Kontrastverlust beim Verkleinern. Der Grund ist 1.5 — bei 11,5 % Versalhöhe sind die Striche auch bei 160×90 mehrere Pixel breit. |
| Peak (`peak_max_dbfs`) | je Kanal, über beide | Mono-Summe kann nicht lauter sein | Keine Lücke: (L+R)/2 ≤ max(\|L\|,\|R\|), je Kanal ist der konservative Fall. |
| 1.1, 1.2, 1.3, 1.4, 1.7, 1.9, 1.10, 1.12, 1.13, 1.14 | Text, Titel, Wortzahl, Motiv | unverändert | Kein Wiedergabefall im Spiel. |

**Eine strukturelle Lücke bleibt und ist nicht geschlossen:** Gate 1 prüft das
**Thumbnail** und die **Tonspur**, aber nichts an der **encodierten Videospur**. Ob der
Nachthimmel nach `libx264 -crf 28` auf einem großen Schirm Streifen zeigt, misst keine
Prüfung — das ist dieselbe Fehlerklasse wie 1.11, nur an anderer Stelle: geprüft wird
die Quelle, ausgeliefert wird das Encodat. Der Banding-Test dazu läuft; ob daraus eine
Prüfung 1.15 wird, ist noch nicht entschieden.

**Die zweite Hälfte von 1.2 ist neu (2026-08-23) und stammt aus einem konkreten
Beinahe-Fehler.** Bei der Titelsuche für V05 lag der zunächst empfohlene Kandidat mit
33,3 % gegen den nächsten Gewinnertitel sauber unter der Grenze — aber mit **44,4 %
gegen C's totes Mashup** *„You're tired, I know… Rest to the Gospel of John"* (17 Views).
Er war der Kopie also ähnlicher als dem Original. Das ist genau die Bauform, vor der V3
warnt, und die Prüfung gegen die Gewinner allein sieht sie nicht: *„Zustand, ich weiß…"*
plus *„das Evangelium nach X"* **ist** C's Bauform. Wer nur gegen Gewinner misst,
kann den Kopisten nachbauen, ohne dass eine Zahl anschlägt.

**1.13 und 1.14 kommen vor allem anderen** — sie entscheiden über Korpus und Titel,
also über das, was Schritt 1 überhaupt baut. Sie sind seit 2026-08-23 die einzigen
Gate-1-Prüfungen aus **eigenen** Kanaldaten; alle übrigen stammen aus Fremdkanälen.

**Die 80-%-Schwelle in 1.13 ist gesetzt, nicht gemessen.** M8 trennt Erzählstoff von
Spruchsammlung, sagt aber nichts über die Grenze dazwischen — die eigenen Daten kennen
nur 81,7 % (V05, erfüllt) und 10,2 % (V06 alt, verletzt), dazwischen liegt nichts.
80 % ist die Zahl, die V05 gerade noch durchlässt; sie ist eine Arbeitsgrenze und wird
korrigiert, sobald ein Video dazwischen liegt. `korpus_pruefung.py` meldet immer den
tatsächlichen Prozentsatz mit, damit die Grenze nachvollziehbar bleibt.

**Die Gattungszuordnung steht im Skript, nicht im Kopf.** `korpus_pruefung.py` führt
kapitelweise, welches Material als Erzählung zählt — Jona 2 (Gebet), 2. Samuel 22
(Danklied), Josua 13–21 (Gebietslisten), Exodus 21–23/25–31/35–40 (Recht und
Stiftshütte), Daniel 7–12 (Visionen) zählen ausdrücklich nicht. Wer die Zuordnung für
falsch hält, ändert sie dort und sieht sofort, was das an den Prozentsätzen bewegt.

**Gegenmessung der Umstellung (2026-08-26).** Beide Bett-Artefakte unabhängig
nachgemessen, damit die Behauptung „Variante (e) schließt die Lücke" aus einem
Artefakt kommt und nicht aus einem Bericht:

| `bett_datei` | L == R | Korrelation L/R | Downmix-Verlust | Mono | je Kanal |
|---|---|---|---|---|---|
| `bett_pad_feuer.flac` (V01–V04) | nein | −0,396 | +5,198 dB | 12,00 dB | **6,80 dB** |
| `bett_mono_feuer_leise.flac` (ab V05) | **bitgleich** | +1,000 | **0,000 dB** | 12,00 dB | **12,00 dB** |

Die Umstellung greift also. V01–V04 bleiben betroffen und sind nicht
reparierbar — sie sind veröffentlicht.

**Wenn eine Prüfung reißt:** anhalten und entscheiden, nicht umgehen. Prüfungen
mit Ermessensspielraum sind **1.3** (ein ungeprüfter Anker ist erlaubt, kostet
aber bewusst einen belegten) und **1.15** (die Zeichenzahl ist gesetzt; die
Bedingung, die die Begründung trägt, ist die Position des Eigennamens).

---

## Gate 2 — Feedback-Schleife nach Video 4

**Auslöser:** Video 4 ist veröffentlicht **und** das älteste Video ist
mindestens **14 Tage** alt — **gesetzt, nicht gemessen**: der Fremddatensatz
enthält weder Impressionen noch CTR noch Zeitreihen, eine Reifekurve ist daraus
nicht ableitbar und steht in keiner Messdatei. Nicht früher: YouTube braucht Zeit, bis
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
| **Traffic-Quellen** | Reichweite | Vorgeschlagene Videos vs. Suche vs. Startseite — entscheidet, ob Titel-Keywords oder Thumbnail wichtiger sind. **Vorsicht beim API-Label `SUBSCRIBER`: es bedeutet Startseite und Abo-Feed, NICHT Aufrufe durch Abonnenten.** |
| **Zuschauer nach Uhrzeit** | Publikum | Für den Upload-Zeitpunkt; im Fremddatensatz nicht ermittelbar. |
| **Gerätetyp** | Publikum | Entscheidet, ob stereo oder mono abgehört wird — und wie lange. Im Fremddatensatz nicht ermittelbar. **2026-08-23 nachgetragen, weil er beim ersten Durchgang gefehlt hat und den größten Einzelbefund enthielt.** |

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

### Durchgeführt am 2026-08-23 — was herauskam

**Datengrundlage:** *The Nightly Word* (`UCai4rcN45WKqNvPdSJGADPg`), 25.07.–22.08.2026,
4 Videos, 151 Aufrufe, 69,4 Wiedergabestunden, 2 Abonnenten, 5.535 Impressionen,
CTR 2,71 %. Rohwerte: [`regeln/daten/gate2_eigene_kanaldaten.json`](../regeln/daten/gate2_eigene_kanaldaten.json).

Die vier geplanten Entscheidungen, der Reihe nach — und was tatsächlich entschieden
werden konnte:

| # | Geplant | Ergebnis |
|---|---|---|
| 1 | CTR-Vergleich der 4 Titel, ggf. eigene Spalte in §10 | **Keine eigene Spalte.** 5.535 Impressionen tragen keine CTR-Aussage. Der belastbare Teil ist ein Ausschluss: V3 hat den zweitschlechtesten CTR (1,82 %) **und** 3.130 der 5.535 Impressionen — ein Titel, der zieht, müsste sich zuerst im CTR zeigen, also zieht dieser nicht. Suche scheidet ebenfalls aus (0 Suchaufrufe). Der **Eigenname ist trotzdem Pflicht** in jedem Titel (§1), aber als billige Konvention; der Wirkmechanismus bleibt ungeklärt. |
| 2 | Thumbnail A gegen B | **Nicht durchführbar** — im Zeitraum lief je Video genau eine Variante. Bleibt offen. Neu ist die *Engpass*-Antwort: Thumbnails sind bei diesem Kanalstand **nicht** der Engpass (`formel/thumbnail-checkliste.md`, vorläufiges NEIN). |
| 3 | Absprungstelle in den ersten 60 s, Hook (a) gegen (b) | **Nicht auflösbar.** YouTubes Messpunkte sind 2-Minuten-Blöcke; der Abfall (V3 100 %→40 %, V2 100 %→29 % zwischen Minute 2 und 4) trifft Hook und Eingangsgebet gemeinsam. Als **Beobachtung** in Formel §9 aufgenommen, **nicht** als Regel. |
| 4 | Laufzeit — bricht die Kurve früh ab, ist §2 zu lang | **§2 bleibt unverändert.** Die Kurve bricht nicht wegen der Länge ab: V3 hält bei derselben Laufzeit 14,4 % Endretention, V2 nur 2,4 %. Nicht die 3,5 Stunden sind das Problem, sondern **womit sie gefüllt sind.** |

**Der eigentliche Befund stand nicht auf der Liste:** die **Korpusart**. Erzählstoff
schlägt Spruchsammlung um Faktor 6 in der Endretention, und V3 allein trägt 80 % der
Kanal-Wiedergabezeit. Daraus wurde **M8** in `regeln/erfolgsregeln.md` — die erste
Regel des Repos aus eigenen Daten — und Gate-1-Prüfung 1.13.
**M8 ist damit der einzige an eigenen Daten belegte Hebel dieser Auswertung.** Alles
andere, was Gate 2 hergegeben hat, sind Ausschlüsse (nicht die Suche, nicht die
Klickrate, nicht die Laufzeit) oder Konventionen (Eigenname). Wer nach der Auswertung
eine Sache anders macht, macht den Korpus anders.

**Zusätzlich entschieden:** Die **Kadenz bleibt bei 5 Tagen** (M1), obwohl eine
Fremdkohorte für häufigeres Hochladen spricht. Grund: V05–V08 sollen den
Korpuswechsel als einzige geänderte Variable testen.

**Nicht entschieden, obwohl an Gate 2 gebunden:** die Wahl zwischen den beiden
Kanalbannern (`produktion/motive/README.md`). Gate 2 liefert Video-Impressionen,
aber keine Kanalseiten-Conversion — und 2 Abonnenten sind keine Grundlage. Bleibt
offen.

### Nachtrag 2026-08-23 — der Gerätetyp fehlte, und er trug den größten Befund

Die Leseliste oben kannte den Gerätetyp nicht. Nachgereicht:

| Gerät | Anteil Aufrufe | Ø Sehdauer | Anteil Wiedergabezeit |
|---|---|---|---|
| Handy | 68 % | 23,0 min | 56,7 % |
| **Fernseher** | **12 %** | **70,4 min** | **30,6 %** |
| Tablet | 11 % | — | zusammen 12,7 % |
| Desktop | 7 % | — | |

*Kreuzprobe: 12 % von 151 Aufrufen sind 18,1 Aufrufe × 70,4 min = 1.276 min von
4.164 min Kanal-Wiedergabezeit = 30,6 %. Die Restzeit verteilt sich auf Tablet und
Desktop mit im Mittel 17,4 min je Aufruf.*

**Zwei Dinge folgen daraus:**

1. **Ein TV-Zuschauer ist gut drei Handy-Zuschauer wert.** 70,4 gegen 23,0 Minuten.
   Wiedergabezeit ist die Größe, nach der YouTube ausliefert (siehe Ergebnis 1 oben) —
   damit ist der kleinste Gerätekanal der zweitwichtigste.
2. **Das Publikum hört mono.** Handy und Fernseher zusammen sind 80 % der Aufrufe, und
   beide geben über Handy-, Bluetooth- oder TV-Lautsprecher aus. Der Mono-Summenfall ist
   der Regelfall. Das hat einen konkreten Fehler im Klangbett aufgedeckt — ausgeführt in
   `formel/video-formel.md` §5b: der 240-Sample-Versatz der Stereobreite erzeugt in Mono
   einen Kammfilter, der die Quinte des Pads um 10,9 dB unter den Bauplan drückt.

**Diese Zeile ist der eigentliche Ertrag des Nachtrags:** Gate 2 hat beim ersten
Durchgang vier Kennzahlen gelesen und den Gerätetyp nicht. Die Leseliste oben ist
entsprechend ergänzt, damit das beim nächsten Messpunkt nicht wieder passiert.

### Was danach passiert

- Jede Korrektur wird **in die Dokumente geschrieben**, mit eigener Fallzahl
  und Datum, und markiert, welcher Fremdbefund sie ersetzt.
- Erst danach werden Videos 5–8 gerendert. Vier Videos sind die kleinste
  Menge, aus der sich überhaupt ein Vergleich ziehen lässt — und n=4 bleibt
  eine schwache Grundlage. Was nicht deutlich ist, bleibt unverändert.

**Nächster Messpunkt (festgelegt 2026-08-23):** nach V08, unter denselben
Auslösebedingungen wie Gate 2 (jüngstes Video veröffentlicht, ältestes ≥ 14 Tage alt).
Gemessen wird dann gegen das **Prüfkriterium von M8** — Endretention der vier
Erzählstoff-Videos gegen die 2,4 % von V02. Liegt sie nicht deutlich darüber, wird M8
gestrichen. Erst danach kommen die drei vertagten Fragen an die Reihe, einzeln und in
dieser Reihenfolge: **Kadenz** (M1) · **gekürzte Rahmung** (Formel §9) · **Hook-Variante
(a) gegen (b)** (`videos-01-08.md`). Eine Variable pro Runde.

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
**„129 px = 11,94 %"** — als Ergebnis einer Schriftvergrößerung an *Video 04*.
Diese Änderung hat es nie gegeben.
`produktion/video-04/thumbnail_messung.json` steht seit seinem einzigen
Commit (`9fcb2a0`) auf `fontgroesse_px 184` · `versalhoehe_px 125` ·
`versalhoehe_pct 11.57` — identisch zu den vier anderen Thumbnails der
Videos 01–04.

Der Wert wurde ungeprüft übernommen und **zwei Runden lang als Ausgangslage
weiterverwendet**. Der Schaden waren nicht die 4 Pixel. Der Schaden war,
dass zwei Runden auf einer Zahl aufbauten, die für dieses Video nie
gemessen worden war.

> **Nachtrag 2026-08-26 — die Zahl selbst war richtig gedacht.**
> Auf dem Zweig `claude/gate-2-befunde-dokumentieren-47ar4s` (zum Zeitpunkt
> dieses Nachtrags 15 Commits vor `main`, nicht gemergt) ist derselbe Befund
> unabhängig gemacht **und aufgelöst** worden: Commit `db333c4` trennt den
> Zielwert von der Prüfgrenze — `CAP_MIN_PCT = 11.5` bleibt die Grenze aus der
> Checkliste, `CAP_ZIEL_PCT = 11.9` ist der Median der B-Serie (n=13), und
> `ceil(1080 × 11,9 %)` ergibt **genau 129 px = 11,94 %**. Das Thumbnail
> `produktion/video-05/thumbnail_messung.json` trägt diesen Wert dort als
> gemessenes Ergebnis. Die 129 war also keine Erfindung, sondern eine
> Absicht, die zum Zeitpunkt des V04-Berichts noch nicht implementiert war —
> und sie ist inzwischen implementiert.
>
> Der ursprüngliche Grund für 125 px war überdies schlecht: 125 ist
> `ceil(1080 × 11,5 %)`, also 0,8 Pixel Reserve über der eigenen Prüfgrenze.
> Eine Prüfung, die ihr Ergebnis gerade so besteht, prüft nichts.

### Der zweite Fehler: `--all` ist nur so vollständig wie die Refs

Die Prüfung, die diesen Prozessbefund ausgelöst hat, wurde mit
`git log --all -S"129"` gemacht — und meldete „kommt in keiner Version der
Historie vor". Das war falsch. Der Arbeitsbaum war frisch geklont, aber
**vor der Suche wurde nicht `git fetch` ausgeführt**; die Refs kannten den
Zweig mit der V05-Messung nicht. `--all` heißt „alle bekannten Refs", nicht
„alle Refs".

Damit hat das Prüfverfahren denselben Fehler gemacht, den es aufdecken
sollte, nur eine Ebene höher: ein Negativbefund wurde gemeldet, ohne dass
die Quelle vollständig war. **`git fetch --all` gehört vor jede Aussage der
Form „existiert nicht".** Und ein Negativbefund über die Historie muss
dazusagen, gegen welchen Ref-Stand er gilt.

**Die Einordnung des Falls wird dadurch eine andere, und das ist der
eigentliche Ertrag.** Die 129 px waren zunächst als „Meldung ohne Deckung"
geführt — als hätte ein Bericht eine Zahl erfunden. Das trifft nicht zu:
**die Meldung war gedeckt, die Prüfung war unvollständig.** Die Zahl lag
auf einem Zweig, den die Suche nicht kannte.

Das ist der schwerere Fehler von beiden. Eine ungedeckte Meldung fällt beim
nächsten Blick in die Messdatei auf. Eine unvollständige Prüfung *bestätigt*
sich selbst: sie liefert einen sauberen Negativbefund, der wie ein Ergebnis
aussieht, und niemand sucht weiter. Deshalb steht die Vollständigkeit der
Quelle jetzt als Schritt 0 vor allem anderen.

Der Kern der Regel bleibt davon unberührt: **für Video 04 wurde die Zahl nie
gemessen**, und sie wurde trotzdem zwei Runden lang als Ausgangslage
weitergegeben. Eine Kennzahl gilt erst aus einer eingecheckten Messdatei —
und ab jetzt zusätzlich: aus einer Messdatei, die man auch gefunden hätte,
wenn man vollständig gesucht hätte.

### Das Prüfverfahren gehört vor die Meldung, nicht in die Rückfrage

Bevor eine Kennzahl in einen Bericht oder in ein Dokument geht:

0. `git fetch --all` — **zuerst.** Ohne das ist jeder Negativbefund wertlos
   (siehe unten). Danach `git branch -a` und `git log --oneline main..<zweig>`
   für jeden Zweig, den `main` nicht enthält.
1. `git log --oneline --all -- <messdatei>` — gibt es die Datei, und wie oft
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

### Was die erste Anwendung der Regel ergeben hat

Der Befund wurde sofort auf das ganze Repository angewandt:
[`messdatei-audit-2026-08-25.md`](messdatei-audit-2026-08-25.md). 218 Zahlenwerte
geprüft, 150 bestätigt, 59 in der Gegenprüfung gefallen. 37 der bestätigten sind
als bindende Vorgabe weitergegeben. Die drei schwersten — Zahlen ohne jede
Messdatei, die trotzdem als Grenze gelten — sind die Thumbnail-Wortgrenze
(`formel/thumbnail-checkliste.md`), Gate 1.4 und der Gate-2-Auslöser.

### Zweite Anwendung 2026-08-26: der Preis, der nie gefallen ist

Am 2026-08-26 hat dieselbe Regel einen zweiten Fall aufgelöst — und zwar
einen, in dem der Widerspruch bereits als „aus dem Repo nicht entscheidbar"
dokumentiert war.

`produktion/motive/README.md` behauptete, Seedance 1.5 Pro habe für Video 01
**144 Credits** je Vierer-Satz gekostet und der Preis habe sich danach auf 72
halbiert. Die Commit-Nachricht zu genau dem Lauf, der angeblich 72 kostete,
schrieb ihrerseits 144. Bis dahin galt für die Planung der teurere Wert.

Das Transaktionsprotokoll bei Higgsfield reichte am 2026-08-26 wieder weit
genug zurück. Ausgezählt: **fünf** Clipsätze, **fünfmal 4 × −18 = 72**, von
V01 am 2026-08-04 bis V05 am 2026-08-26. Der Preis hat sich nie geändert.
Falsch waren beide 144er — und auch die Erzählung von der Halbierung.

Woher die 144 kamen, ist ebenfalls belegt: die **Vorabpreisauskunft** der API
(`get_cost`) meldet für dieselbe Anfrage 36 Credits je Clip. Unmittelbar
danach wurden 18 abgebucht, gegengeprüft am Guthaben (2397,9 → 2325,9).

**Regel, die daraus folgt und über diesen Fall hinausgeht:** Ein
Vorabpreis, ein Kostenvoranschlag, eine Schätzung des Dienstes ist eine
Absicht. Die Abrechnung ist das Ergebnis. Wer eine Kostenzahl in ein Dokument
schreibt, schreibt das Buchungsdatum dazu — eine Kostenangabe ohne
Buchungsdatum ist keine.

**Und der Teil, der wehtut:** Der Widerspruch stand seit dem 2026-08-26 als
„nicht auflösbar" im Repo, weil die abrufbaren Protokollseiten damals nur bis
2026-08-15 zurückreichten. Das war richtig beobachtet und falsch
abgeschlossen: nicht abrufbar hieß nur „nicht auf der ersten Seite". Die
Auflösung brauchte vier Abrufe mit einem Seitenzeiger. Ein Beleg, den man
nicht auf Anhieb sieht, ist nicht dasselbe wie ein Beleg, den es nicht gibt —
derselbe Fehlertyp wie beim fehlenden `git fetch --all` oben.

### Bekannte Lücke: die Renderwerte sind nicht eingecheckt

`produktion/arbeit/` steht in `.gitignore`. Alle QA-Dateien eines
Renderlaufs — `qa_stimme.json`, `qa_mix.json`, `qa_video.json`,
`qa_srt.json`, `qa_bild.json`, `skript.json` — landen dort und sind nie im
Repository. Damit ist **jeder** Messwert in `produktion/video-0*/upload.md`
und in `produktion/video-01/upload-checkliste.md` maschinell erzeugt, aber
im Repo nicht nachprüfbar.

Diese Werte sind nicht erfunden — sie sind unbelegbar, und nach der Regel
oben gelten sie damit nicht als gemessen.

**Geschlossen ab Video 05 (2026-08-26).** `schritt7_paket.py` schreibt die
Messwerte eines Laufs jetzt als **`produktion/video-0N/qa.json`** neben
`upload.md`: rund 40 Felder aus den Schritten 1–6, ein bis zwei Kilobyte je
Video. Draußen bleiben die großen Zwischenstände — Chunk-Listen, ASR-Wortzeiten,
der Skript-Volltext (steht in `videos-01-08.md` und im SRT), die Kapitelmarken
(stehen in `beschreibung.txt`).

Der Kopf der Datei ist der Teil, der die Fehlerklasse tatsächlich schließt:

| Feld | wofür |
|---|---|
| `commit` | der Stand, auf dem gerendert wurde |
| `arbeitsbaum_sauber` | ob dieser Commit den Lauf überhaupt beschreibt — ein Hash über einem geänderten Baum belegt nichts |
| `config_sha256` | die gelesene `config.md`, gehasht |
| `bett_datei`, `videoquelle`, `stimme_id`, `tts_modell`, `prosody_speed` | die Entscheidungen, die den Lauf prägen |

Damit zeigt ein Messwert auf einen **Stand**, nicht auf eine Sitzung. Die
Tabelle in `upload.md` trägt eine Kopfzeile, die auf `qa.json` verweist.

**Nicht rückwirkend.** Für V01–V04 existiert `produktion/arbeit/` nicht mehr;
ihre Tabellen tragen stattdessen einen Vermerk, dass sie unbelegbar bleiben.
