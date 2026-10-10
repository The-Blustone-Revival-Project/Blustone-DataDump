# VSFan extracted assets (2026): source audit and useful findings

> Scope: `analysis/VSFan/Extracted Assets (2026)` only. This report reads the supplied extracted trees and APK; it does not alter them. “In-game help says” below records the text of an archived build, not proof that every rule or balance number stayed current.

## Collection inventory and provenance

- The collection has three top-level deliverables: `1.1.2.0 (blustone.pcap, 2017-09-04)` (2,580 extracted files; about 109.0 MB), `1.1.3.0 (bs_transcendence.pcap, 2017-09-08)` (1,904 files; about 55.0 MB), and `1441 (APK)` (3,167 extracted files; about 96.3 MB). There is also the original 94,877,834-byte APK at the collection root; total inventory is 7,652 files. These are labels recorded by the supplied collection; the two pcap-named directories contain extracted assets, not raw pcap files.
- Root APK: `com-vshower-prd-sr-1441-39567016-ef64fd3f499bd158a709f4c380d3c06d.apk`. Android `aapt dump badging` identifies package `com.vshower.prd_sr`, version code `1441`, version name `1.4.4.1`, min SDK 16, target SDK 26. SHA-256: `0fbd1e08dc6e0dbdf9ecf972552c9de52fc4fd86b4b573af52935e8296199f4a`. Its ZIP has 877 entries including 52 `.jet` payloads; named game packages include `C001`, `C003`, `C009`, `C010`, `LEVELING`, `M001`–`M009` subsets, `M100`, `SNOW`, `ST001`, `UI_CSV`, `UI_TUTO`, and `DIALTU-*`.
- The extracted 1.4.4.1 tree has 2,769 PNGs, 253 MP4s, 162 MP3s, 110 XMLs, 89 JSONs, 35 GLSL files, 21 BINs and 4 TXT files. The two earlier capture trees are image/video/audio-heavy only: 1.1.2.0 has 2,409 PNG / 117 MP4 / 54 MP3; 1.1.3.0 has 1,799 PNG / 76 MP4 / 29 MP3. No images were counted as numerical stats based on file names.
- The 2017 capture labels and APK version are much older than later balance changes already documented in [`stat-version-context.md`](../hunters/base-stats-visual-hunt/stat-version-context.md). Treat these as historical mechanics and terminology. Do not use their rules as a current base-stat calibration point without a dated bridge.

## Strongest discovery: the archived in-game help corpus

`1441 (APK)/UI_CSV/3d98d128.json` contains 157 category/content records (11 top-level categories plus subcategories and help articles). The recovered file has a dangling comma immediately before its final `]`; parsing this copy in memory after removing only that trailing comma yields 157 records. The source file was left unchanged. `3d9fb02e.json` is the navigation index for the same 11 help categories. Together, these provide authoritative archived descriptions for gameplay semantics and historical jewel set bonuses, across Korean, English, Japanese, simplified Chinese and traditional Chinese.

### Direct stat definitions (hero-base-stat research relevance)

- **Primary stats** (`CONTENTS1_4`): HP is survivability; ATK is damage; DEF reduces incoming damage; Attacking Speed is the maximum number of attacks per second / tap-attack speed. The guide defines these but supplies no per-hero values, ranks, levels, or equipment states.
- **Attack stats** (`CONTENTS1_5`): Critical Attack Chance is the probability of a critical tap attack; Critical Attack Damage is the percentage increase to basic damage on a critical attack; Armor Penetration is described as permanent, unconditional additional damage regardless of enemy DEF or element; Elemental Enhancement adds damage when the attacker has an elemental advantage.
- **Defense stats** (`CONTENTS1_6`): Block Chance blocks enemy tap attacks and is said to reduce the enemy’s critical chance and critical-hit damage; Damage Reduction Block is the percentage of damage reduced while blocking and also reduces damage received from enemy skills; Elemental Resistance reduces the extra damage received at an elemental disadvantage; Regeneration is health naturally recovered while the hunter is on standby inside the airship.
- **Element cycle** (`CONTENTS1_1`): Fire is strong against Lightning and weak to Ice; Ice is strong against Fire and weak to Lightning; Lightning is strong against Ice and weak to Fire. The English text labels these as scissors/rock/paper respectively. This is a cycle, not a numeric multiplier.
- **Role descriptions** (`CONTENTS1_2`): Offense defeats enemies faster and attacks outside the airship; Defense survives longer and attacks outside it; Bomber detonates a powerful bomb inside the airship; Support heals or strengthens allies inside. The article defines roles, not hero-by-hero assignments.

These are definitions of stat fields and attack/defense semantics only. No per-character base tuple (`HP/ATK/DEF/…`) was found in the structured UI-help payloads, dialogue records, or APK metadata inspected here.

### Jewel set-bonus table (exact historical help text)

`CONTENTS11_8` (“Set Effect”) lists all 12 named effects. Four jewels are required for the second tier; set counting is independent of equipment slot, and the help text says repeated copies of the same set effect can stack. These are **set bonuses**, not individual jewel primary/substats or polished item-instance rolls.

