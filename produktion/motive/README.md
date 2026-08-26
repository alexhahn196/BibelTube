# Serien-Motivvarianten — Handytest

> **Stand 2026-08-04, zweiter Lauf.** Serienmotiv nach `formel/thumbnail-motive.md`,
> Richtung 2:
> **sitzende Jesus-Figur, allein in dunkler Nachtlandschaft, kein Blickkontakt.**
> Erzeugt mit Higgsfield (nano-banana), 1376×768 → auf 1920×1080 gebracht
> (Höhe skaliert, Breite mittig auf 16:9 beschnitten, Verlust ~0,8 %).

## Dateien

| Datei | Inhalt |
|---|---|
| `motiv-V1.png` | Felsen über weitem Tal, **großer Mond tief am Horizont** als Lichtquelle (Formel §5 zählt den Mond zu den zulässigen warmen Lichtquellen) |
| `motiv-V2.png` | Seeufer, **große Öllampe**, Nebel über dem Wasser |
| `motiv-V3.png` | Alter Baum auf Anhöhe, **großes Lagerfeuer mit sichtbarer Glut**, ferne Hügel |
| `motiv-V4.png` | Wegrand, **große Laterne**, weite Ebene |
| `loops/loop-V?.mp4` | nahtloser 60-s-Animations-Loop je Variante |
| `loops/qa-V?.json` | Naht- und Bitratenmessung je Loop |
| `motiv-V?_160x90.png` | Feed-Größe für die Handy-Entscheidung |
| `motiv-V3_text.png` (+160×90) | Textvariante mit der Zeile von Video 01 |
| `text_messung.json` | Messwerte der Textvariante |
| `kanal-avatar.png` (+`_kreistest.png`) | Kanal-Profilbild, 1024×1024: vereinfachte Silhouette der Serienfigur an verglimmender Glut — quadratisch, Figur mittig mit Randreserve für den Kreisbeschnitt; Kreistest in 800/176/88/48 px |
| `kanal-avatar-b.png` (+`_kreistest.png`) | Profilbild-Variante B: enger Kopf-Schulter-Anschnitt der Serienfigur, dunkelrote Kapuze, Feuerlicht von rechts unten — bei 88/48 px deutlich besser lesbar als Variante A; helle Masse ragt zu 20 % über den Kreis (nur Kapuze/Schulter, Gesicht bleibt zentral) |
| `kanal-avatar-b2.png` (+`_kreistest.png`) | Zweiter Wurf desselben Prompts: näherer Anschnitt, Dreiviertelprofil (Augen zu, kein Blickkontakt), wärmer. Bei 88/48 px die lesbarste der drei Fassungen; 23,5 % der hellen Masse außerhalb des Kreises (Kapuze/Schulter, Gesicht zentral). Dreiervergleich: `kanal-avatar_vergleich_klein.png` |
| `kanal-banner.png` (+`_zonen.png`, `_mobilansicht.png`, `-quelle.png`) | **Finales Kanalbanner, 2560×1440, 3,1 MB** (Limit 6 MB). Neufassung mit zentrierter Figur auf dem Horizont, symmetrische Hügel; vertikal umkomponiert (Versatz −222 px, Bodenfüllung unten), damit Figur+Feuer im Beschnitt liegen: 82 % der warmen Masse im Desktop-Streifen UND im Mobil-Safe (Figur war mit 34 % Bildhöhe größer als bestellt — der Block ist 70 px höher als der 423-px-Streifen, Haarspitze/Feuerbasis ragen minimal hinaus). Mobilansicht als eigene Vorschau |
| `motiv-video-02.png` (+`_160x90.png`, `_messung.json`) | **Standbild Video 02**, 1920×1080: Grundmotiv mit aufgeschlagenem Buch neben der Figur, größeres Feuer, dichteres Sternenfeld (Vorgabe aus `videos-01-08.md`, Thumbnail-Block Video 02). Aus einem 2k-Wurf mit eingebrannten Balken beschnitten — siehe „Standbild Video 02" |
| `kanal-banner-entwurf.png` (+`_zonen.png`) | Banner-Panorama, **als Banner so nicht verwendbar**: Figur+Feuer liegen zu 99 % unter dem Desktop-Streifen und zu 100 % außerhalb des Mobil-Safe-Bereichs (nur leerer Himmel sichtbar); Zonen-Overlay zeigt die Beschnitte. Neufassung braucht Figur+Feuer im Mittelband |
| ⚠️ `../kanal/banner.jpg` (+`banner_safearea.jpg`) | **Zweiter Bannerentwurf, liegt außerhalb dieses Ordners** — reines Textbanner „THE NIGHTLY WORD", ohne Figur. Siehe „Zwei Bannerentwürfe" unten: **die Entscheidung zwischen beiden ist offen.** |

