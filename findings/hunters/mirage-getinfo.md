# `/mirage/GetInfo` — determination, and the native spec needed to close it

Written by the **server agent**, 2026-10-02. Read-only research over the tables
already on disk (`analysis/native-evidence.tsv`, `analysis/native-all-strings.tsv`,
`analysis/ghidra-*.txt`, `analysis/native-*.txt`). No Ghidra, no adb.

---

## 0. Verdict, up front

> **`/mirage/GetInfo` is NOT the carrier of the expedition's five empty enemy
> ref ids.** It is a genuine mock-coverage gap and it should be reconstructed
> eventually, but it is a **different game mode** from the expedition, it is
> **requested at lobby boot and never again at battle time**, and its enemy
> records are consumed by a **Mirage pre-battle popup**, not by
> `CSRGameBase::MakeCamp`.

I did **not** implement a shape for it. Reasoning in §4.

---

## 1. What is actually recovered

### 1.1 The request, exactly

The request body literals are contiguous in `.rodata`, which is a strong
indication they are one function's key list:

```
$ grep 01d72e analysis/native-all-strings.tsv
01d72ecf  reset
01d72ed5  stay
01d72eda  entry
01d72ee0  inst_base
01d72eea  inst_enemy
01d72ef5  ref_stair_list
```

`app_code`, `app_ver`, `market`, `pvid` come from the common request envelope.
This matches the observed `request_keys` in
`analysis/testing/report-009.md` §6 exactly, so the request side is settled.

`reset` / `stay` / `entry` are **flags**: "reset my run", "I am resuming", "this
is a fresh entry". `inst_base` is the player's own Mirage deck base,
`ref_hero` the hero reference, `ref_stair_list` the stair/floor layout,
`inst_enemy` the opponent's instances.

### 1.2 The whole owner class is named and located

Every symbol in the model class is retained in `analysis/native-evidence.tsv`.
This is the complete Mirage-mode request/parse surface:

| address | symbol |
|---|---|
| `0x0092b30c` | `CSRExploreMirageInfo::RequestInfo(bool, int, int, function<void(shared_ptr<CPVHTTPRequest>, shared_ptr<CPVHTTPResponse>)>, unsigned char)` |
| `0x00196a7a` | same, PLT-ish thunk |
| `0x0092c428` | `CSRExploreMirageInfo::ParseDeckInfo(const json&)` |
| `0x0092c5ac` | `CSRExploreMirageInfo::SetSaveDeckInfo(const list<unsigned>&)` |
| `0x0092c64c` | `CSRExploreMirageInfo::Parse_End(const json&)` |
| `0x0092c8e0` | `CSRExploreMirageInfo::Parse_HealHunter(const json&)` |
| `0x0092cb5c` | `CSRExploreMirageInfo::ParseRewardInfo(const json&)` |
| `0x0092dff4` | `CSRExploreMirageInfo::Parse_InstEnemy(const json&)` |
| `0x0092e868` | `CSRExploreMirageInfo::MakeRandResPostFix()` |
| `0x0092e8bc` | `CSRExploreMirageInfo::GetBaseInfo()` |
| `0x0092eb58` | `CSRExploreMirageInfo::GetEnemyInfo() const` |
| `0x0092eb5c` | `CSRExploreMirageInfo::GetStairInfo() const` |
| `0x0092eb60` | `CSRExploreMirageInfo::GetHeroInfo() const` |
| `0x0092eb64` | `CSRExploreMirageInfo::GetFriendInfo() const` |
| `0x0092eb6c` | `CSRExploreMirageInfo::IsMirageEntry(unsigned char)` |
| `0x0092eb90` | `CSRExploreMirageInfo::IsNotiCondition()` |
| `0x0092ec5c` | `CSRExploreMirageInfo::GetSaveDeckInfo() const` |
| `0x0092ecda` | `CSRExploreMirageInfo::IsMirageDeckCard(unsigned char)` |
| `0x0092ed08` | `CSRExploreMirageInfo::RequestEnd(int, int, const list<pair<unsigned,char>>&, const vector<unsigned>&, const function<...>&, unsigned char)` |
| `0x0092fed0` | `CSRExploreMirageInfo::RequestRegisterDeck(const list<unsigned>&, callback)` |
| `0x00930b60` | `CSRExploreMirageInfo::RequestHealHunter(bool, const function<...>&, unsigned char)` |
| `0x00931764` | `CSRExploreMirageInfo::RequestFriend(const function<...>&, unsigned char)` |
| `0x009322d8` | `CSRExploreMirageInfo::RequestNextFloor(const list<unsigned>&, const function<...>&, unsigned, unsigned char)` |
| `0x00932e4c` | `CSRExploreMirageInfo::RequestReward(int, int, cb, cb, const SRREWARD_INFO&)` |
| `0x00933aec` | `CSRExploreMirageInfo::Parse_Entry(const json&)` |
| `0x00933d80` | `CSRExploreMirageInfo::Parse_InstBase(const json&)` |
| `0x009343b4` | `CSRExploreMirageInfo::ParseStairInfo(const json&)` |
| `0x009347f8` | `CSRExploreMirageInfo::ParseHeroInfo(const json&)` |
| `0x00934c00` | `CSRExploreMirageInfo::ParseFriendInfo(const json&)` |
| `0x00934f1c` / `0x00934f80` | `CSRExploreMirageInfo::get()` |

