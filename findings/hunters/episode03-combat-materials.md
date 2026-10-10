# E03 original combat actors and materials

2026-10-08. Read-only original final PAD packages, original recovered JSON and retained native contracts. Only this report written. No ADB, Ghidra, profile/save/server/source changes, original writes, grants, APK rebuilds or web stat hunt. Native E03 combat and residency pending.

## Encounters and exact identity

CB0301 is E03_S02 / EP_0702A despite original stage_name E03_S03_TITLE. Four owned empty left slots versus three CB0301_M1/M023 then CB0301_013_1/ref013/resC013 (Denali). Predicted generated right serials5,6,7,8/camp1; actual left owned high IDs/camp0. Power4500, game_res_id string3, BGM_GULLVEIG, win EP_0703B. CB0302 is E03_S05 / EP_0802A: four owned empty slots versus CB0302_010_1/ref010/resC010 (Vincent), predicted serial5/camp1. Power5800, game_res_id string7, BGM_BATTLE3, win EP_0802B. Both losses EP_0000A/EP_0000B. No fixed left ally or owned Denali/Vincent grant. Native serial/pointer/camp corroboration required.

## Encounter-specific original stats

Original EPISODE_STAT_ACTORS.json is authoritative; values below are encounter definitions, not ordinary card base/growth data. Field strings and omissions are preserved. M023 E03 ATK650/DEF160/regen10 differ from E02 ATK400/DEF130/regen8. Thumbnail level30 does not justify added ordinary growth.

- CB0301_M1: resM023, attr1, role1, cool_time5000. Stat {"rank":"2","hp":"700","atk":"650","def":"160","spd":"0","crt_chance":"20.00","crt_dmg":"200","penetration":"0.00","attr_enhance":"0","block_chance":"20.00","block_dec_dmg":"20","attr_resist":"0","hp_regen":"10"}.
  Original skill type/target-rank pairs [].
- CB0301_013_1: resC013, attr1, role4, cool_time5000. Stat {"rank":"3","hp":"1300","atk":"500","def":"160","spd":"5.00","crt_chance":"20.00","crt_dmg":"200","penetration":"0.00","block_chance":"20.00","block_dec_dmg":"30","attr_resist":"0","hp_regen":"10"}.
  Original skill type/target-rank pairs [(1, 1), (2, 2), (4, 4), (5, 5)].
- CB0302_010_1: resC010, attr3, role1, cool_time5000. Stat {"rank":"4","hp":"3000","atk":"310","def":"210","spd":"5.00","crt_chance":"30.00","crt_dmg":"200","penetration":"10.00","block_chance":"30.00","block_dec_dmg":"30","attr_resist":"99","hp_regen":"0"}.
  Original skill type/target-rank pairs [(1, 1), (2, 2), (4, 4)].

CB0301 thumbs: M023 level30/rank2/hyper0/attr1, skills `[0,0,0,0,0]`; Denali level30/rank3/hyper0/attr1, `[1,1,0,1,0]`. Denali actual definitions types1,2,4,5: no synthesized type3 or enabled type5. Type1 cost4/cool_time8000. CB0302 Vincent thumb level1/rank4/hyper0/attr3, `[1,1,1,1,0]`; actual definitions only types1,2,4, not invented type3. Type1 cost3/cool_time6000. Exact effect arrays remain original, including Vincent base_number -2000 health effect and -3/stat16 effect; no English semantics or balance rewrite inferred.

JSON monster alone does not prove generic Mob backend. Prior root CB0201 verified M023 native Hunter/Image body; Episode actors bind local STAT. No new global GetMonster fixture warranted. Fresh E03 verify actual primary/body branch/resourceID/serial pointer/camp using guarded observer; thumbnails alone insufficient.

## Explicit profile gaps and hashes

Current 34groups/70folded-assets explicitly select M008 and ST001. New combat families are eight C013/C010 base/Q/EFT/SND packs, ST003 and sound-only C018_SND: ten additive combat packs. Dialogue/audio gaps are in episode03-entry-materials.md. No ST007, variant C013A/C010A or full C018 art requirement. Complete base11 duplicate ownership not audited; explicit genuine packs avoid that inference.