| Archived English name | Required count | Bonus as stated in EN | Notes |
|---|---:|---|---|
| HP Jewel | 2 | HP +5% | |
| Offensive Jewel | 2 | AP +5% | Source uses “AP”; likely its attack-power label, but preserve the raw abbreviation. |
| Defensive Jewel | 2 | DP +5% | Source uses “DP”; preserve the raw abbreviation. |
| Critical Jewel | 2 | Critical Attack Chance +4.5% | |
| Block Jewel | 2 | Block Chance +4.5% | |
| Fatal Jewel | 4 | Critical Attack Damage +50% | |
| Super Block Jewel | 4 | Damage Reduction Rate +5% | **Translation conflict:** Korean `막기 피해량 9% 증가` says 9%; Japanese and both Chinese strings say 5%. Do not collapse this to one global value without resolving localization/version semantics. |
| Element Jewel | 4 | Elemental Enhancement +23 | |
| Resistance Jewel | 4 | Elemental Resistance +23 | |
| Speed Jewel | 4 | Attack Speed +1.72 | |
| Regeneration Jewel | 4 | HP Regeneration +30 | |
| Penetration Jewel | 4 | Armor Penetration +12 | |

The two `+23` entries are explicit flat set-bonus values in this guide. They do **not** settle any previously ambiguous decimal placement for an individual Element/Resistance jewel instance (main stat, substat, rarity, polish, or level). The Super Block row is contradicted by the Korean copy (`9%`) versus EN/JP/ZH/ZT (`5%`); retain both readings in the working data and mark the set row as disputed.

### Equipment and jewel mechanics

- `CONTENTS11_1`: three equipment types: Weapon (ATK and attack-related stats), Armor (DEF and defense-related stats), Accessories (HP and other stats).
- `CONTENTS11_2`: equipment upgrades use rupees and Toolboxes; maximum upgrade level depends on equipment modification grade.
- `CONTENTS11_3`: modification becomes available at upgrade levels 10, 20, 30 and 40; modification increases item ability and raises the maximum upgrade cap. Element materials are Flammable Material (Fire), Coolant (Ice), Lightning Box (Electricity). Materials are described as rare Mirage Ruins finds.
- `CONTENTS11_4`–`CONTENTS11_7`: jewels are Metron Crystals, higher classes provide higher ability, obtained by daily free/random-kind mining, Manda mining, rare hunter search or Market; polishing spends rupees and is probabilistic (failed polish loses rupees); mounting requires matching jewel/rabbet shapes in weapons, armor or accessories.
- This help corpus contains no item-by-item accessory table, jewel rarity-by-rarity stat rows, polish-stage multipliers, or individual item IDs. It must not increase item-instance stat coverage by itself.

## Other game-system learning preserved by the guide

- **Combat:** skills require rage built by attacking and a fixed skill-specific rage amount; maximum rage collected at one time is fixed (`CONTENTS1_3`). Fever has at most 3 levels depending on hunter grade and rises faster with faster tapping (`CONTENTS2_1`). Battle has an airship fuel/time limit; when fuel expires, exploring teammates cannot participate; losing or forfeiting returns fuel (`CONTENTS2_2`–`2_3`). Skill animations can be disabled (`2_4`). Dispatch clears stages automatically; stronger hunters reduce dispatch time (`2_5`).
- **Hunter Gym / advancement:** the guide has distinct articles for training, advancing, transcendence, skill training, hunter locks, Fate Stories, role bonus, and group advancement (`CATEGORY4_1`–`4_8`). The full text is included in the appendix below; these article titles are useful for constructing system/reference inventories. The guide does not publish character growth tables or exact advancement costs.
- **Supplies / progression:** attendance rewards include items and veteran points with milestone rewards; Activity Supply grants fuel at defined times; Special Supply is a separate category (`CATEGORY3_1`–`3_3`). No exact quantities/times were extracted from this corpus.
- **Fight Club:** help entries cover auto feature, battle time limit, hidden defense teams, ranking, revenge and friendly match (`CATEGORY5_1`–`5_6`).
- **Abyss / Missing Hunters:** entries cover abyss, missing hunters, Rare Search, Unique Search and waiting/alarms, with an article on a “Missing Hunter Big Rewards” (`CATEGORY6_1`–`6_7`).
- **Market / account:** market goods and item-origin/description; hunter traces; coupons/tickets; sharing; nickname/account linking; veteran ticket/rank; blocking (`CATEGORY7_1`–`7_2`, `CATEGORY8_1`–`8_8`).
- **Mirage Ruins:** described as 5-vs-5 strategy; consumed strength/health does not recover between battles; a fainted hunter cannot fight again until first aid; reset daily at midnight; fragments are Market currency, market resets daily and paid resets cap at 3. Floors are assigned using average team combat power; success moves deeper, failure closer to surface. First ground has 3 battles on floors 1–20, 6 on 21–40, 9 on 41+; enemy strength/rewards rise. Entry notice occurs after clearing general stage 27. Temporary active hunters rotate every few days. These are archived guide claims (`CATEGORY9_1`–`9_12`), not confirmed server behavior.
- **Fishing:** the guide describes bait grades, distance-dependent fish, bite/shake/pull, a fish Fury state that can snap the line if tapping continues, crown rarity/price grading, and bait refund before a bite but bait consumption after a bite on failure/cancel (`CATEGORY10_1`–`10_8`).

## Character identity crosswalks in tutorial-dialogue records

`DIALTU-EN/820e*.json` contains TalkerMaker conversation assets, not stat sheets. The matching `DIALTU-JP`, `-KO`, `-ZH`, and `-ZT` folders have the same 17 filenames. The records embed explicit actor `Name`, `CardID`, `CardType`, and `IsPlayer` fields. This supports names/IDs for identity work; `CardID` alone does not establish that the character has a playable base-stat row.

