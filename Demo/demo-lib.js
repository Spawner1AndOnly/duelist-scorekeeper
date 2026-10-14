// Helpers for the demo video: they call the app's own functions, so every animation is the real one.
window.D=(()=>{
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const D={sleep};
  D.init=async()=>{await cards();
    if(!document.getElementById("democap")){const c=document.createElement("div");c.id="democap";
      c.style.cssText="position:fixed;top:5px;left:50%;transform:translateX(-50%);max-width:94vw;z-index:400;background:#000d;color:#fff;font:700 13px/1.25 system-ui,sans-serif;padding:5px 12px;border-radius:14px;border:1.5px solid #e8c36a;text-align:center;pointer-events:none;opacity:0;transition:opacity .25s";document.body.appendChild(c)}};
  D.cap=t=>{const c=document.getElementById("democap");if(!t){c.style.opacity=0;return}c.textContent=t;c.style.opacity=1};
  D.card=n=>{const c=CARDS.find(x=>x.name===n);if(!c)throw new Error("card missing: "+n);return c};
  D.close=()=>{try{if(dlg.open)dlg.close()}catch(e){}};
  D.btn=re=>[...document.querySelectorAll("dialog[open] button")].find(b=>re.test(b.textContent));
  D.click=async(re,wait=700)=>{const b=D.btn(re);if(!b)throw new Error("no button "+re);await sleep(wait);b.click()};
  D.tap=(p,i,row="mon")=>{const e=document.querySelector(`.slot[data-p="${p}"][data-i="${i}"][data-row="${row}"]`);if(!e)throw new Error("no slot "+p+i);e.dispatchEvent(new MouseEvent("click",{bubbles:true}))};
  D.dlgFor=p=>{DLGP=p};
  D.stEntry=(n,pos)=>{const c=D.card(n);return{name:c.name,kind:/Trap/.test(c.type)?"trap":"spell",type:c.type,pos:pos||"UP",id:c.id,desc:c.desc,setT:S.tc}};
  D.freeSt=p=>[1,2,3].find(k=>!S.st[p][k]);
  D.phase=async(n=1,wait=450)=>{for(let k=0;k<n;k++){phaseClick();await sleep(wait);D.close()}};
  // a Spell from the hand: shown for a moment, then it goes to the Graveyard (skeleton card flies)
  D.cast=async(p,n,show=900)=>{const k=D.freeSt(p),e=D.stEntry(n);S.st[p][k]=e;render();await sleep(show);
    flyToPile(stEl(p,k).getBoundingClientRect(),e,p,"gy");S.st[p][k]=null;sendTo(p,"gy",e,true);render();await sleep(1500)};
  D.counter=async(m,n=1,gap=450)=>{for(let k=0;k<n;k++){m.cnt=(m.cnt||0)+1;render();await sleep(gap)}};
  // Normal Summon / Set straight onto the board (dust)
  D.normal=async(p,zone,n,pos="ATK")=>{placeMon(p,zone,D.card(n),pos==="FD"?"FD":pos,pos==="FD"?"set":"normal");S.ns=true;render();await sleep(900)};
  // Special Summon window: opens the real pop-up, then presses the button
  D.summon=async(p,zone,n,opts,btn,show=900)=>{DLGP=p;summonDialog(p,zone,D.card(n),opts||{});await sleep(show);return btn};
  D.press=async(re,wait=500)=>{await D.click(re,wait)};
  // Field Spell / Equip Spell: real activation flow (tap the target, then Apply)
  D.field=async(p,n,show=700)=>{const e=D.stEntry(n,"FD");putZone(p,0,"field",e);render();DLGP=p;activateIn(p,0,"field",e,()=>{});await sleep(show);await D.click(/Apply card/,600);await sleep(1400)};
  D.equip=async(p,n,tp,ti,show=500)=>{const k=D.freeSt(p),e=D.stEntry(n,"FD");putZone(p,k,"st",e);render();DLGP=p;activateIn(p,k,"st",e,()=>{});await sleep(900);D.tap(tp,ti);await sleep(show+500);await D.click(/Apply equip card/,700);await sleep(1500)};
  D.attack=async(p,i,q,k)=>{DLGP=p;attackDialog(p,i);await sleep(900);if(k<0)await D.click(/Direct attack/,300);else D.tap(q,k);await sleep(900);await D.click(/No, continue/,800);await sleep(300);await D.click(/Apply result/,900)};
  D.pick=async(re,wait=700)=>{const d=[...document.querySelectorAll("dialog[open] .res div")].find(x=>re.test(x.textContent));if(!d)throw new Error("no entry "+re);await sleep(wait);d.click()};
  D.setSt=async(p,n)=>{const k=D.freeSt(p);S.st[p][k]=D.stEntry(n,"FD");render();await sleep(900);return k};
  D.trapEquip=async(p,n,tp,ti)=>{const k=S.st[p].findIndex(e=>e&&e.name===n),e=S.st[p][k];DLGP=p;activateIn(p,k,"st",e,()=>{});await sleep(900);D.tap(tp,ti);await sleep(1100);await D.click(/Apply equip card/,700);await sleep(1600);D.close()};
  D.stat=(p,i)=>stats(p,i);
  return D;
})();
