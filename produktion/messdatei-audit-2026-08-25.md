# Messdatei-Audit 2026-08-25

Vollständige Prüfung aller Zahlenwerte in den Dokumenten dieses Repositories gegen
die eingecheckten Messdateien — ausgelöst durch den Prozessbefund in
[`workflow-gates.md`](workflow-gates.md#prozessbefund-2026-08-25--was-als-gemessen-gilt).

**Verfahren je Wert:** in allen Schreibweisen über alle eingecheckten Daten-
dateien gesucht (Komma und Punkt, gerundet und ungerundet, Prozent und Absolutwert),
dann `git log -S`, dann alle Versionen der vermuteten Messdatei, dann Messdateien
mit anderem Namen. Jeder Fund wurde anschließend von einer zweiten Instanz mit dem
Auftrag gegengeprüft, ihn zu **widerlegen** — nicht ihn zu bestätigen.

**Ergebnis:** 218 Werte geprüft · **150 bestätigt** · 9 unsicher · 59 widerlegt.
Von den bestätigten sind **37** als bindende Vorgabe weitergegeben.

| Kategorie | bestätigt | davon Vorgabe |
|---|---|---|
| **A — unbelegt** | 22 | 3 |
| **B — nicht eingecheckt** | 41 | 6 |
| **C — Widerspruch** | 51 | 3 |
| **D — abgeleitet oder entschieden** | 36 | 25 |

Nicht gemeldet werden Werte, die eine eingecheckte Messdatei deckt.

---

## A — unbelegt

Die Zahl steht in einem Bericht. Es gibt keine Messdatei und keinen Hinweis, dass je gemessen wurde. Der Typ des 129-px-Fehlers.

### `maximal 4 Woerter / "Gewinner 0–4" / Fallzahl 21` — hoch · **als Vorgabe weitergegeben**

**Wo:** `formel/thumbnail-checkliste.md:39 und :107`  
**Wofür:** Bindende Obergrenze fuer die Wortzahl im Thumbnail, angeblich an 21 Gewinner-Thumbnails ausgemessen  
**Messdatei:** keine  

Kein eingechecktes Artefakt fuehrt eine Wortzahl fuer die 90 Feld-Thumbnails. thumb_textmessung.json kennt nur kanal/grp/vid/zeilen/glyphen/glyph_hoehe_pct/kontrast; motiv_inventar.json nur ein binaeres Feld text (0/1); thumb_messung.json nur w/h/bytes/schaerfe; thumb_jobs.json und verlierer_auswahl.json nur Videotitel (nicht Thumbnail-Text). rg -ni "woerter|wortzahl|words" ueber alle Nicht-md-Dateien liefert nur produktion/korpus/* (Skript-Wortzahlen) und produktion/video-0*/thumbnail*_messung.json ("woerter": 3, eigene Thumbnails) — beides deckt "Gewinner 0–4, n=21" nicht. Verschaerfend: der einzige eingecheckte Hinweis auf Gewinner-Textzeilen, regeln/daten/thumbnail_forensik.json, nennt fuer A ('Time To Sleep.', 'Sleep Deep', 'Peaceful Sleep.') und B (TIME TO REST / YOU NEED REST / SLEEP DEEP / JUST SLEEP) ausschliesslich 2- und 3-Wort-Zeilen. Die beobachtete Obergrenze waere also 3; die 4 ist gesetzter Spielraum. Die Zahl ist bindend weitergereicht: produktion/pipeline/thumbnail.py MAX_WOERTER = 4 (bricht mit SystemExit ab), workflow-gates.md Gate 1.4, videos-01-08.md:83, alle vier upload.md.

### `höchstens 4` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:30`  
**Wofür:** Gate 1.4, maximale Wortzahl im Thumbnail — harte Grenze, von thumbnail.py geprueft  

Die Herkunftsaussage bleibt unbelegt. Ich habe alle drei in Frage kommenden Messdateien Feld fuer Feld geprueft: regeln/daten/thumb_textmessung.json (90 Eintraege, Felder kanal/grp/vid/zeilen/glyphen/glyph_hoehe_pct/kontrast — kein Wortfeld), regeln/daten/thumb_messung.json (90 Eintraege, w/h/bytes/schaerfe) und regeln/daten/motiv_inventar.json (text nur als 0/1 plus ratio). regeln/daten/thumb_jobs.json fuehrt Titel, nicht Thumbnail-Text. In keiner eingecheckten Datei steht eine Wortzahl je Konkurrenz-Thumbnail; die Begruendung der Checkliste ('Wortzahl | maximal 4 Wörter | Gewinner 0–4 | Fallzahl 21') ist reine Berichtsprosa. Zwei Entlastungen, die ich dem Fund hinzufuege: (1) Die Grenze selbst ist kein frei schwebender Wert — sie steht als MAX_WOERTER = 4 im eingecheckten produktion/pipeline/thumbnail.py:37 und bricht den Lauf hart ab (Zeile 73/74 raise SystemExit). (2) Die Einhaltung ist gemessen: alle fuenf produktion/video-0*/thumbnail*_messung.json fuehren woerter=3 und woerter_ok=true. Unbelegt ist damit ausschliesslich die empirische Rechtfertigung der 4, nicht ihre Durchsetzbarkeit. Das Gate nennt als Woher korrekt 'Checkliste' und behauptet an dieser Stelle keine Messung.

### `14 Tage` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:74-77`  
**Wofür:** Ausloeserbedingung fuer Gate 2: das aelteste Video muss mindestens 14 Tage alt sein  

Bestaetigt. rg ueber alle Nicht-Bild-Dateien findet '14 Tage' genau einmal, an der gemeldeten Stelle; die drei Treffer von git log -S'14 Tage' betreffen zwei Commits an anderen Dateien und den Commit d36d3b8, der workflow-gates.md anlegt. Eine Reifekurve fuer Impressionen oder CTR existiert in keiner eingecheckten Datei — der Datensatz enthaelt diese Groessen ueberhaupt nicht, was das Gate-2-Kapitel selbst festhaelt ('nur Views sichtbar, keine Impressionen, keine CTR'). regeln/daten/kadenz.json enthaelt Upload-Frequenzen (uploads_pro_woche, wochen, erster_upload), keine Reifezeit. Die Begruendung ist Plausibilitaet, steht aber als harte Ausloeserbedingung. Die Einordnung des Erstpruefers, dass sie praktisch nichts steuert, habe ich nachgerechnet und bestaetigt: produktion/videos-01-08.md:43-52 setzt 01 auf Mo 10.08.2026 und 04 auf Di 25.08.2026 bei durchgehend 5 Tagen Abstand — Video 01 ist beim Erscheinen von Video 04 bereits 15 Tage alt, die Bedingung ist durch die Kadenzentscheidung schon erfuellt. als_vorgabe bleibt true: workflow-gates.md ist in der Aufzaehlung ausdruecklich genannt, und dort ist die Zahl bindend formuliert.

### `rund 4.900 kurze Atempausen von je 0,25 bis 0,4 s` — hoch

**Wo:** `formel/video-formel.md:118`  
**Wofür:** Angebliche Zerlegung des Sprachanteil-Defizits der eigenen Videos in lauter Mikropausen — Kern der Begründung, warum die 97-%-PFLICHT auf 95,0 % abgesenkt wurde  

rg über das gesamte Repo: „4900"/„4.900" trifft nur view_count-Felder in teardown-*_videos.jsonl und SRT-Zeitstempel; „Atempaus" nur in Prosa (video-formel.md:118, bibeltube-wissen.md, upload-checkliste.md:62, ein Kommentar in schritt2_tts.py:278). git log -S"4.900"/"4900" liefert keine Datenfassung. produktion/arbeit/ ist per .gitignore ausgeschlossen, und es wurde nie eine qa_stimme.json eingecheckt. Über den Systembefund hinaus ist die Zahl aber arithmetisch unmöglich, deshalb A statt B: schritt2_tts.py:280-284 rechnet den ausgewiesenen „Sprachanteil (Lücken <1 s zugerechnet)" so, dass ALLE Lücken unter 1,0 s als Sprache gezählt werden. Pausen von 0,25–0,4 s stecken damit definitionsgemäß INNERHALB der 95,3 % und können die verbleibende Lücke von 4,7 % gar nicht erzeugen. Zusätzlich: 12.896,8 s Laufzeit (upload-checkliste.md:51) × 4,4 % = 567 s Lücke gegen 4.900 × 0,25 s = mindestens 1.225 s. Die Obergrenze „0,4 s" ist überdies kein Pipelinewert (gemeinsam.py:149/161 kennt nur min_s=0.25).

### `rund 35 Minuten Rechenzeit` — mittel

**Wo:** `produktion/workflow-gates.md:19`  
**Wofür:** Kosten eines Renderlaufs — traegt die Kernregel 'Kein Rendering, bevor Titel und Thumbnail stehen'  

Bestaetigt — das ist der klarste A-Fall des Satzes. Ich habe alle eingecheckten Artefaktdateien nach Laufzeitfeldern durchsucht (rg 'rechenzeit|dauer_s|laufzeit_s|elapsed' ueber *.json und *.log in produktion/, stimmtest/, teardown/, regeln/): die Treffer sind Clip- und Bettdauern (12,042 s, 60,0 s, 56,0 s) und TTS-Stichproben, keine Renderlaufzeit. produktion/pipeline/render.py:82-83 berechnet zwar genau so eine Zahl, schreibt sie aber nur nach stdout — kein Artefakt, weder im Repo noch in produktion/arbeit/. Das einzige Skript, das eine Rechenzeit persistiert, ist schritt6_srt.py:258 ('rechenzeit_s'), und dessen qa_srt.json liegt in produktion/arbeit/ (.gitignore). Die vier upload.md-Tabellen protokollieren je 14 Renderwerte — Laufzeit des Videos, Dateigroesse, Tempo, Peak, TTS-Zeichen usw. —, eine Rechenzeit ist nicht darunter (an produktion/video-04/upload.md:69-83 Zeile fuer Zeile geprueft). git log -S'35 Minuten' liefert genau einen Commit: d36d3b8, der workflow-gates.md ueberhaupt erst anlegt. Die Zahl existiert im ganzen Repo genau einmal, naemlich an der gemeldeten Stelle. Bestaetigt ist ebenso die Entlastung des Erstpruefers zum zweiten Wert desselben Satzes: '~160.000 TTS-Zeichen' ist gedeckt — produktion/korpus/plan.json + kapitel.json ergeben fuer V1–V8 153.932–165.130 Zeichen, die vier upload.md melden 158.182 / 162.244 / 158.182 / 166.005.

### `11/11 Stichproben` — mittel

**Wo:** `produktion/config.md:117`  
**Wofür:** Behauptete Belegbasis dafuer, dass ein Standmotiv mit sanfter Bewegung PFLICHT ist; traegt zoom = ja im ini-Block und damit zoom_faktor und zoom_zyklus_s.  

Nachgesucht mit "11/11", "11 von 11", "n=11": alle Treffer sind Berichte (formel/video-formel.md:200, teardown/produktions-spec.md:186 und :285, produktion/pipeline/README.md:46, Docstring schritt5_video.py:6, bibeltube-wissen.md:468) - kein Datenartefakt. Zusaetzlich geprueft, was der Erstpruefer nicht erwaehnt: teardown/teardown_batch_20260802_090410/matrix.csv besitzt tatsaechlich eine Spalte visuell (statisch/langsame_bewegung/szenenwechsel, gesetzt in teardown_batch.sh:93-94 per PSNR-Vergleich). Sie deckt den Wert NICHT und widerlegt ihn auch nicht: die Datei hat nur 5 Datenzeilen, alle auf dem Startwert "statisch", und teardown/README.md:25-26 erklaert ausdruecklich "keine Messung, nicht auswerten". Naechstliegender eingecheckter Bewegungsbefund bleibt regeln/daten/stimm_stichprobe.json - dort sind 4 Videos visuell beschrieben (C: 8-Szenen-Rotation, F: statische Huette mit Text-Overlays, G: Stock-Natur, B: ein Gemaelde mit Feuerflackern). Das ist n=4 aus Lauf 2 und stuetzt die Pflichtregel nur in einem Fall. Schwere auf mittel: die Zahl ist unbelegt, die daraus abgeleitete Vorgabe zoom = ja ist unter der aktiven Einstellung videoquelle = ki_clips ohnehin wirkungslos (schritt5_video.py:120 ff. umgeht den Zoom-Zweig), und die Bewegung der aktuell genutzten Clips ist in qa-ki-clips.json gemessen.

### `rund 1,5 Punkte` — mittel

**Wo:** `produktion/config.md:136`  
**Wofür:** Behaupteter systematischer Messversatz zwischen der eigenen Huellkurvenmessung und der 97-%-Marke aus Lauf 1 - die inhaltliche Rechtfertigung dafuer, die Schwelle zu senken statt die eigenen Videos als zu schlecht zu werten.  

Kein eingechecktes Artefakt enthaelt beide Messmethoden auf demselben Audio; produktion/pipeline/qa/ enthaelt nur rhotik_* und pegel_wiedergabe.json, stimmtest/ nur Stimm- und Akustikproben, teardown/ nur die Fremdmessung (matrix_voll.csv sprech_anteil_pct 97,3-100,0 bei n=24). Der Wert 1,5 selbst ist zwar rechnerisch die Differenz der drei eigenen Werte zur 97-%-Marke (97 - 95,3 bis 95,6 = 1,4-1,7), aber diese drei Werte sind ihrerseits Kategorie B - und die eigentliche Behauptung ist nicht die Differenz, sondern ihre Ursache ("liest rund 1,5 Punkte strenger"). Genau die ist ungemessen, und das Repo sagt es selbst: formel/video-formel.md nennt es "die plausibelste Erklaerung des systematischen Abstands, kein nachgewiesener Messversatz" und verlangt als Gegenprobe ein Konkurrenzvideo durch dieselbe Messung; Commit 052d1c0 wiederholt das. In config.md, der maschinell gelesenen Quelle, fehlt der Vorbehalt. als_vorgabe auf false: die 1,5 steht nirgends als Grenze, sie traegt nur die Grenze 95.0.

### `53–243 Wörter` — mittel

**Wo:** `formel/video-formel.md:142`  
**Wofür:** Behauptete Länge der Eingangs-Rahmungen der übrigen Gewinner-Videos; Gegenargument gegen die 400-Wörter-Gebetspflicht  

Bestätigt. „53–243" existiert nur in formel/video-formel.md:142 und bibeltube-wissen.md:410; git log -S"53–243" zeigt nur die beiden Commits, die diese Prosa anlegen (6a19340, 6f69694). Nach einem Rahmungs-Wortzähler gesucht: rg -i „rahmung" über alle Nicht-md-Dateien trifft nur zwei Fließtextstellen in stimm_stichprobe.json. regeln/daten/skript_anatomie.json führt je Video nur die Gesamtwortzahl (39.478 / 24.970 / 47.643 / 25.750) und ein fest geschnittenes 60-s-Fenster hook_60s; dessen Wortzahlen habe ich nachgezählt: 141 / 112 / 150 / 119 für die vier Gewinner-Videos — Bereich 112–150, weder 53 noch 243. Die Transkripte selbst liegen nicht im Repo (produktion/korpus/text/ ist gitignoriert), aus keiner eingecheckten Datei lässt sich der Wert herstellen.

### `A 8/8 und B 13/13` — mittel

**Wo:** `regeln/erfolgsregeln.md:74`  
**Wofür:** Anteil Gewinner-Titel im 'Zustand-plus-Zusage-Muster', Beleg der Regel M4  

Ernsthaft gegengesucht, nichts gefunden: kein Kodier-Artefakt (grep 'zustands|8/8|13/13|Muster' ueber alle Nicht-md-Dateien). Der einzige 13/13-Treffer liegt in regeln/daten/thumbnail_forensik.json und betrifft das THUMBNAIL-Motiv ('identisches Motiv in allen 13 Thumbs'), nicht Titel; ebenso zitiert workflow-gates.md:33 dieses 13/13 nur fuer das Serienmotiv. Am eingecheckten Rohmaterial reproduziert sich die Zahl nicht: mindestens zwei der acht A-Titel tragen keinen Zustand ('Come Little Lamb, Find Rest With Jesus.', 'Let Jesus Give You Rest Tonight'). Das Repo selbst benennt die erste dieser Ausnahmen ausdruecklich — formel/video-formel.md §1 und bibeltube-wissen.md:340: 'Einzige Ausnahme ist A's schwaechster Treffer (Come Little Lamb, 47K)'. Damit ist 8/8 durch den eigenen, spaeter korrigierten Stand widerlegt und die Zeile ein Rest aus dem Erst-Commit 66b4b17. Nicht als Vorgabe weitergereicht: bindend ist in workflow-gates.md 1.3 nur 'einer der 13 belegten Anker'.

### `rund 20 kbit/s` — mittel

**Wo:** `produktion/pipeline/README.md:51`  
**Wofür:** Bitrate der Videospur (Standbild + langsamer Zoom) als Beleg, dass der Zoom "fast nichts kostet"  

Erneut gesucht mit bitrate|kbit|kbps|bit_rate ueber alle eingecheckten *.json/*.jsonl/*.csv/*.log/*.txt: nur vier Treffer, alle in produktion/motive/loops/qa-V{1,2,3,4}.json (183,2 / 199,6 / 234,1 / 198,0 kbps) und alle fuer die Loop-Animation, nicht fuer die Zoom-Bildspur. Keine Version der Historie enthaelt den Wert in einer Datendatei (git log -S"20 kbit" -> nur e59ff94, der Commit des Textes selbst). Zusaetzlich gegengerechnet: bei e59ff94 kannte produktion/config.md noch keinen Schluessel videoquelle (zoom = ja, Standbild-Weg), Video 01 ist also genau der hier gemeinte Fall; die im selben Commit maschinell geschriebene produktion/video-01/upload.md nennt 666,7 MB bei 3:34:57 = 12.897 s -> 413,6 kbit/s gesamt, abzueglich AAC 192k (config.md audio_bitrate) rund 220 kbit/s Bildspur. Das ist Faktor 11 gegen die Behauptung und deckt sich mit den ~200 kbit/s in produktion/motive/README.md:228. ffmpeg/ffprobe sind in dieser Umgebung nicht verfuegbar, ein Nachrendern des 300-s-Zyklus war daher nicht moeglich - es gibt aber keinerlei Datenbasis fuer 20 kbit/s.

### `0,030` — mittel

**Wo:** `produktion/motive/README.md:81`  
**Wofür:** p95-Luminanz des Himmelsbands von V3 — Begruendung, warum die Textvariante auf V3 statt V1 liegt  

Ernsthaft gesucht, nichts gefunden. Zu motiv-V1..V4 existiert in KEINEM Commit je eine Messdatei (git log --all --name-only ueber produktion/motive/*.json: nur text_messung.json, motiv-video-02/03/04_messung.json, loops/qa-V?.json, loops/*/qa-ki-clips.json). Der Wert 0,030 taucht in keiner eingecheckten Nicht-md-Datei auf. Eigene Nachrechnung mit der Luminanzformel aus thumbnail.py: aktuelles V3 oberes Sechstel linear-p95 = 0,0333, altes V3 (bc1876e, der Stand bei Abfassung) = 0,0234 — keiner der beiden Werte ist 0,030. Ich habe zusaetzlich gleitende Baender von 100 bis 270 px Hoehe ueber die volle Breite gescannt, in linearer und in Gamma-Luminanz: nur ein handverlesenes 135-px-Fenster auf dem AKTUELLEN V3 trifft 0,0300. Vor allem ist die Aussage selbst falsch: V3 ist in keiner getesteten Banddefinition das dunkelste Motiv — heute ist V1 dunkler (0,0201), damals waren V2 (0,0124) und V4 (0,0214) dunkler. Restunsicherheit: was genau "durchgehendes Himmelsband" heissen soll, ist nirgends definiert; eine exotische Definition kann ich nicht voellig ausschliessen. A bleibt, weil keine Messdatei existiert und die Zahl an keinem der beiden Bildstaende reproduzierbar ist.

### `unter 110 s (Hook-Länge)` — niedrig

**Wo:** `formel/video-formel.md:389-390`  
**Wofür:** Obergrenze für den optionalen Hook in den Textbausteinen  

Bestätigt. „110" kommt in den Nicht-md-Dateien nur in völlig anderen Zusammenhängen vor (schaerfe 1108.0 in thumb_messung.json, views 110 in katalog_H, psalms 110 in plan.json, f0 110.6 in stimmtest/screen_r2_neu.json). Als Hook-Länge steht die Zahl ausschließlich in formel/video-formel.md:390 und der Kopie bibeltube-wissen.md:658. Ich habe zusätzlich geprüft, ob sie ableitbar wäre: regeln/daten/skript_anatomie.json enthält nur ein fest auf 60 s geschnittenes Textfenster (hook_60s) sowie sprechbeginn_s (3,1 / 2,4 / 2,1 / 0,1) und CTA-Zeitstempel (26/37 s bei A, 33/38 s bei B) — daraus folgt keine Hook-Länge. Die Kapitelmarken in regeln/daten/nexlev/winner_details.json setzen den ersten Vers bei B/166K nach 32 s und bei B/96K nach 59 s, also deutlich unter 110 s. Kein Weg zu dem Wert.

### `4,5:1 (WCAG)` — niedrig

**Wo:** `formel/thumbnail-checkliste.md:45`  
**Wofür:** Externer Vergleichsmassstab, gegen den der eigene 10:1-Wert begruendet wird  
**Messdatei:** keine  

rg -ni "wcag" liefert im gesamten Repo nur zwei Treffer, beide Prosa (formel/thumbnail-checkliste.md:45 und die Kopie in bibeltube-wissen.md:751). rg "4[,.]5" ueber alle Nicht-md-Dateien liefert nur unbeteiligte Zufallstreffer (ratio 4.5 in motiv_inventar.json, schaerfe 1004.5, groesse_kb 2504.5, verspausen_pro_min 4.5). Es gibt im Repo keine Norm- oder Quellenablage. Der Wert ist inhaltlich korrekt (WCAG 2.1 Erfolgskriterium 1.4.3 AA, Normaltext) und wird nirgends als eigene Messung ausgegeben oder als Grenze weitergereicht — deshalb bleibt die Schwere niedrig.

### `12 Woerter / "ab 6 Woertern"` — niedrig

**Wo:** `formel/thumbnail-checkliste.md:60-62`  
**Wofür:** Zusammenbruchsschwelle im 160x90-Feed-Test und Wortzahl des Extremfalls (Kanal D)  
**Messdatei:** nur die 54 Views sind gedeckt (motiv_inventar.json, D_GodMessageToday/FZm0s3-S3Tg)  

Bestaetigt und beim Gegenpruefen sogar verschaerft. (1) Keine Wortzahl fuer Feld-Thumbnails in irgendeiner eingecheckten Datei (siehe Fund "maximal 4 Woerter"). (2) Der zitierte Text hat ausgezaehlt 13 Woerter, nicht 12. (3) Neu: das Thumbnail, dem die Stelle die 12 Woerter zuschreibt, ist ueber die genannten 54 Views eindeutig identifizierbar (D_GodMessageToday/FZm0s3-S3Tg, BEST, 54) — und thumb_textmessung.json misst fuer genau dieses Thumbnail zeilen=0, glyphen=0, also gar keinen erfassten Text; motiv_inventar.json fuehrt dasselbe Bild dagegen mit text=1. Zwei eingecheckte Messdateien widersprechen sich hier, und keine von beiden stuetzt "12 Woerter in einem Kasten". (4) Der hoechste glyphen-Wert im gesamten Datensatz ist 25; der zitierte Satz hat 66 Zeichen — kein Datensatz koennte ihn abbilden. Die Schwelle "ab 6 Woertern" wird nirgends als Grenze weitergereicht (bindend ist max. 4), die 54 Views sind gedeckt.

### `2–4 Woerter (B-Serie durchgehend) / B-Serie 13/13 lesbar` — niedrig

**Wo:** `formel/thumbnail-checkliste.md:56-57 und :144`  
**Wofür:** Belegte Lesbarkeitsspanne im Feed-Test  
**Messdatei:** nur "1 oder 2 Zeilen" gedeckt (thumb_textmessung.json, Feld zeilen)  

Der Teilsatz "eine Zeile oder zwei" ist gedeckt: thumb_textmessung.json gibt fuer die 13 B-Thumbs zeilen=1 (9x) und zeilen=2 (4x). Die Wortzahl 2–4 und das Lesbarkeitsurteil 13/13 sind es nicht — es gibt kein Wortfeld und kein Lesbarkeitsfeld, und feedtest_GEWINNER.png / feedtest_VERLIERER.png sind Bilder, also Artefakt ohne Zahl. Zusatzbefund gegen die Zahl: die einzige eingecheckte Aufzeichnung der B-Textzeilen (thumbnail_forensik.json: TIME TO REST / YOU NEED REST / SLEEP DEEP / JUST SLEEP) enthaelt nur 2- und 3-Wort-Zeilen; die Obergrenze 4 ist im Beleg nicht zu sehen. Wird nicht als Grenze weitergereicht.

### `>= 150 KB (Export) / Gewinner-Median 237 KB` — niedrig

**Wo:** `formel/thumbnail-checkliste.md:129`  
**Wofür:** Mindestdateigroesse beim Thumbnail-Export  
**Messdatei:** nur der Median 237 KB ist gedeckt (regeln/daten/thumb_messung.json, Feld bytes, Gruppe GEW)  

Kategorie korrigiert von D auf A: die 150 KB sind im Dokument NICHT als Entscheidung gekennzeichnet, sie stehen ohne jede Herleitung in einer Zeile, deren Klammer einen echten Messwert nennt. Der Median 237 KB ist gedeckt (thumb_messung.json, GEW n=21, Median 242.892 Byte = 237,2 KiB). Die 150 KB kommen in keiner Messdatei vor; ihr einziger weiterer Fundort ist der Docstring von produktion/pipeline/thumbnail.py Zeile 11 — nach der Definition Bericht, nicht Messdatei, und im Code ist keine Groessenpruefung implementiert (nur CAP_MIN_PCT, KONTRAST_MIN, MAX_WOERTER). Gegenbefund zur Plausibilitaet: zwei der 21 Gewinner-Thumbnails liegen unter der Schwelle (136.047 und 147.114 Byte), die Grenze liegt also NICHT vollstaendig innerhalb des belegten Musters. Praktisch folgenlos, weil die eigenen Exporte bei 2.374–2.980 KB liegen.

### `Klick-Appelle n=4, bestes 54 Views` — niedrig

**Wo:** `formel/thumbnail-motive.md:96`  
**Wofür:** Verlierer-Bauform in der Ausschlusstabelle  
**Messdatei:** nur die 54 Views (motiv_inventar.json, D_GodMessageToday/FZm0s3-S3Tg)  

Anders als beim Alarm-Design finde ich hier kein Feld, das n=4 mit Maximum 54 reproduziert. Kein eingechecktes Artefakt haelt den Thumbnail-TEXTINHALT maschinenlesbar fest — thumb_textmessung.json fuehrt nur Metrik (zeilen/glyphen/hoehe/kontrast), motiv_inventar.json nur ein binaeres Feld text. Die naheliegende Ersatzquelle, die Videotitel in motiv_inventar.json und verlierer_auswahl.json, enthaelt zwar aehnliche Formeln ("GOD SAID: DON'T CLICK AWAY...", "Give Me 2 Minutes Or You Might Miss..."), das sind aber Videotitel, nicht Thumbnail-Texte, und deren bester Wert liegt bei 3 Views, nicht bei 54. Verschaerfend: das 54-Views-Thumbnail (D/FZm0s3-S3Tg) ist in thumb_textmessung.json mit zeilen=0/glyphen=0 erfasst, traegt dort also gar keinen erfassten Text. Der Views-Wert 54 selbst ist in motiv_inventar.json belegt.

### `0/90 (anonyme schlafende Gestalt als Hauptmotiv)` — niedrig

