#!/usr/bin/env python3
"""v2: drei optimierte Stimmen, 5-Minuten-Text, Tempo auf ~135-145 WPM getrimmt."""
import json,os,re,time,urllib.request
from concurrent.futures import ThreadPoolExecutor
KEY=os.environ["FISH_KEY"]; EP="https://api.fish.audio/v1/tts"
TEXT=open("text_5min.txt").read().strip()
STIMMEN=[{"key":"v2a","name":"Dramatic Whisper Male","id":"b879fcec88c542b78d2eb4462e4d4c59","speed":0.64},
         {"key":"v2b","name":"Henry (British Narrator)","id":"55f0cafef00f4e16808bcd75c4b41a6f","speed":0.75},
         {"key":"v2c","name":"Calm Meditation Voice","id":"14c13e72d4644b0dbd2f147df20f6d80","speed":0.92}]
def chunks(t,m=1800):
    s=re.findall(r'[^.!?]*[.!?]+["”’\')\]]*\s*',t); r=t[sum(len(x) for x in s):]
    if r.strip(): s.append(r)
    out,a=[],""
    for x in s:
        if a and len(a)+len(x)>m: out.append(a.strip()); a=x
        else: a+=x
    if a.strip(): out.append(a.strip())
    return out
C=chunks(TEXT); json.dump(C,open("chunks_v2.json","w"),ensure_ascii=False,indent=1)
print(f"{len(TEXT.split())} Woerter -> {len(C)} Chunks, alle mit Satzende: "
      f"{all(re.search(chr(91)+'.!?'+chr(93)+chr(34)+chr(39)+']*$',c.strip()) for c in C)}")
def job(a):
    key,vid,sp,i,txt=a; p=f"chunks/{key}/{i:03d}.wav"
    if os.path.exists(p) and os.path.getsize(p)>2000: return (key,i,"skip")
    b={"text":txt,"reference_id":vid,"format":"wav","sample_rate":44100,"normalize":True,"prosody":{"speed":sp}}
    d=json.dumps(b).encode()
    for k_ in range(5):
        try:
            r=urllib.request.Request(EP,data=d,headers={"Authorization":f"Bearer {KEY}",
                "Content-Type":"application/json","model":"s2.1-pro-free"})
            with urllib.request.urlopen(r,timeout=300) as f: o=f.read()
            if o[:1]==b"{": raise RuntimeError(o[:140].decode("utf-8","replace"))
            t=p+".part"; open(t,"wb").write(o); os.replace(t,p); return (key,i,"ok")
        except Exception as e:
            if k_==4: return (key,i,f"FEHLER {e}")
            time.sleep(2**k_)
jobs=[]
for s in STIMMEN:
    os.makedirs(f"chunks/{s['key']}",exist_ok=True)
    for i,c in enumerate(C): jobs.append((s["key"],s["id"],s["speed"],i,c))
with ThreadPoolExecutor(max_workers=9) as ex:
    for k,i,r in ex.map(job,jobs): print(f"  {k} {i} -> {r}",flush=True)
print("FERTIG")
