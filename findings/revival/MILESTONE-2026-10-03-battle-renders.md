# MILESTONE 2026-10-03 — THE BATTLE SCENE RENDERS. Mission objective MET.

**`analysis/r016-02-BATTLE-SCENE-RENDERED.png`** — verified by eye, not by assertion:
a Snowfield expedition battle. Parallax backdrop (mountains, stone wall, bunting, water)
drawn from `ST099.jet`; player card `001` — a blonde rifleman — against monster `M001`, a
penguin; player HP `100/100`, enemy HP `872` with a green bar, turn dial bottom-left, battle
timer bottom-right, AP counters top-left, exit button top-right, party lock icons on both
sides.

Confirmed on **two independent launches**, and the battle **runs**: turn counter `0→1`, enemy
HP `872→773`, AP `100→89`, and the backdrop visibly scrolls between frames. A later leg shows
the player firing (muzzle flash, damage `1`).

This closes the objective stated in `AGENTS.md` §1: *"the client boots, enters the village,
opens the expedition map, starts a stage, runs the battle, and completes it — all against a
locally reconstructed server."* Everything except **completes it** now works.

---

## 1. The last blocker, and it was a namespace confusion

The client built the scene and died on the **first presented frame**:

```
fault=0x1  PC ELF 0x9aebd7  CSRGameScrollBGDraw::OnUpdate  r0=1
```

`OnUpdate` iterates a `vector<shared_ptr<CMImageNode>>` that was empty, because
`CSRGameScrollBGDraw::Load` attaches a child **only in the `else` of
`if (CMImageNode::LoadAnim(...) == 0)`** and all 30 layers failed.

The 30 names were `_A0.._A9`, `_D0.._D9`, `_E0.._E9` — **prefixless**. They are built as
`CMFormat("%s_%s", ENV_INFO.name, CSRStaticData.<field>)`.

`CSRStaticData::LoadEnv()` had **succeeded** — no `ENVIRONMENTS` / `Load failed` / `CSV` errors
in 22.8 MB of logcat against 495 other `[ERR]` lines. The table was in memory. But
`CSRGameBase::InitBackground` (`0x9cbe8c`) reads `stage+0x70` — `res_prefix` — and passes it as
the map key, and **`find()`'s `end()` is never tested**. A miss reads the tree's end-node, the
`%s` formats as `""`, and every layer name loses its prefix.

**The replica was sending `res_prefix: "ST001"` — an asset prefix — into a table keyed by
environment id.** Same string, two namespaces. `SetStage`'s recovered 22-key list contains no
environment field at all, so `res_prefix` *is* the selector; `ST001` survives only in `thumb`
and the area's `resource_id`, which are genuinely art names.

Publishing `res_prefix: "99"` — row 99 of the recovered `environments.csv`, the only row whose
name is the generic battle word and the only one with positive scroll speeds on two of five
depth bands — made the lookup hit. Layers became `STI099_A01/A1/B01/B1/C01/C1/D01/D1/E01/E1`
plus `STI099B`, all 29 prefixless names disappeared, and the crash cleared 0-of-2.

## 2. A falsified risk, and a methodology trap worth recording

`environments-recovery.md` §7 warned, honestly, that a PKGI1 **hit** was unproven and that the
fix "may move the crash rather than remove it". **A hit is now proven.** Its §3.2 was also wrong:
the suffix set is **five** (`A`–`E`), not three. Strike `STATUS-2026-10-03.md` §2 rather than
amend it.

Separately, the tester disclosed a near-miss worth keeping: its logcat reader started before the
new launch, so the ring still held **all of report-015**. Its first counter pass read *"30
misses, fault=0x1, zero change"* — a **false negative that would have reported total failure**.
Every count in report-016 is sliced on launch markers. This is the third time in four days that
a correct measurement supported a wrong inference (`show_thumbnail`'s type, the withdrawn
`LoadAnim2` lead, and now this). **Slice every log on a launch marker.**

## 3. What is settled, and how it was settled