**Wo:** `formel/thumbnail-motive.md:199-202`  
**Wofür:** Beleg, dass die in videos-01-08.md offen gelassene anonyme Figur im Feld unbelegt ist  
**Messdatei:** keine — motiv_inventar.json fuehrt fig n=2, ohne Unterscheidung  

motiv_inventar.json kennt keine Kategorie fuer eine anonyme schlafende Gestalt; das naechstliegende Kuerzel ist fig (n=2, beide E_QuietMind WORST, 52 und 38 Views). Der Fund haelt und wird durch zwei interne Widersprueche gestuetzt: (1) die Kategorienlegende desselben Dokuments (Zeile 32) beschreibt fig ausdruecklich als "betende Frauen; Schlaefer an Kirche" — ein Schlaefer als Hauptmotiv waere damit 1/90; (2) Zeile 97 fuehrt "weibliche Hauptfiguren | 1 | 52 Views", also ist nur EINER der beiden fig-Datensaetze eine Frau, der andere (38 Views) muss der Schlaefer sein; (3) Zeile 43-44 formuliert vorsichtiger "kommt praktisch nicht vor", Zeile 201 dann absolut "0/90". Aufloesbar allein durch Sichtung von regeln/daten/thumbs/ — Bilder sind Artefakt, aber keine Messdatei. Wird nicht als Grenze weitergereicht.

### `4/8` — niedrig

**Wo:** `regeln/erfolgsregeln.md:91`  
**Wofür:** Anteil Verlierer mit 'klar generisch/maschinellem' Skript, Beleg der Regel M5  

Ernsthaft gegengesucht: kein Kodier- oder Zaehl-Artefakt (grep 'generisch|maschinell' ueber alle Nicht-md-Dateien liefert nur zwei Prosa-Fazits in stimm_stichprobe.json zu C und F). Der Nenner 8 ist nicht erhoben — skript_anatomie.json fuehrt nur 6 Eintraege mit label VERLIERER (C, F, D, G, H, I) plus J als SONDERFALL; fuer E existiert gar kein Transkript ('KEIN TRANSCRIPT: Not Available'). Der Zaehler 4 ist nirgends aufgeschluesselt: der Text nennt namentlich nur drei Faelle (C, F, D). Die Einzelbelege sind dagegen woertlich gedeckt (C 'mandible'-Psalm und verstuemmelter CTA in stimm_stichprobe.json und skript_anatomie.json; F 'reine Atem-/Beruhigungs-Meditation ohne Schriftbezug'; D Droh-Hook), ebenso die Teilangabe '4 geprueften Transkripten' bei A+B (2x A, 2x B in skript_anatomie.json). Nur die Quote selbst ist unbelegt.

### `CTA 1 erst bei 105 s` — niedrig

**Wo:** `produktion/pipeline/README.md:72-73`  
**Wofür:** Kontrafaktische Rechnung, wo CTA 1 laege, waere das Gebet vor die CTAs gesetzt worden  

Nachgerechnet mit allen drei verfuegbaren Basen, keine ergibt 105: mit der gemessenen Gebetsdauer (70,16 s aus video-01.srt) plus Hookende 22,62 s waeren es 92,8 s; mit der im selben Absatz behaupteten Dauer 112 s waeren es 133 s; mit der Zeitleiste des Dokuments (Gebet 38 -> 116 s = 78 s) waeren es 99 s. git log -S ueber alle Schreibweisen findet den Wert nur in e59ff94, dem Commit des Textes selbst, nie in einer Datendatei. Es ist eine frei gesetzte Illustrationszahl in einer kontrafaktischen Aussage - schwere deshalb niedrig, aber unbelegt.

### `4294967295` — niedrig

**Wo:** `stimmtest/README.md:45-47`  
**Wofür:** Angeblich vom API-Antwort-Header gemeldetes Parallelitaets-Limit (ratelimit-limit-concurrency) von Fish Audio  
**Messdatei:** keine — einziger Treffer repoweit und historieweit ist stimmtest/README.md:46 (Commit 6cf9f8e)  

Nicht zu widerlegen. git grep ueber ALLE eingecheckten Dateien: einziger Treffer ist der README-Satz selbst. git log --all -S'4294967295': einziger Commit ist 6cf9f8e, genau der Commit, der den README anlegt — der Wert hat also nie in einer anderen Datei oder Version gestanden. Verschaerfend: KEIN eingechecktes Skript kann diese Zeile je erzeugt haben. gen_par.py:36-40 und gen_r2.py oeffnen die Antwort per urllib und lesen ausschliesslich f.read(); auf das Header-Objekt wird nirgends zugegriffen, und keins der Logs (gen_par.log, gen_v2.log, generate.log, qa.log) enthaelt einen Header-Mitschnitt. Die Zahl kann nur aus einem nicht protokollierten Handversuch stammen. Bestaetigt auch der Gegenbeleg: '9 gleichzeitige Anfragen' ist durch gen_par.py:62 (max_workers=9) und gen_par.log (39/39 ok, keine FEHLER-Zeile) gedeckt. Anschlussrisiko, das der Erstfund nicht nennt: produktion/config.md setzt tts_parallel = 12 — hoeher als die einzige im Repo belegte, tatsaechlich erprobte Parallelitaet von 9. Die einzige Rechtfertigung fuer diesen Sprung ist der unbelegte Header-Satz.

### `HTTP 402` — niedrig

**Wo:** `stimmtest/README.md:43`  
**Wofür:** Angeblicher Fehlercode, mit dem s2.1-pro ohne bezahltes Guthaben antwortet — Begruendung fuer die Wahl von s2.1-pro-free  
**Messdatei:** keine — kein Log, kein Skriptlauf und keine Historieversion enthaelt eine HTTP-Statuszeile  

Nicht zu widerlegen. '402' kommt in stimmtest/ ausser im README-Satz nur in zwei Fish-Voice-IDs vor (voice_shortlist.json:4126, :4474 — Zufallstreffer in Hexstrings). git log --all -S'402' -- stimmtest: nur 6cf9f8e, der Commit des README. Zusaetzliches Gegenargument, das den Fund haerter macht: haette ein eingechecktes Skript je einen 402 gesehen, stuende er im Log — gen_par.py:49-51 faengt jede Exception und gibt sie als 'FEHLER {e}' aus, was bei urllib woertlich 'HTTP Error 402: Payment Required' ergaebe; gen_par.log enthaelt keine einzige FEHLER-Zeile. Und kein eingechecktes Skript fordert je s2.1-pro an: gen_par.py:14 und gen_r2.py setzen den Modell-Header hart auf 's2.1-pro-free'. Belegt ist nur die getroffene Wahl (auch produktion/config.md tts_modell), nicht der Grund. Schwere bleibt niedrig: die Zahl wird nirgends als Grenze weitergereicht, es ist eine Begruendungsanekdote.

---

## B — nicht eingecheckt

Die Zahl stammt nachweislich aus einem Skript- oder Pipelinelauf, dessen Ausgabe nicht im Repository liegt (fast immer `produktion/arbeit/`). Nachvollziehbar, aber nicht prüfbar.

### `11 von 11 (Stichproben mit Bewegung); „11 multimodale Stichproben aus Lauf 1"` — hoch · **als Vorgabe weitergegeben**

**Wo:** `formel/video-formel.md:188 und :200`  
**Wofür:** Beleg-n für die PFLICHT „Ein Standmotiv mit sanfter Bewegung, kein Szenenschnitt"  

Bestätigt. Die Aussage steht ausschließlich in Prosa und Docstrings: teardown/produktions-spec.md:22/183/186/285, formel/video-formel.md:188/200, bibeltube-wissen.md:456/468, formel/thumbnail-motive.md:6, produktion/pipeline/README.md:46, produktion/config.md:117 und der Docstring von produktion/pipeline/schritt5_video.py:6. Einzige eingecheckte Spalte zum Bildverhalten bleibt matrix.csv/„visuell" — sie steht in allen 5 Zeilen auf „statisch", und teardown/README.md:26 sowie produktions-spec.md:32 erklären diesen Startwert ausdrücklich für „keine Messung, nicht auswerten". teardown/run.log und teardown_batch.sh belegen nur den fehlgeschlagenen frames/-Download (403), keine Ausgabe der multimodalen Analyse; nexlev_supplement.json enthält nur Metadaten. Dass der Lauf stattgefunden hat, ist glaubhaft (produktions-spec.md nennt kanalgenaue Schnittintervalle: Grace Beyond Prayer ~25 s, SleepCodex 10–20 s, Night Psalms ~35 s, Marktplatz-Schnitte alle 3–5 s) — nur die Ausgabe fehlt. Die 4 Szenenanalysen aus Lauf 2 sind dagegen in regeln/daten/stimm_stichprobe.json belegt (C, F, G, B-Nachtrag).

### `95,6 % / 95,3 % / 95,3 % Sprachanteil und 1,42 / 1,38 / 1,46 s längste Pause (Video 01–03), daraus „rund 1,5 Punkte" und „Faktor 13"` — mittel · **als Vorgabe weitergegeben**

**Wo:** `formel/video-formel.md:111-113, :118, :132`  
**Wofür:** Eigene Renderwerte, mit denen die Sprachanteil-Warnschwelle von 97,0 % auf 95,0 % gesenkt wurde  

rg über alle Nicht-md-Dateien nach 95,6/95.6/95,3/95.3/1,42/1.42/1,38/1.38/1,46/1.46: kein einziger Treffer mit Bezug zum Sprachanteil (die Treffer sind dauer_sd_h in kanal_dna.json, ratio in motiv_inventar.json, frameschritt-Werte in den Loop-QA-Dateien, f0_med in stimmtest/probe_akustik.json, Kanal-Median-Faktoren in auswertung_population.txt). Die Werte stehen nur in Markdown: video-formel.md:111-113, video-01/upload.md:190-191, video-02/upload.md:182-183, video-03/upload.md:133-134, video-01/upload-checkliste.md:55/57, produktion/config.md:135. Erzeugt werden sie nachweislich von produktion/pipeline/schritt2_tts.py:313-316 (Felder sprachanteil_vergleichbar_pct, laengste_pause_s) nach produktion/arbeit/<video>/qa_stimme.json; produktion/arbeit/ steht in .gitignore und es ist nie eine solche Datei eingecheckt worden (git log --diff-filter=A liefert nichts). Maschinell erzeugt, plausibel, aber nicht prüfbar — die Ableitungen „1,5 Punkte" und „Faktor 13" (20 s / ~1,5 s) erben diesen Status. als_vorgabe true bleibt: config.md:135-139 zitiert die drei Werte und das Band 1,38–1,46 s wörtlich als Begründung für die bindende Schwelle sprachanteil_min_pct = 95.0.

### `11 von 11 Stichproben / 11/11` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/pipeline/README.md:46; produktion/pipeline/schritt5_video.py:6; produktion/pipeline/schritt4_bild.py:9`  
**Wofür:** Stichprobe, die belegen soll, dass alle Gewinner-Videos Bewegung im Bild haben; traegt die Entscheidung fuer Zoom bzw. KI-Loop statt Standbild  
**Messdatei:** regeln/daten/stimm_stichprobe.json (B_2Sh-wNaOCrY_NACHTRAG) deckt die Bewegung qualitativ, nicht die Fallzahl 11/11  

Die Abwesenheit ist bestaetigt: keine eingecheckte Datei enthaelt die 11 multimodalen Videoanalysen. Geprueft: regeln/daten/motiv_inventar.json (90 Eintraege, nur Thumbnail-Merkmale wie lamm/feuer/warmlicht, kein Bewegungsfeld), regeln/daten/kanal_dna.json, thumbnail_forensik.json, skript_anatomie.json, teardown/auswertung_matrix.txt, matrix.csv und matrix_voll.csv sowie alle *_videos.jsonl. Die Spalte visuell in matrix.csv steht in allen 5 Zeilen auf dem Default statisch (teardown_batch.sh:64) - produktions-spec.md:0 erklaert das selbst ausdruecklich fuer keine Messung. ABER: Einordnung von A auf B korrigiert. (1) teardown/produktions-spec.md:22 und :180-218 dokumentieren den Lauf mit Methode, Umfang (7 der 8 TOP, 4 FLOPs, je 60-120 s) und kanalindividuellen Einzelbefunden (Schnittraten ~25 s / 10-20 s / 35 s, namentliche Wasserzeichen HLL, SLEEP BIBLE, SLEEPCODEX, Night Psalms) - das ist ein dokumentierter Werkzeuglauf ohne eingecheckte Ausgabe, nicht eine Zahl ohne jeden Messhinweis. (2) Ein gleichartiger Lauf IST eingecheckt (regeln/daten/stimm_stichprobe.json, Higgsfield/NexLev-Videoanalyse) - nur eben ein anderer, spaeterer. (3) Der getragene Inhalt ist qualitativ gedeckt: stimm_stichprobe.json, Eintrag B_2Sh-wNaOCrY_NACHTRAG: 'Einzige Bewegung: Feuerflackern, langsam sinkende Sonne. KEIN Szenenwechsel.' Unbelegt bleibt allein die exakte Fallzahl 11/11. Schwere deshalb von hoch auf mittel.

### `72 Credits / 18 Credits je Clip` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/motive/README.md:285-288`  
**Wofür:** Kosten der vier KI-Clips fuer Video 02, Grundlage der Kostenplanung Videos 03-08  

Widerlegungsversuch gescheitert: es existiert in regeln/daten/, produktion/, teardown/ und stimmtest/ kein einziges Kosten-, Credit- oder Transaktionsartefakt, auch nicht in der Historie. Das zitierte "Transaktionsprotokoll" ist ein Plattform-Beleg (Higgsfield) ausserhalb des Repos. Verschaerfend: fuer genau diesen V02-Lauf nennt der eigene Commit 072ef0c "144 Credits", waehrend der Bericht 72 sagt — die beiden Repo-eigenen Aufzeichnungen widersprechen sich, aufloesbar nur ueber den spaeteren Commit 126407a ("laut get_cost 3 Credits je Sekunde" = 36/Clip Liste, "abgerechnet wurden durchgaengig 18"). Weitergabe als Vorgabe bestaetigt: produktion/video-01/upload-checkliste.md:78 fuehrt "(~72 Credits)" als Planzahl fuer jede weitere Motivvariation.

### `2` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/video-01/upload.md:196`  
**Wofür:** Anzahl CTA je Video  
**Messdatei:** produktion/video-01/untertitel.srt (2 CTA-Kacheln) · vorlage.py:167 erzwingt genau 2  

Formal bestaetigt (skript.json in produktion/arbeit/), inhaltlich trivial gedeckt: produktion/pipeline/vorlage.py:167-168 bricht ab, wenn die Vorlage nicht genau 2 CTA hat — der Wert ist eine Konstante der Vorlage, keine unabhaengige Messung. Fuer V01 in der eingecheckten untertitel.srt nachvollziehbar (Kachel 6-7 Kommentar-CTA, Kachel 8 Abo-CTA, ab Kachel 9 das Gebet). Die Vorgabe cta_max = 2 (config.md:143) ist belegt.

### `1920x1080 @ 24 fps` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/video-01/upload.md:187`  
**Wofür:** Aufloesung und Bildrate der vier Renderlaeufe  
**Messdatei:** produktion/motive/loops/ki/qa-ki-clips.json (und ki-v02/-v03/-v04) — 1920x1080 @ 24.0 fps fuer die Quellclips aller vier Videos  

Formal bestaetigt (qa_video.json in produktion/arbeit/), praktisch gedeckt — und fuer V01 besser als im Fund behauptet: V01 wurde laut Commit e27e58d mit den KI-Clips neu montiert, deren Quellmessdatei produktion/motive/loops/ki/qa-ki-clips.json fuer alle vier Clips breite 1920, hoehe 1080, fps 24.0 fuehrt (eigene Pruefung). Dasselbe fuer ki-v02/-v03/-v04. Dazu config.md:91-93 (breite/hoehe/fps) als maschinell gelesener Block. Schwere niedrig.

### `-0,13 dBFS` — mittel

**Wo:** `produktion/config.md:71`  
**Wofür:** Angeblicher Spitzenpegel des fertigen Mixes von Video 02; einzige Begruendung dafuer, peak_max_dbfs von -0,3 auf -1,0 zu aendern (harte Vorgabe, von schritt3_bett.py gelesen).  

Gegenpruefung bestaetigt die Nichtauffindbarkeit: rg "-0[.,]13" ueber das gesamte Repo (inkl. aller json/jsonl/csv/log/txt) liefert genau einen Treffer, naemlich diese Kommentarzeile. git log -S"-0,13" -> nur a9b353d (der Commit, der die Zeile einfuegte), git log -S"0.13" -> nur zwei thumbnail-bezogene Commits ohne dBFS-Bezug. Kein geloeschtes qa-Artefakt in der Historie (git log --diff-filter=D zeigt nur den entfernten recherche/-Baum). Auch die neu eingecheckte produktion/pipeline/qa/pegel_wiedergabe.json enthaelt keinen Peak-Wert. ABER: die Einordnung C ist falsch, und das Code-Argument des Erstpruefers kippt bei genauer Lesung ins Gegenteil. schritt3_bett.py:174-179 misst zuerst den ROH-Peak, bildet skal = min(1.0, ziel_peak/spitze) und gibt den Rohwert nur auf stdout aus ("Spitze vor Skalierung %.2f dBFS"); protokolliert wird in qa_mix.json/upload.md ausschliesslich der Peak NACH der Skalierung. Genau -0.3 in produktion/video-02/upload.md:185 ist nur erreichbar, wenn der Rohpeak UEBER -0,3 lag (sonst bliebe der niedrigere Istwert stehen, wie bei V01 -1.61 und V04 -1.18). Ein Rohpeak von -0,13 ist damit nicht nur plausibel, sondern durch den eingecheckten Endwert indirekt gefordert. Es gibt also keine Messdatei mit ABWEICHENDEM Wert fuer dieselbe Groesse (kein C), sondern einen Renderwert ohne eingecheckte Ausgabe (B). Sachlich falsch bleibt die Prosa: das Video "landete" bei -0,3, nicht bei -0,13, und der Halbsatz "der gemessene Spitzenwert lag schon darunter" widerspricht dem eigenen Code.

### `95,6 / 95,3 / 95,3 %` — mittel

**Wo:** `produktion/config.md:135`  
**Wofür:** Sprachanteil der drei eigenen Videos 01-03; einzige Grundlage der Absenkung sprachanteil_min_pct 97,0 -> 95,0.  

Kein Treffer fuer 95[.,]6 / 95[.,]3 in eingecheckten Datendateien. Herkunft bestaetigt: schritt7_paket.py:154-156 schreibt qs['sprachanteil_vergleichbar_pct'] aus qa_stimme.json (schritt2_tts.py:314), und produktion/arbeit/ existiert im Arbeitsbaum gar nicht mehr - der Wert ist nicht nachrechenbar. Eigener Widerlegungsversuch ueber ein anderes eingechecktes Artefakt: aus den Untertiteldateien produktion/video-0*/video-0*.srt habe ich die Kachelabdeckung mit derselben Definition berechnet (Luecken <1 s als Sprache gezaehlt) und erhalte 94,6 / 94,2 / 96,8 / 96,9 % fuer V01-V04. Groessenordnung passt, die Einzelwerte decken sich aber nicht (V03 waere 96,8 statt 95,3), und die SRT-Kacheln sind eine andere Messgrundlage als die Huellkurve - das deckt den Bericht also nicht. Bleibt B: maschinell erzeugt, nicht pruefbar. als_vorgabe auf false gesetzt: bindende Grenze ist 95.0, nicht 95,6/95,3.

### `0.0 s` — mittel

**Wo:** `produktion/video-01/upload.md:188`  
**Wofür:** Ton-Versatz (A/V-Sync) der vier Renderlaeufe; in der Checkliste zusaetzlich "kreuzkorreliert bei t = 1:47:36"  
**Messdatei:** produktion/pipeline/schritt5_video.py:171 — Messpunkt ist min(3600, gesamt/2) = 1:00:00, nicht 1:47:36  

Bestaetigt und verschaerft. Der Versatz 0.0 s stammt aus qa_video.json['sync_versatz_s'] (produktion/arbeit/) und ist nicht pruefbar — B. Der Zusatz in der Checkliste ist dagegen nachweislich falsch und faellt unter A: schritt5_video.py:171 ruft sync_pruefen(ziel, mix, bei_s=min(3600.0, gesamt/2)) auf. Bei 12.896,8 s Laufzeit ist gesamt/2 = 6448 s, das Minimum also 3600 s — kreuzkorreliert wurde bei t = 1:00:00, nicht bei 1:47:36. Die Version zum Renderzeitpunkt (git show e59ff94:produktion/pipeline/schritt5_video.py:133) ist identisch. "1:47:36" (6456 s) trifft auch gesamt/2 nicht (das waere 1:47:28) und steht in keiner Datei. Ein erfundenes Messdetail an einem sonst plausiblen Wert.

### `2,83–3,14` — mittel

**Wo:** `produktion/motive/README.md:253 und 304`  
**Wofür:** Uebergangsschritt Clip zu Clip (mittl. |Δ|) ueber alle 16 Paare der V01-KI-Clips; dient als Vergleichsbasis fuer Video 02  

Bestaetigt. produktion/motive/loops/ki/qa-ki-clips.json vollstaendig gelesen: die Datei ist eine blanke Liste von vier Clip-Objekten (breite, hoehe, fps, frames, dauer_s, groesse_mb, erster_vs_letzter_mad/_max, drift_*, start_/ende_vs_standbild_mad) — kein Schluessel "uebergaenge" und keine 16 Paare, weder heute noch in ihrer einzigen Vorversion (git log: nur e27e58d). Erst ki-v02/qa-ki-clips.json fuehrt "uebergaenge" mit allen 16 Paaren. Der Wert steht nur in der Commit-Nachricht e27e58d; 072ef0c bestaetigt selbst, dass die Messung "bei V01 noch nebenher lief und damit nicht wiederholbar" war. Eigene Nachrechnung nicht moeglich: im Container sind weder ffmpeg/ffprobe noch cv2, av oder imageio-ffmpeg vorhanden, ein H.264-Dekoder fehlt also (ich konnte nur die MP4-Container selbst parsen).

### `1,40–1,53` — mittel

**Wo:** `produktion/motive/README.md:254 und 305`  
**Wofür:** Normaler Frame-zu-Frame-Schritt innerhalb der V01-KI-Clips; Nenner der Kennzahl "Naht / normaler Schritt"  

Bestaetigt. Die Felder frameschritt_median und frameschritt_max fehlen in allen vier Clip-Objekten von loops/ki/qa-ki-clips.json und existieren erst ab ki-v02 (dort 1.705/1.443/1.423/1.415 als Median). ki_clip_pruefung.py hat die Messung laut git log erst in 072ef0c bekommen. Der Wert stammt aus dem Nebenlauf, dessen Ausgabe nie eingecheckt wurde. Nachrechnung mangels Dekoder nicht moeglich.

### `1,38-1,46 s` — niedrig

**Wo:** `produktion/config.md:138`  
**Wofür:** Laengste gemessene Pause der eigenen Videos, als Beleg dafuer angefuehrt, dass die Schutzregel laengste_pause_max_s = 20.0 weit eingehalten wird.  

Suche nach 1[.,]38 / 1[.,]42 / 1[.,]44 / 1[.,]46 in allen eingecheckten Datendateien: nur sachfremde Treffer (kanal_dna.json dauer_sd_h 1.46, qa-V2.json naht_schritt_mad 1.4696, ki-v03 frameschritt_max 1.463, probe_akustik.json f0_med 91,46, auswertung_population.txt "1.38x Kanal-Median"). Herkunft bleibt qs['laengste_pause_s'] aus qa_stimme.json in produktion/arbeit/ (schritt7_paket.py:157) - nicht eingecheckt, Verzeichnis existiert nicht einmal. Eigener Gegencheck an einem eingecheckten Artefakt: die groessten Luecken zwischen Untertitelkacheln betragen V01 11,91 s, V02 21,12 s (00:10:39, zwischen "The LORD, our God, will cut them off." und "Psalm ninety-five."), V03 1,70 s, V04 6,70 s. Das ist eine andere Messgroesse (ASR-Kacheln statt Huellkurve) und widerlegt die 1,38-1,46 s daher nicht - es zeigt aber, dass es keinen eingecheckten Beleg in diese Richtung gibt und mindestens ein eingechecktes Artefakt in die andere weist. Die 20-s-Grenze selbst ist durch matrix_voll.csv (max_pause_s 0,0-16,7 bei n=24) gedeckt.

### `2163 px · 1624 px · 1923 px · 1606 px · 323 px zu breit · 83 px zu breit · Rand 148 px` — niedrig

**Wo:** `produktion/videos-01-08.md:796-805`  
**Wofür:** Textbreiten fuer Video 07 bei 125 px Versalhoehe in FreeSerif Bold - begruenden die verbindliche Kuerzung von REST WITHOUT STRESS auf NO MORE STRESS  

Formal bestaetigt: es existiert kein produktion/video-07/, keine Messdatei traegt diese Werte, und die Suche nach \b(2163|1624|1923|1606)\b in allen Nicht-.md-Dateien trifft nur SRT-Zeilennummern und rhotik_referenz.json (f3_min 1624.0, sachfremd). ABER die Einordnung "nachvollziehbar, aber nicht pruefbar" ist widerlegt - ich habe alle Werte exakt reproduziert: PIL + /usr/share/fonts/truetype/freefont/FreeSerifBold.ttf @ 184 px (erster Eintrag der Fontkette in produktion/pipeline/thumbnail.py:31, Versalhoehe H = 125 px = 11,57 %) ergibt REST WITHOUT STRESS 2163 px (323 ueber 1840), NO MORE STRESS 1624 px (Rand 148 px), NO STRESS TONIGHT 1923 px (83 ueber), LET GO TONIGHT 1606 px - Ziffer fuer Ziffer identisch. Gegenprobe: dieselbe Methode reproduziert auch alle eingecheckten Werte exakt (V01 1787/1807, V02 1726, V03 1609, V04 1548, und die noch ungebauten V05 1328, V06 1565, V08 1750 aus motive/README.md). Die 1840 px verfuegbare Breite ist eingecheckter Code (thumbnail.py:69, rand_min=40 bei 1920 px). Schwere von mittel auf niedrig gesenkt: die Zahlen sind deterministisch und jederzeit nachrechenbar, ein Fabrikationsrisiko wie beim 129/11,94-Vorfall besteht hier nicht.

### `1896 px · 56 px zu breit` — niedrig

**Wo:** `produktion/videos-01-08.md:490-494`  
**Wofür:** Breite der verworfenen Thumbnail-Zeile NO MORE THINKING fuer Video 04 - begruendet die verbindliche Kuerzung auf THINK NO MORE  

Formal bestaetigt: \b1896\b trifft ausserhalb der .md-Dateien nur SRT-Zeilennummern; die verworfene Zeile wurde nie gebaut, also existiert keine Messdatei. Die Einordnung "nicht pruefbar" ist aber widerlegt: mit FreeSerifBold.ttf @ 184 px (Versalhoehe 125 px = 11,57 %) messe ich NO MORE THINKING = 1896 px, exakt 56 px ueber den 1840 px, die sich aus 1920 - 2x40 ergeben (rand_min=40 in produktion/pipeline/thumbnail.py:69, eingecheckter Code). Das Ergebnis der Kuerzung ist ohnehin voll gedeckt: produktion/video-04/thumbnail_messung.json fuehrt text THINK NO MORE, textbreite_px 1548, rand_je_seite_px 186, versalhoehe_px 125, versalhoehe_pct 11.57, fontgroesse_px 184 - und meine Nachrechnung liefert fuer THINK NO MORE ebenfalls 1548 px. Nebenbefund zum Vorfall: die Versalhoehe von FreeSerifBold @ 184 px betraegt gerechnet 125 px = 11,57 %, nie 129 px / 11,94 %. Schwere auf niedrig gesenkt.

### `11 multimodale Videostichproben / 5 der 11 Ein-Szenen-Loops / 4 Szenenanalysen` — niedrig

