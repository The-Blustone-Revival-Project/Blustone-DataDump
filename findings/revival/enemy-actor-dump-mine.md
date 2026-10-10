# enemy-actor-dump-mine — who fills the empty `+0x5c`?

Research agent, dump-mining pass, 2026-10-02. **No Ghidra, no adb, no device.**
Sources: the already-dumped `analysis/native-*.txt`, `analysis/ghidra-*.txt`,
`analysis/native-{all-strings,evidence}.tsv`, plus `server-ts/src/*`.
Read-only except this file.

> Duplicate check first: `analysis/native-makestageinst.txt` and
> `analysis/native-mstage-all.txt` are **byte-identical**
> (SHA256 `005AA6C0DB6A4E09C4D4E46EC2523C34DE1CC32C91438BFE179760BF021144CA`,
> 520246 bytes each). Only one needs reading. Line numbers below cite
> `native-mstage-all.txt`.

---

## 1. Verdict

**The dumps contain the answer.** The five empty `+0x5c` ref ids are **not**
carried by `/lobby/GetCardInven`, **not** by `/relation/GetTargetUserInfo`, and
**not** by `/mirage/GetInfo`. They are produced by
**`CSRGameMob::AddStageMonster` (0xa0d194) parsing `/reference/GetTargetStageMonster`,
and the replica's wave fixture is missing one level of array nesting.**

`AddStageMonster` iterates `ret_data[<stageId>][OUTER_KEY]` **twice nested**
before it reads `ref_id`. The replica sends

```
{ "N003": { "wave_list": [ { _id, ref_id, group, next_spawn_ms, show_thumbnail } ] } }
```

— a *single* level. So the inner loop iterates **the five values of the wave
record object itself** (`"N003_M001"`, `"001"`, `1`, `0`, `1`), asks each of them
for `["ref_id"]` (null on a string/number), `from_json(null, std::string)` yields
`""`, and the client builds **exactly five** `STAGE_MONSTER` records whose
`ref_id` is the empty string.

That is a one-for-one match with all three symptoms:

| observed | predicted |
|---|---|
| `list: ["","","","",""]` — exactly 5 | wave record has exactly 5 keys (`server-ts/src/bootstrap.ts:244`) |
| 5x `SRCard.cpp(731) sRefID.length() > 0` | 5 `STAGE_MONSTER` → 5 `CSRCard::SetRefID(local_ec, pbVar46)` with `""` |
| 1x `SRGameMob.cpp(38) Cannot find MonsterData` | `GetMonsterData("")` on the first enemy, then the fault |

**Second, independent defect, same function:** `CSRGameMob::AddMonster` (0xa0b540)
takes **no id argument** and takes the map key from the record's **first** JSON
key, which is **`_server`**. The replica's `starterMonster`
(`server-ts/src/bootstrap.ts:208-215`) has `id`/`ref_id` and **no `_server`**,
so `m_mMonsters` is keyed on an empty string and
`GetMonsterData(<any wave ref_id>)` can never hit. That is the
`SRGameMob.cpp(38)` assertion and the segfault directly.

So: **two one-line fixes in `bootstrap.ts`, and the `_server` one is provable
without another device cycle** — it follows from `AddMonster`'s signature
(§5 below).

---

## 2. Findings

### 2.1 Target 1 — who constructs the enemy `std::list<ACTOR_INFO>` for `MakeCamp`

**[RECOVERED]** `CSRMStage::MakeStageInst` (0xb33f84) is the function on the
expedition path, and it builds the enemy camp from
`CSRGameMob::GetStageMonsterLinkData()`.

`analysis/native-mstage-all.txt:6627-6703`:

```
6627:   LAB_00b34b0e:
6628:   CSRGameMob::get();
6629:   CSRGameMob::GetStageMonsterLinkData((basic_string *)&local_68);
6630:   p_Var40 = p_Stack_64;
6632:   if (local_68 == p_Stack_64) { local_134 = 0; }
...
6639:     pVar15 = local_68;
6640:     do {
...
6651:       CSRLevelData::GetMonsterGroupID((CSRLevelData *)&local_120);
6652:       local_80 = (CSRLevelData *)&local_120;
6658:            (&local_98,(CMHashID *)(this + 0x264),...)      // emplace into
6659:             //   unordered_map<CMHashID, list<list<ACTOR_INFO>>> at this+0x264
...
6690:     for (pbVar46 = *(basic_string **)pVar15; pbVar46 != pbVar24; pbVar46 = pbVar46 + 0x14) {
6691:         CSRGameActor::ACTOR_INFO::ACTOR_INFO((ACTOR_INFO *)&local_120);
6695:         *(uint *)(local_ec + 0x10) = local_138;
6696:         *(uint *)(local_ec + 0x14) = uVar17;
6697:         CSRCard::SetRefID(local_ec,pbVar46);          // <<< THE EMPTY +0x5c
6698:         *(undefined4 *)(local_ec + 0x24) = 1;
...
6716:         CSRLevelData::CalcBonus(&local_98,uVar16,1,0,uVar41,uVar25);
...
6852:       p_Var15 = p_Var15 + 0xc;                      // outer stride 0xc
6853:     } while (p_Var15 != p_Var40);
```

Read carefully, the loop nest is:

* outer: `p_Var15` steps by `0xc` — that is
  `std::vector<std::vector<...>>` on 32-bit libc++ (begin/end/cap = 12 bytes);
* inner: `pbVar46` steps by `0x14` = 20 = `sizeof(CSRGameMob::STAGE_MONSTER)`;
* `pbVar46` itself is passed **as a `std::string*`** to `SetRefID`, i.e. it is
  `STAGE_MONSTER::m_sRefID`, the first member of the 20-byte record
  (`{string ref_id; unsigned group; float spawn_s;}`).

**So `MakeStageInst` line 6697 is the `+0x5c` writer, and its argument is
`STAGE_MONSTER::ref_id` — straight out of `/reference/GetTargetStageMonster`.**

**[RECOVERED]** There are exactly **two** other `SetRefID` sites in
`MakeStageInst`, and neither can be the culprit:

* `native-mstage-all.txt:6035` — the **player deck**:
  `CSRCard::SetRefID(local_ec,(basic_string *)(local_80 + 0x5c))` where
  `local_80` comes from `CSRInventory::FindCard(inst_id)` (line 6019). Guarded by
  `if (*piVar18 != 0 || piVar18[1] != 0)` at line 6002, and `/mission/Start`
  sent `deck_inst_id_1=1, _2=0, _3=0, _4=0`, so **exactly one** iteration. It is
  the ally, and it is a `CSRCard*`, not a wave.
* `native-mstage-all.txt:6349` and `:6473` — two literal ids inside the
  `CRMDefensedData` branch:
  `CSRCard::SetRefID(pCVar9,(basic_string *)&local_68)` where `local_68` was
  just built from the literals at slots `0xb34a80` / `0xb34a8c`. The project's
  own resolver read those as **`"001"` and `"003"`**
  (`analysis/ghidra-makestageinst-keys.txt:46-47`:
  `ldr@00b3472c ... -> 0x1d7b141 "001"`, `ldr@00b348d0 ... -> 0x1d7b145 "003"`).
  Non-empty by construction. **[RECOVERED]**, and this is an independent reason
  the deck/defence branches are not the source: they cannot emit `""`.

**[RECOVERED]** The container is then handed to `MakeCamp`. The signature is in
`analysis/native-evidence.tsv`:

```
009d39e0  _ZN11CSRGameBase8MakeCampERKNSt6__ndk14listINS1_IN12CSRGameActor10ACTOR_INFOENS0_9allocatorIS3_EEEENS4_IS6_EEEE8TEAM_DIRRK8CMHashID
009e9e68  _ZN11CSRGameBase9MakeActorERKN12CSRGameActor10ACTOR_INFOEjh
009afd58  _ZN15CSRGameActorMob16MakeBackEndActorERKN12CSRGameActor10ACTOR_INFOEj
009ac2ac  _ZN18CSRGameActorHunter16MakeBackEndActorERKN12CSRGameActor10ACTOR_INFOEj
```

