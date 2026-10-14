import sys,os,glob,subprocess,shutil
from PIL import Image
sys.path.insert(0,'.')
from recorder import FF
mp4=sys.argv[1];t0=float(sys.argv[2]);step=float(sys.argv[3]);n=int(sys.argv[4]);out=sys.argv[5];scale=int(sys.argv[6]) if len(sys.argv)>6 else 4
fr="_fr";shutil.rmtree(fr,ignore_errors=True);os.makedirs(fr)
ims=[]
for k in range(n):
    t=t0+k*step
    subprocess.run([FF,"-y","-loglevel","error","-ss",f"{t:.2f}","-i",mp4,"-frames:v","1","-q:v","3",f"{fr}/{k:02d}.jpg"],check=True)
    ims.append(Image.open(f"{fr}/{k:02d}.jpg").convert("RGB"))
w,h=ims[0].size;cw,ch=w//scale,h//scale;cols=min(n,6);rows=(n+cols-1)//cols
sh=Image.new("RGB",(cw*cols,ch*rows))
for i,im in enumerate(ims):sh.paste(im.resize((cw,ch)),((i%cols)*cw,(i//cols)*ch))
sh.save(out);shutil.rmtree(fr,ignore_errors=True);print(sh.size)
