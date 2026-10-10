# ROOT CAUSE v4 (final) — `wave_list` is `vector<vector<monster>>`, we sent a flat vector

Written by the orchestrator, 2026-10-02. **This is the end of the chain.** It supersedes
`ROOT-CAUSE-v3-empty-waves.md` §3/§4 and corrects my own `_id` claim.

**Status: [RECOVERED] from the instruction listing, verified by me against the raw bytes.**

---

## 1. The defect, in one sentence

`CSRGameMob::AddStageMonster` (0xa0d194) reads **`wave_list` as an array of arrays** — one
`vector<STAGE_MONSTER>` per outer element — but the replica sent a **flat array of monsters**.
The inner loop therefore iterated a *monster object's five members* and called
`operator[]("N002_M001", "ref_id")` on each, which nlohmann answers with `type_error.305`.
`AddStageMonster` has **no exception handler**, so the unwind skips both the
`STAGE_MONSTER_LINK` emplace and the wave push, **`CSRGameMob`'s link map is never written at
all**, and the downstream `GetStageMonsterLinkData` lookup misses and returns its unwritten
fallback vectors. `CSRMStage::MakeStageInst` then hits `beq.w 0x00b34e88`, the `"enemy"` key is
never created, and the unconditional store at `0xb3506a` faults at `0xb3507a` with
`str r0,[r1,#0x4c]` and `r1 == 0`.

## 2. The evidence — the instruction listing, not the decompile

From `analysis/ghidra-hasmonster-08-asm-addstagemonster-emplace.txt` (Ghidra's decompiler
flattens the nested iterators and hides the structure; the raw instructions do not):

| Address | Instruction | Meaning |
|---|---|---|
| `0xa0d1ce` | `bl 0x007930f8` | `operator[]("wave_list")` — the **outer** array |
| `0xa0d266` | `bl 0x0072aff0` | outer iterator `deref` |
| `0xa0d2d8` | (loop head) | **inner** iterator over the outer element |
| `0xa0d304` | `bl 0x007930f8` | `operator[]("ref_id")` on the *inner* element |
| `0xa0d34a` | `bl 0x007930f8` | `operator[]("group")` |
| `0xa0d398` | `bl 0x007930f8` | `operator[]("next_spawn_ms")` |
| `0xa0d480` | `bl 0x00a0e4ac` | push one `vector<STAGE_MONSTER>` — **per outer element** |
| `0xa0d512` | `bl 0x007930f8` | `operator[]("show_thumbnail")` at record level |
| `0xa0d672-690` | `ldr/add` + `bl 0x00a0e618` | `emplace` keyed from `param_1` (the top-level key) |

The `bl 0x00a0e4ac` at `0xa0d480` **inside the outer loop** is the decisive one: it proves the
waves value is `vector<vector<STAGE_MONSTER>>`.

## 3. The retraction — `_id` is NOT read, and my tool invented it

I claimed in `ROOT-CAUSE-v2` and `ROOT-CAUSE-v3` that `AddStageMonster` reads both `_id` and
`wave_list` from one literal slot via two addends. **That was a phantom produced by my own
`tools/resolve-literals-offline.py`.** I verified it myself:

```
bytes at 0xa0d1b0:  d05b 4608
  bits[15:11] = 0b10, S = 0  ->  32-bit Thumb-2 BL (a CALL), not a literal load
bytes at 0xa0d1b4:  4689      ->  add r1,sp,#8   (NOT add <Rn>,pc)
```

Both halves of the pairing were wrong. The corroborating count: the function has **exactly
five** `bl operator[]` sites (`0xa0d1ce`, `0xa0d304`, `0xa0d34a`, `0xa0d398`, `0xa0d512`). A
sixth would have meant a sixth key. There is none.

**`wave_list` is the only wave-array key. `_id` is not read at all.** So the `_id` we have been
publishing is inert, and the two `_id`-array variants in the fixture were hedging against my
own bug.

I have fixed the resolver: pairing now requires the `ldr` to be the **immediately preceding**
instruction, and 32-bit `BL`/`BLX` opcodes are rejected outright. Verified after the fix —
the phantom `_id` row is gone, the real `wave_list` row remains, and `--from-dump` still
re-resolves the known-good `ghidra-wave-keys.txt` 7/7 from disk.

