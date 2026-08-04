# Thumbnail-Checkliste

> **Stand: 2026-08-03.** Grundlage: 90 Thumbnails (21 Gewinner, 69 Verlierer aus 8 Kanälen),
> maschinell vermessen plus visueller Test auf 160×90 px (Feed-Größe am Handy).
> Rohdaten: `regeln/daten/thumb_messung.json`, `thumb_textmessung.json`,
> `feedtest_GEWINNER.png`, `feedtest_VERLIERER.png`, `zoom_B_figur.png`.
>
> Alle Vorgaben liegen **innerhalb** der belegten Muster (Serienmotiv, Nachtfarbwelt, warme
> Lichtquelle). Nichts hier bricht ein Muster.

---

## Zuerst: wo die Daten KEINE Mängel zeigen

Damit du dort keine Zeit investierst. Diese drei Verdachtspunkte habe ich gemessen und
**widerlegt**:

| Geprüft | Ergebnis | Fallzahl |
|---|---|---|
| **Auflösung** | 89 von 90 liegen nativ in 1280×720 vor. Der eine Ausreißer (480×360) ist der Fallback **meines Downloads**, kein Kanal-Mangel. Kein Hochskalieren, keine Streckung. | 90 |
| **Kompression** | Median 201–237 KB bei 1280×720 in allen drei Gruppen. Ein einziger Ausreißer (19 KB) ist derselbe Fallback. Keine sichtbaren JPEG-Blöcke. | 90 |
| **Bildschärfe** | Nur 2 von 90 auffällig weich (Laplace-Varianz <150) — je einer bei Gewinnern und Verlierern. Kein Muster. | 90 |

**Wichtig gegen einen Fehlschluss:** Die Gewinner sind *unschärfer* als die Verlierer
(Median 704 gegen 853–906). Das ist kein Mangel, sondern Folge des gemalten Stils —
fotorealistische Thumbnails haben mehr Hochfrequenzdetail. **Jage keine Schärfewerte.**

---

## Die Zielwerte, ausgemessen an der bewährten Serie

Gemessen an allen 13 Thumbnails von Rest in Grace — der Serie mit dem konsistentesten
Erfolg und dem geringsten Streuungsrisiko:

| Größe | Zielwert | Belegte Spanne | Fallzahl |
|---|---|---|---|
| **Versalhöhe** | **≥ 11,5 % der Bildhöhe** (≈ 83 px bei 720p, ≈125 px bei 1080p) | 9,9–12,1 %, Median 11,9 % | 13 |
| **Kontrast Text/Hintergrund** | **≥ 10:1** | 10,1–17,5:1, Median 15,4:1 | 13 |
| **Wortzahl** | **maximal 4 Wörter** | Gewinner 0–4 | 21 |

Zum Vergleich die Verlierergruppen: Versalhöhe Median **9,0–9,5 %** — also rund ein Viertel
kleiner als bei den Gewinnern (n=69). Das ist der einzige typografische Messwert, der Gewinner
und Verlierer sauber trennt.

Der Kontrastwert 10:1 ist bewusst hoch angesetzt: WCAG verlangt 4,5:1, die Gewinner-Serie
liefert aber durchgehend das Doppelte bis Dreifache. Du hast keinen Grund, unter ihren
schlechtesten Wert (10,1) zu gehen.

---

## Feed-Test 160×90: was hält, was zusammenbricht

Visuell geprüft, alle 90 auf echte Feed-Größe heruntergerechnet.

**Hält zuverlässig:**
- Fette Versalien, 2–4 Wörter, eine Zeile oder zwei — bei **allen** geprüften Fällen lesbar
  (B-Serie 13/13, dazu „SLEEP DEEP", „JUST SLEEP", „REST NOW", „PRAY THIS TONIGHT")

**Bricht zusammen:**
- **Ab 6 Wörtern.** Härtester Fall: Kanal D mit *„DO NOT SKIP THIS. God Says: Watch This Today.
  The Waiting Is Over."* — 12 Wörter in einem Kasten, bei Feed-Größe nur noch ein gelber Fleck
  (54 Views).