The `/mirage/GetInfo` **response dispatcher** is the closure
`PVHTTP::TASK_READY<...>::RequestInfo(...)::$_0`, whose RTTI strings sit at
`0x01debadf` (`__func...$_0`) and `0x01deb939` (`...$_0`), with the
`std::function` type instantiations at `0x01debca9` / `0x01debe50`. That
closure is what calls the nine `Parse_*` functions.

### 1.3 `inst_enemy`'s record shape — RECOVERED

`analysis/ghidra-makestageinst-keys.txt` lines 13–25 already resolved the string
literals inside `Parse_InstEnemy` (0x0092dff4):

```
===== 0092dff4 Parse_InstEnemy =====
  "n"            (0x1d6f95a)
  "ref_id"       (0x1d6edf2)
  "rank"         (0x1d6fa90)
  "rank_up_cnt"  (0x1d6fa95)
  "overcome_cnt" (0x1d6fa26)
  "exp"          (0x1d6ede1)
  "skill_1_level" (0x1d6fb41)
  "skill_2_level" (0x1d6fb4f)
  "skill_3_level" (0x1d6fb5d)
  "skill_4_level" (0x1d6fb6b)
  "skill_5_level" (0x1d6fb79)
```

So an `inst_enemy` **element** is
`{ n, ref_id, rank, rank_up_cnt, overcome_cnt, exp, skill_1_level..skill_5_level }`.
`n` is a sequence/position number. This is a card-instance record, not a monster
record — note there is no `hp`/`atk`/`attr`/`role`.

### 1.4 `Parse_InstEnemy` really does feed `CSRCard::SetRefID`

```
$ grep Parse_InstEnemy analysis/ghidra-setrefid-callers.txt
  from 0x92e1f2  Parse_InstEnemy
```

`SetRefID` (0x86c30c) is one of only two call sites inside `Parse_InstEnemy`,
and it asserts `sRefID.length() > 0` at `SRCard.cpp:731`. So the Mirage
opponent's `ref_id` values are turned into `CSRCard` objects exactly the way
`ParseUserDatailInfo` does.

This is the part of the correlation in report-009 §6 that is real. It is also
the part that turns out not to be the expedition.

### 1.5 Where the `inst_enemy` list goes

```
$ grep CSRExploreMirageInfo analysis/native-evidence.tsv | grep ENEMY_INFO
_ZN28CSRPopUpExploreMirageConfirm16SetRightDeckInfoERKNSt6__ndk114listINS0_10shared_ptrIN20CSRExploreMirageInfo10ENEMY_INFOEEENS0_9allocatorIS5_EEEE
_ZN28CSRPopUpExploreMirageConfirm18GetCardCombatPointENSt6__ndk110shared_ptrIKN20CSRExploreMirageInfo10ENEMY_INFOEEE
_ZNSt6__ndk120__shared_ptr_emplaceIN20CSRExploreMirageInfo10ENEMY_INFOENS_9allocatorIS2_EEE16__on_zero_sharedEv
```

The consumer is **`CSRPopUpExploreMirageConfirm::SetRightDeckInfo`** — the
"right-hand deck" panel of the **Mirage confirm popup** — and
`GetCardCombatPoint` computes a power number for it. This is a pre-battle
*preview*, not the battle itself.

---

## 2. Why it is not the expedition's carrier — three independent arguments

### 2.1 Timing: it is a lobby-boot call, not a battle call

From the current `server-ts/logs/server.stdout.log` (the run report-009
analysed plus one more), `/mirage/GetInfo` appears **once per session**, inside
the `/lobby/Enter` bootstrap batch, together with the ~45 `/reference/*`
reference-table pulls:

```
... /lobby/Enter
... /relation/GetTargetUserInfo
... /lobby/V2_GetSupplyInst
... /reference/GetCard
... /mirage/GetInfo            <-- here
... /reference/GetTargetStageMonster   (only after a node tap)
... /mission/Start
<end>
```

`analysis/testing/report-009.md` §3 is explicit: **after `/mission/Start` the
client issues no further requests at all** — it aborts inside `MakeCamp`. So
`/mirage/GetInfo` was already answered long before the crash and is not
consulted while the enemy camp is being built.

