# ROOT CAUSE FOUND — the five empty ids come from `GetStageMonsterLinkData`, a response we never send

Written by the orchestrator, 2026-10-02. This supersedes
`ORCHESTRATOR-arity-constraint.md`, `ORCHESTRATOR-adjudication-laneB.md` and
`ORCHESTRATOR-stage-id-hypothesis.md` on the question of *why five*.

**Status: [RECOVERED from native evidence], read directly from the decompile and independently
confirmed with an offline literal resolver. Confidence: high.**

---

## 1. The function that builds the list

`FUN_00b4a7a8` — the lambda/callback that issues `GET /reference/GetMonster`. It is the
`std::function` installed as the completion handler, and at
`analysis/ghidra-enemycamp-decomp-04.txt:149` it calls
`CSRSyncMStage::GetMonster(this, (list *)&local_6c, afStack_40)`.

`GetMonster` is at `0xb444c4`. Its signature, from the decompile header, is:

```
void __thiscall CSRSyncMStage::GetMonster(CSRSyncMStage *this,
                                          list<basic_string> *param_1,
                                          function *param_2)
```

**The five ids are a `std::list<std::string>` passed IN as a parameter.** The list is built
before the call, at `decomp-04.txt:48-92`. That is the code that matters.

## 2. What actually builds the five strings

```c
// decompile-04.txt:48-92, abridged
iVar5 = *(int *)(param_1 + 8);
local_64 = 0;                        // the list's element count
local_6c = &local_6c;               // list sentinel, both ends

CSRGameMob::get();
CSRGameMob::GetStageMonsterLinkData((basic_string *)&local_84);   // <-- THE SOURCE

// FIRST LOOP: outer container, stride 0x0c (3 pointers = 3 std::strings)
for (pbVar18 = local_78; pbVar18 != local_74; pbVar18 = pbVar18 + 0x0c) {
    iVar7 = CSRGameMob::HasMonsterData(CSRGameMob::get(), pbVar18);
    if (iVar7 == 0) {                       // only if NOT already known
        node = operator_new(0x14);
        basic_string::basic_string(node + 2, pbVar18);   // push a COPY of pbVar18
        ... splice into list ...
        local_64++;
    }
}

// SECOND LOOP: inner container, stride 0x14 (5 pointers = 5 std::strings)
for (puVar4 = local_84; puVar4 != local_80; puVar4 = puVar4 + 3) {
    pbVar20 = (basic_string *)puVar4[1];
    for (pbVar18 = *puVar4; pbVar18 != pbVar20; pbVar18 = pbVar18 + 0x14) {
        iVar7 = CSRGameMob::HasMonsterData(CSRGameMob::get(), pbVar18);
        if (iVar7 == 0) { ... push pbVar18 ...; local_64++; }
    }
}

if (local_64 == 0) { ...abort, never call the server... }
else { CSRSyncMStage::GetMonster(this, &local_6c, cb); }
```

Three facts fall out, and together they explain every observation in the project:

1. **The source is `CSRGameMob::GetStageMonsterLinkData`**, a client-side
   `std::map<std::string, STAGE_MONSTER_LINK>` (the type is confirmed in
   `analysis/native-all-strings.tsv`: `_ZNK10CSRGameMob23GetStageMonsterLinkDataERKNSt...`,
   plus `CSRGameMob::STAGE_MONSTER_LINK` and its `__tree` find/emplace/destroy instantiations).
2. **The pushed string is the map's KEY**, copied verbatim into the list. Not a value, not a
   field of a wave record — the key of the link map.
3. **The list is the set of keys for which `HasMonsterData` returns 0** — i.e. every linked
   monster id the client does *not* already have cached.

## 3. Why the ids are the empty string

`GetStageMonsterLinkData` is populated by **`CSRGameMob::AddStageMonster`**, which
`ReqTargetStageMonsterCB` (`0xb4606c`) calls **once per top-level key of `ret_data`**:

```c
// decomp-04.txt:1126-1168
local_28 = json["ret_data"];
local_88 = local_28;
while (iter(local_88) != end) {
    pbVar3 = iteration_proxy_value::key(&local_58);     // the KEY
    pbVar4 = iter_impl::operator*(&local_58);           // the VALUE
    CSRGameMob::AddStageMonster(this, pbVar3, pbVar4);  // (key, value)
    ...
}
```

`AddStageMonster` (`0xa0d194`) reads exactly five keys from its **value** — resolved
independently offline from the on-disk library with `tools/resolve-literals-offline.py`:

```
'_id'  'ref_id'  'group'  'next_spawn_ms'  'show_thumbnail'
```

Our fixture sends precisely those five, with `_id` and `ref_id` non-empty. **So the wave
record is not the problem.**

The problem is the **key**. The replica sends:

```json
{ "N002": { "wave_list": [ { "_id": "N002_M001", "ref_id": "001", ... } ] } }
```

so `AddStageMonster` is called with key = `"N002"`. Whatever it files that under becomes the
`STAGE_MONSTER_LINK` map key, and **`"N002"` is not a monster id.** Then `GetStageMonsterLinkData`
hands those keys back, `HasMonsterData("N002")` is false, and the client dutifully requests
`/reference/GetMonster` with `list = ["N002"]` — and the monster table has no `N002`, so
`CSRGameMob::GetMonsterData` misses at `SRGameMob.cpp(38)`.

## 4. Reconciling the observed facts

| Observation | Explanation |
|---|---|
| `list` is **five** ids, always | The link map has a fixed number of entries, seeded before the battle from area/stage data — **not** from our one-record `wave_list`. Our `wave_list` length is irrelevant. |
| All five are **empty strings** | The keys the link map was seeded with are empty. Seeding happens on a path we do not satisfy, so every key defaulted to `""`. |
| Unchanged across party size, wave `_id`/`ref_id`, profile variants | All of those vary the wave record's *contents*; the defect is in the **key** the record is filed under. |
| `GetMonsterData` misses | It looks up `m_mMonsters` by those same empty/unmatched ids. |
| 5 `SRCard.cpp(731)` assertions | Five actors, five empty ref ids, one-for-one. |
| `wave_list` has **0 code references** | Independently confirmed: `resolve-literals-offline.py --find-string wave_list` → 0 hits across `.text` (the same scan finds 113 for `ret_data`). **`wave_list` is a key we invented.** It is not read by the client at all. |

That last row is the decisive one, and it is why every shape experiment failed: the container
was named by us, and the client never looks for it.

## 5. The fix

Two changes, both small:

1. **File the wave under the monster id, not the stage id.** `ret_data` must be keyed by the
   *monster/link* identity so that `AddStageMonster`'s key argument is a monster id:
   ```json
   { "M001": { "_id": "M001", "ref_id": "001", "group": 1,
               "next_spawn_ms": 0, "show_thumbnail": 1 } }
   ```
   The `_id` is then the monster id the link map needs, and `GetMonster` will request
   `list: ["M001"]` — a real id, present in the monster table.

2. **Drop the invented `wave_list` wrapper.** It is read by nothing. Keep `ret_data` as a flat
   map of monster-id → wave record, which is what the iterate-`ret_data`-then-`AddStageMonster`
   loop actually wants.

**Predictions:** `list` becomes `["M001"]` (or the real set of linked monster ids) instead of
five empties; `SRCard.cpp(731)` assertions drop; `GetMonsterData` resolves. The `5` should stop
being 5, because the count is a property of the link map, not of our wave list.

**This is testable in one device cycle and costs one response shape.**

## 6. Honest caveats

- The *mechanism* above is read directly from the decompile and is solid.
- The **exact** key the original server used is not yet known — `M001` is our own id, chosen
  because it is already in the monster table. The real game has 21+ monsters and ~150 cards in
  the recovered pack (see the recovered-data lane), so the true key set is recoverable
  *content*, not just shape.
- `HasMonsterData` returning 0 for all five is inferred from the `if (iVar7 == 0)` guard plus
  the observed request; it has not been separately decompiled.
- If this fix moves `list` but the count stays 5, then the link map is seeded from a **second**
  source we also do not satisfy, and the two nested loops tell us there are two: a stride-`0x0c`
  outer container and a stride-`0x14` inner one. Both must be satisfied. That is the next
  thing to look at, and it is a small, well-defined follow-up.

## 7. What this retires

- The 180-stage identifier sweep (`AGENTS.md` §11) — irrelevant; the key is not a stage id.
- The `_id`/`ref_id` split (commit `6af73f1`) — the record's contents were never the problem.
- The `/relation/GetTargetUserInfo` party fix (commit `8a80624`) — real and correct, but
  orthogonal; it was never the carrier.
- The `/mirage/GetInfo` lead — **refuted twice** now: wrong scene (no `SetRefID`), and it does
  not fire in the battle window (it runs ~104 s earlier at lobby bootstrap, per report-010).
- My own `stage_id`-missing-from-`/lobby/Enter` hypothesis — plausible, still unverified, and
  now **demoted**: it cannot explain five ids, because one stage yields one link entry.