**Wo:** `formel/thumbnail-motive.md:5-6, :152, :159-160`  
**Wofür:** Datenbasis fuer Abschnitt 4 "Videospur vs. Thumbnail" und fuer die Schlussfolgerung "Du brauchst EIN Motiv"  
**Messdatei:** keine Messdatei; Prosaquelle fuer 11 / 5 von 11 / 3–5 s: teardown/produktions-spec.md:185-196  

Bestaetigt. git ls-files teardown/ zeigt nur Videolisten (*.jsonl), matrix.csv/matrix_voll.csv, run.log, refill.log, nexlev_supplement.json, ids.txt, Kontaktboegen und Thumbnails — keine Datei mit Szenen-, Schnitt- oder Bewegungsdaten. rg -ni "szenenanalyse|ein-szenen" ueber alle Nicht-md-Dateien liefert nichts Einschlaegiges. Die Zahlen 11, "5 der 11" und "3–5 s" stehen tatsaechlich in teardown/produktions-spec.md Zeilen 185–196, also in Prosa: maschinell erzeugt (multimodale Videoanalyse-Laeufe), aber ohne eingecheckte Ausgabe. Praezisierung gegen den Erstpruefer: die "4 Szenenanalysen aus Lauf 2" stehen NICHT in produktions-spec.md — dort ist ausschliesslich von den 11 Stichproben die Rede; sie werden nur in formel/thumbnail-motive.md:5-6 und formel/video-formel.md:188 behauptet. Fuer diesen Teilwert gibt es also nicht einmal eine Prosaquelle ausserhalb der Berichte selbst.

### `2:30 ohne Schnitt (Szenenanalyse B #3)` — niedrig

**Wo:** `formel/thumbnail-motive.md:157-158`  
**Wofür:** Einzelbeleg fuer den statischen Ein-Szenen-Loop bei Kanal B  
**Messdatei:** keine — auch teardown/produktions-spec.md enthaelt weder "2:30" noch die Szenenanalysen aus Lauf 2  

Bestaetigt und leicht verschaerft. rg "2:30" ueber alle Nicht-md-Dateien liefert nur Zufallstreffer (SRT-Zeitmarken der eigenen Videos, duration_string "2:30:09" in teardown-Videolisten) — nichts, was eine Schnittlaenge waere. rg "Szenenanalyse|statisches Gemaelde|Feuerflacker" findet ausserhalb der Berichte nichts. teardown/produktions-spec.md, das als Quelle zitiert wird, enthaelt die Stelle nicht; es beschreibt in Abschnitt d nur die 11 Stichproben aus Lauf 1. Damit hat der Wert weder eine Messdatei noch eine Prosaquelle ausserhalb von thumbnail-motive.md selbst. Ich belasse die Einordnung dennoch bei B statt A, weil zwei Berichte (thumbnail-motive.md:5-6, video-formel.md:188) den Lauf 2 als Datenquelle des Datensatzes fuehren — es gibt also einen Hinweis, dass gemessen wurde, nur keine Ablage. Einzelwert ohne Grenzwirkung.

### `6 von 11 (eingebrannte Untertitel) · 6 von 11 (Kanal-Wasserzeichen)` — niedrig

**Wo:** `produktion/pipeline/README.md:131 und :134`  
**Wofür:** Haeufigkeit belegter, aber bewusst nicht umgesetzter Gestaltungsmittel  

Die Abwesenheit ist bestaetigt: kein eingechecktes *.json/*.csv/*.txt/*.log traegt diese Zahlen, sie stehen nur als Prosa in teardown/produktions-spec.md:214/216 und im Folgetext produktion/video-01/upload-checkliste.md:71. Gleiche Einordnungskorrektur wie beim 11/11-Befund: dieselbe dokumentierte 11er-Stichprobe, deren Werkzeugausgabe nicht eingecheckt wurde, mit namentlich benannten Einzelbeobachtungen (Wasserzeichen 'HLL', 'SLEEP BIBLE', 'SLEEPCODEX', 'Night Psalms') - das ist B, nicht A. Als Vorgabe nicht weitergegeben: in der Checkliste steht die Zahl nur als Begruendung fuer eine bewusste Auslassung, nicht als bindende Grenze.

### `1,8-fache Echtzeit (zoompan)` — niedrig

**Wo:** `produktion/pipeline/schritt5_video.py:13-14`  
**Wofür:** Encoder-Geschwindigkeit; traegt das Argument, dass der schleifenfaehige Atemzyklus rund zwei Stunden Encoder-Zeit spart  

Erneut gesucht (zoompan|echtzeit|1,8|1\.8|speed=|fps=) ueber alle eingecheckten Datendateien und alle sechs eingecheckten Logdateien (stimmtest/gen_par.log, gen_v2.log, generate.log, qa.log, teardown/run.log, refill.log, produktion/pipeline/qa/rhotik_lang.log): kein Treffer. Die Loop-QA-Dateien fuehren keine Renderzeit; schritt5_video.py:189 schreibt renderzeit_s ausschliesslich nach produktion/arbeit/<video>/qa_video.json, und produktion/motive/loops/render.log steht in .gitignore. git log -S bestaetigt: der Wert erscheint nur in e59ff94. Der Wert ist ausdruecklich als 'gemessen' etikettiert und die Folgezahl 'rund zwei Stunden' ist damit konsistent (12.600 s / 1,8 = 7.000 s = 1,94 h), aber ohne pruefbares Artefakt.

### `293 s stumm am Ende` — niedrig

**Wo:** `produktion/pipeline/schritt5_video.py:64`  
**Wofür:** Ueberhang der Bildspur bei -shortest statt -t; Begruendung fuer die Wahl von -t  

Erneut ueber alle eingecheckten Datendateien gesucht: einziger Treffer ist start_vs_standbild_mad = 5.293 in produktion/motive/loops/ki-v02/qa-ki-clips.json, sachlich unbeteiligt. git log -S findet den Wert nur in e59ff94. Die Ausgabe eines Renderlaufs (qa_video.json unter produktion/arbeit/) ist systematisch nicht eingecheckt - nachvollziehbare Beobachtung, nicht pruefbar. Einstufung B bestaetigt.

### `Video 12.896,79 s / Audio 12.896,70 s → "Differenz < 1 Frame ✓"` — niedrig

**Wo:** `produktion/video-01/upload-checkliste.md:51`  
**Wofür:** Streamlaengen von video-01.mp4 und die daraus gezogene Bewertung  
**Messdatei:** keine — beide Streamlaengen stammen aus produktion/arbeit/qa_video.json (gitignored)  

Bestaetigt. Kein Treffer fuer 12896/12.896 ausserhalb der Prosa; qa_video.json liegt in produktion/arbeit/. Die Rechenkritik haelt der Nachpruefung stand: 12.896,79 - 12.896,70 = 0,09 s, ein Frame bei 24 fps (config.md:93) sind 0,0417 s — die Differenz ist 2,2 Frames, der Haken ist nicht gedeckt. Zwei Entlastungen, die ich geprueft habe: die Laufzeitangabe 3:34:57 passt zu 12.896,79 s, weil gemeinsam.py:178-180 hms() rundet (int(round(12896.79)) = 12897); und meine SRT-Nachrechnung (letztes Kachelende 12.890,15 s + nachlauf_s 6,0 = 12.896,15 s) liegt 0,6 s daneben, also plausibel. Die Zahlen sind wahrscheinlich echt, nur die Bewertung darueber ist arithmetisch falsch.

### `666.7 MB / 2415.3 MB / 1926.4 MB / 1825.1 MB` — niedrig

**Wo:** `produktion/video-01/upload.md:186`  
**Wofür:** Dateigroesse der vier gerenderten MP4s  
**Messdatei:** keine Messdatei; naeherungsweise nachrechenbar aus produktion/motive/loops/ki*/kette-3min.mp4 + produktion/motive/README.md:262-266  

Bestaetigt als B (qa_video.json['groesse_mb'] aus produktion/arbeit/, Systembefund; die MP4s sind ebenfalls gitignored). Zwei Praezisierungen gegen den Fund: (1) 666,7 MB faellt nicht aus der Reihe, sondern ist der ALTE Zoom-Render von V01 — produktion/motive/README.md:265 nennt genau "vorher 0,67 GB mit Standbild-Zoom"; upload.md V01 wurde nach dem KI-Clip-Neuaufbau (e27e58d) nie neu erzeugt. (2) Die drei anderen Werte sind aus eingecheckten Artefakten auf 1-2 % nachrechenbar: kette-3min.mp4 der jeweiligen ki-Ordner (30,61 / 24,70 / 22,17 MB je 192,7 s) plus 192k-Ton ueber die jeweilige Laufzeit ergibt 2386 / 1900 / 1792 MB gegen gemeldete 2415,3 / 1926,4 / 1825,1 MB. Schwere deshalb niedrig.

### `158.256 / 162.244 / 158.182 / 166.005` — niedrig

**Wo:** `produktion/video-01/upload.md:197`  
**Wofür:** TTS-Zeichen je Renderlauf  
**Messdatei:** produktion/korpus/plan.json ist hier kein Gegenbeleg: zeichen_tts dort = woerter x 5,21 (Schaetzung, nur Bibeltext)  

Bestaetigt als B (skript.json['bericht']['zeichen_tts'] aus produktion/arbeit/, schritt1_text.py:186/202 zaehlt die realen Segmenttexte). Die Gegenrechnung des Fundes faellt aber weg: produktion/korpus/plan.json fuehrt zeichen_tts NICHT als Messung, sondern als Schaetzung — der Quotient zeichen_tts/woerter ist fuer alle acht Videos exakt 5,21 (154581/29670 = 5,2100 usw.), also woerter x 5,21. Ausserdem deckt plan.json nur den Bibeltext ohne Rahmen, Hook, CTA und Gebet ab; der Aufschlag von 1,2-2,9 % ist damit erwartbar und keine Inkonsistenz. Als Vorgabe wirkt die Zahl nirgends: workflow-gates.md:19 nennt "~160.000 TTS-Zeichen" als Kostenhinweis, nicht als Grenze — deshalb als_vorgabe auf false korrigiert.

### `96.3 % / 93.9 % / 93.3 % / 94.7 %` — niedrig

**Wo:** `produktion/video-04/upload.md:84`  
**Wofür:** "Standbild dunkel" — Flaechenanteil mit Luminanz < 60 im Platzhalter-Standbild  
**Messdatei:** produktion/video-0*/PLATZHALTER_standbild.png — eigene Nachrechnung ergibt exakt 96.3/93.9/93.3/94.7 %  

Formal bestaetigt (keine Messdatei, qa_bild.json in produktion/arbeit/), praktisch der harmloseste Posten der Liste: ich habe die Rechenvorschrift aus schritt4_bild.py:91-102 unabhaengig auf den vier eingecheckten PLATZHALTER_standbild.png nachgefahren und erhalte exakt 96,3 / 93,9 / 93,3 / 94,7 % sowie die mittleren Helligkeiten 30,3 / 30,2 / 27,4 / 29,2. Vollstaendig aus eingecheckten Artefakten reproduzierbar; nur traegt ein PNG selbst keine Zahl.

### `3:34:57 (3.58 h) / 3:37:32 (3.62 h) / 3:28:02 (3.47 h) / 3:34:48 (3.58 h)` — niedrig

**Wo:** `produktion/video-01/upload.md:185`  
**Wofür:** Laufzeit der vier Renderlaeufe  
**Messdatei:** produktion/video-0*/*.srt — Nachrechnung trifft alle vier Laufzeiten auf 1 s  

Formal bestaetigt (qa_video.json in produktion/arbeit/), inhaltlich gedeckt. Eigene Nachrechnung aus den eingecheckten SRTs (letztes Kachelende + nachlauf_s 6,0): 12.896,15 / 13.050,88 / 12.482,45 / 12.887,69 s = 3:34:56 / 3:37:31 / 3:28:02 / 3:34:48. Die Abweichung von 1 s bei V01/V02 erklaert sich vollstaendig aus gemeinsam.py:178-180 (hms rundet) und daraus, dass die Tonspur wenige Zehntel nach der letzten Kachel endet. Zusaetzlich stuetzt die Commit-Nachricht e27e58d ("3:34:57") den V01-Wert. Schwere niedrig.

### `140.4 / 141.8 / 146.3 / 146.6 WPM` — niedrig

**Wo:** `produktion/video-01/upload.md:189`  
**Wofür:** Sprechtempo der vier Renderlaeufe; in der Checkliste zusaetzlich "über 30.155 Wörter"  
**Messdatei:** produktion/video-0*/*.srt — 30.155 Woerter fuer V01 exakt, alle vier WPM auf 0,1 reproduziert  

Formal bestaetigt (qa_stimme.json['wpm'] in produktion/arbeit/), inhaltlich gedeckt. Eigene Zaehlung ueber die eingecheckten SRTs: V01 30.155 Woerter (trifft die Checklistenangabe exakt), V02 30.821, V03 30.422, V04 31.466; daraus 140,30 / 141,70 / 146,23 / 146,49 WPM gegen gemeldete 140,4 / 141,8 / 146,3 / 146,6 — durchgehend +0,1, also derselbe systematische Rundungs-/Bezugsdauerunterschied. Kein Verdachtsmoment.

### `3300 / 3128 / 2640 / 2705` — niedrig

**Wo:** `produktion/video-01/upload.md:194`  
**Wofür:** Anzahl Untertitelkacheln je Video  
**Messdatei:** produktion/video-0*/*.srt — Kachelzahlen exakt nachgezaehlt  

Formal bestaetigt (qa_srt.json in produktion/arbeit/), inhaltlich vollstaendig gedeckt: eigene Zaehlung in den eingecheckten SRTs ergibt exakt 3300 / 3128 / 2640 / 2705. Zusaetzlich sind produktion/video-01/untertitel.srt und video-01.srt md5-identisch (899b0507...), die Checklistenangabe "3.300 Kacheln" bezieht sich also auf dieselbe Datei. Schwere niedrig.

### `46,5 gegenüber 54,3` — niedrig

**Wo:** `produktion/motive/README.md:187`  
**Wofür:** Mittlere Luminanz der mittigen Untertitelzone, Video-02-Motiv gegen V3  
**Messdatei:** Keine Messdatei, aber exakt aus den eingecheckten Bildern produktion/motive/motiv-V3.png und motiv-video-02.png reproduzierbar (unteres Achtel, horizontal 10–90 % der Bildbreite, Rec.709-Luma).  

EINORDNUNG KORRIGIERT: A -> B. Der Vorpruefer hat sechs Zonenvarianten getestet und die Zahlen nicht getroffen; ich habe die Zonendefinition systematisch durchsucht (drei Luma-Definitionen x neun Bandhoehen x sechs Horizontalausschnitte) und die Kombination gefunden, die das Paar EXAKT trifft: unteres Achtel (135 px), horizontal von 10 % bis 90 % der Breite, Rec.709 -> V3 = 54,3 und motiv-video-02 = 46,5. Die YouTube-Safe-Breite 1546 px mittig liefert praktisch dasselbe (54,2 / 46,6). Der Ausschnitt ist sachlich zwingend, weil der Bericht das helle rechte Drittel (Feuer) im Satz davor gesondert behandelt. Die Messung hat also stattgefunden und ist am eingecheckten Artefakt nachpruefbar — nur ihre Ausgabe liegt nicht im Repo (motiv-video-02_messung.json kennt nur unteres_achtel_p95 = 152.3 fuer den ganzen Streifen). Damit ist es kein Erfindungsfall, sondern der uebliche B-Fall, und die Schwere sinkt auf niedrig. Nebenbei ebenfalls verifiziert: die gesamte Zonentabelle Zeile 175-181 (V3 50,3 / 3,44 % / 48,2 / 104,1 / 104,9 und V02 23,7 / 1,32 % / 30,2 / 110,9 / 213,2) reproduziert sich exakt mit zonen_pruefen() aus motiv_zuschnitt.py.

### `180 Credits je Clip` — niedrig

**Wo:** `produktion/motive/README.md:243-244`  
**Wofür:** Preis, den FLUX 3 je Clip gekostet haette — Begruendung der Modellwahl Seedance 1.5 Pro  

Bestaetigt. Die komplette Preisliste (FLUX 3 180, Cinema Studio 3.0 150, Seedance 2.0 135, MiniMax H3 60, Seedance 1.5 Pro 36) steht nur in der Commit-Nachricht e27e58d; kein eingechecktes Artefakt traegt sie. Externe Plattformpreise sind ohnehin nicht repo-pruefbar. Die dort genannten 36 fuer Seedance stehen im Widerspruch zur tatsaechlichen Abrechnung von 18 (126407a) — d.h. schon die Vergleichsbasis der Modellwahl ist unsicher. Fuer eine Entscheidung, die bereits gefallen und deren Ergebnis eingecheckt ist, bleibt die Tragweite gering.

### `≈ 2,0` — niedrig

**Wo:** `produktion/motive/README.md:257 und 306`  
**Wofür:** Verhaeltnis Nahtsprung zu normalem Frameschritt bei V01 — Vergleichswert, gegen den die V02-Verbesserung auf 1,75 behauptet wird  

Bestaetigt, aber harmlos. Fuer V01 existiert kein Schluessel uebergang_zu_frameschritt; der Wert ist der Quotient der beiden ebenfalls unbelegten Groessen (2,83/1,40 = 2,02 bis 3,14/1,53 = 2,05), und e27e58d schreibt selbst nur "(~2x)", also erkennbar gerundet. Die V02-Seite des Vergleichs ist sauber gedeckt: ki-v02/qa-ki-clips.json -> uebergang_zu_frameschritt = 1.75.

### `~200 kbit/s` — niedrig

**Wo:** `produktion/motive/README.md:228`  
**Wofür:** Bitrate der bisherigen reinen Zoom-Bildspur, Vergleichsmassstab fuer die Animations-Loops  

Bestaetigt. Fuer die reine Zoom-Bildspur gibt es kein eingechecktes Artefakt — der betreffende Render liegt in produktion/arbeit/, die qa-V?.json messen nur die Loops. Der gemeldete Widerspruch stimmt: produktion/pipeline/README.md:51 sagt zur selben Zoom-Bildspur "rund 20 kbit/s", ein Faktor 10. Ich habe versucht, ihn ueber die Groessenangaben aufzuloesen: aus README-Zeile 266 (0,67 GB gesamt, davon 0,31 GB Ton) folgen ueber 3,58 h rund 220 kbit/s Bildspur, was fuer die 200 und gegen die 20 spricht — beide Ausgangszahlen sind aber selbst unbelegt, deshalb bleibt es bei B.

### `16,6 GB / 15 GB` — niedrig

**Wo:** `produktion/motive/README.md:262-263`  
**Wofür:** Hochgerechnete Groesse der per Bitstrom-Kopie geloopten KI-Clips ueber 3,58 h bzw. die Groesse, bei der der Lauf abgebrochen wurde  

Bestaetigt. Renderlauf, Ausgabe in produktion/arbeit/, nichts eingecheckt — der bekannte Systembefund. Die Zahl ist exakt aus der beanstandeten 10,3 Mbit/s gerechnet (12888 s x 10,3 Mbit/s / 8 = 16,59 GB). Mit der von mir aus den Containern gemessenen echten Rate von 11,215 Mbit/s waeren es 18,07 GB. Die 15 GB (Abbruchpunkt) sind eine Laufbeobachtung ohne jede Spur im Repo. Die daraus gezogene Konsequenz (einmal neu kodieren) ist unabhaengig davon richtig.

### `≈ 2,4 GB (2,1 GB Bildspur + 0,31 GB Ton), vorher 0,67 GB, CRF 26 ≈ 3,3 GB` — niedrig

**Wo:** `produktion/motive/README.md:265-267`  
**Wofür:** Prognostizierte Gesamtgroesse von Video 01 mit KI-Clips gegenueber Standbild-Zoom  

Bestaetigt. Keine eingecheckte Messdatei; das Ergebnis des tatsaechlichen Laufs steht nur in Prosa: produktion/video-01/upload-checkliste.md:39 nennt fuer die gerenderte video-01.mp4 2,52 GB, die Prognose 2,4 GB liegt 5 % darunter. Die 0,67 GB des Vorzustands und die 3,3 GB fuer CRF 26 sind Schaetzungen ohne Lauf und ohne Artefakt. Da alle drei Zahlen ausdruecklich als Prognose formuliert sind und keine Grenze setzen, bleibt die Tragweite gering.

### `1,31 Mbit/s / 1,27 Mbit/s` — niedrig

**Wo:** `produktion/motive/README.md:264 und 307`  
**Wofür:** Bitrate der einmal neu kodierten 48-s-Kette (CRF 28) fuer Video 01 bzw. Video 02  
**Messdatei:** Keine Messdatei, aber exakt aus den eingecheckten Artefakten loops/ki/kette-3min.mp4 und loops/ki-v02/kette-3min.mp4 nachpruefbar.  

Bestaetigt als B, inhaltlich aber einwandfrei. Ich habe die Sampletabellen beider Ketten geparst: ki/kette-3min.mp4 4628 Frames, 31.471.176 B Videospur ueber 192,833 s = 1,306 Mbit/s (dateibasiert 1,308); ki-v02/kette-3min.mp4 4624 Frames, 30.554.959 B ueber 192,667 s = 1,269 Mbit/s (dateibasiert 1,271). Beide README-Angaben stimmen auf die angegebene Genauigkeit, ebenso die 192,7 s. Nebenbefund bestaetigt: der V01-Commit e27e58d nennt fuer dieselbe Kette "CRF 28 -> 1,36 Mbit/s" — das ist die falsche Zahl, nicht die im README.

### `152/138 px seitlich, 176/183 px oben/unten (Safe Area 1546×423)` — niedrig

**Wo:** `produktion/motive/README.md:53 (Tabelle "Bestandene Prüfung"), Commit 2626796`  
**Wofür:** Erste der "fuenf Pruefungen" fuer Kanalbanner-Entwurf 2 (produktion/kanal/banner.jpg): Luft des Schriftzugs in der YouTube-Safe-Area  
**Messdatei:** Keine Messdatei; die Zahlen sind aber aus dem eingecheckten Bild produktion/kanal/banner.jpg reproduzierbar.  

Bestaetigt als B. produktion/kanal/ enthaelt in der gesamten Historie ausschliesslich banner.jpg und banner_safearea.jpg — nie eine Messdatei (git log --all --name-only geprueft). Eigene, unabhaengige Nachmessung: zentrierte Safe Area 1546x423, Schwelle Y>180, Auswertung auf das Textband (Zeilen mit >20 hellen Pixeln, das sind 175-240) beschraenkt, ergibt links 152, rechts 138, oben 175, unten 182. Links/rechts treffen exakt; oben/unten weichen um je 1 px ab (176/183 im Bericht) — das ist die uebliche Inklusiv/Exklusiv-Zaehlung, kein Fehler. Ohne die Bandbeschraenkung faengt die Schwelle die warme Lichtquelle mit ein und liefert voellig andere Raender (80/84) — die Messung ist also methodenabhaengig und ohne eingecheckte Ausgabe nicht selbsterklaerend.

### `14 Glyphencluster` — niedrig

**Wo:** `produktion/motive/README.md:53, Commit 2626796`  
**Wofür:** Zweite der fuenf Bannerpruefungen: buchstabengetreue Wiedergabe von "THE NIGHTLY WORD", kein Fremdtext  
**Messdatei:** Keine Messdatei; aus produktion/kanal/banner.jpg reproduzierbar.  

Bestaetigt als B. Keine Messdatei in produktion/kanal/, in keinem Commit. Eigene Nachmessung im isolierten Textband (Spaltenlaeufe heller Pixel, Y>180, Laeufe unter 4 px verworfen): genau 14 zusammenhaengende Cluster — deckungsgleich mit der Behauptung und mit der Buchstabenzahl von THE NIGHTLY WORD. Die Pruefung hat stattgefunden, ihre Ausgabe ist nur nicht eingecheckt. Aussagekraft ohnehin begrenzt: die Zahl ist trivial gleich der Buchstabenzahl.

### `17,5:1` — niedrig

**Wo:** `produktion/motive/README.md:53, Commit 2626796 (dort ergaenzt um "Untergrund Median Y=18,5")`  
**Wofür:** Vierte der fuenf Bannerpruefungen: Kontrast Schrift zu Untergrund von produktion/kanal/banner.jpg  

Bestaetigt als B. Keine Messdatei. Eigene Nachrechnung mit der Projektformel kontrast(l)=1.05/(l+0.05) aus thumbnail.py ueber die Safe Area: 17,82 bis 17,88:1 je nach Untergrunddefinition (alles ausser Text / nur Y<60 / Median aller Pixel); nach WCAG Text-gegen-Untergrund 16,65 bis 16,71:1. 17,5 liegt zwischen diesen Auslegungen, ist also plausibel, aber mit keiner davon exakt reproduzierbar. Der im Commit mitgelieferte Untergrund-Median Y=18,5 bestaetigt sich nicht: ich messe Median Y der Safe Area 22,5 und Median der Nicht-Text-Pixel 22,1. Da die Zahl nur eine bereits getroffene, ohnehin bis Gate 2 offene Bannerentscheidung stuetzt, bleibt die Tragweite gering.

### `82 %` — niedrig

**Wo:** `produktion/motive/README.md:25 und 53`  
**Wofür:** Anteil der warmen Bildmasse von kanal-banner.png im Desktop-Streifen und im Mobil-Safe — der bestandene "Zonen-Test" von Entwurf 1  
**Messdatei:** Keine Messdatei; aus produktion/motive/kanal-banner.png reproduzierbar.  

Bestaetigt als B. Zu keinem Banner und keinem Avatar wurde je eine Messdatei eingecheckt — nur die Overlay-Bilder _zonen.png / _mobilansicht.png / _kreistest.png (git log --all --name-only ueber produktion/motive/ geprueft). Eigene Nachmessung an kanal-banner.png (warm = R>B+20 und Y>60, Desktop-Streifen 2560x423 mittig, Mobil-Safe 1546x423 mittig): 81,3 % im Desktop-Streifen und 81,3 % im Mobil-Safe. Die Messung hat also stattgefunden, der Bericht rundet auf 82 % auf.

### `34 % Bildhöhe / 70 px / Versatz −222 px` — niedrig

**Wo:** `produktion/motive/README.md:25`  
**Wofür:** Restkompromiss von Entwurf 1: Figurengroesse, Ueberstand des Kopf-bis-Feuer-Blocks ueber den 423-px-Streifen und der vertikale Versatz der Umkomposition  

Bestaetigt als B. Keine Messdatei zum Banner, in keinem Commit. Eigene Nachmessung an kanal-banner.png: die warme Masse reicht von Zeile 489 bis 975, also 487 px = 33,8 % der Bildhoehe (Behauptung 34 % — trifft), Ueberstand ueber den 423-px-Streifen 487-423 = 64 px (Behauptung 70 px — 9 % daneben, methodenabhaengig, je nach Schwellenwahl fuer "Block"). Der Versatz -222 px ist am Ergebnisbild grundsaetzlich nicht mehr nachpruefbar, weil die Zwischenstufe nicht eingecheckt ist; kanal-banner-quelle.png liegt zwar bei, deckt die Zahl aber nicht.

### `99 % / 100 %` — niedrig

**Wo:** `produktion/motive/README.md:27`  
**Wofür:** Anteil von Figur+Feuer des verworfenen Bannerentwurfs unterhalb des Desktop-Streifens bzw. ausserhalb des Mobil-Safe  
**Messdatei:** Keine Messdatei; aus produktion/motive/kanal-banner-entwurf.png reproduzierbar.  

Bestaetigt als B. Keine Messdatei zum Entwurf. Eigene Nachmessung (Entwurf von 1376x768 auf 2560x1440 gebracht, warm = R>B+20 und Y>60): 0,2 % der warmen Masse liegen im Desktop-Streifen, also 99,8 % darunter, und 0,0 % im Mobil-Safe, also 100 % ausserhalb. Die Angaben stimmen. Einschraenkung wie gemeldet: die geprueft Upload-Fassung 2560x1440 liegt nicht im Repo, nur die 1376x768-Vorlage — die Skalierung ist meine Annahme.

### `20 % / 23,5 %` — niedrig

**Wo:** `produktion/motive/README.md:23 und 24`  
**Wofür:** Anteil der hellen Masse ausserhalb des Kreisbeschnitts bei den Avatar-Varianten B und B2  
**Messdatei:** Keine Messdatei; aus den eingecheckten Avatar-PNGs reproduzierbar.  

Bestaetigt als B. Zu den Avataren existiert keine Messdatei, in keinem Commit — nur die PNGs und die _kreistest.png-Overlays. Eigene Nachmessung (Kreis mit Radius W/2 mittig, hell = Y>40, 1024x1024): Variante A 97,7 % im Kreis, Variante B 20,4 % ausserhalb, Variante B2 23,6 % ausserhalb. Alle drei Berichtszahlen (97,7 / 20 / 23,5) sind damit gedeckt — die Kreistests haben stattgefunden, nur ihre Ausgabe fehlt. Die Entscheidung zwischen den Varianten ist ohnehin offen.

### `3,1 MB / 3,06 MB / 1,43 MB` — niedrig

**Wo:** `produktion/motive/README.md:25 und 49`  
**Wofür:** Dateigroessen der beiden Bannerentwuerfe gegen das YouTube-Limit von 6 MB  
**Messdatei:** Keine Messdatei, aber die Artefakte selbst tragen den Wert: kanal-banner.png 3.057.863 B, banner.jpg 1.427.720 B.  

Bestaetigt als B, praktisch aber unbedenklich. Keine Messdatei, doch der Wert ist ohne jede Methodenannahme direkt am eingecheckten Artefakt ablesbar und stimmt: kanal-banner.png = 3.057.863 B = 3,06 MB (im Text auf 3,1 MB gerundet), banner.jpg = 1.427.720 B = 1,43 MB; beide Bilder 2560x1440, die drei Avatare 1024x1024 — alles von mir nachgeprueft. Das Limit von 6 MB ist mit grossem Abstand eingehalten.

---

## C — Widerspruch

Die Messdatei existiert und sagt etwas anderes als der Bericht.

### `0,0–3,4 s` — hoch · **als Vorgabe weitergegeben**

**Wo:** `formel/video-formel.md:101`  
**Wofür:** Behauptete Spannweite des Sprechbeginns über die 24 Lauf-1-Stichproben; trägt die PFLICHT-Regel „Sprache beginnt in Sekunde 0–3"  

Nachgerechnet mit csv.DictReader (nicht awk — vier Titel enthalten Kommas und verschieben die Spalten): teardown/teardown_batch_20260802_090410/matrix_voll.csv hat exakt 24 Datenzeilen, sprache_start_s = 0,0 0,0 0,1 0,1 0,1 0,1 0,2 0,2 0,2 0,3 0,6 0,6 1,4 1,5 1,8 2,0 2,4 2,4 3,1 3,4 3,4 3,5 6,8 7,8. Bereich also 0,0–7,8 s; RGkbn94Ks-4 (3,5), FJbu291cR8w (6,8) und eqSO5hlFo7M (7,8) liegen über 3,4 s. teardown/auswertung_matrix.txt (Spalte start_s) zeigt dieselben Werte. Historie geprüft: matrix_voll.csv hat genau einen Commit (ac4f5bd), dort schon max 7,8 — es gab nie eine Fassung mit 3,4 als Maximum. Keine andere eingecheckte Datei trägt eine Sprechbeginn-Spalte. Der Zusatz „Gewinner 0,1–3,1 s" ist dagegen durch regeln/daten/skript_anatomie.json (sprechbeginn_s 3,1 / 2,4 / 2,1 / 0,1) gedeckt. Verschärfend: die drei Ausreißer sind genau die Fälle, die die PFLICHT-Regel widerlegen würden.

### `Sekunde 0-3 (n=24)` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/config.md:83`  
**Wofür:** Behaupteter Wertebereich des Sprechbeginns ueber 24 Konkurrenzvideos aus Lauf 1; begruendet vorlauf_s = 1.5 und die harte Schwelle sprachstart_max_s = 3.0.  

Eigenstaendig per csv.DictReader nachgezaehlt: teardown/teardown_batch_20260802_090410/matrix_voll.csv hat exakt 24 Zeilen, Spalte sprache_start_s laeuft von 0.0 bis 7.8; ueber 3,0 s liegen 3.1, 3.4, 3.4, 3.5, 6.8, 7.8 (6 von 24). Die zweite eingecheckte Messdatei teardown/auswertung_matrix.txt (Spalte start_s) zeigt dieselben Werte. Der Zusatz "(n=24)" ist damit durch zwei eingecheckte Messdateien widerlegt - auch die in Formel §3 genannte Spanne "0,0-3,4 s" trifft nicht zu. ENTLASTEND und vom Erstpruefer richtig erkannt: der Bereich selbst ist durch eine ANDERE eingecheckte Messdatei gedeckt - regeln/daten/skript_anatomie.json enthaelt 11 Videos mit sprechbeginn_s 0.0/0.0/0.0/0.1/0.2/0.2/0.3/0.4/2.1/2.4/3.1, also 0,0-3,1 s. Die abgeleitete Vorgabe sprachstart_max_s = 3.0 ist folglich nicht grundlos, nur die zitierte Population ist es. Deshalb Schwere auf mittel gesenkt: falsche Quellenangabe, nicht falscher Wert.

### `null Mal / 0 von 90` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/videos-01-08.md:72-73`  
**Wofür:** Behauptung, eine anonyme (nicht als Jesus erkennbare) Figur komme in den 90 Feld-Thumbnails nie als Hauptmotiv vor - begruendet die Ersetzung des frueheren Grundmotivs "schlafende Gestalt"  

Ernsthaft gesucht, nicht widerlegbar - im Gegenteil, die Pruefung schaerft den Fund. regeln/daten/motiv_inventar.json fuehrt motiv "fig" (andere Figur ohne Jesus) = 2/90, dazu hist=2 und ort=1 ganz ohne Figur. Entscheidend: ich habe das eingecheckte Thumbnail regeln/daten/thumbs/E_QuietMind__WORST__8TP64R9sdME.jpg angesehen (38 Views, im Inventar als "fig" codiert, in formel/thumbnail-motive.md:32 als "Schlaefer an Kirche" beschrieben). Es zeigt einen bartigen Mann in schlichtem Gewand, SCHLAFEND auf einer Decke, mit Lamm, Nacht, warmes Fensterlicht - also exakt eine anonyme schlafende Gestalt als Hauptmotiv. Damit ist selbst die engere Quellformulierung in thumbnail-motive.md:200-201 ("anonyme schlafende Gestalt ... 0/90 als Hauptmotiv") durch das eigene Inventar widerlegt; videos-01-08.md laesst zusaetzlich das Wort "schlafende" weg und verschaerft die Aussage auf jede anonyme Figur. Das zweite fig-Thumbnail (epWLGVZXkPg, 52 Views) zeigt zwei betende Frauen, ebenfalls ohne Jesus als Hauptfigur.

### `Median 15,4:1` — hoch

**Wo:** `formel/thumbnail-checkliste.md:38`  
**Wofür:** Median-Kontrast Text/Hintergrund der 13 Rest-in-Grace-Thumbnails, Grundlage des Zielwerts "Kontrast >= 10:1"  
**Messdatei:** keine — thumb_textmessung.json belegt Median 15,8 (Widerspruch)  

Gegenpruefung erfolglos: regeln/daten/thumb_textmessung.json enthaelt fuer B_RestInGrace 13 Datensaetze, alle mit Feld kontrast: 10,7/10,8/10,8/12,2/12,4/15,2/15,8/15,8/16,0/16,8/17,0/17,3/18,1. Median = 15,8. Ich habe zusaetzlich geprueft, ob 15,4 als anderer Kennwert entstehen koennte: Mittelwert 14,53; alle 13 Leave-one-out-Mediane ergeben nur 15,5 oder 15,8; alle Leave-one-out-Mittelwerte liegen zwischen 14,23 und 14,85; kein Perzentil zwischen P50 und P60 trifft 15,4; kein Mittelwert zweier vorkommender Kontrastwerte ergibt 15,4 (Sprung 15,25 -> 15,5). GEW-Gesamtmenge (n=21, 17 mit Text) hat Median 12,4. Keine zweite Datei im Repo fuehrt ueberhaupt ein Kontrastfeld fuer Feld-Thumbnails (rg ueber alle *.json/*.csv/*.txt/*.log: nur thumb_textmessung.json und die fuenf eigenen produktion/video-0*/thumbnail*_messung.json). Historie: thumb_textmessung.json hat genau einen Commit (8141d47), nie geaendert; git log -S"15.4" bringt keinen Treffer in regeln/. Der Wert 15,4 existiert nirgends im Repo ausser in der Prosa (Checkliste, bibeltube-wissen.md und der Commit-Text von 8141d47 selbst).

