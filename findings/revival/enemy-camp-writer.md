# ENEMY-CAMP-WRITER — who populates `CSRMStage+0x264`?

Narrow native-analysis lane, 2026-10-02.
Scope: `CSRMStage::MakeStageInst` (Ghidra `0xb33f84`), `CSRGameMob::GetStageMonsterLinkData`
(`0xa0cf38`), `CSRGameMob::AddStageMonster` (`0xa0d194`), `CSRSyncMStage::ReqTargetStageMonsterCB`
(`0xb4606c`), and the `unordered_map` value constructor `__emplace_unique_key_args<CMHashID,…>`
(`0x00904604`).

**Address space: Ghidra image addresses throughout.** Verified in this session, not assumed —
`analysis/ghidra-camp-16-bytes-vs-listing.txt:2` shows Ghidra's own
`IMAGE_BASE 00010000`, and `:5-6` shows that for Ghidra `0xb3507a` / `0xb35078` the program holds
the halfwords `c864` / `8968` (LE `0x64c8` / `0x6889`), i.e.
`str r0,[r1,#0x4c]` / `ldr r1,[r1,#0x8]` — the adjudication's decisive encoding, reproduced from
the program itself. So **ELF = Ghidra − 0x10000** and
`file_offset + 0x10000 = Ghidra address` holds. No new symbol was named after a byte check
in this note; addresses come from Ghidra's disassembler and its function map.

**Method note / a trap I fell into and abandoned.** I first tried to prove "no other function
writes `+0x264`" with a hand-rolled offline Thumb encoder
(`scan-member-offset-offline.py`, written then deleted; its output file
`ghidra-camp-15-scan-offset-264.txt` was deleted with it). It reported 0 hits for an immediate
that demonstrably exists, and my hand decode of known-good instructions disagreed with Ghidra.
**My decoder was wrong; Ghidra was right.** A whole-`.text` offline `bl` scan found *no* call
to any known target, which is the giveaway. I therefore did not use the offline scan for any
claim below. The ownership proof in §2 is done **inside Ghidra** with
`DumpInstructions` over the whole `CSRMStage` method block. This is the same discipline the
adjudication applied to the fault site — a claim about the binary is settled against the binary
— and it is recorded here because a reader may otherwise assume the "no other writer" result
came from a cheaper source than it did.

---

## Q1 — Decompile `MakeStageInst` (`0xb33f84`); where is `this+0x264` read? **[RECOVERED]**

Full decompile: `analysis/native-makestageinst.txt:5689-7036` (`===== 00b33f84 MakeStageInst =====`).
Full instruction listing: `analysis/ghidra-camp-02-insn-full-makestageinst.txt`
(function body `0xb33f84 … 0xb35196`; next function entry is `PopUpPause` at `0xb35650`).

The function has four phases. Only the last two touch the camp map.

### Phase A — player camp (`this+0x250`) — *not* the enemy camp
`this+0x250` is a **second, identical-shaped** map
`unordered_map<CMHashID, list<list<ACTOR_INFO>>>`, keyed by the *decimal string of the deck slot
index*, filled from `/lobby/GetCardInven` via `CSRPlayData::GetDeckInfo`
(`native-makestageinst.txt:5963-6215`; asm `0xb341c2 add.w r1,r9,#0x250`, `0xb341d8 bl 0x009041b8`).
This is the source of the five `CSRCard::SetRefID` assertions in `AGENTS.md` §11 — the **card**
table problem — and it is a *different* member from the one in question.

### Phase B — the stage id
```
native-makestageinst.txt:5856-5857
  this_01 = (CSRGameStage *)CSRGameStage::get();
  iVar14 = CSRGameStage::GetStageData(this_01,(basic_string *)(this + 0x220));
```
`this+0x220` is a `std::string` member: `asm 0xb34026  add.w r10,r9,#0x220` then
`0xb3402c bl 0x00a27f60` (`GetStageData`). **`this+0x220` is the current stage id.**

### Phase C — the enemy camp writer (`this+0x264`) **[RECOVERED]**

Decompile, `analysis/native-makestageinst.txt:6627-6690` (abridged to the structure):