which matches report-009's `BLUSTONE_ARM` chain exactly
(`MakeCamp → MakeActor → MakeBackEndActor → CSRGameMob::INFO::INFO(const&) →
operator new → std::__ndk1::__tree<SRSKILL_TYPE,SRSKILL_INFO>::~__tree_iterator`).

**[INFERRED]** `MakeCamp` itself is **not decompiled anywhere on disk**
(`analysis/ghidra-enemycamp-refs-01.txt:1-4` shows only its two outgoing calls,
to `OpenCamp` 0x9d383c). I did **not** read it and am not claiming its body.
The link from `MakeStageInst`'s `unordered_map<CMHashID, list<list<ACTOR_INFO>>>`
to `MakeCamp`'s `list<ACTOR_INFO>` is inferred from the identical type names and
the fact that `MakeStageInst` is the only expedition-scene producer. **Rejected
alternative:** `CSRExploreMirage::MakeStageInst` (0x925798), which `AGENTS.md` §11
quotes — see §2.4, it is a different scene with a different data source.

### 2.2 Target 1b — `AddStageMonster`: the actual shape bug **[RECOVERED]**

`CSRGameMob::AddStageMonster(const std::string& stageId, const json& j)`,
0xa0d194, decompiled at `analysis/native-monster-stage.txt:5156-5678`.
Exactly **five** `nlohmann::basic_json::operator[](const char*)` call sites, and
the project's resolver resolved all five
(`analysis/ghidra-wave-keys.txt:1-9`, identical in `ghidra-enemy-keys.txt:5-13`):

| # | decompile site | slot | resolved string | applied to |
|---|---|---|---|---|
| 1 | `native-monster-stage.txt:5233` | `0xa0d4f4` | `_id` (0x1d76bd1) | **the whole per-stage object — then ITERATED** |
| 2 | `:5308` | `0xa0d500` | `ref_id` (0x1d6edf2) | innermost element |
| 3 | `:5325` | `0xa0d504` | `group` (0x1d658fa) | innermost element |
| 4 | `:5354` | `0xa0d508` | `next_spawn_ms` (0x1d76bdf) | innermost element |
| 5 | `:5475` | `0xa0d874` | `show_thumbnail` (0x1d76bed) | per-stage object — iterated as a **list of strings** |

The two nested loops, verbatim (`native-monster-stage.txt:5233-5262`, `5266-5301`,
`5385-5436`):

```
5233:  pcStack_70 = json["_id"];                       // outer iterator setup
5262:  while (iter != end) {                           // LOOP A
5266:      pcStack_9c = *iter;                          // one element of json["_id"]
5290:      pcStack_8c = pcStack_9c;                     //   inner iterator setup
5300:      while (iter2 != end2) {                      // LOOP B
5302:          uVar13 = *iter2;
5308:          uVar14 = uVar13["ref_id"];
5313:          from_json(uVar14, &uStack_a8);             //   -> std::string ref_id
5325:          puVar15 = uVar13["group"];                 //   -> int
5354:          puVar15 = uVar13["next_spawn_ms"];        //   -> float * _UNK_00a0d4f8
5385:          ... vector<STAGE_MONSTER>::push_back      //   stride 0x14
5427:      }                                            // end LOOP B
5429:      vector<vector<STAGE_MONSTER>>::push_back(uStack_60)   // one wave
5436:  }                                                // end LOOP A
```

and the final store (`:5475-5513`):

```
5475:  pcStack_44 = json["show_thumbnail"];
5506:  basic_string uStack_d0(param_2);                  // the STAGE ID
5508:  vector<vector<STAGE_MONSTER>> puStack_c4(uStack_60);
5510:  vector<string> pbStack_b8(uStack_58);
5512:  m_mStageMonsterLink.emplace(param_1 + 0xc, uStack_d0, uStack_d0);
```

**[RECOVERED] the required shape is three levels deep:**

```
ret_data = {
  "<stageId>": {
    "<OUTER_KEY>": [            // LOOP A  - one element per WAVE
      [                         // LOOP B  - one element per MONSTER in the wave
        { "ref_id": "...", "group": <int>, "next_spawn_ms": <int> }
      ]
    ],
    "show_thumbnail": [ "..." ] // a flat list of strings, stage level
  }
}
```

