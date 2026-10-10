# ORCHESTRATOR ADJUDICATION — lane B found the function, but its counting argument is refuted

Written by the orchestrator, 2026-10-02, after personally reading
`analysis/native-monster-stage.txt:5233-5322` and `analysis/ghidra-wave-keys.txt`.

**Verdict: keep B's structural finding, discard its arithmetic. No fixture change ships yet.**

---

## 1. What is CONFIRMED

`CSRGameMob::AddStageMonster` (0xa0d194) really does perform **two nested iterations before
reading a keyed string**. From the decompile:

```
5233  operator[](param_3, _DAT_00a0d4f4)          // first key lookup
5262  while( iter_impl::operator!=(&pcStack_44) )     // OUTER loop  (level 1)
5291      pcStack_8c = pcStack_9c;
5300      while( iter_impl::operator!=(&pcStack_8c) ) // INNER loop  (level 2)
5302          uVar13 = iter_impl::deref(&pcStack_8c);
5308          uVar13 = operator[](uVar13, _DAT_00a0d500)   // keyed read
5313          from_json<basic_string>(uVar14, &uStack_a8)   // -> std::string
```

So the access path is `param_3[K_a] -> iterate -> iterate -> [K_b] -> string`.
**B is right that the response needs a specific nesting shape, and that the current fixture's
shape has not been matched by anything the team has tried.**

B is also right that the current `GetCard` shape (array of records with a `base` sub-object) is
correct and should stop being re-litigated, and that `/mirage/GetInfo` is **refuted** as the
carrier — `CSRExploreMirage::MakeStageInst` has no `SetRefID` at all, so it is the wrong scene.
That is a genuinely useful elimination.

## 2. What is REFUTED — and it matters

B's explanation of *why there are exactly five* was: the client iterates the **five values of
our own wave record** and asks each for `ref_id`.

**That cannot be what happens.** The literal table (`analysis/ghidra-wave-keys.txt:4-8`, and
identically `ghidra-enemy-keys.txt`) resolves `AddStageMonster`'s keys:

```
_DAT_00a0d4f4 -> "_id"
_DAT_00a0d500 -> "ref_id"
_DAT_00a0d504 -> "group"
_DAT_00a0d508 -> "next_spawn_ms"
_DAT_00a0d874 -> "show_thumbnail"
```

The innermost read is `["ref_id"]` on the value produced by the inner loop. Our wave record is
`{_id:"N003_M001", ref_id:"001", group:1, next_spawn_ms:0, show_thumbnail:1}` — **`ref_id` is
the non-empty string `"001"`**.

So if the inner loop were really iterating our wave record's five values, the read would yield
`"001"`, and we would see `list:["001","","","",""]` or similar. We observe
`["","","","",""]` — **all five empty**. The innermost element is therefore *not* our wave
record.

**Conclusion: the client never reaches our wave record at all.** The five empty strings are
five iterations over something else entirely, and the count of five is still unexplained by any
wave shape we send.

The apparent elegance of "5 keys ↔ 5 empties ↔ 5 assertions" was a coincidence of two fives.
Acting on it would have been a sixth wrong fix.

## 3. What this does to the hypothesis ranking

This *raises* the priority of `ORCHESTRATOR-stage-id-hypothesis.md` rather than lowering it.
The two are compatible, and the evidence now discriminates between them:

- **Wrong depth** (B's shape theory) would predict the client reaches *something* one level
  short — plausibly our `wave_list` array, and would likely still resolve `ref_id` on a wave
  record. It does not.
- **Wrong or unmatched key** predicts the client indexes a container under a key we do not
  provide, gets a null/absent node, and every read returns null → `from_json(null, string)` →
  `""`. **That is exactly the observed symptom, and it explains all five at once.**

`_DAT_00a0d4f4` is **`"_id"`**, and it is used as the *outer* key: `param_3["_id"]`. So the
outer container is indexed by a literal `"_id"`, not by a stage id. That is a strong hint the
key the client indexes with is not the stage id we assume it is.

## 4. The single decisive next step

Do not guess the shape. One decompile settles it — and the Ghidra agent already holds the
locked project:

1. **Decompile the caller `CSRSyncMStage::ReqTargetStageMonsterCB` at `0xb4606c`** in full. It
   resolves `ret_data` and a literal `"0"`. Establish exactly **what it passes as `param_3`** to
   `AddStageMonster`, and **what key it uses to index it**. That is the whole question.
2. **Resolve the one remaining unresolved literal, `_DAT_00a0d4fc`** (referenced at
   `0xa0d2f4`; it is used to build the key string passed to the innermost `operator[]`, per
   `ghidra-enemycamp-decomp-05.txt`). It is *not* in `ghidra-wave-keys.txt` — only 5 of the
   function's literals were recovered. This literal may be the actual field being read, and it
   is the most likely single unknown left in this function.
3. Confirm whether `param_3` is `ret_data` itself or `ret_data[stageId]`, and whether the
   client iterates `ret_data` per stage before calling in.

If the answer is "the client indexes by `X`", the fix is one key in one response and the five
empties should collapse.

## 5. Second, independently provable defect — safe to ship regardless

B found that `CSRGameMob::AddMonster` (0xa0b540) **takes no id argument**; its first resolved
key is **`_server`** (`ghidra-instenemy2.txt:2`, at `0xa0b558`), and that value is what keys the
`m_mMonsters` map.

`server-ts/src/bootstrap.ts:208-215`, `starterMonster`, has **no `_server` field**. So the
monster map is keyed on the empty string, which is a sufficient explanation for
`CSRGameMob::GetMonsterData` missing at `SRGameMob.cpp(38)` independently of the ref-id defect.

This one does not depend on resolving the shape question, because B's evidence for it is
direct: the literal is resolved, and the field is simply absent from our fixture. It is a
one-line addition and should go in regardless of what the shape turns out to be. It is the
**only** change from this round I am willing to ship without further native confirmation.

## 6. Status

| Claim | Status |
|---|---|
| `AddStageMonster` does two nested iterations then a keyed string read | **CONFIRMED** (read directly) |
| `GetCard` is an array of records with `base` | **CONFIRMED** — stop re-testing |
| `/mirage/GetInfo` is the carrier | **REFUTED** — wrong scene, no `SetRefID` |
| `AddMonster` keys `m_mMonsters` on `_server` | **CONFIRMED by resolved literal**; field absent from our fixture → ship it |
| 5 empties = 5 values of our wave record | **REFUTED** — `ref_id` would have resolved non-empty |
| Response shape is wrong | **LIKELY** — but the wrongness is in the **key**, not (only) the depth |
| The five-count is explained | **STILL UNEXPLAINED** — no wave shape we send accounts for it |

Next: continue the Ghidra lane's session with §4's three questions. Do not ship a shape change
before `ReqTargetStageMonsterCB` is read.
