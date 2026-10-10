# FALSIFIED — `show_thumbnail` is causally inert. And the crash symbol is probably wrong.

Written by the orchestrator, 2026-10-02, after `analysis/testing/report-012.md`.

**Commit `e1ff5f0` is a clean negative. Its central prediction is false. Retract it.**

---

## 1. The result

| | Leg 1b `show_thumbnail:["M001"]` | Leg 2 control `show_thumbnail:1` | r011 |
|---|---|---|---|
| `/reference/GetMonster` | **never issued** | **never issued** | never issued |
| `SRCard.cpp(731)` | 0 | **0** | 0 |
| `SRGameMob.cpp(38)` | 0 | **0** | 0 |
| total ASSERTION | 0 | **0** | 0 |
| crash | `fault=0x4c`, PC `+0xb2507b` | **`fault=0x4c`, PC `+0xb2507b`** | same |
| crash registers | `r0=0000000a r1=0 r2=0 r3=0x7f` | **`r0=0000000a r1=0 r2=0 r3=0x7f`** | same |
| battle window | 4 routes | same 4, same order | same 4 |
| `Opponent Teammates` | 1 | **1** | 1 |

**Array and integer are indistinguishable, down to the crash registers.** The control leg is
what makes this conclusive rather than merely disappointing: one binary, one env var, and the
old body reproduces the new body's behaviour exactly. `show_thumbnail`'s JSON type does not
cause anything.

This falsifies the specific claim in `ROOT-CAUSE-v2-showthumbnail.md` §5 and the VERDICT
prediction in `hasmonsterdata.md` that a non-empty array *forces* the request. It does **not**
falsify the underlying mechanism — `HasMonsterData` is a `m_mMonsters` lookup and `m_mMonsters`
has exactly one writer — because those were verified instruction-by-instruction and stand on
their own. What is falsified is the **causal chain from our response to the request**.

## 2. Why the model is now known to be incomplete

The logic that has to hold is short and airtight:

1. `FUN_00b4a7a8` pushes every id for which `HasMonsterData(id) == 0` (verified: `find` + `itr != end`).
2. `m_mMonsters` is written **only** by `ReqMonsterCB`, i.e. only by a `/reference/GetMonster` response (verified: single `__emplace_unique_key_args` instantiation, no `operator[]`, no `Clear`).
3. The route has never been requested → `m_mMonsters` is empty → `HasMonsterData` returns 0 for
   **every** id → the list must be non-empty → the route **must** fire.

The route does not fire. Therefore at least one of these is false, and the only one the device
can adjudicate is the **input**: the ids never reach `FUN_00b4a7a8` at all. That is, either

- `show_thumbnail` is not what builds `STAGE_MONSTER_LINK::ids`, or
- **`AddStageMonster` is never reached on our record**, so the map is never emplaced at all.

The second is the more likely of the two, and it is the more consequential. If
`ReqTargetStageMonsterCB` never calls `AddStageMonster` for our response, then the entire
`_id` / `show_thumbnail` / `wave_list` / key-shape line of work has been aimed at a function
that does not execute on this path — which would explain why *nothing* about that record has
ever moved a number, across five rounds and both key modes.

**This must be settled before any further fixture work.** It is a reachability question, not a
shape question, and it is answerable in one decompile.

## 3. A second thing I do not trust: the crash symbol

report-012 (and report-011) symbolise PC `+0xb2507b` as `CSRMStage::MakeStageInst`. **I have
now resolved this myself, and the symbolisation is wrong in a way that matters.**

There are **two different `MakeStageInst` functions** in this binary:

| Address | Owner | Verified by |
|---|---|---|
| `0xb23f60` | **`CSRSceneMEpisode::MakeStageInst`** | `_ZN16CSRSceneMEpisode13MakeStageInstEv` in `native-all-strings.tsv:0027c875` |
| `0xb33f84` | `CSRMStage::MakeStageInst` (the mission-map one) | the Ghidra lane's dump |

`0xb2507b` lies between `0xb23f60` and the next entry in that range, `ParseBegin` at
`0xb27d34`. **The crash is therefore genuinely inside `CSRSceneMEpisode::MakeStageInst`** —
the **episode** scene — not the expedition `CSRMStage` one the lane reported.