### `10,1 (schlechtester Kontrast der Gewinnerserie)` — hoch

**Wo:** `formel/thumbnail-checkliste.md:38 und :47`  
**Wofür:** Unterer Rand der belegten Kontrastspanne; einzige Begruendung fuer den bindenden Grenzwert >= 10:1  
**Messdatei:** keine — 10.1 steht in thumb_textmessung.json nur als glyph_hoehe_pct eines Verlierer-Thumbnails  

Der schlechteste B-Kontrast in regeln/daten/thumb_textmessung.json ist 10,7, nicht 10,1. Der einzige Treffer fuer 10.1 im gesamten Repo (rg, alle Nicht-md-Dateien) ist thumb_textmessung.json:785 — dort als glyph_hoehe_pct von J_JesusLovesYou/kbvrAYlY0wc, dessen Kontrast 8,2 betraegt. Auch der niedrigste Kontrast der gesamten GEW-Gruppe (21 Gewinner, 17 mit Text) ist 7,4 (A/NJSq3WYyrCY), nicht 10,1. Es gibt keine dritte Kontrastquelle im Repo und nur eine Version der Datei. Sachlich harmlos ist die Folge: der gesetzte Gate-Wert 10:1 liegt trotzdem unter dem echten B-Minimum 10,7, die Grenze reisst also nicht — falsch ist nur ihre Begruendung.

### `17,4 : 1` — hoch

**Wo:** `produktion/motive/README.md:87`  
**Wofür:** Kontrast der Thumbnail-Schrift zum direkten Hintergrund (Mittel) der Textvariante motiv-V3_text.png  

Widerlegungsversuch gescheitert. Die aktuelle produktion/motive/text_messung.json sagt kontrast_direkter_hintergrund_mittel = 16.8, ebenso produktion/video-01/thumbnail-a_messung.json (kontrast_direkt_mittel 16.8). Entscheidend: ich habe das eingecheckte motiv-V3.png mit exakt der Methode aus produktion/pipeline/thumbnail.py neu vermessen (gleiche lum()/kontrast()/schrift_fuer()) und erhalte 16.8 — der Messwert der Datei ist reproduzierbar, 17,4 nicht. Herkunft geklaert: die Altfassung der Messdatei in Commit bc1876e traegt genau 17.4; die Nachmessung am dort eingecheckten alten motiv-V3.png liefert ebenfalls exakt 17.4. Commit eab1d17 ("Lichtquellen vergroessert") hat alle vier Motive neu erzeugt und die JSON nachgezogen (Commit-Text nennt ausdruecklich "Kontrast 16,8:1 / p95 14,0:1"), den README-Abschnitt aber unangetastet gelassen — der Diff von eab1d17 beruehrt die Zeilen 87-95 nicht. Der Wert ist also keine Erfindung, sondern eine echte Messung eines inzwischen ersetzten Bildes, die im Bericht als aktueller Messwert stehen geblieben ist.

### `15,5 : 1` — hoch

**Wo:** `produktion/motive/README.md:88`  
**Wofür:** Kontrast p95 (unguenstige Pixel) der Textvariante  

Wie Fund 1. Aktuell eingecheckt: kontrast_direkter_hintergrund_p95 = 14.0 (text_messung.json) bzw. kontrast_direkt_p95 = 14.0 (video-01/thumbnail-a_messung.json). Eigene Nachmessung am aktuellen motiv-V3.png mit der thumbnail.py-Methode: 14.0. Nachmessung am alten motiv-V3.png aus bc1876e: exakt 15.5 — identisch mit der dort eingecheckten Altfassung der JSON. 15,5 ist damit der Messwert des ersetzten Bildes, im Bericht nicht nachgezogen.

### `15,8:1` — hoch

**Wo:** `produktion/motive/README.md:93`  
**Wofür:** Kontrast gegen den Rohhintergrund (Mittel), vor dem dunklen Schein hinter der Schrift  

Aktuell eingecheckt: kontrast_rohhintergrund_mittel = 14.8 (text_messung.json) und kontrast_roh_mittel = 14.8 (thumbnail-a_messung.json); eigene Nachmessung am aktuellen motiv-V3.png: 14.8. Nachmessung am alten motiv-V3.png (bc1876e): exakt 15.8, wie in der dortigen Altfassung der JSON. Stolperfalle geprueft und ausgeschlossen: das AKTUELLE motiv-V1.png liefert zufaellig ebenfalls roh_mittel 15.8 — die Textvariante liegt aber ausdruecklich auf V3 (motiv-V3_text.png), der Treffer deckt den Wert also nicht.

### `13,7:1` — hoch

**Wo:** `produktion/motive/README.md:93`  
**Wofür:** Kontrast gegen den Rohhintergrund, p95  

Der Schluessel kontrast_rohhintergrund_p95 existiert in der aktuellen text_messung.json nicht mehr (in bc1876e vorhanden mit 13.7, in eab1d17 entfernt). Die einzige aktuell eingecheckte Messung derselben Groesse ist produktion/video-01/thumbnail-a_messung.json -> kontrast_roh_p95 = 11.0. Eigene Nachmessung am aktuellen motiv-V3.png bestaetigt 11.0, am alten motiv-V3.png exakt 13.7. Bericht und aktueller Stand widersprechen sich um 2,7 Punkte.

### `144 Credits` — hoch

**Wo:** `produktion/motive/README.md:278 und 286-287`  
**Wofür:** Angeblicher Preis der vier V01-KI-Clips, gegen den die Halbierung auf 72 argumentiert wird; zugleich als Kosten fuer einen erneuten Clip-Satz genannt  

Bestaetigt und verschaerft. Es gibt kein Kosten-/Credit-Artefakt im Repo (git grep -i credit|guthaben|transaktion ueber alle eingecheckten Nicht-md-Dateien: nur ein unbeteiligter Kommentar in satzlaengen.py). Der V01-Commit e27e58d protokolliert den Ist-Verbrauch mit Kontostandsspur: "Verbrauch: 72 Credits (4 Clips, 182,9 -> 110,9)" — die Differenz 72 ist in sich stimmig. NEU GEFUNDEN: der V02-Commit 072ef0c nennt fuer die vier V02-Clips ausdruecklich "144 Credits". Der Bericht hat die beiden Laeufe also vertauscht: er schreibt V01 die 144 zu (Ist: 72) und V02 die 72 (Commit: 144). Die 144 ist erkennbar der Listenpreis 4 x 36; Commit 126407a haelt fest, dass "durchgaengig 18 statt 36" abgerechnet wurde. Damit sind sowohl "die fuer V01 vermerkten 144" als auch das Narrativ "Der Preis hat sich halbiert" (Zeile 285) gegenstandslos. VORGABE-FLAG KORRIGIERT auf false: 144 steht ausschliesslich in produktion/motive/README.md (Zeilen 278, 287) — in config.md, workflow-gates.md, videos-01-08.md, in keiner Checkliste und in keinem Pipelineskript kommt "Credit" ueberhaupt vor.

### `22/90` — mittel

**Wo:** `produktion/videos-01-08.md:75`  
**Wofür:** Anteil der "liegenden" Bauform an den 90 Feld-Thumbnails; traegt die Begruendung, die sitzende Bauform (11/90) sei "deutlich seltener kopiert"  

Eigenstaendig nachgeprueft und nicht widerlegbar. regeln/daten/motiv_inventar.json (n=90, einzige Version im Repo, Commit 650da0a) codiert die liegende Bauform als motiv "js" = 41/90. Ich habe erschoepfend gesucht: js+lamm 31, js+feuer 39, js+lamm+feuer 30, js+lamm+feuer+nacht 28, js+lamm+feuer+nacht+warmlicht 28, js+jr 45, js ohne A/B 28, js+lamm+feuer ohne A/B 17. Brute Force ueber alle Motiv-Teilmengen (bis 3 Motive) x alle Kombinationen aus bis zu 3 Binaerfeldern (lamm/feuer/gesicht/blickkontakt/warmlicht/text) x Gruppen- und Kanalfilter (GEW/BEST/WORST/ohneAB/nacht): 41 Teilmengen ergeben 22, aber KEINE davon enthaelt js mit lamm=1 - alle 22er-Schnitte sind jfront/jstand/jbed-Kombinationen oder verlangen lamm=0, was dem Motiv (schlafende Figur MIT Lamm am Feuer) widerspricht. Historie geprueft: motiv_inventar.json hat nur einen Commit; git log -S"22/90" trifft ausschliesslich .md-Dateien. Herkunft geklaert: formel/thumbnail-motive.md:195 sagt "22 der 90 Feld-Thumbnails tragen es fast identisch" - das ist ein visuelles Aehnlichkeitsurteil ueber das GESAMTE Richtung-1-Motiv aus der Sichtung, ohne maschinenlesbare Entsprechung. videos-01-08.md:75 macht daraus eine Bauform-Haeufigkeit in direkter Parallele zu 11/90 (= jsit, korrekt). Gegen diese Lesart steht die Messdatei mit 41/90.

### `tote Kanäle 4–7 (CTAs)` — mittel

**Wo:** `formel/video-formel.md:137`  
**Wofür:** Behauptete CTA-Spannweite der gescheiterten Kanäle als Kontrast zur Regel „maximal 2 CTA pro Video"  

regeln/daten/skript_anatomie.json, cta_anzahl je Verlierer: C_kEmciGJpkR0=4, F_oHsh-paMGeU=0, D_gX2JvLmM-jA=7, G_jx5Z_eHZa00=0, H_W8HjtY3udqA=3, I_uV9cfBYfz_I=1, J_YAxMl1GB8bQ=0 (E_Dk5o37eqgyY hat nur ein Feld „fehler"). Gemessene Spannweite 0–7; nur 2 von 7 Verlierern liegen im Band 4–7, vier liegen unter dem Gewinner-Maximum 2. Keine zweite eingecheckte Datei zählt CTAs (rg „cta" über alle Nicht-md-Dateien trifft nur drei Zitat-Strings in stimm_stichprobe.json). skript_anatomie.json hat genau einen Commit, also keine abweichende Vorfassung. Die Gewinner-Angabe 0–2 ist korrekt (2/0/0/2). Korrektur an der Meldung: die 4–7 steht in produktion/workflow-gates.md:36 nur in der Beleg-Spalte, die bindende Grenze dort ist „höchstens 2" — daher als_vorgabe_weitergegeben auf false gesetzt.

### `Nur 3 von 10 sind ≤3,5 h` — mittel

**Wo:** `formel/video-formel.md:90-92`  
**Wofür:** Argument, dass das Kostenband 3,0–3,5 h an der Unterkante der Trefferverteilung liegt; begründet das neue Zielband 3,4–3,8 h  

Nachgerechnet über regeln/daten/listings/A_HushLittleLamb_videos.jsonl + B_RestInGrace_videos.jsonl (21 Videos, davon 10 mit view_count > 30.000): 3,4425 / 3,4617 / 3,5594 / 3,5594 / 3,5594 / 3,5764 / 3,6039 / 4,1197 / 4,3797 / 5,0236 h. Nur ZWEI liegen ≤3,5 h. Gegenprobe mit den exakten lengthSeconds/views aus regeln/daten/nexlev/winner_details.json: identisches Bild (2 von 10). Auch nach Rundung auf eine Nachkommastelle bleibt es bei 2 (3,4 und 3,5; die nächsten drei sitzen bei 3,56 h). Bereich 3,4–5,0 h und Median 3,6 h (exakt 3,568) sind dagegen korrekt. Beide Listings haben genau einen Commit, also keine abweichende Vorfassung. Korrektur an der Meldung: das neue Zielband 3,4–3,8 h in produktion/config.md:132-134 stützt sich auf den korrekten Median, nicht auf diese Zahl — als_vorgabe_weitergegeben daher false. Der Fehler geht zudem in die für die eigene These ungünstige Richtung.

### `17,5:1` — mittel

**Wo:** `formel/thumbnail-checkliste.md:38`  
**Wofür:** Oberer Rand der belegten Kontrastspanne der Gewinnerserie  
**Messdatei:** keine fuer die B-Serie — 17,5 gehoert in der Messdatei zu einem G-WORST-Thumbnail  

Hoechster B-Kontrast ist 18,1 (B/vmp9HqIFEgE-Reihe), nicht 17,5. Der Wert 17.5 steht zwar in thumb_textmessung.json:605 — aber als kontrast von G_TheSilentShepherd/RXI1Y2oxW8g, einem WORST-Thumbnail. Ein zweiter Treffer, produktion/video-04/thumbnail_messung.json (kontrast_roh_mittel 17.5), stammt vom eigenen Thumbnail und ist 2026-08-2x entstanden, also nach der Checkliste (2026-08-03) — er kann die Aussage ueber die Fremdserie nicht decken. Damit sind alle drei Zahlen der Zelle "10,1–17,5:1, Median 15,4:1" falsch; die tatsaechliche Zelle muesste "10,7–18,1:1, Median 15,8:1" lauten.

### `245K und 184K ("A's zwei groesste Videos")` — mittel

**Wo:** `formel/thumbnail-checkliste.md:143-145`  
**Wofür:** Belegfall fuer die Aussage, dass Thumbnails ganz ohne Text gewinnen koennen  
**Messdatei:** keine — motiv_inventar.json und thumbnail_forensik.json widersprechen beide  

motiv_inventar.json, A_HushLittleLamb absteigend: 245.000 (text=0), 233.000 (text=1), 201.000 (text=1), 184.000 (text=0), 47.000 (text=0), 36.000 (text=1), 12.000 (text=0), 12.000 (text=1). Die zwei groessten sind 245K und 233K, und 233K traegt Text (thumb_textmessung.json: A/UV1mdTGnFVY, 1 Zeile, 11 Glyphen). Richtig waere "A's zwei groesste textlose Videos" oder "245K und 233K haben keinen bzw. minimalen Text" — genau so steht es in der zweiten eingecheckten Datei regeln/daten/thumbnail_forensik.json, die dem Bericht damit woertlich widerspricht. Die Aussage selbst (Thumbnails ohne Text koennen gewinnen) bleibt durch 245K/184K/47K gedeckt.

### `Text im Bild 6/10 (B 4/4, A 2/6)` — mittel

**Wo:** `formel/thumbnail-motive.md:61`  
**Wofür:** Anteil der 10 Treffer-Thumbnails mit Text, Grundlage der Aussage "Text ist offenkundig kein Muss"  
**Messdatei:** keine — motiv_inventar.json ergibt 7/10 (A 3/6)  

Die 10 Treffer (views > 30.000) aus motiv_inventar.json: A 245K text=0, A 233K text=1, A 201K text=1, A 184K text=0, B 166K text=1, B 96K text=1, A 47K text=0, A 36K text=1, B 35K text=1, B 32K text=1. Summe text=1 ist 7, nicht 6; die Aufteilung ist B 4/4 (stimmt) und A 3/6 (nicht 2/6). Gegenprobe ueber thumb_textmessung.json bestaetigt fuer alle drei A-Treffer mit Text tatsaechlich Glyphen (233K: 11, 201K: 5, 36K: 9). Die daraus gezogene Schlussfolgerung ("Text ist kein Muss") bleibt tragfaehig, weil weiterhin 3 von 10 Treffern textlos sind.

### `0,68 (Blickkontakt, kanal-normierter Median, n=18)` — mittel

**Wo:** `formel/thumbnail-motive.md:94 und :112`  
**Wofür:** Kanal-normierter Median der Thumbnails mit Blickkontakt — zentrale Zahl der Negativ-Empfehlung gegen Frontalportraets  
**Messdatei:** keine — motiv_inventar.json ergibt Median 0,713 (= 0,71)  

Alle vier Zeilen der Tabelle nachgerechnet (Feld ratio in motiv_inventar.json, Median je Gruppe): Feuer mit 1,213 / ohne 0,713 -> "1,21 / 0,71" stimmt; warmes Licht mit 1,067 / ohne 0,407 -> "1,07 / 0,41" stimmt; Text mit 1,000 / ohne 0,676 -> "1,00 / 0,68" stimmt; Blickkontakt mit 0,713 (n=18) / ohne 1,0335 (n=72) -> die 1,03 stimmt, die 0,68 nicht: korrekt waere 0,71. Die Fallzahlen 18 und 72 stimmen. Bemerkenswert: der korrekte Blickkontakt-Wert 0,713 ist identisch mit "Feuer ohne" (0,713), und die faelschlich eingetragene 0,68 ist der Wert aus der Zeile direkt darueber (Text ohne, 0,676) — die Verwechslungsthese des Erstpruefers ist plausibel. Richtung und Aussage der Zeile bleiben unveraendert (deutlich unter 1,0).

### `20 Thumbnails / "alle unter 113 Views"` — mittel

**Wo:** `formel/thumbnail-motive.md:76-78`  
**Wofür:** Kernbeleg der Falsifikation "das Motiv erklaert Kanalerfolg nicht"  
**Messdatei:** keine — motiv_inventar.json ergibt 18 und einen Maximalwert von genau 113  

motiv_inventar.json: C_TheBibleSacred hat 8 Thumbnails mit motiv==js, F_GodsPeacefulSleep 10 — zusammen 18, nicht 20. Die Zahlen 8/10 und 10/10 nennt das Dokument selbst zwei Absaetze vorher (Zeilen 69–72), es widerspricht sich also intern. Enger gefasst (js + Lamm + Feuer) waeren es sogar nur 9 (C 7, F 2). Zusaetzlich: C's bestes js-Thumbnail liegt bei exakt 113 Views, ist also nicht "unter 113" — in Zeile 175 desselben Dokuments steht dafuer korrekt "alle <=113 Views". Der Befund selbst (das Motiv traegt tote Kanaele nicht) bleibt vollstaendig gedeckt.

### `22 der 90 Feld-Thumbnails` — mittel

**Wo:** `formel/thumbnail-motive.md:195-196`  
**Wofür:** Saettigungsrisiko von Richtung 1 (schlafende Figur mit Lamm am Feuer)  
**Messdatei:** keine — aus keiner Feldkombination in motiv_inventar.json reproduzierbar  

Ich habe ueber motiv_inventar.json systematisch alle plausiblen Kombinationen ausgezaehlt: js 41; js+Lamm 31; js+Feuer 39; js+Lamm+Feuer 30; js+Lamm+Feuer+Nacht 28; js+Lamm+Feuer+Warmlicht 30; js+Lamm+Feuer+Text 29; js+Lamm+Nacht 29; (js oder jr)+Lamm+Feuer 34; Lamm+Feuer ueber alle Motive 36; js ohne die Gewinnerkanaele A/B 28; js+Lamm ohne A/B 18; js+Lamm+Feuer ohne A/B 17. Keine Kombination ergibt 22. Auch nach Gruppen zerlegt (js+Lamm+Feuer: GEW 13, BEST 11, WORST 6) und nach Kanaelen (B 10, C 7, G 4, A 3, D 2, F 2, J 2) entsteht die 22 nicht. Der naechste sinnvolle Wert waere 30 (bzw. 17 ohne die eigenen Gewinnerkanaele).

### `11` — mittel

**Wo:** `regeln/erfolgsregeln.md:101`  
**Wofür:** Anzahl Gewinner-Videos mit >30K Views als Beleg der Kern-Regel M6 (Laufzeit)  

