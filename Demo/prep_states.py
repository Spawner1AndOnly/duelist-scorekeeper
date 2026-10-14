# Builds the two saved duel states used by the demo ("Continue previous duel") with the app's own functions.
import time,json,sys
from playwright.sync_api import sync_playwright
KEY="ygoref.v2"
JS_A=r"""async()=>{
  const all=await cards();const f=n=>{const c=all.find(x=>x.name===n);if(!c)throw new Error("card missing: "+n);return c};
  S=fresh(8000,5);S.view="2p";S.noAskAct=S.noAskSum=true;
  const spell=(n,pos)=>{const c=f(n);return{name:c.name,kind:/Trap/.test(c.type)?"trap":"spell",type:c.type,pos:pos||"UP",id:c.id,desc:c.desc,setT:1}};
  // Player 1: Battle Ox (Normal Summoned turn 1), Sogen, Mystical Space Typhoon Set on turn 1
  placeMon(0,2,f("Battle Ox"),"ATK","normal");S.mon[0][2].sumT=1;
  const sg=spell("Forest");sg.eff=parseField(sg.desc);S.field[0]=sg;
  S.st[0][1]=spell("Mystical Space Typhoon","FD");
  // Player 2: Cyber End Dragon (Fusion Summoned turn 2, Defense), Silent Magician LV4 (turn 2), Wasteland
  placeMon(1,1,f("Cyber End Dragon"),"DEF","special");S.mon[1][1].sumT=2;
  placeMon(1,3,f("Silent Magician LV4"),"ATK","normal");S.mon[1][3].sumT=2;
  const wl=spell("Wasteland");wl.eff=parseField(wl.desc);S.field[1]=wl;
  const gy=n=>{const c=f(n);return{name:c.name,id:c.id,type:c.type}};
  S.gy[1]=[gy("Cyber Dragon"),gy("Cyber Dragon"),gy("Cyber Dragon"),gy("Polymerization")];
  S.tc=3;S.turn=0;S.ph=0;S.sub=0;S.ns=false;S.startPlayer=0;
  S.log=["Turn 1: Player 1 Normal Summoned Battle Ox and activated Forest","Turn 2: Player 2 Fusion Summoned Cyber End Dragon (3 Cyber Dragons)","Turn 2: Player 2 Normal Summoned Silent Magician LV4 and activated Wasteland"];
  S.mon[1]=S.mon[1].map(x=>x);
  save();return JSON.stringify(S)}"""
JS_B=r"""async()=>{
  const all=await cards();const f=n=>{const c=all.find(x=>x.name===n);if(!c)throw new Error("card missing: "+n);return c};
  S=fresh(8000,5);S.view="2p";S.noAskAct=S.noAskSum=true;
  placeMon(0,1,f("Junk Synchron"),"ATK","normal");placeMon(0,2,f("Speed Warrior"),"ATK","special");placeMon(0,3,f("Beaver Warrior"),"ATK","special");
  for(const k of [1,2,3])S.mon[0][k].sumT=3;
  const gy=n=>{const c=f(n);return{name:c.name,id:c.id,type:c.type}};
  S.gy[0]=[gy("Battle Ox")];
  placeMon(1,2,f("Giant Red Seasnake"),"DEF","normal");S.mon[1][2].sumT=4;
  S.tc=5;S.turn=0;S.ph=0;S.sub=0;S.ns=false;S.startPlayer=0;
  S.log=["Bonus: a few more summons"];
  save();return JSON.stringify(S)}"""
with sync_playwright() as p:
    b=p.chromium.launch(channel="chrome",headless=True)
    for name,js in (("A",JS_A),("B",JS_B)):
        pg=b.new_context(viewport={"width":390,"height":844}).new_page();errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.goto("http://localhost:8123/?x="+str(time.time()));pg.wait_for_timeout(1200)
        pg.evaluate("document.getElementById('splash').hidden=true")
        st=pg.evaluate(js);pg.wait_for_timeout(400)
        raw=pg.evaluate(f"localStorage.getItem('{KEY}')")
        open(f"state-{name}.json","w",encoding="utf-8").write(raw);print(name,len(raw),errs)
    b.close()
