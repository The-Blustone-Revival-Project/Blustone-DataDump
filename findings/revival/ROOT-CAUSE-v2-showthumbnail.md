# ROOT CAUSE v2 — the five empty ids are `show_thumbnail[]` read as a scalar, not the map key

Supersedes §2.2/§3 of `ROOT-CAUSE-stagemonster-link.md`. Written 2026-10-02 after
`analysis/research/ghidra-enemy-actor-trace.md` (Ghidra lane) and
`analysis/testing/report-011.md` (device lane) landed.

**Status: [RECOVERED from native evidence] + [CONFIRMED on device]. This is the whole chain.**

---

## 1. The device result that proved the key half

Commit `5acb45e` keyed `ret_data` by monster id. Test `report-011`:

| | r010 baseline | fix (monster key) | **control** (`BLUSTONE_STAGE_MONSTER_KEY=stage_id`) |
|---|---|---|---|
| `GetMonster` `list` | 5 empties | **route never issued** | **5 empties, byte-identical** |
| `SRCard.cpp(731)` | 5 | **0** | 5 |
| `SRGameMob.cpp(38)` | 1 | **0** | 1 |
| total ASSERTION | 6 | **0** | 6 |
| crash | `fault=0x10`, PC `+0x8643bb` | `fault=0x4c`, PC `+0xb2507b` = **`CSRMStage::MakeStageInst()`** | `fault=0x10`, PC `+0x8643bb` |

The control is what makes this conclusive: one binary, one day, one env var, and the old
behaviour returns exactly. The seven-run invariant is broken, and the crash PC moved to a
**named game function** for the first time in this project. Total assertions went to **zero**,
and the client got far enough to build the battle HUD (registering `UI_IG_SK_*`, `UI_IG_NAV`,
`BGM_BATTLE1`, ~1000 sprites) before dying.

**So the key was half the bug. The other half is `show_thumbnail`.**

## 2. The real source of the five empty strings

`CSRGameMob::AddStageMonster` (`0xa0d194`) reads exactly five keys off the record — resolved
offline from the on-disk `.so`, agreeing byte-for-byte with Ghidra:

```
_id            ref_id      group      next_spawn_ms      show_thumbnail
```

and it uses them **two different ways**:

```c
/* part 1 -- the waves */
for (it = value["_id"].begin(); it != end; ++it) {   /* _id IS an array          */
    STAGE_MONSTER rec;                              /* per-element ref_id/group  */
    waves.push_back(rec);                           /*   /next_spawn_ms          */
}

/* part 2 -- the ID LIST, and this is the one that matters */
for (it2 = value["show_thumbnail"].begin(); it2 != end; ++it2) {   /* ARRAY of str */
    ids.push_back( from_json<std::string>(*it2) );
}
m_stageMonsterLink.emplace(key, STAGE_MONSTER_LINK{ waves, ids });
```

`STAGE_MONSTER_LINK::ids` — the second vector that `GetStageMonsterLinkData` returns — is
**built from `show_thumbnail`**, and `FUN_00b4a7a8` walks exactly that vector, pushing each
element into the `list` of `GET /reference/GetMonster` for every id where
`HasMonsterData` is false.

**The replica sends `"show_thumbnail": 1` — an integer.** Iterating a JSON number in nlohmann
yields nothing, and `from_json<std::string>` on a null/absent element yields `""`. That is the
five empty strings, and it is why they were invariant: **no key, party size, profile or wave-id
change could ever alter a number we were sending in the wrong JSON type.**

The empty-key theory in my first root-cause note was wrong about the mechanism, and the note
already said so in its caveats. The correct field to change is `show_thumbnail`, and the type
is as load-bearing as the name.

## 3. Corrected understanding of the map key

The Ghidra lane corrected me on one point and the correction matters:

- `ret_data`'s top-level key is the `emplace` key — **one entry per stage**, not per monster.
- The strings that become the request `list` are the elements of
  `ret_data[<stageKey>]["show_thumbnail"]`.

Both changes in commit `5acb45e` were still necessary: the key had to be something the client
could resolve, and the `""` ids had to stop being empty. But the key change alone suppressed
the *symptom* (no ids to request → `HasMonsterData` short-circuits → route never fires) without
supplying the data, which is why the crash moved rather than disappeared.

## 4. The fix

`/reference/GetStageMonster` and `/reference/GetTargetStageMonster` must send, per stage entry:

```json
{
  "N002": {
    "_id": [
      { "_id": "M001", "ref_id": "001", "group": 1,
        "next_spawn_ms": 0, "show_thumbnail": ["M001"] }
    ],
    "show_thumbnail": ["M001"]
  }
}
```

- `show_thumbnail` is a **top-level array of non-empty monster-id strings**. This is the field
  that feeds the request.
- `_id` is an array of wave objects (already correct in `5acb45e`).
- The monster ids must exist in the table published by `/reference/GetMonster`, or the fetch
  will miss and the camp will still be built from an `INFO` the client does not have.
- `/reference/GetMonster` must keep publishing under those exact ids.

## 5. Why the crash moved to `MakeStageInst` — and what to expect next

`report-011`'s best-supported reading (a) is now much stronger in light of §2. `FUN_00b4a7a8`
only calls `GetMonster` when the list is non-empty (`if (local_64 == 0) { ...abort... }`). With
the key fix, every id resolved as *already known*, the list came out empty, the fetch was
skipped, and the client proceeded into camp construction **without ever populating
`m_mMonsters`** — then dereferenced a null `INFO` at offset `+0x4c`. Zero assertions, new PC.

Once `show_thumbnail` yields real ids, `GetMonster` will actually fire, `m_mMonsters` will be
populated, and `MakeStageInst` should have the data it needs.

**The open risk, and it is a real one:** `CSRGameMob::HasMonsterData` is still only inferred
to be a lookup in `m_mMonsters`. If it is not, then nothing ever put `M001` in that map (the
route was never called in the fix run), and the "0 means not already known" inference in the
root-cause note is wrong. That is a cheap, decisive decompile and should be done before the
next device cycle if time allows.

## 6. Corrections to the record

For honesty (`AGENTS.md` §15), three claims of mine were wrong and are now retracted:

1. **"`wave_list` has zero code references; it is a key we invented."** Wrong. It is a real
   recovered key at `0x1d76bd5`, tail-merged 4 bytes after `_id`, read off the same load slot
   via a second `add`. The false negative came from a bug in *my own* resolver's pairing
   window, which I have fixed (`tools/resolve-literals-offline.py`) and documented in-source.
2. **"The pushed strings are the map key."** Wrong — they are `show_thumbnail[]`.
3. **"The key is what matters."** Half right. The key is necessary; the *type* of
   `show_thumbnail` is the actual source of the five empties.

I verified each of these against raw bytes before acting, which is the only reason the fix
moved. The project's standing rule — a wrong shape must be settled by the parser, never by
tuning the fixture — is what kept the device cycle cheap.
