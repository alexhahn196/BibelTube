# Thumbnail-Motive — Auswertung der 90 Thumbnails und Motiv-Entscheidung

> **Stand 2026-08-04.** Grundlage: alle 90 Thumbnails unter `regeln/daten/thumbs/`
> einzeln gesichtet (nicht nur Dateinamen), dazu die Kontaktbögen
> (`sheet_GEWINNER/VERLIERER/FLOP/MEDIAN`, `zoom_B_figur.png`), die 4 Szenenanalysen
> aus Lauf 2 und die 11 multimodalen Videostichproben aus Lauf 1
> (`teardown/produktions-spec.md` Abschnitt d).
> Vollständiges Inventar maschinenlesbar: `regeln/daten/motiv_inventar.json`
> (je Thumbnail: Motiv, Lamm, Feuer, Gesicht, Blickkontakt, Tageszeit, Farbe,
> Warmlicht, Text, Views, Views/Kanalmedian).
>
> **Stichproben-Vorbehalt:** Für C–J liegen je Kanal nur die 5 besten und 5
> schlechtesten Videos vor (A und B: nur Gewinner). Quervergleiche über Kanäle
> hinweg sind dadurch verzerrt — die sauberen Tests sind (1) die Treffer-Menge
> selbst und (2) der Best-gegen-Worst-Vergleich **innerhalb** eines Kanals.

---

## 1. Motiv-Inventar (Aufgabe 1)

Kategorien nach Sichtung, Anzahl über alle 90:

| Kategorie | Kürzel | n | Beschreibung |
|---|---|---|---|
| Jesus schlafend/liegend | `js` | 41 | meist mit Lamm und Feuer, gemalte Nachtszene |
| Jesus frontal, Blickkontakt | `jfront` | 17 | „God-Message"-Porträt, Text in Blockversalien |
| Jesus sitzend (Augen zu/gesenkt) | `jsit` | 11 | Einzelszene, kein Blickkontakt |
| Jesus stehend | `jstand` | 5 | Porträt/Ganzfigur, teils mit Lamm |
| Jesus ruhend, wach zurückgelehnt | `jr` | 4 | Variante des Schlafmotivs |
| Jesus mit Kind | `jchild` | 2 | E: wiegend bzw. zum schlafenden Kind gebeugt |
| Jesus am Bett e. Schlafenden (innen) | `jbed` | 2 | Schlafzimmer-Szene |
| andere Figur (ohne Jesus) | `fig` | 2 | betende Frauen; Schläfer an Kirche |
| Historie ohne Jesus | `hist` | 2 | Babylon-Tor; Pestszene |
| Jesus lehrt Menge | `jteach` | 1 | |
| Erscheinung im Wohnraum | `japp` | 1 | |
| Collage | `collage` | 1 | Geburt–Kreuz–Grab |
| Ort ohne Figur | `ort` | 1 | Atlantis-Fantasiestadt |

Querschnitt: Jesus im Bild 85/90 · Gesicht sichtbar 88/90 · **Blickkontakt 18/90** ·
Nacht 66/90 · warme Lichtquelle 79/90 · Text im Bild 75/90 · Lamm 44/90 · Feuer 46/90.