**[INFERRED] `<OUTER_KEY>` is `wave_list`, not `_id`.** Reasoning:

* The resolver's `_id` (0x1d76bd1) is a genuine distinct literal — it is
  tail-merged into `cut_in_id` at 0x1d76bcb, and `wave_list` sits immediately
  after it at 0x1d76bd5. I confirmed both addresses directly out of
  `analysis/native-all-strings.tsv`:
  `01d76bcb cut_in_id`, `01d76bd5 wave_list`, `01d76bdf next_spawn_ms`,
  `01d76bed show_thumbnail`. So both candidates exist and are 4 bytes apart.
* If `OUTER_KEY` really were `_id`, then with the replica's current fixture
  (`{wave_list:[record]}`, no `_id`) `json["_id"]` would be **null**, LOOP A
  would iterate **zero** times, `GetStageMonsterLinkData` would return an empty
  vector, and we would see **zero** `SRCard.cpp(731)` assertions and an **empty**
  `list`. We see 5 and 5.
* If `OUTER_KEY` is `wave_list`, LOOP A yields the single record object, LOOP B
  iterates that object's **five values** (`"N003_M001"`, `"001"`, `1`, `0`,
  `1`), each `value["ref_id"]` is null, `from_json(null, std::string)` yields
  `""`, and we get **exactly five** empty ref ids. Matches.
* This also explains report-008's negative: mutating `_id`'s *value* to
  `N003_M001` cannot change a count that is driven by the record's *key count*,
  and cannot make any of the five values into a sub-object carrying `ref_id`.
  So "byte-identical `list`" was the correct and expected result — that
  experiment was sound, it just probed the wrong axis.

**Recommended hedge (one line, disambiguates on the next run):** publish the same
doubly-nested array under **both** `wave_list` and `_id`. Only one is read, so
this cannot break, and whichever one the client reads will now contain real
records instead of a record's scalar fields.

**[INFERRED]** `show_thumbnail` is a **stage-level list of strings**, not a
per-monster boolean. It is the only other `operator[]` in the function, it is
applied to the same per-stage object as the wave list, and it is consumed by
`from_json<std::string>` in a loop (`:5611`) into a `vector<string>` that becomes
the second member of `STAGE_MONSTER_LINK` (`:5510`). **Rejected alternative:**
per-monster `show_thumbnail` — that would require a sixth `operator[]` inside
LOOP B, and there is none. Note this changes the fixture's TypeScript type
(`bootstrap.ts:241` currently types it as a per-wave `number`).

### 2.3 Target 2 — who builds the 5-element `list` for `/reference/GetMonster`

**[RECOVERED]** the *callback* side. `analysis/native-reqmonster.txt:1-121`:

```
 36:  iVar3 = CPVHTTPResponse::GetResultCode(*(CPVHTTPResponse **)param_2);
 37:  pbVar4 = basic_json::operator[](param_3, "ret_data");     // "ret_data" per ghidra-reqmonster-keys.txt:2
 74:  if (iVar3 == 0) {
 75:    do {
 80:      pbVar4 = iter_impl::operator*(&local_2c);
 81:      this_00 = (CSRGameMob *)CSRGameMob::get();
 82:      CSRGameMob::AddMonster(this_00, pbVar4);
...
112:    } while (iVar3 == 0);
```

Two things fall out, both **[RECOVERED]**:

1. `ret_data` is iterated with `iter_impl`, which accepts an array **or** an
   object. The container shape does not matter here.
2. **`AddMonster` receives only the element — no key.** So the monster's
   identity cannot come from the container key.

**[RECOVERED]** the request builder exists but is **not dumped**:
`CSRSyncMStage::GetMonster(const std::list<std::string>&, const std::function<void(int)>&)`
at **0xb444c4** (`analysis/native-evidence.tsv`, listed at
`analysis/ghidra-fnlist16.txt:13` and `ghidra-enemycamp-names-01.txt:47`).
The `/reference/GetMonster` literal is at `0x1d7b3d5`
(`analysis/native-all-strings.tsv`). **I did not read `GetMonster`'s body — it
is not in any `analysis/*.txt`.** Its callers are not dumped either.