Nachgezaehlt in DREI unabhaengigen eingecheckten Messdateien, alle sagen 10: (a) regeln/daten/listings/A_*_videos.jsonl 6 Treffer + B_*_videos.jsonl 4 Treffer; (b) regeln/daten/nexlev/katalog_A/katalog_B (voller Katalog, 8+13 Videos) ebenfalls 6+4; (c) winner_details.json (19 Datensaetze) 9 Treffer, das fehlende 10. Video TRGA1Kk_W3U (32.000) steht in katalog_B. Kein Snapshot, keine Historie enthaelt ein 11. Video >30K — die Listings wurden genau einmal committet (66b4b17) und nie geaendert. Zusaetzlich als 10 bestaetigt in einer Messdatei: regeln/daten/stimm_geschlecht.json ('Trefferquote ohnehin nur bei 10/21'), und in der Commit-Botschaft desselben Commits 909c465, der diese Zeile anfasste ('Trefferquote als Planungsgroesse: 10 von 21 Gewinner-Videos ueber 30.000 Views'). Der Fehler ist ein nicht nachgezogener Rest: 909c465 hob Ueberschrift und Ankreuzzeile von 2,5 auf 3,0 h an, liess die Beleg-Zeile aber unveraendert. Die Sachaussage selbst haelt (alle 10 Treffer sind ≥3,44 h). Korrektur zur Meldung: als_vorgabe_weitergegeben ist FALSCH — beide bindenden Stellen tragen die 10 (produktion/workflow-gates.md:27 'alle 10 Treffer ≥ 3,2 h', formel/video-formel.md:85). Die 11 ist nur in einen weiteren Bericht gewandert (bibeltube-wissen.md:117), der an neun anderen Stellen selbst 10 sagt.

### `11 Hit-Videos` — mittel

**Wo:** `regeln/erfolgsregeln.md:170`  
**Wofür:** Fallzahl der EGAL-Zeile 'Genaue Hit-Laenge oberhalb der Schwelle'  

Gleiche Auszaehlung wie oben: 10, nicht 11 (Listings, katalog_A/katalog_B, winner_details + stimm_geschlecht.json 10/21). Zusatzbefund, den die Meldung uebersehen hat: auch die angegebene Spanne '3,2–5,0 h' ist nicht gedeckt. Die 10 Treffer laufen 3,44–5,02 h (Minimum 8m6NqWG9p2o 12.393 s = 3,44 h). Die in der Meldung genannten 3,27 h gehoeren zu VtihhRDeLO8 mit 559 Views — kein Treffer; TRGA1Kk_W3U hat 12.974 s = 3,60 h. Die eigene Nachschaerfung im Repo sagt es richtig: formel/video-formel.md:90 'Die Treffer liegen bei 3,4–5,0 h, Median 3,6 h'. Die Zeile traegt also zwei veraltete Zahlen.

### `1800 Zeichen` — mittel

**Wo:** `produktion/pipeline/README.md:118`  
**Wofür:** Chunk-Obergrenze fuer die TTS-Aufteilung in Schritt 2  

Nachgeprueft und bestaetigt: produktion/korpus/satzlaengen.json:2 hat "grenze": 1900, produktion/config.md:61 hat chunk_max_zeichen = 1900 (mit Begruendung: Psalm 136 = 1827 Zeichen). Historie je Commit ausgelesen: e59ff94, e27e58d, 072ef0c = 1800; ab 3675e73 ("Chunk-Limit auf 1900, alle acht Korpora vorher gemessen") bis heute 1900. Der Wert 1800 ist also seit 3675e73 nur noch im README stehengeblieben und widerspricht der eingecheckten Messdatei. Keine alternative Schreibweise und keine andere Messdatei traegt heute 1800.

### `1 min 52 s (Gebetsdauer)` — mittel

**Wo:** `produktion/pipeline/README.md:72`  
**Wofür:** Dauer des Eingangsgebets; traegt das Argument fuer die Platzierung des Gebets hinter den CTAs  

Eigene Auswertung von produktion/video-01/video-01.srt (maschinell geschriebene, eingecheckte Artefaktdatei mit gemessenen Zeiten; identisch mit untertitel.srt, unveraendert seit e59ff94): Gebet laeuft von Cue 9 (38,920 s, 'Father, I come to you...') bis Cue 27 (109,080 s, 'Amen.') = 70,16 s. 112 s kommt in keiner Datei und keiner Version vor. Auch die Gegenrechnung stuetzt 70 s: das Gebet hat 182 Woerter, bei den gemessenen 140,4 WPM sind das 77,8 s, bei wpm_erwartet = 145,9 (config.md) 74,8 s; 112 s entspraechen 97,5 WPM und damit einem Tempo, das die Datei selbst nirgends kennt. Zusaetzlich widerspricht der Wert der Zeitleiste im selben Absatz (38 s -> 116 s = 78 s). Keine alternative Schreibweise (1:52, 112 s) gefunden.

### `tote Kanaele 4-7 (CTA-Anzahl)` — mittel

**Wo:** `produktion/pipeline/schritt1_text.py:13`  
**Wofür:** Angeblich belegte Spanne der CTA-Anzahl bei den erfolglosen Kanaelen; Begruendung fuer die CTA-Obergrenze  

Gegen die Messdatei regeln/daten/skript_anatomie.json ausgezaehlt: cta_anzahl der Verlierer/toten Kanaele C = 4, D = 7, F = 0, G = 0, H = 3, I = 1, J = 0 (E ohne Wert). Die belegte Spanne ist damit 0-7; nur zwei der sieben Kanaele liegen im behaupteten Band 4-7, und auch die Teilmenge 'Kanaele mit CTA' ergaebe 1-7, nicht 4-7. Die Gewinner-Angabe 0-2 ist dagegen korrekt (2 / 0 / 0 / 2). Der Docstring zitiert formel/video-formel.md:137 wortgetreu, der Widerspruch steckt also schon in der Formel. Nicht als Vorgabe weitergegeben: die bindende Grenze ist cta_max = 2 in produktion/config.md:143 und stuetzt sich auf die korrekte Gewinner-Spanne.

### `90` — mittel

**Wo:** `produktion/motive/README.md:93-94`  
**Wofür:** Anzahl einzelner Sternpixel unter den Glyphen, die nackt durchfallen wuerden  

Der Schluessel sternpixel_unter_glyphen: 90 existierte ausschliesslich in der Altfassung von text_messung.json (bc1876e) und wurde in eab1d17 ersatzlos entfernt; thumbnail.py schreibt kein solches Feld. Es gibt heute keine eingecheckte Messdatei, die diese Zahl traegt. Die analoge Groesse ist am aktuellen Bild grundverschieden: eigene Zaehlung der Rohpixel unter der Glyphenmaske mit Kontrast < 10:1 ergibt am aktuellen motiv-V3.png 2521 Pixel (am alten 334). Welche Schwelle bc1876e genau benutzt hat, ist nicht mehr rekonstruierbar — dass die 90 fuer das heute eingecheckte Bild gilt, ist damit ausgeschlossen. Kein A: die Messung hat nachweislich stattgefunden, ihre Datei ist nur ueberschrieben.

### `2,0:1` — mittel

**Wo:** `produktion/motive/README.md:95`  
**Wofür:** Kontrast des unguenstigsten Pixels unter der Schrift im fertigen Bild  

kontrast_direkter_hintergrund_max_lum: 2.0 stand nur in bc1876e und ist seit eab1d17 weg; thumbnail.py schreibt das Feld nicht mehr. Eigene Nachrechnung mit der Projektformel kontrast(l)=1.05/(l+0.05) ueber die Glyphenmaske im fertigen Bild: altes motiv-V3.png 2,04:1 (deckt die 2,0 des Altstands exakt), aktuelles motiv-V3.png 3,59:1. Der Bericht nennt fuer das heutige Bild also einen um 44 % zu niedrigen Wert.

### `~10,3 Mbit/s` — mittel

**Wo:** `produktion/motive/README.md:261`  
**Wofür:** Rohbitrate der von Seedance gelieferten KI-Clips; Grundlage der 16,6-GB-Hochrechnung und des "Bitraten-Vorfalls"  

Bestaetigt, jetzt exakt statt nur ueberschlaegig. Ich habe die MP4-Container der eingecheckten V01-Clips selbst geparst (moov/trak/stsz-Sampletabelle gegen mdhd-Dauer) — die Clips haben nur eine Videospur, keinen Ton, Overhead scheidet als Erklaerung also aus. Videospur-Bitraten: clip-1 11,934 · clip-2 10,269 · clip-3 11,383 · clip-4 11,275 Mbit/s, zusammen 11,215 Mbit/s. Das deckt sich mit der eingecheckten qa-ki-clips.json (groesse_mb 17.98/15.47/17.15/16.99 bei dauer_s 12,042). "~10,3" trifft ausschliesslich clip-2 und untertreibt den Satz um 8 %. Kein Deckungsfund in irgendeiner anderen Messdatei.

### `3,52 h` — mittel

**Wo:** `produktion/motive/README.md:319`  
**Wofür:** Laufzeit von Video 02, auf die die Bildspurgroesse hochgerechnet wird  

Bestaetigt und besser belegt als gemeldet. Es gibt zwar keine Render-QA im Repo (produktion/arbeit/ ist gitignored), aber ein eingechecktes, maschinell geschriebenes Artefakt traegt die Laufzeit sehr wohl: produktion/video-02/video-02.srt endet mit dem Cue 03:37:23,123 --> 03:37:24,883. Zusammen mit produktion/video-02/upload.md:177 (3:37:32 = 3.62 h) ist die Laufzeit damit repo-intern belegt. Herkunft der 3,52 h geklaert: sie stammen aus dem Planungsstand des Commits 072ef0c vom 2026-08-06 ("rund 2,0 GB Bildspur fuer 3,52 h"); der tatsaechliche Render kam erst mit a4fef38. Der Bericht praesentiert eine Vor-Render-Schaetzung als "die Laufzeit". Die Folgezahl bleibt fast unberuehrt (2,07 statt 2,0 GB).

### `tote Kanäle 4–7` — niedrig

**Wo:** `produktion/workflow-gates.md:36`  
**Wofür:** Gate 1.10, Beleg fuer die CTA-Obergrenze: gescheiterte Kanaele haetten 4 bis 7 CTAs je Video  

Nachgeprueft und bestaetigt. regeln/daten/skript_anatomie.json ist die einzige eingecheckte Quelle mit CTA-Zahlen (rg 'cta_anzahl' ueber alle Nicht-md-Dateien: nur diese Datei plus zwei Pipelineskripte, die das Feld schreiben). Gemessene cta_anzahl der als tot gefuehrten Kanaele: C=4, D=7, E=null (kein Transcript), F=0, G=0, H=3, I=1, J=0. Die tatsaechliche Spanne ist 0–7; '4–7' nennt nur die zwei hoechsten Faelle und praesentiert sie als Band der toten Kanaele. Sechs von acht liegen ausserhalb, die Mehrheit bei 0–1 — also unter dem, was das Gate den Gewinnern zuschreibt. Der Nebenbefund stimmt ebenfalls: D traegt cta_anzahl 7, das Feld ctas listet aber nur sechs Zeitmarken [435, 805, 1216, 1576, 2040, 2508]; bei allen anderen Eintraegen stimmen Zaehler und Liste exakt ueberein (2/2, 4/4, 3/3, 1/1, 0/0), D ist der einzige Ausreisser. Die Gegenseite der Klammer ist sauber: Gewinner-cta_anzahl 2/0/0/2 und die vier Gewinner-CTAs bei 26/37 s bzw. 33/38 s, also in den ersten 60 s. Entlastend: die bindende Grenze des Gates ('hoechstens 2, beide in den ersten 60 s') stuetzt sich auf die korrekte Gewinnerseite und wird durch den Fehler nicht beruehrt.

### `1,3K bis 166K` — niedrig

**Wo:** `produktion/videos-01-08.md:317-318`  
**Wofür:** Behauptete Streubreite der Views von Kanal B - begruendet, dass der schwaecher belegte Anker "If You're Overwhelmed," keine Aussage ueber Zugkraft erlaubt  

Nachgezaehlt und bestaetigt. regeln/daten/listings/B_RestInGrace_videos.jsonl (view_count, alle 13): 140, 303, 559, 660, 788, 911, 1300, 1800, 2500, 32000, 35000, 96000, 166000. regeln/daten/nexlev/katalog_B_RestInGrace.json bestaetigt dasselbe Bild (304 bzw. 915 statt 303/911). Die Untergrenze ist 140, nicht 1.300. Die 1,3K ist ausschliesslich der Viewwert des Ankervideos Bdj77Dfh_AU ("If You're Overwhelmed, Sleep To These Psalms Tonight"), der drei Zeilen darueber korrekt zitiert wird - im Streu-Satz ist er faelschlich zur Untergrenze des Kanals geworden. Gegenprobe: regeln/daten/thumbnail_forensik.json nennt die richtige Spanne selbst ("B-Thumbs sind bei 166.000 UND bei 140 Views praktisch identisch"). Streuung Faktor ~1186 statt 128. Das Argument (Titel erklaeren die Streuung nicht) wird durch die Korrektur staerker, nicht schwaecher.

### `A (Kanalzuordnung in den Zeilen 01 und 05)` — niedrig

**Wo:** `produktion/videos-01-08.md:955, 959`  
**Wofür:** Die Titelpruefungstabelle weist den naechstliegenden Konkurrenztitel "God Knows You're Tired... Sleep To These Psalms Tonight" dem Kanal A zu  

Bestaetigt. Der Titel steht in regeln/daten/nexlev/katalog_B_RestInGrace.json (id JYGUW6LpDio, 140 Views, publishDate 2026-06-05) und in produktion/gewinner_titel.json an Position 10 - die ersten acht Eintraege sind A's Titel, ab Position 9 folgen B's 13. In katalog_A_HushLittleLamb.json (alle 8 Titel geprueft) kommt er nicht vor. Ich habe produktion/titel_pruefung.py ausgefuehrt (Exit 0): das Skript reproduziert alle acht Prozentwerte exakt (50,0 / 44,4 / 44,4 / 44,4 / 50,0 / 44,4 / 50,0 / 50,0) und nennt fuer V1 und V5 genau diesen Titel als naechsten Konkurrenten - gibt aber keinen Kanalbuchstaben aus. Das "A" ist also von Hand ergaenzt und in beiden Zeilen falsch; die uebrigen sechs Zeilen sind korrekt zugeordnet. Betroffen ist nur die Herkunftsangabe, nicht das Pruefergebnis.

### `20-30 Zeilen` — niedrig

**Wo:** `produktion/videos-01-08.md:103`  
**Wofür:** Geschaetzter Umfang von Kapitelmarken bei den Evangelien-Videos (03, 04, 05, 07) - begruendet die Empfehlung, dort keine zu setzen  

Bestaetigt und zusaetzlich empirisch belegt. produktion/korpus/plan.json: V3 43 refs, V4 41, V5 36, V7 43. Das Paketformat ist nachweislich eine Marke je Kapitel plus "Opening prayer": video-01/upload.md fuehrt "## Kapitelmarken (100)" bei 99 refs, video-02 "(93)" bei 92 refs, video-03 "(44)" bei 43 refs - jeweils refs+1. Fuer 03/04/05/07 waeren es also 44/42/37/44 Zeilen, nicht 20-30. Video 03 hat die 44 Marken sogar tatsaechlich im Paket stehen. Der genannte Band 20-30 entsteht nur, wenn man ausschliesslich das jeweilige Evangelium zaehlt (Mk 16, Joh 21, Lk 24, Mt 28) - die Videos enthalten aber jeweils weitere Buecher. als_vorgabe auf false korrigiert: die Zahl 20-30 selbst steht nirgends als bindende Grenze; die von ihr getragene Entscheidung steht in produktion/config.md:116 (kapitelmarken_videos = V1,V2,V6,V8) und in produktion/pipeline/schritt7_paket.py:87-94. Die Fehlrichtung schwaecht die Schlussfolgerung nicht - mehr Marken heisst mehr Ballast.

### `Gospel of John 3,0–3,3× (n=14)` — niedrig

**Wo:** `formel/video-formel.md:378`  
**Wofür:** Multiplikator-Band für den Eigennamen „Gospel of John" — das Zugpferd der Testreihe in §1  

Bestätigt, nachdem ich alle plausiblen Rechenwege durchprobiert habe. n=14 ist die globale Trefferzahl für 'john' — korrekt. Für das Band 3,0–3,3 gibt es aus dem Stichwort 'john' allein keine Grundlage: kanal-normiert ergeben sich NightPsalms 7,30× (n=2), RestInJesus 3,20× (n=1), RestInFaith 3,04× (n=5), SleepCodex 0,24× (n=2), HushLittleLamb 2,11× (n=1), TheSleepBible 3,74× (n=3); gepoolt 2,79×, Median der Kanalwerte 3,12×. Global normiert (die Methode der Revelation/Jeremiah/Genesis-Einträge) ergibt 'john' 8,07× und 'gospel of john' 12,82×. Auch ohne den >300-s-Filter ändert sich nichts. Der einzige Weg zu einer 3,3 führt über ein ANDERES Stichwort: teardown/auswertung_population.txt listet unter 'gospel' RestInFaith 3,33× (n=20), unter 'john' nur RestInFaith 3,04× (n=5). Das Band ist also aus zwei Auswertungen zusammengesetzt; n und Multiplikatoren gehören nicht zur selben Rechnung. Die Nachbarangabe „Gospels 2,8–3,3× (n=31)" ist dagegen sauber (2,84 / 3,33 aus derselben 'gospel'-Zeile; n=31 global).

### `Sermon on the Mount (413K, n=1) · Proverbs (93K, n=1)` — niedrig

**Wo:** `formel/video-formel.md:380`  
**Wofür:** Stichprobengrößen in der Eigennamen-Liste  

Nachgezählt über alle 454 Videos in teardown/teardown_batch_20260802_090410/*_videos.jsonl: 'sermon on the mount' kommt in 2 Videos vor (beide Night Psalms: 13.000 und 413.000 Views), 'proverbs' in 8 Videos (3.700 / 93.000 / 55.000 / 23.000 / 39.000 / 62.000 / 21.000 / 347.000). n=1 ist in beiden Fällen falsch, auch bei exakter Phrasensuche. Alle übrigen n-Werte derselben Aufzählung habe ich gegengerechnet und sie sind exakt die globalen Trefferzahlen: john 14, gospel 31, isaiah 10, enoch 46, angel 36, daniel 11, revelation 12, jeremiah 4, genesis 13, psalm 32. Der Definitionswechsel ist also unangekündigt und betrifft nur diese beiden Einträge. Anders als vom Gegenprüfer stehengelassen ist „Ephesians/Galatians/Colossians (1,0 Mio., n=1)" vertretbar: der zusammengesetzte Titel trifft genau ein Video (Fall Asleep to Ephesians, Galatians, Colossians & Philippians, 1.000.000, The Sleep Bible). Die Views 413K und 93K sind korrekt (auswertung_population.txt, H4).

### `9,9–12,1 %` — niedrig

**Wo:** `formel/thumbnail-checkliste.md:37`  
**Wofür:** Belegte Spanne der Versalhoehe in der 13er-Gewinnerserie, Grundlage des Zielwerts >= 11,5 %  
**Messdatei:** keine — thumb_textmessung.json belegt 10,0–12,2 % (Widerspruch in beiden Randwerten)  

glyph_hoehe_pct der 13 B-Datensaetze: 10,0 / 11,2 / 11,7 / 11,7 / 11,9 (7x) / 12,2 / 12,2. Spanne also 10,0–12,2 %, Median 11,9 % — der Median stimmt, beide Randwerte nicht. 9.9 kommt in der Datei nur bei C_TheBibleSacred/apOTcKsvt6g und F_GodsPeacefulSleep/3HKk8W82EkY vor (beides Verlierer), 12.1 nur als kontrast von A/UV1mdTGnFVY. Auch die GEW-Gesamtmenge (17 mit Text) reicht von 4,3 bis 13,3 % und ergibt keine Spanne 9,9–12,1. Abweichung jeweils 0,1 Prozentpunkte; da der tragende Kennwert (Median 11,9) korrekt ist und die abgeleitete Grenze 11,5 % dadurch nicht beruehrt wird, senke ich die Schwere auf niedrig.

### `n=69 (Verlierer-Versalhoehe Median 9,0–9,5 %)` — niedrig

**Wo:** `formel/thumbnail-checkliste.md:41-42`  
**Wofür:** Fallzahl der Verlierergruppe fuer den Median der Versalhoehe  
**Messdatei:** thumb_textmessung.json deckt 69 als Gruppengroesse, aber nur 61 als Fallzahl des Medians  

Nachgerechnet: BEST 39 Datensaetze, davon 34 mit glyph_hoehe_pct, Median 9,5 %; WORST 30 Datensaetze, davon 27 mit glyph_hoehe_pct, Median 9,0 %. Die Mediane 9,0–9,5 % stimmen exakt. Die Verlierermenge umfasst tatsaechlich 69 Thumbnails (39+30), aber 8 davon haben zeilen=0/glyphen=0 und liefern gar keine Versalhoehe — die Fallzahl hinter dem Median ist 61. Formal ist "(n=69)" im Satz auf die Verlierergruppen bezogen und nicht ausdruecklich auf den Median, deshalb belasse ich es bei niedriger Schwere; die Zahl wird nirgends als Grenze weitergereicht.

### `Nacht 66/90` — niedrig

**Wo:** `formel/thumbnail-motive.md:40`  
**Wofür:** Anteil der Nacht-Thumbnails im 90er-Inventar  
**Messdatei:** keine — motiv_inventar.json zaehlt 65  

Nachgezaehlt in motiv_inventar.json: tageszeit == "nacht" 65x; uebrige Auspraegungen tag 15, daemmerung 4, neutral 4, tag-abend 1, gemischt 1. 66 ergaebe sich nur unter Hinzunahme von "tag-abend", was der Text nicht sagt. Alle uebrigen sieben Zahlen derselben Zeile habe ich gegengerechnet und exakt bestaetigt: Jesus im Bild 85 (90 minus fig 2, hist 2, ort 1), Gesicht 88, Blickkontakt 18, warmes Licht 79, Text 75, Lamm 44, Feuer 46. Nur die Nacht-Zahl ist um 1 zu hoch. Einzige Version der Datei (Commit 650da0a). Reiner Beschreibungswert, keine Grenze — deshalb niedrige Schwere.

### `Tag 0/18` — niedrig

**Wo:** `formel/thumbnail-motive.md:272`  
**Wofür:** Tageszeit-Signal im Abschnitt "Wo die Daten schweigen"  
**Messdatei:** keine — motiv_inventar.json zaehlt 15 Tag-Thumbnails  

motiv_inventar.json: tageszeit=="tag" kommt 15x vor; alle Nicht-Nacht-Auspraegungen zusammen 25x (tag 15, daemmerung 4, neutral 4, tag-abend 1, gemischt 1). Keine Teilmenge der Tageszeit ergibt 18: tag+daemmerung = 19, tag+neutral = 19, tag+tag-abend = 16, tag+tag-abend+gemischt = 17. Die 18 ist im Datensatz die Anzahl der Blickkontakt-Thumbnails — im selben Dokument (Zeile 39) steht sie genau so. Der Nenner ist also mit hoher Wahrscheinlichkeit aus der falschen Spalte uebernommen. Die Zaehlerangabe ("Nacht 10/10 Treffer", "Tag 0") stimmt: alle 10 Treffer sind Nacht, kein Tag-Thumbnail ist Treffer.

### `D 8, H 7, G 2, E 1` — niedrig

**Wo:** `formel/thumbnail-motive.md:94`  
**Wofür:** Kanalverteilung der 18 Frontal-/Blickkontakt-Thumbnails  
**Messdatei:** keine — motiv_inventar.json ergibt D 8, H 6, G 2, E 2  

motiv_inventar.json, blickkontakt==1 nach Kanal: D 8, H 6, G 2, E 2 (Summe 18). Die Summe stimmt, die Aufteilung nicht (H 6 statt 7, E 2 statt 1). Zusatzbefund, der den Fund stuetzt: die Zeile vermischt zwei Groessen — motiv=="jfront" kommt 17x vor und verteilt sich exakt auf D 8, H 6, G 2, E 1; blickkontakt==1 kommt 18x vor. Der 18. Fall ist E_QuietMind/UiVSFtnfK3k (jsit, 261 Views, BEST). Die genannte Verteilung ist also die jfront-Verteilung, die Fallzahl 18 dagegen die Blickkontakt-Fallzahl — und beide passen nicht zusammen.

### `E: BEST 5/5 ohne Blickkontakt` — niedrig

**Wo:** `formel/thumbnail-motive.md:86`  
**Wofür:** Best-gegen-Worst-Befund innerhalb Kanal E  
**Messdatei:** keine — motiv_inventar.json ergibt 4/5  

motiv_inventar.json, E_QuietMind BEST: 512 js bk=0, 486 jchild bk=0, 341 jchild bk=0, 262 jsit bk=0, 261 jsit bk=1. Also 4/5 ohne Blickkontakt. Es ist derselbe Datensatz (261 Views), der schon die Fallzahl-18-Zeile bricht. Die WORST-Haelfte der Aussage stimmt: 69 jfront, 63 jstand, 52 fig, 38 fig, 28 jstand — 5/5 frontal/stehend/Frauenfiguren. Auch die Bezeichnung "Szenen-Jesus" ist fuer BEST nicht ganz sauber, weil 2 von 5 jchild sind. Reiner Beschreibungsbefund ohne Grenzwirkung.

### `4 der 10 Treffer sitzen (A 233K, 201K, 184K, 47K)` — niedrig

**Wo:** `formel/thumbnail-motive.md:222-224`  
**Wofür:** Datenbasis fuer die empfohlene Motivrichtung 2 (sitzender Jesus)  
**Messdatei:** keine — motiv_inventar.json ergibt 3 (233K ist jr)  

motiv_inventar.json, Treffer (>30.000 Views): motiv==jsit genau 3x (A 201K, A 184K, A 47K). A 233K ist als jr erfasst ("Jesus ruhend, wach zurueckgelehnt"). Die Treffer-Tabelle desselben Dokuments in Zeile 54 schreibt korrekt "js 6 · jsit 3 · jr 1" — das Dokument widerspricht sich also selbst. Gegengeprueft und bestaetigt sind die uebrigen Zahlen desselben Absatzes: jsit gesamt 11/90 (stimmt exakt), A 184K ohne Lamm/Feuer/Text (lamm=0, feuer=0, text=0 — stimmt), H's Ausreisser 27.000 ist jsit ohne Blickkontakt (stimmt). Die Empfehlung selbst bleibt tragfaehig, nur mit n=3 statt n=4.

### `7/10 Kanaele >= 50 % dominantes Motiv` — niedrig

**Wo:** `formel/thumbnail-motive.md:141`  
**Wofür:** Beleg, dass Serienkonsistenz in der Nische Standard ist  
**Messdatei:** keine — motiv_inventar.json ergibt 8/10  

Anteil des haeufigsten Motivs je Kanal aus motiv_inventar.json: F 10/10 = 100 %, C 8/10 = 80 %, D 8/10 = 80 %, B 10/13 = 77 %, I 3/4 = 75 %, H 6/10 = 60 %, A 4/8 = 50 %, G 5/10 = 50 %, J 2/5 = 40 %, E 2/10 = 20 %. Bei ">= 50 %" (so steht es im Text) sind es 8 Kanaele, bei strikt "> 50 %" waeren es 6 — die 7 ist unter keiner Lesart erreichbar. Die Werte selbst decken sich mit der Anteils-Tabelle des Dokuments (Zeilen 125–136), die Zusammenfassung eine Zeile spaeter nicht. Die Schlussfolgerung ("Konsistenz ist Standard") wird durch 8/10 eher gestaerkt als geschwaecht.

### `C, D, F: Motivverteilung BEST/WORST identisch` — niedrig

**Wo:** `formel/thumbnail-motive.md:84`  
**Wofür:** Befund "kein Motivsignal" im Best-gegen-Worst-Test  
**Messdatei:** keine — bei C weichen die Randfaelle ab (jteach vs jr)  

motiv_inventar.json, Kreuztabelle je Kanal: D BEST {jfront 4, js 1} vs WORST {jfront 4, js 1} — identisch; F BEST {js 5} vs WORST {js 5} — identisch; C BEST {js 4, jteach 1} vs WORST {js 4, jr 1} — NICHT identisch. Der Unterschied ist allerdings minimal (ein jteach gegen ein jr, beide Einzelfaelle), und die Aussage "kein Motivsignal" bleibt fuer C ebenso tragfaehig, weil das dominante Motiv js in beiden Haelften 4x auftritt. Reine Formulierungsungenauigkeit, keine Grenzwirkung.

### `je Kanal 5 beste und 5 schlechteste (C–J)` — niedrig

**Wo:** `formel/thumbnail-motive.md:12-15`  
**Wofür:** Stichprobenaufbau, auf dem der "saubere Test" Best-gegen-Worst beruht  
**Messdatei:** keine — verlierer_auswahl.json belegt I 4/0 und J 5/0 (Widerspruch)  

Von zwei unabhaengigen eingecheckten Messdateien bestaetigt. regeln/daten/verlierer_auswahl.json fuehrt die Auswahl explizit als best/worst-Listen: C 5/5, D 5/5, E 5/5, F 5/5, G 5/5, H 5/5, aber I best 4 / worst 0 und J best 5 / worst 0. thumb_messung.json und motiv_inventar.json bestaetigen das (I: 4 Datensaetze, alle BEST; J: 5, alle BEST; gesamt BEST 39 / WORST 30, nicht 40/40). Fuer I und J ist der Best-gegen-Worst-Vergleich damit gar nicht durchfuehrbar. Entlastend: das Dokument nennt in seiner eigenen Konsistenz-Tabelle "I 3/4" und "J 2/5" und legt die kleineren Fallzahlen dort offen; die Gesamtzahl 69 Verlierer stimmt ebenfalls.

### `12` — niedrig

**Wo:** `regeln/erfolgsregeln.md:5`  
**Wofür:** Anzahl 'vollstaendige Transkripte' in der Datengrundlage  

regeln/daten/skript_anatomie.json enthaelt 12 Schluessel, aber nur 11 mit Messfeldern (wpm, woerter, sprechbeginn_s ...). Der 12. Eintrag Dk5o37eqgyY (E_QuietMind) besteht ausschliesslich aus {'kanal','label','fehler': 'KEIN TRANSCRIPT: Not Available'} — es gibt kein Transkript, also erst recht kein vollstaendiges. Kein zweites Transkript-Artefakt im Repo (grep ueber alle Nicht-md-Dateien: nur skript_anatomie.json und teardown/analyse.py). Das Dokument selbst rechnet an drei Stellen richtig mit 11 (Z.165–167 '11 Transkripte'). Reiner Kopfzeilen-Fehler um eins; alle uebrigen Grundlagenzahlen der Kopfzeile habe ich nachgerechnet und sie stimmen (150 Langform, 141 Shorts, 90 Thumbs, 19 von 21).

### `0,1–0,5 h` — niedrig

**Wo:** `regeln/erfolgsregeln.md:146`  
**Wofür:** Laufzeit-Spanne der Videos von Verlierer D, Beleg der Verbots-Regel V5  

Gegengeprueft in zwei Messdateien statt einer: regeln/daten/listings/D_GodMessageToday_videos.jsonl UND regeln/daten/nexlev/katalog_D_GodMessageToday.json zeigen uebereinstimmend 0,13–2,05 h. Auch die wohlwollendste Lesart rettet die Spanne nicht: beschraenkt man sie auf die 13 'GOD SAYS'-Kurzvideos bis zum Format-Schwenk am 19.07., reichen sie immer noch bis 0,77 h (J7Cxr4wKEJc 2.788 s, gX2JvLmM-jA 2.665 s, pxQ1mN428vk 2.215 s) — die Obergrenze 0,5 deckt davon nur 10. regeln/daten/kanal_dna.json nennt fuer D dauer_mean_h 0.71 bei sd 0.57, ebenfalls unvereinbar mit '0,1–0,5 h'. Die qualitative Aussage (D macht kurze Droh-Clips) haelt, die Zahl nicht. Die uebrigen Zahlen desselben Satzes sind gedeckt (7 CTAs: skript_anatomie.json/gX2JvLmM-jA cta_anzahl = 7).

### `Tags NUR in der Flop-Phase` — niedrig

**Wo:** `regeln/erfolgsregeln.md:171`  
**Wofür:** Zeitliche Zuordnung der Tag-Nutzung bei B ('B hat Tags beim Breakout abgelegt')  

Alle Zahlen der Zeile sind gedeckt (winner_details.json: A 8x 0 Tags; getaggte B-Videos 5–22 Tags bei 140–2.567 Views; 0 Tags auf 166K/96K/35K). Nicht gedeckt ist die zeitliche Aussage: der Breakout 8m6NqWG9p2o datiert auf 2026-06-25, aber Bdj77Dfh_AU (2026-07-01, 6 Tags) und GMguilmIaP0 (2026-07-05, 22 Tags) liegen danach — B hat nach dem Breakout weiter getaggt, sogar am staerksten. Haltbar ist nur die Lesart 'Tags nur auf Videos, die gefloppt sind'; die Kausalformulierung 'beim Breakout abgelegt' widerspricht der Messdatei. Nicht als Vorgabe weitergereicht: produktion/videos-01-08.md:23-24 entscheidet ausdruecklich gegen die Regel ('Ich liefere Tags, weil sie nichts kosten').

### `99 Kapitelmarken` — niedrig

**Wo:** `produktion/pipeline/README.md:122`  
**Wofür:** Anzahl der Kapitelmarken in Video 01, Vergleichsbasis gegen das Band 40-93  

Bestaetigt: produktion/video-01/beschreibung.txt (eingecheckte .txt in produktion/video-*/) enthaelt 100 Zeitmarkenzeilen, produktion/video-01/upload.md:167 schreibt maschinell '## Kapitelmarken (100)' (schritt7_paket.py:131 gibt len(marken) aus), und die Commit-Message von e59ff94 nennt ebenfalls 100. Alle Versionen der Historie geprueft: beschreibung.txt existiert nur in d36d3b8 und hatte dort schon 100 Zeilen; 99 kommt in keiner Datei und keiner Version vor. Wahrscheinliche Herkunft: 100 minus die Marke '0:00 Opening prayer', also 99 Schriftkapitel - eine Abweichung um eins, die das Argument nicht veraendert (auch 100 liegt 'knapp ueber' 93). Schwere deshalb von mittel auf niedrig.