Alle vier erfüllen die nicht verhandelbaren Vorgaben: gemalter Stil, Nacht,
dunkles Blau dominant, genau **eine** warme Lichtquelle, Figur sitzend im
Profil/halb abgewandt, kein Blickkontakt, kein Innenraum, kein Text (außer der
ausgewiesenen Textvariante).

## Zwei Bannerentwürfe — Entscheidung OFFEN bis Gate 2

Es liegen **zwei fertige Kanalbanner** im Repo, beide 2560×1440, beide je für
sich geprüft, und sie widersprechen sich in der Grundentscheidung: **mit Figur
oder ohne.** Der Grund für das Nebeneinander ist historisch — der zweite Entwurf
entstand am 05.08.2026 auf einem Nebenbranch
(`claude/video-01-subtitle-placement-wsogb8`) und wurde erst am 10.08.2026 in den
Hauptbranch gemergt. Bis dahin kannte ihn keine Sitzung, die auf dem
Hauptbranch arbeitete.

| | Entwurf 1 — Figur | Entwurf 2 — Text |
|---|---|---|
| Datei | `kanal-banner.png` (dieser Ordner) | `../kanal/banner.jpg` |
| Nebendateien | `_zonen.png`, `_mobilansicht.png`, `-quelle.png` | `../kanal/banner_safearea.jpg` |
| Format | PNG, 3,06 MB | JPEG, 1,43 MB |
| Motiv | zentrierte Figur auf dem Horizont, symmetrische Hügel | **reiner Schriftzug, keine Figur** |
| Erzeugt mit | Higgsfield (nano-banana-Linie) | `gpt_image_2`, 16:9, 4k, quality high |
| Commit | `3dc06b5`, 05.08. **10:24** | `2626796`, 05.08. **11:16** |
| Bestandene Prüfung | Zonen-Test: 82 % der warmen Masse im Desktop-Streifen **und** im Mobil-Safe; Figur ragt minimal über den 423-px-Streifen | Fünf Prüfungen: Schriftzug vollständig in der Safe Area 1546×423 (152/138 px seitlich, 176/183 px oben/unten) · „THE NIGHTLY WORD" buchstabengetreu, 14 Glyphencluster, kein Fremdtext · keine Figur/Person/Tier · Kontrast 17,5:1 · genau eine warme Lichtquelle |

**Der Widerspruch:** Entwurf 2 ist 52 Minuten jünger und schließt eine Figur
ausdrücklich aus — Entwurf 1 setzt sie ins Zentrum. Entwurf 1 ist der oben in
der Dateitabelle als „Finales Kanalbanner" geführte; Entwurf 2 war bis zum
Merge nirgends dokumentiert, und nichts im Repo verweist auf seinen Pfad.

**Regelung bis Gate 2:**

- **Beide Entwürfe bleiben erhalten. Nichts wird gelöscht.**
- Die Entscheidung fällt **nicht** nach Bildwirkung, sondern an **Gate 2**
  (`produktion/workflow-gates.md`, Feedback-Schleife nach Video 4): Dort liegen
  erstmals eigene Impressionen und CTR vor. Ein Banner wirkt auf die
  Kanalseiten-Conversion, nicht auf die Video-CTR — deshalb ist vor eigenen
  Zahlen keine belastbare Entscheidung möglich, und Gate 2 gilt ohnehin die
  Kernregel „eigene Daten schlagen Fremddaten".
- Solange keine Entscheidung gefallen ist, gilt für den tatsächlichen Upload
  **Entwurf 1** — nicht weil er besser ist, sondern weil er der dokumentierte
  Stand ist. Wer Entwurf 2 hochlädt, hält das hier fest.
- Die Formel gibt keinen Ausschlag: `formel/video-formel.md` regelt Thumbnails
  und Standmotive, **nicht** das Kanalbanner. Für Banner existiert keine aus den
  10 Fremdkanälen abgeleitete Vorgabe — auch das ein Grund, es an eigenen Zahlen
  zu entscheiden.

**Nachtrag 2026-08-23 — Gate 2 ist gelaufen und entscheidet es NICHT.**
*(eigene Kanaldaten Gate 2)*

Die erwarteten Zahlen liegen vor, aber es sind die falschen für diese Frage. Gate 2
liefert **Video**-Impressionen und Video-CTR; ein Banner wirkt auf die
**Kanalseiten**-Conversion, und die steht in dieser Auswertung nicht. Was an
Kanalseiten-Signal da ist, trägt nichts: **2 Abonnenten** im ganzen Zeitraum, und
die 36 Aufrufe aus „Startseite/Abo-Feed" sind kein Kanalseitenbesuch (das API-Label
`SUBSCRIBER` bedeutet Startseite und Abo-Feed, nicht Abonnenten-Aufrufe).

