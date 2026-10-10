# E04 entry and original material audit

2026-10-08. Read-only final PAD headers/bodies and recovered local JSON. Only this report written. No ADB, Ghidra, server, state, profile or original writes. Native residency/playback pending.

## Progression

E04 has four stories. Original reward `{"item": [{"ref_id": "GC8", "qty": 1}], "free_iap": 0}` has unknown GC8 metadata/pool/redemption. No grant follows. All story res1 literal RES1; no alias.

- **E04_S01**: EP_0901A, battle=False, local_MIDGARD x1235/y1150, portrait C003_DIALOG.
- **E04_S02**: EP_0902A, battle=False, local_BREAD x1205/y1145, portrait C003_DIALOG.
- **E04_S03**: EP_0903A, battle=True, local_BREAD x1205/y1145, portrait C003_DIALOG.
- **E04_S04**: EP_0904A, battle=False, local_BREAD x1205/y1145, portrait C003_DIALOG.

**Original mismatch:** CB0401.stage_name is E04_S05_TITLE, but E04 has only four stories. SEASON1 links CB0401 to E04_S03, and EP_0903A terminal enters it. EP_0903B wins clear E04_S03, not a fictional fifth story.

## Original dialogue paths

Each path follows IsRoot and outgoing links; all nodes reached, no branches/nonempty conditions. Text counts include narration. Fades can ignore taps; verify final displayed line before terminal advance. RW hashes include full inflated record bytes.

### EP_0901A

Header2488392, packed2541, RW38283, SHA256 `db66190ce6b004f246d6040692ac1ca15d69a5c64383afbeebc62869125853cc`. 26 nodes/22 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→13→14→15→16→17→18→25→19→20→21→22→23→24.
First node2 %user_name%: Relaxing afternoon, chill music, fresh hot coffee. What a perfect holiday.
**Final node23 %user_name%: .... Sigh, my perfect holiday only lasted a few minutes...**
Terminal24: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Gerard/Char005, Lapis/Char017, Dumble/Char048, Narration/.
Exact named dependencies: BG002_1, BG003_1, BGM_TRAIN, C005_SND03.

### EP_0902A

Header2490957, packed2357, RW35002, SHA256 `12895aa4316f3609e568d049e3bcbdc3cad01fb7af363319dbe24f17d4cfc22f`. 23 nodes/19 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→12→13→14→15→16→17→18→20→21→22→23.
First node2 Narration: CRACK-!
**Final node22 Lapis: !!! That's right! You still have one left!**
Terminal23: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Gerard/Char005, Lapis/Char017, Dumble/Char048, Tyltyl/Char004, Narration/.
Exact named dependencies: BG002_1, BGM_COMIC1, C005_SND03, C017_SND04, FX_CLASH.

### EP_0903A

Header2493338, packed2469, RW39018, SHA256 `55b3b21e2de6db7927bfa876cfe1e2a22c9a44ab8eac34d4481adf5fce8a233b`. 26 nodes/22 texts. Path 0→1→2→3→4→5→6→7→8→9→10→11→26→12→13→14→15→16→19→20→23→27→24→25→21→22.
First node2 Tyltyl: Th-This one is not for you guys! I'm keeping it for someone else!
**Final node21 %user_name%: What's going on with these guys?!**
Terminal22: `scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; combat_goto id:CB0401`.
Speakers: %user_name%/Char009, Gerard/Char005, Lapis/Char017, Locke/Char014, Tyltyl/Char004, Bear/Char036.
Exact named dependencies: BG002_1, BGM_BATTLE2, BGM_GULLVEIG.

### EP_0904A