### `Gebet bis 116 s` — niedrig

**Wo:** `produktion/pipeline/README.md:74`  
**Wofür:** Ende des Eingangsgebets in der Zeitleiste von Video 01  

Bestaetigt gegen produktion/video-01/video-01.srt: Cue 27 'Amen.' endet 00:01:49,080 = 109,08 s, Cue 28 'Psalm one.' beginnt 00:01:49,500 = 109,50 s. Abweichung rund 6,5 s. Die uebrigen Werte desselben Satzes sind dagegen korrekt gemessen (CTA 1 endet 31,38 s -> 'bis 32 s'; CTA 2 endet 38,28 s -> 'bis 38 s'), der Fehler ist also isoliert auf den Gebetsblock. 116 findet sich in keiner Datei; der naechstgelegene Zeitwert (116,70 s) ist das Ende von Cue 29 mitten in Psalm 1 und kein Blockende.

### `55 Hz (A1) + Quinte + Oktave + Duodezime` — niedrig

**Wo:** `stimmtest/musik-prompt.md:58-60`  
**Wofür:** Beschreibung der Teiltoene, aus denen musikbett.py die Pad-Schicht baut  
**Messdatei:** kein Messdatei-Widerspruch; die Abweichung besteht gegenueber dem eingecheckten Generator stimmtest/musikbett.py:42-43. Die Einzelzahlen 55 Hz, 1,8 kHz und 56 s sind gedeckt (musikbett.py:29/:56 bzw. produktion/pipeline/qa/pegel_wiedergabe.json bett_dauer_s 56.0)  

Die Unvollstaendigkeit ist reproduziert: musikbett.py:42-43 baut FUENF Teiltoene — (55,0 | 0.55), (82,5 Quinte | 0.30), (110 Oktave | 0.30), (165 Duodezime | 0.14) UND (220 Doppeloktave | 0.08). Die Doppeloktave fehlt in der Beschreibung. Zusatzbefund: der Fehler entsteht nicht erst im Bericht — der Codekommentar musikbett.py:41 fuehrt selbst nur 'Grundton, Quinte, Oktave, Duodezime - kein Terzton' und ist ebenso unvollstaendig; musik-prompt.md hat ihn nur uebernommen. Alle uebrigen Zahlen des Absatzes sind dagegen gedeckt und von mir nachgerechnet: ROOT = 55.0 (:29), Hoehenabsenkung fr/1800.0 (:56) = 1,8 kHz, Dauer 56 s (LOOP_S 60,0 minus fade_s 4,0; eingecheckte Datei 2.469.600 Samples @ 44,1 kHz = 56,0 s; pegel_wiedergabe.json bett_dauer_s 56.0), 'zwei leicht verstimmte Schichten' (det -0.12/+0.12, :45), 'unregelmaessige Amplitudenbewegung' (LFO-Perioden 23 s und 37 s, :47-49). Das 'Beide' bleibt nur zur Haelfte pruefbar (bett_pad.wav liegt in musik/, gitignored) — die 56-s-Angabe gilt aber fuer beide deterministisch aus derselben Codezeile. Kein Messwertfehler, sondern eine Beschreibungsluecke; Schwere niedrig.

### `180–234 kbit/s` — niedrig

**Wo:** `produktion/motive/README.md:228`  
**Wofür:** Bitratenspanne der vier Animations-Loops  

Bestaetigt, aber ausdruecklich als Rundungsfall. qa-V1..V4.json -> bitrate_kbps 183.2 / 199.6 / 234.1 / 198.0; die gemessene Untergrenze ist 183,2. Auch der Commit eab1d17 nennt korrekt "183-234 kbit/s", und die README-Tabelle Zeile 212 gibt 183 an. Nur der Fliesstext rundet auf eine nicht gemessene 180 ab (1,7 % Abweichung, in die konservative Richtung). Sachlich folgenlos, formal ein Wert ohne Messdatei.

---

## D — abgeleitet oder entschieden

Kein Fehler, solange es dabeisteht. Gemeldet, weil die Zahl anderswo als Messwert auftritt oder der Vorbehalt an der bindenden Stelle fehlt.

### `12 dB (Zahl 12)` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:37`  
**Wofür:** Gate 1.11, geforderter Pegelabstand Stimme zu Klangbett  

Bestaetigt, und der Fund ist staerker als gemeldet. Der qualitative Beleg ist gedeckt: regeln/daten/stimm_stichprobe.json, Abschnitt STIMMTEST_2026-08-03, enthaelt genau 6 Videos (3 GEWINNER, 3 VERLIERER), jedes mit einem Feld musikbett, das auf 'Stimme klar obenauf' endet; der Unterabschnitt KLANGBETT_ERSTMALS_GEMESSEN formuliert 'Stimme in 3/3 klar ueber dem Bett'. Ein dB-Wert steht nirgends in der Datei — 6/6 ist qualitativ, die 12 ist abgeleitet, und das Gate kennzeichnet das vorbildlich. Gemeldet bleibt sie, weil sie danach genau als Messgroesse auftritt: produktion/config.md:70 abstand_soll_db = 12.0 · produktion/pipeline/qa/pegel_wiedergabe.json soll_abstand_db 12.0, toleranz_db 1.0, bestanden false · alle vier produktion/video-0*/upload.md fuehren 'Abstand Stimme zu Bett | 12.0 dB | 12.0 dB (§5b)' als bestandenen Messwert. Zusatzbefund aus meiner Gegenpruefung: auch der scheinbar gemessene Gegenwert ist keiner. pegel_wiedergabe.json vermerkt selbst 'stimme_quelle': 'config.md: pegel_stimme_dbfs (Sollwert)' und pegelt das Bett per gain_bett_db 0.198 auf exakt -31,0 dBFS — abstand_mono_db 12.0 faellt damit rechnerisch aus zwei Sollwerten heraus und ist keine unabhaengige Messung. Die uebrigen Zahlen der Mono/Stereo-Tabelle (Zeilen 54-57) habe ich gegen die Datei geprueft und alle bestaetigt: -31,00 / 12,00 / -25,80 (Datei -25.802) / 6,80 / 5,20 (downmix_verlust_db 5.198) / -0,396 (bett_korrelation_LR -0.39579).

### `3.8 (laufzeit_ziel_bis_h)` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/config.md:132`  
**Wofür:** Obergrenze des Ziel-Laufzeitbands, unter der Ueberschrift "(Formel §2)" gefuehrt und dadurch wie ein datengestuetzter Wert lesbar.  

Listings selbst ausgewertet: regeln/daten/listings/A_HushLittleLamb_videos.jsonl (8 Videos, 3,56-5,31 h) und B_RestInGrace_videos.jsonl (13 Videos, 1,10-3,60 h). Die 10 Treffer (>=32.000 Views) liegen bei 3,44 / 3,46 / 3,56 / 3,56 / 3,56 / 3,58 / 3,60 / 4,12 / 4,38 / 5,02 h, Median 3,57 h - das deckt die Untergrenze 3,4 und den in Formel §2 genannten Median 3,6 h, aber nicht die Obergrenze 3,8: sie schneidet 4,12 h/245K, 4,38 h/36K und 5,02 h/233K ab. Formel §2 kennzeichnet das Band ausdruecklich als "Kostenentscheidung" und schreibt "Eine Obergrenze ist weiterhin nicht belegt (A trifft auch bei 5,0 h)". Damit sauber D - kein Fehler, aber der Vorbehalt fehlt an der Stelle, wo die Zahl bindend wird: config.md unter "(Formel §2)", workflow-gates.md:27 (Gate 1.1 "Ziel 3,4-3,8 h") und schritt5_video.py, das im_zielband daraus berechnet.

### `10:1` — mittel · **als Vorgabe weitergegeben**

**Wo:** `formel/thumbnail-checkliste.md:38, :45, :110`  
**Wofür:** Bindender Mindestkontrast Text/Hintergrund  
**Messdatei:** keine fuer 10:1 selbst; das echte B-Minimum 10,7 in thumb_textmessung.json stuetzt die Grenze aber inhaltlich  

Bestaetigt als D: keine Messdatei fuehrt 10:1 als gemessenen Wert, und das Dokument kennzeichnet die Zahl ausdruecklich als Setzung ("bewusst hoch angesetzt"). Der Missbrauchstest faellt negativ aus — 10:1 erscheint nirgends als Messwert, sondern durchgehend als Soll-Spalte (workflow-gates.md Gate 1.6, videos-01-08.md:84, upload-checkliste.md:59, thumbnail.py KONTRAST_MIN = 10.0). Meldung bleibt trotzdem berechtigt, aber aus einem anderen Grund als vom Erstpruefer genannt: die im selben Absatz gegebene Begruendung ("schlechtester Wert 10,1") ist falsch. Wichtige Entlastung: der echte B-Minimalwert ist 10,7 — die Grenze 10:1 liegt also innerhalb des belegten Musters und ist sachlich unbedenklich, nur ihre Herleitung ist es nicht.

### `12 dB / 12,0 dB (abstand_soll_db)` — mittel · **als Vorgabe weitergegeben**

**Wo:** `produktion/pipeline/README.md:92-106; produktion/pipeline/schritt3_bett.py:7`  
**Wofür:** Pegelabstand Stimme zu Klangbett, im README ausdruecklich als abgeleitet gekennzeichnet  

Die Selbstauskunft des README stimmt: regeln/daten/stimm_stichprobe.json enthaelt null Treffer fuer db/rms/lufs (case-insensitive gezaehlt), dort steht nur qualitativ 'Stimme klar obenauf'. Die Kennzeichnung als Ableitung ist also korrekt und der Fund als D richtig eingeordnet. Bestaetigt ist auch der Meldegrund: die Zahl tritt anderswo mit Datenbeleg-Etikett auf - produktion/video-01/upload.md:192 fuehrt sie in der Messwert-Tabelle als 'Abstand Stimme zu Bett | 12.0 dB | 12.0 dB (§5b)', wobei §5b im Formel-Dokument nur den qualitativen 6/6-Hoereindruck traegt. Bindend gesetzt ist sie in produktion/config.md:70 (abstand_soll_db = 12.0) und wird von schritt3_bett.py:193-200 mit ±1 dB Toleranz geprueft.

### `Ziel 3,4–3,8 h` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:27 (wiederholt in :109)`  
**Wofür:** Gate 1.1, Ziel-Laufzeitband des Korpus  

Bestaetigt, geteilte Deckung. Die Untergrenze 3,4 ist gemessen: das Minimum der 10 Treffer liegt bei 3,4425 h (regeln/daten/listings/B_RestInGrace_videos.jsonl, 8m6NqWG9p2o, duration 12393). Die Obergrenze 3,8 steht in keiner Messdatei — die gemessenen Treffer reichen bis 5,0236 h, und formel/video-formel.md haelt im selben Absatz ausdruecklich fest: 'Eine Obergrenze ist weiterhin nicht belegt (A trifft auch bei 5,0 h)'. Damit ist 3,8 eine Kostenentscheidung. Sie wird als Zahl weitergereicht: produktion/config.md:132 laufzeit_ziel_bis_h = 3.8, produktion/pipeline/schritt7_paket.py:147 schreibt sie in den Paketbericht, und alle vier produktion/video-0*/upload.md fuehren 'Ziel 3.4–3.8 h' in der Vorgabespalte. Die Kennzeichnung ist schwaecher als bei 1.11: das Gate schreibt 'Ziel', nennt aber nicht, dass die Obergrenze unbelegt ist — diese Einschraenkung steht nur in Formel §2, auf die die Woher-Spalte pauschal verweist. Genau der Fall, den D melden soll.

### `< 50 %` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:28`  
**Wofür:** Gate 1.2, maximal erlaubte Titelaehnlichkeit zu jedem Gewinnertitel  

Bestaetigt. Fuer die 50 gibt es keine Messdatei — es ist eine gesetzte Schwelle, und sie ist im Gate nicht als solche gekennzeichnet. Die vom Erstpruefer gemeldete Grenzabweichung habe ich im Quelltext verifiziert: produktion/titel_pruefung.py definiert pruefe(eigene, fremde, grenze=0.5) und entscheidet mit 'ok = anteil <= grenze', die Ausgabe lautet 'Grenze 50 %'. Exakt 50 % passieren also, waehrend das Gate '< 50 %' fordert. Der Docstring derselben Datei formuliert das Kriterium als 'kein eigener Titel darf mehr als die Haelfte ... teilen' — das deckt sich mit dem <=, nicht mit dem < des Gates. Die Abweichung liegt somit zwischen Dokument und ausfuehrendem Skript, nicht gegen eine Messdatei. Der Beleg derselben Zeile ist sauber und von mir gegengeprueft: regeln/daten/thumb_jobs.json fuehrt ['F_GodsPeacefulSleep','BEST','chbqtGJ1oRE',18,"I Know You're Tried... Jesus Watches Over you Toni"] gegen A's UV1mdTGnFVY mit 233.000 — Kopie inklusive Tippfehler, 18 Views, exakt wie im Gate zitiert.

### `≥ 10 : 1` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:32`  
**Wofür:** Gate 1.6, Mindestkontrast Thumbnail-Text zum direkten Hintergrund  

Bestaetigt. regeln/daten/thumb_textmessung.json misst fuer die Referenzserie B (n=13) Kontraste von 10,7 bis 18,1 bei Median 15,8 — die 10 liegt bewusst unter dem gemessenen Minimum und ist damit eine Entscheidung, keine Messung. produktion/pipeline/thumbnail.py:36 setzt sie als KONTRAST_MIN = 10.0. formel/thumbnail-checkliste.md:45-47 kennzeichnet die Entscheidung ausdruecklich ('Der Kontrastwert 10:1 ist bewusst hoch angesetzt'), das Gate uebernimmt nur die Zahl ohne diesen Vermerk. Der Nebenbefund des Erstpruefers zur Herkunft ist bestaetigt und wiegt schwerer als er ihn darstellt: die Zielwerte-Tabelle der Checkliste (Zeile 38) gibt die belegte Spanne mit '10,1–17,5:1, Median 15,4:1' an — gemessen sind 10,7–18,1 bei Median 15,8. Die Checkliste begruendet die 10 sogar mit 'keinen Grund, unter ihren schlechtesten Wert (10,1) zu gehen', und genau diese 10,1 steht so nicht in der Messdatei. Die Datei hat seit ihrem einzigen Commit (8141d47) unveraenderte Werte, eine aeltere Fassung als Erklaerung gibt es also nicht. Eine Korrektur am Erstbefund: die eigenen Thumbnails erfuellen die Grenze, aber die Zahlen 16,7–19,4 sind kontrast_direkt_mittel; geprueft wird laut thumbnail.py:126 kontrast_direkt_p95, und der liegt bei 14,0 / 14,1 / 18,0 / 18,9 / 17,7 — weiterhin klar ueber 10, aber deutlich naeher dran.

### `300 (zoom_zyklus_s)` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/config.md:124`  
**Wofür:** Laenge des Atem-Zoom-Zyklus in Sekunden; harte Vorgabe, wird in schritt5_video.py:39 gelesen. Der Kommentar behauptet zusaetzlich, dieser Zyklus sei nahtlos schleifbar.  

Alle vier eingecheckten Loop-Messungen produktion/motive/loops/qa-V1.json bis qa-V4.json melden dauer_s 60.0 mit wrap_unauffaellig=true und naehte_unauffaellig=true - belegt ist die Nahtlosigkeit also fuer 60 s, nicht fuer 300 s. Zu einem 300-s-Zyklus existiert kein Artefakt (qa_video.json liegt in produktion/arbeit/). produktion/motive/README.md:234 weist die Zahl selbst als Ableitung aus ("300 ist ein ganzzahliges Vielfaches von 60 ... 5 Loop-Durchlaeufe je Zoom-Atemzug"), config.md uebernimmt diesen Hinweis nicht. Ergaenzend: unter der aktiven Einstellung videoquelle = ki_clips laeuft zyklus_bauen() gar nicht (schritt5_video.py:120 ff.), der 300-s-Zyklus beschreibt die aktuellen Renderlaeufe also nicht - qa_video.json protokolliert trotzdem zoom=true und zoom_faktor (Zeile 186).

### `1.04 (zoom_faktor)` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/config.md:120`  
**Wofür:** Zielfaktor des Atem-Zooms; harte Vorgabe, wird in schritt5_video.py:40 und :186 gelesen und in qa_video.json protokolliert.  

Erneute Suche nach 1[.,]04 ueber alle eingecheckten Datendateien: einziger Treffer bleibt "frameschritt_max": 1.046 in produktion/motive/loops/ki-v04/qa-ki-clips.json - ein Mass fuer Bildunterschiede zwischen Frames, sachlich ohne Bezug zum Zoomfaktor. produktion/pipeline/README.md:120 kennzeichnet den Wert selbst als ungedeckt ("Zoom-Zyklus 300 s, Faktor 1,04. 'Langsam' ist belegt, eine Zahl nicht."); in config.md steht er ohne diesen Vorbehalt. Wie bei 300 gilt: unter videoquelle = ki_clips wird der Faktor nie angewandt, aber weiterhin in qa_video.json als angewandt protokolliert.

### `3.0 (laufzeit_min_h)` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/config.md:130`  
**Wofür:** Harte Untergrenze der Laufzeit; wird in produktion/workflow-gates.md:27 als Gate 1.1 und in den Upload-Checklisten als Pruefkriterium gefuehrt.  

Die Belegaussage habe ich exakt nachgerechnet: B_RestInGrace_videos.jsonl enthaelt genau 6 Videos unter 3 h (1,10/1,21/1,36/1,92/2,17/2,83 h) mit hoechstens 2.500 Views - "kein Video unter 3 h je ueber 2.500 Views (n=6)" stimmt fuer diese Population Wort fuer Wort. Ueber alle eingecheckten Listings A-J (150 Videos) faellt die Absolutform aber zusaetzlich: H_TimeForGod "Jesus' Most Powerful Teaching: The Sermon on the Mount" hat 1,24 h und 27.000 Views - ein Gegenbeispiel, das der Erstpruefer nicht nennt und das nicht aus Lauf 1 stammt. Dazu die von ihm gefundenen Lauf-1-Gegenbeispiele in matrix_voll.csv (1,89 h/1.025.839; 2,35 h/551.916; 1,16 h/49.000; 1,39 h/28.078). Die 3,0 ist damit eine auf A/B beschraenkte Entscheidung, steht in config.md und Gate 1.1 aber unbeschraenkt.

### `2100 Hz` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/config.md:19`  
**Wofür:** Grenze, unterhalb derer ein Token als rhotisch gilt; entscheidet jede Zeile der Akzentpruefungs-Tabelle in config.md. Als phonetische Tatsache formuliert, tatsaechlich eine gesetzte Schwelle (GRENZE_HZ = 2100.0 in produktion/pipeline/rhotik.py:45).  

2100 taucht in keiner Messdatei als gemessener Wert auf; die einzigen sachbezogenen Fundstellen sind der Konstantendefinition rhotik.py:45 (GRENZE_HZ = 2100.0), ihr Docstring rhotik.py:15 und config.md:19. stimmtest/akzent_rhotik.json vollstaendig geprueft: rhotische Stimmen bis 1872,0 Hz ("w2w" 5/5), nicht-rhotische ab 2132,0 Hz ("Calm Meditation Guide" 0/3, "Gentle Reflective Voice" 2156,0 Hz 0/4) - die Schwelle liegt exakt in der Luecke 1872-2132 und ist damit an den Daten kalibriert, aber selbst kein Messwert. In config.md ist sie als phonetische Tatsache formuliert ("darunter wird das r gesprochen"), nicht als Setzung. Die uebrigen Tabellenwerte sind unstrittig gedeckt.

### `3,53 h · 3,60 · 3,57 · 3,70 · 3,56 · 3,65 · 3,47 · 3,55 h` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/videos-01-08.md:128, 218, 321, 437, 558, 657, 750, 853`  
**Wofür:** Laufzeit je Video, in jedem Videoblock unter der Ueberschrift "Gemessen:" gefuehrt  
**Messdatei:** produktion/korpus/plan.json - Feld "stunden" je V1-V8 enthaelt exakt 3.53 / 3.6 / 3.57 / 3.7 / 3.56 / 3.65 / 3.47 / 3.55  

Die Werte selbst sind durch eine eingecheckte Messdatei gedeckt (plan.json), die Wortzahlen ebenso. Die Einordnung als D bleibt trotzdem richtig: die Stunde ist keine Messung, sondern round(w/140/60,2) aus produktion/wortzahlen.py:37. produktion/config.md:49 setzt dagegen wpm_erwartet = 145.9, gemessen belegt in stimmtest/analyse_runde1.json und stimmtest/qa_bericht.json ("wpm": 145.9), und produktion/pipeline/schritt1_text.py:189-204 rechnet laufzeit_erwartet_h mit genau diesem Wert - die Pipeline verwendet also eine andere Annahme als der Plan. Die real gerenderten Laufzeiten weichen entsprechend ab: V01 3,58 statt 3,53, V02 3,62 statt 3,60, V03 3,47 statt 3,57, V04 3,58 statt 3,70 (produktion/video-0*/upload.md). Nur die V1-Zeile nennt "bei 140 WPM"; die anderen sieben stehen als "Gemessen:" ohne die Annahme.

### `3,4-3,8 h` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/videos-01-08.md:32`  
**Wofür:** Zielband der Korpuslaenge, im Plan als mit Formel §2 deckungsgleich dargestellt  
**Messdatei:** formel/video-formel.md §2 kennzeichnet es selbst als Empfehlung; die Rohdaten stehen in regeln/daten/nexlev/katalog_A_HushLittleLamb.json + katalog_B_RestInGrace.json (lengthSec)  

