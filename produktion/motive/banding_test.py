#!/usr/bin/env python3
"""
banding_test.py - misst, was die Encode-Kette mit dem dunklen Nachthimmel macht.

ANLASS (2026-08-23): 12 % der Aufrufe kommen vom Fernseher, tragen aber 30 %
der Wiedergabezeit. Auf einem grossen Schirm im dunklen Zimmer sind Streifen
im Nachthimmel sichtbar, die auf dem Handy niemand bemerkt. Gate 1 prueft
Thumbnail und Ton, aber nichts an der encodierten Videospur - diese Luecke ist
im Gate-Audit festgehalten.

MESSGROESSE: Ein Streifen ist eine grosse zusammenhaengende Flaeche mit exakt
gleichem Luma-Wert. Im Quellbild verhindert die gemalte Textur das (groesste
einfarbige Flaeche 0,012 % des Bildes); die Frage ist, ob der Encoder sie
stehen laesst.

BEFUND: Zwei getrennte Effekte, die nicht verwechselt werden duerfen.

  1. STUFENVERLUST - strukturell, durch keine Bitrate zu beheben.
     Der dunkle Bereich des Quellbilds nutzt 48 Luma-Werte. Videofarbraum ist
     limited range (16-235), also bleiben 48 x 219/255 = 41,2 davon uebrig.
     Gemessen: 41, in JEDER 8-Bit-Variante, auch bei CRF 20. In 10 Bit
     (limited range 64-940) bleiben alle 48.

  2. FLECKENGROESSE - haengt an der Bitrate.
     CRF 28 -> Faktor 90 gegenueber dem Quellbild, CRF 22 -> 28, CRF 20 -> 11.
     10 Bit bei CRF 28 -> 15, also besser als 8 Bit bei CRF 22, bei halber
     Dateigroesse.

Dither hilft NICHT: sowohl `noise=alls=4` als auch `-tune grain` haben die
Fleckengroesse verschlechtert (109x bzw. 113x). Der Grund ist derselbe wie
unter 1 - beide arbeiten in 8 Bit, wo die Stufen schon fehlen.

GRENZE DIESER MESSGROESSE: sie misst Flachheit, und Rauschen macht flach
unflach. Am unencodierten Standbild senkt `noise=alls=4` den Wert allein
schon um Faktor 5 (0,0124 -> 0,0025 %), ohne jeden Encode. Der Vergleich
8 Bit gegen 10 Bit ist davon nicht betroffen (keine der beiden ist
gedithert), und der Stufenwert erst recht nicht. Die Dither-Varianten sind
konfundiert - aber zu ihren Gunsten: haette das Rauschen den Encode
ueberlebt, waere ihr Wert gesunken statt gestiegen.

Aufruf:  python3 produktion/motive/banding_test.py [--encode]
         Ohne --encode werden nur vorhandene Testdateien vermessen.
"""
import argparse
import json
import os
import subprocess

import numpy as np
from PIL import Image
from scipy import ndimage

try:
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
except ImportError:
    FF = "ffmpeg"

BILD = "produktion/motive/motiv-video-03.png"   # dunkelstes Standbild, Median-Luma 20
ZIEL = "produktion/motive/bandingtest"
W, H, FPS, T = 1920, 1080, 24, 300
DUNKEL = 48            # Luma-Schwelle, unter der 87-89 % des Bildes liegen
LAUFZEIT_S = 3.5 * 3600
TON_BYTES = 192000 / 8 * LAUFZEIT_S

VARIANTEN = [
    ("i    8 Bit CRF 28 (Ist)",      28, "yuv420p",     None,      None),
    ("ii   10 Bit CRF 28",           28, "yuv420p10le", None,      None),
    ("iii  8 Bit CRF 28 + noise",    28, "yuv420p",     "noise=alls=4:allf=t+u", None),
    ("iv   8 Bit CRF 28 tune=grain", 28, "yuv420p",     None,      "grain"),
    ("v    8 Bit CRF 22",            22, "yuv420p",     None,      None),
    ("vi   8 Bit CRF 20",            20, "yuv420p",     None,      None),
]


def dateiname(nm):
    return f"{ZIEL}/{nm.split()[0]}.mp4"


