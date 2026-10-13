# Duelist Scorekeeper

**A free life-point counter and rules helper for your Yu-Gi-Oh! card duels. Made for your phone.**
Built by Spawner Industries. Status: **beta**.

**As the name suggests, it is a scorekeeper for your duel:** your life points, the cards on the field, and the ATK/DEF changes from Equip and Field Spells. It also helps with the rules: you can check in the app whether a move is allowed *before* you do it in your real duel.

You keep playing with your own cards. This app sits next to the table and keeps track of what is happening, so nobody has to count on paper, wonder whether a move was allowed, or argue about whose turn it is. So go grab that drink or snack, take a break, and come back with confidence: the app remembers where you were.

**Also built in:** Graveyard and Banished piles, Extra Monster Zones with Link arrows, Pendulum Zones, Speed Duel with Skill Cards, a coin toss to decide who starts, and undo.

## How to use it

You do **not** need to download anything from this GitHub page, install anything from an app store, or make an account. It is simply a web page.

1. Open **https://spawner1andonly.github.io/duelist-scorekeeper/** on your phone (portrait mode works best).
2. *Optional, but recommended:* add it to your home screen so it opens like an app, full screen, and keeps working without internet.
   - **Android (Chrome):** tap the menu (⋮) and choose **Install app** or **Add to Home screen**.
   - **iPhone (Safari):** tap the Share button and choose **Add to Home Screen**.
3. Tap **Start duel**, pick 1 or 2 players and Master rules or Speed Duel, and play.

Your duel is saved on your phone, so closing the app does not lose it (use **Continue previous duel**).

---

## What it does

**Keeps score**
- Life Points for two players (8000, or 4000 in Speed Duel), with basic animation for the life-point counters and for the start of the duel (coin toss, who goes first).
- Undo for every action (up to 60 steps), plus a Surrender button.

**Plays on one phone or two**
- *2 players, 1 phone:* the opponent's half of the screen is upside down so both of you can read it. The middle strip with the buttons and the pop-ups turn towards the player whose turn it is (and you can flip a pop-up by hand).
- *1 player, own phone:* each player uses their own phone.

**Knows the turn structure**
- Draw, Standby, Main, Battle and End Phase, and the first-turn rules (no draw and no Battle Phase for the first player).
- A **Rules** button that tells you what you may and may not do in the current phase.
- Normal Summon limit, Tribute counts, Flip Summon, changing battle position, attacks, and Spell/Trap timing are checked. If something is not allowed the app tells you why, and you can still choose **Do it anyway**, because a card effect may allow it.

**Shows the board**
- Every face-up monster shows its **Level** (orange star badge), Xyz **Rank** or **Link rating**.
- Every monster that has Equip Spells gets its own **symbol and colour** (blue circle, green triangle, yellow square, orange cross, red star, purple arrow, cyan diamond, pink heart, white x, lime club), shown on the monster (one per Equip Spell) and on the Equip Spell itself. Because the symbol is a shape, it also works without colours. To equip a card you simply tap the monster on the field.
- Monster Zones, Spell & Trap Zones, Field Zone, Graveyard and Banished piles.
- Master rules: two shared **Extra Monster Zones** with **Link arrows** (all Link Monsters are included) and the official placement rules, and **Pendulum Zones** with scales and Pendulum Summon checks.
- Speed Duel: 3 Monster Zones, 3 Spell & Trap Zones, no Main Phase 2, and **Skill Cards** (124 Skills, set face-down, with the official activation rules).

**Searches cards**
- Around 14,600 cards with their full text. Load a monster, Spell or Trap onto the board in one tap.
- Attacks are calculated for you: damage, destroyed monsters, face-down monsters being flipped. You see who attacks what (rings, arrow and numbers) before the attack effect, and the defender is asked whether they want to respond with a Trap, Quick-Play Spell or effect. A small **effect builder** lets you enter that response (change ATK/DEF, destroy a monster, negate the attack, change Life Points) and the attack then continues with the new numbers.
- Destroyed and used cards fly to the Graveyard or Banished pile, and back onto the field when you Special Summon them from there.

**Knows who owns a card (control changes)**
- Change of Heart, Snatch Steal, Creature Swap, Soul Exchange and other cards that take control: a monster you control but do not own always goes to its **owner's** Graveyard or Banished pile; "until the End Phase" effects give the monster back automatically; Snatch Steal-style cards give it back when the card leaves the field.
- Cards that are Special Summoned to the opponent's side by their own text (Lava Golem with its Tributes, Kaiju…) belong to you.
- Monster Reborn on a card in the opponent's Graveyard puts it on your side.
- At the end of the duel the app reminds you which cards to give back to their owner.

**Does the maths for stat changes**
- Equip Spells and Field Spells that raise or lower ATK/DEF are applied automatically when the card text allows it, including bonuses that grow with counters or the number of monsters.
- When a card changes ATK/DEF in a way the app cannot work out (a condition, a one-turn effect), it says so and you adjust by hand.
- Every Field Spell has its own background picture; the screen changes when one is played.

**Practical**
- Counters on cards, "used this turn" markers and "once per Duel" ticks.
- Coin and dice.
- Install it on your home screen; it works offline after the first visit.

## What it does not do

- **It is not a card game.** There is no deck, no hand and no drawing. Your real cards (or any other way you play) stay in your hands.
- **It does not read or run card effects.** No real chains, no costs, no "destroy that card" (the effect builder at an attack is a simple helper, not a rules engine). You apply effects yourself with the life-point buttons and by moving cards to the Graveyard, and the app helps where it can.
- **It does not track** Xyz materials, Fusion/Link materials or tokens as real cards, and "banished instead" effects are not applied automatically.
- **It does not check your deck**: no deck size, no forbidden/limited list.
- **It is not a judge.** It follows the official rules as far as they were available to the author, but you can always override it, and it can be wrong. If a card or a ruling says otherwise, the card and the rulebook win.
- No online play and no syncing between two phones (yet), no timer, no match tracking (best of 3).
- No card pictures. English only.

## Rules used

- Standard TCG rules ("Master Duel" in the menu = 8000 LP, 5 zones, Extra Monster Zones, Pendulum Zones) and **Speed Duel** (4000 LP, 3 zones, no Main Phase 2, Skills). Sources: the official Konami rulebook and starter guides, the Speed Duel Addendum, and Yugipedia.

## Free, and fan-made

Duelist Scorekeeper is free to use. If you like it, you can support it on [Ko-fi](https://ko-fi.com/spawnerindustries).

*Unofficial fan tool. Not affiliated with or endorsed by Konami. Yu-Gi-Oh! and all card names and card text are © Konami. This app shows no card artwork (the card back, logo and field backgrounds are original). Card data via YGOPRODeck.*
