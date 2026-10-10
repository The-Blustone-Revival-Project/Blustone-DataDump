# The crash is not in `MakeStageInst` at all — and the episode scene is not server-selected

Native-analysis lane, 2026-10-02. Program `libnative_core.so`, Ghidra 12.1.3 headless,
`-noanalysis -readOnly`, project `BlustoneNative` (held exclusively for this lane).
All raw output in `analysis/ghidra-episode-*.txt` (54 files, listed at the end).

Everything below is tagged **[RECOVERED]** (function + address + excerpt),
**[INFERRED]** or **[UNKNOWN]**.

---

## 0. Headline

Three corrections, in order of how much work they save.

1. **PC `0xb2507b` is inside `CSRSceneMEpisode::OnFinish` (`0xb24f40`), not
   `MakeStageInst`.** The orchestrator's "it is between `0xb23f60` and the next
   entry `ParseBegin` at `0xb27d34`" used a *range* endpoint. `0xb27d34` is
   `CSRMFishing::ParseBegin` — **a different class** — and the real next entry
   after `MakeStageInst` is `PopUpPause` at `0xb24aec`. So the second
   re-symbolisation is wrong in exactly the same way as the first.
2. **`0xb2507b` is not an instruction boundary.** The on-disk bytes there are
   `01 28`, i.e. the halfword `0x2801` = Thumb-1 `CMP R0, #1`, which spans
   `0xb2507a..0xb2507b` and touches no memory. A PC of `0xb2507b` is a genuine
   `uc_mcontext.arm_pc`, but it cannot be the address of a faulting instruction.
   **`si_addr = 0x4c` is not self-consistent with this instruction stream
   either.** See §2. No cause should be built on `r0 = 0x0a`.
3. **The episode scene is chosen by an integer that is never derived from a
   server response.** `CSRGameBase::MODE == 7` → `CSRSceneMEpisode`;
   `default` → `CSRMStage`. Every construction site of the game scene passes a
   **compile-time immediate**; `CSRSceneGame::OnInit` reads no JSON to pick the
   subclass. So "a bare-mocked `/episode/…` response pulled us into the wrong
   scene" is **falsified as a mechanism**. (Which of the construction sites
   actually ran is **[UNKNOWN]** — see §Q1b.)

---

## Q1 — Why is an episode scene running during an expedition mission?

### Q1a. The scene selector, in full

**[RECOVERED]** `CSRSceneGame::OnInit` @ `0xe3c9a8`
(`analysis/ghidra-episode-decomp-06.txt:38-437`). The entire dispatch is one
switch on a 32-bit member at `this + 0x660`, which is the `CSRGameBase::MODE`
that was handed to the constructor (the same address is passed as
`CSRGameBase::MODE const&` to every `make_shared`):

```c
/* CSRSceneGame::OnInit() */
switch(*(undefined4 *)(this + 0x660)) {              /* ghidra-episode-decomp-06.txt:38 */
case 1:  ... make_shared<CSRFC>                     ...                       /* :47  */
case 2:  ... make_shared<CSRExploreMirage>          ...                       /* :89  */
case 3:  ... make_shared<CSRExploreAbyss>           ...                       /* :131 */
case 4:  ... make_shared<CSRFindShard>              ...                       /* :173 */
case 5:  ... make_shared<CSRTutorialMStageSkill>    ...                       /* :208 */
case 6:  ... make_shared<CSRTutorialPrologue>       ...                       /* :243 */
case 7:  ... make_shared<CSRSceneMEpisode>          ...                       /* :285 */
case 8:  ... make_shared<CSRTutorialSupportSkill>   ...                       /* :320 */
case 9:  ... make_shared<CSRGuildBattle>            ...                       /* :362 */
default: ... make_shared<CSRMStage>                 ...                       /* :404 */
}
```

**The complete, recovered MODE table:**

| `MODE` (`this+0x660`) | scene class instantiated |
|---|---|
| 1 | `CSRFC` |
| 2 | `CSRExploreMirage` |
| 3 | `CSRExploreAbyss` |
| 4 | `CSRFindShard` |
| 5 | `CSRTutorialMStageSkill` |
| 6 | `CSRTutorialPrologue` |
| **7** | **`CSRSceneMEpisode`** |
| 8 | `CSRTutorialSupportSkill` |
| 9 | `CSRGuildBattle` |
| **0, and anything ≥ 10** | **`CSRMStage`** |

So **`MODE` must be exactly `7`** for the episode scene to be built, and
**`CSRMStage` — the expedition scene — is the `default` arm.**

### Q1b. `MODE` is a constructor argument, and every value is a compile-time constant

**[RECOVERED]** `make_shared<CSRSceneGame>(CSRGameBase::MODE const&)` is at
`0xeb7394` (Ghidra: `make_shared<CSRGameBase::MODE_const&>`).
`ListCallers` gives **exactly 12 call sites**
(`analysis/ghidra-episode-callers-makescene-15.txt`):