**[INFERRED]** the 5 strings in `list` are the same 5 `STAGE_MONSTER::ref_id`
values that `MakeStageInst:6697` wrote into the enemy `ACTOR_INFO`s, because
(a) the count is identical, (b) both are 5, (c) `GetMonsterData` is called with
the `ACTOR_INFO` ref id and is asserted once — the first actor — before the
process dies, and (d) no other client-side source produces exactly five empty
strings anywhere in these dumps. **Rejected alternative:** a separate
deck-derived list. `GetDeckInfo` yields one live slot
(`deck_inst_id_1=1`, `_2..4=0`), so a deck-derived list would have length 1, not
5.

### 2.4 Target 4 — `/mirage/GetInfo` is **not** the carrier **[RECOVERED]**

This is a clean refutation of report-009 §6, on dumped evidence.

`CSRExploreMirage::MakeStageInst` (0x925798) — the mirage scene — is dumped at
`analysis/ghidra-enemycamp-decomp-01.txt:6084-6600` (and identically at
`native-mstage-all.txt:2324-3130`). It does **not** read
`CSRGameMob::GetStageMonsterLinkData`. It reads a completely different
singleton, `CSRExploreMirageInfo`:

```
6505:  pCVar9 = (CSRExploreMirageInfo *)CSRExploreMirageInfo::get();
6506:  iVar17 = CSRExploreMirageInfo::GetEnemyInfo(pCVar9);
6508:  iVar7  = CSRExploreMirageInfo::GetStairInfo(pCVar9);
6516:  iVar14 = CSRExploreMirageInfo::GetBaseInfo(pCVar9);
6523:  iVar12 = CSRExploreMirageInfo::GetStairInfo(pCVar9);
```

and there is **no `CSRCard::SetRefID` anywhere in 6084-6600**. The mirage
`SetRefID` sites are at 0x925958 / 0x92602e (`analysis/ghidra-setrefid-callers.txt:4-5`),
a different region of the same function, and they are not on the expedition path
(`/mission/Start` opens `CSRMStage`, not `CSRExploreMirage`).

**[RECOVERED]** `CSRExploreMirageInfo::Parse_InstEnemy` (0x92dff4) *does* call
`SetRefID` at 0x92e1f2 (`ghidra-setrefid-callers.txt:17`) and its recovered keys
are in `analysis/ghidra-makestageinst-keys.txt:13-25`:

```
0092e11c -> "ref_id"      0092e122 -> "rank"       0092e128 -> "rank_up_cnt"
0092e29c -> "overcome_cnt" 0092e2f4 -> "exp"      0092e364 -> "skill_1_level"
0092e42c -> "skill_2_level" 0092e4ea -> "skill_3_level"
0092e5a8 -> "skill_4_level" 0092e666 -> "skill_5_level"
0092e10e -> "n"
```

That is a genuinely useful recovered schema for `inst_enemy`, and
`/mirage/GetInfo` is a real defect worth fixing on its own merits — but it is a
**different scene**. Its callers are `ParseRewardInfo` (0x92cdc8) and
`FUN_009359ac` (`analysis/ghidra-instenemy-callers.txt:1-5`), both inside
`CSRExploreMirageInfo`. **[UNKNOWN]** — `Parse_Entry` (0x933aec),
`Parse_InstBase` (0x933d80), `ParseStairInfo` (0x9343b4), `ParseHeroInfo`
(0x9347f8), `ParseFriendInfo` (0x934c00), `Parse_End` (0x92c64c),
`Parse_HealHunter` (0x92c8e0), `ParseDeckInfo` (0x92c428) and `RequestInfo`
(0x92b30c) are **not decompiled on disk**. I recovered no keys for them. The
only mirage keys present in the string tables are the request-side ones
(`analysis/native-all-strings.tsv`: `01d72eea inst_enemy`, `01d72ee0 inst_base`,
`01d72f04 ref_hero`, `01d72ef5 ref_stair_list`) plus
`01d72f7d inst_list` / `01d7b29c deck_info` from
`analysis/ghidra-deck-keys.txt:7,16,29`.