This is the **third** defect in this one tool, and all three produced a wrong *string key*
rather than a missed literal. The `wave_list` case (a too-narrow window) was a false negative;
the `_id` case (a too-wide window) was a false positive. Documented in-source so neither
recurs.

## 4. Second defect — the map key must ALSO be the stage id

`AddStageMonster` keys the link map from `param_1` — the **top-level `ret_data` key**
(`0xa0d672-690`, pair key copy-built from `param_1`). But `MakeStageInst` reads that map with
`GetStageMonsterLinkData(this+0x220)`, and `this+0x220` is the **stage id** (traced
`0xb34026 → 0xb34198 → 0xb34686 → 0xb34b16`).

On a miss, `GetStageMonsterLinkData` (0xa0cf38) substitutes fallback vectors from
`CSRGameMob+0x18`/`+0x24`, **which have no writer**.

So `BLUSTONE_STAGE_MONSTER_KEY=monster_id` — the shipped default — was structurally
**unfindable** by the consumer. That is why the client never resolved anything while we
believed it was resolving. The response must carry **both** keys: the stage id *and* the
monster id. Both agents independently reached this, from the native side and from the wire
capture respectively, which is the strongest corroboration in this whole investigation.

## 5. Why this explains every failed round

| Round | What we changed | Why it could not work |
|---|---|---|
| 1-3 | party size, deck slots | wrong structure entirely |
| 4-6 | wave `_id`/`ref_id` split | `ref_id` is read on the **inner** element of a nested array we never sent |
| 7 | `wave_list` **created** | right key, wrong **shape** — flat instead of nested |
| 8 | map key → monster id | key not findable by the consumer |
| 9 | `show_thumbnail` array | correct but causally inert (device-verified) |

Every intervention was individually reasonable and each was addressing a defect that the
previous one had masked. The failure mode was never a wrong theory about *a field* — it was
that no round ever read the **structure** (`vector<vector<>>`) before changing contents.

## 6. The fix — one structural change

```json
{
  "M001": { ... },                       // key = monster id  (already shipped)
  "N003": {                              // key = stage id    (NEW, required)
    "wave_list": [
      [ { "ref_id": "001", "group": 1, "next_spawn_ms": 0, "show_thumbnail": ["M001"] } ]
    ],
    "show_thumbnail": ["M001"]
  }
}
```

Shipped as `BLUSTONE_WAVE_SHAPE=nested` (default) with `flat` retained, and
`BLUSTONE_STAGE_MONSTER_KEY=both` (default). The regression guard was proven to **fail** on all
four control legs.

## 7. What is still open — and it is a *different* defect

The crash site is `this+0x264` = the **enemy** camp map. But the analysis found a **second,
sibling** camp map at **`this+0x250`**, which is the **player** deck, and that is where the five
`SetRefID` assertions live. Fixing the enemy camp should clear the crash at `0xb3507a`; it will
**not** clear the `SRCard.cpp(731)` assertions, which are a separate defect in the player camp
built from `CSRUserDB::GetDeck()`.

Also unresolved, and stated as such:
- `ref_id` is a **card** id (`"001"`) while `CSRGameMob::GetMonsterData` wants a **monster**
  id. Still [FIXTURE], still the known `AGENTS.md` §11 conflict. The recovered pack has 21+
  real monsters and ~150 real cards, so this is fixable with real content — but not guessed.
- Whether the nested array's inner elements need `_id` at all (it is not read) — the fixture
  currently includes it; harmless but should be annotated.

## 8. Honest summary of confidence

| Claim | Status |
|---|---|
| `wave_list` is `vector<vector<monster>>` | **Recovered** — vector push inside the outer loop |
| Flat shape → `type_error.305` → unwind → no emplace | **Recovered** — no handler in the function |
| The link map is keyed by the top-level `ret_data` key | **Recovered** |
| The consumer looks it up by **stage id** | **Recovered** |
| Empty waves → `beq.w` skip → null store at `0xb3507a` | **Recovered** (v3, derived from `std::list`'s constructor) |
| `_id` is not read | **Recovered + verified by me** from the opcode bytes and the five-site count |
| The fix opens the battle scene | **NOT YET TESTED** — this is the first structural change in eleven rounds |

The battle scene has still never opened. But every link from the server response to the
faulting instruction is now accounted for, and the one thing that was never verified in eleven
rounds — the **shape** — is finally the thing being changed.