| Card ID | Name as recorded | Evidence / qualification |
|---|---|---|
| 003 | Nene | Named `Char` actor in 820e90e3, 820e90e4, 820e9109, 820e912e, 820e9154. |
| 009 | `???` | Unnamed actor in later dialogue records 820e9070/71, 820e9096/97, 820e90e2/3, 820e9109/2e/2f/30, and 820e9154. Other speakers have placeholders such as “New Character”, “Strange Woman”, or “Unknown Man”; do not assign a catalog identity from these strings. |
| 010 | Vincent; “Unknown Man” | Vincent in 820e904a–904d; later story files label ID 010 “Unknown Man”. Same ID may be intentionally anonymized in later story context. |
| 047 | Lily & Lyla | Named `Char` actor in 820e904e. |
| 052 | Windblade | Named `Char` actor in 820e904b–904d. |
| 056 | Genovia | Named `Char` actor in 820e904a–904e. `IsPlayer` is empty in these rows; do not infer player status. |
| 001 | Lantern (`Char`), Lana (`NPC`) | Both types occur in 820e9109/912e; `CardType` differs. Do not merge the character and NPC rows. |

The dialogue files add story labels/location strings including “Unknown Snowfields” (`820e90e3` conversation title) and include story dialogue around these actors. They do not contain numeric stats, growth, rarity, role, element, gear, or an explicit protagonist identity. Card IDs here are string IDs and are not automatically equivalent to the unrelated `C001` art-resource package name.

## Asset-family map: re-usable visual/resource leads

- **Early capture family, 1.1.2.0 (2017-09-04):** 39 top-level resource folders, dominated by `C###` character groups, with `_EFT` effects and `_SND` audio subgroups, plus a single `AUTOPLAY_20170418150948` group. Character IDs represented include C002, C004–C008, C012–C016, C018 and C020; some have only effect/sound packages. Folder suffixes preserve apparent package/export timestamps such as `20170811151651`; they are not balance version dates by themselves.
- **Early capture family, 1.1.3.0 (2017-09-08):** new C021–C030 art/effect/sound groups plus C017 effects; C029 has effects but no main art folder. This provides asset-presence/variant evidence, but not combat data.
- **APK 1.4.4.1 families:** character resources C001/C003/C009/C010 and related effect/sound, shared character rigs/cut-ins (`CE_PUB`, `CFE_PUB`, `CHA_AT`, `SKE_PUB`, `WAG_PUB`, `UI_CHA_RANK_NEW`); monster art packages M001, M002, M005, M006, M008, M009, M100; stage/background families `ST001`, `SNOW`, `STORY_TUTO`, and UI/tutorial/effect packages. File tree contains 110 small motion XML/JSON definitions and shader/layout/font assets. These are strong art/animation/scene leads for identity and compatibility work, not evidence of HP/ATK/DEF.
- Extracted `LEVELING/6a434cb8.bin` (39 B) and `LEVELING/6c1781a5.bin` (195 B), as well as `LAYOUT-BASE/*.bin`, are opaque binary payloads in this extracted representation. Their names alone are not readable tables. This pass did not decode them; do not derive level curves from file names or bytes.
- The root APK contains compressed `.jet` resources (52 entries). These are the corresponding package containers; the extracted folder is an unpacked view. No raw pcap file, server reference table, card-stat CSV, monster-stat CSV, equipment-instance table, or stage-reward table was present as a directly parseable file in this collection.

## Locale / UI-string data

- `UI_CSV/3d98d128.json` is the multi-language in-game help content; `3d9fb02e.json` maps help entry points to category IDs.
- `UI_CSV/e44ab8ed.txt` is a large six-column localized UI string table (`#COR,KR,EN,JP,ZH,ZH-HANT`), useful for mapping older UI terms and names. It includes labels such as Recruit Hunters, Train Teammate, See Details, stage/market and equipment vocabulary. It is not a stat table.
- `UI_CSV/7adedb12.txt` is a rendering/style string table (font, alignment, colors, bounds); `300e08f5.txt` is sound-event metadata. `7f8605b6.txt` is a localized profanity/filter dictionary and is intentionally not reproduced here; it has no game-stat value.
- Five DIALTU locale folders preserve the same 17 story-conversation filenames, allowing localization comparison. The 89 JSON files comprise 85 localized dialogue files, 2 help/navigation JSON files and 2 motion behavior JSON files.

## Coverage impact and next useful action

- **Heroes:** no base-stat tuple or verified clean state/rank/gear panel was found. The tutorial assets add identity-only name↔ID leads for Nene, Vincent/Unknown Man, Lily & Lyla, Windblade, Genovia, and an unresolved ID 009. Keep them as identity corroboration or polluted/unclear leads; do not add strict stat coverage.
- **Jewelry:** the help guide gives exact set bonuses for all 12 sets in one archived build; this is broader corroboration for the set-bonus subcatalog, but not 12/12 individual jewel item instances, quality grades, polished values, or socket instance stats. The Korean 9% Super Block variant is a genuine contradiction requiring a disputed-value row.
- **Monsters:** art/animation resource groups exist for M001, M002, M005, M006, M008, M009 and M100. The directories contain visual resources, not max-HP/ATK/DEF records or a mapping from a screen HUD number to a base stat.
- Strongest follow-up is to align IDs/names from `DIALTU` and character art packages with the live hero catalog as identity-only evidence, and to carry the `CONTENTS11_8` jewel bonus table into the research set-bonus sheet while preserving the Korean 9% conflict. Do not infer base hero or monster stats from art files.