### 2.5 Target 3 — `/reference/GetCard` shape: **array of records with `base`** **[RECOVERED]**

Settled, and it is in a dump. `CSRCardInfoContainer::SetCard` is at
**0x87baa4**, and its 32 resolved keys are in `analysis/ghidra-card-keys.txt:21-62`
(the call site is `ReqCardCB` 0xf83a10 → 0xf839f2, cross-referenced in
`analysis/ghidra-enemycamp-refs-01.txt:32-34`):

```
0087bac2 -> "ret_data"     0087bb3a -> "base"        0087bb4e -> "is_main"
0087bc68 -> "id"           0087bcbe -> "char_id"     0087bd16 -> "name"
0087bdcc -> "attr"         0087be48 -> "role"        0087be9a -> "res_prefix"
0087bee4 -> "is_source"    0087bf34 -> "source_field"
0087bff6 -> "equipment"    0087c106 -> "type"        0087c16e -> "rank"
0087c228 -> "stat"         0087c278 -> "stat"        0087c2be -> "rank"
0087c392 -> "cool_time"    0087c3e2 -> "skill"       0087c418 -> "skill"
0087c480 -> "dialog"       0087c4f8 -> "dialog"      0087c508 -> "dialog_id"
0087c55e -> "target_rank"  0087c5dc -> "chain_id"
```

It resolves `ret_data` → **`base`** → `id`/`char_id`/`name`/`attr`/`role`/
`res_prefix`/…, and then `equipment`, `stat[]`, `skill[]`, `dialog[]` as
siblings of `base`. So `ret_data` is a list of records, each with a `base`
sub-object. **The object-keyed-by-id form is refuted**: iterating an object
yields the *values*, and those values have no `base`.

This is the answer already encoded in `server-ts/src/game-routes.ts:60-67`, and
it is **correct**. No change needed there — worth recording so it stops being
re-litigated.

### 2.6 Target 5 — why `GetMonsterData`'s `map<string,INFO>::find` misses **[RECOVERED]**

Two independent reasons, both now proven.

**(a) The id being looked up is `""`.** Follows from §2.2.

**(b) Even a non-empty id cannot hit, because `AddMonster` never reads an `id`
field.** `AddMonster`'s signature takes the json alone
(`analysis/native-evidence.tsv`):
`_ZN10CSRGameMob10AddMonsterERKN8nlohmann10basic_jsonI…EEE`
and its **first** `operator[]` is `_server`
(`analysis/native-monster-stage.txt:464`, slot `0xa0b874`;
`analysis/ghidra-mob-keys.txt:2`: `ldr@00a0b558 slot=0xa0b874 … -> 0x1d676bb "_server"`).
It then stores into the map
(`analysis/native-monster-stage.txt:4941-4942`):

```
4941:  __tree<__value_type<std::string, CSRGameMob::INFO>>…::__emplace_unique_key_args
4942:            (&uStack_118, param_1, &uStack_2b8, &uStack_2b8);
```

where `uStack_2b8` is the `std::string` built at the top of the parse — i.e.
the value of `_server`. `AddMonster` reads **27 keys** and *none of them is an
id* (`analysis/ghidra-mob-keys.txt:1-61`: `_server, title, attr, role,
res_prefix, rank, level, overcome, hp, atk, def, crt_chance, crt_dmg,
penetration, block_chance, block_dec_dmg, attr_enhance, attr_resist, hp_page,
skill_start_time, skill_list, name, desc, type, effect, effect_type`) — so
`_server` **is** the identity field.

I verified `_server` is a real, distinct literal and not a resolver artefact:
it is absent from `native-all-strings.tsv` because it is **tail-merged into
`/selected_server`** at 0x1d676b2 — offset 9 of `/selected_server` is exactly
`_server`, at 0x1d676bb. (Confirmed against `analysis/native-all-strings.tsv`:
`01d676b2 /selected_server`.)

