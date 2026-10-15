# Duelist Scorekeeper

**Een gratis levenspunten-teller en regelhulp voor je Yu-Gi-Oh!-kaartduels. Gemaakt voor je gsm.**
Door Spawner Industries. Status: **beta**.

**Zoals de naam zegt, is het een scorekeeper voor je duel:** je levenspunten, de kaarten op het veld en de ATK/DEF-wijzigingen van Equip- en Field Spells. Hij helpt ook met de regels: je kunt in de app nagaan of een zet mag *voor* je hem in je echte duel doet.

Je speelt gewoon verder met je eigen kaarten. De app ligt naast de tafel en houdt bij wat er gebeurt, zodat niemand meer op papier hoeft te tellen, zich afvraagt of een zet mocht, of ruzie maakt over wiens beurt het is. Ga dus gerust een drankje of snack halen, neem een pauze en kom met vertrouwen terug: de app onthoudt waar je gebleven was.

**Zit er ook in:** Graveyard en Banished, Extra Monster Zones met Link-pijlen, Pendulum Zones, Speed Duel met Skill Cards, een muntworp om te bepalen wie begint, en ongedaan maken.

## Zo gebruik je hem

Je hoeft **niets** te downloaden van deze GitHub-pagina, niets te installeren uit een app-store en geen account te maken. Het is gewoon een webpagina.

1. Open **https://spawner1andonly.github.io/duelist-scorekeeper/** op je gsm (rechtopstaand werkt het best).
2. *Optioneel, maar aanbevolen:* zet hem op je startscherm, zodat hij als een app opent, schermvullend, en ook zonder internet blijft werken.
   - **Android (Chrome):** tik op het menu (⋮) en kies **App installeren** of **Toevoegen aan startscherm**.
   - **iPhone (Safari):** tik op de Deel-knop en kies **Zet op beginscherm**.
3. Tik op **Start duel**, kies 1 of 2 spelers en Master-regels of Speed Duel, en speel.

Je duel wordt op je gsm bewaard, dus de app afsluiten kost je niets (gebruik **Continue previous duel**).

---

## Wat de app wél doet

**Houdt de score bij**
- Levenspunten voor twee spelers (8000, of 4000 bij Speed Duel), met eenvoudige animaties voor de levenspunten-tellers en voor de start van het duel (muntworp, wie begint).
- Ongedaan maken voor elke actie (tot 60 stappen) en een opgeefknop.

**Op één gsm of op twee**
- *2 spelers, 1 gsm:* de helft van de tegenstander staat ondersteboven, zodat jullie allebei kunnen lezen. De middenstrook met de knoppen en de pop-ups draaien mee naar de speler die aan de beurt is (en je kunt een pop-up met de hand omdraaien).
- *1 speler, eigen gsm (online):* elke speler gebruikt zijn eigen gsm en komt in dezelfde kamer met een code van 5 tekens. Je ziet jezelf altijd onderaan. Face-down kaarten en een Skill blijven verborgen voor je tegenstander, de "Respond?"-vragen (aanval, summon, activatie) gaan naar de gsm van je tegenstander, en de animaties spelen op beide gsm's.

**Kent de beurtstructuur**
- Draw, Standby, Main, Battle en End Phase, en de regels van de eerste beurt (de starter trekt niet en heeft geen Battle Phase). In **Quick**-modus (standaard) vraagt een venster of je getrokken hebt en wordt een Standby Phase waarin geen enkele kaart iets te doen heeft overgeslagen; in **Manual**-modus tik je zelf door elke fase.
- Een **Rules**-knop die uitlegt wat je in de huidige fase wel en niet mag.
- De limiet van één Normal Summon, het aantal Tributes, Flip Summon, positie wisselen, aanvallen en de timing van Spells en Traps worden gecontroleerd. Mag iets niet, dan zegt de app waarom, en je kunt toch kiezen voor **Do it anyway**, want een kaarteffect kan het wel toelaten.