```c
6627: LAB_00b34b0e:
6628:   CSRGameMob::get();
6629:   CSRGameMob::GetStageMonsterLinkData((basic_string *)&local_68);
...
6632:   if (local_68 == p_Stack_64) {
6633:     local_134 = 0;                                   /* no waves at all  */
6634:   } else {
...
6651:       CSRLevelData::GetMonsterGroupID((CSRLevelData *)&local_120);   /* == "enemy" */
...
6658:       ...(CMHashID *)(this + 0x264), (piecewise_construct_t *)&local_120, ...
6661:       piVar18 = operator_new(0x14);
...
6689:       pbVar24 = *(basic_string **)(p_Var15 + 4);
6690:       for (pbVar46 = *(basic_string **)p_Var15; pbVar46 != pbVar24; pbVar46 = pbVar46 + 0x14) {
6691:         CSRGameActor::ACTOR_INFO::ACTOR_INFO((ACTOR_INFO *)&local_120);
6697:         CSRCard::SetRefID(local_ec,pbVar46);
```

and the per-monster half, `native-makestageinst.txt:6755-6853`:

```c
6755:       CSRLevelData::GetMonsterGroupID((CSRLevelData *)&local_98);
6762:       ...(CMHashID *)(this + 0x264), ...
6764:       iVar31 = *(int *)(local_80 + 0x20);
6765:       piVar22 = operator_new(0x68);
...
6825:       piVar22[1] = iVar31 + 8;
6830:       *(int *)(iVar31 + 0x10) = *(int *)(iVar31 + 0x10) + 1;
6834:       local_134 = local_134 + 1;
6852:       p_Var15 = p_Var15 + 0xc;
6853:     } while (p_Var15 != p_Var40);
```

Matching instructions (`ghidra-camp-02-insn-full-makestageinst.txt`):

```
1042: 00b34b0e  bl 0x00a0dac0            ; CSRGameMob::get()
1046: 00b34b18  bl 0x00a0cf38            ; CSRGameMob::GetStageMonsterLinkData(sret sp+0x100, this, key)
1051: 00b34b28  beq.w 0x00b34e88         ; <-- waves.begin == waves.end  ->  SKIP EVERYTHING
1063: 00b34b4e  add.w r0,r0,#0x264        ; sp+0x2c = this + 0x264   (r0 = this from sp+0xc)
1095: 00b34ba4  ldr r1,[sp,#0x2c]
1099: 00b34bac  bl 0x00904604            ; __emplace_unique_key_args<CMHashID, list<list<ACTOR_INFO>>>
1102: 00b34bb4  blx 0x00e0b280           ; operator new(0x14)  -> the empty inner list
1137: 00b34c18  ldr r0,[r5,#0x4]          ; wave.begin / wave.end  (one element of the outer vector)
1142: 00b34c24  bne 0x00b34c38           ; wave non-empty -> add an ACTOR_INFO
1159: 00b34c50  bl 0x0086c30c            ; CSRCard::SetRefID(actor, ref_id_string)
1252: 00b34d54  ldr r1,[sp,#0x2c]
1257: 00b34d60  movs r0,#0x68            ; operator new(0x68) -> the populated wave node
```

So `this+0x264` is **written by `MakeStageInst` itself**, from
`CSRGameMob::GetStageMonsterLinkData(this->stage_id)`. Not by `InitBeforeOpen`.

### Phase D — the faulting store **[RECOVERED]**

`analysis/native-makestageinst.txt:6939-6959`:

```c
6939:   iVar29 = *(int *)(iVar14 + 4);
6950:   CSRLevelData::GetMonsterGroupID((CSRLevelData *)&local_120);
6957:       ...&local_80,(CMHashID *)(this + 0x264), (piecewise_construct_t *)&local_120,
6959:   *(int *)(*(int *)(*(int *)(local_80 + 0x20) + 8) + 0x4c) = iVar29 - local_134 * (iVar12 + -1);
```

and the instructions that realize it (`ghidra-camp-02-insn-full-makestageinst.txt:1519-1535`):

```
1519: 00b35050  bl 0x00a1bff8            ; CSRLevelData::GetMonsterGroupID  -> CMHashID("enemy")
1527: 00b35064  add.w r1,r9,#0x264        ; r9 = this
1529: 00b3506a  bl 0x00904604            ; emplace-or-get "enemy" in this+0x264  (NO emptiness check)
1530: 00b3506e  ldr r1,[sp,#0xe8]         ; r1 = __hash_node* returned by the emplace
1532: 00b35072  ldr r1,[r1,#0x20]         ; r1 = <value>.list.__m_begin_        (offset 0x20 in the node)
1533: 00b35074  mls r0,r0,r6,r8           ; r0 = r8 - r0*r6
1534: 00b35078  ldr r1,[r1,#0x8]          ; r1 = *(__m_begin_ + 8)              <-- FIRST WAVE NODE
1535: 00b3507a  str r0,[r1,#0x4c]         ; *** the adjudicated faulting store ***
```