`server-ts/src/bootstrap.ts:208-215` defines `starterMonster` with `id` and
`ref_id` and **no `_server`**. So every monster enters `m_mMonsters` under `""`,
`HasMonsterData`/`GetMonsterData` (0xa0b428 / 0xa0b43c,
`analysis/native-mob.txt:1-84`) can only ever hit on the empty string — which is
precisely the key that §2.2 produces. **This is a closed loop, and it is
fixable with zero further device evidence.**

### 2.7 The crash, explained **[RECOVERED + INFERRED]**

`CSRGameMob::GetMonsterData` is `void` and on a miss only asserts and returns
(`analysis/native-mob.txt:51-77` — the `if (this + 4 == pCVar1)` branch builds
`"Cannot find MonsterData"` and calls `_RMAssert`, then falls through to
`return`). The caller does not check. So
`CSRGameActorMob::MakeBackEndActor` (0x9afd58) copy-constructs a
`CSRGameMob::INFO` from an `end()` iterator's garbage
(`analysis/native-mob-keys.txt:70`: the map is
`__tree<__value_type<std::string, CSRGameMob::INFO>>`), which is report-009's
`CSRGameMob::INFO::INFO(CSRGameMob::INFO const&)` frame, and the copy of that
object's `std::map<SRSKILL_TYPE, SRSKILL_INFO>` member faults. The PC symbol in
report-009 is a *mis-attribution* by the stack scanner: it resolved
`+0x8643bb` to a `~__tree_iterator()` symbol, but that address is the tail of a
cold/merged chunk; the frame it names is a destructor being inlined into
`INFO`'s copy constructor. **[INFERRED]** — I did not disassemble 0x8643bb.

---

## 3. What the server should send

### 3.1 `/reference/GetTargetStageMonster` (and `/reference/GetStageMonster`) — the fix

`ret_data` must be a map keyed by stage id whose value has a **doubly-nested**
array. Publish the identical nested array under both `wave_list` and `_id` so the
run also settles §2.2's open question:

```jsonc
{
  "result_code": 1,
  "ret_data": {
    "N003": {
      "wave_list": [
        [ { "ref_id": "M001", "group": 1, "next_spawn_ms": 0 } ]
      ],
      "_id": [
        [ { "ref_id": "M001", "group": 1, "next_spawn_ms": 0 } ]
      ],
      "show_thumbnail": [ "M001" ]
    }
  }
}
```

Notes:
* one array = one wave; one object = one monster in that wave.
* `show_thumbnail` is a **flat list of strings at stage level**, not a per-record
  boolean — §2.2.
* `_id` must be **removed from the monster record**. If `_id` survives at record
  level it becomes one more iterated value and the count grows.
* `next_spawn_ms` is multiplied by a float constant (`_UNK_00a0d4f8`,
  `native-monster-stage.txt:5235`, `fVar6`) — almost certainly a ms→s scale.
  Harmless at 0 either way, but do not put a float there.

Concretely in `server-ts/src/bootstrap.ts:241-249`, `starterStageMonsters` changes
type and value from
`{ wave_list: Array<{_id,ref_id,group,next_spawn_ms,show_thumbnail}> }` to:

```ts
type StageWaveMonster = { ref_id: string; group: number; next_spawn_ms: number };
type StageMonsterBlock = {
  wave_list: StageWaveMonster[][];
  _id: StageWaveMonster[][];
  show_thumbnail: string[];
};
```

and `game-routes.ts:117-133`'s `wavesFor` keeps its single-requested-stage
behaviour (that part is right and should stay).

### 3.2 `/reference/GetMonster` — the fix

`ret_data` is iterated with `iter_impl`, so array-or-object both work, but every
record **must carry `_server`**, and `_server` must equal the wave's `ref_id`.
Add `_server: "M001"` to `starterMonster` (`bootstrap.ts:208`), and keep
publishing it under both keys (`game-routes.ts:103`) so either lookup resolves:

```jsonc
{ "result_code": 1, "ret_data": { "M001": { "_server": "M001", ... }, "001": { "_server": "001", ... } } }
```