### 2.2 Call graph: the crash chain has no Mirage symbol in it

report-009 §2 gives the `BLUSTONE_ARM` stack candidates (third consecutive
identical run, `signal=11 code=1 fault=0x10`, PC `+0x8643bb`):

```
CSRUserDB::GetCurStageID()
  -> CSRGameActor::OnInit()
    -> CSRGameBase::MakeCamp(const std::list<ACTOR_INFO>&, TEAM_DIR, CMHashID const&)
      -> CSRGameBase::MakeActor(const ACTOR_INFO&, unsigned, unsigned char)
        -> CSRGameActorMob::MakeBackEndActor(const ACTOR_INFO&, unsigned)
          -> CSRGameMob::INFO::INFO(const CSRGameMob::INFO&)   <-- crash
```

Not one of those is a `CSRExploreMirage*` frame. The expedition camp is built
from `CSRMStage` / `CSRSyncMStage` / `CSRGameMob` state, fed by
`/reference/GetStageMonster` → `CSRGameMob::AddStageMonster`.

### 2.3 It is a separate game mode with its own whole subsystem

`analysis/native-evidence.tsv` contains a **complete, self-contained** Mirage
mode that has nothing to do with the expedition map:

```
CSRExploreMirage                    (the scene)
CSRExploreMirageInfo                (the model / server sync)
CSRExploreMirageDeckHandler         (its own deck handler)
CSRExploreMirageStairDraw           (0x0093a600 Init(int, REWARD_TYPE))
CSRSceneExploreMirageInfo
CSRPopUpExploreMirage               (0x00bf9948 CreateStair(int, REWARD_TYPE))
CSRPopUpExploreMirageConfirm / RetryConfirm / RetryInfo
CSRSceneTutorialMFishing*  ... (unrelated siblings)
```

and, on the wire, a whole route family the expedition never touches:
`RegisterDeck`, `End`, `NextFloor`, `Reward`, `HealHunter`, `Friend`.

The expedition map, by contrast, is
`CSRSceneMStageMap` / `CSRMStageDeckHandler` / `CSRSyncMStage` /
`CSRGameStage::SetStage`.

`inst_enemy` is the opponent's deck in a **floor-based roguelike with stairs and
a registered deck**. It is not the expedition's stage wave.

---

## 3. The honest residual: what I could NOT rule out

Two things keep this at "not the carrier" rather than "ruled out":

1. **`CSRExploreMirage::MakeStageInst` exists** at `0x00925798`, and `SetRefID`
   is called from `0x00926958` inside it (`analysis/ghidra-setrefid-callers.txt`
   line 8, `from 0x925958 MakeStageInst`). So the Mirage mode *does* build
   battle actors and *does* call `SetRefID`. If some code path let a Mirage
   enemy list reach `MakeCamp`, that would change the answer.
2. The `ARITY-5` question (`analysis/research/ORCHESTRATOR-arity-constraint.md`)
   is still open, and its §6 lists `/mirage/GetInfo` as "the standing
   candidate" purely on the strength of the name.

Neither survives the timing argument in §2.1 though: the response is fetched at
boot and never re-fetched at battle time, so it cannot be what fills a structure
that is built *after* `/mission/Start`.

---

## 4. Why I did not implement a shape

