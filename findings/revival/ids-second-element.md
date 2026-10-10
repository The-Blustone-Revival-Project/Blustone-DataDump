# WHERE THE SECOND `ids` ELEMENT COMES FROM — the wave `ref_id`, via the **waves** loop in `FUN_00b4a7a8`

Native-analysis lane, 2026-10-02. Scope: `CSRGameMob::AddStageMonster` (`0xa0d194`),
`CSRGameMob::GetStageMonsterLinkData` (`0xa0cf38`), and the request-list builder
`FUN_00b4a7a8` (`0xb4a7a8`).

**Address space: Ghidra image addresses throughout.** No `BLUSTONE_ARM` offset is used
for any structural claim here, and no symbol was attributed by nearest-preceding-name.
Every claim below is quoted from raw instruction listings in this session's dumps.

---

## VERDICT (read this first)

> **The second requested id does NOT come from `STAGE_MONSTER_LINK::ids` at all, and it
> does not come from a second `show_thumbnail` read.**
>
> **`FUN_00b4a7a8` — the function that builds the `GET /reference/GetMonster` `list` —
> walks BOTH vectors returned by `GetStageMonsterLinkData`: it iterates `ids` (stride
> `0xc`, our `show_thumbnail`) *and then* it iterates the `waves` structure at stride
> `0x14`, appending every wave record's embedded string to the SAME list.**
>
> Therefore the second element is the wave **`ref_id`** (`"001"`), and the fix is **A**:
> the wave `ref_id` must be a **monster** id, not the card id `"001"`.

This inverts the premise of the question. Two sub-answers, both **[RECOVERED]**:

| Question | Answer |
|---|---|
| Does `ids` have one writer or two? | **Exactly ONE** — the record-level `show_thumbnail` loop at `0xa0d50c`. **[RECOVERED]** |
| Is `show_thumbnail` read at record level or per-wave? | **Record level only**, and it is read **once, after** the wave loop. **[RECOVERED]** |
| Does `ref_id` ever enter `ids`? | **No.** It goes only into the 20-byte `STAGE_MONSTER` wave record. **[RECOVERED]** |
| So where does `"001"` come from? | **The second loop in `FUN_00b4a7a8`, over `waves`, stride `0x14`.** **[RECOVERED]** |

The tester's framing — "either `show_thumbnail` is read twice, or `ref_id` is pushed into
`ids`" — was a well-posed binary choice, and **both of its horns are false**. The
second element is real, but it is contributed by the *consumer*, not by `AddStageMonster`.

---

## 1. `AddStageMonster` has exactly five `operator[]` sites, and there is no sixth **[RECOVERED]**

Counted from the raw listing, not from the offline resolver:

```
$ Select-String -Path analysis\ghidra-ids-03-asm-addstagemonster.txt -Pattern "bl 0x007930f8"
  27: 00a0d1ce  bl 0x007930f8
 154: 00a0d304  bl 0x007930f8
 180: 00a0d34a  bl 0x007930f8
 209: 00a0d398  bl 0x007930f8
 347: 00a0d512  bl 0x007930f8
```