## Appendix: English in-game help articles

The following is a faithful extraction of every English help article body in `3d98d128.json` (rich-text color tags kept). It preserves more of the moderately useful rules text than a short thematic summary can; it is not a claim that wording or values remained current after version 1.4.4.1.

### CONTENTS1_1 — Understanding the Elements

Know the 3 elements and their relation!
 <color='227,109,85,255'>Fire</color>(Scissors) element is weak to <color='60,200,217,255'>Ice</color> but
stronger than <color='214,179,40,255'>Lightning.</color>
<color='60,200,217,255'>Ice</color>(Rock)element is weak to <color='214,179,40,255'>Lightning</color> but
stronger than <color='227,109,85,255'>Fire.</color>
<color='214,179,40,255'>Lightning</color>(Paper) element is weak to <color='227,109,85,255'>Fire</color> but
stronger than <color='60,200,217,255'>Ice.</color>

### CONTENTS1_2 — Understanding Hunter Roles

Hunters have 4 different roles!

Offense : Defeats the enemy <color='255,156,0,255'>quicker</color> and attacks outside
the airship.
Defense : Withstands enemy’s attacks <color='255,156,0,255'>longer</color> and attacks
outside the airship.
Bomber : <color='255,156,0,255'>Explodes a powerful bomb</color> inside the airship.
Support : <color='255,156,0,255'>Heals or strengthens</color> your ally inside the airship.

### CONTENTS1_3 — Understanding Skills

To use skills you need to raise your rage
by attacking your enemy.
To use skills you need <color='255,156,0,255'>the same number</color> of
rage as the one above the Hunter’s head.
<color='255,156,0,255'>Touch the speech bubble</color> that’s above their
head to activate their skill!
Note that the maximum amount of rage you
can collect at one time is fixed.

### CONTENTS1_4 — Primary Hunter Stats

Figures that show hunters’ basic abilities.


HP : A measure of how far you can <color='255,156,0,255'>stand an enemy’s attack.</color> If your life drops down to 0 during battle, you will no
longer be able to fight.
ATK : A measure of how much <color='255,156,0,255'>damage you give to
an enemy.</color> The higher your attacking power, the quicker you
 will be able to defeat your enemy.
DEF: A measure of how much you <color='255,156,0,255'>reduce damage from
your enemy’s attack.</color> The higher the defense power, the
more resilient a character is to damage.
Attacking Speed : Maximum number of attacks per second.
The higher the number, the faster you can tap-attack.

### CONTENTS1_5 — Hunter Attack Stats

Stat details of hunters’ attack abilities.


Critical Attack Chance: The <color='255,156,0,255'>probability that activates a high damage critical attack</color> during tap-attacks.
Critical Attack Damage: The <color='255,156,0,255'>percentage that increases your basic damage</color> amount during Critical Attack.
Armor Penetration: <color='255,156,0,255'>Additional damage that is permanent and unconditional</color>, regardless of enemy’s DEF or element.
Elemental Enhancement: <color='255,156,0,255'>Additional damage amount</color> when
your <color='255,156,0,255'>element is in an advantageous position.</color>

### CONTENTS1_6 — Hunter Defense Stats

Stat details of hunters’ defense abilities.


Block Chance: The <color='255,156,0,255'>probability that blocks your enemy’s tap-
attacks.</color> It simultaneously <color='255,156,0,255'>reduces your enemy’s chance of a critical attack</color> and the <color='255,156,0,255'>damage you recieve when hit by
a critical attack.</color>
Damage Reduction Block: The <color='255,156,0,255'>percentage of how much
damage you reduce by blocking.</color> It also <color='255,156,0,255'>reduces the damage you receive when hit by an enemy’s skill.</color>
Elemental Resistance: <color='255,156,0,255'>Reduces</color> the <color='255,156,0,255'>additional damage</color> you
get when your <color='255,156,0,255'>element is in a disadvantageous element
position.</color>
Regeneration: The <color='255,156,0,255'>amount of health regenerated
naturally</color> when you are inside the airship in stand-by.

### CONTENTS2_1 — Fever Gauge

There is a maximum of 3 levels for Fever
Gauge depending on the Hunter's grade.
The <color='255,156,0,255'>faster you tap</color> the higher the gauge gets.

### CONTENTS2_2 — Ornithopter Time Limit

Did you know that there is a <color='255,156,0,255'>time limit</color>
when battling? The fuel meter on the bottom
right corner drops lower as time passes.
When the airship is out of oil, the exploring
teammates <color='255,156,0,255'>cannot participate in the battle.</color>
It is very difficult to fight alone in a team so
try to complete the battle in time.

### CONTENTS2_3 — Forfeit or Losing in the Game

Did you unfortunately lose or forfeit?
Don’t worry! <color='255,156,0,255'>The fuel is returned to you</color> when
you lose or forfeit a battle.

### CONTENTS2_4 — Skill Skip

Did you ever feel that your battles take too
long because of the skill animations?
Go to the menu then your settings and turn off
<color='255,156,0,255'>“Skill Animation!”</color>
You’ll be able to <color='255,156,0,255'>complete battles quicker.</color>

### CONTENTS2_5 — Dispatch

Try dispatching!
A convenient feature that allows you to clear
stages <color='255,156,0,255'>automatically</color> and earn items!
Note that the stronger your hunters are the
less time it’ll take to complete~

### CONTENTS3_1 — Daily Supplies

