# Demo-video – plan (15/10/2026)

Doel: een korte mp4 (ca. 90–110 s, staand, 780x1688, 30 fps) van een deel-duel in 2P / Master Duel dat ALLE animaties van de app toont, met kloppende getallen.

## Software (klaar)
- Chrome (staat al op je pc) wordt door `playwright` bestuurd; beeld = Chrome-screencast, omgezet naar mp4 met `imageio-ffmpeg` (H.264). Beide geinstalleerd (pip, jouw toestemming).
- De app draait via `python -m http.server 8123` (staat al aan). Het script klikt echt in de app; saaie keuzes (zoeken, tikken op kaarten) gebeuren snel via dezelfde functies.
- Ondertitels in beeld (kleine balk bovenaan) leggen elke stap kort uit (Engels, zoals de app).

## Geverifieerde getallen (berekend met de eigen code van de app)
| Wat | Waarde | Hoe |
|---|---|---|
| Blue-Eyes White Dragon | 3000 -> **3700 ATK** | Mountain +200 (Dragon, Winged Beast, Thunder) + Black Pendant +500 |
| Silent Magician LV8 (P2) | **3500 ATK**, 1000 DEF | niet beinvloed (Spellcaster; Wasteland/Mountain raken hem niet) |
| Cyberdark End Dragon (P2) | 5000 ATK / **3800 DEF**, DEF-stand | Machine: niet beinvloed door Mountain/Wasteland/Sogen |
| Silent Magician LV4 | 1000 + 5 x 500 = **3500** | tellers (5 draws van P1) |
| Gevecht | 3700 vs 3500 -> LV8 vernietigd, P2 -200 LP | |
**NIET gebruiken:** Umi (Machine -200: zou Cyberdark End Dragon op 3600 DEF zetten), Yami/Empowerment (Spellcaster +).

## Scenario (5 beurten; je zei 4 beurten + de beslissende beurt)
Speler 1 (jij, onderaan) = Dragon/Beast-Warrior; speler 2 (bovenaan) = Cyberdark/Silent Magician.

| Beurt | Gebeurtenis | Animatie(s) |
|---|---|---|
| Start | Splash: 2 players + Master Duel, Start duel, munt (P1 wint), 'I go first' | intro, munt, IT'S TIME TO… DUEL!, LP telt op |
| 1 P1 | Normal Summon Battle Ox (Lv4). Field Spell **Sogen** (Warrior/Beast-Warrior +200: Ox 1900). Set **Mystical Space Typhoon** face-down. | stof bij summon, veld fade-in (gras), groene ATK-gloed, Set-kaartrug |
| 2 P2 | Draw. **Fusion Summon Cyber End Dragon** (3 Cyber Dragons uit de hand, via Polymerization). Normal Summon Silent Magician LV4. Field Spell **Wasteland** (tweede achtergrond op de helft van P2). | Fusion-swirl vanaf bovenrand, Spell-skelet naar Graveyard, stof, 2 veldbeelden |
| 3 P1 | Draw (teller +1), **Graceful Charity** (draw 3: +3), **Upstart Goblin** (draw 1: +1, P2 krijgt 1000 LP) = 5 tellers -> LV4 = 3500 ATK. Normal Summon Beaver Warrior. **Xyz Summon Number 39: Utopia** (Battle Ox + Beaver Warrior, Lv4+Lv4). **Mystical Space Typhoon** (Quick-Play, uit Set) vernietigt **Wasteland**. | tellers + groene ATK-gloed per teller, LP-groene flits bij P2, Xyz-draaikolk + Overlay Units, omdraai (MST), Spell-skelet naar GY, veld fade-out op P2-helft |
| 4 P2 | Draw. Standby: LV4 (5 tellers) -> Graveyard, **Special Summon Silent Magician LV8** (3500/1000). **Fusion Summon Cyberdark Dragon** (Cyberdark Horn + Edge + Keel uit de hand). **Fusion Summon Cyberdark End Dragon** (Cyberdark Dragon + Cyber End Dragon van het veld) in **DEF**. Normal Summon **Mystic Tomato**. | tombsteen-pile, Fusion uit hand, Fusion met veldmaterialen, stof |
| 5 P1 | Draw. **Change of Heart** op Mystic Tomato (tot End Phase). Field Spell **Mountain** vervangt Sogen. **Tribute Summon Blue-Eyes White Dragon** (Lv8 = 2 Tributes: Utopia + de overgenomen Tomato; Tomato gaat naar de GY van P2). **Black Pendant** op Blue-Eyes -> **3700 ATK**. Battle Phase: Blue-Eyes valt Silent Magician LV8 (3500) aan -> vernietigd, P2 -200 LP. | controlewissel-glijden (fxMove), Sogen vliegt als skelet naar GY + nieuw veld fade-in, rode ATK-gloed (Sogen weg) + groene gloed (Mountain), Tributes vliegen naar GY, equip-gloed, aanvalsring/chip/pijl, uitval, slash, rode flits, tombsteen, LP schudt rood |
| Bonus | Korte reeks (nieuw bord, snel): **Synchro Summon** (Junk Synchron + Speed Warrior -> Junk Warrior), **Link Summon** (Link Spider op een EMZ met Cyber Dragon... of Normal Monster), Special Summon uit Graveyard (vliegt van de pile naar de zone), Banish (portaal), Surrender/einde niet nodig. | Synchro goud, Link cyaan + pijlen, pile -> zone, Banished-portaal |

