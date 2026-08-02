#!/usr/bin/env python3
"""
analyse.py - baut aus den vorhandenen Rohdaten die vollstaendige
Vergleichsmatrix.

Quellen:
  1. teardown_batch_*/matrix.csv        - was das Originalskript messen konnte
  2. teardown_batch_*/*_videos.jsonl    - Kanal-Listing (Dauer, Views, Titel)
  3. NexLev-Bulk-Transcripts (JSON)     - Sprechzeitpunkte mit Millisekunden

Der Medien-Download ist in dieser Umgebung durch YouTube blockiert (403 auf
allen googlevideo-URLs). sprache_bis_pct wird deshalb NICHT aus Audio-Peaks
geschaetzt, sondern exakt aus den Caption-Zeitstempeln berechnet.
"""
import json, glob, csv, os, sys, statistics

BASE = sorted(glob.glob("teardown_batch_*"))[-1]
TRANS = sorted(glob.glob(
    "/root/.claude/projects/-home-user-BibelTube/"
    "9aef74de-a06c-511a-a222-c5a7615907d5/tool-results/"
    "mcp-NexLev-get_bulk_video_transcripts-*.txt"))

# ---- 1. Kanal-Listings: id -> dauer/views/titel + Kanalstatistik ----------
vid_meta, chan_videos = {}, {}
for f in glob.glob(f"{BASE}/*_videos.jsonl"):
    chan = os.path.basename(f).replace("_videos.jsonl", "")
    rows = []
    for line in open(f):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if not d.get("id"):
            continue
        vid_meta[d["id"]] = {
            "titel": d.get("title") or "",
            "dauer": d.get("duration") or 0,
            "views": d.get("view_count") or 0,
            "kanal": chan,
        }
        rows.append(d)
    chan_videos[chan] = rows

# ---- 2. Transcripts: Sprechabdeckung exakt bestimmen ---------------------
speech = {}
for tf in TRANS:
    doc = json.load(open(tf))
    for res in doc["transcripts"]["results"]:
        if not res.get("success"):
            continue
        segs = res["data"]["transcript"]
        iv = []
        for s in segs:
            try:
                a, b = int(s["startMs"]), int(s["endMs"])
            except (KeyError, TypeError, ValueError):
                continue
            if b > a:
                iv.append((a, b))
        if not iv:
            continue
        iv.sort()
        # Overlaps verschmelzen -> echte Netto-Sprechzeit
        merged = [list(iv[0])]
        for a, b in iv[1:]:
            if a <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], b)
            else:
                merged.append([a, b])
        netto = sum(b - a for a, b in merged) / 1000.0
        gaps = [(merged[i + 1][0] - merged[i][1]) / 1000.0
                for i in range(len(merged) - 1)]
        speech[res["videoId"]] = {
            "erste_s": merged[0][0] / 1000.0,
            "letzte_s": merged[-1][1] / 1000.0,
            "netto_s": netto,
            "segmente": len(segs),
            "max_pause_s": max(gaps) if gaps else 0.0,
            "pausen_ueber_60s": sum(1 for g in gaps if g > 60),
        }

# ---- 3. matrix.csv einlesen (was das Skript geschafft hat) --------------
script_rows = {}
mpath = f"{BASE}/matrix.csv"
with open(mpath) as fh:
    for r in csv.DictReader(fh):
        script_rows[r["video_id"]] = r

# ---- 4. Rollenliste ------------------------------------------------------
picks = [l.split() for l in open(f"{BASE}/ids.txt") if l.strip()]

sup = json.load(open("nexlev_supplement.json"))

out = []
for chan, role, vid in picks:
    m = vid_meta.get(vid, {})
    s = speech.get(vid)
    sr = script_rows.get(vid, {})
    nx = sup.get(vid, {})
    dauer = int(sr.get("dauer_s") or 0) or nx.get("dauer_s") or m.get("dauer", 0)
    views = int(sr.get("views") or 0) or nx.get("views") or m.get("views", 0)
    likes = sr.get("likes") or nx.get("likes") or ""
    rate = sr.get("like_rate_pct") or (
        round(likes * 100 / views, 2) if (likes and views) else "")

    if sr.get("tags_gesetzt"):
        tags = sr["tags_gesetzt"]
    elif "tags_n" in nx:
        tags = "JA" if nx["tags_n"] else "NEIN"
    else:
        tags = "NA"

    rec = {
        "kanal": chan,
        "rolle": role,
        "video_id": vid,
        "titel": (sr.get("titel") or m.get("titel", ""))[:70],
        "views": views,
        "likes": likes,
        "like_rate_pct": rate,
        "dauer_s": dauer,
        "dauer_h": round(dauer / 3600, 2) if dauer else "",
        "aufloesung": sr.get("aufloesung", "NA"),
        "fps": sr.get("fps", "NA"),
        "tags_gesetzt": tags,
        "tags_anzahl": nx.get("tags_n", "NA"),
        "captions": sr.get("captions") or nx.get("captions", "NA"),
    }
    if s and dauer:
        rec.update({
            "sprache_start_s": round(s["erste_s"], 1),
            "sprache_bis_s": round(s["letzte_s"], 1),
            "sprache_bis_pct": round(100 * s["letzte_s"] / dauer, 1),
            "sprech_netto_s": round(s["netto_s"], 1),
            "sprech_anteil_pct": round(100 * s["netto_s"] / dauer, 1),
            "max_pause_s": round(s["max_pause_s"], 1),
            "pausen_ueber_60s": s["pausen_ueber_60s"],
        })
    else:
        for k in ("sprache_start_s", "sprache_bis_s", "sprache_bis_pct",
                  "sprech_netto_s", "sprech_anteil_pct", "max_pause_s",
                  "pausen_ueber_60s"):
            rec[k] = "NA"
    out.append(rec)