Als D bestaetigt. formel/video-formel.md:85-95 formuliert das Band ausdruecklich als Empfehlung ("Ein Zielband von 3,4-3,8 h trifft die Datenlage besser") und haelt im selben Absatz fest: "Eine Obergrenze ist weiterhin nicht belegt (A trifft auch bei 5,0 h)". Die 10 Treffer aus den Katalogdateien nachgerechnet: 3,44 / 3,46 / 3,56 / 3,56 / 3,56 / 3,58 / 3,60 / 4,12 / 4,38 / 5,02 h, Median 3,57. Korrektur am Fund: DREI von 10 Treffern liegen ueber 3,8 h (4,12 / 4,38 / 5,02), nicht vier. Die Untergrenze 3,4 ist datennah, die Obergrenze 3,8 ist eine Kostenentscheidung - und steht als harte Vorgabe in produktion/config.md (laufzeit_ziel_bis_h = 3.8) sowie produktion/workflow-gates.md Gate 1.1. Das ist genau der D-Fall, der zu melden ist.

### `5 Tage = 1,4 Uploads/Woche` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/videos-01-08.md:39-52`  
**Wofür:** Upload-Abstand und daraus abgeleitete Wochenfrequenz des eigenen Achterblocks  
**Messdatei:** Referenzband belegt in regeln/daten/nexlev/winner_details.json (publishDate); die 1,4 selbst in keiner Messdatei  

Als D bestaetigt. regeln/daten/kadenz.json vollstaendig gelesen: enthaelt nur uploads_pro_woche (A 0,9 · B 1,5) und keinerlei Abstandsdaten; regeln/daten/listings/B_RestInGrace_videos.jsonl fuehrt timestamp durchgehend null. Die 1,4 ist reine Arithmetik (7/5) aus einer Planungsentscheidung und steht in keiner Messdatei. Der Referenzteil des Satzes ist dagegen sauber belegt, nur in einer anderen Datei als vermutet: aus regeln/daten/nexlev/winner_details.json (publishDate, 11 B-Videos) ergeben sich fuer B genau 10 Abstaende - 3,97 / 3,98 / 3,98 / 4,02 / 4,03 / 4,24 / 4,81 / 5,08 / 5,90 / 6,82 Tage, alle im Band 4-7 (A dagegen 7 Abstaende, 2,23 bis 19,98 Tage). Die Obergrenze 2/Woche ist eine Ableitung aus kadenz.json (alle 8 Verlierer 2,0-13,5/Woche); formel/video-formel.md §6 nennt fuer die Gewinner 1,3-1,5/Wo, worin die geplante 1,4 liegt.

### `12 dB` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/videos-01-08.md:94`  
**Wofür:** Pegelabstand Stimme ueber Klangbett als Vorgabe fuer alle acht Videos  
**Messdatei:** stimmtest/qa_r2.json (5x abstand_stimme_bett_db 12.0), stimmtest/qa_v2.json (stimme_ueber_bett_db 12.1 / 12.0 / 12.0), produktion/pipeline/qa/pegel_wiedergabe.json (abstand_mono_db 12.0, soll_abstand_db 12.0)  

Als D bestaetigt: die 12 dB sind eine eigene Festlegung (produktion/config.md:70 abstand_soll_db = 12.0), aus den Konkurrenzdaten stammen sie nicht - formel/video-formel.md §5b misst dort nur die Richtung ("Stimme in 6/6 Faellen klar ueber dem Bett"), keinen dB-Wert. Als erreichter eigener Messwert ist die Zahl jedoch durch drei eingecheckte Messdateien voll gedeckt (siehe Belegstelle), sie ist also weder erfunden noch unbelegt. Korrektur am Fund: der Plan formuliert sie NICHT wie einen Feldbefund - der Satz steht im Block "## Gemeinsame Vorgaben fuer alle acht" und traegt keine Datenquellenangabe. Schwere bleibt niedrig; kein Handlungsbedarf ausser der sauberen Kennzeichnung als Zielwert.

### `max. 4 Woerter · ≥ 11,5 % · ≥ 125 px · ≥ 10:1` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/videos-01-08.md:83-84`  
**Wofür:** Harte Thumbnail-Schwellen fuer alle acht Videos  
**Messdatei:** Einhaltung gedeckt durch produktion/video-01..04/thumbnail*_messung.json und produktion/motive/text_messung.json; Herleitungsdaten in regeln/daten/thumb_textmessung.json  

Als D bestaetigt: die vier Werte sind Festlegungen von formel/thumbnail-checkliste.md (Zielwert-Tabelle und Upload-Checkliste), keine gemessenen Groessen. Ihre Einhaltung ist sauber belegt - alle vier gebauten Thumbnails fuehren versalhoehe_px 125, versalhoehe_pct 11.57, woerter 3, kontrast_direkt_mittel 16,7 bis 19,4. Der Nebenbefund des Funds ist ebenfalls bestaetigt und liegt in formel/thumbnail-checkliste.md:37-38, nicht in videos-01-08.md: die Datei gibt als Herleitung "9,9-12,1 %, Median 11,9 %" und "10,1-17,5:1, Median 15,4:1" an, waehrend regeln/daten/thumb_textmessung.json fuer B (n=13) glyph_hoehe_pct 10,0-12,2 (Median 11,9) und kontrast 10,7-18,1 (Median 15,8) ergibt - beide Randwerte und der Kontrastmedian sind leicht danebengegriffen. Die Schwellen selbst bleiben davon unberuehrt, weil sie unterhalb der belegten Spannen liegen.

### `Zoom-Zyklus 300 s, Faktor 1,04` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/pipeline/README.md:120`  
**Wofür:** Laenge und Staerke des Atem-Zooms der Videospur  

Einordnung als D bestaetigt: der README fuehrt beide Zahlen im Abschnitt 'Wo kein Dokument etwas sagt' und schreibt ausdruecklich 'Langsam ist belegt, eine Zahl nicht' - also selbst gekennzeichnete Setzung, kein Fehler. Bindend gesetzt in produktion/config.md:120/124 (zoom_faktor = 1.04, zoom_zyklus_s = 300) und maschinell gelesen in produktion/pipeline/schritt5_video.py:38-40 (T = cfg.get('zoom_zyklus_s', 300), A = float(cfg['zoom_faktor']) - 1.0). Geprueft, ob die Zahlen anderswo als Messwert auftreten: in keiner eingecheckten Messdatei und in keiner upload.md - qa_video.json (mit zoom_faktor) liegt unter produktion/arbeit/. Meldung also berechtigt als Warnung, aber ohne Befund.

### `1,5 s Vorlauf mit 1,5 s Einblende` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/pipeline/README.md:61-62`  
**Wofür:** Laenge des Bett-Vorlaufs vor dem Spracheinsatz; Ersatz fuer die 4 s aus stimmtest/musik-prompt.md  

Einordnung als D bestaetigt und das Ergebnis unabhaengig geprueft: produktion/config.md:85-86 setzt vorlauf_s = 1.5 und einblende_s = 1.5 mit ausdruecklicher Begruendung als Entscheidung gegen musik-prompt.md; alle vier eingecheckten SRTs (produktion/video-0{1,2,3,4}/video-0*.srt) beginnen exakt bei 00:00:01,500 - die Setzung ist also umgesetzt und ihr Ergebnis gemessen belegt. Der Meldegrund trifft zu (produktion/video-01/upload.md:195 fuehrt 'erste Kachel | 1.5 s' in der Messwert-Tabelle), ist hier aber unkritisch: das ist eine echte Messung am Rendering, die zufaellig mit der Vorgabe zusammenfaellt. Kein Fehler.

### `H.264, CRF 28, AAC 192 kbit/s` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/pipeline/README.md:116`  
**Wofür:** Encoding-Parameter der Pipeline  

Einordnung als D bestaetigt: die Werte stehen bindend in produktion/config.md:125-127 (video_crf = 28, video_preset = medium, audio_bitrate = 192k) und werden in schritt5_video.py:52/73 gelesen; sie treten in keiner Messdatei und keiner upload.md als Messwert auf. Kein Fehler. Zwei Korrekturen am Fund selbst: (1) die Begruendung des Vorpruefers stimmt so nicht - regeln/erfolgsregeln.md enthaelt null Treffer fuer Codec, Bitrate, Aufloesung, Dateigroesse oder Encoding (274 Zeilen durchsucht), fuehrt diesen Negativbefund also nicht; auch teardown/produktions-spec.md nennt weder Codec noch Bitrate (nur die Abdeckungsluecke 'Aufloesung, fps 5/24'). Der Satz produktion/pipeline/README.md:114-115 zitiert damit eine Quelle, die das nicht sagt - ein Zitat-, kein Zahlenbefund, aber derselben Sorgfaltsluecke zuzurechnen. (2) Die Selbsteinordnung 'Wo kein Dokument etwas sagt' bleibt inhaltlich richtig, weil tatsaechlich kein Dokument Encoding-Daten fuehrt.

### `12` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/workflow-gates.md:37`  
**Wofür:** Soll-Pegelabstand Stimme ueber Bett; laut Gate 1.11 ausdruecklich eine abgeleitete, nicht gemessene Zahl  
**Messdatei:** produktion/pipeline/qa/pegel_wiedergabe.json — soll_abstand_db 12.0 ist dort ausdruecklich das Soll  

Die Ableitung ist bestaetigt: Gate 1.11 kennzeichnet sie ausdruecklich ("qualitativ belegt, die Zahl 12 ist abgeleitet"), config.md:65-68 fuehrt abstand_soll_db = 12.0 unter der Ueberschrift "Formel §5b: Stimme in 6/6 Faellen klar ueber dem Bett". Die Einordnung des Fundes ist aber zu scharf: in den Uploaddokumenten steht die 12 in der VORGABE-Spalte (schritt7_paket.py:161-162 schreibt qm['soll_abstand_db'] mit dem Zusatz "(§5b)"), also korrekt als Soll und nicht als Messwert. Der eigentliche D-Punkt liegt in der Wert-Spalte: die dort gemeldeten 12,0 dB sind ihrerseits konstruktionsbedingt gleich dem Soll (siehe Fund 2). Deshalb Schwere von hoch auf niedrig gesetzt.

### `−19,0 dBFS` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/video-01/upload-checkliste.md:52`  
**Wofür:** "Stimme"-Pegel in der Klammer der Zeile Abstand Stimme zu Bett, praesentiert als Messwert des Renderlaufs  
**Messdatei:** produktion/pipeline/qa/pegel_wiedergabe.json — stimme_dbfs -19.0 mit Feld stimme_quelle "(Sollwert)"  

Bestaetigt und durch Code gehaertet: pegel_wiedergabe.json markiert stimme_dbfs -19.0 selbst als "config.md: pegel_stimme_dbfs (Sollwert)", und schritt3_bett.py:60-61 berechnet den Stimmen-Gain als g_stimme = 10^(pegel_stimme_dbfs/20) / 10^(sprach_rms_db/20) — die Sprach-RMS landet danach zwangslaeufig auf genau -19,0 dBFS. In der Checkliste erscheint der Wert ohne diesen Hinweis als Messwert des Renderlaufs. Das Bett-Pendant -31,0 ist dagegen aus dem gemessenen Rohwert -31,198 abgeleitet (bett_rms_roh_mono_dbfs) und ebenfalls auf den Sollwert normiert. Schwere von mittel auf niedrig: die Zahl ist nicht falsch, nur ihr Status.