This is a scene mix-up, and it is the same class of error as the r009 chain: the
`BLUSTONE_ARM` candidate offsets are return/mid-function addresses, not entries, so
"nearest preceding symbol" silently attributes a crash to the wrong class whenever two
classes share a method name. `AGENTS.md` §11's `MakeStageInst` at `0x925798` is a **third**
one (`CSRExploreMirage::MakeStageInst`).

What I recovered from that function with `tools/resolve-literals-offline.py --function
0xb23f60:0xb27d34` (no Ghidra, ~40 literals):

```
'episode_stage'  'episode'  'monster'  'monster'
'Cannot convert Src(%s) to Dst(%s)'   'sic.h'
'009'                                   <-- the only literal in 0xb25000..0xb25600
'BGM_BATTLE1'  'FX_RESULT'
'common1'
'place_id'  'cast_dist'  'lure_id'      <-- FISHING request fields
'app_code' 'app_ver' 'market' 'pvid' 'otp'
```

Two consequences, both material:

1. **The `009` literal sits 0x4C3 bytes from the crash PC and is the only string in that
   window.** With `fault=0x4c` and `r0=0x0a`, an indexed access off a short container whose
   size comes from something like a `009`-keyed table is a plausible reading — but that is a
   **guess**, and it is labelled as one.
2. **`place_id` / `cast_dist` / `lure_id` are fishing fields, and `FX_RESULT` /
   `PopUpResultWin` / `OnFinish` are episode-result handlers.** So this function spans
   stage instantiation *and* a result popup, and the crash is in a function that is
   simultaneously reading episode/monster data and preparing a result UI. That is consistent
   with report-011/012 observing the battle HUD being built *before* the fault.

**The open question this creates:** why is an *episode* scene's `MakeStageInst` running at all
during an *expedition* mission? Either the client legitimately reuses it, or the replica is
driving the client into the wrong scene entirely — which would be a much more consequential
finding than any response-shape bug, and would explain why nothing in the stage-monster
response has ever moved a number.

## 4. What is actually established, and what is not

| Claim | Status |
|---|---|
| `ret_data` must be keyed so the client can resolve it | **CONFIRMED on device** (`5acb45e`): 6 assertions → 0, route stopped firing, control reproduces exactly |
| `HasMonsterData` = `m_mMonsters::find`, `0` = must fetch | **RECOVERED**, instruction-level, member named by the client's own assert literal |
| `m_mMonsters` has exactly one writer (`/reference/GetMonster` response) | **RECOVERED** |
| `show_thumbnail` is an array of strings | **TRUE but CAUSALLY INERT** — no observable effect either way |
| `show_thumbnail[]` builds the request `list` | **REFUTED on device** (this was the v2 claim) |
| `_id` must be an array | **UNKNOWN**, unobservable from outside |
| `wave_list` is a real recovered key | **RECOVERED** (corrected my earlier false negative) |
| PC `+0xb2507b` is `CSRMStage::MakeStageInst` | **WRONG** — it is `CSRSceneMEpisode::MakeStageInst` (`0xb23f60`); two classes share the method name |
| the crash is localised | **to a function, but the wrong scene** — an *episode* scene during an *expedition* mission |

## 5. Next step — reachability, not fixtures

Do **not** change another field of the stage-monster response. Three questions, in order:

1. **Is `AddStageMonster` reached at all on this path?** Instrument or verify the call from
   `ReqTargetStageMonsterCB` (0xb4606c) given our exact response body. If it is not reached,
   the shape work is aimed at dead code and must be abandoned.
2. **What actually fills the `list`?** `GetStageMonsterLinkData` (0xa0cf38) returns **two**
   vectors; the lane established `ids` comes from `show_thumbnail`. If the id vector is empty on
   this path, the *other* vector — the wave vector walked at stride `0x14` — is the real
   source, and its elements are wave records, not bare strings.
3. **What function actually contains PC `0xb2507b`?** Resolve the containing function by
   address range, not by nearest preceding symbol name. This is the current crash and it has
   never been correctly symbolised.

Questions 1 and 3 are each a single decompile. Neither requires a device cycle, and both are
prerequisites for the next one.

## 6. Note on the fix that did work

`5acb45e` stands: assertions 6 → 0 and the crash PC changed. That is real, reproducible, and
control-verified. It is not a cosmetic change — the client now reaches further into native
battle construction than it ever has, and builds the battle HUD before dying. Whatever replaces
this line of work should preserve that.