**Also unverändert:** beide Entwürfe bleiben, für den Upload gilt weiter **Entwurf 1**.
Neues Kriterium statt eines neuen Termins: Die Frage wird erst entscheidbar, wenn
Kanalseitenaufrufe und Abo-Conversion in dreistelliger Größenordnung vorliegen. Bis
dahin ist jede Entscheidung hier Geschmack, nicht Datenlage — und Geschmack rechtfertigt
keinen Wechsel weg vom dokumentierten Stand.

## Textvariante — gemessene Werte

Auf **V3** gelegt, nicht auf V1: Bei V1 steht der Mond in der Textzone, und die
Checkliste verbietet weißen Text über dem Mond. V3 hat das dunkelste
durchgehende Himmelsband (p95-Luminanz 0,030) und ist zugleich die
Serien-Kernvariante (Feuer als Lichtquelle wie in 8/10 Treffern).

| Größe | gemessen | Vorgabe |
|---|---|---|
| Versalhöhe | **125 px = 11,57 %** der Bildhöhe | ≥ 125 px / ≥ 11,5 % |
| Kontrast zum direkten Hintergrund (Mittel) | **17,4 : 1** | ≥ 10 : 1 |
| Kontrast (p95, ungünstige Pixel) | **15,5 : 1** | ≥ 10 : 1 |
| Wörter | 3 (`SO TIRED TONIGHT`) | ≤ 4 |
| Schrift | FreeSerif Bold, weiß, Versalien, oberes Drittel, zentriert | B-Serie 13/13 |

Gegen den **Rohhintergrund** (vor dem weichen dunklen Schein hinter der
Schrift): Mittel 15,8:1, p95 13,7:1 — 90 einzelne Sternpixel unter den Glyphen
würden nackt durchfallen; der Schein im fertigen Bild löst das (ungünstigster
Pixel dort 2,0:1 → nur noch abgedunkelte Sterne unter deckend weißer Schrift).

## Textbreiten aller acht Zeilen — erledigt (Stand 2026-08-07)

Bei 1920 px Bildbreite und 40 px Rand je Seite stehen **1840 px** zur
Verfügung. Die Versalhöhe von 125 px ist nicht verhandelbar (Checkliste,
≥ 11,5 % der Bildhöhe), und die Checkliste schreibt bei Überlänge
ausdrücklich vor: **Wörter kürzen, nicht die Schrift verkleinern.** Alle Werte
in FreeSerif Bold @ 184 px, der schmalsten der drei installierten Serifen.

| | Zeile | Zeichen | Breite | Rand je Seite | |
|---|---|---|---|---|---|
| V01 | `SO TIRED TONIGHT` | 16 | 1787 px | 66 px | knapp |
| V02 | `QUIET YOUR MIND` | 15 | 1726 px | 97 px | |
| V03 | `GOSPEL OF JOHN` | 14 | 1609 px | 155 px | |
| V04 | `THINK NO MORE` | 13 | 1548 px | 186 px | gekürzt |
| V05 | **`GOSPEL OF LUKE`** | 14 | **1659 px** | 130 px | gebaut 2026-08-25, 129 px |
| V06 | ~~`ISAIAH TONIGHT`~~ | 14 | 1616 px | 152 px | **hinfällig, Korpus wird neu geschnitten** |
| V07 | ~~`NO MORE STRESS`~~ | 14 | 1677 px | 121 px | **hinfällig, Korpus wird neu geschnitten** |
| V08 | `IN THE BEGINNING` | 16 | 1807 px | 56 px | knapp |

**Alle liegen unter 1840 px — kein Textfall ist offen.**

> **Die Werte für V05–V08 sind seit 2026-08-25 bei 129 px Versalhöhe gerechnet**
> (vorher 125). Grund: `thumbnail.py` trennt jetzt Prüfgrenze (11,5 %) und Zielwert
> (11,9 %, B-Median) — siehe `formel/thumbnail-checkliste.md`. V01–V04 in der Tabelle
> darüber stehen weiter bei 125 px, sie sind so veröffentlicht.