### `1,5 s` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/video-01/upload-checkliste.md:49`  
**Wofür:** "Sprechbeginn" bzw. "erste Kachel", in allen fuenf Dokumenten als Messwert des Renderlaufs gefuehrt  
**Messdatei:** produktion/video-0*/*.srt (alle 00:00:01,500) · schritt6_srt.py:188 — der Wert ist vorlauf_s aus config.md:86  

Bestaetigt und im Code gehaertet: schritt6_srt.py:188 setzt basis = vorlauf + c['start_s'], und erste_kachel_s (Zeile 254) ist damit vorlauf_s plus dem Startzeitpunkt des ersten erkannten Wortes im ersten Chunk. Ich habe alle vier eingecheckten SRTs geprueft — jede beginnt auf 00:00:01,500, also exakt dem config-Wert vorlauf_s = 1.5 (config.md:83-86, dort ausdruecklich als Entscheidung begruendet). Der Wert ist eine gesetzte Groesse, die als Messwert des Renderlaufs erscheint. Die Vorgabe "Sekunde 0-3 (n=24)" ist dagegen belegt: matrix_voll.csv hat genau 24 Datenzeilen mit sprache_start_s.

### `12 dB / 12,0 dB` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `stimmtest/musik-prompt.md:49 (auch :47, Tabelle :15)`  
**Wofür:** Pegelabstand Stimme ueber Musikbett — die 'einzige harte Abmischregel' des Kanals  
**Messdatei:** stimmtest/qa_v2.json (stimme_ueber_bett_db 12.1/12.0/12.0 — echte Nachmessung des Mixes; deckt die Umsetzung, nicht die Herleitung)  

Kernaussage haelt: regeln/daten/stimm_stichprobe.json enthaelt (von mir vollstaendig gelesen) keinen einzigen dB-, RMS- oder LUFS-Wert; der 6/6-Befund lautet woertlich nur 'Stimme klar obenauf'. Ebenso formel/video-formel.md:236 — §5b nennt KEINE Zahl. Bestaetigt auch die Zirkularitaet: final_r2.py:50 schreibt round(VOICE_DB-BETT_DB,1), und pegel_wiedergabe.py:66+71+91 setzt bett_mono per Gain exakt auf den Sollwert, sodass abstand_mono_db 12.0 rechnerisch zwangslaeufig ist. Einzig qa_v2.json ist eine echte Nachmessung am fertigen Mix (mix_v2.py:87 misst sprach_rms(v) - rms(bett)), Ergebnis 12,1 / 12,0 / 12,0. ABER die Schwere ist zu hoch angesetzt: das Projekt legt die Ableitung selbst und prominent offen — produktion/workflow-gates.md:37 schreibt woertlich 'qualitativ belegt, die Zahl 12 ist abgeleitet', und produktion/pipeline/README.md fuehrt einen eigenen Abschnitt 'Die 12-dB-Regel ist nicht gemessen'. Das ist ein sauber deklarierter D-Fall, kein verdeckter Fehler. Der verbleibende Mangel, den der D-Meldetrigger verlangt: die Zahl tritt anderswo doch als Messwert-mit-Quelle auf — produktion/video-0{1,2,3,4}/upload.md fuehren 'Abstand Stimme zu Bett | 12.0 dB | 12.0 dB (§5b)' und schreiben sie damit einer Formel-Sektion zu, die sie nicht enthaelt; die Ist-Spalte stammt aus dem nie eingecheckten qa_mix.json (Systembefund produktion/arbeit/).

### `2100 Hz` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/pipeline/rhotik.py:15 und :45; produktion/config.md:19`  
**Wofür:** F3-Grenze: unterhalb dieses Formant-Minimums gilt ein postvokalisches /r/ als gesprochen (rhotisch)  
**Messdatei:** keine Messdatei nennt 2100; die Robustheit ist aber belegt durch produktion/pipeline/qa/rhotik_lang.json (max. rhotisch 1968,9 Hz — 'lord' @887,28 s; min. nicht-rhotisch 2112,6 Hz — 'darkness' @21,88 s) und rhotik_referenz.json (min. nicht-rhotisch 2124,0 Hz)  

Suche bestaetigt: git grep '2100' ueber alle eingecheckten Nicht-.md-Dateien liefert ausserhalb von SRT-Zeitcodes und teardown-Listings ausschliesslich rhotik.py:15 und :45. Keine Messdatei belegt die Herkunft. ABER die Einordnung als A ist falsch und die Schwere zu hoch: die Zahl wird nirgends als Messergebnis praesentiert, sondern durchgaengig als Schwelle ('GRENZE_HZ = 2100.0  # unterhalb = /r/ gesprochen'; config.md:19 'Grenze 2100 Hz') — also als Setzung, wie ein Grenzwert es per Definition ist. Vor allem widerlegt die Datenlage die Behauptung, sie 'entscheidet jedes einzelne Rhotik-Urteil': in den drei eingecheckten Messdateien mit Einzeltoken-Werten (rhotik_referenz.json, rhotik_probe_r1.json, rhotik_lang.json, zusammen 44 Tokens) liegt der hoechste als rhotisch gewertete f3_min bei 1968,9 Hz und der niedrigste als nicht-rhotisch gewertete bei 2112,6 Hz. Jede Schwelle im Band (1968,9 … 2112,6] Hz erzeugt exakt dieselben Urteile — 17/17, 2/17, 5/5, 0/5, 5/5, 5/5. Die 2100 liegt mitten in dieser Luecke und ist fuer kein publiziertes Urteil ausschlaggebend. Nicht pruefbar bleibt akzent_rhotik.json/screen_r2d.json, die nur Mediane und Quoten fuehren (dort Mediane 2132 und 2156 dicht ueber der Linie).

### `1328 / 1565 / 1624 / 1750 px (V05–V08) sowie 1896 / 2163 / 1967 px` — niedrig · **als Vorgabe weitergegeben**

**Wo:** `produktion/motive/README.md:111-116, 125-126, 133`  
**Wofür:** Textbreiten der noch nicht gebauten Zeilen V05–V08 und der zwei verworfenen Langfassungen; Grundlage der Aussage "kein weiterer Textfall ist offen"  

Bestaetigt. Fuer V05-V08 gibt es kein Bild und keine Messdatei; die Ableitung ist im README selbst offengelegt (Zeilen 118-122). Eigene Nachrechnung mit schrift_fuer() aus thumbnail.py und der Fontkette FreeSerifBold: bei 184 px Fontgroesse / 125 px Versalhoehe reproduzieren sich ALLE Werte exakt — 1787, 1726, 1609, 1548, 1328, 1565, 1624, 1750 sowie 1896, 2163, 1923, 1606 und DejaVuSerif-Bold @171 px = 1967 px. Die Rechnung ist also korrekt und mit dem eingecheckten Skript nachvollziehbar. Der Meldegrund bleibt bestehen und ist von mir verifiziert: produktion/videos-01-08.md:801 fuehrt denselben Wert als Messung ("`NO MORE STRESS` misst **1624 px** (Rand 148 px je Seite)", dazu "Gemessene Alternativen"), und Commit 44ac7f4 nennt die Tabelle "die gemessene Endtabelle aller acht Zeilen" — obwohl fuer V05-V08 nur gerechnet, nicht gemessen wurde. Weitergabe als Vorgabe bestaetigt (videos-01-08.md ist ausdrueckliches Vorgabedokument).

### `≥2,5 h` — mittel

**Wo:** `regeln/erfolgsregeln.md:107 und :265`  
**Wofür:** Laufzeit-Untergrenze der Regel M6 im Widerspruch zur eigenen Ueberschrift ≥3,0 h  

Keine Messdatei traegt eine 2,5-h-Schwelle (grep '2,5 h|2.5 h' ueber alle Nicht-md-Dateien: einziger Treffer ist eine Videolaenge in teardown/auswertung_population.txt, ohne Bezug). Die Zahl ist auch nicht als Messwert praesentiert, sondern ausdruecklich als Setzung ('darum konservativ ≥2,5 h', 'konservativ mit 2,5 h angesetzt') — deshalb D statt C. Der Befund selbst ist belegt: git show 909c465 zeigt, dass derselbe Commit Ueberschrift und Ankreuzzeile von 2,5 auf 3,0 h hob und die Saetze in Z.107 und Z.265 stehen liess. Korrektur zur Meldung: als_vorgabe_weitergegeben ist FALSCH — bindend ist ueberall 3,0 h (produktion/config.md:130 laufzeit_min_h = 3.0, workflow-gates.md:27, und schritt1_text.py:244 bricht unter 3,0 h ab). Die 2,5 h ist in keiner Vorgabe angekommen.

### `3,2–4,0 h` — mittel

**Wo:** `regeln/erfolgsregeln.md:100`  
**Wofür:** 'Zielband' der Laufzeit im Ankreuzkasten der Regel M6  

Ein Zielband ist eine Entscheidung, kein Messwert — insoweit regelkonform. Der doppelte Stand ist real und nachgeprueft: erfolgsregeln.md:100 sagt 3,2–4,0 h (per git show 909c465 aus dem alten '3–4 h' entstanden), waehrend die bindende Fassung 3,4–3,8 h lautet: produktion/config.md:131-132 (laufzeit_ziel_von_h = 3.4 / laufzeit_ziel_bis_h = 3.8, von schritt1_text.py, schritt5_video.py und schritt7_paket.py gelesen), workflow-gates.md:27, formel/video-formel.md:92, videos-01-08.md:32. Erschwerend: workflow-gates.md:10 fuehrt erfolgsregeln.md ausdruecklich als 'bindende Quelle', dort steht also ein zweites, abweichendes Band. Korrektur zur Meldung: als_vorgabe_weitergegeben ist FALSCH — die Pipeline liest 3,4–3,8 aus config.md; die 3,2–4,0 ist nirgends Vorgabe geworden.

### `LCM-Zyklus 1200 s` — niedrig

**Wo:** `produktion/config.md:100`  
**Wofür:** Behaupteter gemeinsamer Zyklus, wenn man den 300-s-Atem-Zoom auf den 48-s-Clip-Zyklus legt; Begruendung dafuer, den Zoom bei videoquelle = ki_clips wegzulassen.  

Nachgemessen in allen vier eingecheckten Clip-Messdateien: produktion/motive/loops/ki, ki-v02, ki-v03 und ki-v04 melden jeweils viermal dauer_s 12.042 (ki auch frames 289). Der Clip-Zyklus ist damit 48,168 s, nicht 48 s; kgV(48, 300) = 1200 ist eine Rechnung auf gerundeter Basis. Der Text kennzeichnet sie als Ableitung ("LCM-Zyklus"), produktion/motive/README.md:273 wiederholt sie - kein Fehler, aber ungenau, und die 1200 taucht in keiner Messdatei auf. Praktisch folgenlos, weil der Zoom im ki_clips-Zweig ohnehin nicht angewandt wird.

### `~46.500 Zeichen TTS je Stunde → rund 160.000–177.000 Zeichen` — niedrig

**Wo:** `formel/video-formel.md:93`  
**Wofür:** Umrechnung des Zielbands 3,4–3,8 h in ein TTS-Zeichenbudget; Planungsgröße für jeden Renderlauf  

Bestätigt und durch eine weitere Messdatei verschärft. Die Rate selbst steht in regeln/daten/stimm_stichprobe.json (Feld WPM_KORREKTUR) — formal eine eingecheckte Datei, inhaltlich aber ein fortgeschriebener Prosasatz („das TTS-Budget von ~46.500 Zeichen/Stunde bleibt gueltig"); der eigentliche Messwert „Median 46.428 Zeichen pro Stunde" existiert nur als Prosa in teardown/produktions-spec.md:160, matrix_voll.csv hat keine Zeichenspalte. Neu gefunden: produktion/korpus/plan.json ist eine eingecheckte Messdatei mit woerter/stunden/zeichen_tts je Video und widerspricht der Rate durchgehend — 154.581/3,53 h = 43.791, 151.731/3,47 h = 43.727, 162.094/3,70 h = 43.809, über alle acht Videos also rund 43.800 statt 46.500 Zeichen/h (rund 6 % Differenz). Dazu die Renderläufe: video-01/upload.md 158.256 Zeichen bei 3,58 h = 44.206/h. Die Aufrundung 3,4 h × 46.500 = 158.100 → „rund 160.000" verstärkt den Versatz. Korrektur an der Meldung: die 160.000 steht in produktion/workflow-gates.md:19 nur als Kostenangabe im Begründungstext, nicht als Grenze — als_vorgabe_weitergegeben daher false.

### `~400 selbst geschriebene Wörter` — niedrig

**Wo:** `formel/video-formel.md:139 und :329`  
**Wofür:** Umfang des eigenen Eingangsgebets je Video  

Bestätigt und breiter belegbar als gemeldet. Die 400 ist im Dokument ausdrücklich als Geschäfts-/Policy-Entscheidung ohne Datenbeleg gekennzeichnet und nach §8 verschoben (video-formel.md:30, :139, :329) — insoweit korrekt deklariert und kein Fehler. Meldepflichtig bleibt sie, weil kein einziges eigenes Gebets-Artefakt sie erfüllt: produktion/textbausteine/gebet_mind-wont-stop.txt hat 209 Wörter (wc -w), und produktion/videos-01-08.md gibt für alle acht geplanten Eingangsgebete 182 / 166 / 195 / 161 / 179 / 166 / 153 / 183 Wörter an — durchweg unter der Hälfte. Als Gate ist die 400 nirgends weitergereicht: rg „400" in workflow-gates.md, config.md und videos-01-08.md liefert keinen Gebetsbezug, sie taucht auch nirgends als Messwert wieder auf.

### `2,5 h und 3,5 h` — niedrig

**Wo:** `regeln/erfolgsregeln.md:181`  
**Wofür:** Pruefkriterium der Hypothese H1 — geplante Testbedingung  

Korrekt als Entscheidung eingeordnet: die Zahlen sind ausdruecklich als Pruefkriterium gekennzeichnet, keine Messdatei behauptet sie. Meldepflichtig bleibt der Konflikt, und er ist haerter als in der Meldung beschrieben: nicht nur workflow-gates.md Gate 1.1 verlangt ≥3,0 h, sondern produktion/config.md:130 setzt laufzeit_min_h = 3.0 und produktion/pipeline/schritt1_text.py:244 meldet jede Laufzeit darunter als 'UNTER der harten Untergrenze 3,0 h'. Das 2,5-h-Bein von H1 laesst sich mit der eigenen Pipeline nicht produzieren; die Hypothese ist so nicht pruefbar. Korrektur zur Meldung: als_vorgabe_weitergegeben ist FALSCH — die 2,5 h steht in keiner Vorgabedatei, sie kollidiert nur mit ihnen.

### `Ziel: 1` — niedrig

**Wo:** `regeln/erfolgsregeln.md:41`  
**Wofür:** Zielwert der Upload-Kadenz in der Ueberschrift der MUSS-Regel M1  

Ein Zielwert ist eine Entscheidung, keine Messung — insoweit regelkonform, und die bindende Obergrenze 2/Woche ist durch kadenz.json sauber belegt (alle 8 Verlierer 2,0–13,5). Meldepflichtig bleibt, dass die Umsetzung dem Ziel nicht folgt: produktion/videos-01-08.md:39 plant 5 Tage Abstand = 1,4 Uploads/Woche. Korrektur zur Meldung: die Behauptung, der Zielwert liege 'unter beiden Gewinner-Messwerten', stimmt nicht — kadenz.json nennt A 0,9 (unter 1) und B 1,5; das Ziel 1 liegt also zwischen den beiden gemessenen Kadenzen. als_vorgabe_weitergegeben ist FALSCH: in den Vorgabedateien steht nur die Obergrenze 2/Woche (videos-01-08.md:40), nirgends das Ziel 1.

### `38,5 s` — niedrig

**Wo:** `produktion/video-01/upload-checkliste.md:56`  
**Wofür:** Zeitpunkt, bis zu dem beide CTA abgeschlossen sein sollen  
**Messdatei:** produktion/video-01/untertitel.srt — Ende CTA 2 bei 38,280 s, Gebetsbeginn 38,920 s  

Bestaetigt als D, aber inhaltlich harmlos. Die Zahl steht in keiner Datendatei, und workflow-gates.md:36 nennt als Quelle ausdruecklich "Zeitpunkt aus der Rahmen-Wortzahl", also eine Hochrechnung. Die eingecheckte produktion/video-01/untertitel.srt deckt die Aussage aber inhaltlich: Kachel 8 (Abo-CTA, "...subscribing helps you find the next one.") endet bei 38,280 s, Kachel 9 (Eingangsgebet) beginnt bei 38,920 s. "Beide bis Sekunde 38,5" ist damit auf 0,22 s genau richtig und die Aussage "innerhalb der ersten 60 s" belegt. Schwere bleibt niedrig.

### `4 s (Vorlauf) / 3 s (Einblende)` — niedrig

**Wo:** `stimmtest/musik-prompt.md:51`  
**Wofür:** Bett laeuft 4 s allein vor der Stimme, mit 3 s Einblende  
**Messdatei:** stimmtest/qa_v2.json deckt nur die Summe 10,0 s (= VOR 4 + NACH 6); die Aufteilung selbst steht in keiner Messdatei  

Sachlich bestaetigt: die 4/6-Aufteilung steht nur als Codekonstante (mix_v2.py:27 VOR_S, NACH_S = 4.0, 6.0; final_r2.py:10), die 3 s als int(3.0*SR) in mix_v2.py:71 bzw. int(3*SR) in final_r2.py:34. In einer Messdatei steht davon nur die Summe: qa_v2.json dauer_datei_s − dauer_stimme_s = 322,9−312,9 = 316,3−306,3 = 313,5−303,5 = exakt 10,0 s. Deterministisch nachvollziehbar, aber nicht als Einzelgroessen belegt. Die Schwere ist zu entschaerfen: der gemeldete Veraltungs-Konflikt ist bereits dokumentiert, nicht still. produktion/config.md:83-85 setzt vorlauf_s = 1.5 / einblende_s = 1.5 MIT ausdruecklicher Notiz 'Deshalb 1,5 s statt der 4 s aus stimmtest/musik-prompt.md - siehe Konflikt-Notiz in der README', und produktion/workflow-gates.md:35 bindet Gate 1.9 explizit an vorlauf_s aus config.md, nicht an musik-prompt.md. Die bindende Kette laeuft also nachweislich an der veralteten Zahl vorbei.

### `−0,3 dBFS` — niedrig

**Wo:** `stimmtest/musik-prompt.md:54`  
**Wofür:** Obergrenze fuer den Gesamt-Peak des Mixes ('Reserve fuer die MP3-Kodierung')  
**Messdatei:** stimmtest/qa_v2.json peak_dbfs -0.3/-0.3/-2.6 und qa_r2.json peak_mix_dbfs decken den erreichten Wert, sind aber Rundung des 0,97-Begrenzers (mix_v2.py:80-81), keine unabhaengige Bestaetigung des Zielwerts  

Als Zielwert korrekt eingeordnet (Spaltenkopf 'Zielwert', musik-prompt.md:45), als geltende Vorgabe ueberholt: produktion/config.md:71-74 setzt peak_max_dbfs = -1.0. Gegen die Deckung durch qa_v2.json/qa_r2.json spricht ein Detail, das der Erstfund uebersieht: die dort stehenden -0.3 sind KEINE unabhaengige Messung, sondern der gerundete Begrenzer. mix_v2.py:80-81 und final_r2.py:37-38 skalieren bei Ueberschreitung auf exakt 0,97 = 20*log10(0,97) = -0,2646 dBFS -> gerundet -0,3. Der Begrenzer liegt damit sogar 0,035 dB UEBER dem eigenen Ziel 'unter -0,3 dBFS'; die Vorgabe wurde technisch nie ganz erreicht, sondern nur weggerundet. Zweiter offener Punkt, passend zur D-Meldepflicht: config.md:71 begruendet die neue Grenze mit 'Video 02 landete mit -0,13 dBFS ueber der eigenen Vorgabe von -0,3', waehrend produktion/video-02/upload.md:185 fuer denselben Render 'Peak | -0.3 dBFS' meldet — zwei Berichte, zwei Zahlen fuer einen Lauf, und die zugrunde liegende qa_mix.json liegt in produktion/arbeit/ und ist nicht eingecheckt.

### `~0,8 %` — niedrig

**Wo:** `produktion/motive/README.md:7`  
**Wofür:** Breitenverlust beim Beschnitt der 1376×768-Motive auf 16:9  

Bestaetigt als D, Meldewuerdigkeit grenzwertig. Fuer motiv-V1.png bis motiv-V4.png existiert tatsaechlich keine Messdatei (anders als fuer motiv-video-02/03/04) — auch nicht in der Historie. Der Wert ist aber reine Geometrie und im Satz selbst als Ableitung kenntlich gemacht ("Hoehe skaliert, Breite mittig auf 16:9 beschnitten"): 768 x 16/9 = 1365,3 px, Verlust (1376-1365,3)/1376 = 0,78 %. Nach der D-Regel ist das kein Fehler, und die Zahl taucht nirgends sonst als Messwert auf — sie erfuellt das Meldekriterium fuer D streng genommen nicht. Ich lasse sie der Vollstaendigkeit halber mit niedrigster Schwere stehen.

---

## Unsicher

Die Gegenprüfung konnte weder eine deckende Messdatei finden noch ausschließen,
dass es eine gibt. Im Zweifel gilt der Wert als **nicht gemessen**.

- **`nie über 2.500 Views (n=6)`** — `formel/video-formel.md:85` · Harte Untergrenze 3,0 h — kein Video unter 3 h habe je mehr als 2.500 Views erreicht
  Zwei eingecheckte Messdateien geben unterschiedliche Auskunft, deshalb kein klares Urteil. n=6 ist korrekt: unter 3 h liegen genau 6 Videos, alle von B (6.921 / 7.803 / 10.200 / 4.361 / 3.949 / 4.881 s). Das größte davon, r-2MB8lZSjQ (1,92 h), steht in regeln/daten/listings/B_RestInGrace_videos.jsonl mit dem gerundeten yt-dlp-Wert 2500 — danach ist „nie über 2.500" wörtlich richtig; in regeln/daten/nexlev/winner_details.json steht derselbe Fall mit dem exakten Wert 2567 — danach ist die Aussage um 67 Views falsch. Die Schwelle „2.500" ist also erkennbar aus dem gerundeten Listenwert abgeleitet

- **`13/13 (Text im oberen Drittel)`** — `formel/thumbnail-checkliste.md:113` · Belegzahl fuer die Pflichtvorgabe zur Textposition
  Numerisch bleibt der Fund stehen: kein eingechecktes Feld erfasst die Textposition — thumb_textmessung.json (zeilen/glyphen/hoehe/kontrast), thumb_messung.json (w/h/bytes/schaerfe) und motiv_inventar.json (16 Felder, keines zur Position) fuehren nichts dergleichen. ABER: die eingecheckte regeln/daten/thumbnail_forensik.json deckt den Sachverhalt qualitativ und traegt sogar die Fallzahl — "identisches Motiv in allen 13 Thumbs ... grosse weisse Serifen-VERSALIEN oben". Die Kombination aus "allen 13" und "oben" ist inhaltlich genau die Aussage 13/13. Das ist kein Positionsmesswert, aber deutlich 

- **`Alarm-Design n=3, bestes 142 Views`** — `formel/thumbnail-motive.md:95` · Verlierer-Bauform in der Ausschlusstabelle
  Ich habe nach einem Stellvertreterfeld gesucht und eines gefunden, das beide Zahlen exakt reproduziert: motiv_inventar.json fuehrt ein Feld farbe. Filtert man D und H auf rot-dominierte Paletten (rot-schwarz, gold-rot), ergibt sich D/4CrR1BqzZqw (rot-schwarz, 3 Views), H/YgwWhVezTYw (rot-schwarz, 142 Views), H/gold-rot (7 Views) — also n=3, bestes Ergebnis 142 Views, Vorkommen D und H. Das deckt sich Zahl fuer Zahl mit der Tabellenzeile. Eine Stilkategorie "Alarm-Design" gibt es zwar in keiner Datei, und farbe beschreibt die Gesamtpalette, nicht die Typografie — aber die Uebereinstimmung in al

- **`Esoterik-Aesthetik n=2, bestes 261 Views`** — `formel/thumbnail-motive.md:98` · Verlierer-Bauform in der Ausschlusstabelle
  Auch hier reproduziert das Feld farbe in motiv_inventar.json beide Zahlen exakt: E_QuietMind mit farbe=="bunt" ergibt genau zwei Datensaetze, UiVSFtnfK3k (BEST, 261 Views) und QhmhyX_E3B4 (WORST, 28 Views) — n=2, bestes Ergebnis 261, Vorkommen nur E. Eine Stilkategorie "Esoterik-Aesthetik" gibt es in keiner Datei, aber die Uebereinstimmung von Fallzahl, Maximum und Kanal ist vollstaendig, und thumbnail_forensik.json stuetzt den Sachverhalt qualitativ (E: "New-Age-Aesthetik: Kristalle, Glitzer, violett-tuerkise Feen-Optik"). Im Zweifel daher UNSICHER, nicht BESTAETIGT.

- **`Hook 0–21 s`** — `produktion/pipeline/README.md:73` · Ende des Hook-Blocks in der Zeitleiste von Video 01
  Teilweise gedeckt. Gemessen aus produktion/video-01/video-01.srt: erster Cue 1,500 s, letzter Hook-Cue ('Get comfortable, and let your eyes close.') endet 22,620 s, CTA 1 setzt bei 23,480 s ein. Als absolutes Intervall ist '0–21 s' an beiden Enden um rund 1,5 s falsch. Als DAUER ist die Zahl dagegen exakt gedeckt: 22,620 - 1,500 = 21,12 s, gerundet 21 s - und die 1,5 s Vorlauf sind eine bekannte, in config.md gesetzte Groesse. Da die uebrigen Angaben des Satzes absolute Endzeiten sind, bleibt die Mischform unsauber, aber die Zahl 21 selbst stammt nachweislich aus der Messung. Im Zweifel deshal

- **`exakt eingehalten (12,0 dB)`** — `produktion/pipeline/README.md:103` · Behauptung, der geforderte Pegelabstand sei im fertigen Mix exakt erreicht
  Die ZAHL ist gedeckt, die Wortwahl nicht. produktion/pipeline/qa/pegel_wiedergabe.json enthaelt abstand_mono_db = 12.0 mit mono_eingehalten = true; zusaetzlich misst schritt3_bett.py:116-200 den Abstand pro Renderlauf ueber die volle Laenge beider Signale (gemessener_abstand_db), und produktion/video-01/upload.md:192 gibt daraus 12.0 dB aus. Ein Widerspruch der Zahl gegen eine Messdatei liegt also nicht vor. Nicht gedeckt ist das unqualifizierte 'exakt eingehalten': dieselbe Messdatei weist abstand_stereo_db = 6.8, stereo_eingehalten = false und "bestanden": false aus, der Abstand haelt also n

- **`95,6 % / 95,3 % / 95,3 % / 95,6 %`** — `produktion/video-01/upload.md:190` · Sprachanteil der Renderlaeufe V01-V04, Konvention "Luecken <1 s als Sprache gezaehlt"
  Ich habe die Ersatzrechnung unabhaengig wiederholt und komme auf dieselben Zahlen (94,55 / 94,19 / 96,74 / 96,82 %). Sie widerlegt die Berichtswerte aber nicht: sprachanteil_vergleichbar_pct ist ein Huellkurvenmass auf der Tonspur (schritt2_tts.py:270-285, Luecken <1 s werden in der MASKE geschlossen), waehrend die SRT-Kacheldauern ASR-Zeiten sind, die nachweislich verrutschen (siehe Fund 8/9: Saetze mit 0,30 s Dauer). Zwei verschiedene Groessen, kein sauberer Gegenbeweis. Was bleibt und das schwerste an diesem Posten ist: die vier Zahlen sind durch keine eingecheckte Messdatei pruefbar (qa_st

- **`30 Minuten`** — `stimmtest/README.md:3` · Umfang des Blindtest-Materials je Stimme
  Der Zahlenbefund stimmt: keine eingecheckte Datei nennt 30 Minuten; qa_bericht.json und qa.log fuehren 29,0 / 25,3 / 28,4 min (1741,9 / 1519,0 / 1702,8 s). Auch der Commit-Betreff 6cf9f8e traegt die 30. Gegen die Einordnung als Widerspruch spricht aber, dass der Satz den TESTUMFANG benennt, nicht ein Messergebnis: derselbe README nennt zwei Absaetze weiter die praezise Grundlage ('Zielmenge von 4.000-4.500 Woertern ... jetzt 4.237'), und stimmtest/generate.log bestaetigt '4,237 Woerter, 22,084 Zeichen'. Ein Text ergibt je Stimme eine andere Dauer — eine einzelne 'gemessene' Zahl wird gar nicht

- **`3,27 (Clip 1→2) und 3,46 (Clip 4→1)`** — `produktion/motive/README.md:316-317` · Angeblich gemessene Nahtsprünge an den zwei gesichteten Uebergaengen der V02-Kette
  EINORDNUNG KORRIGIERT: C -> B, Urteil UNSICHER. Der Vorpruefer schreibt, der Bericht gebe "keine abweichende Messbasis" an — das trifft nicht zu. Der Satz lautet "Nahtsichtung an kette-3min.mp4 (16 Uebergaenge, Produktionsqualitaet, 192,7 s): ... Gemessen an den beiden geprueften Naehten 3,27 und 3,46". Die 2,566/2,520 aus der JSON sind rohe Frame-Differenzen zwischen den QUELLCLIPS, die 3,27/3,46 sind an der neu kodierten Kette gemessen. Genau diesen Versatz dokumentiert das Repo an anderer Stelle selbst: im Loop-Abschnitt liegt der rohe Wrap-Schritt bei 0,0016-0,0094, der DEKODIERTE Nahtspru

---

## Widerlegt

59 Verdachtsfälle sind in der Gegenprüfung gefallen — eine eingecheckte
Messdatei deckt den Wert doch, oft unter einem anderen Namen als vermutet. Sie
stehen hier, damit sie nicht ein zweites Mal geprüft werden.

| Wert | Fundstelle | gedeckt durch |
|---|---|---|
| `Median 201–237 KB bei 1280x720` | `formel/thumbnail-checkliste.md:21` | regeln/daten/thumb_messung.json — Gruppenmediane 237,2 / 233,0 / 201,2 KiB |
| `11,5 % / 125 px` | `formel/thumbnail-checkliste.md:37 und :109` | produktion/video-01/thumbnail-a_messung.json, -b, video-02/03/04/thumbnail_messung.json (versalhoehe_px 125, versalhoehe_pct 11.57); produktion/mot… |
| `8 von 8 per Audio geprüften Stimmen männlich` | `formel/video-formel.md:256-257` | regeln/daten/stimm_geschlecht.json, A3_vergleich.maennlich_per_audio_verifiziert.faelle — acht namentlich aufgeführte, alle männlich; dieselbe Date… |
| `Gewinner 1,3–1,5 Uploads/Woche` | `formel/video-formel.md:291-292` | regeln/daten/nexlev/winner_details.json (publishDate aller 8 A-Videos) für die 1,3; regeln/daten/kadenz.json (B_RestInGrace.uploads_pro_woche = 1.5… |
| `856.688 Shorts-Views` | `formel/video-formel.md:292-293` | regeln/daten/listings/J_JesusLovesYou_shorts.jsonl — Summe der view_count über alle 22 Zeilen = exakt 856.688 |
| `Revelation 1,5× (n=12)` | `formel/video-formel.md:381` | teardown/teardown_batch_20260802_090410/*_videos.jsonl — 12 Treffer mit Median 20.000 Views gegen den globalen Median 13.500 aller 454 Videos = 1,4… |
| `Jeremiah 1,17× (n=4)` | `formel/video-formel.md:382` | teardown/teardown_batch_20260802_090410/*_videos.jsonl — 4 Treffer (6.300, 6.500, 25.000, 296.000), Median 15.750 gegen globalen Median 13.500 = 1,… |
| `Genesis 0,43× (n=13)` | `formel/video-formel.md:382` | teardown/teardown_batch_20260802_090410/*_videos.jsonl — 13 Treffer, Median 5.800 Views gegen globalen Median 13.500 = 0,4296× |
| `Faktor 297` | `formel/video-formel.md:88` | regeln/daten/listings/B_RestInGrace_videos.jsonl — 7 Videos ≥3 h, max 166.000 / min 559 Views = exakt 297,0 |
| `23 Semikolon-Verse` | `produktion/config.md:59` | produktion/korpus/satzlaengen.json (Eintrag V2: laengster_satz_zeichen 1827, herkunft "psalms 136", anfang "Give thanks to the Lord of lords, for h… |
| `40–93 Marken (bei Kanal B)` | `produktion/pipeline/README.md:122` | regeln/daten/nexlev/winner_details.json, Feld chapters, 11 B-Videos: 40-93 |
| `3,58 h` | `produktion/pipeline/README.md:88` | produktion/video-01/video-01.srt (12.890,146 s) + config.md nachlauf_s 6.0 = 3,582 h |
| `140,4 WPM` | `produktion/pipeline/README.md:89` | produktion/video-01/video-01.srt: 30.155 Woerter / 12.890,146 s = 140,4 WPM |
| `0,0016 · 0,0998 · "60-mal größer"` | `produktion/pipeline/README.md:90` | produktion/klang/bett_pad_feuer.flac, verankert durch produktion/pipeline/qa/pegel_wiedergabe.json (bett_dauer_s 56.0, bett_rms_roh_mono_dbfs -31.198) |
| `546 Millionen Samples` | `produktion/pipeline/gemeinsam.py:101` | gemeinsam.py:18 SR=44100 + pegel_wiedergabe.json bett_samplerate 44100 + Laufzeiten aus produktion/video-0*/video-0*.srt |
| `weit über tausendmal` | `produktion/pipeline/loop_animation.py:6-7` | produktion/motive/loops/ki*/qa-ki-clips.json dauer_s = 12.042 -> 12.600 s / 12,042 = 1.046 Durchlaeufe |
| `2269,0 Hz und 1638,0 Hz` | `produktion/pipeline/rhotik.py:21-22; produktion/config.md:30-32` | stimmtest/akzent_rhotik.json (2269.0 / 1638.0 woertlich); Gegenprobe produktion/pipeline/qa/rhotik_referenz.json (2268,4 / 1634,7, aus den Einzelto… |
| `2-3 dB (3-s-Ausschnitt gegen Mittel der 56-s-Schleife)` | `produktion/pipeline/schritt3_bett.py:119-120` | produktion/klang/bett_pad_feuer.flac; Ankerwerte in produktion/pipeline/qa/pegel_wiedergabe.json (bett_dauer_s 56.0, bett_rms_roh_mono_dbfs -31.198) |
| `0 von 19 (Untertitelspur)` | `produktion/pipeline/schritt6_srt.py:5` | regeln/daten/nexlev/winner_details.json, Feld hasCaption: 19x False |
| `2,52 GB` | `produktion/video-01/upload-checkliste.md:39` | Commit e27e58d (Nachricht: "V1 damit neu montiert: 3:34:57, 2,52 GB") · produktion/motive/README.md:262-266 · produktion/motive/loops/ki/kette-3min… |
| `12,0 dB` | `produktion/video-01/upload-checkliste.md:52` | produktion/pipeline/qa/pegel_wiedergabe.json — abstand_mono_db 12.0 (Mono-Wiedergabefall haelt); Stereobefund separat in workflow-gates.md dokument… |
| `6 von 11` | `produktion/video-01/upload-checkliste.md:71` | teardown/produktions-spec.md:214, :216, :257 — "6 der 11 Stichproben" (Prosa, aber mit namentlich genannten Faellen) |
| `≥97.0 %` | `produktion/video-01/upload.md:190` | teardown/teardown_batch_20260802_090410/matrix_voll.csv (24 Zeilen, sprech_anteil_pct 97,3-100,0) · git show e59ff94:produktion/config.md:107 |
| `1.42 s / 1.44 s` | `produktion/video-01/upload.md:191` | produktion/pipeline/schritt6_srt.py — SRT-Zeiten sind ASR-/Interpolationszeiten, keine Tonpausen |
| `<-0,3 dBFS` | `produktion/video-01/upload.md:193` | git show e59ff94:produktion/config.md:69 — peak_max_dbfs = -0.3 zum Renderzeitpunkt |
| `1.38 s` | `produktion/video-02/upload.md:183` | produktion/pipeline/schritt6_srt.py (Zeiten aus ASR, Luecken linear interpoliert) — die SRT ist keine Pausenmessung |
| `-0.3 dBFS` | `produktion/video-02/upload.md:185` | produktion/pipeline/schritt3_bett.py:177-181 (Normalisierung auf peak_max_dbfs) · git show a4fef38:produktion/config.md (peak_max_dbfs = -0.3 zum R… |
| `44` | `produktion/video-03/upload.md:110` | produktion/video-03/beschreibung.txt — 44 Zeitmarkenzeilen, selbst nachgezaehlt |
| `-1.0 dBFS` | `produktion/video-03/upload.md:136` | produktion/pipeline/schritt3_bett.py:177-181 · config.md:74 (Grenze galt bereits beim V03-Render) |
| `8/8` | `produktion/videos-01-08.md:388-389` | regeln/daten/motiv_inventar.json - A: tageszeit=nacht 8/8, Jesus im Bild 8/8, blickkontakt 0/8 |
| `13 von 13` | `produktion/videos-01-08.md:69` | regeln/daten/thumbnail_forensik.json, Feld gewinner_muster.B_RestInGrace: "EXTREM konsistente Serie: identisches Motiv in allen 13 Thumbs"; zusaetz… |
| `4/10` | `produktion/videos-01-08.md:73-74` | regeln/daten/motiv_inventar.json - unter den 10 Treffern jsit=3 + jr=1 = 4; visuell bestaetigt durch regeln/daten/thumbs/A_HushLittleLamb__GEW__UV1… |
| `6 von 13` | `produktion/videos-01-08.md:808-809` | regeln/daten/nexlev/katalog_B_RestInGrace.json - 6 von 13 Titeln tragen die Serienformel "Sleep To These ..." |
| `97-100 %` | `produktion/videos-01-08.md:93` | teardown/teardown_batch_20260802_090410/matrix_voll.csv, Spalte sprech_anteil_pct: n=24, Werte 97,3 bis 100,0 % |
| `Sekunde 0-3` | `produktion/videos-01-08.md:93` | produktion/config.md:142 sprachstart_max_s = 3.0; formel/video-formel.md:98 fuehrt "Sprache beginnt in Sekunde 0-3" als PFLICHT |
| `alle 10 Treffer ≥ 3,2 h` | `produktion/workflow-gates.md:27` | regeln/daten/listings/A_HushLittleLamb_videos.jsonl und B_RestInGrace_videos.jsonl — 10 Treffer >30.000 Views, alle zwischen 3,4425 h und 5,0236 h,… |
| `13 belegte Anker` | `produktion/workflow-gates.md:29` | formel/video-formel.md §10 (Tabelle mit genau 13 Ankern) gegen produktion/gewinner_titel.json (21 Gewinner-Titel) — alle 13 Anker sind Anfaenge dor… |
| `die 7 abgeleiteten` | `produktion/workflow-gates.md:29` | formel/video-formel.md §10, Block 'Ungeprüft — abgeleitet, ohne Beleg (7)' — genau sieben Eintraege, ausdruecklich als unbelegt markiert |
| `≥ 11,5 % der Bildhöhe (≥ 125 px bei 1080p)` | `produktion/workflow-gates.md:31` | produktion/pipeline/thumbnail.py:35+77 (CAP_MIN_PCT 11.5 → cap_ziel = ceil(1080*11,5/100) = 125); produktion/motive/text_messung.json Feld 'soll'; … |
| `13/13` | `produktion/workflow-gates.md:33` | regeln/daten/motiv_inventar.json (B n=13: lamm/feuer/gesicht/warmlicht/text je 13/13, blickkontakt 0 in 13/13); formel/thumbnail-motive.md:130 und … |
| `n=24` | `produktion/workflow-gates.md:35` | teardown/teardown_batch_20260802_090410/matrix_voll.csv (24 Datenzeilen) fuer n=24; regeln/daten/skript_anatomie.json (4 GEWINNER, sprechbeginn_s 3… |
| `Gewinner 0,1–3,1 s` | `produktion/workflow-gates.md:35` | regeln/daten/skript_anatomie.json — vier GEWINNER-Eintraege mit sprechbeginn_s 3.1 / 2.4 / 2.1 / 0.1 |
| `Die vier gerenderten Videos 01–04 sind betroffen` | `produktion/workflow-gates.md:61` | produktion/config.md:81 (bett_datei als einziger Kanalwert) und produktion/pipeline/qa/pegel_wiedergabe.json (bett_datei, bett_dauer_s 56.0, downmi… |
| `Bei 3,5 h Laufzeit` | `produktion/workflow-gates.md:93` | produktion/korpus/plan.json + produktion/korpus/kapitel.json (V1–V8: 3,33–3,55 h bei config-eigenem wpm_erwartet 145,9; 3,47–3,70 h bei 140 WPM) so… |
| `0,7–3,8 h` | `regeln/erfolgsregeln.md:105` | regeln/daten/start_confounder.json (J: 'Musik-Video, dann Langform') + regeln/daten/nexlev/katalog_J_JesusLovesYou.json (4 Langform-Videos 2.579–13… |
| `täglich` | `regeln/erfolgsregeln.md:126` | regeln/daten/start_confounder.json ('dann TAEGLICH ~1.0h-Videos') + regeln/daten/nexlev/katalog_F_GodsPeacefulSleep.json (Uploaddaten 21.07.–01.08.) |
| `Ø 16 Views bei 33 Uploads` | `regeln/erfolgsregeln.md:146` | regeln/daten/nexlev/katalog_D_GodMessageToday.json (Ø 16,2 Langform) + regeln/daten/kadenz.json (D gesamt 33) |
| `788/140/304/660/1.800/2.500` | `regeln/erfolgsregeln.md:156` | regeln/daten/nexlev/katalog_B_RestInGrace.json (Eintraege 1–6: 788/140/304/660/1800/2500, Eintrag 7: 166000) |
| `141–163 WPM` | `regeln/erfolgsregeln.md:165` | regeln/daten/skript_anatomie.json (label-Feld: J = SONDERFALL, die 6 VERLIERER-Eintraege ergeben 141–163 WPM) |
| `6 Monate` | `regeln/erfolgsregeln.md:168` | regeln/daten/start_confounder.json (confounder.kanalalter) + regeln/daten/nexlev/about_A_HushLittleLamb.json (joinedDate 2025-11-08) |
| `16` | `regeln/erfolgsregeln.md:23` | regeln/daten/nexlev/katalog_D_GodMessageToday.json (19 Videos, Summe 308, davon 2 explizit views = 0) |
| `1,3/Woche` | `regeln/erfolgsregeln.md:43` | regeln/daten/nexlev/winner_details.json (publishDate aller 8 A-Videos: 2026-05-08 bis 2026-06-21) |
| `1,4/Woche` | `regeln/erfolgsregeln.md:44` | regeln/daten/nexlev/winner_details.json + katalog_B_RestInGrace.json (13 Uploaddaten 2026-05-31 bis 2026-08-02) |
| `5/8` | `regeln/erfolgsregeln.md:62` | regeln/daten/thumbnail_forensik.json (systematik: '3 Verlierer (C, F, I) haben ordentliche bis gute Thumbs' bei 8 dokumentierten Verlierern) |
| `9 von 10` | `regeln/erfolgsregeln.md:69` | regeln/daten/listings/*_videos.jsonl (Titel + view_count) und regeln/daten/stimm_geschlecht.json:148 (10/21) |
| `1 von 21 / 0 von 13` | `regeln/erfolgsregeln.md:70` | regeln/daten/listings/A_HushLittleLamb_videos.jsonl + B_RestInGrace_videos.jsonl (alle 21 Titel im Klartext) |
| `−31 dBFS RMS` | `stimmtest/musik-prompt.md:47` | produktion/pipeline/qa/pegel_wiedergabe.json: bett_rms_roh_mono_dbfs −31.198 (echte Messung), bett_mono_dbfs −31.0; eigene Nachrechnung an produkti… |
| `−19 dBFS RMS` | `stimmtest/musik-prompt.md:48` | keine Messdatei deckt −19 als Messwert; die Einordnung als Zielwert ist jedoch durch musik-prompt.md:45 (Spaltenkopf 'Zielwert') und produktion/pip… |
| `0,00017` | `stimmtest/musik-prompt.md:67` | produktion/klang/bett_pad_feuer.flac (eigene Nachrechnung: Monosumme-Naht 0,00016785; Kanal L 0,00128 / R 0,00162; max. Innensprung L 0,09976) sowi… |

