#!/usr/bin/env python3
"""
gen_par.py - parallele Variante von generate.py.

Gleiche Chunks (chunks.json), gleiche Satzgrenzen, gleiche Retry-Logik -
nur mit Thread-Pool statt seriell. Bereits vollstaendig vorhandene WAVs
werden uebersprungen, teilweise geschriebene Dateien koennen nicht
entstehen (Schreiben nach .part, dann atomares os.replace).
"""
import json, os, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

KEY = os.environ["FISH_KEY"]
MODEL = "s2.1-pro-free"
EP = "https://api.fish.audio/v1/tts"
CHUNKS = json.load(open("chunks.json"))
STIMMEN = [
    {"key": "milo",  "id": "cb6381fb822345bd89c207fb49551d24", "speed": 0.88},
    {"key": "medit", "id": "8d797adca9af48ca9e8a1c7284db1d6c", "speed": 1.0},
    {"key": "calm",  "id": "d012487fa0824e5eb235f983d21eccac", "speed": 1.0},
]


def job(a):
    key, vid, speed, i, text = a
    p = f"chunks/{key}/{i:03d}.wav"
    if os.path.exists(p) and os.path.getsize(p) > 2000:
        return (key, i, "skip")
    body = {"text": text, "reference_id": vid, "format": "wav",
            "sample_rate": 44100, "normalize": True}
    if speed != 1.0:
        body["prosody"] = {"speed": speed}
    data = json.dumps(body).encode()
    for a_ in range(5):
        try:
            r = urllib.request.Request(EP, data=data, headers={
                "Authorization": f"Bearer {KEY}",
                "Content-Type": "application/json", "model": MODEL})
            with urllib.request.urlopen(r, timeout=300) as f:
                out = f.read()
            if out[:1] == b"{":
                raise RuntimeError(out[:150].decode("utf-8", "replace"))
            if len(out) < 2000:
                raise RuntimeError(f"zu klein {len(out)}")
            tmp = p + ".part"
            open(tmp, "wb").write(out)
            os.replace(tmp, p)
            return (key, i, "ok")
        except Exception as e:
            if a_ == 4:
                return (key, i, f"FEHLER {e}")
            time.sleep(2 ** a_)


def main():
    jobs = []
    for st in STIMMEN:
        os.makedirs(f"chunks/{st['key']}", exist_ok=True)
        for i, c in enumerate(CHUNKS):
            jobs.append((st["key"], st["id"], st["speed"], i, c))
    n = 0
    with ThreadPoolExecutor(max_workers=9) as ex:
        for key, i, s in ex.map(job, jobs):
            n += 1
            print(f"[{n}/{len(jobs)}] {key} chunk {i} -> {s}", flush=True)
    print("FERTIG")


if __name__ == "__main__":
    main()