Five. The five keys previously believed (`wave_list`, `ref_id`, `group`,
`next_spawn_ms`, `show_thumbnail`) are correct, and `_id` is **not** among them
(`ROOT-CAUSE-v4` §3's retraction stands; I did not rely on it — see §6).

### 1a. Each site's key, resolved by dataflow **[RECOVERED]**

Ghidra's own flow analysis (not the offline heuristic) plus literal reads from Ghidra's
**relocated** memory, `analysis/ghidra-ids-07-opbracketkeys-addstagemonster.txt`:

```
--- call #1 @ 00a0d1ce   r1: wave_list      [literal@01d76bd5  ldr@00a0d1b0  add@00a0d1b8]
--- call #2 @ 00a0d304   r1: ref_id         [literal@01d6edf2  ldr@00a0d2fa  add@00a0d300]
--- call #3 @ 00a0d34a   r1: group          [literal@01d658fa  ldr@00a0d33e  add@00a0d342]
--- call #4 @ 00a0d398   r1: next_spawn_ms  [literal@01d76bdf  ldr@00a0d390  add@00a0d394]
--- call #5 @ 00a0d512   r1: show_thumbnail [literal@01d76bed  ldr@00a0d50c  add@00a0d50e]
```

These **match the known-good offline resolution 7/7**, independently reproduced here.

> **Two bugs I hit and fixed in my own script, both of which silently produced a
> plausible-but-wrong key — the exact failure class this project has been bitten by three
> times. They are recorded because a reader must be able to distrust the tool.**
>
> 1. **PC is *not* word-aligned.** For `add rD,pc`, PC = instruction address **+4** with
>    only bit 0 cleared. Rounding down to 4 gives `0x01d76beb` = the **tail of
>    `next_spawn_ms`** instead of `0x01d76bed` = `show_thumbnail`. Verified against raw
>    bytes: only `0x01d76bed` is preceded by a NUL
>    (`analysis/ghidra-ids-11-pool-showthumbnail.txt:33`, `nulBefore=true`).
> 2. **`getLength()` returns 2, not 4, for these Thumb literal loads**, so a
>    "must be a 4-byte Thumb-2 `ldr`" filter rejects *every* one of them
>    (`loads=0`). Also, Ghidra prints the whole instruction (`ldr r0,[0x...]`), so
>    matching a leading `r` register against the full string always fails.
>
> The **register match** (`add` must write the same register as the `ldr`) is what makes
> attribution unambiguous, and it is strictly better than the offline tool's
> "next instruction" rule: at `0xa0d1b0` the real `add r1,pc` is **five** instructions
> below the `ldr`, with `add r0,pc` (the stack guard) in between — which is how `_id`
> was invented in the first place.

---

## 2. `show_thumbnail` is read at **record level**, and only **once** **[RECOVERED]**

This is the specific thing the brief asked me to verify ("earlier analysis says record
level only, reached from `0xa0d260 bne.w 0x00a0d50c`"). **Confirmed, by tracking the
object register rather than by reading the comment.**

`ghidra-ids-03-asm-addstagemonster.txt:344-347` — the `show_thumbnail` call:

```
344: 00a0d50c  ldr r1,[0x00a0d874]     ; the 'show_thumbnail' literal
345: 00a0d50e  add r1,pc
346: 00a0d510  ldr r0,[sp,#0xc]        ; <-- the json object
347: 00a0d512  bl 0x007930f8           ; operator[](json, "show_thumbnail")
```

Compare the `wave_list` call, `ghidra-ids-03-asm-addstagemonster.txt:25-27`:

```
25: 00a0d1ca  mov r0,r3              ; r3 = param_2, set at 0xa0d1a8
26: 00a0d1cc  str r3,[sp,#0xc]        ; sp+0xc  =  param_2  (the RECORD)
27: 00a0d1ce  bl 0x007930f8           ; operator[](record, "wave_list")
```

So at `0xa0d512`, `r0 = param_2` — **the record**, not a wave element. There is a
complete, exhaustive audit of the slot:

```
=== EVERY write to sp+0xc, in address order ===
26: 00a0d1cc  str r3,[sp,#0xc]        ; = param_2  (the record json)
398: 00a0d588 str r0,[sp,#0xc]        ; = sp+0x8c  (the ids vector, see §3)

=== EVERY read of sp+0xc, in address order ===
346: 00a0d510  ldr r0,[sp,#0xc]        ; the show_thumbnail operator[]  <-- BEFORE the rewrite
427: 00a0d5d4  ldr r0,[sp,#0xc]        ; ids.push_back slow path
497: 00a0d686  ldr r1,[sp,#0xc]        ; the pair construction
```

`sp+0xc` is a **reused compiler scratch slot**. It is written twice:
`0xa0d1cc` (=`param_2`) and `0xa0d588` (=`sp+0x8c`, inside the `show_thumbnail` loop,
computed at `0xa0d582: add r0,sp,#0x80` + `0xa0d586: adds r0,#0xc`). The read at
`0xa0d510` is **before** the second write, so it sees `param_2`. ✔

**Control flow confirms it is reached once, on loop exit:**
`0xa0d260 bne.w 0x00a0d50c` is the `wave_list` loop's exit edge, and from `0xa0d50c`
the only onward path is `0xa0d672` (the emplace) — `0xa0d59c bne 0x00a0d672` is the
`show_thumbnail` loop's own exit. So `show_thumbnail` is read **after** all waves are
consumed, **not** per wave.

**⇒ Hypothesis (B) is FALSE.** `show_thumbnail` is not read at two levels. Our
per-wave `show_thumbnail` is **inert**; only the record-level one contributes.

---

## 3. `ids` has exactly ONE writer, and `ref_id` never reaches it **[RECOVERED]**

The `ids` vector occupies `sp+0x8c` (`begin`), `sp+0x90` (`end`), `sp+0x94` (`cap`).
Every access to it:

```
 24: 00a0d1c8  str r4,[sp,#0x90]        ; zero-init end  (r4 = 0, from 0xa0d1b6)
398: 00a0d588  str r0,[sp,#0xc]         ; remember &ids.begin for the push_back path
414: 00a0d5b0  ldrd r6,r0,[sp,#0x90]     ; load end,cap
458: 00a0d62c  str r0,[sp,#0x90]         ; *** THE ONLY ADVANCE ***  end += 0xc
566: 00a0d73c  ldr r4,[sp,#0x8c]         ; teardown
580: 00a0d75e  ldr r0,[sp,#0x8c]
583: 00a0d764  str r4,[sp,#0x90]
```

**There is exactly one `ids` advance: `0xa0d62c`, `end += 0xc`** — a 12-byte
`std::string` — and it sits inside the `show_thumbnail` loop:

```
457: 00a0d628  add.w r0,r6,#0xc        ; 12 bytes == one std::string
458: 00a0d62c  str r0,[sp,#0x90]        ; ids.end++
```

with the element copy-constructed from the loop's own 12-byte string at `sp+0x70`
(`0xa0d5c6 vldr.64 d16,[sp,#0x70]` / `0xa0d5cc str r0,[r6,#0x8]` / `0xa0d5ce vstr.64 d16,[r6]`).

**Where `ref_id` goes instead — the 20-byte wave record**, `ghidra-ids-03:246-249`:

```
246: 00a0d3fc  str r1,[r0,#0x8]         ; STAGE_MONSTER+0x8   \
247: 00a0d3fe  vstr.64 d16,[r0]         ; STAGE_MONSTER+0x0   / 12-byte ref_id string
248: 00a0d402  ldrd r1,r2,[sp,#0x1c]     ; group, next_spawn_ms
249: 00a0d410  adds r0,#0x14            ; stride 0x14 = 20 bytes  (ref_id 12 + int + float)
```

That `0x14` stride is `CSRGameMob::STAGE_MONSTER`, and it is pushed into the **outer**
`waves` vector, never into `ids` (`0xa0d470 bl 0x00a0d0cc`, `0xa0d480 bl 0x00a0e4ac`).

**⇒ `ids` has exactly one writer: the record-level `show_thumbnail`.**
**⇒ Hypothesis (A) is FALSE as stated for `ids`** — `ref_id` is *not* pushed into `ids`.

---

## 4. The actual second element: `FUN_00b4a7a8` walks **both** vectors **[RECOVERED]**

This is the answer the recovered model was missing. The function that builds the
`GetMonster` request `list` has **two** loops over the two vectors returned by
`GetStageMonsterLinkData`, and **both append to the same list**.

First, the sret shape. `GetStageMonsterLinkData` (`ghidra-ids-02-asm-getlink.txt:26-38`)
returns **24 bytes**: a 12-byte `vector<vector<STAGE_MONSTER>>` then a 12-byte
`vector<string>`:

```
26: 00a0d46   add.w r4,r1,#0xc          ; this+0xc  == the map<string,STAGE_MONSTER_LINK>
...
72: 00a0cf72  add.w r1,r4,#0x1c         ; node+0x1c == waves
76: 00a0cf76  mov r0,r8
78: 00a0cf78  bl 0x00a0dca8              ; -> param_1 (sret+0x00) = waves
79: 00a0cf7c  add.w r0,r8,#0xc          ; sret+0x0c
80: 00a0cf80  add.w r1,r4,#0x28         ; node+0x28 == ids
81: 00a0cf84  bl 0x00706700              ; -> param_1+0x0c = ids
```

So in `FUN_00b4a7a8`, with `sret` at `sp+0xc` (`0xb4a7e4 add r0,sp,#0xc`):

* `sp+0x0c .. sp+0x17` = **waves** (begin/end/cap)
* `sp+0x18 .. sp+0x23` = **ids** (begin/end/cap)

And now the two loops (`analysis/ghidra-ids-01-asm-fun-b4a7a8.txt`):

### Loop 1 — over `ids`, stride `0xc` (our `show_thumbnail`)

```
27: 00b4a7ea  ldrd r5,r8,[sp,#0x18]      ; r5 = ids.begin, r8 = ids.end
32: 00b4a7f8  adds r5,#0xc              ; 12-byte std::string
37: 00b4a804  bl 0x00a0b428              ; HasMonsterData(r5)
39: 00b4a80a  bne 0x00b4a7f8             ; have it -> skip
45: 00b4a81a  bl 0x006d7efc              ; basic_string copy ctor from r5
48: 00b4a828  str r4,[sp,#0x24]          ; *** append to the list at sp+0x24 ***
51: 00b4a82c  str r0,[sp,#0x2c]          ; *** count++ ***
```

### Loop 2 — over **`waves`**, outer stride `0xc`, **inner stride `0x14`**

```
54: 00b4a830  ldrd r8,r9,[sp,#0xc]       ; r8 = waves.begin, r9 = waves.end
60: 00b4a842  add.w r8,r8,#0xc           ; 12 bytes == one vector<STAGE_MONSTER>
63: 00b4a84a  ldrd r5,r10,[r8,#0x0]      ; r5 = that wave's begin, r10 = its end
74: 00b4a864  adds r5,#0x14              ; *** 20 bytes == STAGE_MONSTER ***
79: 00b4a870  bl 0x00a0b428              ; HasMonsterData(r5)   <-- on the WAVE RECORD
81: 00b4a876  bne 0x00b4a864             ; have it -> next wave element
87: 00b4a886  bl 0x006d7efc              ; basic_string copy ctor from r5  (ref_id!)
76: 00b4a85c  ldr r0,[sp,#0x2c]
77: 00b4a85e  str r4,[sp,#0x24]          ; *** SAME list at sp+0x24 ***
80: 00b4a862  str r0,[sp,#0x2c]          ; *** SAME counter at sp+0x2c ***
```

**Both loops push to the identical list head (`sp+0x24`) and bump the identical counter
(`sp+0x2c`).** That list becomes the `list` field of the request.

**The stride `0x14` in loop 2 is the proof.** It is exactly the `STAGE_MONSTER` stride
established independently in §3 (`0xa0d410 adds r0,#0x14`), and `STAGE_MONSTER`'s first
12 bytes are the `ref_id` string — which is why `HasMonsterData` is handed `r5` directly
and why the copy at `0xb4a886` produces a `basic_string`.

**⇒ `list` = `ids` ∪ {every wave record's `ref_id`}.**

Our response:

```json
"show_thumbnail": ["M001"],              -> ids   = ["M001"]
"wave_list": [[{"ref_id": "001", ...}]]  -> waves = [["001"]]
```

⇒ `list = ["M001", "001"]` — **exactly the observed request, in the observed order.**
One entry from loop 1, one from loop 2. Fully accounted for; nothing is left over.

---

## 5. The fix

**Option A.** The wave `ref_id` must name a **monster**, because `AddStageMonster` files
it as a `STAGE_MONSTER` (loop 2 → `HasMonsterData` → `m_mMonsters`), *and*
`MakeStageInst` separately feeds the same `ref_id` to `CSRCard::SetRefID`
(`enemy-camp-writer.md` §Q4). Two consumers, one string — so `ref_id` must be a string
that is simultaneously a valid monster id and a valid card id in the real data.

Concretely, either of these clears the `"001"` request:

1. **Set the wave `ref_id` to the monster id** (`"M001"`), and make sure the card
   referenced by the enemy camp resolves. Then `ids` and the wave agree and `list`
   de-duplicates naturally to one entry.
2. **Publish a monster under `_server: "001"`** from `/reference/GetMonster`, so the
   existing `ref_id` has a node in `m_mMonsters`.

Option 1 is preferable if the *card* side can be satisfied, because it removes the
card/monster id split that `AGENTS.md` §11 has been carrying for many rounds. **Which
card id the enemy camp needs is not decided here** — that is the separate `SRCard.cpp(731)`
defect and out of this lane's scope.

**Explicitly NOT recommended:** adding `"001"` to `show_thumbnail`. It would silence the
assert without fixing the underlying card/monster confusion, and loop 2 would still
request `"001"` separately. The assert would move rather than clear.

---

## 6. Method notes and honest caveats

* **No nearest-symbol attribution.** Every structural claim quotes an instruction from a
  listing produced in this session. The only names used (`AddStageMonster`,
  `GetStageMonsterLinkData`, `HasMonsterData`, `FUN_00b4a7a8`) are Ghidra's own
  function entries at the addresses named in the headings.
* **`_id` was not taken on trust.** `ROOT-CAUSE-v4` §3 retracted it; I re-derived the
  key set independently (§1a) and confirm there is no `_id` `operator[]` site. I did not
  read its bytes.
* **`FUN_00b4a7a8` has zero static callers** (`ghidra-ids-05-callers-fun-b4a7a8.txt`,
  `callers: 0`) — it is reached through a function pointer (it builds a `std::function`
  at `0xb4a916-0xb4a94c` and passes it to `0x00b444c4`). Who installs that pointer is
  **[UNKNOWN]** and does not affect the verdict: the request demonstrably fired.
* **No `adb`, no Docker, no server, no Git, no `server-ts` edit.** Ghidra was used
  exclusively, as owned.
* **`STAGE_MONSTER`'s field layout** (12-byte `ref_id` + `group` + `next_spawn_ms`, 20
  bytes) is **[RECOVERED]** from the stride and the three stores at `0xa0d3f6-0xa0d40c`.
  The individual field offsets inside the tail 8 bytes are **[INFERRED]** from the
  `group` / `next_spawn_ms` key order; only the first 12 bytes are load-bearing here.
* **One negative result stated as such:** I did not enumerate all callers of
  `GetStageMonsterLinkData` beyond confirming `MakeStageInst` consumes it. Whether any
  *other* consumer reads `ids` is **[UNKNOWN]** and irrelevant to this question, because
  the `GetMonster` request is built in exactly one place — `FUN_00b4a7a8` — and
  `HasMonsterData` is called from nowhere else in the binary
  (`hasmonsterdata.md` §Q2, re-confirmed by the two `0x00a0b428` sites in
  `ghidra-ids-01`, one per loop).

---

## 7. Raw dumps (this session)

| file | contents |
|---|---|
| `analysis/ghidra-ids-01-asm-fun-b4a7a8.txt` | **full instruction listing of `FUN_00b4a7a8`** — the two loops, the shared list at `sp+0x24`/`sp+0x2c`, strides `0xc` and `0x14`. **The primary evidence.** |
| `analysis/ghidra-ids-02-asm-getlink.txt` | instructions of `GetStageMonsterLinkData` `0xa0cf38` — the 24-byte sret split (`node+0x1c` waves, `node+0x28` ids) |
| `analysis/ghidra-ids-03-asm-addstagemonster.txt` | full listing of `AddStageMonster` `0xa0d194` — the 5 `operator[]` sites, the single `ids` advance, the `STAGE_MONSTER` build |
| `analysis/ghidra-ids-04-decomp-getlink.txt` | decompile of `GetStageMonsterLinkData`, naming both `vector` types explicitly |
| `analysis/ghidra-ids-05-callers-fun-b4a7a8.txt` | negative result: `FUN_00b4a7a8` has no static callers (function-pointer invoked) |
| `analysis/ghidra-ids-06-callers-getlink.txt` | callers of `GetStageMonsterLinkData` |
| `analysis/ghidra-ids-07-opbracketkeys-addstagemonster.txt` | **the five `operator[]` keys resolved by dataflow**, with slot/add/load addresses and distances |
| `analysis/ghidra-ids-07b-inventory-AddStageMonster.txt` | the full pc-relative literal inventory of `AddStageMonster` (7 literals) |
| `analysis/ghidra-ids-08-decomp-b4a7a8.txt` | decompile of `FUN_00b4a7a8` (corroborates the two loops at the C level) |
| `analysis/ghidra-ids-11-pool-showthumbnail.txt` | **raw pool bytes** at `0x01d76bd0` — proves `0x01d76bed` is a NUL-preceded `show_thumbnail` and `0x01d76beb` is the tail of `next_spawn_ms` |
| `analysis/ghidra-ids-13/15-code-*.txt`, `-14/16-slot-*.txt` | raw code + literal-slot bytes for the `show_thumbnail` and `group` sites (hand-decode check) |
| `analysis/ghidra-ids-run-01.log` … `-04.log` | headless runs |

### Scripts added (additive, per ownership)

| script | why |
|---|---|
| `analysis/ghidra-scripts/ResolveOperatorBracketKeys.java` | Resolves the key for every `operator[]` call by **register dataflow** (`add rD,pc` must write the same register as the `ldr`), scanning up to 6 instructions ahead. Does not use the offline tool's "immediately next" pairing. Needed because that pairing produced three wrong keys in this project. |
| `analysis/ghidra-scripts/DumpByteRange.java` | Dumps raw bytes as hex+ASCII and enumerates every NUL-delimited candidate start with `nulBefore`/`nulAfter`. Exists because a mis-resolved literal yields a *plausible truncated string* rather than a visible error, so resolution must be checkable against bytes. |

---

## 8. What this closes and what it does not

**Closes:** where the second requested id comes from. Not `show_thumbnail`, not a second
read of it, not `ids` — it is the wave `ref_id`, appended by the consumer's second loop
over `waves` at stride `0x14`.

**Also closes, as a side effect:** `report-014` §6's open row "Where the second `ids`
element comes from (not `show_thumbnail`, which has 1)" is answered, and the
"`show_thumbnail` is the query" model in `hasmonsterdata.md` §Q3 is **incomplete** —
`show_thumbnail` is *an* input to `list`, not the only one. That note's *other*
conclusions (the `list` is verbatim, `m_mMonsters` keyed by `_server`, single writer) are
unaffected and remain sound.

**Does not close:** whether `MakeStageInst`'s `CSRCard::SetRefID` will accept the chosen
`ref_id` — the separate player/player-camp card-table defect (`SRCard.cpp(731)`), which
this lane did not examine and which must not be conflated with the fix above.