| Fact | How |
|---|---|
| `res_prefix` is the environment selector | `SetStage`'s recovered 22-key list has no environment field; `InitBackground` reads `stage+0x70` |
| Valid environment keys | the 50 `#ID` rows of the recovered `environments.csv` |
| `end()` is untested on that lookup | recovered from the decompile; the faulting `ldr r1,[r0]` has no guard |
| `99` is the battle backdrop | asserted against the CSV in `tests/smoke.ts`, not asserted in a comment |
| `/mission/Start` is finally fresh | `BLUSTONE_MISSION_START_IDEMPOTENCY_SECONDS=0`; unique `battle_id`; `ap` 44→43→42 |

**The battle is 100% client-side.** The battle window is exactly **three** dispatches
(`/relation/GetTargetUserInfo`, `/reference/GetTargetStageMonster`, `/mission/Start`) and then
**zero server traffic** for the whole battle. The client simulates combat itself; the server's
job is only to describe the stage, the waves and the monsters correctly — which it now does.

## 4. Also fixed along the way

- **`/mission/Start` was a one-way latch**, not an idempotency window: it tested only
  `state === "active"`, and the only thing that ever cleared that was `/mission/Complete` —
  which the client had never reached. It replayed r010's `battle_id` for **six** reports.
  Now windowed (default 30 s; `0` = always fresh; `forever` = old behaviour, kept reproducible).
- **`battle_id` was not unique** (`local-${pvid}-${Date.now()}`, colliding within a millisecond).
- **`/mission/Complete` re-paid 10 gold** for an already-cleared stage whenever any battle was
  active, contradicting its own documented contract.
- **`environments.csv` was recovered** from `LEVELING.jet` chunk 5 in the base APK — it was
  never missing, contrary to my own earlier note.

## 5. Corrections I owe the record

Five of my own claims were wrong across this work, each caught by checking bytes or the wire
rather than a symbol name:

1. "`wave_list` has zero code references" — a false negative from my own resolver's pairing
   window.
2. "`_id` is also read" — a false positive; the bytes at `0xa0d1b0` are a 32-bit `BL`, and the
   function has exactly **five** `operator[]` sites.
3. "`show_thumbnail`'s type causes the empty ids" — falsified by a device control leg.
4. "The crash is in the episode scene" — an ELF/Ghidra `+0x10000` confusion; and I dropped a hex
   digit once, writing Ghidra `0xaaebd7` for `0x9bebd7`.
5. "`environments.csv` does not exist" — it does; the cause was an unchecked `find()` miss.

`tools/resolve-literals-offline.py` alone had three defects, all producing a wrong **string
key** — the most dangerous failure mode here, since it makes the server answer with a field the
client never asked for. It is now hardened and its known-good regression dump still resolves
7/7 from disk.

## 6. What remains

- **`/mission/Complete` is still unreachable.** The battle does not end on its own (zero
  requests, ≥298 s observed). **This is the last piece of the mission loop** — until a battle
  can be completed and progression applied, the loop is not closed. A live idle client is
  available at the command UI, which costs **0 AP** per attempt versus 1 AP per fresh start.
- The five `SRCard.cpp(731)` assertions in the **player** camp map (`this+0x250`) remain masked
  and unexplained — a genuinely separate defect.
- `[ERR] [RES] Can't find 'ST001' in ResMap.` fires 39.6 s **before** the battle, from
  `thumb`/`resource_id`, so the prep-screen thumbnail is a separate live gap.
- Combat is one card against one monster at level 1 — real content (21+ monsters, ~150 cards
  exist in the recovered pack) is still fixture.

## 7. Honesty

Real expedition gameplay now runs against the local replica: map, stage selection, battle
entry, rendered combat, running turn loop, animated parallax backdrop, live HP and AP.

It is **not** a faithful game. The battle is 1 card vs 1 level-1 monster; economy values are
provisional placeholders; the CDN serves 11 of the original packages; and no battle has yet
been *completed*. Document recovered-vs-fixture-vs-unknown as `AGENTS.md` §15 requires, and do
not let this milestone soften the standing gaps listed in §6.