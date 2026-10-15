(()=>{if(!window.AudioContext||!window.MediaRecorder)return;
 // two recordings: 'fx' = the sound effects (compressor -> speakers), 'mus' = the background music (its own gain -> speakers)
 // kept apart so the trailer can lay one continuous music track under its cuts
 const oc=AudioNode.prototype.connect;window.__aud={fx:{chunks:[],t0:null,rec:null},mus:{chunks:[],t0:null,rec:null}};
 AudioNode.prototype.connect=function(dst,...a){const r=oc.call(this,dst,...a);
  try{if(dst&&dst===this.context.destination){const c=this.context,k=this instanceof GainNode?"mus":"fx",A=__aud[k];
    c.__msd=c.__msd||{};
    if(!c.__msd[k]){c.__msd[k]=c.createMediaStreamDestination();const mr=new MediaRecorder(c.__msd[k].stream,{mimeType:"audio/webm;codecs=opus",audioBitsPerSecond:160000});
      mr.ondataavailable=e=>{if(e.data.size)A.chunks.push(e.data)};mr.start(1000);A.rec=mr;A.t0=Date.now()/1000}
    oc.call(this,c.__msd[k])}}catch(e){}
  return r};
 const stop1=A=>new Promise(res=>{const mr=A.rec;if(!mr)return res(null);
  mr.onstop=async()=>{const u=new Uint8Array(await new Blob(A.chunks,{type:"audio/webm"}).arrayBuffer());let s="";for(let i=0;i<u.length;i+=32768)s+=String.fromCharCode.apply(null,u.subarray(i,i+32768));res({t0:A.t0,b64:btoa(s)})};mr.stop()});
 window.__audStop=async()=>({fx:await stop1(__aud.fx),mus:await stop1(__aud.mus)});
})();
