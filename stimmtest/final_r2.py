#!/usr/bin/env python3
"""Runde 2: fuegen, mischen, verblinden, pruefen."""
import json,os,re,secrets,shutil,subprocess,statistics
import numpy as np,soundfile as sf
SR=44100
S=json.load(open("stimmen_r2.json"))
C=json.load(open("chunks_r2.json"))
T=open("text_psalmen.txt").read()
W=len(T.split())
VOICE_DB=-19.0; BETT_DB=-31.0; VOR,NACH=4.0,6.0
def rms(x): return 20*np.log10(np.sqrt((x**2).mean())+1e-12)
def sprach_rms(x):
    w=int(0.02*SR); env=np.convolve(np.abs(x),np.ones(w)/w,mode="same")
    m=env>0.15*np.percentile(env,95)
    return rms(x[m]) if m.sum()>SR else rms(x)
bett=sf.read("musik/bett_pad_feuer.wav",dtype="float32",always_2d=True)[0]
os.makedirs("out_r2",exist_ok=True)
qa={}
for st in S:
    teile,grenzen,pos=[],[],0
    for i in range(len(C)):
        y,s=sf.read(f"chunks/{st['key']}/{i:03d}.wav",dtype="float32",always_2d=True)
        y=y.mean(axis=1); assert s==SR
        if i>0: grenzen.append(pos/SR)
        teile.append(y); pos+=len(y)
    v=np.concatenate(teile); dauer=len(v)/SR
    v*=10**(VOICE_DB/20)/10**(sprach_rms(v)/20)
    # trocken
    sf.write(f"out_r2/_{st['key']}_a.wav",v,SR)
    # mit Bett
    ges=int((dauer+VOR+NACH)*SR)
    b=np.tile(bett,(int(ges/len(bett))+2,1))[:ges]
    b*=10**(BETT_DB/20)/10**(rms(b.mean(axis=1))/20)
    f=int(3*SR); b[:f]*=np.linspace(0,1,f)[:,None]; b[-f:]*=np.linspace(1,0,f)[:,None]
    mix=b.copy(); o=int(VOR*SR)
    mix[o:o+len(v),0]+=v; mix[o:o+len(v),1]+=v
    sp=float(np.abs(mix).max())
    if sp>0.97: mix*=0.97/sp
    sf.write(f"out_r2/_{st['key']}_b.wav",mix,SR)
    # Nahtpruefung an Sprachfenstern
    naht=[]
    for g in grenzen:
        i=int(g*SR); Wn=int(1.0*SR); G=int(0.15*SR)
        a1=v[max(0,i-G-Wn):i-G]; c1=v[i+G:i+G+Wn]
        if len(a1)>SR//4 and len(c1)>SR//4:
            naht.append(round(float(rms(c1)-rms(a1)),2))
    qa[st["key"]]={"name":st["name"],"id":st["id"],"speed":st["speed"],
        "dauer_min":round(dauer/60,2),"wpm":round(W/(dauer/60),1),
        "naht_zeiten_s":[round(g,2) for g in grenzen],"naht_pegel_db":naht,
        "abstand_stimme_bett_db":round(float(VOICE_DB-BETT_DB),1),
        "peak_mix_dbfs":round(float(20*np.log10(np.abs(mix).max())),1)}
    print(f"{st['name'][:30]:30s} {dauer/60:5.2f} min  {W/(dauer/60):6.1f} WPM  Naht {naht}",flush=True)
# MP3 + Verblindung
ordn=list(range(5))
for i in range(4,0,-1):
    j=secrets.randbelow(i+1); ordn[i],ordn[j]=ordn[j],ordn[i]
os.makedirs("hoertest2",exist_ok=True)
zu=[]
for n,idx in enumerate(ordn,1):
    st=S[idx]
    for suf in ("a","b"):
        wav=f"out_r2/_{st['key']}_{suf}.wav"; mp3=f"hoertest2/{n:02d}{suf}.mp3"
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",wav,"-codec:a","libmp3lame",
                        "-b:a","192k","-map_metadata","-1","-write_xing","0","-fflags","+bitexact",mp3],check=True)
    zu.append((n,st))
with open("aufloesung2.txt","w") as f:
    f.write("AUFLOESUNG STIMMTEST RUNDE 2 - erst nach dem Hoeren oeffnen\n"+"="*62+"\n\n")
    f.write("a = trocken, b = mit Klangbett (synthetisches Pad + Feuer, -31 dBFS)\n\n")
    for n,st in zu:
        q=qa[st["key"]]
        f.write(f"{n:02d}a/{n:02d}b\n   Stimme       : {st['name']}\n   Fish-ID      : {st['id']}\n"
                f"   Modell       : s2.1-pro-free\n   prosody.speed: {st['speed']}\n"
                f"   gemessen     : {q['wpm']} WPM, {q['dauer_min']} min\n\n")
    f.write("Text: WEBBE Psalm 23 + Psalm 91 + Johannes 14 (Anfang), 715 Woerter\n")
    f.write("'LORD' fuer die TTS als 'Lord' normalisiert (klanglich identisch)\n")
json.dump(qa,open("qa_r2.json","w"),ensure_ascii=False,indent=1)
print("\nVerblindung: "+", ".join(f"{n:02d}->[verdeckt]" for n,_ in zu))