## Alle animaties van de app en waar ze in de video zitten
Intro (munt/DUEL!/LP telt op) • stof bij summon • LP-teller (schudden, rode/groene flits, balk) • aanvalsmarkering (ring, chip, pijl) • lunge • slash • schild (DEF-stand: breekt of houdt stand 'BLOCKED') • tombsteen • directe aanval (slash op de LP-balk) • kaart vliegt naar GY/Banished • Spell/Trap-skeletkaart • kaart vliegt van pile naar zone • ATK/DEF-gloed (groen/rood) • omdraai (face-down -> open) • controlewissel (fxMove) • veld fade in/out (NIEUW) • Fusion/Synchro/Xyz/Link (NIEUW).
Het DEF-schild en de directe aanval komen in de bonus-reeks (Cyberdark End Dragon in DEF aanvallen met Blue-Eyes op 3700 < 3800: schild houdt stand, en een directe aanval op een leeg veld) – dat past niet in het hoofdverhaal; zie beslispunt 3.

## Eerlijke kanttekeningen (regels die de app niet volgt)
1. **Handkaarten:** de app telt geen hand. P2 heeft voor 3 Fusion Summons + LV4 + LV8 + Tomato meer kaarten nodig (±11) dan een echte hand (5 + 2 draws = 7). Cyberdark End Dragon vraagt nu eenmaal Cyberdark Dragon + Cyber End Dragon als materiaal, en elk daarvan is zelf een Fusion. In de video staat een korte ondertitel 'Demo: the hands are not tracked'.
2. **Silent Magician LV8** mag enkel door LV4 (effect, 5 tellers, Standby Phase van P2's volgende beurt): zo staat het in het plan. De 5 draws van P1 (1 natuurlijke + Graceful Charity 3 + Upstart Goblin 1) kloppen.
3. Blue-Eyes (3700) kan Cyberdark End Dragon (3800 DEF) niet breken; daarom valt hij Silent Magician aan.

## Beslispunten voor Tom
1. Akkoord met dit verhaal (en met Mountain + Black Pendant i.p.v. Dragon Treasure, omdat 3000 + 300 + 300 geen 3700 is)?
2. Akkoord dat Umi niet gebruikt wordt (zie hierboven)?
3. Wil je het DEF-schild en de directe aanval in een korte bonus-reeks, of laten we ze weg om de video kort te houden?
4. Ondertitels in beeld: ja of nee?
5. Duur: ±100 s is nodig voor alles; korter kan door de bonus-reeks te schrappen.
