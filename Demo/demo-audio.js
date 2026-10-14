(()=>{if(!window.AudioContext||!window.MediaRecorder)return;
 const oc=AudioNode.prototype.connect;window.__aud={chunks:[],t0:null,rec:null};
 AudioNode.prototype.connect=function(dst,...a){const r=oc.call(this,dst,...a);
  try{if(dst&&dst===this.context.destination){const c=this.context;
    if(!c.__msd){c.__msd=c.createMediaStreamDestination();const mr=new MediaRecorder(c.__msd.stream,{mimeType:"audio/webm;codecs=opus",audioBitsPerSecond:160000});
      mr.ondataavailable=e=>{if(e.data.size)__aud.chunks.push(e.data)};mr.start(1000);__aud.rec=mr;__aud.t0=Date.now()/1000}
    oc.call(this,c.__msd)}}catch(e){}
  return r};
 window.__audStop=()=>new Promise(res=>{const mr=__aud.rec;if(!mr)return res(null);
  mr.onstop=async()=>{const u=new Uint8Array(await new Blob(__aud.chunks,{type:"audio/webm"}).arrayBuffer());let s="";for(let i=0;i<u.length;i+=32768)s+=String.fromCharCode.apply(null,u.subarray(i,i+32768));res({t0:__aud.t0,b64:btoa(s)})};mr.stop()});
})();