Do you know about the attendance supplies?
You can get various items and veteran points.
Don’t forget that <color='255,156,0,255'>special rewards</color> await
when your <color='255,156,0,255'>attendance dates are accumulated!</color>

### CONTENTS3_2 — Activity Supply

Do you know about the <color='255,156,0,255'>timely activity rewards</color>
that the Hunter Union prepares for active
hunters?
At certain times you can get <color='255,156,0,255'>additional fuel</color> so
don’t forget to collect them!
Forgot to collect your fuel at that time period?
 Don’t worry! Use your Manda to collect it back.

### CONTENTS3_3 — Special Supply

Bought Manda or a Package but don’t know
where to get the items?
Check Schumann’s<color='255,156,0,255'> Special Supply</color>, he takes
care of all Midgard’s supplies!!

### CONTENTS4_1 — Training

Make your hunter stronger through training!
You can level up through battling in areas,
but using a hunter as your training mate
can make you <color='255,156,0,255'>stronger much faster</color>. Note that
the training mate you use will be <color='255,156,0,255'>gone</color>.

### CONTENTS4_2 — Advancing

Do you have a hunter that can no longer level
 up?
When the level has reached MAX use advance
instead to make them stronger!
For advancement you need a hunter with the
<color='255,156,0,255'>same grade</color> and the higher the grade the more
hunters you need.
Of course, don’t forget that hunters you use
for advancement will be <color='255,156,0,255'>gone</color>.

### CONTENTS4_3 — Transcendence

Do you want to grow stronger?
How about making a hunter stronger by
matching it with the same hunter?
You can trascened ★3 hunters or above by
using the <color='255,156,0,255'>same hunter</color>.
Also, the hunter you are using as fodder needs
to also be ★3 or above.
Don’t forget that the hunter you used for
transcendence will be <color='255,156,0,255'>gone</color>.

### CONTENTS4_4 — Skill Training

Did you know hunters have basic skills and
additional skills? You can use additional skills
 from ★4 and above and these are activated <color='255,156,0,255'>
by chance</color>.
 Train the skills your hunters use! You will be
able activate more power in your skills.


1st Skill  - Using the 1st skill can <color='255,156,0,255'>increase damage</color> to your
opponent.
2nd Skill - Using the 2nd skill can increase <color='255,156,0,255'>additional</color> effect
that happens when using the skill.
3rd Skill - Using the 3rd skill you can <color='255,156,0,255'>permanently</color> increase
the hunter’s basic ability that is important to your hunter’s
role.
4th Skill - Using the 4th skill you can <color='255,156,0,255'>increase the
additional effect</color> that occurs by chance.
5th Skill - Using the 5th skill you can increase each
hunter’s <color='255,156,0,255'>unique effect regularly</color>.

### CONTENTS4_5 — Locking Feature

Do you know about the locking feature?
It is a feature to <color='255,156,0,255'>secure</color> hunters to prevent
you from using them for training or
advancement.
Note that <color='255,156,0,255'>you can’t use</color> hunters who are set
 on your exploring team, Fight Club’s offense
 or defense team.

### CONTENTS4_6 — Fate Stories

Do you know the fate of each hunter in
Midgard?
Each hunter has its own story, and when
collecting hunters that relate to each other,
their fate is activated.
When the fate is activated new stories will
open, and the hunters’ <color='255,156,0,255'>ability</color> will increase
<color='255,156,0,255'>permanently.</color>

### CONTENTS4_7 — Hunter Role Bonus

You can increase hunters’ <color='255,156,0,255'>Role Bonus</color> when
recruiting various hunters! This bonus exists
for each role and this effect applies to <color='255,156,0,255'>all the
hunters.
</color>Collect all Midgard hunters to get maximum
bonus!

### CONTENTS4_8 — Group Advancement

The group advancement feature uses the lower grade <color='255,156,0,255'>hunters at random.
</color>It is a convenience feature that<color='255,156,0,255'>trains and
advances</color>the grouped hunters at once.
 Note that the hunters who have been skill
trained or earned experience won’t be used.

Hunters needed for ★1->★2 group advance:
FOUR ★1 HUNTERS
Hunters needed for ★2->★3 group advance:
FIVE ★2 HUNTERS

### CONTENTS5_1 — Fight Club Auto Feature

There are 3 modes for Fight Club battles.
When battling in Fight Club, you can change
the mode by clicking on the round button on
<color='255,156,0,255'>the bottom left.</color>
Manual - Control all your hunters activity <color='255,156,0,255'>
manually.</color>
Auto - Everything is automatic such as
activating skills and swapping teammates.
Tap Auto - <color='255,156,0,255'>Tapping is automatic</color>, the skill
activating and swapping is manual.

### CONTENTS5_2 — Fight Club Battle’s Time Limit

Did you know that Fight Club also has a <color='255,156,0,255'>time
limit?</color>
When you can’t defeat your opponent’s team
in time you will <color='255,156,0,255'>lose</color>.

### CONTENTS5_3 — Hidden Defense Team

To defend your team from your attacking
opponent in Fight Club, you need to set a
strong defense team.
You can select some hunters to <color='255,156,0,255'>hide them
from your opponent.</color>
Use the hiding option to form a strategic lining
of your defense hunters!

### CONTENTS5_4 — Checking Rankings

There are <color='255,156,0,255'>three</color> different rankings.
My Rank - You can know your current ranking.
Friend Rank - You can know your friends’
rankings.
Leaderboards - You can know all users’
 rankings.

### CONTENTS5_5 — Revenge