`ghidra-camp-16-bytes-vs-listing.txt:5-6` confirms from the program's own bytes that
`0xb35078` is `ldr r1,[r1,#0x8]` and `0xb3507a` is `str r0,[r1,#0x4c]` (bytes `8968` / `c864`).

### Why `r1 == 0` — the layout, proven from the value constructor **[RECOVERED]**

The map value is `unordered_map<CMHashID, list<list<ACTOR_INFO>>>`; its entry object is built in
`__emplace_unique_key_args` (`0x00904604`, shared by every `MakeStageInst`). I did not trust
Ghidra's C++ types for this; I read the constructor
(`analysis/ghidra-camp-09-insn-emplace.txt:75-95`):

```
75: 009046c0  movs r0,#0x30              ; sizeof(entry) = 48
78: 009046c8  blx 0x00a16570             ; operator new(0x30)
81: 009046d0  adds r0,#0x8               ; the CMHashID key is copy-constructed at entry+8  -> 24 bytes
88: 009046e6  add.w r2,r6,#0x18
91: 009046f0  add.w r8,r6,#0x20          ; r8 = entry + 0x20
92: 009046f4  stm r2,{r0,r1,r8}          ; entry+0x20 = entry+0x20
94: 009046fc  strd r8,r9,[r6,#0x24]      ; entry+0x24 = entry+0x20 ; entry+0x28 = 0
```

So, for a freshly-created entry:

* `entry+0x20` = `list::__m_begin_` = **`entry+0x20`** — the list's own self-referential sentinel,
* `entry+0x24` = `list::__m_end_`   = `entry+0x20`,
* `entry+0x28` = `list::__m_size_`  = **0**.

Now trace `0xb3506e/0xb35072/0xb35078` with the list **empty**:

| instruction | value |
|---|---|
| `ldr r1,[sp,#0xe8]` | `r1 = entry` |
| `ldr r1,[r1,#0x20]` | `r1 = __m_begin_ = entry+0x20`  (the sentinel — **not null**) |
| `ldr r1,[r1,#0x8]`  | `r1 = *(entry+0x28) = __m_size_ = ` **`0`** |
| `str r0,[r1,#0x4c]` | store to address `0x4c` with `r1 == 0` |

**This is an exact match for the reported fault: `fault = 0x4c`, `r1 = 0`.** The pointer that is
null is not the list — it is the `__m_size_` word that the code mistakes for a wave-node pointer.
The three-way coincidence (fault address = the store's displacement, `r1 == 0`,
PC = instruction + 1) is the same standard the adjudication used, now re-derived from the
value's own constructor rather than from the crash report.

Cross-check with the *populated* path, which is the same code shape one level down
(`0xb34d5e`–`0xb34e2a`): there `r4 = *(entry+0x20)` is the 20-byte **outer** node, and
`r1 = *(r4+8)` is that node's inner `list<ACTOR_INFO>.__m_begin_`, i.e. a real 0x68-byte wave
node's `list` header. `str r0,[r1,#0x4c]` then writes a field inside the **first enemy actor of
the first wave**. Same instruction, meaningful pointer. So the store is *only* a null deref when
the outer list is empty.

---

## Q2 — Who writes `this+0x264`? **[RECOVERED]**

**`CSRMStage::MakeStageInst` (`0xb33f84`), and nowhere else.**

Proof, done inside Ghidra (not offline): `DumpInstructions` over the entire `CSRMStage` method
block, Ghidra `0xb33000 … 0xb37200` (121 206 bytes of listing,
`analysis/ghidra-camp-17-insn-csrmstage-block.txt`), then grepping for the immediate
(line numbers are from that file):

```
 1333: 00b341c2  add.w r1,r9,#0x250   ; this+0x250 -- the sibling *player* camp map
 2182: 00b34b4e  add.w r0,r0,#0x264
 2646: 00b35064  add.w r1,r9,#0x264
```

