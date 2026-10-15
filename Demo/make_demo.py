"""Records the demo video of the Duelist Scorekeeper with Chrome + Playwright (no extra browser download).
Usage:  python make_demo.py A      -> Demo/demo-A.mp4  (turns 3-5, the Blue-Eyes story)
        python make_demo.py B      -> Demo/demo-B.mp4  (bonus: Synchro, Link, pile -> zone, shield, direct attack)
        python make_demo.py all    -> both + demo.mp4 (joined)
Needs: the app running on http://localhost:8123 (python -m http.server 8123 in the project folder), state-A.json / state-B.json (prep_states.py)."""
import sys,os,time,json,subprocess,shutil
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from playwright.sync_api import sync_playwright
from recorder import Recorder,FF,AUDIO_JS,mux
URL="http://localhost:8123/"
LIB=open(os.path.join(HERE,"demo-lib.js"),encoding="utf-8").read()
KEY="ygoref.v2"

SCENE_A=[
# ---------------- Turn 3: Player 1 ----------------
r"""D.cap("Continue previous duel – Turn 3, Player 1. Both Field Spells fade in.");await D.sleep(2600);""",
r"""D.cap("Draw Phase: Player 1 draws, so Silent Magician LV4 gets a Spell Counter (+500 ATK)");await D.sleep(900);
 await D.counter(S.mon[1][3],1,900);""",
r"""D.cap("Main Phase 1: Graceful Charity (draw 3) = 3 more counters");await D.phase(2,350);
 await D.cast(0,"Graceful Charity");await D.counter(S.mon[1][3],3,550);""",
r"""D.cap("Upstart Goblin: draw 1 (5th counter) and the opponent gains 1000 LP");
 await D.cast(0,"Upstart Goblin");changeLP(1,1000);await D.sleep(900);await D.counter(S.mon[1][3],1,900);await D.sleep(900);""",
r"""D.cap("Normal Summon Beaver Warrior, then Xyz Summon Number 39: Utopia (2 Level 4 monsters)");
 await D.normal(0,3,"Beaver Warrior");
 await D.summon(0,1,"Number 39: Utopia",{mat:{field:[2,3],hand:0}});
 await D.press(/Special Summon \(ATK\)/,300);await D.sleep(3300);D.close();await D.sleep(500);""",
r"""D.cap("Mystical Space Typhoon (Set last turn): it flips and destroys Wasteland");
 await D.sleep(600);await D.touch(stEl(0,1));S.st[0][1].pos="UP";render();await D.sleep(1700);
 {const fe=fieldEl(1);flyToPile(fe.getBoundingClientRect(),S.field[1],1,"gy");sendTo(1,"gy",S.field[1],true);S.field[1]=null;render();}
 await D.sleep(2200);
 {const e=S.st[0][1],el=stEl(0,1);flyToPile(el.getBoundingClientRect(),e,0,"gy");S.st[0][1]=null;sendTo(0,"gy",e,true);render();}
 await D.sleep(2000);""",
r"""D.cap("Battle: Utopia (2500 ATK) attacks Cyber End Dragon in Defense (2800 DEF) – the shield holds");
 await D.phase(1,500);await D.attack(0,1,1,1);await D.sleep(2800);D.close();""",
r"""D.cap("End of turn 3");await D.phase(3,500);await D.sleep(800);""",
# ---------------- Turn 4: Player 2 ----------------
r"""D.cap("Turn 4 – Player 2. Draw and Standby Phase");await D.phase(1,600);D.close();await D.sleep(500);""",
r"""D.cap("Silent Magician LV4 (5 counters) goes to the Graveyard; Silent Magician LV8 is Special Summoned");
 await D.touch(monEl(1,3));removeMon(1,3);render();await D.sleep(1600);
 await D.summon(1,3,"Silent Magician LV8",{});await D.press(/Special Summon \(ATK\)/,300);await D.sleep(1200);D.close();await D.sleep(600);""",
r"""D.cap("Main Phase 1: Fusion Summon Cyberdark Dragon (3 cards from the hand)");await D.phase(1,500);
 await D.cast(1,"Polymerization");
 await D.summon(1,2,"Cyberdark Dragon",{mat:{field:[],hand:3}});await D.press(/Special Summon \(ATK\)/,300);await D.sleep(3300);D.close();await D.sleep(400);""",
r"""D.cap("Fusion Summon Cyberdark End Dragon from the field (3800 DEF) in Defense Position");
 await D.cast(1,"Polymerization");
 await D.summon(1,4,"Cyberdark End Dragon",{mat:{field:[2,1],hand:0}});await D.press(/Special Summon \(DEF\)/,300);await D.sleep(3300);D.close();await D.sleep(400);""",
r"""D.cap("Normal Summon Mystic Tomato");await D.normal(1,0,"Mystic Tomato");D.close();await D.sleep(600);
 D.cap("End of turn 4");await D.phase(4,450);await D.sleep(700);""",
# ---------------- Turn 5: Player 1 ----------------
r"""D.cap("Turn 5 – Player 1");await D.phase(2,550);D.close();await D.sleep(300);""",
r"""D.cap("Change of Heart: Player 1 takes control of Mystic Tomato until the End Phase");
 await D.cast(0,"Change of Heart");await D.touch(monEl(1,0));const j=moveCtl(1,0,0,{ep:true});addLog("Player 1 took control of Mystic Tomato until the End Phase");render();await D.sleep(2000);""",
r"""D.cap("Field Spell Mountain replaces Forest: Mystic Tomato loses its bonus, Dragons gain +200");
 await D.field(0,"Mountain");await D.sleep(900);D.close();""",
r"""D.cap("Tribute Summon Blue-Eyes White Dragon (Level 8 = 2 Tributes: Utopia + Mystic Tomato)");
 {const tz=S.mon[0].findIndex((m,k)=>m&&m.name==="Mystic Tomato"),uz=S.mon[0].findIndex(m=>m&&m.name==="Number 39: Utopia");
  await D.touch(monEl(0,2));DLGP=0;summonDialog(0,2,D.card("Blue-Eyes White Dragon"),{tr:{own:[uz,tz],opp:[],lava:[]}});}
 await D.sleep(1300);await D.click(/^Normal Summon$/,300);await D.sleep(1800);D.close();await D.sleep(600);""",
r"""D.cap("Equip Black Pendant to Blue-Eyes: +500 ATK = 3700 ATK");
 await D.equip(0,"Black Pendant",0,2);await D.sleep(900);D.close();""",
r"""D.cap("Battle: Blue-Eyes (3700 ATK) attacks Silent Magician LV8 (3500 ATK)");
 await D.phase(1,500);await D.attack(0,2,1,3);await D.sleep(3200);D.close();""",
r"""D.cap("Silent Magician LV8 is destroyed. Player 2 takes 200 damage.");await D.sleep(2200);
 D.cap("Main Phase 2: Set Tyrant Wing (a Trap that equips and gives up to 2 attacks)");await D.phase(1,500);await D.setSt(0,"Tyrant Wing");await D.sleep(500);
 D.cap("End of turn 5");await D.phase(2,500);await D.sleep(500);""",
# ---------------- Settings: switch the music twice ----------------
r"""D.cap("Settings: switch the background music");await D.sleep(1500);D.cap();   // the menu covers the caption: 'Now playing' tells the story
 await D.touch($("btnMenu"));$("btnMenu").onclick();await D.sleep(1600);
 await D.click(/⏭/,300);await D.sleep(4800);
 await D.click(/⏭/,300);await D.sleep(5200);D.close();await D.sleep(400);""",
# ---------------- Turn 6: Player 2 passes, Turn 7: Player 1 ----------------
r"""D.cap("Turn 6 – Player 2 passes");await D.phase(6,380);D.close();await D.sleep(300);""",
r"""D.cap("Turn 7 – Player 1: Blue-Eyes (3700 ATK) attacks Cyberdark End Dragon (3800 DEF) – blocked");await D.phase(3,450);D.close();
 await D.attack(0,2,1,4);await D.sleep(2800);D.close();""",
r"""D.cap("Flip Tyrant Wing: Blue-Eyes gets +400 (4100 ATK) and may attack a second time");
 await D.trapEquip(0,"Tyrant Wing",0,2);await D.sleep(500);""",
r"""D.cap("Second attack: 4100 ATK breaks the 3800 DEF – Cyberdark End Dragon is destroyed");
 await D.attack(0,2,1,4);await D.sleep(3200);D.close();D.cap("Demo: the hands are not tracked by the app");await D.sleep(2000);D.cap();""",
]