Someone challenged you and you lost your
point. Don’t worry! You can revenge them.
You can check this feature by clicking <color='255,156,0,255'>Defense</color>,
and see which user battled with you and the
results. You can <color='255,156,0,255'>revenge</color> opponents who have
attacked you and won.

### CONTENTS5_6 — Friendly Match

Friendly Match is just between Captains who
are your friends.
You <color='255,156,0,255'>don’t lose anything</color> or use any materials when you are doing a Friendly Match.
So, battle your friends carelessly!

### CONTENTS6_1 — What is an Abyss?

The Abyss is a place where you can collect
Metron Crystals and skill materials that make your hunters <color='255,156,0,255'>stronger</color>. Different abysses are
set to open on different days.
 At first, you can excavate 1 time on a set day,
but you can do a reset up to 3 times
depending on your Veteran rank.

### CONTENTS6_2 — Missing Hunters

Find the missing hunters!
You can search for missing 2★ hunters for a
limited number of times by going to Gullveig’s
 Challenge.
The hunters <color='255,156,0,255'>change every week</color> so remember to check the schedule!

### CONTENTS6_3 — Rare Search

When completing general areas, you will some
times find 3★ hunters hidden ruins by chance.
Remember to clear the hidden ruins before it
closes as they have a <color='255,156,0,255'>set time</color>.

### CONTENTS6_4 — Unique Search

If you’re very lucky, you can sometimes find
unique ruins after completing rare ruins!
You can earn <color='255,156,0,255'>better rewards</color> from unique ruins than the rare ones and can clear them with
your friends.
You can get <color='255,156,0,255'>extra rewards</color> when more of your friends participate in your ruin.
 So try to tell many people.

### CONTENTS6_5 — Unique Search Waiting Time

Did you know that the unique ruins you or
your friends find has a waiting time after
completing?
You cannot enter unique ruins again until this
time is over.
But you can <color='255,156,0,255'>immediately reset</color> the waiting time using Manda.

### CONTENTS6_6 — Unique Search Alarm

The <color='255,156,0,255'>more friends you have that participate</color> in your ruin, the more rewards you get.
 So make more friends!
When you find a unique ruin your friends will
get a <color='255,156,0,255'>push alarm</color> and it will also be announced on the General Chat!

### CONTENTS6_7 — Missing Hunter Big Rewards

While you are on your search for missing
hunters you can win <color='255,156,0,255'>Big Rewards</color> by chance.
You can get that Hunter’s Traces, Rupees,
Request scrolls, Metron Crystals and other
unexpected items.
So, don’t forget to go on hunter searches!

### CONTENTS7_1 — Market Goods

Running out of materials? Visit the market that sells various goods!
The list of items in Rupee Shop and Fight
Chips Shop will change after a certain time.
Also, you can renew the list of items by using Manda!


Rupee Shop: Use the <color='255,156,0,255'>Rupees</color> you have earned to buy
necessary goods.
Fight Chips Shop: Use the <color='255,156,0,255'>Fight Chips</color> you have earned from Fight Club to buy necessary goods.
Manda Shop: Use <color='255,156,0,255'>Manda</color> to buy necessary goods.

### CONTENTS7_2 — Item Origin and Description

Have a specific item you need but don’t know where to get them?
Don’t worry! Click on the item information icon and see the <color='255,156,0,255'>origin</color> and the <color='255,156,0,255'>description</color> of the
item.
By using this you can <color='255,156,0,255'>go to get that item
instantly</color>, so make use of it!

### CONTENTS8_1 — About Hunter Traces

Do you know about Hunters’ Traces?
You can earn Hunter Traces through your
battles.
After you have collected all the Hunter Traces that is required you can <color='255,156,0,255'>immediately recruit</color>
them.

### CONTENTS8_2 — Coupons & Tickets Instructions

There are 3 types of lottery like tickets and
coupons such as Rupees, Fuel, and Challenge
Invitations.
By a rare chance you can win the lottery and
get a <color='255,156,0,255'>tremendous amount!</color>

### CONTENTS8_3 — Sharing Feature

Did you get lucky and recruit a hunter you
wanted?
Share it on your social media and tell your
friends!
When sharing via SNS you can get <color='255,156,0,255'>Rupee
rewards</color> once on your first share a day!

### CONTENTS8_4 — Nickname Change

Want to change your nickname?
You can get <color='255,156,0,255'>1 free change per account</color>.
If you want to change your nickname again you can do so by using Manda.

### CONTENTS8_5 — Linking Account

You can <color='255,156,0,255'>secure your account and record</color> by
linking Blustone to either your SNS or Email.
It is highly recommended for users who are
changing their device or reinstalling the app.

### CONTENTS8_6 — Veteran Ticket

Do you know about the Veteran Tickets?
You can give other users Veteran Tickets and it will increase <color='255,156,0,255'>that user’s veteran points</color>.
You can get Veteran Tickets when you win the lottery with a coupon or a ticket.

### CONTENTS8_7 — Veteran Rank

Do you know about the Veteran Rank?
The more you are active and popular in
Midgard, the higher your Veteran Rank you’ll be. There are many <color='255,156,0,255'>useful features</color> and <color='255,156,0,255'>various benefits</color> you can get when your Veteran Rank
is higher.
You can raise your Veteran Rank through
attendance checks or package purchases.

### CONTENTS8_8 — Blocking

Was there a user who made you feel
uncomfortable in the General Chat?
Then you can <color='255,156,0,255'>block that user</color>.
Even if you accidentally blocked someone by
mistake, you can unblock them by going
to the Menu-Settings-General Chat Settings.

