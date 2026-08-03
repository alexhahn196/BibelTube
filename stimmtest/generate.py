#!/usr/bin/env python3
"""
generate.py - Fish Audio S2.1 Pro (free tier) TTS fuer den Stimmtest.

Chunking IMMER an Satzenden, nie mitten im Satz. Chunks werden als WAV
geholt (verlustfrei), sample-exakt aneinandergehaengt und erst am Ende
EINMAL nach MP3 kodiert - so entstehen keine Encoder-Luecken oder Knackser
an den Uebergaengen.

Aufruf: FISH_KEY=... python3 generate.py
"""
import json, os, re, subprocess, sys, time, urllib.request, urllib.error

KEY = os.environ["FISH_KEY"]
MODEL = "s2.1-pro-free"
ENDPOINT = "https://api.fish.audio/v1/tts"
MAX_CHARS = 1800          # konservativ unter dem Timeout-Risiko langer Requests
TEXT = open("text_johannes_1-5.txt").read().strip()

STIMMEN = [
    {"key": "milo",  "name": "MILO SOOTHING VOICE",
     "id": "cb6381fb822345bd89c207fb49551d24", "speed": 0.88},
    {"key": "medit", "name": "meditation",
     "id": "8d797adca9af48ca9e8a1c7284db1d6c", "speed": 1.0},
    {"key": "calm",  "name": "Calm",
     "id": "d012487fa0824e5eb235f983d21eccac", "speed": 1.0},
]


def satz_chunks(text, maxlen):
    """Teilt an Satzenden. Ein Satz wird nie zerschnitten."""
    saetze = re.findall(r'[^.!?]*[.!?]+["”’\')\]]*\s*', text)
    rest = text[sum(len(s) for s in saetze):]
    if rest.strip():
        saetze.append(rest)
    chunks, akt = [], ""
    for s in saetze:
        if akt and len(akt) + len(s) > maxlen:
            chunks.append(akt.strip())
            akt = s
        else:
            akt += s
    if akt.strip():
        chunks.append(akt.strip())
    return chunks


def tts(text, vid, speed, ziel, versuche=5):
    body = {"text": text, "reference_id": vid, "format": "wav",
            "sample_rate": 44100, "normalize": True}
    if speed != 1.0:
        body["prosody"] = {"speed": speed}
    data = json.dumps(body).encode()
    for a in range(versuche):
        try:
            req = urllib.request.Request(
                ENDPOINT, data=data,
                headers={"Authorization": f"Bearer {KEY}",
                         "Content-Type": "application/json", "model": MODEL})
            with urllib.request.urlopen(req, timeout=300) as f:
                out = f.read()
            if out[:1] == b"{":
                raise RuntimeError(out[:200].decode("utf-8", "replace"))
            if len(out) < 2000:
                raise RuntimeError(f"zu klein: {len(out)} bytes")
            open(ziel, "wb").write(out)
            return True
        except Exception as e:
            if a == versuche - 1:
                print(f"      FEHLGESCHLAGEN: {e}")
                return False
            time.sleep(2 ** a)
    return False


def main():
    chunks = satz_chunks(TEXT, MAX_CHARS)
    print(f"Text: {len(TEXT.split()):,} Woerter, {len(TEXT):,} Zeichen")
    print(f"Chunks: {len(chunks)} (max {max(len(c) for c in chunks)} Zeichen)")
    # Kontrolle: jeder Chunk endet auf Satzzeichen
    schlecht = [i for i, c in enumerate(chunks) if not re.search(r'[.!?]["”’\')\]]*$', c.strip())]
    print(f"Chunks ohne Satzende: {schlecht if schlecht else 'keine'}")
    json.dump(chunks, open("chunks.json", "w"), ensure_ascii=False, indent=1)

    for st in STIMMEN:
        d = f"chunks/{st['key']}"
        os.makedirs(d, exist_ok=True)
        print(f"\n=== {st['name']} (speed {st['speed']}) ===")
        ok = 0
        for i, c in enumerate(chunks):
            p = f"{d}/{i:03d}.wav"
            if os.path.exists(p) and os.path.getsize(p) > 2000:
                ok += 1
                continue
            if tts(c, st["id"], st["speed"], p):
                ok += 1
            print(f"   chunk {i+1}/{len(chunks)} {'ok' if os.path.exists(p) else 'FEHLT'}", flush=True)
        print(f"   fertig: {ok}/{len(chunks)}")


if __name__ == "__main__":
    main()