```
0xeb22e4  LoadGameScene        0xeba836  <no function>   0xec4b02  <no function>
0xeba618  <no function>        0xeba966  <no function>   0xec4c32  <no function>
0xeba6a8  <no function>        0xebad16  <no function>
0xeba6ea  <no function>        0xebae46  <no function>
0xec49d2  <no function>
```

`CSRSceneMgr::LoadGameScene(CSRGameBase::MODE)` @ `0xeb22b8` is the only one
that takes the mode as a parameter
(`analysis/ghidra-episode-insn-14.txt`):

```
00eb22b8  push {r4,r5,r7,lr}
00eb22be  mov  r4,r0
00eb22c8  str  r2,[sp,#0x8]      ; the MODE&, argument 3
...
00eb22e4  bl   0x00eb7394        ; make_shared<CSRSceneGame>(MODE&)
00eb22ec  strd r0,r1,[r4,#0x0]   ; store into the scene manager's slot
```

…but `ListCallers 0xeb22b8` returns **no caller at all**
(`ghidra-episode-callers-loadgamescene-02.txt`: `from 0x0 <no function>`,
`callers: 1`). So `LoadGameScene` is an out-of-line copy whose callers were all
inlined; **the live mode-setting code is the eleven unanalysed sites.**

**[RECOVERED]** Every dumped site stores an immediate immediately before the
call, with the same construction preamble (`ClearTextureCache(1)`,
`ClearTextureCache(2)`, then `make_shared`):

| call site | `movs r0,#N` | ⇒ `MODE` | scene per the `OnInit` table |
|---|---|---|---|
| `0xeba618` | `#0x5` @ `0xeba5fc` | 5 | `CSRTutorialMStageSkill` |
| `0xeba6a8` | `#0x1` @ `0xeba68c` | 1 | `CSRFC` (only if the string test at `0xeba660` succeeds) |
| `0xeba6ea` | `#0x0` @ `0xeba6ce` | **0** | **`CSRMStage`** (the else branch) |
| `0xec49d2` | `#0x7` @ `0xec49b6` | 7 | `CSRSceneMEpisode` |
| `0xec4b02` | `#0x8` @ `0xec4ae6` | 8 | `CSRTutorialSupportSkill` |
| `0xec4c32` | `#0x8` @ `0xec4bca` | 8 | `CSRTutorialSupportSkill` |
| (same body) | `#0x9` @ `0xec4c16` | 9 | `CSRGuildBattle` |
| `0xeba836`, `0xeba966`, `0xebad16`, `0xebae46` | not dumped | ? | ? |

Two literals resolved **offline**, no Ghidra, from the on-disk `.so`
(`ldr rX,[lit]` at *A* + `add rX,pc` at *B* ⇒ `w[B-slot] + B + 4`):

```
ldr@0xeba668 slot=0xeba798 -> 0x1d80650  'b_00_01'
ldr@0xec4a0e slot=0xec4a68 -> 0x1d8c663  'SR_EPISODE_COMBAT'
```

The **`b_00_01` test is the only conditional mode decision found anywhere**, and
it selects **`CSRMStage` (0) vs `CSRFC` (1)** — i.e. it sits on the *expedition*
side of the switch, not the episode side:

```
/* 0xeba640..0xeba6ce  -- analysis/ghidra-episode-insn-16.txt */
00eba640  bl   0x008b3390            ; singleton get
00eba644  bl   0x008b26dc            ; -> some string accessor
00eba64c  mov  r0,r4                 ; build std::string at sp+0x10
00eba64e  bl   0x0109a89c
00eba652  ldrb.w r1,[sp,#0x10]
00eba658  ands r5,r1,#0x1            ; libc++ SSO "is long" bit
00eba65e  lsreq r0,r1,#0x1           ; length
00eba660  cmp  r0,#0x7               ; *** exactly 7 characters? ***
00eba662  bne  0xeba67e
00eba666  movs r2,#0x7
00eba668  ldr  r1,[0x00eba798]
00eba670  add  r1,pc                 ; -> "b_00_01"
00eba672  blx  0x00621b18            ; char_traits::compare
00eba68c  movs r0,#0x1               ; equal -> MODE 1 (CSRFC)
00eba6ce  movs r0,#0x0               ; not   -> MODE 0 (CSRMStage)
```

**[RECOVERED]** Ownership: `0xeba5f0` and `0xec49a0` are both in regions Ghidra
never turned into functions (`ListFunctionsInRange 0xeba400..0xec4d00`,
`ghidra-episode-ranges-16.txt`). `0xec49a0` sits between
`shared_ptr<CSRSceneMEpisodeStageList>` @ `0xec469c` (+ its
`~__shared_ptr_pointer` / `__on_zero_*` / `__get_deleter` thunks,
`0xec465c..0xec4798`) and `shared_ptr<CSRTableSkinList>` @ `0xec4cf0`.
`0xeba5f0` is the mirror image: right after `shared_ptr<CSRSceneMStageMap>` @
`0xeba430`.

**[RECOVERED]** They are `std::function` bodies. `0xec4964` is the factory:

```c
/* ghidra-episode-decomp-16.txt:83-94 */
void FUN_00ec4964(int param_1) {
    int *piVar1 = operator_new(8);                     /* sizeof(std::function) */
    int iVar2   = *(int *)(param_1 + 4);
    *piVar1     = (int)&DAT_00ec4980 + DAT_00ec4980;   /* PC-relative -> 0xec4984 */
    piVar1[1]   = iVar2;                               /* captured context      */
}
```

and `0xec4984` is the manager thunk that rebinds the invoker and copies the
captured pointer into place (`analysis/ghidra-episode-insn-19.txt`).

**[UNKNOWN] — and this is the honest limit of this section.** I do **not** know
which of the twelve sites ran. `0xec49a0` constructs **three** scenes in one
body (`MODE 7` @ `0xec49d2`, `MODE 8` @ `0xec4b02`, `MODE 8`/`9` @
`0xec4c32`/`0xec4c16`), and each time does
`holder.scene = make_shared(...); release(old); scene->vtable[0x48]("<name>")` —
that is the signature of a **registry / table builder**, not of a single
selection, and its proximity to `CSRSceneMEpisodeStageList` is address
adjacency only. So I am **not** claiming `0xec49b6` is "the site that chose the
episode scene". What *is* certain, and is all Q1 requires:

* `MODE` is a constructor argument, never a parsed field;
* every recovered construction site passes a compile-time immediate, so no
  response body can change it;
* `CSRSceneGame::OnInit` performs no JSON read to pick the subclass.

**[UNKNOWN]** To close it: find which of the twelve `make_shared<CSRSceneGame>`
sites executes. `ListCallers 0xec4964` is the cheapest first step, but prefer
the `0xeba534` neighbourhood — the `b_00_01` test there is the only mode
decision in the binary that is *conditional on data*, and it is the one that
yields `CSRMStage`.

### Q1c. Answer: is the replica driving it there?

**No — and this is the answer to the question that matters most.**

**[RECOVERED]** Three independent negatives:

1. `CSRSceneGame::OnInit` reads no JSON. It switches on `*(uint32*)(this+0x660)`.
   `ResolvePcRelativeStringsWide` over `CSRSceneGame` / `OnInit`
   (`ghidra-episode-strings-06.txt`, 90 KB, `OnInit` included) resolves UI
   resource paths only (`SR_INGAME/UI_BOSS`, `SR_INGAME/UI_SKILL`,
   `SR_INGAME/UI_HP_N`); `LoadGameScene` resolves **0** literals
   (`ghidra-episode-strings-02.txt:11-12`).
2. `MODE` is never parsed from a response anywhere in the trace. It is a
   constructor argument, and every live construction passes a compile-time
   immediate (§Q1b).
3. `/episode/*` in this binary is exactly three route strings —
   `/episode/GetLog`, `/episode/Read`, `/episode/Reward`
   (`analysis/native-all-strings.tsv:01d79d72, 01d7ad4e, 01d7ad5c`). The replica
   serves only `/episode/GetLog`, and its consumer is
   `CSRInstanceSync::ReqEpisodeCB` → `CSRMEpisode::ParseLog`, which populates
   `read_log` / `reward_log`. **[RECOVERED]** `CSRSceneMEpisode::MakeStageInst`
   and `CSRSceneMEpisode::OnFinish` read **no** JSON at all (below), so no
   `/episode/GetLog` reply can steer them.

**⇒ "an `/episode/...` bare mock pulls the client into the wrong scene" is
falsified as a mechanism.** The replica has no lever on that switch: the mode
is a constructor argument, every recovered value is a compile-time immediate,
and the switch that consumes it reads no JSON.

### Q1d. What the episode scene actually needs — and why it cannot work here

**[RECOVERED]** `CSRSceneMEpisode::MakeStageInst` @ `0xb23f60` (next entry
`PopUpPause` @ `0xb24aec`, so the body is `0xb23f60..0xb24aeb`) resolves
**exactly four literals and nothing else** — no JSON key, no route, no
`/reference/*` name:

```
$ python tools/resolve-literals-offline.py --function 0xb23f60:0xb24aec
ldr@0x00b23f7c r6 slot=0x00b242d8 w=0x012519ba add_pc=0x00b23f88 -> 0x01d75942  'episode_stage'
ldr@0x00b24008 r4 slot=0x00b242dc w=0x01256cc3 add_pc=0x00b24010 -> 0x01d7acd3  'episode'
ldr@0x00b24170 r4 slot=0x00b242e4 w=0x01256d49 add_pc=0x00b2417e -> 0x01d7aec7  'monster'
ldr@0x00b247a6 r7 slot=0x00b24ae4 w=0x01256713 add_pc=0x00b247b4 -> 0x01d7aec7  'monster'
resolved: 4
```

> **Correction to `analysis/research/FALSIFIED-showthumbnail.md` §3.** That file
> quotes the same tool run as `--function 0xb23f60:0xb27d34` and presents all 39
> literals as coming from `CSRSceneMEpisode::MakeStageInst`. That range spans
> **six functions of two classes**; only the first four literals above belong to
> `MakeStageInst`. See §Q2c for the full attribution table. The orchestrator's
> own summary of it ("only literal within ~1 KB of the crash PC is `009`") is
> also wrong on both counts — `009` is in a different function from the crash.