### CONTENTS9_1 — About Mirage Ruins?

It has not been discovered yet how deep the
Mirage Ruins are and how far you can go.
The enemies that pop in and out of the Mirage Ruins look exactly like the hunters in Midgard and the <color='255,156,0,255'>further down you go</color> into the ruins the stronger the enemies get.
You will be able to collect <color='255,156,0,255'>more</color> Mirage
Fragments the stronger your enemies are.

### CONTENTS9_2 — Sortie Team

You can take <color='255,156,0,255'>all your hunters that you have</color> to challenge the Mirage Ruins.
If you have <color='255,156,0,255'>many of the same hunters</color>
only the <color='255,156,0,255'>strongest one</color> out of them can be
 taken to go on a sortie.
<color='255,156,0,255'>Once you decide</color> which one you will take,
it will be fixed to that hunter, until you have
cleared the ruins.

### CONTENTS9_3 — Ruins Battle

The mirage ruins are going to be <color='255,156,0,255'>5 vs 5</color> battle strategy.
As you are conquering the ruins, the <color='255,156,0,255'>strength
consumed</color> during the battle of the level in
process, your <color='255,156,0,255'>health is not recovered</color> due to
the ruin’s power.
Also, when your <color='255,156,0,255'>hunter completely passes out</color> that hunter will <color='255,156,0,255'>no longer be able to fight.</color>

### CONTENTS9_4 — Re-entry

The ruins will reset once a day, at 12:00AM
each day.
 When you click the retry button you will be able to enter the ruins again, but when you are just re-entering to a level you made progress
on this <color='255,156,0,255'>data will reset from the start.</color>
So please be aware of that.

### CONTENTS9_5 — Mirage Market

Mirage fragments will be used as the currency for Mirage Market.
We suggest you collect Mirage Fragments to
get your hands on <color='255,156,0,255'>special and valuable items!</color>
The Mirage Market items will automatically
reset every day at 12:00AM, and the maximum
times you can reset with purchase is 3 times.

### CONTENTS9_6 — Active Hunters

A <color='255,156,0,255'>minority of hunters</color> will get the Mirage Ruin
’s mysterious powers and be <color='255,156,0,255'>stronger than
usual</color>.
<color='255,156,0,255'>While they are in the ruins</color> they will be able to activate more power and this power will
alternate to different hunters every few days.

### CONTENTS9_7 — Strategy Status

The level where your <color='255,156,0,255'>strategy is in process</color>
and the <color='255,156,0,255'>highest level</color> you have cleared will
be displayed.
When viewing the strategy status you will be able to see your friends’ highest level reached.How about competing with your friends to go
to the most challenging ruins?

### CONTENTS9_8 — How to Enter!

You can enter the Mirage Ruins by going to the Excavation Association where Gullveig is.
You will get an entrance notice when you clear above stage 27 in the general stages.
And after you have cleared that you will be
able to enter the Mirage Ruins by clicking on
Gullveig's third option 'I want to challenge the Mirage Ruins!'

### CONTENTS9_9 — Assigned Floors

It is said that the Mirage Ruins are assigned
according to the <color='255,156,0,255'>average combat power of your
team</color>. And if you <color='255,156,0,255'>clear the entire battles in the floor</color> you are on and re-enter then you will go <color='255,156,0,255'>down to a deeper</color> level. If you <color='255,156,0,255'>fail to clear that floor</color> then you will move slightly <color='255,156,0,255'>higher to the surface</color>. The deeper the ruins level, the
stronger the rewards will be, but it is better to be well-prepared for a readmission as the
mirage hunters will be stronger too.

### CONTENTS9_10 — Stage Structure of Mirage Ruins

The Mirage Ruins' first ground is composed of
<color='255,156,0,255'>3 battles</color> between the floors <color='255,156,0,255'>1 to 20, 6 battles
with 21 to 40</color>, and <color='255,156,0,255'>9 battles with 41 and above</color>.
The level of difficulty varies considerably with the higher number of battles, so there is a
significant difference in the volume of prizes.
Strengthen your team and clean up the mirage sites every day to receive a bigger reward
as soon as possible!

### CONTENTS9_11 — Recover the Fainted Hunter

It is possible to recover a hunter that has
passed out and can no longer battle in the
Mirage Ruins <color='255,156,0,255'>using Manda</color> to offer a
limited-use of a <color='255,156,0,255'>first aid kit</color>.
The first aid will return a hunter's HP and can be <color='255,156,0,255'>immediately put into the next battle</color>.

### CONTENTS9_12 — New 4★ Hunter, Harley's Traces

While there are many useful products in the
mirage market, <color='255,156,0,255'>Harley's trace</color> is a special item that can <color='255,156,0,255'>only be obtained in the mirage market</color>.Harley is a powerful 4-star, ice-defender and
will not be able available through Lottery
Mouse's draw inthe future, but only through
the mirage market.

### CONTENTS10_1 — Midgard Fishing

Midgard is a cold, rough place but as
temperatures have warmed in recent years,
fishing spots are emerging here and there.
You can catch various <color='255,156,0,255'>FISHES</color> in the fishing
spots and can sell them in the market.
And, of course, you could compete with other
Captains for a big fish.

### CONTENTS10_2 — Select Bait

You need to choose your fishing bait to start
fishing. <color='255,156,0,255'>AVERAGE BAIT</color> isn't the most effective
but is inexpensive, on the other hand <color='255,156,0,255'>HIGH-
QUALITY BAIT</color> is as effective as its price.
Both are available for immediate purchase at
the fishing areas.

