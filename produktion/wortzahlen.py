#!/usr/bin/env python3
"""Zaehlt WEBBE-Wortzahlen kapitelweise, damit die Textzuordnung auf gemessenen
Zahlen steht statt auf Schaetzungen. Ergebnis: produktion/korpus/wortzahlen.json"""
import json,os,re,time,urllib.request,urllib.parse
from concurrent.futures import ThreadPoolExecutor
BUECHER={"psalms":150,"john":21,"matthew":28,"luke":24,"mark":16,"proverbs":31,
         "isaiah":66,"revelation":22,"1 john":5,"romans":16,"ephesians":6,
         "philippians":4,"colossians":4,"james":5,"1 peter":5,"hebrews":13,
         "acts":28,"genesis":50,"ecclesiastes":12,"daniel":12,
         # 2026-08-30 ergaenzt fuer die V06-Neuplanung (Erzaehlkorpus, Regel M8):
         "exodus":40,"joshua":24,"judges":21,"ruth":4,"1 samuel":31,
         "2 samuel":24,"1 kings":22,"2 kings":25,"esther":10,"jonah":4}
CACHE="produktion/korpus/kapitel.json"
cache=json.load(open(CACHE)) if os.path.exists(CACHE) else {}
def hole(key):
    if key in cache: return key,cache[key]
    u=f"https://bible-api.com/{urllib.parse.quote(key)}?translation=webbe"
    for a in range(4):
        try:
            with urllib.request.urlopen(u,timeout=60) as r:
                d=json.load(r)
            t=" ".join(re.sub(r"\s+"," ",v["text"]).strip() for v in d["verses"])
            return key,{"w":len(t.split()),"c":len(t),"v":len(d["verses"])}
        except Exception:
            time.sleep(1.5*(a+1))
    return key,None
jobs=[f"{b} {i}" for b,n in BUECHER.items() for i in range(1,n+1)]
jobs=[j for j in jobs if j not in cache]
print(f"{len(jobs)} Kapitel zu holen (Cache: {len(cache)})")
with ThreadPoolExecutor(max_workers=8) as ex:
    for n,(k,v) in enumerate(ex.map(hole,jobs),1):
        if v: cache[k]=v
        if n%50==0: print(f"  {n}/{len(jobs)}",flush=True); json.dump(cache,open(CACHE,"w"))
json.dump(cache,open(CACHE,"w"))
summe={}
for b,n in BUECHER.items():
    ks=[cache.get(f"{b} {i}") for i in range(1,n+1)]
    fehl=[i for i,x in enumerate(ks,1) if not x]
    w=sum(x["w"] for x in ks if x)
    summe[b]={"woerter":w,"kapitel":n,"fehlend":fehl,"stunden_140wpm":round(w/140/60,2)}
json.dump(summe,open("produktion/korpus/wortzahlen.json","w"),indent=1)
for b,v in sorted(summe.items(),key=lambda x:-x[1]["woerter"]):
    f=f" FEHLEND:{v['fehlend']}" if v["fehlend"] else ""
    print(f"{b:14s} {v['woerter']:>7,} W  {v['stunden_140wpm']:>5.2f} h{f}")