**Exactly two `#0x264` sites in the whole class block, and both are inside `MakeStageInst`**
(`0xb33f84 … 0xb35196`; the next function entry in the block is `PopUpPause` at `0xb35650`).

Corollaries:

* **`InitBeforeOpen` (`0xb33ccc`) does not write it.** Its decompile
  (`analysis/ghidra-leveldata-insn-01.txt`, and the `leveling_m` call site at `0xb33cea`–`0xb33cf2`)
  loads level data and UI and never reaches `0x264`; the block listing above proves no `#0x264`
  instruction exists anywhere between `0xb33ccc` and `0xb35196` other than the two above.
* **No other `CSRMStage` method reads it either.** Same grep. The only consumer of the camp maps
  is code outside this class; I did not chase it (out of scope, and not needed for the verdict).
* Caller graph caveat: `ListCallers` on both `0xb33f84` and `0xb33ccc` returns only
  `from 0x0 <no function>` (`ghidra-camp-13-*`, `ghidra-camp-14-*`), i.e. **they are reached
  through a virtual/member-function table, not a static call edge.** The relative order of
  `InitBeforeOpen` and `MakeStageInst` therefore cannot be read from static references; do not
  infer it.

---

## Q3 — What data does the writer consume? **`GetStageMonsterLinkData` + `STAGE_MONSTER_LINK`**

### The call **[RECOVERED]**
```
00b34b0e  bl 0x00a0dac0            ; CSRGameMob::get()
00b34b12  mov r1,r0
00b34b14  add r0,sp,#0x100         ; sret: 24-byte { vector<vector<STAGE_MONSTER>> ; vector<string> }
00b34b16  mov r2,r11               ; r11 == this + 0x220  (see below)
00b34b18  bl 0x00a0cf38            ; GetStageMonsterLinkData
00b34b1c  ldrd r5,r0,[sp,#0x100]    ; waves.begin , waves.end
00b34b28  beq.w 0x00b34e88         ; if empty -> skip the whole writer
```

**The key is `CSRMStage+0x220`, the scene's own stage-id string, not a literal.**
Proven by instruction, not by symbol proximity:
`0xb34026 add.w r10,r9,#0x220` (r10 = `this+0x220`) →
`0xb34198 str.w r10,[sp,#0x1c]` →
`0xb34686 ldr.w r11,[sp,#0x1c]` →
`0xb34b16 mov r2,r11`.
(`ghidra-camp-02-insn-full-makestageinst.txt:66, 200, 629, 1046`.)

### The accessor **[RECOVERED]**
`analysis/ghidra-enemycamp-decomp-05.txt:1-62` (also `ghidra-hasmonster-01-lookup.txt:107-124`):

```c
uVar1 = __count_unique( (tree*)(in_r1 + 0xc), in_r2 );      /* map<string,STAGE_MONSTER_LINK> */
if (uVar1 == 0) {
    vector<vector<STAGE_MONSTER>>::vector( param_1,        (vector *)(in_r1 + 0x18) );
    vector<string>::vector(               (param_1 + 0xc), (vector *)(in_r1 + 0x24) );
} else {
    ... __find_equal( (tree*)(in_r1+0xc), &it, in_r2 );
    p_Var3 = *it;
    if (p_Var3 == 0) FUN_006d8570("map::at:  key not found");   /* decomp-05.txt:44-46 */
    vector<vector<STAGE_MONSTER>>::vector( param_1,     (vector *)(p_Var3 + 0x1c) );
    vector<string>::vector(               (param_1+0xc),(vector *)(p_Var3 + 0x28) );
}
```

The literal is confirmed offline:
`ghidra-camp-07-literals-getlink.txt` → `ldr@0x00a0cfb6 … -> 0x01d694f3 'map::at:  key not found'`.

So, `STAGE_MONSTER_LINK` = `{ vector<vector<STAGE_MONSTER>> waves ; vector<string> ids }` with
`waves` at node `+0x1c` and `ids` at node `+0x28`, and **`CSRGameMob+0xc` is the map, while
`CSRGameMob+0x18` / `+0x24` are two default/fallback vectors.**