**Toont het bord**
- Elk open monster toont zijn **Level** (oranje sterbolletje), Xyz-**Rank** of **Link-rating**.
- Elke open kaart toont zijn **attribuut** (WIND, WATER, EARTH, FIRE, DARK, LIGHT, DIVINE) rechtsboven; Spells en Traps tonen een Spell- of Trap-symbool.
- **Kaartkleuren zoals de echte kaarten**: Normal (geel), Effect (oranje), Ritual (blauw), Fusion (paars), Synchro (wit), Xyz (zwart), Link (donkerblauw), Spell (donker muntgroen), Trap (fuchsia). De kaart op het veld en zijn pop-up hebben dezelfde kleur, en de pop-up ziet eruit als een kaart (naamkader, tekstvak met Level en attribuut). Face-down kaarten blijven kleurloos.
- De Graveyard en Banished hebben een eigen look (een begraafplaats en een portaal), en de kaarten in de lijst dragen hun kaartkleur. De lijst draait naar de speler aan de beurt.
- Een face-down kaart die open gaat (Flip Summon, een geactiveerde Trap) draait om met een kleine animatie.
- Een nieuwe Equip Spell, Field Spell of Continuous Spell met een ATK/DEF-effect wacht tot je op **Apply** tikt voor de bonus meetelt, zodat je altijd de gloed ziet.
- Een monster dat in de Spell & Trap-zone ligt (Continuous Spell of Equip card) kan terug als Special Summon naar de Monster Zone.
- Elk monster met Equip Spells krijgt een eigen **vorm en kleur** (blauw bolletje, groen driehoekje, geel vierkantje, oranje kruisje, rood sterretje, paarse pijl, cyaan ruitje, roze hartje, wit kruisje, lime klaver), getoond op het monster (één per Equip Spell) en op de Equip Spell zelf. Omdat het een vorm is, werkt het ook zonder kleuren. Om een kaart te equippen tik je gewoon op het monster op het veld.
- Monsterzones, Spell & Trap-zones, Field Zone, Graveyard en Banished.
- Standaardregels: twee gedeelde **Extra Monster Zones** met **Link-pijlen** (alle Link-monsters zitten erin) en de officiële plaatsingsregels, en **Pendulum Zones** met schalen en controle op Pendulum Summon.
- Speed Duel: 3 monsterzones, 3 Spell & Trap-zones, geen Main Phase 2 en **Skill Cards** (124 Skills, face-down gelegd, met de officiële activeerregels).

**Zoekt kaarten op**
- Ongeveer 14.600 kaarten met hun volledige tekst. Leg een monster, Spell of Trap met één tik op het bord.
- Aanvallen worden berekend: schade, vernietigde monsters, omgedraaide face-down monsters. Je ziet wie wie aanvalt (ringen, pijl en cijfers) vóór het aanvalseffect, en de verdediger wordt gevraagd of hij wil reageren met een Trap, Quick-Play Spell of effect. Met een kleine **effectbouwer** voer je die reactie in (ATK/DEF wijzigen, een monster vernietigen, de aanval negeren, levenspunten wijzigen) en de aanval gaat daarna verder met de nieuwe cijfers.
- Vernietigde en gebruikte kaarten vliegen naar de Graveyard of Banished, en terug het veld op als je ze van daaruit Special Summont.

**Weet wie een kaart bezit (controlewissels)**
- Change of Heart, Snatch Steal, Creature Swap, Soul Exchange en andere kaarten die controle overnemen: een monster dat je controleert maar niet bezit, gaat altijd naar de Graveyard of Banished van zijn **eigenaar**; effecten "tot de End Phase" geven het monster automatisch terug; kaarten als Snatch Steal geven het terug als de kaart het veld verlaat.
- Kaarten die door hun eigen tekst aan de kant van de tegenstander Special Summoned worden (Lava Golem met zijn Tributes, Kaiju…) horen bij jou.
- Monster Reborn op een kaart in de Graveyard van de tegenstander zet die aan jouw kant.
- Op het einde van het duel herinnert de app je aan welke kaarten je moet teruggeven aan hun eigenaar.

**Helpt bij effecten die getallen veranderen (voert de rest nooit uit)**
- Het venster van elk open monster, elke open Spell en Trap toont **meteen de kaarttekst**, zodat je een effect direct kan nalezen. Je speelt nog altijd met je echte kaarten; de app houdt enkel de score bij.
- Effecten die **levenspunten of ATK/DEF met een vast bedrag** veranderen, worden knoppen op basis van de kaarttekst, bijvoorbeeld *Apply: you gain 1000 LP*, *This turn: +1000 ATK (this card)* of *choose a monster*. Eenmalige kaarten gaan naar de Graveyard als je ze toepast. Een eenmalige Spell/Trap met maar één zo'n effect wordt meteen toegepast, nadat je tegenstander kon reageren, en gaat dan naar de Graveyard. Kaarten met meerdere effecten houden hun knoppen en jij drukt op degene die je wil. De app controleert geen kosten of voorwaarden: jij beslist of je de kaart mag activeren.
- Effecten die afgaan **als een kaart het veld verlaat** hebben een eigen deel, en **Standby Phase**-effecten (Snatch Steal, Lava Golem, Cure Mermaid, onderhoudskosten, tellers) komen in een herinneringsvenster als de Standby Phase begint. Je tikt per effect op **Apply** (of **Apply all**); de app past ze niet zelf toe.
- Een monster kan als **Continuous Spell** (Pumprincess) of als **Equip-kaart** (Black Metal Dragon, Union-monsters) in de Spell & Trap-zone worden gelegd, en de stats volgen.
- Een **waarschuwing** verschijnt bij ATK/DEF-wijzigingen die de app niet kan uitrekenen (een voorwaarde, "wordt", "verdubbelt"), en dan pas je het zelf aan.
- Verandert ATK/DEF, dan gloeit het monster **groen met witte plusjes** of **rood met witte minnetjes**; levenspunten en treffers laten de helft van de betrokken speler flitsen.

