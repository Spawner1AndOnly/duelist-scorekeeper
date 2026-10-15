"""Cuts the trailer (demo-trailer.mp4) out of demo-A.mp4 and demo-B.mp4 with the scene times from the *.marks.json files.
Sound: the cuts use the sound effects alone (demo-X.fx.m4a) and ONE continuous music track runs underneath (no jumps at every cut);
only during the 'switch music' cut the real recording (effects + the music changing) is heard and the music bed fades away."""
import json,os,sys,subprocess
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
from recorder import FF
A=json.load(open(os.path.join(HERE,"demo-A.marks.json")));B=json.load(open(os.path.join(HERE,"demo-B.marks.json")))
BED=os.path.join(HERE,"..","snd","music5.m4a")   # Rock Loop - Mystical Energy (the app's default track)
BED_VOL=0.224                                     # same level as in the recording (music slider 80%: .35 * 0.8²)
# (video, scene, offset inside the scene, length, real sound)  -- None scene = absolute start
CUTS=[("A",None,0.3,1.9),("A",0,0.0,2.8),("A",1,0.2,1.6),("A",2,0.7,3.4),("A",3,0.0,4.4),("A",4,1.1,4.4),("A",5,0.4,6.0),("A",6,3.5,3.6),
      ("A",9,0.0,4.2),("A",10,0.4,6.5),("A",11,0.0,6.8),("A",12,0.0,1.6),("A",14,0.0,4.2),("A",15,0.0,3.4),("A",16,0.2,3.6),("A",17,0.0,4.8),
      ("A",18,3.0,4.4),("A",19,0.0,2.4),
      ("A",20,1.5,11.6,True),   # settings: the music switches twice (real sound)
      ("A",22,3.6,4.4),("A",23,0.0,4.6),("A",24,3.2,6.0),
      ("B",1,0.6,4.2),("B",2,0.6,4.4),("B",3,0.0,4.2),
      ("B",4,0.6,4.4),("B",4,14.5,7.5),   # chain: Dian Keto, Magic Jammer, Seven Tools, resolves backwards
      ("B",5,1.0,3.8),("B",5,11.6,3.6),   # Summon answered by Bottomless Trap Hole: the banish portal
      ("B",6,2.4,4.4),("B",7,2.4,3.6)]
os.makedirs(os.path.join(HERE,"_cut"),exist_ok=True);parts=[];t=0;real=[]
for n,c in enumerate(CUTS):
    v,sc,off,ln=c[:4];own=len(c)>4 and c[4]
    m=A if v=="A" else B
    start=(0 if sc is None else m["scene_start"][sc])+off
    out=os.path.join(HERE,"_cut",f"{n:02d}.mp4")
    vf=f"fade=t=in:st=0:d=0.1,fade=t=out:st={ln-0.12:.2f}:d=0.12"
    af=f"afade=t=in:st=0:d=0.05,afade=t=out:st={ln-0.12:.2f}:d=0.12"   # the sound fades with the picture (no clicks between the cuts)
    src=os.path.join(HERE,f"demo-{v}.mp4");fx=os.path.join(HERE,f"demo-{v}.fx.m4a")
    aud=["-ss",f"{start:.2f}","-t",f"{ln:.2f}","-i",src if own or not os.path.exists(fx) else fx]
    subprocess.run([FF,"-y","-loglevel","error","-ss",f"{start:.2f}","-t",f"{ln:.2f}","-i",src]+aud+["-map","0:v","-map","1:a","-vf",vf,"-af",af,"-r","30","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-ar","48000",out],check=True)
    parts.append(out)
    if own:real.append((t,t+ln))
    t+=ln
lst=os.path.join(HERE,"_cut","list.txt");open(lst,"w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
joined=os.path.join(HERE,"_cut","joined.mp4")
subprocess.run([FF,"-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",joined],check=True)
# music bed: loops for the whole trailer, fades away around the 'real sound' cuts, fades out at the end
dk="*".join(f"(1-min(1,max(0,min(t-{a-0.6:.2f},{b+0.6:.2f}-t)/0.6)))" for a,b in real) or "1"
bed=f"[1:a]volume={BED_VOL},volume='{dk}':eval=frame,afade=t=in:st=0:d=1.5,afade=t=out:st={t-2.5:.2f}:d=2.5,atrim=0:{t:.2f}[m];[0:a][m]amix=inputs=2:normalize=0:duration=first[a]"
subprocess.run([FF,"-y","-loglevel","error","-i",joined,"-stream_loop","-1","-i",BED,"-filter_complex",bed,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","160k","-ar","48000","-movflags","+faststart",os.path.join(HERE,"demo-trailer.mp4")],check=True)
os.remove(joined)
print(round(t,1),"seconds")