The recovered facts give me the **element** shape (§1.3) and the **set of
sub-objects** (§1.2). What I do **not** have is the **container keys** — which
JSON key each `Parse_*` is handed. `inst_enemy` is a *request* key; the
response key could be `inst_enemy`, `enemy`, or something else, and
`Parse_InstEnemy` is reached from `ParseRewardInfo` (0x0092cb5c →
`0x0092dff4, see analysis/ghidra-instenemy-callers.txt), so it is nested one or
two levels down and the nesting is unknown.

Filling in nine containers from the parser *names* would be inventing the
container layer while claiming the element layer is recovered. Per `AGENTS.md`
§15 that is exactly the thing not to do, and per §6 a wrong shape crashes the
client where a mock does not. **`/mirage/GetInfo` stays on the generic mock.**

---

## 5. Precise spec for the Ghidra agent

Everything below is a single decompile target. Start with **5.1** — it is the
whole answer.

### 5.1 The `/mirage/GetInfo` response dispatcher  ← the one that matters

Locate the `operator()` body of the closure whose RTTI is at **`0x01debadf`**
(`_ZZN20CSRExploreMirageInfo11RequestInfoEhhi...3$_0vE`). Its enclosing thunk
type is at `0x01deb939`; the `PVHTTP::TASK_READY<...>` instantiations are at
`0x01debc a9` and `0x01debe50`.

That body is the `/mirage/GetInfo` response handler. **Read, in order:**

- which JSON node (or nodes) it hands to each of
  `Parse_Entry` (0x00933aec), `Parse_InstBase` (0x00933d80),
  `ParseStairInfo` (0x009343b4), `ParseHeroInfo` (0x009347f8),
  `ParseFriendInfo` (0x00934c00), `ParseDeckInfo` (0x0092c428),
  `ParseRewardInfo` (0x0092cb5c), `Parse_HealHunter` (0x0092c8e0),
  `Parse_End` (0x0092c64c) — i.e. the literal key used in each
  `basic_json::operator[](json, const char*)` call preceding the call.
  For every one of these the answer is a **single string literal**; run them
  through `analysis/ghidra-scripts/ResolvePcRelativeStrings.java`, which will
  pick them up in one pass if you point it at the function.
- whether it reads `ret_data` itself first (compare with
  `CSRSyncMStage::ReqTargetStageMonsterCB`, `analysis/native-target-stage-cb.txt`,
  which reads the whole envelope) or is handed an already-extracted sub-node.

That single decompile yields the complete container layer. Everything below is
corroboration.

### 5.2 `Parse_InstEnemy` call site

Decompile **`ParseRewardInfo`** (0x0092cb5c) and find the call to
`Parse_InstEnemy` (0x0092dff4). Report the literal key used as the argument.
This tells us whether `inst_enemy` sits at `ret_data.<key>.inst_enemy[]` or one
level deeper. `analysis/ghidra-instenemy-callers.txt` already lists the two
call sites (`0x92cdc8` inside `ParseRewardInfo`, and `0x935c50`), so the work is
one function.

Also confirm from `Parse_InstEnemy` whether the `inst_enemy` value is iterated
**directly** (bare array) or via `iteration_proxy_value::key()` (object). The
element keys are known; only the container kind is not. The `"n"` key read at
the very top (`0x0092e10e`, before `ref_id`) suggests a positional field, which
slightly favours a bare array, but that is an inference, not evidence.

### 5.3 `Parse_InstBase` (0x00933d80)

The player's own Mirage deck base. Its key list should be identical to
`Parse_InstEnemy`'s (same record type: `n`/`ref_id`/`rank`/`rank_up_cnt`/
`overcome_cnt`/`exp`/`skill_1_level..5_level`). If it is, we can populate
`inst_base` and `inst_enemy` from the same generator, which is what the replica
needs. Confirm, do not assume — the two functions are 0x1400 bytes apart and
nothing forces them to agree.

### 5.4 The one question that would change the verdict

`CSRExploreMirage::MakeStageInst` is at **`0x00925798`** and calls
`CSRCard::SetRefID` at **`0x00926958`**. Find its callers. If any caller is
reachable from `CSRGameBase::MakeCamp` (0x009d39e0) or from
`CSRGameActor::OnInit`, then the Mirage enemy list *is* on the expedition camp
path and §0 is wrong. If its only callers are inside `CSRExploreMirage` /
`CSRSceneExploreMirageInfo` / `CSRExploreMirageDeckHandler`, the verdict stands.

This is a 5-minute `callers` query in the existing caller-listing script
(`analysis/ghidra-setrefid-callers.txt` and
`analysis/ghidra-instenemy-callers.txt` were produced that way).

### 5.5 Bonus, and it is the actual blocker

While in `CSRSyncMStage`, the arity-5 question is one function away:

- `CSRSyncMStage::RequestMonsterRef(const std::string&, function<void()>)`
  — `0x00b46218` (thunk `0x002246ea`). **This builds the `list<string>` that is
  serialised into `/reference/GetMonster`'s `list` field.**
- `CSRSyncMStage::GetMonster(const list<std::string>&, function<void(int)>)`
  — `0x00b44424` (thunk `0x002822bd`); its success continuation is the closure
  at `0x01e24ee9` / `0x01e250c1`.
- `CSRGameBase::RequestMonsterRef()` / `ReqMonsterRefCB()` — `0x009c9a2c` /
  `0x009c9ae4`.
- `CSRSceneStageConfirm::RequestMonsterRef()` — `0x00e7cf74`
  (**the Prepare-for-Battle screen**, i.e. the exact call site in the failing
  run).

The five empty strings are produced in one of these. If they come from a
fixed-size native array of 5 that nothing writes, the defect is upstream of
every route and the mock triage is the wrong lever entirely. That question is
worth more than all 44 remaining mocks put together.

---

## 6. Server-side state

- `server-ts/src/game-routes.ts`: **`/mirage/GetInfo` is unchanged and still
  served by the generic mock fallback.** No invented shape was added.
- When a shape *is* recovered, implement it in `game-routes.ts` and mark the
  block `[RECOVERED]` with the native function and address, exactly like the
  `GetTargetStageMonster` block. `bootstrap.ts` is where the Mirage fixture
  belongs.