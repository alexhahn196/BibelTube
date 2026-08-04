#!/usr/bin/env python3
"""
ki_clip_pruefung.py - prueft KI-generierte Bild-zu-Video-Clips auf
Loop-Tauglichkeit.

Ein Clip taugt als Loop-Baustein, wenn
  a) sein letzter Frame (nahezu) auf dem Startbild endet - das ist der
     Zweck des start_image==end_image-Tricks,
  b) die Kamera nicht driftet (Phasenkorrelation der Randzonen zwischen
     erstem und letztem Frame),
  c) keine Objekte entstehen/verschwinden (Stichproben-Frames sichten -
     das uebernimmt der Mensch bzw. die Sichtung im Chat),
  d) Auflösung/fps/Dauer stimmen.

Aufruf:
    python3 produktion/pipeline/ki_clip_pruefung.py clip-1.mp4 clip-2.mp4 …
"""
import json
import os
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image


def ffprobe_info(p):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height,r_frame_rate,nb_frames,duration",
         "-of", "json", p], capture_output=True, text=True, check=True)
    s = json.loads(r.stdout)["streams"][0]
    z, n = s["r_frame_rate"].split("/")
    return dict(breite=int(s["width"]), hoehe=int(s["height"]),
                fps=round(int(z) / int(n), 3),
                frames=int(s.get("nb_frames") or 0),
                dauer_s=round(float(s["duration"]), 3),
                groesse_mb=round(os.path.getsize(p) / 1e6, 2))


def frames_holen(p, zeiten):
    aus = []
    for t in zeiten:
        r = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", f"{t:.4f}", "-i", p,
             "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
            capture_output=True, check=True)
        arr = cv2.imdecode(np.frombuffer(r.stdout, np.uint8), cv2.IMREAD_COLOR)
        aus.append(cv2.cvtColor(arr, cv2.COLOR_BGR2RGB).astype(np.float32))
    return aus


def letzter_frame(p):
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-sseof", "-0.2", "-i", p, "-vsync", "0",
         "-f", "image2pipe", "-vcodec", "png", "-"],
        capture_output=True, check=True)
    # Letztes PNG im Strom
    daten = r.stdout
    sig = b"\x89PNG"
    pos = daten.rfind(sig)
    arr = cv2.imdecode(np.frombuffer(daten[pos:], np.uint8), cv2.IMREAD_COLOR)
    return cv2.cvtColor(arr, cv2.COLOR_BGR2RGB).astype(np.float32)


def drift_messen(a, b):
    """Kameraverschiebung zwischen zwei Frames ueber die Randzonen.

    Phasenkorrelation auf vier Randstreifen (oben/unten/links/rechts,
    je 15 % der Bildhoehe/-breite). Bewegte Bildmitte (Feuer, Funken)
    bleibt aussen vor. Median der vier Verschiebungen = Kameradrift;
    echte Szenenbewegung schlaegt nur in einzelnen Streifen aus.
    """
    h, w = a.shape[:2]
    g1 = cv2.cvtColor(a.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    g2 = cv2.cvtColor(b.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    zonen = {
        "oben": (slice(0, int(h * .15)), slice(0, w)),
        "unten": (slice(int(h * .85), h), slice(0, w)),
        "links": (slice(0, h), slice(0, int(w * .15))),
        "rechts": (slice(0, h), slice(int(w * .85), w)),
    }
    versch = {}
    for name, (ys, xs) in zonen.items():
        (dx, dy), _ = cv2.phaseCorrelate(g1[ys, xs], g2[ys, xs])
        versch[name] = (round(float(dx), 3), round(float(dy), 3))
    dxs = [v[0] for v in versch.values()]
    dys = [v[1] for v in versch.values()]
    return versch, (round(float(np.median(dxs)), 3), round(float(np.median(dys)), 3))


def pruefe(p, referenz=None):
    info = ffprobe_info(p)
    dauer = info["dauer_s"]
    f0 = frames_holen(p, [0.0])[0]
    fN = letzter_frame(p)

    d = np.abs(fN - f0)
    b = dict(datei=os.path.basename(p), **info)
    b["erster_vs_letzter_mad"] = round(float(d.mean()), 3)
    b["erster_vs_letzter_max"] = int(d.max())
    b["pixelidentisch"] = bool(d.max() == 0)

    zonen, (mx, my) = drift_messen(f0, fN)
    b["drift_zonen_px"] = zonen
    b["drift_median_px"] = [mx, my]
    b["drift_unauffaellig"] = bool(abs(mx) < 1.5 and abs(my) < 1.5)

    if referenz is not None:
        d0 = np.abs(f0 - referenz)
        b["start_vs_standbild_mad"] = round(float(d0.mean()), 3)
        dN = np.abs(fN - referenz)
        b["ende_vs_standbild_mad"] = round(float(dN.mean()), 3)
    return b, f0, fN


def main():
    dateien = sys.argv[1:]
    ref_pfad = None
    if dateien and dateien[0].endswith(".png"):
        ref_pfad = dateien.pop(0)
    referenz = None
    if ref_pfad:
        referenz = np.asarray(Image.open(ref_pfad).convert("RGB"), np.float32)

    alle = []
    for p in dateien:
        b, _, _ = pruefe(p, referenz)
        alle.append(b)
        print(f"\n{b['datei']}")
        print(f"  {b['breite']}x{b['hoehe']} @ {b['fps']} fps · {b['dauer_s']} s · "
              f"{b['groesse_mb']} MB")
        print(f"  erster vs letzter Frame   mittl. |Δ| {b['erster_vs_letzter_mad']}, "
              f"max {b['erster_vs_letzter_max']} → "
              f"{'pixelidentisch' if b['pixelidentisch'] else 'NICHT identisch'}")
        if referenz is not None:
            print(f"  Start vs Standbild        mittl. |Δ| {b['start_vs_standbild_mad']}")
            print(f"  Ende  vs Standbild        mittl. |Δ| {b['ende_vs_standbild_mad']}")
        print(f"  Kameradrift (Median Randzonen) {b['drift_median_px']} px → "
              f"{'unauffällig' if b['drift_unauffaellig'] else 'DRIFT'}")
        print(f"    je Zone: {b['drift_zonen_px']}")
    ziel = os.path.join(os.path.dirname(dateien[0]), "qa-ki-clips.json")
    json.dump(alle, open(ziel, "w"), ensure_ascii=False, indent=1)
    print(f"\ngeschrieben: {ziel}")


if __name__ == "__main__":
    main()