- C013.jet: 745049 bytes/6 records, SHA256 `be6a19cabdbecc1487fd2ba82588560c62de481012f398cbba78452862224733`. Complete header walk ends at filesize.
- C013_Q.jet: 47270 bytes/39 records, SHA256 `1a09892b4e9ac4809b83e9e60a54f768d790caf98024677e85726eba8dd8d583`. Complete header walk ends at filesize.
- C013_EFT.jet: 3741764 bytes/6 records, SHA256 `4b673e0b3e3f84383629cb19d20ffcd04ada5bb25de6344714275c1dca662911`. Complete header walk ends at filesize.
- C013_SND.jet: 115037 bytes/3 records, SHA256 `e46aa30fe6afc99b3ef9172a4aaa0fa3ebc3d1b499839e87a34f4cc2f6ba59ed`. Complete header walk ends at filesize.
- C010.jet: 2759458 bytes/9 records, SHA256 `3592c448aca8b7096f4adde8420e2ef19988cc6e452c23ef513f0e4fc6c59067`. Complete header walk ends at filesize.
- C010_Q.jet: 53683 bytes/45 records, SHA256 `f2a19358c627047df72baa8329428147e70f8a0d36960b1e0a3996301985955d`. Complete header walk ends at filesize.
- C010_EFT.jet: 3818579 bytes/13 records, SHA256 `692d3a46d7eddf39fb9b526b713d171c9e79d1b250e6408aa231bf62d87eb797`. Complete header walk ends at filesize.
- C010_SND.jet: 175008 bytes/9 records, SHA256 `e32a4e85807a49e2961ebc5de7b178295c9c818c20816df92f85528ba1879df9`. Complete header walk ends at filesize.
- ST003.jet: 1181521 bytes/20 records, SHA256 `a58c3a55a0b89c4beaf73bc46babac9b837874c5dabad88bc1b7c099fcd87e61`. Complete header walk ends at filesize.
- C018_SND.jet: 95425 bytes/4 records, SHA256 `e1b1ffaeb0dd44c9a01a87c1f225097ab99cef553b3bfb496d6643d244c1bf3d`. Complete header walk ends at filesize.
- M008.jet: 223669 bytes/134 records, SHA256 `04b37480c31248de3a2a23f09901961923441a9ba7524abae037a0eb805074f5`. Complete header walk ends at filesize.
- ST001.jet: 1733825 bytes/42 records, SHA256 `9948876a679a9cfce6a88233c7985e82b641137f639fae2aff8167e614e32cd7`. Complete header walk ends at filesize.

## Closed AT → S2 → I2 graphs

