#!/usr/bin/env python3
"""
mix_v2.py - fuegt die v2-Chunks zusammen und mischt das Musikbett darunter.

Pegelverhaeltnis nach dem gemessenen Befund: in 6 von 6 vermessenen
Konkurrenzvideos sitzt die Stimme klar ueber dem Bett. Umgesetzt als
12 dB Abstand (Stimme -19 dBFS RMS, Bett -31 dBFS RMS), gemessen ueber
die Sprachabschnitte, nicht ueber die Pausen.

Das Bett laeuft durchgehend und wird NICHT gaduckt: bei den Gewinnern
ist kein Ducking hoerbar, und ein atmendes Bett zieht Aufmerksamkeit.
"""
import json, os, subprocess
import numpy as np
import soundfile as sf

SR = 44100
STIMMEN = [
    {"key": "v2a", "name": "Dramatic Whisper Male",    "id": "b879fcec88c542b78d2eb4462e4d4c59", "speed": 0.64},
    {"key": "v2b", "name": "Henry (British Narrator)", "id": "55f0cafef00f4e16808bcd75c4b41a6f", "speed": 0.75},
    {"key": "v2c", "name": "Calm Meditation Voice",    "id": "14c13e72d4644b0dbd2f147df20f6d80", "speed": 0.92},
]
C = json.load(open("chunks_v2.json"))
WOERTER = len(open("text_5min.txt").read().split())
VOICE_DB = -19.0
BETT_DB = -31.0
VOR_S, NACH_S = 4.0, 6.0     # Bett laeuft vor und nach der Stimme weiter


def rms_db(x):
    return 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12)


def sprach_rms_db(x, sr):
    """RMS nur ueber die Sprachabschnitte - Pausen wuerden den Wert verfaelschen."""
    w = int(0.02 * sr)
    env = np.convolve(np.abs(x), np.ones(w) / w, mode="same")
    m = env > (0.15 * np.percentile(env, 95))
    return rms_db(x[m]) if m.sum() > sr else rms_db(x)


def fuegen(key):
    teile, grenzen, pos = [], [], 0
    for i in range(len(C)):
        y, s = sf.read(f"chunks/{key}/{i:03d}.wav", dtype="float32", always_2d=True)
        y = y.mean(axis=1)
        assert s == SR
        if i > 0:
            grenzen.append(pos / SR)
        teile.append(y)
        pos += len(y)
    return np.concatenate(teile), grenzen


def main():
    os.makedirs("out_v2", exist_ok=True)
    bett_src, _ = sf.read("musik/bett_pad_feuer.wav", dtype="float32", always_2d=True)
    bericht = {}
    for st in STIMMEN:
        v, grenzen = fuegen(st["key"])
        dauer = len(v) / SR
        wpm = WOERTER / (dauer / 60)
        # Stimme auf Zielpegel (ueber Sprachabschnitte gemessen)
        v = v * (10 ** (VOICE_DB / 20) / 10 ** (sprach_rms_db(v, SR) / 20))

        ges = int((dauer + VOR_S + NACH_S) * SR)
        # Bett auf Laenge bringen
        b = np.tile(bett_src, (int(ges / len(bett_src)) + 2, 1))[:ges]
        b = b * (10 ** (BETT_DB / 20) / 10 ** (rms_db(b.mean(axis=1)) / 20))
        # Ein- und Ausblende des Betts
        f = int(3.0 * SR)
        b[:f] *= np.linspace(0, 1, f)[:, None]
        b[-f:] *= np.linspace(1, 0, f)[:, None]

        mix = b.copy()
        o = int(VOR_S * SR)
        mix[o:o + len(v), 0] += v
        mix[o:o + len(v), 1] += v
        sp = float(np.abs(mix).max())
        if sp > 0.97:
            mix *= 0.97 / sp
        sf.write(f"out_v2/_{st['key']}.wav", mix, SR)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"out_v2/_{st['key']}.wav",
                        "-codec:a", "libmp3lame", "-b:a", "192k", "-map_metadata", "-1",
                        f"out_v2/_{st['key']}.mp3"], check=True)

        abstand = sprach_rms_db(v, SR) - rms_db(b.mean(axis=1))
        bericht[st["key"]] = {
            "name": st["name"], "id": st["id"], "speed": st["speed"],
            "dauer_stimme_s": round(dauer, 1), "dauer_datei_s": round(ges / SR, 1),
            "wpm": round(wpm, 1), "stimme_ueber_bett_db": round(float(abstand), 1),
            "peak_dbfs": round(float(20 * np.log10(np.abs(mix).max())), 1),
            "naehte": [round(g + VOR_S, 2) for g in grenzen],
        }
        print(f"{st['name']:26s} {dauer/60:.2f} min Stimme, {wpm:6.1f} WPM, "
              f"Stimme {abstand:.1f} dB ueber dem Bett", flush=True)
    json.dump(bericht, open("qa_v2.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