Note the two entries need **different `_server` values**, matching their own
object keys, if the wave `ref_id` is to be able to select between them. Skill
sub-records (`skill_list`) use the recovered keys
`effect_type, target_type, target_stat, refer_target_stat, refer_target_type,
base_number, up_number, duration, duration_up, interval, cool_time, crt_chance,
is_active, cut_in_id` (`analysis/ghidra-mob-keys.txt:29-61`).

### 3.3 `/reference/GetCard` — **no change**

§2.5: array of records with a `base` sub-object. `game-routes.ts:60-67` is
already correct.

### 3.4 `/mirage/GetInfo` — genuine defect, but not this bug

Still `{"mock":true}`. Recovered so far: `inst_enemy` records are
`{n, ref_id, rank, rank_up_cnt, overcome_cnt, exp, skill_1_level..skill_5_level}`
(§2.4). The other five parsers are undumped — see §4. Fix it on its own merits;
do not expect it to move `SRCard.cpp(731)`.

---

## 4. Gaps — fresh Ghidra decompiles the Ghidra agent should take, in order

| # | address | symbol | why it matters |
|---|---|---|---|
| 1 | **0xa0d194** | `CSRGameMob::AddStageMonster` | Already decompiled — but **re-run `ResolvePcRelativeStrings.java` over it alone**. The project's dump says slot `0xa0d4f4` → `_id` (0x1d76bd1) while §2.2 argues for `wave_list` (0x1d76bd5). A single-function, single-slot re-read of that one literal settles it. Highest value per minute of the whole list. |
| 2 | **0xa0cf38** | `CSRGameMob::GetStageMonsterLinkData` | Confirms the return type is `vector<vector<STAGE_MONSTER>>` and that it is a pure lookup on `m_mStageMonsterLink`. Not decompiled anywhere on disk. |
| 3 | **0xb444c4** | `CSRSyncMStage::GetMonster(const list<string>&, function<void(int)>&)` | The `/reference/GetMonster` request builder. Confirms the `list` is built from the `STAGE_MONSTER::ref_id` values and shows the exact JSON it serialises. Also needs its **callers**, which is the one piece I could not establish from the dumps. |
| 4 | **0x9d39e0** | `CSRGameBase::MakeCamp` | Confirms the `unordered_map<CMHashID, list<list<ACTOR_INFO>>>` → `MakeCamp` handoff and which team gets which list. Currently inferred, not read. |
| 5 | **0xaeb5b0** | `CSRInventory::FindCard(unsigned)` | Rule out the ally deck conclusively. It is the source of `local_80 + 0x5c` at `MakeStageInst:6035`. Low priority: the deck loop provably runs once and cannot produce five. |
| 6 | 0x92b30c, 0x933aec, 0x933d80, 0x9343b4, 0x9347f8, 0x934c00 | `CSRExploreMirageInfo::RequestInfo`, `Parse_Entry`, `Parse_InstBase`, `ParseStairInfo`, `ParseHeroInfo`, `ParseFriendInfo` | The only way to get real `/mirage/GetInfo` keys. Off the critical path. |

---

## 5. Honest negatives

Things I searched for and did **not** find, so nobody re-searches them:

* **`MakeCamp`'s body** — not in any `analysis/*.txt`.
* **`MakeActor` (0x9e9e68)** — not decompiled.
* **`MakeBackEndActor` (0x9afd58 / 0x9ac2ac)** — not decompiled; only their
  *callers* are listed (`ghidra-enemycamp-refs-01.txt:160-164`).
* **`CSRGameMob::GetMonsterData`'s callers' argument derivation** — inferred, not read.
* **`Parse_InstEnemy`'s body** — keys recovered, but the decompile is absent; I
  only have the resolver output.
* **`wave_list` as a string is referenced nowhere else** in the dumps — no
  function other than (possibly) `AddStageMonster` reads it, which is why the
  resolver's `_id` could not be cross-checked from a second site.

One provenance note: `analysis/ghidra-enemycamp-{names,refs,decomp}-01.txt`
appeared in the working tree while I was working. I have **not** run Ghidra and
did not create them; they are the parallel agent's output. I read them as
evidence and cite them by line. If that agent has since moved past them, the
addresses in §4 are still current.