Reconstructed body (`analysis/ghidra-episode-decomp-02.txt:90-777`):

```c
/* CSRSceneMEpisode::MakeStageInst() */
this->str_244.assign("episode_stage", 13);              /* :90-92   */
this->pair_230 = *(CPVDataMgr + 0x58);                  /* :93-96    */
this->u_240   = *(CSRUserDB + 0x1fc);                  /* :97-123   */
basic_string k = "episode";                             /* :129-132  */
CSRUserDB::GetDeck(&deck_list, k);                      /* :133      */
/* camp A -> this+0x250, camp B -> this+0x264, both keyed CMHashID(to_string(...)) */
for (i over CSRMEpisode::GetCombat()->vec_68, stride 0x48) {          /* :185-556 */
    if (rec.name.empty()) {                        /* player side          */
        CSRInventory::FindCard(deck[i]);            /* :217                  */
        CSRCard::SetRefID(actor, card + 0x5c);      /* :240  (the +0x5c)   */
        CSRCard::SetAwake / SetOvercome / GetRank;                       /* :234-239 */
        CSRLevelData::CalcBonus(...); CMHashID::Set(...);               /* :288-315 */
    } else {                                       /* enemy side           */
        if (rec.name.size()==7 && memcmp(rec.name,"monster",7)==0)       /* :405-421 */
            actor_flags |= 0x18;
        actor->rank = rec[0x10]; CSRCard::SetAwake(rec[0x18]);
        CSRCard::SetOvercome(rec[0x14], rec[0x1c]); ...
    }
}
for (j over CSRMEpisode::GetCombat()->vecvec_74_78, inner stride 0x48) {/* :557-752 */
    if (!rec.name.empty()) { ... same enemy build, again memcmp "monster" ... }  /* :627-636 */
}
```

**There is no `CSRGameMob` call in it.** `ListCallers 0xa0cf38`
(`GetStageMonsterLinkData`, `ghidra-episode-callers-getlink-03.txt`) has 9 call
sites and **`0xb23f60` is not one of them**:

```
from 0x9008e4  MakeStageInst      from 0xe1b648  OnReset
from 0x906bee  MakeStageInst      from 0xe7fccc  SetMission
from 0xb34b18  MakeStageInst      from 0xe81602  SetAbyss
from 0xefe6a8  MakeStageInst      from 0xb4a7e6  FUN_00b4a7a8
```

`0xb34b18` lies inside `CSRMStage::MakeStageInst` @ `0xb33f84` (body 4552 ⇒
`0xb33f84..0xb3514c`). **[RECOVERED]** So the *only* function on the
expedition path that reads the stage-monster link table to build a camp is
`CSRMStage::MakeStageInst`, and **while the client is in the episode scene it is
never entered.** That is a structural explanation for why five rounds of
`/reference/GetTargetStageMonster` work moved nothing: the consumer was not
running.

**[RECOVERED]** `CSRSceneMEpisode::OnFinish` @ `0xb24f40` (next entry
`PopUpResultWin` @ `0xb2547c`, so the body is `0xb24f40..0xb2547b`) has the
same shape — no JSON, and one hard dependency:

```c
/* CSRSceneMEpisode::OnFinish(unsigned char result) -- ghidra-episode-decomp-02.txt:782-1112 */
CSRGameBase::ReleaseResource(this, 1);
if (result == 0) {
    CSRMEpisode::get(); CSRMEpisode::GetCombat();
    /* std::string at combat+0x48 : size/flag @+0x48, data ptr @+0x4c, capacity @+0x50 */
    pbVar14 = (basic_string *)(local_60 + 0x48);                       /* :856  */
    uVar3   = length_or_flag;  if (uVar3 != 0) {                       /* :881  */
        CSRUserDB::IsFirstAction(db, pbVar14);                         /* :884  */
        if (== 1) CSRUserDB::PutFirstAction(db, pbVar14);              /* :900  */
    }
} else if (result == 1) {
    pbVar13 = (basic_string *)(local_60 + 0x3c);                       /* :909  */
}
if (*pbVar13 == 0) {                     /* empty                          */
    CSRPopUpGameResultFail::SetStageID(popup, this + 0x220);           /* :942  */
    CSRScene::SetCurScene(popup, 0x37);                                /* :944  */
    CSRUIModalHandler::Push(...);                                      /* :1029 */
} else {                                 /* non-empty                      */
    CSRUserDB::PutDialogID(db, pbVar13);                               /* :1060 */
    CSRUIModalHandler::PushDlg(..., pbVar13, ...);                     /* :1063 */
    CSRPopUpDlg::SetSoundRestore(popup, 0);                           /* :1073 */
}
```

`CSRMEpisode::COMBAT` is created by the episode flow
(`CSRSceneMEpisodeStageList::SelectEpisode`, `CheckSceneState`,
`RequestClear`, `RequestReward` — `analysis/native-all-strings.tsv:0030f71a`ff).
**[INFERRED — strong]** On an expedition mission nothing ever creates it, so
`GetCombat()` yields a null/empty record and every `+0x3c / +0x48 / +0x54`
member read is on a bad pointer. That is the only crash-relevant dependency in
`OnFinish`, and it is exactly the thing an expedition cannot supply.

