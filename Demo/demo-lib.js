// Helpers for the demo video: they call the app's own functions, so every animation is the real one.
window.D=(()=>{
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const D={sleep};
  // the tap look is available at once (also on the start screen, before D.init)
  if(!document.getElementById("demotapcss")){const st=document.createElement("style");st.id="demotapcss";
      st.textContent=".demotap{position:absolute;left:50%;top:50%;width:40px;height:40px;margin:-20px 0 0 -20px;border-radius:50%;border:3px solid #fff;background:#ffffff59;box-shadow:0 0 12px #fff;pointer-events:none;z-index:50;animation:demotap .6s ease-out forwards}@keyframes demotap{0%{transform:scale(.3);opacity:1}60%{opacity:.9}100%{transform:scale(1.5);opacity:0}}.demopress{scale:.93!important;filter:brightness(1.45) drop-shadow(0 0 5px #e8c36acc)!important}";
      document.head.appendChild(st)}
  D.init=async()=>{await cards();S.noAskAct=true;S.noAskSum=true; // the chain questions are shown in their own scenes

    if(!document.getElementById("democap")){const c=document.createElement("div");c.id="democap";
      c.style.cssText="position:fixed;top:5px;left:50%;transform:translateX(-50%);max-width:94vw;z-index:400;background:#000d;color:#fff;font:700 13px/1.25 system-ui,sans-serif;padding:5px 12px;border-radius:14px;border:1.5px solid #e8c36a;text-align:center;pointer-events:none;opacity:0;transition:opacity .25s";document.body.appendChild(c)}};
  D.cap=t=>{const c=document.getElementById("democap");if(!t){c.style.opacity=0;return}c.textContent=t;c.style.opacity=1};
  D.card=n=>{const c=CARDS.find(x=>x.name===n);if(!c)throw new Error("card missing: "+n);return c};
  D.touch=async(el,hold=200)=>{if(!el)return;const r=el.getBoundingClientRect(),dot=document.createElement("span");dot.className="demotap";
    const old=el.style.position;if(getComputedStyle(el).position==="static")el.style.position="relative";el.appendChild(dot);el.classList.add("demopress");
    try{el.dispatchEvent(new PointerEvent("pointerdown",{bubbles:true,clientX:r.left+r.width/2,clientY:r.top+r.height/2}))}catch(e){}
    await sleep(hold);el.classList.remove("demopress");setTimeout(()=>{dot.remove();el.style.position=old},450)};
  D.close=()=>{try{if(dlg.open)dlg.close()}catch(e){}};
  D.btn=re=>[...document.querySelectorAll("dialog[open] button")].find(b=>re.test(b.textContent));
  D.click=async(re,wait=700)=>{const b=D.btn(re);if(!b)throw new Error("no button "+re);await sleep(wait);await D.touch(b);b.click()};
  D.tap=async(p,i,row="mon")=>{const e=document.querySelector(`.slot[data-p="${p}"][data-i="${i}"][data-row="${row}"]`);if(!e)throw new Error("no slot "+p+i);await D.touch(e,160);e.dispatchEvent(new MouseEvent("click",{bubbles:true}))};
  D.dlgFor=p=>{DLGP=p};
  D.stEntry=(n,pos)=>{const c=D.card(n);return{name:c.name,kind:/Trap/.test(c.type)?"trap":"spell",type:c.type,pos:pos||"UP",id:c.id,desc:c.desc,setT:S.tc}};
  D.freeSt=p=>[1,2,3].find(k=>!S.st[p][k]);
  D.phase=async(n=1,wait=450)=>{for(let k=0;k<n;k++){await D.touch($("phase"),150);phaseClick();await sleep(wait);D.close()}};
  // a Spell from the hand: shown for a moment, then it goes to the Graveyard (skeleton card flies)
  D.cast=async(p,n,show=900)=>{const k=D.freeSt(p),e=D.stEntry(n);await D.touch(stEl(p,k));S.st[p][k]=e;render();await sleep(show);
    flyToPile(stEl(p,k).getBoundingClientRect(),e,p,"gy");S.st[p][k]=null;sendTo(p,"gy",e,true);render();await sleep(1500)};
  D.counter=async(m,n=1,gap=450)=>{for(let k=0;k<n;k++){m.cnt=(m.cnt||0)+1;render();await sleep(gap)}};
  // Normal Summon / Set straight onto the board (dust)
  D.normal=async(p,zone,n,pos="ATK")=>{await D.touch(monEl(p,zone));placeMon(p,zone,D.card(n),pos==="FD"?"FD":pos,pos==="FD"?"set":"normal");S.ns=true;render();await sleep(900)};
  // Special Summon window: opens the real pop-up, then presses the button
  D.summon=async(p,zone,n,opts,btn,show=900)=>{await D.touch(monEl(p,zone));DLGP=p;summonDialog(p,zone,D.card(n),opts||{});await sleep(show);return btn};
  D.press=async(re,wait=500)=>{await D.click(re,wait)};
  // Field Spell / Equip Spell: real activation flow (tap the target, then Apply)
  D.field=async(p,n,show=700)=>{const e=D.stEntry(n,"FD");await D.touch(fieldEl(p));putZone(p,0,"field",e);render();DLGP=p;activateIn(p,0,"field",e,()=>{});await sleep(show);await D.click(/Apply card/,600);await sleep(1400)};
  D.equip=async(p,n,tp,ti,show=500)=>{const k=D.freeSt(p),e=D.stEntry(n,"FD");await D.touch(stEl(p,k));putZone(p,k,"st",e);render();DLGP=p;activateIn(p,k,"st",e,()=>{});await sleep(900);await D.tap(tp,ti);await sleep(show+500);if(D.btn(/Apply equip card/))await D.click(/Apply equip card/,700);await sleep(1500)}; // an Equip is applied at once (no pop-up)
  D.attack=async(p,i,q,k)=>{await D.touch(monEl(p,i));DLGP=p;attackDialog(p,i);await sleep(900);if(k<0){const b=document.getElementById("pickd")||D.btn(/Direct attack/);await sleep(300);await D.touch(b);b.click()}else await D.tap(q,k);await sleep(900);await D.click(/No, continue/,800);await sleep(300);await D.click(/Apply result/,900)};
  D.pick=async(re,wait=700)=>{const d=[...document.querySelectorAll("dialog[open] .res div")].find(x=>re.test(x.textContent));if(!d)throw new Error("no entry "+re);await sleep(wait);await D.touch(d);d.click()};
  D.setSt=async(p,n)=>{const k=D.freeSt(p);await D.touch(stEl(p,k));S.st[p][k]=D.stEntry(n,"FD");render();await sleep(900);return k};
  D.trapEquip=async(p,n,tp,ti)=>{const k=S.st[p].findIndex(e=>e&&e.name===n),e=S.st[p][k];await D.touch(stEl(p,k));DLGP=p;activateIn(p,k,"st",e,()=>{});await sleep(900);await D.tap(tp,ti);await sleep(1100);if(D.btn(/Apply equip card/))await D.click(/Apply equip card/,700);await sleep(1600);D.close()};
  D.src=async(key,wait=600)=>{const d=document.querySelector(`dialog[open] [data-s="${key}"]`);if(!d)throw new Error("no source "+key);await sleep(wait);await D.touch(d);d.click()};
  D.stat=(p,i)=>stats(p,i);
  return D;
})();