### Does the fallback ever get filled? **[RECOVERED: no writer found]**
`CSRGameMob::GetStageWaveData` (`0xa0d088`, `ghidra-camp-10-decomp-getwavedata.txt`) is the only
other reader of `CSRGameMob+0xc` in that class and it has **zero callers**
(`ghidra-camp-11-callers-getwavedata.txt`), and it *reads* the map rather than writing the
fallback. The only writer of `CSRGameMob+0xc` is `AddStageMonster`, whose single caller is
`ReqTargetStageMonsterCB` (`ghidra-camp-03-callers-addstagemonster.txt`:
`from 0xb4612c ReqTargetStageMonsterCB`, 2 refs total).
**I found no code that writes `CSRGameMob+0x18` / `+0x24`.** [INFERRED-strong] therefore: those
two vectors are empty unless the constructor fills them, so **a miss on the stage-id key is
indistinguishable from "no waves".** That is the trap this whole path sets.

### The producer: `AddStageMonster` **[RECOVERED]**

`ghidra-camp-04-decomp-addstagemonster.txt` (`CSRGameMob::AddStageMonster(this, key, json)`)
builds, per wave, a `vector<STAGE_MONSTER>` of `ref_id` strings (`__emplace_back_slow_path`),
pushes each onto `vector<vector<STAGE_MONSTER>>` (`__push_back_slow_path`), and finally:

```c
__emplace_unique_key_args<string, pair<string, STAGE_MONSTER_LINK>>( local_44, this + 0xc );
```

Literal inventory of `0xa0d194:0xa0d800` (`ghidra-camp-06-literals-addstagemonster.txt`):

```
'_id'   'wave_list'   'ref_id'   'group'   'next_spawn_ms'   'show_thumbnail'
```

and the instruction order pins `wave_list` as the *outer* key
(`ghidra-hasmonster-08-asm-addstagemonster-emplace.txt`):

```
00a0d1b0  ldr r1,[0x00a0d4f4]
00a0d1b8  add r1,pc                 ; r1 = &"wave_list"
...
00a0d1ca  mov r0,r3                 ; r0 = param_2 (the per-stage json)
00a0d1ce  bl 0x007930f8             ; json::operator[](r1)  -> r0 = the "wave_list" value
00a0d1de  ldrb r1,[r0,#0x0]         ; begin()/end() of that array, NO empty check -> no early return
```

`ref_id` / `group` / `next_spawn_ms` / `show_thumbnail` are read from each **wave** object
(`ref_id` at `0xa0d2fa`, `group` `0xa0d33e`, `next_spawn_ms` `0xa0d390`,
`show_thumbnail` `0xa0d50c` — all between the two `iteration_proxy` loops in
`ghidra-camp-04-decomp-addstagemonster.txt`).

**⇒ `AddStageMonster` still inserts a map entry when `wave_list` is missing or empty — the entry
just has an empty `waves` vector.** No `continue`, no skip.

### The producer of the map: `ReqTargetStageMonsterCB` **[RECOVERED]**

`analysis/ghidra-enemycamp-decomp-04.txt:1074-1211`:

```c
1122:  iVar2 = CPVHTTPResponse::GetResultCode(...);
1123:  if (iVar2 != 1) goto LAB_00b4619e;                     /* result_code must be 1 */
1124:  local_28 = json::operator[]( "ret_data" );
1127:  iteration_proxy<...>::begin();
...
1157:      this = (CSRGameMob *)CSRGameMob::get();
1162:      pbVar3 = iteration_proxy_value<...>::key();          /* the stage id      */
1167:      pbVar4 = iter_impl<...>::operator*();                 /* the stage object  */
1168:      CSRGameMob::AddStageMonster(this,pbVar3,pbVar4);
```

`'ret_data'` confirmed by `ghidra-camp-08-literals-reqtargetcb.txt`
(`ldr@0x00b46090 r6 … -> 0x01d689bb 'ret_data'`). It uses
`iteration_proxy` + `::key()`, i.e. **`ret_data` is consumed as a JSON OBJECT whose keys are the
stage ids**, exactly as `AGENTS.md` §11 records. This corroborates the adjudication's
"`bl 0xa0d194`, unconditional, gated on `result_code == 1`" and closes Q3: `AddStageMonster`
**is** reached, the link map **is** populated — but populated with whatever `wave_list` says.

---

## Q4 — The conversion between the two structures **[RECOVERED]**

The conversion is **not** a separate function. It is the Phase-C loop inside
`MakeStageInst` itself: `0xb34b0e … 0xb34e8c`.