SCENE_B=[
r"""D.cap("Bonus: more summons and battles");await D.sleep(1800);""",
r"""D.cap("Synchro Summon: Junk Synchron (Tuner) + Speed Warrior = Junk Warrior");await D.phase(2,350);
 await D.summon(0,0,"Junk Warrior",{mat:{field:[1,2],hand:0}});await D.press(/Special Summon \(ATK\)/,300);await D.sleep(3000);D.close();await D.sleep(500);""",
r"""D.cap("Link Summon: Link Spider (1 Normal Monster) in an Extra Monster Zone");
 await D.touch(monEl(0,1));DLGP=0;summonDialog(0,1,D.card("Link Spider"),{mat:{field:[3],hand:0}});await D.sleep(1000);await D.click(/EMZ left/,200);await D.sleep(600);
 await D.press(/Special Summon \(ATK\)/,300);await D.sleep(3000);D.close();await D.sleep(600);""",
r"""D.cap("Monster Reborn: Special Summon Battle Ox from the Graveyard – it flies from the pile to its zone");await D.cast(0,"Monster Reborn");
 {const gz=S.mon[0].findIndex((m,k)=>k<5&&!m);await D.touch(pileBtn(0,"gy"));pileDialog(0,"gy");await D.sleep(1000);}
 await D.pick(/Battle Ox/,300);await D.sleep(900);await D.click(/Special Summon \(ATK\)/,300);await D.sleep(2200);D.close();""",
r"""D.cap("Chains: Player 1 activates Dian Keto the Cure Master – Player 2 may respond");
 S.noAskAct=false;S.st[1][1]=D.stEntry("Magic Jammer","FD");S.st[1][1].setT=1;S.st[0][3]=D.stEntry("Seven Tools of the Bandit","FD");S.st[0][3].setT=1;render();await D.sleep(1000);
 {await D.touch(stEl(0,1));const e=D.stEntry("Dian Keto the Cure Master","FD");putZone(0,1,"st",e);render();DLGP=0;activateIn(0,1,"st",e,()=>{});}await D.sleep(1600);
 D.cap("Player 2 answers with Magic Jammer: negate the activation (the window turns to Player 2)");
 await D.click(/^Yes/,900);await D.click(/Trap Card/,600);await D.src("st:1",600);await D.click(/Negate the activation/,700);await D.click(/^Activate$/,800);
 D.cap("Player 1 chains Seven Tools of the Bandit (pay 1000 LP): negate Magic Jammer");
 await D.click(/^Yes/,1400);await D.click(/Trap Card/,600);await D.src("st:3",600);await D.click(/Negate the activation/,700);
 await D.click(/Life Points/,600);$("el1").value="-1000";await D.click(/^Add$/,700);await D.click(/^Activate$/,800);
 D.cap("Player 2 passes: the chain resolves backwards – Magic Jammer is negated, Dian Keto gives +1000 LP");
 await D.click(/^No/,1500);await D.sleep(2600);await D.click(/OK/,1800);await D.sleep(2600);S.noAskAct=true;""",
r"""D.cap("Summons can be answered too: Player 1 Normal Summons Gemini Elf");
 S.noAskSum=false;S.st[1][3]=D.stEntry("Bottomless Trap Hole","FD");S.st[1][3].setT=1;render();await D.sleep(700);
 await D.touch(monEl(0,2));DLGP=0;summonDialog(0,2,D.card("Gemini Elf"),{});await D.sleep(1000);await D.click(/^Normal Summon$/,400);await D.sleep(1900);
 D.cap("Player 2 answers with Bottomless Trap Hole: Gemini Elf is banished");
 await D.click(/^Yes/,900);await D.click(/Trap Card/,600);await D.src("st:3",600);await D.click(/Destroy a monster/,700);
 dlg.querySelector('input[name="tg"][value="0:2"]').checked=true;$("eb").checked=true;await D.sleep(500);await D.click(/^Add$/,600);await D.click(/^Activate$/,800);
 await D.click(/^No/,1400);await D.sleep(3200);await D.click(/OK/,1600);await D.sleep(600);S.noAskSum=true;""",
r"""D.cap("Battle: Junk Warrior (2300 ATK) attacks Giant Red Seasnake in Defense (800 DEF): the shield breaks");
 await D.phase(1,500);await D.attack(0,0,1,2);await D.sleep(3000);D.close();""",
r"""D.cap("Direct attack: Link Spider attacks the empty field");
 {const li=S.mon[0].findIndex(m=>m&&m.name==="Link Spider");await D.attack(0,li,1,-1);}await D.sleep(3000);D.close();""",
r"""D.cap("Banish a card from the Graveyard (portal)");
 await D.touch(pileBtn(0,"gy"));pileDialog(0,"gy");await D.sleep(900);await D.pick(/./,300);await D.sleep(900);
 await D.click(/Banished/,300);await D.sleep(2500);D.close();D.cap();""",
]

