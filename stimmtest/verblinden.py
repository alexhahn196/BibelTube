#!/usr/bin/env python3
"""
verblinden.py - vergibt 01/02/03 in zufaelliger Reihenfolge und schreibt die
Zuordnung nach aufloesung.txt. Die MP3s enthalten keine Metadaten und keinen
Hinweis auf die Stimme im Dateinamen.

Der Zufall wird aus os.urandom gezogen, nicht aus einem Seed - ich kenne die
Zuordnung danach nur noch aus aufloesung.txt.
"""
import json, os, secrets, subprocess, shutil

b = json.load(open("qa_bericht.json"))
keys = list(b["stimmen"].keys())

# Fisher-Yates mit kryptographischem Zufall
for i in range(len(keys) - 1, 0, -1):
    j = secrets.randbelow(i + 1)
    keys[i], keys[j] = keys[j], keys[i]

os.makedirs("hoertest", exist_ok=True)
zuordnung = []
for n, k in enumerate(keys, 1):
    ziel = f"hoertest/{n:02d}.mp3"
    shutil.copyfile(f"out/_{k}.mp3", ziel)
    # Metadaten sicher entfernen (auch ID3v1/v2)
    tmp = ziel + ".tmp.mp3"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", ziel,
                    "-codec", "copy", "-map_metadata", "-1",
                    "-fflags", "+bitexact", tmp], check=True)
    os.replace(tmp, ziel)
    s = b["stimmen"][k]
    zuordnung.append((n, s["name"], s["id"], s["speed"], s["wpm"], s["dauer_min"]))

with open("aufloesung.txt", "w") as f:
    f.write("AUFLOESUNG STIMMTEST - erst nach dem Hoeren oeffnen\n")
    f.write("=" * 62 + "\n\n")
    for n, name, vid, speed, wpm, dmin in zuordnung:
        f.write(f"{n:02d}.mp3\n")
        f.write(f"   Stimme      : {name}\n")
        f.write(f"   Fish-ID     : {vid}\n")
        f.write(f"   Modell      : s2.1-pro-free\n")
        f.write(f"   prosody.speed: {speed}\n")
        f.write(f"   gemessen    : {wpm} WPM, {dmin} min\n\n")
    f.write("Text: World English Bible British Edition (WEBBE), Johannes 1-5\n")
    f.write("Quelle: bible-api.com?translation=webbe\n")

print("hoertest/01.mp3 02.mp3 03.mp3 geschrieben, Zuordnung in aufloesung.txt")
for n, name, *_ in zuordnung:
    print(f"  {n:02d} -> [verdeckt]")
# Kontrolle: keine Metadaten mehr drin
for n in (1, 2, 3):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format_tags",
                          "-of", "default=nw=1", f"hoertest/{n:02d}.mp3"],
                         capture_output=True, text=True).stdout.strip()
    print(f"  {n:02d}.mp3 Metadaten: {out if out else 'keine'}")