```
map<string, STAGE_MONSTER_LINK>                       list<list<ACTOR_INFO>>  at this+0x264
  CSRGameMob+0xc                 --GetStageMonsterLinkData(this->stage_id)-->
                                     CSRLevelData::GetMonsterGroupID() -> CMHashID("enemy")
                                     emplace "enemy"                     0xb34bac
                                     operator new(0x14)  empty inner list 0xb34bb4
  outer element  = STAGE_MONSTER_LINK.waves[i]   (a vector, stride 0xc, 0xb34b62)
                                     per ref_id string:
                                       ACTOR_INFO ctor                    0xb34c3a
                                       CSRCard::SetRefID(actor, ref_id)    0xb34c50
                                       emplace "enemy" (again)             0xb34d58
                                       operator new(0x68)  wave node       0xb34d60
```

Layout cross-checks that make the shape unambiguous:

* The **outer** vector's element size is `0xc`
  (`0xb34b62 adds r5,#0xc`, `0xb34b64 cmp r5,r0`) — a 3-word `std::vector` is 12 bytes, so each
  element of `waves` is itself a `vector<STAGE_MONSTER>`. **[RECOVERED]**
* The **inner** vector's element stride is `0x14` (20 bytes)
  (`0xb34c2e add.w r11,r11,#0x14`), and the element is passed straight to
  `CSRCard::SetRefID` (`0xb34c50 bl 0x0086c30c` with `r1 = r11`) — so
  **`CSRGameMob::STAGE_MONSTER` is a 20-byte string type and it holds the monster reference id.** **[RECOVERED]**
  This independently re-confirms the `AGENTS.md` §11 note that the wave `ref_id` is what the
  enemy cards are built from.
* Two distinct allocation sizes appear, matching the two nesting levels exactly:
  `operator new(0x14)` = `list<vector<STAGE_MONSTER>>` node (8 link bytes + 12 empty-vector
  bytes), `operator new(0x68)` = the wave node (8 link bytes + the actor payload that the
  constructor fills at offsets `+0x18`, `+0x24`, `+0x30`, `+0x3c`, `+0x4c`, `+0x58`
  — `0xb34d90`, `0xb34d98`, `0xb34dca`, `0xb34df0`, `0xb34e0a`, `0xb34e12`). **[RECOVERED]**
* `CSRLevelData::GetMonsterGroupID()` returns the constant `CMHashID("enemy")`
  (`leveldata-id-source.md` Q4), so the map has exactly **one** key on this path — the constant
  `"enemy"` — for every stage. There is no per-stage or per-group keying to get wrong.

`this+0x250` is filled by an analogous but independent loop from the player deck (§Q1 Phase A);
it is the card-table defect and is **not** the crash site.

---

## Q5 — What does the converter do when `ids` / a wave vector is empty?

Two different "empty" cases, and **they behave differently**. This is the answer to
"is our data wrong, or did the conversion bail?"

**(a) A wave whose `STAGE_MONSTER` vector is empty → an empty inner list is still inserted.**
```
00b34c18  ldr r0,[r5,#0x4]      ; wave.end
00b34c1a  ldr.w r11,[r5,#0x0]    ; wave.begin
00b34c22  cmp r11,r0
00b34c24  bne 0x00b34c38         ; non-empty -> build an ACTOR_INFO
00b34c26  b 0x00b34b5e           ; EMPTY -> go straight to the next wave
```
The 20-byte node with the empty inner list was already pushed at `0xb34bba…0xb34bd6`
(`strd r1,r2,[r0,#0x4]`, `str r0,[r4,#0x20]`, `str r0,[r4,#0x28]`) **before** this test.
**⇒ an empty wave still occupies a list node.** No `skip`.

**(b) The `waves` vector itself empty → nothing at all is inserted; the `"enemy"` key is never
created by the writer.**
```
00b34b1c  ldrd r5,r0,[sp,#0x100]  ; waves.begin , waves.end
00b34b24  cmp r5,r0
00b34b28  beq.w 0x00b34e88        ; -> movs r0,#0 ; str r0,[sp,#0x34]   (wave count = 0)
```
(`native-makestageinst.txt:6632-6634` is the same thing as `local_134 = 0`.)

