# Offene Punkte

Aufgefallen, nicht bearbeitet. Eine Zeile je Punkt.

- 2026-09-02 · `v07_v08_moeglichkeiten.json/laufzeit_h` sind Korpusstunden (`W/WPM/60`, die von Prüfung 1.1 gatende Größe), die Zeile „Videolaufzeit" in `korpus_pruefung.py` ist `_video_h()` mit Rahmen und Ansagen — rund 0,04 h mehr; acht der 47 Korpora liegen je nach Größe innerhalb oder außerhalb des Bandes 3,4–3,8 h.
- 2026-09-02 · `FISH_KEY` ist in dieser Umgebung nicht gesetzt; Pipeline-Schritt 2 (TTS) bricht hart ab. V07 ist bis Schritt 1 gebaut (`produktion/arbeit/video-07/skript.json`, 159.859 TTS-Zeichen), Motiv, Thumbnail und KI-Clips liegen vor — Mischung, Video, SRT, Rendermessdatei und GoFile fehlen.
- 2026-09-02 · Erster V07-Clipsatz kam als 720p mit Tonspur, weil `resolution` und `generate_audio` nicht gesetzt waren (Vorgabe: 1080p, `generate_audio: false`). Neu erzeugt — der erste Satz ist bezahlt und verworfen. Für den nächsten Lauf: beide Parameter gehören in den Skill-Abschnitt „KI-Clips erzeugen", dort stehen sie bisher nur als Fließtext.
- 2026-09-02 · Aussprache-QA für V07 steht aus: der Korpus bringt rund 300 im Kanal noch nie gesprochene Eigennamen mit (Ahithophel, Mephibosheth, Ishbosheth, Barzillai, Jehoshaphat, Tahchemonite, Jerubbesheth …). Nach dem Render sind sie 159.859 TTS-Zeichen teuer.