Header2497367, packed2178, RW30336, SHA256 `5285d1f1e4186afa29506fc04e38147710d8840eb3fb3c52d307e5c0b92911c4`. 21 nodes/18 texts. Path 0→1→2→3→21→4→5→6→7→8→9→10→11→12→13→14→15→16→18→19→20.
First node2 %user_name%: Phew... They're finally gone. How good is this pastry supposed to be? I still can't believe they were fighting for this.
**Final node19 Denali: %user_name% is such a warm-hearted person...**
Terminal20: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6`.
Speakers: %user_name%/Char009, Denali/Char013.
Exact named dependencies: BG002_1.

### EP_0903B

Header2495831, packed1512, RW14869, SHA256 `3f19da84af7fcc133051c44540be78309405cd4a00e15da1d69b62e1473591f6`. 9 nodes/6 texts. Path 0→1→2→3→8→6→7→4→5.
First node2 Lapis: Ugh... It's embarrassing that we can't even beat that stupid bear.
**Final node4 %user_name%: Oh, dear! I was so excited to finally spend a peaceful day by myself!**
Terminal5: `episode_clear ; scr-fade duration:0.6 color:(0,0,0,255) ; wait duration:0.6 ; ctrl-scene-back cnt:2`.
Speakers: %user_name%/Char009, Gerard/Char005, Lapis/Char017.
Exact named dependencies: BG002_1, BGM_COMIC1.

No numbered dialogue voice resources occur in these five XMLs (unlike E03). No extra VOICE_CDN justified by scripts; this does not prove which sounds execute.

## Combat contract

Original CB0401: `{"id":"CB0401","title":"E04_TITLE","stage_name":"E04_S05_TITLE","power":"6000","bgm":"BGM_BATTLE2","game_res_id":"99","field_bg_res":"BG_RES","win_dialog":"EP_0903B","lose_dialog":"EP_0000A","lose_dialog2":"EP_0000B","left":[[{},{},{},{}]],"right":[[{"type":"hunter","actor_id":"CB0401_005_1","thumb":{"level":1,"rank":4,"hyper":0,"attr":2},"skill":[1,1,0,1,0]},{"type":"hunter","actor_id":"CB0401_017_1","thumb":{"level":1,"rank":4,"hyper":0,"attr":2},"skill":[1,1,0,1,0]}]]}`.

- CB0401_017_1: ref017/resC017, attr2, role1, cool_time5000. Encounter stat `{"rank": "4", "hp": "1500", "atk": "280", "def": "180", "spd": "6.00", "crt_chance": "30.00", "crt_dmg": "200", "penetration": "0.00", "block_chance": "20.00", "block_dec_dmg": "30", "attr_resist": "0", "hp_regen": "50"}`.
  Skill type/target_rank pairs [(1, 1), (2, 2), (4, 4)]. Original effect arrays remain unchanged; no added type3.

- CB0401_005_1: ref005/resC005, attr2, role2, cool_time5000. Encounter stat `{"rank": "4", "hp": "2000", "atk": "240", "def": "200", "spd": "5.00", "crt_chance": "20.00", "crt_dmg": "200", "penetration": "0.00", "block_chance": "30.00", "block_dec_dmg": "30", "attr_resist": "0", "hp_regen": "50"}`.
  Skill type/target_rank pairs [(1, 1), (2, 2), (4, 4)]. Original effect arrays remain unchanged; no added type3.

Four owned placeholders; predicted right serial5 Gerard/serial6 Lapis, camp1. Fresh native pointer/camp/body corroboration required. Fixed actors do not imply owned grants. Environment99/STI099 and existing ST099 require original ENV_INFO binding, not numeric pack-name inference. Preserve namespace1 IDs, earned levels, decks and current stat projection.

## Exact original owners and missing packs

774 PAD top-level JETs walked with 24-byte headers, uint32 packed size+8/base38 uint64+12 and exact EOF. Explicit selected comparison uses saved base profile plus seven overlays through E03, without sourcing/mutating environment. Base-package duplicate contents are not globally audited.

- BG002_1: DIAL_BG2.jet header2972650/packed31.
- BG003_1: DIAL_BG2.jet header2972705/packed32.
- BGM_BATTLE2: SND1.jet header1358916/packed479408.
- BGM_COMIC1: SND_CDN.jet header4074657/packed682118.
- BGM_GULLVEIG: SND1.jet header3470466/packed646624.
- BGM_TRAIN: SND_CDN.jet header6514908/packed929968.
- C005_SND03: C005_SND.jet header59208/packed51468.
- C017_SND04: C017_SND.jet header65109/packed12894.
- FX_CLASH: SND1.jet header5799887/packed20071.

C017 base/Q/EFT/SND is complete Lapis combat family. C014 base is Locke dialogue portrait (EP_0903A). C048 base is Dumble dialogue portrait; no C048_Q/EFT/SND inferred solely from appearance. Existing C005 family covers Gerard. No character variants or owned grants.

### Bounded Spine external material symbols

- C005_B header605383, RW126152, SHA256 `73b5db413d25a4a4361e067f81daba199dab9f09be437136cdfe0175a30587c8`; symbols: C005_E01 [C005_EFT.jet], C005_E02 [C005_EFT.jet], C005_E03 [C005_EFT.jet], C005_E04 [C005_EFT.jet], C005_EC [C005_EFT.jet], C005_SND01 [C005_SND.jet], C005_SND02 [C005_SND.jet], C005_SND03 [C005_SND.jet], C005_SND04 [C005_SND.jet], C005_SND05 [C005_SND.jet].
- C005_DB header1694351, RW814, SHA256 `cca86bd7996d84d5be5c60be3a474a6458e4d200a796b37046d2aa9607606a07`; symbols: none matching EFT/SND regex.
- C017_B header446622, RW119029, SHA256 `b40f3cc419eecad5a579ffa4a9f34cd243316f858cff5b1be5e0b7a741ebf511`; symbols: C017_E01 [C017_EFT.jet], C017_E02 [C017_EFT.jet], C017_E03 [C017_EFT.jet], C017_E04 [C017_EFT.jet], C017_E05 [C017_EFT.jet], C017_E06 [C017_EFT.jet], C017_E07 [C017_EFT.jet], C017_EC [C017_EFT.jet], C017_SND01 [C017_SND.jet], C017_SND02 [C017_SND.jet], C017_SND03 [C017_SND.jet], C017_SND04 [C017_SND.jet], C017_SND05 [C017_SND.jet], C017_SND06 [C017_SND.jet], C017_SND07 [C017_SND.jet].
- C017_DB header858147, RW912, SHA256 `b9f5247f3beb3394e40dc0660c63fb61f13c8367d8555479a11121d22532af6b`; symbols: none matching EFT/SND regex.
- C048_B header329614, RW252742, SHA256 `9f7e22edd8eaa7d6c26c6763d20ec75062f0c05f37636a57e08a404edfdacf20`; symbols: C041_EC [C041_EFT.jet], C048_E01 [C048_EFT.jet], C048_E02 [C048_EFT.jet], C048_E03 [C048_EFT.jet], C048_E04 [C048_EFT.jet], C048_E05 [C048_EFT.jet], C048_E06 [C048_EFT.jet], C048_E07 [C048_EFT.jet], C048_E08 [C048_EFT.jet], C048_SND01 [C048_SND.jet], C048_SND02 [C048_SND.jet], C048_SND03 [C048_SND.jet], C048_SND04 [C048_SND.jet], C048_SND05 [C048_SND.jet], C048_SND06 [C048_SND.jet], C048_SND07 [C048_SND.jet], C048_SND08 [C048_SND.jet], C058_SND05 [C058_SND.jet].
- C048_DB header1038303, RW759, SHA256 `3d3966c5fde280dddcc349d631e36478d6a6704cd074bfa916c73d922fc82d51`; symbols: none matching EFT/SND regex.

**E04 additive entry/combat minimum: six folded packs** - C014.jet, C017.jet, C017_EFT.jet, C017_Q.jet, C017_SND.jet, C048.jet. No additional voice/environment pack.

C048_B is Dumble battle-only skeleton, unused by this chapter's portrait DB. Its C041_EC/C058_SND05/C048 effects/sounds are recorded for future Dumble combat closure, **not** E04 entry requirements. Four optional future-combat packs C041_EFT/C048_EFT/C048_SND/C058_SND are hashed below; do not add merely because battle bytes coexist with portrait in same original base pack.

- C005.jet: 1694783 bytes/6 records; SHA256 `91300b866f3728f8019f433598cdab424e88e76323feb71f8f91370f7ee15411`; selected.
- C005_EFT.jet: 3142972 bytes/12 records; SHA256 `991561e47fde62b889c0ab49d380fc1f32acd56f3e097001905d3ba02288be88`; selected.
- C005_Q.jet: 56743 bytes/39 records; SHA256 `e42fa21170173e51328f69bd97ac56252f65e0c61be41c5fef923283e4a97afe`; selected.
- C005_SND.jet: 211032 bytes/6 records; SHA256 `b5d7002b46e2fce102557866284df6ca424817c60d4788f120a40b942acfe5d7`; selected.
- C017.jet: 858562 bytes/6 records; SHA256 `e0d08b1d07c526b41d5ea3c95438c834e9875ca5110d4f74fc54bb15e3a56975`; **missing**.
- C017_EFT.jet: 1384474 bytes/16 records; SHA256 `800907c131ac6d9a7f5a530dbbc8edacc2511b59bb50d78fe83c690970aa941f`; **missing**.
- C017_Q.jet: 49164 bytes/39 records; SHA256 `6c773754a1242733743da0554a35184e7b361c6da576bfae12c1da1f2de6728b`; **missing**.
- C017_SND.jet: 151884 bytes/8 records; SHA256 `91c1fcc9fa21fafc5fac75b4b93edebbf22e4327aff989b1a1503987b279416c`; **missing**.
- C041_EFT.jet: 1624641 bytes/12 records; SHA256 `75772d466f4cec1fc6b13541988977c46135bc2e54800bdf8554e739f1fd310b`; **missing**.
- C048.jet: 1038671 bytes/6 records; SHA256 `f09f52954868d42a467e9d591204d8381a0cb6daff8cef6037dad17f398392ce`; **missing**.
- C048_EFT.jet: 2848635 bytes/18 records; SHA256 `e0441f76f60bdd970419a98ec379a529a367dac10e3c61e21aa7c48a9d6c803f`; **missing**.
- C048_SND.jet: 181536 bytes/8 records; SHA256 `e06d38a895d0e08ca89452e6b50f7b68632eb0340371bc8c0559e847388fcf0a`; **missing**.
- C058_SND.jet: 146582 bytes/5 records; SHA256 `e0d4086a0152ea757c26b67185a94ea2348f792d368a07b410b774ead0a4f070`; **missing**.
- DIAL_BG2.jet: 2973203 bytes/30 records; SHA256 `3a432787750763d8becb9bd598419a352f06a01da2b5d40bd5dad3190ae001b7`; selected.
- SND1.jet: 7173961 bytes/68 records; SHA256 `4c0e83adbfc401c19be6bbc331cf3a97b248fb837208c0717a13d5728f81c5c2`; selected.
- SND_CDN.jet: 10911430 bytes/105 records; SHA256 `a9a2cfe2250ba21c1cca953b4e1a115a2a2c06290b0c4b06e4a42f3bffb232f7`; selected.
- ST099.jet: 1252287 bytes/25 records; SHA256 `e99d2c7df04f4c32f539d4b79d44791a69f97046dd61b48d4a89211a72f50e81`; selected.

Bounded skeleton symbol ownership is not a full binary attachment/skin/timeline parser. Generated portrait IDs are not literal header records; preserve original atlas/skeleton triads. Native portraits, environment, skills, HP/serial/camp/win and correct Read are pending. GC8 metadata/pool/settlement remains unknown.

## Closed original material edges

### Spine atlas pages and texture bounds

PNG payloads are original RW bytes+6. Atlas page filename uppercased basename resolves same-pack header. Region sizes are swapped for rotate:true; all origin/rectangle extents checked. This is atlas closure, not complete binary attachment/skin/timeline semantics.
- C005_A page C005.png → C005 header0, 1024×512, positive-alpha pixels258038.
  74 regions; all page references and rotated bounds valid.
- C005_DA page C005_d.png → C005_D header639285, 1024×1024, positive-alpha pixels578028.
  7 regions; all page references and rotated bounds valid.
- C017_A page C017.png → C017 header0, 1024×512, positive-alpha pixels225795.
  57 regions; all page references and rotated bounds valid.
- C017_DA page C017_d.png → C017_D header483807, 1024×1024, positive-alpha pixels517710.
  9 regions; all page references and rotated bounds valid.
- C048_A page C048.png → C048 header0, 1024×256, positive-alpha pixels140111.
  47 regions; all page references and rotated bounds valid.
- C048_DA page C048_d.png → C048_D header397921, 1024×1024, positive-alpha pixels652913.
  7 regions; all page references and rotated bounds valid.

### AT → S2 → I2

AT uint32 frame count+43, frames+47 with uint64 ref/float duration/uint16 eventlength/eventbytes. S2 uint64 texture ID+46. Every cursor consumes exact body; images decode through project decoder and Pillow.

#### C017_Q.jet

- C017_AC → C017_ACCRY.
- C017_AM → C017_AMOR.
- C017_WP → C017_WEP.
- C017_STH → C017_STHN.
- C017_TH → C017_THN.
- C017_SI1 → C017_SI01.
- C017_SI2 → C017_SI02.
- C017_SI3 → C017_SI03.
- C017_SI4 → C017_SI04.
- C017_SI5 → C017_SI05.
- C017_SHADOW → C017_SHA.
- I2 0x4734c6f header29674, 104×118, positive-alpha pixels8605.
- I2 0x2ab3a8dc header1583, 83×61, positive-alpha pixels742.
- I2 0x38371111 header5223, 56×70, positive-alpha pixels1595.
- I2 0x3bf2c0aa header45720, 64×64, positive-alpha pixels1492.
- I2 0x45907b0a header3085, 65×61, positive-alpha pixels2862.
- I2 0x61a7ffaa header42524, 64×64, positive-alpha pixels2173.
- I2 0x7ea53bee header7916, 175×210, positive-alpha pixels27156.
- I2 0x99bed7a1 header40994, 64×64, positive-alpha pixels1449.
- I2 0xc1277d47 header44092, 64×64, positive-alpha pixels2027.
- I2 0xda667dfa header47233, 84×29, positive-alpha pixels1816.
- I2 0xe52e1122 header39468, 64×64, positive-alpha pixels1581.
11 AT / 11 S2 / 11 I2. Zero unresolved/type-mismatched edges.

#### C017_EFT.jet

No AT/S2/I2 body records (RW Spine resources); the AT graph check is not applicable and does not prove this effect pack complete. Exact requested symbol ownership is established above; native effect animations remain pending.

#### ST099.jet

- STI099B → STI099B_01.
- STI099_A1 → STI099_A01.
- STI099_B1 → STI099_B01.
- STI099_C1 → STI099_C01.
- STI099_D1 → STI099_D01.
- STI099_E1 → STI099_E01.
- I2 0x19c836f header236577, 748×306, positive-alpha pixels178855.
- I2 0x34c4c2d9 header384563, 1295×272, positive-alpha pixels334035.
- I2 0x66ce4a5d header201340, 318×105, positive-alpha pixels33390.
- I2 0x95882502 header0, 480×568, positive-alpha pixels272640.
- I2 0xbfd576b0 header65387, 342×166, positive-alpha pixels56088.
6 AT / 6 S2 / 5 I2. Zero unresolved/type-mismatched edges.

Original environments.csv row99: STI099, A111/-5/160, B11/-10/273, C111/20/648, D111/30/840, E111/-5/1000. Native OnInitBackground uses ENV_INFO prefix. Configuration digits do not justify invented literal suffix111/11 aliases. Original A1..E1 graphs close above.

### Locke original portrait (required by EP_0903A)

- C014.jet: 1597371 bytes/7 records, SHA256 `f3e8c809407139685e06c7790ca5873c6ba77d2700d6977081bd672a31f763ca`; **missing** from existing E03 selections. No C014_Q/EFT/SND required by dialogue-only Locke.
- C014_DA page C014_d.png resolves C014_D header737091, 1024x1024, positive-alpha pixels368488.
- C014_DA page C014_d2.png resolves C014_D2 header1360432, 1024x1024, positive-alpha pixels317915.
4 C014_DA regions; all page references/rotated bounds valid. C014_DB header1597025, RW1804, SHA256 `c011dcff1eafa80a8af3810e14ed5000d8f2672c4c8d1b1835be24304bdc20d3`; no bounded EFT/SND external symbols.