cols = list(out[0].keys())
with open(f"{BASE}/matrix_voll.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(out)

# ---- 5. Kanalstatistik: Streuung Top vs Median --------------------------
print(f"== matrix_voll.csv geschrieben ({len(out)} Zeilen) ==\n")
hdr = ("rolle", "video_id", "views", "dauer_h", "aufl", "fps", "tags", "caps",
       "spr_bis%", "spr_anteil%", "maxPause", "start_s")
print("%-7s %-12s %10s %6s %10s %4s %5s %5s %8s %10s %8s %7s" % hdr)
for r in out:
    print("%-7s %-12s %10s %6s %10s %4s %5s %5s %8s %10s %8s %7s" % (
        r["rolle"], r["video_id"], r["views"], r["dauer_h"], r["aufloesung"],
        r["fps"], r["tags_gesetzt"], r["captions"], r["sprache_bis_pct"],
        r["sprech_anteil_pct"], r["max_pause_s"], r["sprache_start_s"]))

def med(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return statistics.median(xs) if xs else None


print("\n== TOP vs MEDIAN vs FLOP: Median je Kennzahl ==")
print("%-16s %12s %12s %12s" % ("kennzahl", "TOP", "MEDIAN", "FLOP"))
for key, label in (("dauer_h", "Laufzeit h"),
                   ("views", "Views"),
                   ("like_rate_pct", "Like-Rate %"),
                   ("sprache_bis_pct", "Sprache bis %"),
                   ("sprech_anteil_pct", "Sprechanteil %"),
                   ("max_pause_s", "max Pause s")):
    vals = {}
    for rolle in ("TOP", "MEDIAN", "FLOP"):
        v = med([r[key] for r in out if r["rolle"] == rolle])
        vals[rolle] = f"{v:,.2f}" if v is not None else "NA"
    print("%-16s %12s %12s %12s" % (label, vals["TOP"], vals["MEDIAN"], vals["FLOP"]))

print("\n== Laufzeit TOP vs FLOP je Kanal ==")
for chan in sorted({r["kanal"] for r in out}):
    t = next((r["dauer_h"] for r in out if r["kanal"] == chan and r["rolle"] == "TOP"), None)
    f = next((r["dauer_h"] for r in out if r["kanal"] == chan and r["rolle"] == "FLOP"), None)
    if t and f:
        mark = "TOP laenger" if t > f else "FLOP laenger"
        print(f"{chan}  TOP={t:5.2f}h  FLOP={f:5.2f}h  -> {mark}")

print("\n== Tags / Untertitel je Kanal (belegte Videos) ==")
for chan in sorted({r["kanal"] for r in out}):
    rs = [r for r in out if r["kanal"] == chan and r["tags_gesetzt"] != "NA"]
    if not rs:
        continue
    tg = ", ".join(f"{r['rolle']}={r['tags_gesetzt']}" for r in rs)
    cp = ", ".join(f"{r['rolle']}={r['captions']}" for r in rs)
    print(f"{chan}\n   tags: {tg}\n   caps: {cp}")

print("\n== Kanal-Streuung (aus Listing, alle Videos >300s) ==")
for chan, rows in sorted(chan_videos.items()):
    vs = sorted(d["view_count"] for d in rows
                if d.get("view_count") and (d.get("duration") or 0) > 300)
    ds = [d["duration"] for d in rows
          if d.get("view_count") and (d.get("duration") or 0) > 300]
    if not vs:
        continue
    print(f"{chan}  n={len(vs):3d}  min={vs[0]:>9,}  median={statistics.median(vs):>10,.0f}"
          f"  max={vs[-1]:>9,}  faktor={vs[-1]/max(vs[0],1):>7.1f}x"
          f"  dauer_median={statistics.median(ds)/3600:.2f}h")