**Rekent mee met ATK/DEF-wijzigingen**
- Equip Spells en Field Spells die ATK/DEF verhogen of verlagen worden automatisch toegepast als de kaarttekst dat toelaat, ook bonussen die groeien met tellers of het aantal monsters.
- Verandert een kaart ATK/DEF op een manier die de app niet kan uitrekenen (een voorwaarde, een effect voor één beurt), dan meldt de app dat en pas je het zelf aan.
- Wordt er een Field Spell gespeeld, dan verandert de achtergrond naar een passend landschap (zee, berg, vuur…). Sommige Field Spells hebben een eigen beeld, de andere delen er één met gelijkaardige kaarten, dus niet elke Field Spell heeft een unieke achtergrond.

**Praktisch**
- Tellers op kaarten, "deze beurt gebruikt"-markeringen en "één keer per Duel"-vinkjes.
- Munt en dobbelsteen.
- Zet hem op je startscherm; hij werkt offline na het eerste bezoek.

## Wat de app niet doet

- **Het is geen kaartspel.** Er is geen deck, geen hand en geen kaarten trekken. Je echte kaarten (of hoe je ook speelt) blijven in je eigen handen.
- **Hij voert in het algemeen geen kaarteffecten uit.** Hij kan niet lezen wat de meeste kaarten doen. Hij handelt enkel wat hij in de kaarttekst herkent: vaste levenspuntenwijzigingen, ATK/DEF-bonussen (Equip-, Field- en Continuous-kaarten), tellers en controlewissels, en sommige daarvan worden voor je toegepast. Kosten en voorwaarden worden niet gecontroleerd en er zijn geen volledige kettingregels. In de effectbouwer (die je gebruikt als iemand reageert op een aanval, een summon of een Spell/Trap-activatie) voer je de reactie zelf in (ATK/DEF wijzigen, een monster of Spell/Trap vernietigen, negeren, levenspunten wijzigen) en de app past dan toe wat je invoerde. De rest doe je met de hand, met de LP-knoppen en door kaarten naar de Graveyard te verplaatsen.
- **Tokens worden niet bijgehouden** als echte kaarten (gebruik een eigen monster), en "banished instead"-effecten van kaarten worden niet automatisch toegepast. Xyz-materialen blijven onder het monster als Overlay Units, en Fusion-, Synchro- en Link-materialen gaan naar de Graveyard van hun eigenaar.
- **Hij controleert je deck niet:** geen decksgrootte. Hij blokkeert wel een 4e exemplaar van dezelfde kaart dat hij kan zien (veld, Graveyard, Banished), en de Forbidden & Limited List (TCG) kan je in het menu aanzetten; standaard staat ze uit.
- **Hij is geen scheidsrechter.** Hij volgt de officiële regels voor zover de maker ze kon opzoeken, maar je kunt hem altijd overrulen en hij kan fout zijn. Zegt een kaart of een uitspraak iets anders, dan wint de kaart en het regelboek.
- Online spelen met twee gsm's is nieuw en wordt nog getest. Geen timer, geen bijhouden van wedstrijden (best of 3).
- Geen kaartafbeeldingen. Alleen in het Engels.

## Gebruikte regels

- Standaard TCG-regels ("Master Duel" in het menu = 8000 LP, 5 zones, Extra Monster Zones, Pendulum Zones) en **Speed Duel** (4000 LP, 3 zones, geen Main Phase 2, Skills). Bronnen: het officiële Konami-regelboek en de startersgidsen, het Speed Duel Addendum en Yugipedia.

## Gratis, en gemaakt door een fan

Duelist Scorekeeper is gratis te gebruiken. Vind je hem leuk, dan kun je hem steunen via [Ko-fi](https://ko-fi.com/spawnerindustries).

*Onofficiële fan-tool. Niet verbonden met of goedgekeurd door Konami. Yu-Gi-Oh! en alle kaartnamen en kaartteksten zijn © Konami. Deze app toont geen kaartillustraties (de kaartrug, het logo en de veldachtergronden zijn eigen werk). Kaartgegevens via YGOPRODeck.*
