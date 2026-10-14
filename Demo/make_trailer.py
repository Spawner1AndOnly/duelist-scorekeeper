"""Cuts the trailer (demo-trailer.mp4) out of demo-A.mp4 and demo-B.mp4 with the scene times from the *.marks.json files."""
import json,os,sys,subprocess
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,HERE)
from recorder import FF
A=json.load(open(os.path.join(HERE,"demo-A.marks.json")));B=json.load(open(os.path.join(HERE,"demo-B.marks.json")))
# (video, scene, offset inside the scene, length)  -- None scene = absolute start
CUTS=[("A",None,0.3,1.9),("A",0,0.0,2.8),("A",1,0.2,1.6),("A",2,0.7,3.4),("A",3,0.0,4.4),("A",4,1.1,4.4),("A",5,0.4,6.0),("A",6,3.5,3.6),
      ("A",9,0.0,4.2),("A",10,0.4,6.5),("A",11,0.0,6.8),("A",12,0.0,1.6),("A",14,0.0,4.2),("A",15,0.0,3.4),("A",16,0.2,3.6),("A",17,0.0,4.8),
      ("A",18,3.0,4.4),("A",19,0.0,2.4),("A",21,3.6,4.4),("A",22,0.0,4.6),("A",23,3.2,6.0),
      ("B",1,0.6,4.2),("B",2,0.6,4.4),("B",3,0.0,4.2),
      ("B",4,0.6,4.4),("B",4,14.5,7.5),   # chain: Dian Keto, Magic Jammer, Seven Tools, resolves backwards
      ("B",5,1.0,3.8),("B",5,11.6,3.6),   # Summon answered by Bottomless Trap Hole: the banish portal
      ("B",6,2.4,4.4),("B",7,2.4,3.6)]
os.makedirs(os.path.join(HERE,"_cut"),exist_ok=True);parts=[]
for n,(v,sc,off,ln) in enumerate(CUTS):
    m=A if v=="A" else B
    start=(0 if sc is None else m["scene_start"][sc])+off
    out=os.path.join(HERE,"_cut",f"{n:02d}.mp4")
    vf=f"fade=t=in:st=0:d=0.1,fade=t=out:st={ln-0.12:.2f}:d=0.12"
    af=f"afade=t=in:st=0:d=0.05,afade=t=out:st={ln-0.12:.2f}:d=0.12"   # the sound fades with the picture (no clicks between the cuts)
    subprocess.run([FF,"-y","-loglevel","error","-ss",f"{start:.2f}","-t",f"{ln:.2f}","-i",os.path.join(HERE,f"demo-{v}.mp4"),"-vf",vf,"-af",af,"-r","30","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-ar","48000",out],check=True)
    parts.append(out)
lst=os.path.join(HERE,"_cut","list.txt");open(lst,"w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
subprocess.run([FF,"-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy","-movflags","+faststart",os.path.join(HERE,"demo-trailer.mp4")],check=True)
print(sum(c[3] for c in CUTS),"seconds")