> **Nachtrag 2026-08-23** *(eigene Kanaldaten Gate 2)*. Drei Zeilen sind
> überholt:
> - **V05** trägt jetzt `GOSPEL OF LUKE` — Entscheidung des Kanalinhabers, damit
>   Titel und Thumbnail denselben Eigennamen führen. Mit **1607 px** liegt die
>   Zeile 2 px unter `GOSPEL OF JOHN` (V03, 1609 px); die Serie bleibt in der
>   Zeilenbreite deckungsgleich. Neu gemessen mit derselben Fontkette
>   (FreeSerif Bold @ 184 px, Versalhöhe 125 px).
> - **V06 und V07** hängen an Korpora, die M8 verletzen bzw. grenzwertig sind
>   (`videos-01-08.md`). Ihre Thumbnail-Zeilen werden erst festgelegt, wenn die
>   Korpusentscheidung gefallen ist.
>
> **Offen und bewusst nicht entschieden:** ob der Eigenname aus Formel §1 auch
> im **Thumbnail** Pflicht ist oder nur im Titel. §1 regelt den Titel. V03 und
> jetzt V05 führen ihn in beiden; V08 (`IN THE BEGINNING`) spielt auf Genesis an,
> ohne das Buch zu nennen. Solange der Wirkmechanismus des Eigennamens ungeklärt
> ist (§1, „die sparsamere Erklärung"), ist das keine dringende Frage — aber es
> ist eine.

Quellen: V01–V04 aus den Messdateien der gebauten Thumbnails
(`produktion/video-0?/thumbnail*_messung.json`), nicht neu gemessen.
V05–V08 mit der Methode aus `thumbnail.py` gerechnet (gleiche Fontkette,
gleiche 125 px Versalhöhe) — bisher ohne Bild, weil diese Videos erst nach
Gate 2 starten. `GOSPEL OF LUKE` am 2026-08-23 auf demselben Weg nachgemessen.

Zwei Zeilen mussten weichen, beide dokumentiert in `videos-01-08.md`:
`NO MORE THINKING` (1896 px, 56 px zu breit) → `THINK NO MORE`, und
`REST WITHOUT STRESS` (2163 px, 323 px zu breit) → `NO MORE STRESS`.

Die praktische Faustregel bleibt: **13–14 Zeichen sitzen bequem**, 16 gehen
nur mit schmalen Glyphen. `SO TIRED TONIGHT` und `NO MORE THINKING` haben
beide 16 Zeichen und unterscheiden sich um 109 px — `M`, `N`, `K` und `W`
sind breit, `S`, `T`, `I` schmal. Zeichen zählen reicht also nicht, es muss
gemessen werden. Zum Vergleich: dieselbe V01-Zeile bräuchte in DejaVu Serif
Bold 1967 px und passte dort nicht.

> Die frühere Warnung an dieser Stelle („fünf der acht Zeilen liegen über der
> bequemen Breite, vor dem Rendern entscheiden") ist mit den beiden Kürzungen
> aufgelöst und wurde durch die Tabelle oben ersetzt.

## Wie es weitergeht

Die Entscheidung fällt am Handy auf den 160×90-Versionen. Danach wird die
gewählte Variante das **Serienbild**: gleiche Figur, gleiche Palette, je Video
nur die dokumentierte Detailvariation (`produktion/videos-01-08.md`,
Thumbnail-Blöcke). Generierungs-Prompts für Nachschübe stehen in
`formel/thumbnail-motive.md` §5.

## Standbild Video 02 (2026-08-06)

Serienmotiv mit der Detailvariation aus `videos-01-08.md`: **aufgeschlagenes
Buch** neben der Figur (belegt in A's 245K), größeres Feuer, dichteres
Sternenfeld. Figur unverändert — Serienkonsistenz nach Formel §3.

**Befund: nano-banana brennt Letterbox-Balken ins Bild.** Alle vier erzeugten
Kandidaten hatten schwarze Balken oben *und* unten — gemalte Kinobalken im
Bild, nicht am Bildrand. Der ausdrückliche Prompt-Zusatz „no letterbox, no
black cinematic bars, sky continues to the very top edge" im zweiten Lauf hat
daran **nichts** geändert. Für Nachschübe einplanen: nach der Generierung
immer `motiv_zuschnitt.py` laufen lassen und das Ergebnis auf Restbalken
prüfen. Angefordert war `nano_banana_2`, ausgeführt und abgerechnet hat die
Plattform beide Male `nano_banana_flash`.

Gewählt wurde Kandidat D (2752×1536, 2k). Zuschnitt mit
`produktion/pipeline/motiv_zuschnitt.py`, **0 Credits**:

| Schritt | Wert |
|---|---|
| Balken oben / unten | 184 px (12,0 %) / 182 px (11,8 %) |
| Nutzband nach Balkenschnitt | 2752×1170 = 2,352 : 1 |
| Breitenschnitt mittig auf 16:9 | 2752 → 2080 px, je Seite 336 px = **12,2 %** |
| Skalierung auf 1920×1080 | Faktor **0,923** — Verkleinerung, keine Hochrechnung |
| Restbalken am Ergebnis | 0 px oben, 0 px unten |

Zonenwerte im Vergleich zum Video-01-Motiv (`motiv-V3.png`):

| | V3 (Video 01) | Video 02 |
|---|---|---|
| oberes Sechstel p95 (Textzone) | 50,3 | **23,7** |
| oberes Drittel, Anteil heller Pixel | 3,44 % | **1,32 %** |
| Gesamtmittel (dunkles Bild, Formel §5) | 48,2 | **30,2** |
| unteres Achtel p95, Mitte (Untertitel) | 104,1 | 110,9 |
| unteres Achtel p95, rechtes Drittel | 104,9 | **213,2** |

Die Textzone ist deutlich dunkler als bei Video 01 — das Thumbnail gewinnt
dadurch Kontrast. Heller ist nur das **rechte** untere Drittel: das Feuer
reicht nach dem Balkenschnitt bis an die Unterkante. In der mittigen
Untertitelzone (110,9 gegenüber 104,1) ist der Unterschied belanglos, im
Mittel ist das neue Motiv dort sogar dunkler (46,5 gegenüber 54,3).

**Bekannte Schwäche, bewusst angenommen:** Die Hand auf dem Knie ist weich
gemalt und geht in die Gewandfalte über. Bei Feed-Größe 160×90 nicht sichtbar
— dieselbe Abwägung wie bei den drei dokumentierten Mängeln im 166K-Thumbnail
von Kanal B (`formel/thumbnail-checkliste.md`).

## Animations-Loops (`loops/`)

Erzeugt mit `produktion/pipeline/loop_animation.py` — **keine KI-Videoclips**,
sondern mathematische Ebenen über dem Standbild: alle Bewegungen sind Sinus-
bzw. deterministische Rauschfunktionen, deren Frequenzen ganzzahlige Vielfache
von 1/60 s sind. Frame 0 und Frame 1440 sind dadurch **bitidentisch berechenbar**
(gemessen: max. Pixeldifferenz 0 bei allen vier).

Ebenen je Variante: Lichtpuls (drei überlagerte Sinuswellen) überall ·
V1 zusätzlich Sternfunkeln · V2 Nebel-Drift + Wasserglitzern + Sterne ·
V3 Glutflackern + 12 Funken (Helligkeit an beiden Lebensenden null) +
Rauchfahne + Baum-Wiegen + Sterne · V4 Gras-Wiegen + Sterne.
Alles bewusst sehr dezent — Einschlaf-Video, kein Blickfang.

### Messwerte (qa-V?.json)

| | Wrap-Schritt roh | normale Schritte roh (Median/Max) | Naht dekodiert (3×-Rendering) | interne Keyframes (Median/Max) | kbit/s | 3,5 h Bildspur |
|---|---|---|---|---|---|---|
| V1 | 0,0016 | 0,0011 / 0,0576 | 1,284 | 0,998 / 1,295 | 183 | 0,29 GB |
| V2 | 0,0036 | 0,0023 / 0,0125 | 1,470 | 1,134 / 1,435 | 200 | 0,31 GB |
| V3 | 0,0094 | 0,0085 / 0,0195 | 1,532 | 1,313 / 1,505 | 234 | 0,37 GB |
| V4 | 0,0027 | 0,0018 / 0,0209 | 1,406 | 1,104 / 1,412 | 198 | 0,31 GB |

Lesart der Nahtprüfung: Der **rohe** Wrap-Schritt (Bewegung selbst) liegt bei
allen vier innerhalb der normalen Frame-zu-Frame-Bewegung — die Animation
schließt mathematisch exakt. Der **dekodierte** Sprung an der Bitstrom-Naht
(~1,3–1,5 mittlere |Δ|/Pixel von 255) ist kein Animationsfehler, sondern der
Keyframe-Refresh des Encoders — er tritt **in gleicher Höhe alle 10 s mitten im
Stream auf** (interne Keyframes, gemessen). Die Naht ist davon nicht
unterscheidbar; kleiner kann sie physikalisch nicht werden, und YouTube
enkodiert das Material ohnehin neu.

### Bitrate

180–234 kbit/s gegenüber ~200 kbit/s der bisherigen reinen Zoom-Bildspur —
**kein nennenswerter Anstieg** (die Ebenen sind klein und dunkel). 3,5 h
Bildspur ≈ 0,3–0,4 GB, mit Ton ~0,6–0,7 GB gesamt.

### Integration in die Pipeline

Der Atem-Zoom aus `schritt5_video.py` (300-s-Zyklus) bleibt: 300 ist ein
ganzzahliges Vielfaches von 60, der gemeinsame Zyklus schließt also exakt
(5 Loop-Durchläufe je Zoom-Atemzug). Nach der Motiv-Entscheidung wird der
gewählte Loop statt des Standbilds als Quelle des 300-s-Zyklus gerendert;
Montage per Bitstrom-Kopie bleibt unverändert.

## Echte KI-Clips (`loops/ki/`, 2026-08-04)

Bild-zu-Video über Higgsfield, Modell **Seedance 1.5 Pro** (einziges Modell,
dessen 4 Clips ins Guthaben passten — FLUX 3 hätte 180 Credits **je** Clip
gekostet). Loop-Trick: `motiv-V3.png` als `start_image` **und** `end_image`,
dadurch enden alle Clips wieder auf dem Ausgangsbild und sind beliebig
aneinanderreihbar. 4 Clips à 12 s = 48-s-Zyklus.

| Messung (alle 4 Clips) | Wert |
|---|---|
| Auflösung / fps / Dauer | 1920×1080 · 24 fps · 12,04 s |
| Kameradrift (Phasenkorrelation Randzonen) | ≤ 0,05 px — praktisch null |
| erster vs. letzter Frame | mittl. \|Δ\| 2,78–2,91 (nicht pixelidentisch — der Generator trifft das Zielbild nur näherungsweise) |
| Übergangsschritt Clip→Clip (alle 16 Paare) | 2,83–3,14 |
| normaler Frameschritt im Clip | 1,40–1,53 |
| Artefakte | keine verformten Objekte, kein Stilbruch, Figur ruhig; **Rauch deutlich kräftiger als „thin wisps"** — Geschmacksfrage, im 3-min-Test beurteilen |

Ein Schnitt zwischen Clips ist also ≈2× ein normaler Frameschritt — beide
Grenzframes nähern dasselbe ruhige Ausgangsbild an. `kette-3min.mp4` zeigt
16 Übergänge in Produktionsqualität.

**Bitraten-Vorfall, gemeldet:** Die Clips kommen mit ~10,3 Mbit/s. Per
Bitstrom-Kopie geloopt wären das **16,6 GB** für 3,58 h (Lauf nach 15 GB
abgebrochen). Lösung in `schritt5_video.py`: der 48-s-Zyklus wird **einmal**
neu kodiert (CRF 28 → 1,31 Mbit/s), danach loopt die Montage wieder per
Kopie. Gesamtvideo damit ≈ 2,1 GB Bildspur + 0,31 GB Ton ≈ **2,4 GB**
(vorher 0,67 GB mit Standbild-Zoom; CRF 26 wäre mit ≈ 3,3 GB gesamt die
höherwertige Option — `video_crf` in `config.md`).

**Atem-Zoom: entfällt bei `videoquelle = ki_clips`.** Er stört visuell nicht,
aber er ist doppelt verzichtbar: Die PFLICHT aus Formel §5 („Standmotiv mit
sanfter Bewegung") erfüllen die Clips selbst, und ein Zoom obendrauf würde
die kopierfähige Montage in einen vollständigen Re-Encode von 3,5 h
verwandeln (zusätzlich LCM-Zyklus 1200 s). Umschaltbar bleibt beides über
`videoquelle` in `config.md`.

**Gültigkeit:** Diese 4 Clips gehören zum aktuellen `motiv-V3.png`. Fällt die
Handytest-Entscheidung auf eine andere Variante, braucht sie eigene Clips
(erneut 72 Credits bei Seedance 1.5 — die hier ursprünglich stehenden 144
waren der Vorabpreis, nicht die Buchung; siehe den Kasten im V02-Abschnitt).

## KI-Clips Video 02 (`loops/ki-v02/`, 2026-08-06)

Gleiches Verfahren wie oben, Quelle ist `motiv-video-02.png` als `start_image`
**und** `end_image`.

Die vier Clips haben **72 Credits** gekostet, 18 je Clip.

> **Widerspruch aufgelöst am 2026-08-26 — beide 144er waren falsch.**
> Am 2026-08-26 reichte das Transaktionsprotokoll wieder bis vor den Lauf
> zurück. Abgerufen und ausgezählt:
>
> | Clipsatz | Buchung | Summe |
> |---|---|---|
> | V01 | 2026-08-04 18:59:53 / 19:00:05 / 19:00:18 / 19:00:29, je −18 | **72** |
> | V02 | 2026-08-06 12:14:19, 4 × −18 | **72** |
> | V03 | 2026-08-06 15:49:48, 4 × −18 | **72** |
> | V04 | 2026-08-07 09:09:48, 4 × −18 | **72** |
> | V05 | 2026-08-26 19:18:28–29, 4 × −18 | **72** |
>
> Damit fällt nicht nur der Widerspruch, sondern auch die Geschichte
> drumherum. **Der Preis hat sich nie halbiert.** Seedance 1.5 Pro hat von
> V01 an 18 Credits je Clip gekostet. Falsch waren beide 144er: die
> Commit-Nachricht `072ef0c` und der Satz „(erneut 144 Credits bei
> Seedance 1.5)" im V01-Abschnitt oben. Und falsch war auch der hier zuvor
> stehende Satz, der Preis sei von 36 auf 18 gefallen — 36 wurde nie
> abgerechnet.
>
> **Woher die 144 stammen, ist ebenfalls belegt.** Die Vorabpreisauskunft der
> API (`get_cost`) meldet für Seedance 1.5 Pro, 1080p, 12 s **36 Credits je
> Clip** — auch heute noch, unmittelbar bevor derselbe Aufruf mit 18 belastet
> wurde (Guthaben 2397,9 → 2325,9 = −72 für vier Clips). Die Vorabauskunft ist
> für dieses Konto also **doppelt so hoch wie die Rechnung**.
>
> **Regel daraus:** Der Vorabpreis ist eine Absicht, das Transaktions­protokoll
> ist das Ergebnis. Für Kostenangaben in diesem Repo gilt ausschließlich das
> Protokoll, und eine Kostenangabe ohne Buchungsdatum ist keine.
> Für die Planung von V06–V08: **72 Credits je Vierer-Satz**, belegt an fünf
> Sätzen. Der Vorabpreis (144) taugt als Obergrenze, nicht als Erwartung.

Drei Prompt-Änderungen gegenüber V01, alle aus dem V01-Befund:

- **Buch ausdrücklich still** („the open book lies completely still — its pages
  do not turn, do not flutter"). Blätternde Seiten wären in einem
  Einschlafvideo ein Blickfang und hätten den Loop gebrochen.
- **Rauch schwächer** („very faint thin wisps, barely visible") — bei V01 war
  er „deutlich kräftiger als bestellt" und als Geschmacksfrage vermerkt.
- Kein Baum mehr im Prompt: dieses Motiv hat keinen.

| Messung | Video 01 | **Video 02** |
|---|---|---|
| Auflösung / fps / Dauer | 1920×1080 · 24 fps · 12,04 s | identisch |
| Kameradrift (Median Randzonen) | ≤ 0,05 px | ≤ 0,065 px |
| erster vs. letzter Frame (mittl. \|Δ\|) | 2,78–2,91 | **2,43–2,49** |
| Übergangsschritt Clip→Clip (16 Paare) | 2,83–3,14 | **2,43–2,70** (Median 2,51) |
| normaler Frameschritt im Clip | 1,40–1,53 | 1,42–1,71 |
| Naht / normaler Schritt | ≈ 2,0 | **1,75** |
| Bitrate der Kette (CRF 28) | 1,31 Mbit/s | 1,27 Mbit/s |

Die Nähte sind also **relativ kleiner** als bei Video 01: der Sprung an einem
Schnitt ist nur noch das 1,75-fache eines normalen Frameschritts. Schlimmstes
Paar `clip-2 → clip-1` mit 2,695.

Nahtsichtung an `kette-3min.mp4` (16 Übergänge, Produktionsqualität, 192,7 s):
Figur, Buch, Fels und Hügellinie stehen über den Schnitt hinweg exakt still;
sichtbar wechselt allein die Flammenform — die ändert sich innerhalb eines
Clips ohnehin von Frame zu Frame. Gemessen an den beiden geprüften Nähten
3,27 (Clip 1→2) und 3,46 (Clip 4→1, der Loop-Rücksprung).

Hochgerechnet auf die 3,52 h Laufzeit: **≈ 2,0 GB Bildspur**, mit Ton ≈ 2,3 GB.

**Zuordnung:** Diese Clips gehören zu `motiv-video-02.png` und zu keinem
anderen Motiv. Die Pipeline liest den Ordner deshalb je Video aus
`ki_clip_ordner_V2` in `config.md`; der allgemeine `ki_clip_ordner` bleibt
für V01 stehen.

## KI-Clips Video 05 (`loops/ki-v05/`, 2026-08-26)

Gleiches Verfahren wie oben, Quelle ist `motiv-video-05.png` als `start_image`
**und** `end_image`. Modell `seedance1_5`, 1080p, 12 s, 16:9,
`generate_audio: false` — dieselben Parameter, mit denen V01–V04 erzeugt
wurden. Nachgesehen in der Generierungshistorie bei Higgsfield, nicht aus dem
Gedächtnis: dort stehen für alle vier früheren Sätze `width 1920`,
`height 1080`, `resolution 1080p`, `duration 12`, `generate_audio false` und
`start_image` = `end_image` = dieselbe `media_input`-ID.

**Warum überhaupt.** V05 war am 2026-08-23 auf `videoquelle = standbild`
gestellt worden mit der Begründung, KI-Clips wären „eine zusätzliche Variable
ohne Beleg" und V05–V08 sollten den Korpuswechsel als einzige Änderung testen.
Das war falsch herum gedacht: V01, V02, V03 und V04 liefen **alle** mit
KI-Clips. Standbild war bei V05 also nicht die Konstante, sondern die zweite
Änderung neben dem Korpus. Der Rücksprung auf `ki_clips` entfernt eine
Variable, er fügt keine hinzu.

### Kosten und Zeit — gemessen, nicht geschätzt

| | Wert | Beleg |
|---|---|---|
| Credits | **72** (4 × 18) | Transaktionsprotokoll, vier Buchungen `Seedance 1.5 Pro −18` am 2026-08-26 19:18:28–29 |
| Gegenprobe Guthaben | 2397,9 → 2325,9 = **−72,0** | `balance` vor und nach dem Lauf |
| Vorabpreis derselben Anfrage | **144** (4 × 36) | `get_cost` unmittelbar vor dem Absenden |
| Wanduhr: Absenden → alle vier fertig | **4 min 30 s** | 19:18:35 → 19:23:05, vier Jobs parallel |
| davon: erster Clip fertig | 3 min 27 s | 19:22:02 |
| Bildspur neu rendern (Schritt 5) | **5 min 38 s** | `renderzeit_s` 337,5 in `qa_video.json` |

Die Vorabauskunft der API liegt für dieses Konto **um den Faktor 2 über der
Rechnung**. Sie taugt als Obergrenze, nicht als Erwartung. Zur Auflösung des
alten 72-gegen-144-Widerspruchs siehe den Kasten im V02-Abschnitt: alle fünf
Clipsätze haben 72 gekostet, der Preis hat sich nie geändert.

Zum Vergleich: eine neue Tonspur hätte TTS-Kosten verursacht. Die entfielen —
`produktion/arbeit/video-05/mix.wav` lag noch, es wurde kein einziges Zeichen
neu synthetisiert.

### Loop-Tauglichkeit (`qa-ki-clips.json`)

| Messung | Video 01 | Video 02 | **Video 05** |
|---|---|---|---|
| Auflösung / fps / Dauer | 1920×1080 · 24 fps · 12,04 s | identisch | **identisch** |
| Kameradrift (Median Randzonen) | ≤ 0,05 px | ≤ 0,065 px | **≤ 0,063 px** |
| erster vs. letzter Frame (mittl. \|Δ\|) | 2,78–2,91 | 2,43–2,49 | **3,03–3,15** |
| Übergangsschritt Clip→Clip (16 Paare) | 2,83–3,14 | 2,43–2,70 | **3,03–3,22** (Median 3,11) |
| normaler Frameschritt im Clip | 1,40–1,53 | 1,42–1,71 | **1,15–1,27** |
| Naht / normaler Schritt | ≈ 2,0 | 1,75 | **2,65** |
| Bitrate der Kette (CRF 28) | 1,31 Mbit/s | 1,27 Mbit/s | **1,41 Mbit/s** |

Schlimmstes Paar `clip-4 → clip-1` mit 3,218 — das ist zugleich der
Loop-Rücksprung. Der Faktor 2,65 liegt zwischen V02 (1,75) und V04
(Frameschritt-Median 0,37–0,60 bei Nähten um 2,9, also Faktor ≈ 5,6); beide
sind ausgeliefert worden. V05 ist damit nicht der beste und nicht der
schlechteste Satz der Serie.

### Sichtung — ein Befund, keine Beanstandung

An Stichproben bei 0, 4, 8 und 11,9 s aller vier Clips: Stil erhalten, Figur
bewegungslos, Mondsichel und Hügellinie stehen, keine verformten Objekte, kein
Szenenschnitt, keine neuen Objekte. Der letzte Frame liegt wieder am
Ausgangsbild.

**Der Rauch ist wieder kräftiger als bestellt.** Der Prompt verlangt „very
faint thin wisps of smoke barely visible"; in Clip 1 bei 4 s und Clip 2 bei
8 s steht stattdessen eine helle Rauchfahne im oberen Bildviertel, bei Clip 1
zieht sie kurz vor der Mondsichel vorbei. Clip 4 ist der ruhigste. Das ist
derselbe Befund wie bei V01 („deutlich kräftiger als bestellt") und dort als
Geschmacksfrage vermerkt worden — die Prompt-Verschärfung von V02 hat ihn bei
diesem Motiv nicht verhindert. Ein neuer Satz kostet wieder 72 Credits und
4,5 Minuten, ohne Zusage, dass er ruhiger ausfällt. Entscheidung des
Kanalinhabers; ausgeliefert ist der vorliegende Satz.

### Auswirkung auf die Datei

| | Standbild + Atem-Zoom | **KI-Clips** |
|---|---|---|
| Videospur | 358,4 kbit/s | **1411,1 kbit/s** |
| Tonspur (AAC) | 191,4 kbit/s | 191,4 kbit/s |
| Gesamt | 556,0 kbit/s | **1608,3 kbit/s** |
| Datei bei 3,404 h | 851,6 MB | **2463,6 MB** |

Faktor 2,89 auf die Gesamtdatei, 3,94 auf die reine Bildspur. Beides
8 Bit `yuv420p`, Profil High, CRF 28 — die Einstellungen sind identisch, der
Unterschied ist ausschließlich Bildinhalt. Ton-Versatz gemessen 0,0 s,
Streamlängen-Differenz 0,1 s.

**Zuordnung:** Diese Clips gehören zu `motiv-video-05.png` und zu keinem
anderen Motiv. Die Pipeline liest den Ordner je Video aus `ki_clip_ordner_V5`
in `config.md`.