Header uint32 packed size+8/uint64 ID+12; base38 alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`; raw or zlib body per original bytes. AT count uint32+43, frames+47, each uint64 ref/float duration/uint16 eventlength/eventbytes; variable events consumed and final cursor equals full body. S2 image uint64 **+46**, not reserved+2. All following edges resolve with exact type in same original pack. I2 decoded by existing decode_i2_texture and PNG opened with Pillow. Alpha counts use decoded alpha plane rather than compressed PNG bytes; no images written.

### M023 in M008.jet

12 AT / 21 referenced S2 / 12 I2, zero missing/type-mismatched edges.

- M023_AS1 → M023_SHA.
- M023_AS2 → M023_SHA.
- M023_AS3 → M023_SHA.
- M023_DIE → M023_H10.
- M023_H1 → M023_H01,M023_H02,M023_H03,M023_H04,M023_H05.
- M023_H2 → M023_H06,M023_H07,M023_H08,M023_H09,M023_H10.
- M023_H3 → M023_H11,M023_H12,M023_H13,M023_H14,M023_H15.
- M023_R1 → M023_R01,M023_R02,M023_R01,M023_R03,M023_R04,M023_R03,M023_R04.
- M023_R2 → M023_R01,M023_R02,M023_R01,M023_R03,M023_R04,M023_R03,M023_R04.
- M023_S → M023_R01,M023_R02,M023_R01,M023_R03,M023_R04,M023_R03,M023_R04.
- M023_SHADOW → M023_SHA.
- M023_TH → M023_THN.

- I2 `0x373bc07e` header86241: 151×129, positive-alpha pixels11161.
- I2 `0x56db90b4` header99122: 141×113, positive-alpha pixels10236.
- I2 `0x6f7bd8f8` header121669: 123×112, positive-alpha pixels10544.
- I2 `0x8a512831` header203258: 94×99, positive-alpha pixels6473.
- I2 `0x90708bc3` header73638: 149×110, positive-alpha pixels10726.
- I2 `0x911bc848` header128121: 121×105, positive-alpha pixels9339.
- I2 `0xa1b77c03` header79907: 153×126, positive-alpha pixels10909.
- I2 `0xa541ada7` header92904: 158×110, positive-alpha pixels11272.
- I2 `0xaa0260a1` header114345: 139×169, positive-alpha pixels13631.
- I2 `0xafd827e3` header67058: 150×120, positive-alpha pixels11415.
- I2 `0xd51d4c77` header105419: 145×173, positive-alpha pixels14731.
- I2 `0xf93af6a1` header196991: 157×31, positive-alpha pixels3610.

### STI003 in ST003.jet

6 AT / 6 referenced S2 / 5 I2, zero missing/type-mismatched edges.

- STI003_A1 → STI003_A01.
- STI003_B1 → STI003_B01.
- STI003_C1 → STI003_C01.
- STI003_D1 → STI003_D01.
- STI003_E1 → STI003_E01.
- STI003B → STI003B_01.

- I2 `0x8966623b` header1049765: 441×280, positive-alpha pixels107145.
- I2 `0xa0b7e1aa` header1029258: 352×280, positive-alpha pixels89458.
- I2 `0xb3f79378` header906710: 480×568, positive-alpha pixels272640.
- I2 `0xc2d110ba` header1142317: 384×230, positive-alpha pixels88320.
- I2 `0xd75f7458` header1096233: 692×230, positive-alpha pixels100280.

### STI001 in ST001.jet

6 AT / 6 referenced S2 / 5 I2, zero missing/type-mismatched edges.

- STI001B → STI001B_01.
- STI001_A1 → STI001_A01.
- STI001_B1 → STI001_B01.
- STI001_C1 → STI001_C01.
- STI001_D1 → STI001_D01.
- STI001_E1 → STI001_E01.

- I2 `0x4a79564` header1692282: 424×230, positive-alpha pixels97520.
- I2 `0x141d2abc` header1562171: 453×280, positive-alpha pixels111633.
- I2 `0x2e13da2d` header1615641: 892×230, positive-alpha pixels164432.
- I2 `0xf838c823` header1392330: 480×568, positive-alpha pixels272640.
- I2 `0xfab59e57` header1525672: 441×280, positive-alpha pixels115202.

### C013 in C013_Q.jet

11 AT / 11 referenced S2 / 11 I2, zero missing/type-mismatched edges.

- C013_WP → C013_WEP.
- C013_AM → C013_AMOR.
- C013_AC → C013_ACCRY.
- C013_STH → C013_STHN.
- C013_TH → C013_THN.
- C013_SI1 → C013_SI01.
- C013_SI2 → C013_SI02.
- C013_SI3 → C013_SI03.
- C013_SI4 → C013_SI04.
- C013_SI5 → C013_SI05.
- C013_SHADOW → C013_SHA.

- I2 `0x26bc46d4` header45333: 84×29, positive-alpha pixels1818.
- I2 `0x35121dd8` header41189: 64×64, positive-alpha pixels2006.
- I2 `0x38b00ea8` header38287: 64×64, positive-alpha pixels1355.
- I2 `0x434e93f2` header9789: 175×210, positive-alpha pixels25301.
- I2 `0x53b3a0c9` header42342: 64×64, positive-alpha pixels2237.
- I2 `0x652bb91c` header28484: 98×132, positive-alpha pixels8486.
- I2 `0x745d3764` header3509: 65×83, positive-alpha pixels3899.
- I2 `0x8b16f8da` header39838: 64×64, positive-alpha pixels1845.
- I2 `0x94498010` header1582: 75×79, positive-alpha pixels2848.
- I2 `0xc63c8b46` header7204: 49×50, positive-alpha pixels1856.
- I2 `0xeada11fc` header43717: 64×64, positive-alpha pixels1967.

### C010 in C010_Q.jet

11 AT / 11 referenced S2 / 11 I2, zero missing/type-mismatched edges.

- C010_WP → C010_WEP.
- C010_AM → C010_AMOR.
- C010_AC → C010_ACCRY.
- C010_TH → C010_THN.
- C010_STH → C010_STHN.
- C010_SI1 → C010_SI01.
- C010_SI2 → C010_SI02.
- C010_SI3 → C010_SI03.
- C010_SI4 → C010_SI04.
- C010_SI5 → C010_SI05.
- C010_SHADOW → C010_SHA.

- I2 `0x55a6ed73` header19171: 157×210, positive-alpha pixels23322.
- I2 `0x5883bd0f` header0: 82×71, positive-alpha pixels2024.
- I2 `0x60720ea7` header47103: 84×29, positive-alpha pixels1795.
- I2 `0x90d37c24` header40594: 64×64, positive-alpha pixels1487.
- I2 `0x9a0f2cf4` header38822: 64×64, positive-alpha pixels2110.
- I2 `0xe294cb3e` header42127: 64×64, positive-alpha pixels2291.
- I2 `0xe5013adf` header9960: 90×114, positive-alpha pixels6980.
- I2 `0xeaa04940` header45465: 64×64, positive-alpha pixels2262.
- I2 `0xece8a3fb` header5987: 60×78, positive-alpha pixels1700.
- I2 `0xeedbe728` header2403: 65×93, positive-alpha pixels4493.
- I2 `0xffcde097` header43705: 64×64, positive-alpha pixels2498.

## Spine atlas/page and external material closure

Original RW texture/atlas/binary skeleton triads retained intact. Atlas pages resolve to original same-pack uppercase base names, all pages decode, all regions are in bounds including rotated dimensions. Bounded skeleton material symbols resolve to same-base EFT/SND plus C018_SND. This lane does not implement a full Spine attachment/skin/timeline binary parser; full binary semantic validation and native processed animations remain pending. Do not call bounded atlas/events ownership a complete binary skin-graph validation.

### C013

- C013_A: 58 atlas regions, all in bounds; pages C013.png.
  Texture C013 header0, 1024×512, positive-alpha pixels186411.
- C013_DA: 10 atlas regions, all in bounds; pages C013_d.png.
  Texture C013_D header439842, 1024×1024, positive-alpha pixels542799.
- C013_B header407168, inflated100007, RW SHA256 `26700fd4b2c88239a3f5d031e5fcc4e08ce1bedd9485fe8e532374d0ac9be1a3`.
  Bounded external symbols: C013_E01 [C013_EFT], C013_E02 [C013_EFT], C013_EC [C013_EFT], C013_SND01 [C013_SND], C013_SND02 [C013_SND], C013_SND03 [C013_SND].
- C013_DB header744574, inflated1037, RW SHA256 `51db4d5c293c529c246ad0c667303b3c6becc16324f5a61f053df710ba10ff8c`.
  Bounded external symbols: none matching bounded character-EFT/SND pattern.

### C010

- C010_A: 36 atlas regions, all in bounds; pages C010.png.
  Texture C010 header0, 1024×1024, positive-alpha pixels379500.
- C010_DA: 20 atlas regions, all in bounds; pages C010_d.png,C010_d2.png,C010_d3.png,C010_d4.png.
  Texture C010_D header764572, 1024×1024, positive-alpha pixels558364.
  Texture C010_D2 header1283686, 1024×1024, positive-alpha pixels454331.
  Texture C010_D3 header1964619, 1024×1024, positive-alpha pixels417454.
  Texture C010_D4 header2583336, 512×512, positive-alpha pixels70947.
- C010_B header734641, inflated100626, RW SHA256 `48174fa9f9c2f9a2c7036eb32f4b29a7e6e54feab33162de9f543c7af5c6ffa3`.
  Bounded external symbols: C010_E01 [C010_EFT], C010_E02 [C010_EFT], C010_E03 [C010_EFT], C010_E04 [C010_EFT], C010_E05 [C010_EFT], C010_E06 [C010_EFT], C010_EC [C010_EFT], C010_SND01 [C010_SND], C010_SND02 [C010_SND], C010_SND03 [C010_SND], C010_SND04 [C010_SND], C010_SND05 [C010_SND], C010_SND06 [C010_SND], C010_SND07 [C010_SND], C010_SND08 [C010_SND], C010_SND09 [C010_SND], C018_SND01 [C018_SND].
- C010_DB header2731201, inflated88973, RW SHA256 `2d0b753d0dbea35fb518a1188baba05a8f0d79795f1443fce4ce4755893ab2f0`.
  Bounded external symbols: none matching bounded character-EFT/SND pattern.

**C010_B cross-family dependency C018_SND01 is absent C010_SND.** Original C018_SND.jet has C018_SND01..04; restore this sound-only pack. Regex presence identifies actual byte-string ownership, not which animations execute or proof sound played.

## Environment binding

Original environments.csv row3 prefix STI003 (Red Rock): A111/-5/0, B111/-20/80, C111/-40/210, D111/-60/580, E111/-20/850. Row7 prefix STI001 (White Forest): A111/-5/0, B11/-20/160, C111/-40/210, D111/-60/580, E111/-20/850. Config digits do not justify invented literal suffix111/11 aliases. Original A1..E1 graphs above close. Existing native contracts establish game_res_id string → OnInitBackground → ENV_INFO prefix, not ST plus numeric-ID concatenation; inspected consumer does not read field_bg_res BG_RES. No alias warranted.

ST003 also supplies ST003BG/ST003_BG. ST001 includes ST001BG and genuine STI000 aliases. Five combat parallax layers A1..E1 and extra original B graph checked. Native rendering, exact actor branches/HP/serial/camp, wins/losses and proper Story02/05 Read remain root validation. Original LEVELING_E remains existing selected Episode tuning; no stat/growth/attack-rate edit follows. Preserve actual party/earned levels and high namespace1 owned IDs.
