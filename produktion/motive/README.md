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

Alle vier erfüllen die nicht verhandelbaren Vorgaben: gemalter Stil, Nacht,
dunkles Blau dominant, genau **eine** warme Lichtquelle, Figur sitzend im
Profil/halb abgewandt, kein Blickkontakt, kein Innenraum, kein Text (außer der
ausgewiesenen Textvariante).

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

## Befund am Rand: Die Textzeile kollidierte fast mit der Versalhöhen-Regel

`SO TIRED TONIGHT` (16 Zeichen) ist bei 125-px-Versalien in **keiner**
installierten Serifen fetter Schnitt unter 1.884 px breit — DejaVu bräuchte
2.082 px. Nur FreeSerif Bold passt, mit 66 px Rand je Seite, **exakt an der
Untergrenze**. Praktische Folge für die Serie: Bei 1920 px Breite trägt eine
Zeile etwa **13–14 Zeichen bequem** (B's Feldbeispiele: alle ≤ 13). Von den
acht geplanten Textzeilen liegen fünf darüber (`REST WITHOUT STRESS` mit 19
Zeichen am weitesten). Vor dem Rendern der weiteren Thumbnails entscheiden:
Wörter kürzen (Weg der Checkliste) oder schmalere Serife zulassen.

## Wie es weitergeht

Die Entscheidung fällt am Handy auf den 160×90-Versionen. Danach wird die
gewählte Variante das **Serienbild**: gleiche Figur, gleiche Palette, je Video
nur die dokumentierte Detailvariation (`produktion/videos-01-08.md`,
Thumbnail-Blöcke). Generierungs-Prompts für Nachschübe stehen in
`formel/thumbnail-motive.md` §5.

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
(erneut 144 Credits bei Seedance 1.5).
