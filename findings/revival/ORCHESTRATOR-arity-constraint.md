# ORCHESTRATOR FINDING — the "5" is a native constant, not a count of anything we send

Written by the orchestrator, 2026-10-02. **[INFERRED from measured invariants]** — but the
measurements underneath it are hard, and the conclusion is falsifiable. This reframes the
search and should be read before proposing another fixture change.

---

## 1. The invariant

`GET /reference/GetMonster {"list":"[\"\",\"\",\"\",\"\",\"\"]","pvid":"1000001"}` has been
observed **byte-identical in every single run**, and `SRCard.cpp(731)` has been asserted
**exactly 5 times** in every single run. Across all of it, the party size, the wave identity,
and the profile contents were varied:

| Run | What was varied | `GetMonster list` | `731` count |
|---|---|---|---|
| report-001 | baseline, party of 1 | 5 empty | 5 |
| report-002 | `BLUSTONE_PARTY_SIZE=5`, **4 filled slots**, Ally 50→200 | 5 empty | **5** |
| report-003 | party of 4 confirmed on screen, no empty `+` | 5 empty | **5** |
| report-004 | — | 5 empty | 5 |
| report-006 | — | 5 empty | 5 |
| report-008 | wave `_id` → `N003_M001` | **byte-identical** | 5 |
| report-009 | profile `ref_id_1..4` + `_leader` = `001` | **byte-identical** | 5 |

**The count never moved. Not once, across seven runs and every fixture variation tried.**

## 2. The arithmetic contradiction

The replica sends **exactly one wave** for the stage in question. From
`server-ts/src/bootstrap.ts:241-249`, for `N003`:

```ts
["N001", "N002", "N003"].map((id) => [id, {
  wave_list: [{ _id: `${id}_M001`, ref_id: "001", group: 1, next_spawn_ms: 0, show_thumbnail: 1 }],
}])
```

`wave_list.length === 1`, and its single `ref_id` is the non-empty string `"001"`.

Yet the client asks for **five** monster ids, and **all five are the empty string**.

Five requested ids cannot come from a one-element list. And the one id we *do* send (`"001"`)
does not appear in the request. So:

> **The array the client reads to build those five ids is not `wave_list`, and is not
> populated by anything the replica currently sends.**

The only way to emit five empty strings is a **fixed-size native array of 5 that the
replica never fills**.

## 3. Why this explains the whole failed campaign

This is the load-bearing consequence. Every experiment run so far has varied data *the client
does not read on this path*:

- filling deck slots → no change (report-002/003)
- splitting wave `_id` vs `ref_id` → byte-identical (report-008)
- putting the profile's `ref_id_1..4` on the wire → byte-identical (report-009)
- 180 stage identifiers across 10 naming schemes → no change
- populating the stage's `item` array → temporarily changed `GetMonsterData`, reverted

None of these were wrong. They were **structurally incapable of moving the number**, because
the number is a constant baked into the client. The repeated "no change" results are not five
independent failures to find the right key — they are the *expected* result of perturbing a
variable the equation does not contain. That is why three separate agents each converged on a
plausible carrier and each was wrong.

## 4. The corroborating oddity

The Prepare screen reads **`Opponent Teammates 1`** in red on every single prep screenshot
(reports 002, 003, 004), while the client simultaneously requests **five** monster ids. So the
client's own UI believes the enemy team is one unit, and its data layer is asking for five.
That inconsistency is itself a symptom: the UI reads a *resolved* enemy count from one place,
and the five-slot read at `MakeCamp` time is coming from somewhere that resolved to nothing.

Also note the crash PC sits in
`std::__ndk1::__tree<SRSKILL_INFO>::__emplace_hint_unique_key_args<...>::~__tree_iterator()`
with `fault=0x10` — a null-ish dereference at offset `+0x10` while emplacing into a
`CSRGameMob::INFO` skill tree during `CSRGameMob::INFO::INFO(const&)`'s copy constructor. An
absent skill map is consistent with monsters that were never really resolved.

## 5. What this predicts, and how to falsify it

**Prediction:** the five ids are read from a native structure sized 5 (a formation/party
array) that is filled by a route currently served as a **mock or a stub**, or by a field of a
route we shape but omit. Nothing in
`/reference/GetStageMonster`, `/reference/GetMonster`, `/lobby/GetCardInven`,
`/lobby/Enter` or `/relation/GetTargetUserInfo` populates it.

**Falsifiers — any of these kills the conclusion:**
1. A run in which `GetMonster list` is **not** exactly five empties. That has not happened in
   seven runs and would mean the array *is* data-driven after all.
2. Native evidence that the five ids are read out of `CSRGameStage`'s stage-monster table
   **after** a successful `AddStageMonster` — in which case the real defect is upstream
   (`AddStageMonster` is not being reached or is storing nothing), not a missing route.
3. A decompile showing the array is a hard-coded literal of five empty `std::string`s. Unlikely,
   but it would mean the enemy team is meant to come from somewhere we have not found at all,
   and the route inventory is incomplete.

## 6. The two questions this hands to native analysis

1. **Where does the size-5 array live, and what writes into it?** Its address, its type, and
   every function that stores into it. This is a much narrower question than "who builds the
   enemy list" and it is answerable by finding the array and working back from its writers,
   rather than forward from `MakeCamp`.
2. **Which route's response is supposed to fill it?** The request/response key inventory for
   whatever that turns out to be. `/mirage/GetInfo` — which the client calls with `inst_enemy`,
   `inst_base`, `ref_hero`, `ref_stair_list` and which the replica answers with
   `{"mock":true,...}` — is the standing candidate, and it is the one route in the inventory
   whose *name* matches the shape of what is missing. It is a candidate, **not** a conclusion;
   it has not been tested, and the two prior "obvious" candidates were both wrong.

## 7. Immediate consequence for how the team should work

- **Stop varying the data we already send.** `wave_list`, `_id`, `ref_id`, deck slots,
  `BLUSTONE_PARTY_SIZE` and the profile keys are all proven not to be in the equation.
- **Find the writer of the size-5 array in native code.** That is the single blocking question.
- **A cheap, decisive experiment is available:** make `/mirage/GetInfo` a real route with a
  populated `inst_enemy` of five entries. It costs one fixture, it is the one correlation
  nobody has tested, and — critically — if the theory in §3 is right it is the first
  intervention in five failed rounds that *could* move the number. If it does not move, the
  five-empty-strings invariant survives another falsification attempt and §5(2) becomes the
  priority.
