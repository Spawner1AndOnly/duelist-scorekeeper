import base64,time,os,shutil,subprocess,glob
import imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe()

class Recorder:
    """Screen recording through Chrome's own screencast (no extra downloads): frames + timestamps -> constant 30 fps mp4."""
    def __init__(self,page,ctx,quality=88,max_w=780,max_h=1688):
        self.page=page;self.frames=[];self.cdp=ctx.new_cdp_session(page);self.q=quality;self.mw=max_w;self.mh=max_h;self.t0=None
        self.cdp.on("Page.screencastFrame",self._on)
    def _on(self,ev):
        ts=ev["metadata"]["timestamp"]
        if self.t0 is None:self.t0=ts
        self.frames.append((ts-self.t0,base64.b64decode(ev["data"])))
        try:self.cdp.send("Page.screencastFrameAck",{"sessionId":ev["sessionId"]})
        except Exception:pass
    def start(self):
        self.cdp.send("Page.startScreencast",{"format":"jpeg","quality":self.q,"maxWidth":self.mw,"maxHeight":self.mh,"everyNthFrame":1})
    def stop(self):
        try:self.cdp.send("Page.stopScreencast")
        except Exception:pass
    def save(self,out,fps=30,tail=0.6,work=None):
        work=work or (os.path.dirname(out)+"/_frames");shutil.rmtree(work,ignore_errors=True);os.makedirs(work)
        fr=self.frames
        if not fr:raise RuntimeError("no frames")
        end=fr[-1][0]+tail;n=int(end*fps)+1;j=0
        for k in range(n):
            t=k/fps
            while j+1<len(fr) and fr[j+1][0]<=t:j+=1
            with open(f"{work}/{k:05d}.jpg","wb") as f:f.write(fr[j][1])
        subprocess.run([FF,"-y","-loglevel","error","-framerate",str(fps),"-i",f"{work}/%05d.jpg","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-movflags","+faststart","-vf","scale=trunc(iw/2)*2:trunc(ih/2)*2",out],check=True)
        shutil.rmtree(work,ignore_errors=True)
        return len(fr),n,end

# Sound: demo-audio.js (init script) taps every Web Audio connection to the speakers into a MediaRecorder; __audStop() returns {t0 (epoch s), b64 webm}
AUDIO_JS=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"demo-audio.js"),encoding="utf-8").read()
def mux(video,aud,t0_video,out,dur):
    """aud = result of __audStop() = {fx, mus}; each track starts its t0-t0_video seconds into the video; dur = video length (s).
    out = video with effects + music mixed; next to it <name>.fx.m4a = the effects alone, same timing (for the trailer)."""
    tr=[(k,a) for k,a in (("fx",(aud or {}).get("fx")),("mus",(aud or {}).get("mus"))) if a]
    if not tr:os.replace(video,out);return "no audio"
    ins=[];flt=[];info=[]
    for n,(k,a) in enumerate(tr):
        wa=f"{video}.{k}.webm";open(wa,"wb").write(base64.b64decode(a["b64"]));ins+=["-i",wa]
        d=max(0,int(round((a["t0"]-t0_video)*1000)));info.append(f"{k} {d} ms")
        flt.append(f"[{n+1}:a]adelay={d}:all=1,apad=whole_dur={dur:.3f},atrim=0:{dur:.3f}[{k}]")
    labels="".join(f"[{k}]" for k,_ in tr)
    mix=f"{labels}amix=inputs={len(tr)}:normalize=0[a]" if len(tr)>1 else f"{labels}anull[a]"
    fc=";".join(flt)+";"+mix
    subprocess.run([FF,"-y","-loglevel","error","-i",video]+ins+["-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","160k","-ar","48000","-t",f"{dur:.3f}","-movflags","+faststart",out],check=True)
    if tr[0][0]=="fx":   # the effects alone, for the trailer
        subprocess.run([FF,"-y","-loglevel","error"]+ins[:2]+["-filter_complex",flt[0].replace("[1:a]","[0:a]"),"-map","[fx]","-c:a","aac","-b:a","160k","-ar","48000",out.replace(".mp4",".fx.m4a")],check=True)
    for k,_ in tr:os.remove(f"{video}.{k}.webm")
    os.remove(video);return "audio: "+", ".join(info)