### CONTENTS10_3 — Start Fishing

The distance gauge will charge when you have selected your bait. Start Fishing by selecting
the area you want to throw your fishing float
and click the throw button. Aim near or far.
Depending on the distance, you might catch
a different fish.

### CONTENTS10_4 — Waiting

Patience is the beauty of fishing. Enjoy having conversations with other Captains while fishing. No worries! You will be alarmed in the chat
when your bait has been bitten.

### CONTENTS10_5 — Bite

In order to pull your fish, you need to wait for your fish to be hooked well. When your fishing float wobbles and drowns, it will start <color='255,156,0,255'>SHAKING.</color> Click the pull button then.

### CONTENTS10_6 — Compete Strength

Quickly tap the screen to fill the strength
gauge. But you must be careful. Occasionally, a fish can get into a <color='255,156,0,255'>FURY STATE.</color>
If you keep tapping while the fish is angry, the line will snap and you will lose your fish.
At this time, stop tapping the screen and wait until the fish is exhausted.

### CONTENTS10_7 — Check & Sell Fish

Check the size of your fish in your fishing
basket.
A big fish will have a gold or silver crown.
The ones with a gold or silver crown can be
sold for a higher price in the market.
But of course, the fish with the gold crown is
bigger and more expensive.

### CONTENTS10_8 — Withdraw Bait

Your bait will be used if you fail or cancel
fishing after you feel a bite.
But, you can bring back your bait anytime
before then. So if you have other business
to take care of, withdraw your bait before you
catch something!

### CONTENTS11_1 — What is Equipment?

- A hunter has three types of equipment:
Weapons, armor, and accessories.
- You can upgrade all equipment, and you can also increase item-specific ability stats.
Weapon: ATK + Attack related ability stats
increase
Armor: DEF + Defense related ability stats
increase
Accessories: HP + Other ability stats increase

### CONTENTS11_2 — Upgrading Equipment

- Upgrade each piece of equipment and make your hunter stronger.
- To upgrade your equipment, you need rupees and a Toolbox.
- You can often find Toolboxes in the
Mirage Ruins.
- But keep in mind, the maximum upgrade level of all equipment is based on the modification
grade.

### CONTENTS11_3 — Modify Equipment

- You can upgrade your equipment to levels 10, 20, 30, and 40, then you can modify your
equipment.
- Modifying your equipment significantly
increasesthe ability of the equipment and the
maximum upgrading limit expands.
- Different materials are required for hunters
of different elements to modify their equipment. Fire Element: Flammable Material, Ice Element: Coolant, Electricity Element: Lightning Box
- Modification materials can rarely be found in the Mirage Ruins.

### CONTENTS11_4 — What are Jewels?

- A rare type of Metron Crystals. If you mount them on a piece of equipment, the hunter's
overall ability will increase.
- These Jewels are rated in different classes,
and the higher their class is, the higher the
ability it provides.
- By design, you can collect Jewels through
mining.
- But you can find them through Hunter Search if you are lucky, and they are also sold at the Market.
- Polishing the Jewels can further enhance
their effectiveness.
- Wearing multiple Jewels of the same kind
can make the Jewels come together to create
a powerful synergy effect.

### CONTENTS11_5 — Mining Jewels

-The Hunter Union supports free mining every day.
- You can select the kind of Jewel you want,
and you will mine a random Jewel of that kind.
- In addition to free mining, you can acquire
rarer Jewels by using Manda to mine.
- Advanced mining will enable you to acquire
higher-class Jewels quicker.

### CONTENTS11_6 — Polishing Jewels

- You can use the Jewels as they are but if
you polish them, you will increase their
effectiveness.
- You don't need particular materials to polish them, but you need large sums of rupees.
- The higher the stage at which you are
polishing is, the more difficult polishing the
Jewels will be in terms of probability.
- If you fail to polish the Jewels, the rupees
you used will be lost, but there are no further
ramifications beyond that.

### CONTENTS11_7 — Mounting Jewels

- To activate the true power within the Jewels,
you need to mount Jewels to the rabbets
in your equipment.
- There are three types of equipment
that have rabbets
where the Jewels can be mounted on: Weapons, armor, and accessories.
- The shape of the Jewels has to match the
shape of the rabbet for each piece of
equipment you wish to mount with Jewels.

### CONTENTS11_8 — Set Effect

- You can apply the set effect by mounting the same Jewels required.
- Having the sufficient number of Jewels will
activate the effect regardless of where you
mount the Jewel.
- The same set effect is available many times.

HP Jewel - Mount 2, Increase HP 5%
Offensive Jewel - Mount 2, Increase AP 5%
Defensive Jewel - Mount 2, Increase DP 5%
Critical Jewel - Mount 2, Increase Critical Attack Chance 4.5%
Block Jewel - Mount 2, Increase Block Chance 4.5%
Fatal Jewel - Mount 4, Increase Critical Attack Damage 50%
Super Block Jewel - Mount 4, Damage Reduction Rate
Increase 5%
Element Jewel - Mount 4, Increase Elemental Enhancement 23
Resistance Jewel - Mount 4, Increase Elemental Resistance 23 Speed Jewel - Mount 4, Increase Attack Speed 1.72
Regeneration Jewel - Mount 4, Increase HP Regeneration 30
Penetration Jewel - Mount 4, Increase Armor Penetration 12