def encode(nm, crf, pix, extra_vf, tune):
    """Dieselbe Kette wie schritt5_video.py:zyklus_bauen()."""
    a = 1.04 - 1.0
    z = f"1+{a/2:.6f}*(1-cos(2*PI*on/{FPS*T}))"
    vf = (f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d=1:s={W}x{H}:fps={FPS}")
    if extra_vf:
        vf += "," + extra_vf
    vf += f",format={pix}"
    cmd = [FF, "-y", "-loglevel", "error", "-loop", "1", "-framerate", str(FPS),
           "-t", str(T), "-i", BILD, "-vf", vf, "-c:v", "libx264",
           "-preset", "medium", "-crf", str(crf)]
    if tune:
        cmd += ["-tune", tune]
    cmd += ["-g", str(FPS * 10), "-pix_fmt", pix, "-an", dateiname(nm)]
    subprocess.run(cmd, check=True)


def bild_aus(mp4, t=150.0):
    roh = subprocess.run([FF, "-v", "error", "-ss", str(t), "-i", mp4,
                          "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(roh, dtype=np.uint8).reshape(H, W).astype(np.int16)


def groesste_einfarbige_flaeche(im):
    dunkel = im < DUNKEL
    groesst = 0
    for v in np.unique(im[dunkel]):
        lab, n = ndimage.label((im == v) & dunkel)
        if n:
            groesst = max(groesst, int(ndimage.sum(np.ones_like(lab), lab,
                                                   range(1, n + 1)).max()))
    return groesst


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--encode", action="store_true",
                    help="Testdateien neu erzeugen (6 Encodes, je einige Minuten)")
    a = ap.parse_args()
    os.makedirs(ZIEL, exist_ok=True)

    src = np.asarray(Image.open(BILD).convert("L"), dtype=np.int16)
    sd = src[src < DUNKEL]
    sg = groesste_einfarbige_flaeche(src)

    if a.encode:
        for nm, crf, pix, vfx, tune in VARIANTEN:
            print(f"  encodiere {nm} ...", flush=True)
            encode(nm, crf, pix, vfx, tune)

    bericht = {"erzeugt_am": "2026-08-23", "quelle": BILD, "crf_basis": 28,
               "dunkelschwelle_luma": DUNKEL,
               "quelle": {"stufen": int(len(np.unique(sd))),
                          "groesste_flaeche_pct": round(100 * sg / src.size, 3)},
               "varianten": {}}
    print(f"\n{'Variante':30s} {'Datei 3,5h':>11s} {'Stufen':>7s} "
          f"{'gr. Flaeche':>12s} {'vs Quelle':>10s}")
    print(f"{'Quellbild (PNG, full range)':30s} {'':>11s} "
          f"{len(np.unique(sd)):7d} {100*sg/src.size:11.3f} % {'1x':>10s}")
    for nm, crf, pix, vfx, tune in VARIANTEN:
        p = dateiname(nm)
        if not os.path.exists(p):
            print(f"{nm:30s} fehlt - mit --encode erzeugen")
            continue
        g = os.path.getsize(p)
        im = bild_aus(p)
        b = groesste_einfarbige_flaeche(im)
        st = int(len(np.unique(im[im < DUNKEL])))
        voll = (g * LAUFZEIT_S / T + TON_BYTES) / 2 ** 30
        bericht["varianten"][nm.strip()] = {
            "crf": crf, "pixelformat": pix, "zyklus_mb": round(g / 1048576, 2),
            "datei_3h30_gb": round(voll, 2), "stufen": st,
            "groesste_flaeche_pct": round(100 * b / im.size, 3),
            "faktor_gegen_quelle": round(b / sg, 1)}
        print(f"{nm:30s} {voll:10.2f}G {st:7d} {100*b/im.size:11.3f} % {b/sg:9.0f}x")

    print(f"\nErwarteter Stufenverlust durch limited range: "
          f"{len(np.unique(sd))} x 219/255 = {len(np.unique(sd))*219/255:.1f}")
    json.dump(bericht, open(f"{ZIEL}/messung.json", "w"), indent=1, ensure_ascii=False)
    print(f"Bericht: {ZIEL}/messung.json")


if __name__ == "__main__":
    main()
