# Ghidra trace: where the five empty enemy ref-ids come from

Ghidra agent, 2026-10-02. Program `libnative_core.so`, project `BlustoneNative`,
Ghidra 12.1.3 headless, `-noanalysis`. Every claim below cites a function name +
address and a raw dump in `analysis/ghidra-enemycamp-*.txt` /
`analysis/ghidra-mirage-*.txt`.

**Method note.** All string keys were read with the Thumb
`ldr [pc,#imm]` + `add pc` model against Ghidra's *relocated* memory
(`ResolvePcRelativeStrings.java`). Where that reported `resolved: 0` on a function
that demonstrably calls `nlohmann::operator[](const char*)` many times, I re-ran
with a wider LDR→ADD window using a new script,
`analysis/ghidra-scripts/ResolvePcRelativeStringsWide.java`. That recovered keys
the narrow script misses (`equipment[].id`, `"901"`, and every key of
`CSRExploreMirageInfo`'s `/mirage/GetInfo` callback). Treat the wide dumps
(`ghidra-enemycamp-strings-13.txt`, `ghidra-mirage-strings-13/14.txt`) as
authoritative where the two disagree.

**Correction to the crash offsets in report-009.** The `+0x9c3df1 MakeCamp`,
`+0x9d9ef9 MakeActor`, `+0x99fde5 MakeBackEndActor` etc. in the candidate stack
are **return addresses, not function entries**. Real entries:

| symbol in report | real entry |
|---|---|
| `CSRGameBase::MakeCamp` | **`0x9d39e0`** (not `0x9c3df1`) |
| `CSRGameBase::MakeActor` | **`0x9e9e68`** |
| `CSRGameActorMob::MakeBackEndActor` | **`0x9afd58`** |
| `CSRGameMob::GetMonsterData` | **`0xa0b43c`** |
| `CSRGameBase::OpenCamp` | **`0x9d383c`** |

---

## Q1 — `MakeCamp`, the ENEMY list, and the `+0x5c` string

### Q1a/b/c. The call chain, and what `MakeCamp` actually does

**[RECOVERED]** `CSRGameBase::MakeCamp` — mangled signature from the string table
(`analysis/native-all-strings.tsv:0x223f12`):

```
_ZN11CSRGameBase8MakeCampERKNSt6__ndk14listINS1_IN12CSRGameActor10ACTOR_INFOENS0_9allocatorIS3_
  EEEENS4_IS6_EEEE8TEAM_DIRRK8CMHashID
```

so it is `MakeCamp(std::list<std::list<CSRGameActor::ACTOR_INFO>> const&,
unsigned /*TEAM_DIR*/, CMHashID const&)`.

Its **only** callers are two call sites inside `CSRGameBase::OpenCamp` (`0x9d383c`)
— `analysis/ghidra-enemycamp-refs-01.txt`:

```
TARGET 009d39e0 MakeCamp
CALL 009d387c 009d383c OpenCamp
CALL 009d3898 009d383c OpenCamp
```

`OpenCamp` (`ghidra-enemycamp-decomp-02.txt:4140-4230`) reads two
NULL-terminated node lists hanging off the scene object and feeds each node to
`MakeCamp`:

```c
/* CSRGameBase::OpenCamp() */
for (piVar6 = *(int **)(this + 600); piVar6 != 0; piVar6 = (int *)*piVar6) {
    MakeCamp(this, piVar6 + 8, 0, piVar6 + 2);      /* TEAM_DIR 0 */
}
for (piVar6 = *(int **)(this + 0x26c); piVar6 != 0; piVar6 = (int *)*piVar6) {
    MakeCamp(this, piVar6 + 8, 1, piVar6 + 2);      /* TEAM_DIR 1 */
}
for (piVar6 = *(int **)(this + 0x33c); piVar6 != 0; piVar6 = (int *)*piVar6) {
    CSRGameActorGroup::Activate(piVar6[5], 0);      /* groups already built */
}
CSRInspector::MakeVerifyBattleInfo(...);
```

Node layout, read off `MakeCamp`'s use of `param_4` (a `CMHashID const&`):
`{ +0 next, +8 CMHashID{int crc; basic_string key}, +32 std::list<std::list<ACTOR_INFO>> }`.

**`MakeCamp` reads no JSON key at all** — `ResolvePcRelativeStrings` on it
(`ghidra-enemycamp-strings-13.txt`) yields only assertion text, `"right"`,
`"Box2."`, `"OUTSIDE_ROOT"`, `"run"`. So **the camp contents are already built
when `OpenCamp` runs**; `MakeCamp` only materialises them.

Inside the camp loop (`ghidra-enemycamp-decomp-02.txt:4609-4673`):

```c
for (iVar23 = *(int *)(iVar4 + 0xc); iVar4 + 8 != iVar23; iVar23 = *(int *)(iVar23 + 4)) {
    CSRDataMgr::get(); CSRDataMgr::GetPlayData(...);
    CSRLevelData::GetMonsterGroupID(&local_b0);
    MakeActor(&local_128, <hash>, <the ACTOR_INFO node>);   /* 0x9e9e68 */
    ...
    CSRGameActorBaseDraw::SetGroupID(local_128, param_4);
    ...
    CSRGameActorGroup::AddActor(local_1e4, &local_210);
}
```

**[RECOVERED]** `CSRGameBase::MakeActor` — mangled
(`_ZN11CSRGameBase9MakeActorERKN12CSRGameActor10ACTOR_INFOEjh`), entry `0x9e9e68`,
decompile at `ghidra-enemycamp-decomp-02.txt:5599-5656`:

```c
if (in_stack_00000000 == 1)   std::shared_ptr<CSRGameActorMob>::make_shared<>(...);
else                          std::shared_ptr<CSRGameActorHunter>::make_shared<>(...);
... vtable+0xa0 / +0xbc ...
CSRGameActor::RegistBaseSkill(this_00);
```

The mob-vs-hunter choice is an explicit `unsigned` argument, **not** something
derived from the `ACTOR_INFO`. So `MakeCamp` does not distinguish player from
enemy either — the distinction is baked into the camp lists by whoever built
them.

### Q1d. Where the empty string comes from — the direct answer

**[RECOVERED]** The ref-id consumed by the mob path is read in
`CSRGameActorMob::MakeBackEndActor` (`0x9afd58`, decompile
`ghidra-enemycamp-decomp-03.txt:9774-9777`):

```c
this_00 = (CSRGameMob *)CSRGameMob::get();
pIVar6 = (INFO *)CSRGameMob::GetMonsterData(this_00,
              (basic_string *)(*(int *)(param_1 + 0x34) + 0x5c));
CSRGameMob::INFO::INFO(&local_1c4, pIVar6);
```

So the string handed to `CSRGameMob::GetMonsterData` is `*(ACTOR_INFO+0x34)->m_refID`,
i.e. **`CSRCard::m_refID` lives at offset `+0x5c` of the card object**. That is
the same `+0x5c` recorded in `AGENTS.md` §11 for `MakeStageInst` (0x925798), and
the two independent readers agree.

**[RECOVERED]** `GetMonsterData` (`0xa0b43c`, decompile `ghidra-enemycamp-decomp-02.txt:5664-5721`)
is a bare `std::map<std::string, CSRGameMob::INFO>::find` on `CSRGameMob+0x4`:

```c
pCVar1 = __tree<value_type<basic_string, CSRGameMob::INFO>>::find(this, param_1);
if (this + 4 == pCVar1) {
    ... basic_string("Cannot find MonsterData").append(...) ...
    _RMAssert(0, "(itr != m_mMonsters.end())", "SRGameMob.cpp", 0x26, "GetMonsterData", ...);
}
```

**[RECOVERED] The set of strings the client will ever look up in that map is
exactly the `list` it sends to `/reference/GetMonster`.** See Q2: that list is
`CSRGameMob::m_stageMonsterLink[<key>].ids`, populated from
`/reference/GetTargetStageMonster`. The reported wire value is
`list = ["","","","",""]`, and `GetMonsterData` is called with those same five
empties. **The two observations are the same five strings.**

**[RECOVERED] The player-side `ACTOR_INFO` builder, for contrast**, is
`CSRMStage::MakeStageInst` (`0xb33f84`, decompile
`ghidra-enemycamp-decomp-03.txt:955-1002`):

```c
CSRPlayData::GetDeckInfo(&local_bc, uVar16, 1);              // team_dir 1
for (piVar18 = local_bc; local_bc != local_b8; piVar18 += 2) {
    if (*piVar18 != 0 || piVar18[1] != 0) {
        CSRGameActor::ACTOR_INFO::ACTOR_INFO(&local_120);
        *(int *)(local_ec + 0x10) = *piVar18;
        *(int *)(local_ec + 0x14) = piVar18[1];
        CSRInventory::FindCard(<inst_id>, &local_80);
        CSRCard::SetRefID(local_ec, (basic_string *)(local_80 + 0x5c));   /* <== +0x5c */
        *(undefined4 *)(local_ec + 0x24) = CSRCard::GetRank(local_80);
        CSRSkin::get(); CSRSkin::FindWornSkinByCardRefId(&local_68);
        ... CSRCard::SetAwake(local_ec, CSRCard::GetAwake(local_80));
        CSRLevelData::CalcBonus(&local_68, levelData, *piVar18, piVar18[1], 0);
        CMHashID::Set(&local_68, to_string(calcBonusString));
        unordered_map<CMHashID, list<list<ACTOR_INFO>>>::__emplace_unique_key_args(
              &local_74, this + 0x250, key);
        ... splice ACTOR_INFO into map[key].back() ...
    }
}
```

The camp map is at `this + 0x250`
(`unordered_map<CMHashID, list<list<ACTOR_INFO>>>` — confirmed by the mangled
`_ZN11CSRGameBase14ApplyBonusBuffER...unordered_mapI8CMHashID...ACTOR_INFO...`).
The same function contains the only *other* `SetRefID` producers, both
**hard-coded literals**, and both inside `if (this->m_stageId == <one global
std::string>)`:

```c
/* ghidra-enemycamp-decomp-03.txt:1299-1306 */
pcVar35 = (char *)(DAT_00b34a80 + 0xb34734);              /* "001" */
*(uint *)(local_ec + 0x10) = local_138 + 1;
*(uint *)(local_ec + 0x14) = uVar17 + (0xfffffffe < local_138);
basic_string(&local_68, pcVar35);
CSRCard::SetRefID(pCVar9, &local_68);                     /* "001" */
/* ghidra-enemycamp-decomp-03.txt:1423-1430 */
pcVar35 = (char *)(DAT_00b34a8c + 0xb348de);              /* "003" */
CSRCard::SetRefID(pCVar9, &local_68);                     /* "003" */
```

`ResolvePcRelativeStrings` on `0xb33f84` confirms the two literals
(`ghidra-enemycamp-strings-13.txt:252-258`): `"001"` and `"003"`, and nothing
else. That branch is the single-stage "defence" fixture and does not run for
`N003`.

**[UNKNOWN]** I did **not** locate the function that populates the **enemy**
camp's `ACTOR_INFO` list. I searched:

- every function whose mangled name contains `ACTOR_INFO`
  (`analysis/native-all-strings.tsv`) — the only members are the copy ctor
  `_ZN12CSRGameActor10ACTOR_INFOC2ERKS0_`, the destructor, `MakeCamp`,
  `MakeActor`, both `MakeBackEndActor`s, `CSRCardAnalyzer::Load*` and
  `CSRGameBase::ApplyBonusBuff`. **There is no `Parse`/`Set` for `ACTOR_INFO`**,
  so `ACTOR_INFO` is only ever populated by field assignment inside scene code;
- every function that pushes into `CSRGameBase+0x258` / `+0x26c` (the two camp
  queues `OpenCamp` drains) — not found;
- the whole `CSRMStage` class (entry-point dump
  `analysis/ghidra-enemycamp-ranges-05.txt:39-63`): `CSRMStage` 0xb33ca8,
  `InitBeforeOpen` 0xb33ccc, `MakeStageInst` 0xb33f84, `PopUpPause` 0xb35650,
  `OnFinish` 0xb35ce4, `SetBGM` 0xb362d4, `OpenStage` 0xb36348,
  `PopUpResultWin` 0xb3635c. None of the others resolve any JSON key
  (`ghidra-enemycamp-strings-06.txt` shows `InitBeforeOpen` reads only
  `"leveling_m"`, `"UI_ROOT"`, `"UI"`, `"Cannot find Mission Information"`).

**[INFERENCE — strong, not proven]** The five failing `SRCard.cpp(731)` slots are
the *enemy* actors (the player camp carries `inst_id_1 = 1` and the profile fix
proved it is not the source). `MakeCamp` performs no string reading, so the
empty strings must already be in the camp lists; and the only monster-identity
strings the client ever holds for a stage are the `m_stageMonsterLink[...].ids`
entries, which are precisely the five empty strings it just asked for over the
wire. **The empty `ACTOR_INFO` ref-id and the empty `/reference/GetMonster`
`list` element are the same string**, and its origin is
`/reference/GetTargetStageMonster`. Fixing that route (Q2, below) should clear
both the `731` assertions and the `GetMonsterData` miss together.

**Do not spend another cycle on `GetCardInven`, wave `_id`/`ref_id` splits, or
`GetTargetUserInfo`.** All three are already disproven on-device (report-002,
-008, -009) and none of them appears on the `MakeCamp` → `MakeActor` →
`MakeBackEndActor` → `GetMonsterData` path this trace establishes.

---

## Q2 — who builds the five-element `list` for `/reference/GetMonster`

### The request builder

**[RECOVERED]** `CSRSyncMStage::GetMonster` — mangled-free signature from the
decompile header (`ghidra-enemycamp-decomp-03.txt:3-8`):

```c
void CSRSyncMStage::GetMonster(CSRSyncMStage *this,
                               std::list<std::string> *param_1,      /* the ids */
                               std::function<void(int)> *param_2)
```

Request keys, in order (`ghidra-enemycamp-strings-02.txt:197-205`):

```
"app_code"  "app_ver"  "market"  "pvid"  "otp"  "list"  "/reference/GetMonster"
```

Body (`ghidra-enemycamp-decomp-03.txt:106-124`) — the list is walked node by
node and each element pushed as a JSON string, then `dump()`ed into `list`:

```c
local_1f0[0] = (basic_json)0x0;                       /* array */
for (plVar15 = *(list **)(param_1 + 4); param_1 != plVar15;
         plVar15 = *(list **)(plVar15 + 4)) {
    this_00 = operator_new(0xc);                     /* 12-byte std::string */
    basic_string::basic_string(this_00, (basic_string *)(plVar15 + 8));
    json::push_back(local_1f0, json_string(this_00));
}
```

### The list builder — `FUN_00b4a7a8`

**[RECOVERED]** `FUN_00b4a7a8` (`0xb4a7a8`, decompile
`ghidra-enemycamp-decomp-04.txt:45-99`), the completion lambda inside
`CSRSyncMStage::RequestMonsterRef`:

```c
if (*param_2 != 1) goto LAB_00b4aa48;                  /* result_code != 1 -> stop */
iVar5 = *(int *)(param_1 + 8);
local_64 = 0;                                          /* output list count */
local_6c = &local_6c; local_68 = &local_6c;            /* list sentinel */

CSRGameMob::get();
CSRGameMob::GetStageMonsterLinkData((basic_string *)&local_84);

/* FIRST LOOP: std::vector<std::string>, stride 0x0c (12-byte string) */
for (pbVar18 = local_78; pbVar18 != local_74; pbVar18 += 0x0c) {
    if (CSRGameMob::HasMonsterData(CSRGameMob::get(), pbVar18) == 0) {
        node = operator_new(0x14);                     /* {next,prev,string12} */
        basic_string::basic_string(node + 2, pbVar18);
        ... splice into list ...
        local_64++;
    }
}
/* SECOND LOOP: std::vector<std::vector<STAGE_MONSTER>>, stride 0x3 (12-byte vector) */
for (puVar4 = local_84; puVar4 != local_80; puVar4 += 3) {
    for (pbVar18 = *puVar4; pbVar18 != puVar4[1]; pbVar18 += 0x14) {
        if (CSRGameMob::HasMonsterData(CSRGameMob::get(), pbVar18) == 0) {
            node = operator_new(0x14);
            basic_string::basic_string(node + 2, pbVar18);
            ... local_64++;
        }
    }
}
if (local_64 == 0) { (*(code **)(**(int **)(param_1 + 0x28) + 0x18))(); }
else { CSRSyncMStage::GetMonster(syncMgr->m_mstage, &local_6c, cb); }
```

So: **every monster id in the link table that is not already in `m_mMonsters`
becomes one element of `list`.**

### The link table and its two payloads

**[RECOVERED]** `CSRGameMob::GetStageMonsterLinkData` (`0xa0cf38`,
`ghidra-enemycamp-decomp-05.txt:6-62`) returns **two** vectors out-parameters,
and `CSRGameMob::STAGE_MONSTER_LINK` is the mapped type:

```c
std::map<std::string, CSRGameMob::STAGE_MONSTER_LINK>  m_stageMonsterLink;   /* at this+0xc */

if (__count_unique(this->m_stageMonsterLink, key) == 0) {
    /* key not present at all: copy the WHOLE aggregate map contents out */
    vector<vector<STAGE_MONSTER>>::vector(out1, this + 0x18);
    vector<string>::vector(out2, this + 0x24);
} else {
    node = __find_equal(this->m_stageMonsterLink, key);
    if (node == 0) FUN_006d8570("map::at: key not found");     /* fatal */
    vector<vector<STAGE_MONSTER>>::vector(out1, node + 0x1c);   /* waves  */
    vector<string>::vector(out2, node + 0x28);                  /* ids    */
}
```

**Note the `count_unique == 0` fallback:** if the requested key is absent the
client silently substitutes the *entire* table. That is a second way to get five
ids regardless of how many keys we send.

**[RECOVERED]** `CSRGameMob::AddStageMonster` (`0xa0d194`,
`ghidra-enemycamp-decomp-05.txt:75-473`) is the **only** writer
(`ReqTargetStageMonsterCB` is its only caller, `ghidra-enemycamp-refs-02.txt:21`).
It takes `(std::string const& key, json const& value)` and reads **exactly five
keys** (`ghidra-enemycamp-strings-06.txt`, and the wide re-run
`ghidra-enemycamp-strings-13.txt:173-179` which agrees exactly):

```
_id   ref_id   group   next_spawn_ms   show_thumbnail
```

Reconstructed body:

```c
/* part 1 -- the waves */
for (it = value["_id"].begin(); it != end; ++it) {          /* _id is an ARRAY   */
    STAGE_MONSTER rec;
    rec.id           = std::string();                      /* init from a const */
    rec.id           = from_json<string>( (*it)["ref_id"] );        /* must be string  */
    rec.group        = (*it)["group"];                                /* int            */
    rec.next_spawn_ms= (*it)["next_spawn_ms"];                        /* int            */
    waves.push_back(rec);
}
/* part 2 -- the id list */
for (it2 = value["show_thumbnail"].begin(); it2 != end; ++it2) {       /* ARRAY of str  */
    ids.push_back( from_json<string>(*it2) );
}
m_stageMonsterLink.emplace(key, STAGE_MONSTER_LINK{ waves, ids });   /* at this+0xc   */
```

**⇒ Q2 answer: the five empty ids are the elements of
`ret_data[<key>]["show_thumbnail"]` in the `/reference/GetTargetStageMonster`
response.** They are `from_json<std::string>` reads, so they must be JSON
strings, and they must be non-empty for anything to work.

This **corrects** `analysis/research/ROOT-CAUSE-stagemonster-link.md` §2.2/§3,
which asserts the pushed strings are the *map key*. They are not: the map key is
the outer `ret_data` key (`"N003"`), and there is one map entry per stage. The
strings are the `show_thumbnail[]` array of the matched entry. The consequence for
the fix is the same in direction (the link table must carry real monster ids) but
the field to change is `show_thumbnail`, **not** the `ret_data` key.

### Why `GetMonsterData` misses

**[RECOVERED]** `CSRSyncMStage::ReqMonsterCB` (`0xb4514c`,
`ghidra-enemycamp-decomp-04.txt:239-350`) — the `/reference/GetMonster` response
parser:

```c
if (CPVHTTPResponse::GetResultCode(resp) == 1) {
    for (it = json["ret_data"].begin(); it != end; ++it)          /* ret_data = ARRAY */
        CSRGameMob::AddMonster(CSRGameMob::get(), *it);
}
```

**[RECOVERED, strong inference]** `CSRGameMob::AddMonster` (`0xa0b540`) takes
**one** parameter — the mangled name in the string table
(`analysis/native-all-strings.tsv:0x239263`) is

```
_ZN10CSRGameMob10AddMonsterERKN8nlohmann10basic_json...
```

i.e. `AddMonster(json const&)` — and it reads **no identity key**. 63 literals
were resolved from it with the wide matcher (`ghidra-enemycamp-strings-13.txt:108-172`):

```
_server title attr role res_prefix rank level overcome hp atk def crt_chance crt_dmg
penetration block_chance block_dec_dmg attr_enhance attr_resist hp_page
skill_start_time skill_list name desc type effect effect_type
target_type target_stat refer_target_stat refer_target_type
base_number up_number duration duration_up interval cool_time crt_chance
is_active cut_in_id
```

The only string read **first**, before anything else, is **`_server`**, and the
tail of the function moves that string into the pair that is then inserted:

```c
/* ghidra-enemycamp-decomp-03.txt:9283-9396 */
... build local_2b8 (12-byte string) from {local_1a0, uStack_19f, uStack_19e,
                                            puStack_19c, local_198} ...  /* = _server */
... move local_2b8 / local_194 / local_188 into the pair slots ...
__tree<value_type<basic_string, CSRGameMob::INFO>>::__emplace_unique_key_args(
        (basic_string *)&local_118, this);        /* m_mMonsters.emplace(key, INFO) */
```

`_server` is a standalone NUL-terminated literal, verified in relocated memory
(`ghidra-enemycamp-addr-15.txt`):

```
ADDRESS 01d676bb
WORD  0x7265735f  wordString=_server
NEAR  -8  01d676b3  "selected_server"
NEAR  +8  01d676c3  "id"
```

**⇒ `/reference/GetMonster`'s `ret_data` array elements must carry a non-empty
`_server` string, and that string — not `id`, not `ref_id` — is the key of
`m_mMonsters`.** This is the single most likely reason `GetMonsterData` misses
even after the request `list` is fixed: today's fixture publishes monsters under
object keys `M001`/`001` and (per the report) has no `_server` field, so
`m_mMonsters` is keyed by `""` and every lookup fails.

*Caveat:* the specific Ghidra local that becomes the `std::map` key could not be
followed through the register-allocated tail (Ghidra's stack naming is scrambled
there). The claim rests on (a) the one-parameter signature, (b) the total absence
of any other identity-shaped key across 63 resolved literals, and (c) `_server`
being the first read and the string that gets moved into the inserted pair.

---

## Q3 — the exact shape of `/reference/GetCard`'s `ret_data`

**[RECOVERED]** `CSRCardInfoContainer::SetCard` — `0x87baa4`, called from
`CSRSyncRef::ReqCardCB` at `0xf83a10` (`ghidra-enemycamp-refs-01.txt:34`).

### The container

```c
/* ghidra-enemycamp-decomp-03.txt:2116-2142 */
pbVar10 = json::operator[](param_1, "ret_data");
pCVar1 = this + 4;
__tree<value_type<basic_string, shared_ptr<CSRCardInfo>>>::destroy(this, *(this+4));
*(undefined4 *)pCVar1 = 0; *(this) = pCVar1; *(this + 8) = 0;     /* fresh map  */

bVar4 = *pbVar10;
if (bVar4 == 0x0) goto done;                          /* null  -> nothing    */
if (bVar4 == 0x1) iVar26 = *(int *)(*(int *)(pbVar10 + 8) + 8);       /* object */
else if (bVar4 == 0x2) iVar26 = (*(int**)(pbVar10+8))[1] - **(int**)(pbVar10+8) >> 4; /* array */
else iVar26 = 1;
```

`>> 4` = element stride 16 = `sizeof(nlohmann::basic_json)`. **The array branch is
the one that works**: the element is then fetched with
`json::operator[](size_type)` and indexed with `operator[]<char const>`.

### Per element

```c
/* ghidra-enemycamp-decomp-03.txt:2152-2258 */
this_01 = json::operator[](pbVar10, i);          /* array element        */
pbVar14 = json::operator[](this_01, "base");     /* sub-object           */
this_02 = operator_new(0xc4);                    /* CSRCardInfo, 196 B   */
...                                               /* CSRCardInfo at +0x0c */
this_02[0x4c] = to_bool(pbVar14["is_main"]);      /* bool                 */
pbVar15 = pbVar14["id"];  from_json<string>(pbVar15, &local_160);
*(ulonglong *)this_03 = local_160;                /* CSRCardInfo+0x00     */
pbVar15 = pbVar14["char_id"];                     /* string               */
pbVar15 = pbVar14["name"];  from_json<string>(...);
   /* ... memcmp(buf, "%user_name%", 0xb); if hit -> replace with CPVDataMgr user name */
pbVar15 = pbVar14["attr"];  CSRCardInfo::SetRefAttr(this_03, to_int(pbVar15));
pbVar15 = pbVar14["role"];  CSRCardInfo::SetRefRole(this_03, to_int(pbVar15));
```

### The key

```c
/* ghidra-enemycamp-decomp-03.txt:3078-3116 */
LAB_0087c71a:
    basic_string::basic_string(&local_160, (basic_string *)this_03);   /* = base.id */
    __tree<value_type<basic_string, shared_ptr<CSRCardInfo>>>::__find_equal(
            this, &local_170, &local_160);
    if (*pp_Var23 == 0) {           /* insert node { key = base.id, value = shared_ptr<CSRCardInfo> } */
```

### Full key list (34 literals, wide matcher)

`ghidra-enemycamp-strings-13.txt:22-57`:

```
ret_data
  base       . is_main (bool) . id (string, THE MAP KEY) . char_id (string)
             . name (string, "%user_name%" substituted) . attr (int)
             . role (int) . res_prefix
             . is_source (int; switch compares against "901" "902" "903"
                          "904" "912" "913" "914")
             . source_field
  equipment[] . id . type . rank
  stat[]      . stat . rank . cool_time
  skill        . skill
  dialog[]     . dialog . dialog_id . target_rank . chain_id
```

### Q3 answer

**`ret_data` is a bare ARRAY of records, each record containing a `base`
sub-object.** Not an object keyed by card id. The current replica fixture
(`[{base:{id:"001",...}, stat:[...], equipment:[], skill:[], dialog:[]}]`) is
structurally correct; the defect is elsewhere.

**[RECOVERED] The most likely remaining defect is JSON *type*, not shape.**
`base.id`, `base.char_id` and `base.name` are read with
`nlohmann::detail::from_json<std::string>` and the result is written into a
`CSRCardInfo` **only at the very end of the loop iteration** (line 3115). A
single `type_error` from any of those three — a numeric `id`, a missing `char_id`,
a `null` — throws out of `SetCard` **before the node is inserted**, and because
the map was destroyed at function entry the card table ends up **completely
empty**. That is precisely the observed symptom (every slot, including the one the
player owns, gets an empty ref id).

Therefore, all three of these must be present **and be JSON strings**:

- `ret_data[i].base.id`
- `ret_data[i].base.char_id`
- `ret_data[i].base.name`

The `equipment[]`, `stat[]`, `dialog[]` arrays must be present as arrays (they may
be empty). `skill` is read as an object (`skill.skill`) — send `{"skill": []}`
rather than omitting it, to stay on the recovered shape.

---

## Q4 — `/mirage/GetInfo`

### Request

**[RECOVERED]** `CSRExploreMirageInfo::RequestInfo` at **`0x92b30c`**
(`ghidra-mirage-strings-07.txt`, `RequestInfo` block). It builds, in order:

```
app_code  app_ver  market  pvid  otp  reset  stay  entry  inst_base
inst_enemy  ref_stair_list  ref_hero          ->  POST "/mirage/GetInfo"
```

Sibling routes for reference, same run:

- `/mirage/End` — `CSRExploreMirageInfo::RequestEnd` (0x92ed08):
  `app_code app_ver market pvid otp floor stair remain_deck_hp remain_enemy_hp`
- `/mirage/RegisterDeck` — `RequestRegisterDeck` (0x92fed0):
  `app_code app_ver market pvid otp inst_list`

`inst_enemy` is the **enemy instance list**, as the tester suspected. It is built
client-side; the exact source of its elements is **[UNKNOWN]** — I did not trace
the construction of the `inst_enemy` value, only that it is a request key.

### Response

**[RECOVERED]** The `/mirage/GetInfo` completion handler is **`FUN_009359ac`**
(`0x9359ac`, 1110 bytes). The mangled string table confirms the binding:

```
_ZNKSt6__ndk110__function6__funcINS_6__bindIM16CSRExploreMirage
  Fv6_ERRORRKN8nlohmann10basic_json...JPS3_RKNS_12placeholders4__phILi1EEE
  RKNSP_ILi2EEEEEENSC_ISW_EEFvS4_SK_EE11target_typeEv
```

i.e. `std::function<void(_ERROR, json const&, bool, char const*, char, char const*, char, char const*)>`
bound to `CSRExploreMirage::OnProcLoopBackMirageOpening`. `FUN_009359ac` is that
bind's invoker; it calls `Parse_Entry`, `Parse_InstBase`, `Parse_InstEnemy`,
`ParseStairInfo`, `ParseHeroInfo` (`ghidra-mirage-refs-09.txt`).

Its container keys, recovered **only** with the wide matcher
(`ghidra-mirage-strings-13.txt`; the narrow script reported `resolved: 0`):

```
ret_data.achievement
ret_data.entry       -> Parse_Entry      (0x933aec)
ret_data.inst_base   -> Parse_InstBase   (0x933d80)
ret_data.inst_enemy  -> Parse_InstEnemy  (0x92dff4)
ret_data.ref_stair   -> ParseStairInfo   (0x9343b4)
ret_data.ref_hero    -> ParseHeroInfo    (0x9347f8)
```

**Note the asymmetry: the request key is `ref_stair_list`, the response key is
`ref_stair`.** This is native evidence, not a typo.

Sub-object keys:

| parser | address | keys |
|---|---|---|
| `Parse_Entry` | 0x933aec | `id`, `mirage_remain_hp` |
| `Parse_InstBase` | 0x933d80 | `bg_res`, `dlg_begin`, `dlg_end`, `new_record`, `floor`, `stair`, `state`, `deck` → `inst_id`, `remain_hp_percent`, `tier_percent`, `highest`, `revive_price`, `begin_ltime` |
| `Parse_InstEnemy` | 0x92dff4 | `ref_id`, `rank`, `rank_up_cnt`, `overcome_cnt`, `exp`, `skill_1_level` … `skill_5_level` |
| `ParseStairInfo` | 0x9343b4 | `res_prefix`, `res_postfix_list`, `list[]` → `grade`, `balance` |
| `ParseHeroInfo` | 0x9347f8 | `bonus`, `end_ltime`, `cur`, `next` |
| `Parse_End` | 0x92c64c | `state`, `deck[]` → `inst_id`, `remain_hp_percent` |
| `Parse_HealHunter` | 0x92c8e0 | `inst_id`, `mirage_remain_hp`, `revive_price`, `user.iap.free_iap_qty`, `user.iap.iap_qty` |

**Assessment of priority.** `/mirage/GetInfo` is the *Explore-Mirage* roguelike
mode (`CSRExploreMirage` is a different `CMScene` from `CSRMStage`). The blocking
crash is in the `CSRMStage` expedition path: `MakeCamp` →
`CSRGameActorMob::MakeBackEndActor` → `GetMonsterData`. **`/mirage/GetInfo` is a
real defect worth fixing but it is not on the crash path** — it will not clear
the `731` assertions. `inst_enemy[].ref_id` is nonetheless the closest thing to a
documented enemy-instance list in the whole binary and is worth populating.

---

## Q5 — `CSRUserDB::GetCurStageID`

**[RECOVERED, low value]** Entry `0x109a89c`, decompile
`ghidra-enemycamp-decomp-06.txt:303-331`. It is a plain LevelDB read:

```c
void CSRUserDB::GetCurStageID(void) {
    FUN_006daa2c(local_28, in_r1 + 0x20, <key literal>);
    CGMLevelDB::Get<std::string>(out, this);
    ...
}
```

It reads a local, client-side value out of LevelDB; it parses no server JSON and
cannot be the source of an empty id. `CSRUserDB::GetCurStageInfo` (`0xb6ea30`) is
what `CSRMStage::MakeStageInst` calls, and on failure it logs
`"[ERR] Cannot find Mission Information"` and carries on. **Not a blocker.**

---

## What the server should send

Shapes below are **[RECOVERED]** except where marked. Send the listed keys; the
string-valued ones are read with `from_json<std::string>` and **must be JSON
strings**, not numbers and not null, or the parser throws and the table stays
empty.

### `/reference/GetTargetStageMonster` — the primary suspect

Request: `{ stage_id: "N003", pvid, otp, app_code, app_ver, market }`

```json
{
  "result_code": 1,
  "ret_data": {
    "N003": {
      "_id": [
        { "ref_id": "M001", "group": 1, "next_spawn_ms": 0 },
        { "ref_id": "M002", "group": 1, "next_spawn_ms": 800 }
      ],
      "show_thumbnail": ["M001", "M002"]
    }
  }
}
```

`ret_data` must be an **object**; `AddStageMonster` is called once per top-level
key. `_id` must be an array of objects; `show_thumbnail` must be an array of
**non-empty strings**, and it is this array that becomes the `/reference/GetMonster`
`list`. If the outer key does not match what the client asks for, the client
silently substitutes the entire table (see the `count_unique == 0` fallback above),
so a stable, predictable key matters.

### `/reference/GetMonster`

Request: `{ list: "[\"M001\",\"M002\"]", pvid, otp, app_code, app_ver, market }`
(`list` is a JSON **string** containing a dumped array.)

```json
{
  "result_code": 1,
  "ret_data": [
    {
      "_server": "M001",
      "title": "Wolf", "name": "Wolf", "desc": "",
      "attr": 0, "role": 0, "res_prefix": "M001",
      "rank": 1, "level": 1, "overcome": 0,
      "hp": 1000, "atk": 100, "def": 50,
      "crt_chance": 0, "crt_dmg": 0, "penetration": 0,
      "block_chance": 0, "block_dec_dmg": 0,
      "attr_enhance": [], "attr_resist": [], "hp_page": 0,
      "skill_start_time": 0, "skill_list": [],
      "type": 0, "effect": [], "effect_type": 0,
      "cut_in_id": 0, "is_active": 1
    },
    { "_server": "M002", "...": "same shape" }
  ]
}
```

`ret_data` is an **array**. **`_server` is the map key** — this is the field the
current fixture is missing. Publish under `_server`, and it is fine to *also*
include `id`/`ref_id` (they are ignored) — but do not rely on them.

### `/reference/GetCard`

Request: whatever the client sends. Response:

```json
{
  "result_code": 1,
  "ret_data": [
    {
      "base": {
        "id": "001",
        "char_id": "001",
        "name": "Rookie",
        "attr": 0,
        "role": 0,
        "res_prefix": "001",
        "is_main": true,
        "is_source": 901,
        "source_field": ""
      },
      "equipment": [ { "id": "000", "type": 0, "rank": 1 } ],
      "stat":      [ { "stat": 0, "rank": 1, "cool_time": 0 } ],
      "skill":     { "skill": [] },
      "dialog":    [ { "dialog": "", "dialog_id": 0, "target_rank": 0, "chain_id": 0 } ]
    }
  ]
}
```

Hard requirements, all **[RECOVERED]**:
- `ret_data` is a **bare array**;
- `base.id`, `base.char_id`, `base.name` are **strings** (any one of the three
  throwing leaves the whole table empty);
- `base.id` is the map key;
- `equipment`, `stat`, `dialog` are arrays; `skill` is an object with a `skill`
  member;
- `is_source` is an integer (compared against 901/902/903/904/912/913/914).

### `/mirage/GetInfo`

```json
{
  "result_code": 1,
  "ret_data": {
    "achievement": {},
    "entry":       { "id": 0, "mirage_remain_hp": 0 },
    "inst_base":   {
      "bg_res": "", "dlg_begin": "", "dlg_end": "",
      "new_record": 0, "floor": 0, "stair": 0, "state": 0,
      "deck": [], "tier_percent": 0, "highest": 0,
      "revive_price": 0, "begin_ltime": 0
    },
    "inst_enemy":  [ { "ref_id": "M001", "rank": 1, "rank_up_cnt": 0,
                       "overcome_cnt": 0, "exp": 0,
                       "skill_1_level": 0, "skill_2_level": 0,
                       "skill_3_level": 0, "skill_4_level": 0,
                       "skill_5_level": 0 } ],
    "ref_stair":   { "res_prefix": "", "res_postfix_list": [], "list": [] },
    "ref_hero":    { "bonus": [], "end_ltime": 0, "cur": {}, "next": {} }
  }
}
```

`ref_stair`, **not** `ref_stair_list`.

---

## Open / not resolved

1. **[UNKNOWN]** The function that populates the *enemy* camp's `ACTOR_INFO`
   list (i.e. the writer to `CSRGameBase+0x258` / `+0x26c`). `ACTOR_INFO` has no
   parser, so it is assigned field-by-field somewhere; I did not find the site.
   The inference that it draws from `m_stageMonsterLink[...].ids` is consistent
   with all five observations but is not proven from the binary.
2. **[UNKNOWN]** Which exact Ghidra local becomes the `m_mMonsters` map key in
   `AddMonster`. `_server` is the only candidate left by elimination.
3. **[UNKNOWN]** The construction of `inst_enemy` on the `/mirage/GetInfo`
   request side.
4. `MakeStageInst` at `0x925798` (the one in `AGENTS.md` §11) was not
   re-decompiled — `0x925798` is inside `CSRExploreMirage::MakeStageInst`
   (`analysis/ghidra-enemycamp-ranges-05.txt` shows `CSRExploreMirage` at
   0x925044 and `MakeStageInst` at 0x925798). The `+0x5c` claim in §Q1d is
   independently confirmed by `MakeBackEndActor`, so this does not affect any
   conclusion, but the `AGENTS.md` attribution to the *mission* path is
   probably wrong: 0x925798 is the **mirage** scene.

## Evidence files (all new, none modified)

Dumps:
- `analysis/ghidra-enemycamp-names-01.txt`, `-03.txt`, `-05.txt`
- `analysis/ghidra-enemycamp-refs-01.txt`, `-02.txt`
- `analysis/ghidra-enemycamp-decomp-01.txt` … `-06.txt`
- `analysis/ghidra-enemycamp-strings-02.txt`, `-03.txt`, `-04.txt`, `-06.txt`,
  `-13.txt`
- `analysis/ghidra-enemycamp-ranges-05.txt`, `analysis/ghidra-enemycamp-addr-15.txt`
- `analysis/ghidra-mirage-names-07.txt`, `-ranges-07.txt`, `-refs-09.txt`
- `analysis/ghidra-mirage-decomp-08.txt`, `-10.txt`
- `analysis/ghidra-mirage-strings-07.txt` … `-14.txt` (all seven)

Run logs: `analysis/ghidra-enemycamp-run-01.log` … `-06.log`,
`analysis/ghidra-enemycamp-run-15.log`,
`analysis/ghidra-mirage-run-07.log` … `-11.log`,
`analysis/ghidra-wide-run-13.log`.

New scripts (additive only; no existing script was modified):
- `analysis/ghidra-scripts/ListFunctionsInRange.java`
- `analysis/ghidra-scripts/ResolvePcRelativeStringsWide.java`