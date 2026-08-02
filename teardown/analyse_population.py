#!/usr/bin/env python3
"""
analyse_population.py - prueft die Hypothesen aus matrix_voll.csv gegen die
GESAMTE Videoliste aller 8 Kanaele (454 Videos mit Views und Dauer).

Grund: die 24 Stichproben (Top/Median/Flop) sind per Konstruktion Extremwerte.
Was dort wie ein Muster aussieht, muss gegen die Grundgesamtheit geprueft
werden, sonst wird ein Auswahleffekt als Ursache gelesen.

Wichtig: Kanal-Median als Bezugsgroesse. Ein roher Kanalvergleich ist durch
die Kanalgroesse verzerrt (SleepCodex hat 131 Videos bei Median 3.200 Views;
seine Treffer verschwinden im globalen Median).
"""
import json, glob, statistics

BASE = sorted(glob.glob("teardown_batch_*"))[-1]
NAMES = {
    'UCBnoLXdJ9tIR-8vjSdgiYAw': 'Hush Little Lamb',
    'UC1AOmfQ2hsB0G0QBw5iCaUQ': 'Grace Beyond Prayer',
    'UC_oYrNMZ081r-ZgxY-883_w': 'The Sleep Bible',
    'UCo6ArZxfwPQ4uSCFiqfDK9A': 'Rest in Jesus',
    'UCMbWbGbTG23WSa5M6VJgctw': 'Rest In Faith',
    'UCiKc3XR_CAwWx1rtLFQnlvQ': 'SleepCodex',
    'UCP7dYl63OzMZXZiWlOCcv1g': 'Night Psalms',
    'UCiolk5zOhJjJta3iS6HJDCw': 'Rest in Grace',
}


def spearman(x, y):
    n = len(x)
    if n < 5:
        return None
    rx = {v: i for i, v in enumerate(sorted(range(n), key=lambda i: x[i]))}
    ry = {v: i for i, v in enumerate(sorted(range(n), key=lambda i: y[i]))}
    rx = [rx[i] for i in range(n)]
    ry = [ry[i] for i in range(n)]
    mx, my = statistics.mean(rx), statistics.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** .5
    return num / den if den else None


data = {}
for f in glob.glob(f"{BASE}/*_videos.jsonl"):
    chan = f.split('/')[-1].replace('_videos.jsonl', '')
    rows = []
    for line in open(f):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get('view_count') and (d.get('duration') or 0) > 300:
            rows.append(d)
    data[chan] = rows

allr = [(c, d) for c, rows in data.items() for d in rows]
print(f"Grundgesamtheit: {len(allr)} Videos ueber {len(data)} Kanaele\n")

print("== H1: Laengere Videos = mehr Views? ==")
rho = spearman([d['duration'] for _, d in allr], [d['view_count'] for _, d in allr])
print(f"Spearman rho(Dauer, Views) global = {rho:+.3f}  -> praktisch kein Zusammenhang")
for c, rows in sorted(data.items(), key=lambda kv: NAMES.get(kv[0], '')):
    r = spearman([d['duration'] for d in rows], [d['view_count'] for d in rows])
    if r is not None:
        print(f"   {NAMES[c]:22s} n={len(rows):3d}  rho={r:+.2f}")
print("   Fazit: 4 Kanaele positiv, 4 Kanaele null/negativ -> Dauer ist KEIN Hebel.")

print("\n== H2: Gibt es eine Untergrenze? (<1.5h vs >=1.5h, Median-Views) ==")
for c, rows in sorted(data.items(), key=lambda kv: NAMES.get(kv[0], '')):
    k = [d['view_count'] for d in rows if d['duration'] < 5400]
    l = [d['view_count'] for d in rows if d['duration'] >= 5400]
    if len(k) >= 3 and len(l) >= 3:
        mk, ml = statistics.median(k), statistics.median(l)
        print(f"   {NAMES[c]:22s} kurz n={len(k):3d} {mk:>9,.0f}   "
              f"lang n={len(l):3d} {ml:>9,.0f}   {ml/max(mk,1):>5.2f}x")
    else:
        print(f"   {NAMES[c]:22s} nicht testbar (kurz={len(k)}, lang={len(l)})")

print("\n== H3: Themen-Effekt, normiert auf den KANAL-Median ==")
print("   (nur Kanaele mit >=4 Videos je Stichwort)")
for kw in ['enoch', 'banned', 'nephilim', 'angel', 'gospel', 'john', 'isaiah',
           'psalm', 'jesus', 'prayer', 'protection', '4k', 'complete', 'full']:
    zeilen = []
    for c, rows in data.items():
        cm = statistics.median([d['view_count'] for d in rows])
        sel = [d['view_count'] for d in rows if kw in (d.get('title') or '').lower()]
        if len(sel) >= 4:
            zeilen.append(f"      {NAMES[c]:22s} n={len(sel):3d}  "
                          f"{statistics.median(sel)/max(cm,1):>6.2f}x Kanal-Median")
    if zeilen:
        print(f"   '{kw}':")
        for z in zeilen:
            print(z)

print("\n== H4: Die drei groessten Treffer je Kanal ==")
for c, rows in sorted(data.items(), key=lambda kv: NAMES.get(kv[0], '')):
    cm = statistics.median([d['view_count'] for d in rows])
    print(f"\n   {NAMES[c]} (Kanal-Median {cm:,.0f}):")
    for d in sorted(rows, key=lambda d: -d['view_count'])[:3]:
        print(f"      {d['view_count']:>9,}  ({d['view_count']/max(cm,1):>6.1f}x)  "
              f"{d['duration']/3600:>4.1f}h  {(d.get('title') or '')[:62]}")