**[UNKNOWN]** Why the client ends up in the episode scene at all. Per §Q1b I did
not establish which of the twelve `make_shared<CSRSceneGame>` sites runs, and I
am not going to guess from address adjacency. The concrete facts a follow-up
needs:

* `CSRSceneMEpisode` is reachable only via `MODE == 7`, and the recovered
  `MODE 7` construction sits in a `std::function` body (`0xec49a0`, factory
  `FUN_00ec4964` @ `0xec4964`) inside the
  `CSRSceneMEpisodeStageList` **neighbourhood** of the scene-factory table.
* The one *data-dependent* mode decision in the binary is the `b_00_01` test at
  `0xeba660`, and it is on the **expedition** side: it chooses
  `CSRMStage` (0) over `CSRFC` (1).

**Exact next probes, in order:** (1) `ListCallers 0xec4964` and
`ListCallers` on the `FUN_00eba534` factory, to find who registers these
`std::function`s; (2) find the string source feeding the `b_00_01` compare at
`0xeba640` (`bl 0x008b3390` / `bl 0x008b26dc`) and check whether the replica
can influence it — **if it can, that is a server-controlled scene selector and
Q1 flips from "client-side" to "server-side", so this is the highest-value
single question in this report.**

### Q1e. `ApplyScene` / `SceneGoTo` are not involved

For completeness, so nobody re-checks them: `CSRSceneMgr::ApplyScene` @ `0xea6600`
is scene-stack plumbing (`[WRN] [%s] `, `"Make sure that you really called
AddScene"`, `"Scene Not Found"` — `ghidra-episode-strings-02.txt:1-10`); it never
touches `MODE`. `CSRSceneMgr::SceneGoTo(CSRScene::TYPE)` @ `0xeb48c4` is a
130-reference dispatcher over a *different* enum (`CSRScene::TYPE`: cases 9,
0x10, 0x11, 0x14, 0x19, 0x20, 0x26, 0x28, 0x34, 0x36, 0x3a, 0x42, 0x46, 0x52,
0x57, 0x59, 0x5d, 0x66, 0x68, 0x6f, 0x75, 0x76, 0x7d, 0x82…0x98) and never
touches `MODE` either. **[RECOVERED]** Do not conflate `CSRScene::TYPE` with
`CSRGameBase::MODE`; they are unrelated enums and neither is JSON.

---

## Q2 — What is at PC `0xb2507b`, and what is `009`?

### Q2a. The containing function

**[RECOVERED]** `DecompileAtAddress 0xb2507b` returns
`===== 0xb2507b OnFinish @ 00b24f40 =====`
(`ghidra-episode-decomp-02.txt:780-782`), confirmed by
`ListFunctionsInRange 0xb23000..0xb29000`
(`ghidra-episode-ranges-02.txt:14-19`):

```
FUNC 00b23c14  CSRSceneMEpisode          body=32
FUNC 00b23c38  InitBeforeOpen            body=430
FUNC 00b23e80  InitBackground            body=154
FUNC 00b23f60  MakeStageInst             body=2516     <- entry, ends 0xb24aeb
FUNC 00b24aec  PopUpPause                body=522
FUNC 00b24dc0  smart_point_cast<...>     body=300
FUNC 00b24f40  OnFinish                  body=1024     <- CONTAINS 0xb2507b
FUNC 00b2547c  PopUpResultWin            body=850
FUNC 00b25930  SetBGM                    body=272
```

So `0xb2507b ∈ CSRSceneMEpisode::OnFinish(unsigned char)`, entry `0xb24f40`,
body `0xb24f40..0xb2547b`. **`OnFinish` is the battle-*finish* callback** —
`CSRGameBase` invokes it as a virtual once the stage concludes. That is
consistent with report-011/012 observing the battle HUD built before the fault:
the battle ran, and the client died in the end-of-battle handler.

### Q2b. The faulting instruction — there isn't one

**[RECOVERED, byte-level, offline]** `tools/resolve-literals-offline.py`'s
address model (`Ghidra address == file offset + 0x10000`) applied to file offset
`0xa15060`:

```
0xb25060 c107 0x7c1      ldrb r0,[r6,#0x0]
0xb25062 0cbf 0xbf0c     ite  eq
0xb25064 4008 0x840      lsreq r0,r0,#0x1
0xb25066 e86c 0x6ce8     ldreq r0,[r5,#0x4c]        <-- candidate A
0xb25068 f0b1 0xb1f0     cbz  r0,0x00b250a8
0xb2506a 8ef5 0xf58e     bl   0x008b3390             (CSRDataMgr::get)
0xb2506e 8df5 0xf58d     bl   0x008b26dc             (GetUserLocalDB)
0xb25072 3146 0x4631     mov  r1,r6
0xb25074 77f1e6f6        bl   0x0109ce44             (CSRUserDB::IsFirstAction)
0xb25078 04ac 0xac04     add  r4,sp,#0x10
0xb2507a 0128 0x2801     cmp  r0,#0x1                <-- *** 0xb2507a..0xb2507b ***
0xb2507c 15d1 0xd115     bne  0x00b250aa
0xb2507e b442 0x42b4     cmp  r4,r6
0xb25080 0bd0 0xd00b     beq  0x00b2509a
0xb25082 95f848 0xf895   ldrb.w r0,[r5,#0x48]
0xb25086 d5e91321        ldrd r2,r1,[r5,#0x4c]       <-- candidate B
0xb2508a 10f00103        ands r3,r0,#0x1
```

