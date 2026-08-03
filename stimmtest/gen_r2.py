#!/usr/bin/env python3
"""Runde 2: fuenf Stimmen, Psalm-Text, Chunking an Satzenden, WAV-Chunks."""
import json,os,re,time,urllib.request
from concurrent.futures import ThreadPoolExecutor
K=os.environ["FISH_KEY"]; EP="https://api.fish.audio/v1/tts"
T=open("text_psalmen.txt").read().strip().replace("LORD","Lord")
S=[{"key":"r2_konv","name":"Calm Conversational Narrator","id":"e20aab7ac410488daa28a89a4e693509","speed":0.74},
   {"key":"r2_prof","name":"Calm Professional Narrator","id":"56446c2a40c141589c9143940ec88c17","speed":0.62},
   {"key":"r2_nath","name":"Nathan English Man (US)","id":"bbb58d698b5f46719fd04688dfac7359","speed":0.77},
   {"key":"r2_seni","name":"Gentle Senior Male","id":"b379a24b6ed04f4daed9d6f4e49c49b7","speed":0.71},
   {"key":"r2_gent","name":"Calm and Gentle Voice","id":"7213baebcf1b4b1a8c0ec010c8847f9c","speed":0.85}]
def chunks(t,m=1800):
    s=re.findall(r'[^.!?]*[.!?]+["”’\')\]]*\s*',t); r=t[sum(len(x) for x in s):]
    if r.strip(): s.append(r)
    out,a=[],""
    for x in s:
        if a and len(a)+len(x)>m: out.append(a.strip()); a=x
        else: a+=x
    if a.strip(): out.append(a.strip())
    return out
C=chunks(T); json.dump(C,open("chunks_r2.json","w"),ensure_ascii=False,indent=1)
print(f"{len(T.split())} Woerter -> {len(C)} Chunks")
def job(a):
    key,vid,sp,i,txt=a; p=f"chunks/{key}/{i:03d}.wav"
    if os.path.exists(p) and os.path.getsize(p)>2000: return (key,i,"skip")
    b={"text":txt,"reference_id":vid,"format":"wav","sample_rate":44100,"normalize":True,"prosody":{"speed":sp}}
    d=json.dumps(b).encode()
    for k_ in range(5):
        try:
            r=urllib.request.Request(EP,data=d,headers={"Authorization":f"Bearer {K}",
                "Content-Type":"application/json","model":"s2.1-pro-free"})
            with urllib.request.urlopen(r,timeout=300) as f: o=f.read()
            if o[:1]==b"{": raise RuntimeError(o[:140].decode("utf-8","replace"))
            t2=p+".part"; open(t2,"wb").write(o); os.replace(t2,p); return (key,i,"ok")
        except Exception as e:
            if k_==4: return (key,i,f"FEHLER {e}")
            time.sleep(2**k_)
jobs=[]
for st in S:
    os.makedirs(f"chunks/{st['key']}",exist_ok=True)
    for i,c in enumerate(C): jobs.append((st["key"],st["id"],st["speed"],i,c))
with ThreadPoolExecutor(max_workers=10) as ex:
    for k,i,r in ex.map(job,jobs): print(f"  {k} {i} -> {r}",flush=True)
json.dump(S,open("stimmen_r2.json","w"),ensure_ascii=False,indent=1)
print("FERTIG")