So the writer **never bails on bad data in case (a)**; it silently produces a shorter inner list.
Only case (b) produces an *absent* map entry — and case (b) then reaches the unconditional final
store at `0xb35050…0xb3507a`, which emplaces `"enemy"` into a brand-new, empty list and
immediately dereferences its `__m_size_` as a pointer. **Case (b) is the crash.**

There is a third, quieter sub-case worth naming: the `"enemy"` entry may already exist from a
previous `MakeStageInst` call, in which case the emplace returns the existing entry and the store
lands on whatever wave was there before. That is why the fault is intermittent-looking across
runs rather than deterministic-looking from the outside.

---

## VERDICT

> **`CSRMStage+0x264` is populated by `CSRMStage::MakeStageInst` (Ghidra `0xb33f84`), and by
> nothing else in the class. It consumes
> `CSRGameMob::GetStageMonsterLinkData(this->stage_id /* this+0x220 */)` (`0xa0cf38`), i.e. the
> `STAGE_MONSTER_LINK { vector<vector<ref_id>> waves ; vector<string> ids }` stored in the
> `map<string, STAGE_MONSTER_LINK>` at `CSRGameMob+0xc`, which is filled exclusively by
> `CSRGameMob::AddStageMonster` (`0xa0d194`) from `ret_data`'s per-stage object
> (`_id`, `wave_list[].ref_id`, `.group`, `.next_spawn_ms`, `.show_thumbnail`) via
> `CSRSyncMStage::ReqTargetStageMonsterCB` (`0xb4606c`). It is empty on our responses because
> `GetStageMonsterLinkData` returned an empty `waves` vector for the requested stage — either
> because the response produced a `STAGE_MONSTER_LINK` with an empty/absent `wave_list`, or
> because the stage id the scene holds in `CSRMStage+0x220` is not a key of the link map, in
> which case the accessor returns its two fallback vectors `CSRGameMob+0x18`/`+0x24` for which
> I found no writer at all.**

Which of the two is the case here is a **wire question, not a static-analysis question**, and it
is decidable immediately from the server log: `BLUSTONE_LOG_GAME_VALUES=1` logs
`/reference/GetTargetStageMonster`. Two things must line up:

1. `ret_data` must be an **object** keyed by stage id, and every key must match the string in
   `CSRMStage+0x220` (the same string that `CSRGameStage::GetStageData(this+0x220)` resolves, i.e.
   the one that produced the successful `GetStageData` — a non-empty `stages[]`).
2. each value must carry a **non-empty `wave_list`**, each entry carrying a **non-empty
   `ref_id`** string.

`AGENTS.md` §11 already says `/reference/GetTargetStageMonster` is called with
`{"stage_id":"N003"}` and that `GetTargetStageMonster` is "a map keyed by stage id with
`wave_list` entries", so the container shape is believed right. **[UNKNOWN]** whether our
`wave_list` entries actually carry `ref_id` — that key was recovered here for the first time
(`ghidra-camp-06`), and `AGENTS.md` §11's rule list never mentions it. **That is the single
cheapest next check**: log the decrypted `ret_data` of `/reference/GetTargetStageMonster` and
confirm every wave object has a non-empty `ref_id`.

Two further findings worth carrying forward, both **[RECOVERED]**:

* `CSRMStage+0x250` is a *second*, structurally identical camp map (keyed by the decimal deck-slot
  index) filled from `CSRPlayData::GetDeckInfo` → `CSRInventory::FindCard`. The five
  `CSRCard::SetRefID` assertions are that map, not this one. **Two separate empty-container
  defects exist in one function**; fixing one will not fix the other.