def run(which,scenes,out):
    state=open(os.path.join(HERE,f"state-{which}.json"),encoding="utf-8").read()
    with sync_playwright() as p:
        b=p.chromium.launch(channel="chrome",headless=True,args=["--force-device-scale-factor=2","--autoplay-policy=no-user-gesture-required"])
        ctx=b.new_context(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True)
        ctx.add_init_script(f"try{{if(!sessionStorage.getItem('demoSeed')){{localStorage.setItem({json.dumps(KEY)},{json.dumps(state)});sessionStorage.setItem('demoSeed','1');localStorage.setItem('ygoref-mv','0.8')}}}}catch(e){{}}")   # music slider at 80%: clearly audible in the video
        ctx.add_init_script(AUDIO_JS)
        pg=ctx.new_page();errs=[]
        pg.on("pageerror",lambda e:errs.append(str(e)))
        pg.on("console",lambda m:m.type=="error" and errs.append("console: "+m.text[:160]))
        pg.goto(URL+"?demo="+str(time.time()));pg.wait_for_timeout(1500)
        rec=Recorder(pg,ctx,quality=82);rec.start();pg.wait_for_timeout(1200)   # splash screen with 'Continue previous duel'
        pg.evaluate(LIB)
        pg.evaluate("D.touch(document.getElementById('spCont'),260)");pg.wait_for_timeout(120)   # the tap on 'Continue previous duel' is visible too
        pg.click("#spCont");pg.wait_for_timeout(300)
        pg.evaluate("D.init()")
        marks=[]
        for n,sc in enumerate(scenes):
            marks.append(time.time())
            try:
                pg.evaluate("async()=>{"+sc+"}")
            except Exception as e:
                print("SCENE",n,"FAILED:",str(e)[:300]);errs.append(f"scene {n}: {e}")
                pg.evaluate("D.close()")
        pg.wait_for_timeout(600);rec.stop()
        aud=pg.evaluate("__audStop()")
        # video time of every scene start: frame timestamps are Chrome's epoch clock, same clock as time.time()
        json.dump({"scene_start":[round(m-rec.t0,2) for m in marks],"end":round(rec.frames[-1][0],2)},open(out.replace(".mp4",".marks.json"),"w"))
        tmp=out.replace(".mp4","_v.mp4");sv=rec.save(tmp);print(sv);print(mux(tmp,aud,rec.t0,out,sv[1]/30));print("errors:",errs[:6])
        ctx.close();b.close()

if __name__=="__main__":
    w=sys.argv[1] if len(sys.argv)>1 else "A"
    if w in("A","all"):run("A",SCENE_A,os.path.join(HERE,"demo-A.mp4"))
    if w in("B","all"):run("B",SCENE_B,os.path.join(HERE,"demo-B.mp4"))
    if w=="all":
        lst=os.path.join(HERE,"_list.txt");open(lst,"w").write("file 'demo-A.mp4'\nfile 'demo-B.mp4'\n")
        subprocess.run([FF,"-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",os.path.join(HERE,"demo.mp4")],check=True);os.remove(lst)