(The two 4-byte rows are Thumb-2 `ldrd`; Ghidra's listing prints the same bytes.)

Halfword `0x2801` is Thumb-1 `CMP R0, #1` (`00101 Rd imm8`, `Rd = r0`,
`imm8 = 1`). It occupies `0xb2507a`–`0xb2507b` and **performs no memory
access**. Its neighbours are clean 16-bit boundaries: `0xb25074` is a 4-byte
`BL` (`0xf177`/`0xf6e6`) and `0xb25078` is `0xAC04` = `ADD R4, SP, #16`.

The probe is trustworthy on this point: `tools/arm-crash-probe.c:395-400`

```c
static void fault(int signal_number, siginfo_t *signal_info, void *opaque) {
    ucontext_t *context = opaque;
    __android_log_print(..., "signal=%d code=%d fault=%p",
        signal_number, signal_info->si_code, signal_info->si_addr);
    address("ARM-PC", context->uc_mcontext.arm_pc);
```

so `pc=0x4b2507b` is a real `arm_pc` with module base `0x4000000`
(`offset=0xb2507b`), and `fault=0x4c` is a real `si_addr` of `0x4c`.

**[RECOVERED]** Therefore:

* the reported PC cannot be the address of the faulting instruction, and
* **`si_addr = 0x4c` is not self-consistent with this instruction stream
  either.** The only two instructions here that could fault at `0x4c` are
  `ldreq r0,[r5,#0x4c]` @ `0xb25066` and `ldrd r2,r1,[r5,#0x4c]` @ `0xb25086`,
  and both require `r5 == 0`. But `ldrb r0,[r6,#0x0]` @ `0xb2505e` with
  `r6 = r5 + 0x48` executes *first*, so `r5 == 0` would have faulted at
  **`0x48`**, not `0x4c`.

**[INFERRED]** The `(pc, si_addr, r0..r3)` triple from reports 011/012 is not a
coherent single frame and must not be used to build a mechanism. This is the
same trap `ghidra-enemy-actor-trace.md` already flagged for the stack-candidate
offsets ("the `+0x9c3df1 MakeCamp` … offsets are **return addresses, not
function entries**") — the register/PC triple deserves the same scepticism.

**[RECOVERED]** For the record, `r0 = 0x0a` at `0xb2507a` is *benign*: `r0` is
the return value of `CSRUserDB::IsFirstAction`, and `cmp r0,#1 / bne` simply
means "not the first action for this episode", taking `LAB_00b250aa`.

**Do not assert a cause here.** There is nothing at this PC to assert one from.

### Q2c. `009` is not near the crash, and the literal dump that suggested it was contaminated

**[RECOVERED]** `tools/resolve-literals-offline.py --function 0xb23f60:0xb27d34`
(quoted in `analysis/research/FALSIFIED-showthumbnail.md` §3) was run over a
**range spanning six functions of two classes**, not over `MakeStageInst`.
Attributing those 39 literals to one function is wrong. Correct attribution,
using the `ListFunctionsInRange` boundaries:

| literal(s) | load site | actually inside |
|---|---|---|
| `episode_stage`, `episode`, `monster` ×2 | `0xb23f7c`–`0xb247a6` | `CSRSceneMEpisode::MakeStageInst` (`0xb23f60..0xb24aeb`) |
| `[AST] [%s] `, `Cannot convert Src(%s) to Dst(%s)`, `sic.h`, `)` | `0xb24e36`–`0xb24e8e` | `smart_point_cast<CSRSceneMEpisode,…>` (`0xb24dc0`) |
| **`009`** | **`0xb2553e`** | **`CSRSceneMEpisode::PopUpResultWin` (`0xb2547c..0xb2592f`)** |
| `BGM_BATTLE1` | `0xb25982` | `CSRSceneMEpisode::SetBGM` (`0xb25930..0xb25a3f`) |
| `PopUpPause`/`OnFinish`/`PopUpResultWin` `$N` lambda name strings | `0xb25d10`–`0xb261f0` | unanalysed lambda bodies / vtable thunks |
| `FX_RESULT` | `0xb26270` | a `PopUpResultWin` lambda |
| `common1` | `0xb265c4` | unanalysed lambda body |
| **`place_id`, `cast_dist`, `lure_id`, `/fishing/Begin`, `app_code`…`otp`** | `0xb26d32`–`0xb27044` | **`CSRMFishing::RequestBegin` (`0xb26cbc..0xb274b5`)** — a different class |
| `result_code` | `0xb27c14` | `CSRMFishing::ReqBeginCB` (`0xb27b38..0xb27cb7`) |
| — | — | `0xb27d34` is **`CSRMFishing::ParseBegin`**, not the episode's |

So: `009` is `0x4C3` bytes from `0xb2507b`, **but in a different function**
(`PopUpResultWin`, the *result popup*). It is used at `0xb2553e`
(`ghidra-episode-insn-03.txt:25-33`) as a `const char*` handed to
`bl 0x006d5ff4` (a `std::string` constructor) and then compared at `0xb25550`
via `bl 0x0087d2ec`, i.e. **a string value, not a container size or index
bound.** `PopUpResultWin`'s own code shows the pattern: it reads
`CSRDataSyncMgr`'s monster/level pointer (`ldr.w r0,[r8,#0x2f0]`) and, when
that is empty, falls into the `009` string path
(`analysis/ghidra-episode-insn-03.txt:3-23` vs `:24-33`).

**[UNKNOWN]** Why `009`. It is not a container size and it is not near the
faulting function. I did not recover its meaning. Per the brief, I am not
asserting a cause.

---

## Q3 — Was `AddStageMonster` ever reached?

### Q3a. Yes. Unconditionally, once per top-level `ret_data` key.

**[RECOVERED]** `CSRSyncMStage::ReqTargetStageMonsterCB` @ `0xb4606c`
(`analysis/ghidra-episode-decomp-02.txt:1151-1291`):

```c
if (CPVHTTPResponse::GetResultCode(resp) != 1) goto LAB_00b4619e;      /* :1199-1200 */
json = operator[](resp, "ret_data");                                    /* :1201-1203 */
iteration_proxy::begin();                                              /* :1204-1206 */
/* array(0x2) / object(0x1) / scalar all produce >=1 iteration */
while (iter != end) {                                                  /* :1230-1233 */
    this     = CSRGameMob::get();                                       /* :1234    */
    pbVar3   = iteration_proxy_value::key(&iter);      /* the object KEY */ /* :1235-1239 */
    pbVar4   = iter_impl::operator*(&iter);           /* the VALUE      */ /* :1240-1244 */
    CSRGameMob::AddStageMonster(this, pbVar3, pbVar4);   /* <== UNCONDITIONAL */ /* :1245 */
    ... iterator advance ...
}
```

Instruction-level confirmation (`analysis/ghidra-episode-insn-11.txt`):

```
00b46100  str  r0,[sp,#0x3c]
00b46102  ldr  r0,[sp,#0x40]
00b46104  adds r0,#0x1
00b46106  str  r0,[sp,#0x40]
00b46108  mov  r0,r4
00b4610a  mov  r1,r8
00b4610c  bl   0x0072af38          ; iter_impl::operator!=  -> loop test
00b46110  cbnz r0,0x00b46166      ; exit
00b46112  bl   0x00a0dac0         ; CSRGameMob::get
00b46116  mov  r6,r0
00b46118  mov  r0,r4
00b4611a  bl   0x007211b8         ; iteration_proxy_value::key
00b4611e  mov  r5,r0
00b46120  mov  r0,r4
00b46122  bl   0x0072aff0
00b46126  mov  r2,r0              ; value
00b46128  mov  r0,r6              ; CSRGameMob*
00b4612a  mov  r1,r5              ; key
00b4612c  bl   0x00a0d194         ; <<< CSRGameMob::AddStageMonster
00b46130  ldr  r0,[sp,#0x30]      ; loop bookkeeping
00b46132  ldrb r0,[r0,#0x0]
00b46134  cmp  r0,#0x2
00b46136  beq  0x00b4615e
00b46138  cmp  r0,#0x1
00b4613a  bne  0x00b460fc         ; back-edge
```

There is **no guard between the loop test and the call** — no test of
`_id`, no test of `show_thumbnail`, no key comparison. The only gate is
`result_code == 1`. Our replica returns `1`.

`ListCallers 0xa0d194` (`ghidra-episode-callers-addstagemonster-02.txt`)
confirms the single live caller:

```
target 0xa0d194  function=AddStageMonster
  from 0x0  <no function>
  from 0xb4612c  ReqTargetStageMonsterCB
callers: 2
```

### Q3b. What that retires, and what it does not

**`analysis/research/FALSIFIED-showthumbnail.md` §2's second hypothesis —
"`AddStageMonster` is never reached on our record" — is FALSE.** It is reached,
and `m_stageMonsterLink` is emplaced once per `ret_data` key. **The
`_id` / `show_thumbnail` / `wave_list` / key-shape line of work is therefore
*not* aimed at dead code**, and the "`AddStageMonster` never runs" reading in
`ghidra-enemy-actor-trace.md` §Q2's "Open / not resolved" item 1 should be
closed as **recovered: it does run**.

What survives, and is now the only remaining explanation for
"`/reference/GetMonster` never fires", is downstream of the emplace.
**[RECOVERED]** `CSRGameMob::GetStageMonsterLinkData` @ `0xa0cf38`
(`analysis/ghidra-episode-decomp-03.txt:7-63`) — note carefully that the
`__count_unique == 0` fallback copies **`this + 0x18` and `this + 0x24`**, two
*other* vectors of `CSRGameMob`, **not** the map's contents:

```c
/* CSRGameMob::GetStageMonsterLinkData(key) -- ghidra-episode-decomp-03.txt:26-56 */
if (__count_unique(this + 0xc /*m_stageMonsterLink*/, key) == 0) {
    vector<vector<STAGE_MONSTER>>::vector(out1, this + 0x18);   /* :31  NOT the map */
    vector<string>::vector          (out2, this + 0x24);       /* :35  NOT the map */
} else {
    node = __find_equal(this + 0xc, key);
    if (!node) FUN_006d8570("map::at:  key not found");       /* :47  fatal */
    vector<vector<STAGE_MONSTER>>::vector(out1, node + 0x1c);  /* :52  waves */
    vector<string>::vector          (out2, node + 0x28);      /* :56  ids    */
}
```

If the key `FUN_00b4a7a8` asks for is **not** a key we published, the client
silently substitutes `CSRGameMob+0x18` / `+0x24`. **[UNKNOWN]** I did not
determine whether those two vectors have any writer in the binary, so I cannot
say whether that is what makes the `list` empty. That is now the single
highest-value reachability question on this path, and it is one decompile plus
one writer search.

**Independent of all of the above**, §Q1d supplies the structural reason the
stage-monster response could never have mattered *in these runs*: the client is
in `CSRSceneMEpisode`, whose `MakeStageInst` does not call
`GetStageMonsterLinkData` at all, so the expedition enemy-camp builder
`CSRMStage::MakeStageInst` @ `0xb33f84` never runs.

---

## Method notes / corrections for the record

* **Function boundaries, not range endpoints.** `ghidra-episode-ranges-02.txt`
  is the authority for "which function owns address X". A wide literal scan
  must be intersected with it before any literal is attributed.
* **`CSRSceneGame::ApplyScene` @ `0xea6600` times out** the 120 s
  `DecompileAtAddress` budget; `DumpInstructions` on `0xea6600..0xea6840`
  succeeded and is sufficient (it contains no mode logic).
* **`analyzeHeadless` on Windows `cmd.exe` chokes on `<` and `&` in
  `-postScript` arguments** (`"& was unexpected at this time"`,
  `"The system cannot find the file specified"`). Avoid `make_shared<…>` and
  `MODE&` as name fragments in `ListFunctionNames` / `ResolvePcRelativeStrings`
  arguments; use `CSRSceneGame` or `MODE` instead.
* **An ad-hoc offline Thumb `BL`/`B.W` scanner I wrote gave 0 hits for
  `AddStageMonster`,** which Ghidra proves is called from `0xb4612c`
  (`bl 0x00a0d194`). My halfword discrimination was wrong. Do not trust that
  scanner; `ListCallers` plus `DumpInstructions` are correct. The
  `resolve-literals-offline.py` `ldr`+`add pc` model was independently
  re-verified here on three literals (`b_00_01`, `SR_EPISODE_COMBAT`,
  `009`) and is sound.

## Verdict

**Yes, the client is in the wrong scene — and no server response drives it
there.** `CSRSceneGame::OnInit` @ `0xe3c9a8` picks the scene class from a
`CSRGameBase::MODE` int at `this + 0x660` (`case 7` → `CSRSceneMEpisode`,
`default` → `CSRMStage`), and that mode is a *constructor argument* passed as a
compile-time immediate at every recovered construction site, with no JSON read
anywhere on the path — so the `/episode/…` theory is dead as a mechanism. The
concrete, recovered defect on the crash path is that
`CSRSceneMEpisode::MakeStageInst` (`CSRMEpisode::GetCombat()` +
`CSRUserDB::GetDeck("episode")`, four literals, no JSON) and
`CSRSceneMEpisode::OnFinish` (`CSRMEpisode::GetCombat()` again, then member
reads at `combat+0x3c`/`+0x48` with no null check) are being run with an episode
`COMBAT` record that an expedition mission never creates, while
`CSRMStage::MakeStageInst` — the *only* consumer of the stage-monster link table
on the mission path — is never entered.

## Files (all new, nothing existing modified)

Dumps:
`ghidra-episode-names-01/05/08/14.txt`, `-ranges-02/03/04/07/16/17.txt`,
`-decomp-02/03/04/05/06/07/09/10/12/15/16.txt`,
`-insn-02/03/06/11/12/13/14/15/16/17/18/19.txt`,
`-strings-02/03/06/08/09/16.txt`,
`-callers-{addstagemonster,applyscene,csrscenegame,epinitbeforeopen,episodemakeshared,episodemsi,funb4a3cc,getlink,loadgamescene,makescene,movescene,mstagemakeshared,pushfadeoutin,pushscene,reqtgt,scenegoto,sceneinit}-*.txt`

Run logs: `ghidra-episode-run-01.log` … `-run-19.log`

Scripts: **none added or modified** — every run used the existing
`analysis/ghidra-scripts/*`. All Ghidra access was `-readOnly`.