Die Nische malt fast ausnahmslos Jesus selbst. Ein schlafender *gewöhnlicher*
Mensch als Hauptmotiv kommt in 90 Thumbnails praktisch nicht vor (nur als
Nebenfigur in den Verlierer-Bettszenen und bei E's Kind-Motiven).

---

## 2. Was mit Erfolg korreliert (Aufgabe 2)

### Die Treffer (>30.000 Views): n=10, ausschließlich A und B

| Merkmal | Befund |
|---|---|
| Motiv | `js` 6 · `jsit` 3 · `jr` 1 — **alle 10: Jesus ruht in gemalter Szene** |
| Blickkontakt | **0/10** |
| Gesicht sichtbar | 10/10 — aber Augen zu oder gesenkt, gemalt, nie fotorealistisches Frontalporträt |
| Lamm | 9/10 (fehlt nur bei A 184K) |
| Feuer | 8/10 (fehlt bei A 184K und dem SW-Stich 47K) |
| Nacht | 10/10 |
| warme Lichtquelle | 9/10 (fehlt nur beim Schwarzweiß-Stich, 47K) |
| Text im Bild | 6/10 (B 4/4, A 2/6) — Text ist offenkundig kein Muss |
| Palette | 9/10 tiefes Blau + Gold/Orange; 1/10 komplett schwarzweiß (47K) |

**Wichtigste Einschränkung: die 10 Treffer stammen aus genau 2 Kanälen.** Das
Motiv-Signal ist von den Kanälen A/B nicht trennbar.

### Die Gegenprobe entscheidet: dasselbe Motiv trägt tote Kanäle nicht

- **C**: 8/10 Thumbnails mit dem Gewinnermotiv (schlafender Jesus + Lamm + Feuer,
  gemalt, kompetent ausgeführt) — bestes Video **113 Views**.
- **F**: 10/10 Gewinnermotiv in fotorealistischer Variante, sogar mit A's
  Textzeilen („Time To Sleep") — bestes Video **23 Views**.
- Kontrolle auf Bildebene: `zoom_B_figur.png` zeigt B's Figur bei 166.000 und
  bei 911 Views praktisch identisch.

**→ Das Motiv erklärt Kanalerfolg nicht.** 20 Thumbnails bei C+F tragen das
Treffer-Motiv und liegen alle unter 113 Views. Das deckt sich mit der
Thumbnail-Forensik (B-Thumbs bei 166K und 140 Views identisch).

### Der saubere Test: Best gegen Worst innerhalb der Kanäle

| Kanal | Befund (je 5 BEST / 5 WORST) |
|---|---|
| C, D, F | Motivverteilung in BEST und WORST **identisch** — kein Motivsignal |
| G | Innenraum-Szenen (`jbed` 2×, `japp` 1×) **nur** in WORST (16–28 Views) |
| E | BEST 5/5 Szenen-Jesus ohne Blickkontakt · WORST 5/5 frontal/stehend/Frauenfiguren |
| H | WORST 4/5 frontal; der Kanal-Ausreißer (27.000 = **519× Kanalmedian**, stärkster normierter Wert des Datensatzes) ist ein **sitzender Jesus in Landschaft ohne Blickkontakt** |

### Motive, die ausschließlich bei Verlierern vorkommen

| Motiv/Bauform | n | bestes Ergebnis | Vorkommen |
|---|---|---|---|
| Bett-/Innenraumszene (`jbed`, `japp`) | 3 | 28 Views | nur G WORST |
| Frontal-Jesus mit Blickkontakt | 18 | 0 Treffer; kanal-normiert Median 0,68 (ohne Blickkontakt: 1,03) | D 8, H 7, G 2, E 1 |
| Alarm-Design (rote Versalien, URGENT, Pfeile) | 3 | 142 Views | D, H |
| Klick-Appelle im Bild („DON'T SKIP", „DON'T CLICK AWAY", „I AM BEGGING") | 4 | 54 Views | D, H |
| weibliche Hauptfiguren | 1 | 52 Views | E WORST |
| Esoterik-Ästhetik (Lotus, Regenbogen-Aura) | 2 | 261 Views | E |

Vorbehalt beim Frontal-Befund: frontal ist der Hausstil der God-Message-Kanäle
D/H — innerhalb von D ist frontal bestes **und** schlechtestes Video. Das ist
also eher ein Kanaltyp-Signal als ein bewiesener Bildhebel. Aber: in 10 Treffern
kommt es nicht ein einziges Mal vor.

### Merkmale kanal-normiert (Median Views/Kanalmedian, alle 90)

| Merkmal | mit | ohne |
|---|---|---|
| Feuer | 1,21 (n=46) | 0,71 (n=44) |
| warme Lichtquelle | 1,07 (n=79) | 0,41 (n=11) |
| Text im Bild | 1,00 (n=75) | 0,68 (n=15) |
| Blickkontakt | 0,68 (n=18) | 1,03 (n=72) |

Der Text-Wert ist irreführend (E hat nie Text und ist tot — Kanalstil, kein
Bildhebel). Gegenprobe innerhalb A: 4 Thumbs ohne Text (Median 115K) gegen
4 mit Text (Median 118K) — **kein Unterschied**. Text bleibt frei wählbar,
geregelt allein durch `thumbnail-checkliste.md`.

---

## 3. Serienkonsistenz (Aufgabe 3)

Anteil des dominanten Feinmotivs je Kanal (aus dem Inventar):

| Kanal | dominant | Anteil | Kanalstatus |
|---|---|---|---|
| F | `js` | **10/10** | tot (Median 7,5 Views) |
| C | `js` | 8/10 | tot (38) |
| D | `jfront` | 8/10 | tot (8) |
| B | `js` | 10/13 (Bildwelt: **13/13**) | **Gewinner** |
| I | `jstand` | 3/4 | tot (92) |
| H | `jfront` | 6/10 | tot (52) |
| A | `jsit`/`js` | 4/8 (Bildwelt: 8/8, davon 1 Stilbruch SW) | **Gewinner** |
| G | `js` | 5/10 | tot (62) |
| J | `js` | 2/5 | tot (34) |
| E | — | 2/10 | tot (102) |

**Konsistenz korreliert nicht mit Erfolg.** Der konsistenteste Kanal der
Stichprobe (F, 10/10) ist der toteste; C und D sind mit 80 % ebenso tot wie
das inkonsistente E. B ist **kein** Beleg für „Konsistenz → Erfolg" — Konsistenz
ist in dieser Nische schlicht Standard (7/10 Kanäle ≥50 % dominantes Motiv).

Was von der Serienregel übrig bleibt (und warum sie trotzdem in der Formel
steht): Sie kostet nichts und trägt die **Wiedererkennung** — B's Serie ist bei
166.000 und bei 140 Views identisch, sie ist Kanalidentität, kein Einzeltreffer-
Hebel. Als PFLICHT begründbar bleibt sie nur darüber, nicht über Reichweite.

---

## 4. Videospur vs. Thumbnail (Aufgabe 4)

Aus den 11 Videostichproben und den 4 Szenenanalysen:

- Bei den Gewinnern zeigt die Videospur **dieselbe Bildwelt wie das Thumbnail**:
  häufigstes Video-Motiv im Sample ist der schlafende Jesus mit Lamm am
  Lagerfeuer — bei A und B fast deckungsgleich mit deren Thumbnails
  (produktions-spec d; Szenenanalyse B #3: ein statisches Gemälde, einzige
  Bewegung Feuerflackern, 2:30 ohne Schnitt).
- 5 der 11 Stichproben sind Ein-Szenen-Loops (alle Gewinnerkanäle darunter);
  Szenenfolgen kommen vor, der schnellste Schneider (3–5 s) ist ein Flop (n=1).
- Kein einziger Fall im Sample, in dem Thumbnail und Videospur zwei
  verschiedene Welten zeigen.

**→ Du brauchst EIN Motiv, keine zwei.** Ein Basisbild pro Video, zwei
Ableitungen: Videospur ohne Text (macht die Pipeline bereits), Thumbnail mit
Textzeile und ggf. engerem Ausschnitt. Genau so ist `produktion/pipeline/`
gebaut — hier ändert sich nichts.

---

## 5. Entscheidungsvorlage (Aufgabe 5)

**Vorweg das ehrliche Gesamtergebnis:** Eine Motiv-Präferenz, die Erfolg
*erklärt*, geben die Daten **nicht** her — C und F falsifizieren das Motiv als
Hebel (20 Gewinnermotiv-Thumbs, alle ≤113 Views). Was die Daten hergeben, ist
asymmetrisch:

1. **Positiv, schwach:** Nur eine Motivfamilie kommt in Treffern überhaupt vor —
   „gemalter Jesus ruht in dunkler Nachtszene, kein Blickkontakt" (10/10, aber
   nur 2 Kanäle).
2. **Negativ, klarer:** Mehrere Bauformen kommen in 0 Treffern vor und clustern
   in Verlierer-Hälften: Frontal mit Blickkontakt (18 Thumbs), Innenraum-
   Bettszenen (3), Alarm-Design (3), Klick-Appelle (4), keine warme Lichtquelle
   (11 Thumbs, Median-Ratio 0,41).

Das Motiv ist also **innerhalb der Gewinner-Bildwelt frei wählbar**; die harte
Arbeit leisten Abgrenzung (siehe Kanal F) und Konsistenz als Identität. Beide
folgenden Richtungen sind mit der Videospur-Welt deckungsgleich und mit
`videos-01-08.md` kompatibel.

### Richtung 1 — Schlafende Figur mit Lamm am Feuer (das Treffer-Kernmotiv)

**Datenbasis:** 6 der 10 Treffer (`js`: B 166K/96K/35K/32K, A 245K/36K); Lamm
9/10, Feuer 8/10 der Treffer; deckungsgleich mit dem häufigsten Videospur-Motiv.
**Risiko:** 22 der 90 Feld-Thumbnails tragen es fast identisch — F ist an der
wörtlichen Kopie gestorben (10/10 Kopien, max. 23 Views). Wer es wählt, braucht
eine sichtbare eigene Handschrift (Perspektive, Palette-Akzent, wiederkehrendes
Serienelement), analog zur 50-%-Regel bei den Titeln.
**Anmerkung zur Figur:** Die Treffer zeigen erkennbar **Jesus selbst** (Gewand,
Bart, teils Halo) — 10/10. Eine anonyme schlafende Gestalt, wie sie
`videos-01-08.md` offen lässt, ist im Feld **unbelegt** (0/90 als Hauptmotiv).
Beides bleibt möglich; nur ist die Jesus-Variante die belegte.

**Generierungs-Prompt (direkt verwendbar):**

```
Quiet devotional oil painting, visible soft brushwork, NOT photorealistic.
Night scene: a bearded man in a simple robe lies fast asleep on a blanket
in an open landscape, a small white lamb nestled against his chest, a deep
red blanket over him. To one side a small, calm campfire — the ONLY warm
light source — casts amber light on the sleeper. Above, a vast deep-blue
night sky full of stars fills the upper two thirds; a thin crescent moon.
Composition: figure large, lower third, slightly left; fire right; nothing
else in frame. Palette: deep night blue and near-black against one pool of
warm orange-gold. High contrast, overall dark image. Perspective: eye level,
slight distance, reverent stillness. No text, no watermark, no eye contact,
no second light source.
```

### Richtung 2 — Sitzender Jesus, allein in dunkler Landschaft (die unterschätzte Treffer-Variante)

**Datenbasis:** 4 der 10 Treffer sitzen statt zu liegen (A 233K, 201K, 184K,
47K) — darunter A's **184K ganz ohne Lamm, Feuer und Text**. Dazu der stärkste
kanal-normierte Einzelwert des gesamten Datensatzes: H's 27.000-Views-Ausreißer
(**519× Kanalmedian**) ist genau diese Bauform. Nur 11/90 Feld-Thumbs nutzen
sie → deutlich mehr Abgrenzungsraum als Richtung 1.
**Risiko:** kleinere Fallzahl als Richtung 1, und der H-Wert ist n=1 von einem
Mischkanal.

**Generierungs-Prompt (direkt verwendbar):**

```
Quiet devotional oil painting, visible soft brushwork, NOT photorealistic.
Night scene: a bearded man in a simple dark-red robe sits alone on a rock
under an old tree, eyes closed, head slightly bowed, hands resting in his
lap — asleep sitting up, or deep in prayer. A vast dark landscape rolls away
behind him; low hills on the horizon, a pale moon behind thin clouds, stars.
One faint warm glow (distant village lights or dying embers) low in the
frame as the only warm accent. Palette: near-black, deep blue, muted brown-
grey, one restrained warm gold accent. Composition: figure large, right of
centre, lower half; sky fills the top. Perspective: slight low angle, calm
and monumental. No text, no watermark, no eye contact, no halo kitsch.
```

### Was NICHT zur Wahl steht (0 Treffer, Verlierer-Cluster)

Frontalporträt mit Blickkontakt · Innenraum-/Schlafzimmerszenen ·
Alarm-Farben und Warn-Banner · Klick-Appelle im Bild · Bilder ohne warme
Lichtquelle · fotorealistischer Look (F: 10/10, max. 23 Views — n=1 Kanal,
aber der einzige Fotoreal-Kanal im Feld ist zugleich der toteste).

### Nicht empfehlbar mangels Fallzahl (ausdrücklich)

- **Jesus mit schlafendem Kind** (E): bester kanal-normierter Median (4,05),
  aber n=2, ein toter Kanal, absolut 341–486 Views. Kein Fundament.
- **Schwarzweiß-Stich** (A, 47K): ein Treffer, n=1 — zeigt nur, dass ein
  starker Kanal auch einen Stilbruch trägt.
- **Serienkonsistenz als Erfolgshebel**: durch Aufgabe 3 nicht gestützt;
  begründbar bleibt sie allein als Wiedererkennung/Kanalidentität.

---

## Wo die Daten schweigen

- Ob **Jesus-Figur oder anonyme Gestalt** besser trägt: keine Daten (anonyme
  Gestalt kommt im Feld nicht vor). Erst nach mehreren eigenen Videos mit
  CTR-Daten beantwortbar.
- Ob die Motivwahl **überhaupt** CTR bewegt: aus Views nicht ableitbar —
  Impressionen/CTR hat nur YouTube Studio. Die offene Frage aus
  `erfolgsregeln.md` (was B #7 von B #8 trennt) bleibt offen.
  > **Teilbefund 2026-08-23** *(eigene Kanaldaten Gate 2)*: Die Motivfrage bleibt offen —
  > die **Engpassfrage** nicht. Das eigene Video mit dem zweitschlechtesten CTR (1,82 %)
  > bekam 3.130 von 5.535 Impressionen, weil es 80 % der Kanal-Wiedergabezeit trägt.
  > Ausliefern nach Wiedergabezeit schlägt Klickrate; das Thumbnail ist bei diesem
  > Kanalstand **nicht** der Engpass. Ausgeführt in
  > [`thumbnail-checkliste.md`](thumbnail-checkliste.md), Abschnitt „Was diese Analyse
  > nicht beantwortet". Für Motivvergleiche fehlen weiterhin A/B-Daten: im Zeitraum lief
  > je Video nur eine Variante.
- Tageszeit-Signal (Nacht 10/10 Treffer, Tag 0/18): konfundiert — fast alle
  Tag-Thumbs sind Frontal-Stil von D/H.
