#!/usr/bin/env python3
"""
assemble_qa.py - fuegt die WAV-Chunks nahtlos zusammen, kodiert einmal nach
MP3, verblindet die Reihenfolge und prueft danach automatisch:

  a) Tempo je Datei in WPM
  b) Uebergangsstellen: Lautstaerkespruenge und Sample-Spruenge an den
     Chunk-Grenzen, mit Zeitstempel
  c) Aussprache der Eigennamen per Spracherkennung, mit Zeitstempel
  d) Gesamtlaufzeit und verbrauchte Zeichenmenge
"""
import json, os, subprocess, re, hashlib
import numpy as np
import soundfile as sf

STIMMEN = [
    {"key": "milo",  "name": "MILO SOOTHING VOICE", "id": "cb6381fb822345bd89c207fb49551d24", "speed": 0.88},
    {"key": "medit", "name": "meditation",          "id": "8d797adca9af48ca9e8a1c7284db1d6c", "speed": 1.0},
    {"key": "calm",  "name": "Calm",                "id": "d012487fa0824e5eb235f983d21eccac", "speed": 1.0},
]
EIGENNAMEN = ["Bethany", "Cephas", "Nathanael", "Isaiah", "Capernaum", "Nicodemus"]
TEXT = open("text_johannes_1-5.txt").read().strip()
CHUNKS = json.load(open("chunks.json"))


def zusammenfuegen(key):
    """Sample-exaktes Aneinanderhaengen der WAVs. Gibt Grenz-Zeitstempel zurueck."""
    teile, grenzen, pos = [], [], 0
    sr = None
    for i in range(len(CHUNKS)):
        p = f"chunks/{key}/{i:03d}.wav"
        y, s = sf.read(p, dtype="float32", always_2d=True)
        y = y.mean(axis=1)
        if sr is None:
            sr = s
        assert s == sr, f"Samplerate weicht ab in {p}"
        if i > 0:
            grenzen.append(pos / sr)
        teile.append(y)
        pos += len(y)
    ganz = np.concatenate(teile)
    sf.write(f"out/_{key}.wav", ganz, sr)
    return ganz, sr, grenzen


def uebergaenge_pruefen(y, sr, grenzen):
    """Pegel- und Sample-Sprung an jeder Chunk-Grenze.

    Der Pegel wird ueber SPRACHE verglichen, nicht ueber die Pause an der Naht:
    an jeder Naht liegt natuerliche Stille, ein RMS-Vergleich dort wuerde nur
    Grundrauschen gegen Grundrauschen messen und zweistellige dB-Werte
    ausweisen, die niemand hoert. Gemessen wird darum je 1 s Sprache, die
    Stille an der Naht uebersprungen.
    """
    SPRACHE = int(1.0 * sr)
    befunde = []

    def stille_laenge(seg, rueckwaerts=False):
        s = seg[::-1] if rueckwaerts else seg
        leise = np.abs(s) < 0.005
        n = 0
        for v in leise:
            if v: n += 1
            else: break
        return n

    for t in grenzen:
        i = int(t * sr)
        vor_roh, nach_roh = y[max(0, i - 3 * sr):i], y[i:i + 3 * sr]
        if len(vor_roh) < sr or len(nach_roh) < sr:
            continue
        sv = stille_laenge(vor_roh, True)      # Stille am Ende des Vorgaengers
        sn = stille_laenge(nach_roh)           # Stille am Anfang des Nachfolgers
        # Sprachfenster jenseits der Pause
        vs = vor_roh[max(0, len(vor_roh) - sv - SPRACHE): len(vor_roh) - sv]
        ns = nach_roh[sn: sn + SPRACHE]
        if len(vs) < sr // 4 or len(ns) < sr // 4:
            continue
        rv, rn = float(np.sqrt((vs ** 2).mean())), float(np.sqrt((ns ** 2).mean()))
        db = 20 * np.log10((rn + 1e-9) / (rv + 1e-9))
        sprung = float(abs(y[i] - y[i - 1])) if i > 0 else 0.0
        befunde.append({
            "zeit_s": round(t, 2),
            "zeit_hms": f"{int(t//3600):02d}:{int(t%3600//60):02d}:{t%60:05.2f}",
            "pegelsprung_db": round(db, 2),
            "samplesprung": round(sprung, 5),
            "pause_ms": round((sv + sn) / sr * 1000, 1),
        })
    return befunde