- **Dünne Serifen in Gemischtschreibung** verlieren deutlich gegenüber fetten Versalien.
  Betrifft **auch Gewinner**: A's *„Time To Sleep."* (233K) und *„Peaceful Sleep."* (12K)
  sind bei 160×90 noch erkennbar, aber merklich schwächer als B's Versalien. Bei Kanal C
  (*„Hear the Teachings of Jesus"*, 89 Views) kippt derselbe Stil ins Unlesbare.
- **Heller Text auf hellem Grund.** Kanal F setzt „Just Sleep" in hellem Grau auf helle
  Wolken — bei Feed-Größe praktisch verschwunden (14 Views).

**Ein echter Mangel bei einem Gewinner:** A's Video mit **201.000 Views** trägt unten links
die Mikroschrift *„we are"* — bei Feed-Größe vollständig unlesbar und inhaltlich sinnlos
(vermutlich ein abgeschnittener Textrest). Das Video lief trotzdem. **Lesbarkeitsmängel sind
also nicht tödlich** — aber es gibt keinen Grund, sie zu kopieren.

---

## KI-Artefakte

Geprüft an Ausschnitten in voller Auflösung, Schwerpunkt auf den bekannten Schwachstellen.

**Im gemalten Stil (A, B, C, F, I) verstecken sich die typischen Fehler weitgehend** — keine
verformten Hände, keine sechsten Finger in der Stichprobe. Der weiche Pinselduktus verzeiht
Anatomie.

**Aber die bewährte B-Serie hat drei sichtbare Schwächen** (geprüft am 166.000-Views-Motiv,
das du kopieren würdest):
1. Der **Arm unter dem Kopf** verschmilzt mehrdeutig mit Kissen und Haar — man sieht nicht,
   wo er endet.
2. **Fuß und Beinlänge** rechts unten lesen sich seltsam, Zehen undeutlich, Unterkörper wirkt
   gegenüber dem Rumpf zu lang.
3. **Das Lagerfeuer beleuchtet die Figur nicht.** Das Feuer steht rechts, die Figur wird von
   vorn-links beleuchtet. Der warme Akzent ist da, aber physikalisch unstimmig — und das
   wiederholt sich über die Serie.

Bei fotorealistischen Motiven war die klassische Schwachstelle unauffällig: D's ausgestreckte
Hand (77 Views) ist sauber gerendert, Finger zählbar.

**Einordnung, damit du nicht überinvestierst:** Alle drei B-Mängel stecken in einem Thumbnail
mit 166.000 Views und sind bei Feed-Größe unsichtbar. Prüfen ja — nachbessern nur, wenn es
schnell geht.

---

## Checkliste vor dem Upload

**Typografie**
- [ ] Maximal **4 Wörter** im Bild
- [ ] Versalien, fett — keine dünnen Serifen in Gemischtschreibung
- [ ] Versalhöhe **≥ 11,5 % der Bildhöhe** (bei 1920×1080: **≥ 125 px**)
- [ ] Kontrast Text zu direktem Hintergrund **≥ 10:1** (weißer Text nur über dem dunklen
      Nachthimmel, nie über Feuerschein, Mond oder heller Wolke)
- [ ] Kein zweiter, kleinerer Textblock — keine Mikroschrift, keine Textreste
- [ ] Text sitzt im oberen Drittel, Figur und Lichtquelle darunter (B-Serie: 13/13)

**Motiv (Serienbindung — nicht verhandelbar)**
- [ ] Gleiches Motiv wie die letzten Uploads: **sitzende Jesus-Figur, allein in
      dunkler Nachtlandschaft, kein Blickkontakt** *(Serienentscheidung
      2026-08-04, `thumbnail-motive.md` Richtung 2 — ersetzt die frühere
      „schlafende Figur, Lamm, Lagerfeuer")*
- [ ] Tiefes Nachtblau als Grundton, genau **eine** warme Lichtquelle
- [ ] Keine Grelltöne, kein Tageslicht, keine gesättigten Neonfarben

**Bildprüfung (2 Minuten, in dieser Reihenfolge)**
- [ ] **Auf 160×90 verkleinern und ansehen.** Ist der Text in einer Sekunde erfassbar? Wenn
      nein: Wörter streichen, nicht die Schrift verkleinern.
- [ ] Hände, Arme, Füße der Figur einzeln prüfen — verschmilzt etwas mehrdeutig?
- [ ] Beleuchtet die warme Lichtquelle die Figur tatsächlich aus ihrer Richtung?
- [ ] Lammbeine und Gesichtszüge auf Verformung prüfen
- [ ] Export als **1280×720 oder 1920×1080 JPEG, ≥ 150 KB** (Gewinner-Median 237 KB)

**Nicht prüfen — nachweislich irrelevant**
- ~~Schärfe/Detailgrad~~ (Gewinner sind unschärfer als Verlierer)
- ~~Auflösung über 1080p~~
- ~~Kompressionsartefakte~~ (bei keinem Kanal ein Problem)

---

## Was diese Analyse nicht beantwortet

- **Ob die Zielwerte kausal wirken.** Versalhöhe und Kontrast trennen Gewinner und Verlierer
  sauber — aber B's Thumbnails sind bei 166.000 und bei 140 Views praktisch identisch. Die
  Werte qualifizieren das Thumbnail; sie erklären den Einzeltreffer nicht.
- **Ob 4 Wörter besser sind als 0.** A's zwei größte Videos (245K, 184K) haben **gar keinen
  Text**, B's Serie hat durchgehend 2–4 Wörter. Beide Muster gewinnen. Die Obergrenze von 4 ist
  belegt, eine Untergrenze nicht.
- **Klickrate.** Ohne Impressions und CTR aus fremden Analytics bleibt offen, ob Thumbnails
  überhaupt der Engpass sind. Deine eigenen Analytics schließen das ab Video 1.