* `MakeStageInst` contains a **hard-coded dummy-wave branch**. If `CSRMStage+0x220` equals one
  specific static string — compared at `0xb346ba … 0xb346de` against a runtime-initialised global
  loaded via `ldr r0,[0x00b34720]` — the client builds two synthetic waves without touching the
  link map, with `CSRCard::SetRefID` given the literals **`'001'`** (loaded `0xb3472c`) and
  **`'003'`** (`0xb348d0`), which are *card* ids (`AGENTS.md` §11: "pointing the wave `ref_id` at
  card `001`… cut `SetRefID` from three to one"). Every other stage id falls through to the
  `GetStageMonsterLinkData` path. **[INFERRED]** that string is the tutorial/dummy stage, but
  **[UNKNOWN]** which literal it is — it is a runtime-initialised `std::string`, not a resolvable
  literal-pool entry, so I could not name it. Worth knowing, because a stage id matching it would
  *mask* this bug entirely.

### Method caveats, stated honestly

* Every address here comes from Ghidra's disassembler and function map. I verified the address
  space independently (`IMAGE_BASE 00010000`, byte-confirmed fault site) and I verified the
  decisive null-pointer chain from the map value's own constructor, but I did **not**
  independently re-decode the `bl` targets. I tried, failed, and deleted the attempt — see the
  method note at the top.
* `ListCallers` cannot see the callers of `MakeStageInst`, `InitBeforeOpen` or `OnFinish`
  (virtual dispatch). Their call *order* is **[UNKNOWN]** from static evidence.
* `CSRGameMob+0x18` / `+0x24`: "no writer found" is a **negative result from
  `ListFunctionsInRange` over `0xa0b000…0xa0d400` plus the two `ListCallers` runs**, not a
  proof. A writer in another class, or in the `CSRGameMob` constructor outside that range, is
  not excluded. It does not change the verdict, because case (b) crashes either way.

---

## Raw dumps (this session)

| file | contents |
|---|---|
| `analysis/ghidra-camp-01-literals-makestageinst.txt` | 5 literals in `0xb33f84:0xb35400`: `'[ERR] [%s] '`, `'Cannot find Mission Information'`, `'MakeStageInst'`, **`'001'`**, **`'003'`** |
| `analysis/ghidra-camp-02-insn-full-makestageinst.txt` | full instruction listing of `MakeStageInst` (`0xb33f84`–`0xb35196`), 1645 instructions — the primary evidence for every instruction citation |
| `analysis/ghidra-camp-03-callers-addstagemonster.txt` | `AddStageMonster` callers: only `0xb4612c ReqTargetStageMonsterCB` |
| `analysis/ghidra-camp-04-decomp-addstagemonster.txt` | `CSRGameMob::AddStageMonster` `0xa0d194`, full |
| `analysis/ghidra-camp-05-fns-gamemob.txt` | function map `0xa0b000…0xa0d400` — enumerates the whole `CSRGameMob` block |
| `analysis/ghidra-camp-06-literals-addstagemonster.txt` | `AddStageMonster` literals: `_id`, `wave_list`, `ref_id`, `group`, `next_spawn_ms`, `show_thumbnail` |
| `analysis/ghidra-camp-07-literals-getlink.txt` | `GetStageMonsterLinkData` literals: `'map::at:  key not found'` |
| `analysis/ghidra-camp-08-literals-reqtargetcb.txt` | `ReqTargetStageMonsterCB` literals: `'ret_data'`, `'0'` |
| `analysis/ghidra-camp-09-insn-emplace.txt` | instructions of `__emplace_unique_key_args<CMHashID,…>` `0x00904604` — **the proof of the entry layout that explains `r1 == 0`** |
| `analysis/ghidra-camp-10-decomp-getwavedata.txt` | `CSRGameMob::GetStageWaveData` `0xa0d088`, full |
| `analysis/ghidra-camp-11-callers-getwavedata.txt` | `GetStageWaveData` has **no callers** |
| `analysis/ghidra-camp-12-fns-gamemob2.txt` | function map `0xa0a000…0xa0b100` (negative result: no `CSRGameMob` writer of `+0x18`/`+0x24` there) |
| `analysis/ghidra-camp-13-callers-makestageinst.txt` | negative result: no static call edge into `0xb33f84` |
| `analysis/ghidra-camp-14-callers-initbeforeopen.txt` | negative result: no static call edge into `0xb33ccc` |
| `analysis/ghidra-camp-16-bytes-vs-listing.txt` | `IMAGE_BASE 00010000` + program bytes vs mnemonic for 10 addresses incl. the fault site (new script `analysis/ghidra-scripts/InspectInstructions.java`) |
| `analysis/ghidra-camp-17-insn-csrmstage-block.txt` | instruction listing of `0xb33000…0xb37200` (the whole `CSRMStage` block) — grep shows exactly two `#0x264` sites, both in `MakeStageInst` |

Headless runs: `analysis/ghidra-camp-run-01.log` … `-04.log`.

New script added (additive, per ownership): `analysis/ghidra-scripts/InspectInstructions.java` —
prints program bytes, length and mnemonic side by side for a list of addresses. It exists
because a hand re-decode disagreed with Ghidra and the disagreement had to be attributable.