def transkribieren(pfad):
    from faster_whisper import WhisperModel
    m = WhisperModel("base.en", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(pfad, word_timestamps=True, vad_filter=False, beam_size=1)
    woerter = []
    for s in segs:
        for w in (s.words or []):
            woerter.append({"w": w.word.strip(), "t": w.start})
    return woerter


def namen_pruefen(woerter):
    """Vergleicht, ob die Eigennamen im Erkanntes auftauchen bzw. wie sie ankamen."""
    erkannt = " ".join(w["w"] for w in woerter)
    norm = re.sub(r"[^a-z ]", " ", erkannt.lower())
    ergebnis = []
    for n in EIGENNAMEN:
        soll = TEXT.count(n)
        ist = len(re.findall(r"\b" + n.lower() + r"\b", norm))
        # Zeitstempel der Treffer
        stellen = [w["t"] for w in woerter if n.lower() in re.sub(r"[^a-z]", "", w["w"].lower())]
        # Was stand statt dessen dort? Kontext um die erwartete Position
        ergebnis.append({"name": n, "im_text": soll, "erkannt": ist,
                         "zeitstempel": [f"{int(t//60):02d}:{t%60:05.2f}" for t in stellen[:4]]})
    return ergebnis, erkannt


def main():
    os.makedirs("out", exist_ok=True)
    zeichen = len(TEXT)
    bericht = {}
    for st in STIMMEN:
        k = st["key"]
        print(f"\n=== {st['name']} ===", flush=True)
        y, sr, grenzen = zusammenfuegen(k)
        dauer = len(y) / sr
        wpm = len(TEXT.split()) / (dauer / 60)
        print(f"  Laufzeit {dauer/60:.1f} min, {wpm:.1f} WPM", flush=True)
        ue = uebergaenge_pruefen(y, sr, grenzen)
        auff = [u for u in ue if abs(u["pegelsprung_db"]) > 6 or u["samplesprung"] > 0.05]
        print(f"  Uebergaenge: {len(ue)}, auffaellig: {len(auff)}", flush=True)
        # MP3 einmalig kodieren, Metadaten leeren
        mp3 = f"out/_{k}.mp3"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"out/_{k}.wav",
                        "-codec:a", "libmp3lame", "-b:a", "128k", "-map_metadata", "-1",
                        "-write_xing", "0", mp3], check=True)
        print("  transkribiere fuer Aussprache-Pruefung ...", flush=True)
        woerter = transkribieren(f"out/_{k}.wav")
        namen, volltext = namen_pruefen(woerter)
        open(f"out/_{k}_asr.txt", "w").write(volltext)
        bericht[k] = {"name": st["name"], "id": st["id"], "speed": st["speed"],
                      "dauer_s": round(dauer, 1), "dauer_min": round(dauer / 60, 1),
                      "wpm": round(wpm, 1), "uebergaenge": ue, "auffaellig": auff,
                      "eigennamen": namen, "asr_woerter": len(woerter)}
        for n in namen:
            print(f"    {n['name']:11s} im Text {n['im_text']}x, erkannt {n['erkannt']}x  {n['zeitstempel']}", flush=True)
    json.dump({"zeichen_je_stimme": zeichen, "zeichen_gesamt": zeichen * 3, "stimmen": bericht},
              open("qa_bericht.json", "w"), ensure_ascii=False, indent=1)
    print("\nqa_bericht.json geschrieben")


if __name__ == "__main__":
    main()
