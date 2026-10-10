# `ReqGroupRankUpCB` + `RequestGroupRankUp` + `RequestSellCard` + `ParseSellCard` body audit — 2026-10-05

**Lane:** close out the four remaining unaudited bodies listed in
`analysis/research/base-stats-visual-hunt/batch-rankup-chucoin-2026-10-05.md`
§1.3 (rule 8 `/gym/RankUpBundle` and rule 9 `/shop/SellCard`).

**Read-only compliance.** No Ghidra project was opened or written (it is
parent-owned/locked). Only pre-existing tables plus the read-only
`analysis/extracted/lib/armeabi-v7a/libnative_core.so` were read. No server,
APK, state or account change; no implementation. Helper scripts were written to
the OS temp dir, **not** to the workspace, so this file is the only artefact in
`analysis/research/base-stats-visual-hunt/` produced this run.

**Coverage:** unchanged — heroes **1/113**, accessories **1/100**, monsters
**0/22**. Nothing below is a hero/item/monster base statistic.

**Address convention:** `0x00xxxxxx` = Ghidra image address (= ELF + `0x10000`);
`0x01dxxxxx` = `.rodata` literal address. All code ranges were confirmed Thumb-1
(each entry point begins `push {r4-r7,lr}` = `0xb5f0`), so the literal idiom is
`ldr rN,[pc,#imm]` + `add rN,pc`.

> ### ⚠️ CONVENTION CORRECTION 2026-10-05 — the `0x01dxxxxx` literal column is **Ghidra**, not ELF
>
> The line above left the literal column **unlabelled**, and
> [`resolver-hardening-2026-10-05.md`](resolver-hardening-2026-10-05.md) §1.1
> recorded that it had been *read* as ELF VA. **It is Ghidra image addresses
> (= ELF VA + `0x10000`), exactly like the code column.** Measured: **36/36**
> literal↔address pairs in this file match byte-exactly at `address − 0x10000`
> and **0/36** at the address as printed. Spot proofs:
>
> | literal | as printed here | ELF VA / file offset | bytes there |
> |---|---|---|---|
> | `/gym/RankUpBundle` | `0x01d8f7d4` | `0x01d7f7d4` | `b'/gym/RankUpBundle\x00part\x00car'` |
> | `src_rank` | `0x01d8f7cb` | `0x01d7f7cb` | `b'src_rank\x00/gym/RankUpBundle'` |
> | `inst_id_list` | `0x01d78609` | `0x01d68609` | `b'inst_id_list\x00/gem/Sell\x00max'` |
> | `removed_inst_id_list` | `0x01d8f8b7` | `0x01d7f8b7` | `b'removed_inst_id_list\x00/aren'` |
> | `target_list` | `0x01d6a771` | `0x01d5a771` | `b'target_list\x00/message/Read\x00'` |
>
> So the corrected statement is:
> **`0x00xxxxxx` = Ghidra image address; `0x01dxxxxx` = Ghidra image address of a
> `.rodata` literal. Both columns are ELF VA + `0x10000`.** To read the bytes,
> subtract `0x10000` (these literals are all in the first `PT_LOAD`, where
> `p_vaddr == p_offset`, so no further mapping is needed).
>
> The table values in §1.1–§1.4 are **left exactly as printed** — they were always
> correct *as Ghidra addresses* and all of them are copied straight from
> `analysis/native-all-strings.tsv`, which uses that convention. What was wrong was
> the note, not the numbers.
>
> Definitive table: [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md).

---

## 1. PURE — recovered literals, keys, structure

### 1.0 Method, controls, and one false positive caught

Per `analysis/systems/gym.md` §4 the four ranges were scanned with the hardened
`tools/resolve-literals-offline.py`. Before trusting any of it, the tool was
re-validated against the known-good dump, as `AGENTS.md` §16.7 requires:

```
python tools/resolve-literals-offline.py --from-dump analysis/ghidra-wave-keys.txt
  -> resolved: 7   _id / ref_id / group / next_spawn_ms / show_thumbnail / ret_data / "0"
```

**7/7, strings identical to the dump.** The tool is trustworthy for this library.

Two deliberate controls were added on top, because the hardened tool's
contiguity rule (`ldr` must be the *immediately* preceding instruction of the
`add <Rn>,pc`) is a documented false-negative source:

* **Capstone pass** — `tools/disasm-literals.py` (independent implementation,
  looser `+1..+3` window) over the same ranges.
* **Exhaustive pc-load pass** — every `ldr [pc,#imm]` in range whose slot word
  points at a printable C string, with **no** contiguity requirement.

Agreement: the two passes found a strict subset of the hardened tool's hits, plus
**four** extra real keys the hardened tool missed (§1.1 `otp`, §1.4 `cur`,
`inst_id`). All three passes agree on every shared key.

**False positive caught and excluded.** The hardened tool also reported one hit
it should not have:

| site | reported | actual |
|---|---|---|
| `0x00f589e6` (in `RequestGroupRankUp`) | `'X'` @ `0x021bebb4` | **not a string** — a load of a global **pointer** at `0x021bebb6`, 2 bytes past where a printable byte happens to sit |

> ⚠️ **`0x021bebb4` in this row is the old tool's BIASED PRINT, not an ELF VA**
> (annotated 2026-10-05; see
> [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md) §5 and
> [`c4-row-census-2026-10-05.md`](c4-row-census-2026-10-05.md) §5.2). The correct
> ELF VA is **`0x021aebb4`**, in `.got` (`0x021aafe4`–`0x021b3000`), whose two words
> are `0x00f48da1` and `0x01e7a185` — odd Thumb targets in R-X, the relocated
> code-pointer pair. Byte-verified this pass:
>
> | reading | file offset | bytes |
> |---|---|---|
> | `0x021aebb4` (ELF VA; RW- ⇒ `p_offset = p_vaddr − 0x1000`) | `0x021adbb4` | `\xa1\x8d\xf4\x00\x85\xa1\xe7\x01…` — the pointer pair |
> | `0x021bebb4` (ELF VA) | `0x021bdbb4` | all zeros — **not** the documented target |
> | naive `− 0x10000` of the tool's `0x021bebb4` print | `0x021aebb4` | `X\x00\x1c\x02\xf8\x01…` — the phantom `'X'` |
>
> **The verdict of this section is unaffected.** Both `0x021aebb4` and
> `0x021bebb4` lie in the RW- segment `0x0210e550–0x028bc790`, so the
> segment-classification argument below holds either way. The value is left
> exactly as printed, per this folder's "correct the note, not the numbers"
> policy; only its coordinate space needed saying. The identical value was
> already annotated in `resolver-hardening-2026-10-05.md` §1.4-D1 and §2.1.
>
> Correction to the folder's audit trail: `address-convention-2026-10-05.md` §6.1
> item 4 states this §1.0 row "was corrected" to `0x021aebb4`. **It had not been** —
> the two lines below still printed `0x021bebb4` unannotated. Now fixed.

Proof by ELF `PT_LOAD` classification: every genuine literal above
(`/gym/RankUpBundle` `0x01d8f7d4`, `inst_id_list` `0x01d78609`, `target_list`
`0x01d6a771`, `removed_inst_id_list` `0x01d8f8b7`) lies in the **R-X** segment
`0x00000000–0x0210d320`; the `'X'` target `0x021bebb4` lies in the **RW-**
segment `0x0210e550–0x028bc790`. (`0x021aebb4`, the corrected ELF VA, is in that
same RW- range — see the note above; the conclusion does not change.)
**Tooling implication for the parent:** the
resolver's acceptance test is printable-ASCII, which is not sufficient — a
segment check (target inside an R-X/R-- load) would close this class of false
positive. Do not widen any window before adding it.

### 1.1 `CSRSyncCard::RequestGroupRankUp` (`0x00f586e4`–`0x00f58da0`) — **all 5 request fields recovered**

Signature `RequestGroupRankUpEjjjjj` = `this` + **five uints** +
`const std::function<void(int)>&`. Field names and their argument sources:

| field | `.rodata` | load site | literal slot | value source |
|---|---|---|---|---|
| `app_code` | `0x01d689d0` | `0x00f58718` | `0x00f58a9c` | global inline string |
| `app_ver` | `0x01d689d9` | `0x00f58742` | `0x00f58aa0` | global inline string |
| `market` | `0x01d689ee` | `0x00f58760` | `0x00f58aa4` | `to_string(PV_MARKET)` (`0x007c2790`) — **global, not a parameter** |
| `pvid` | `0x01d686aa` | `0x00f5878e` | `0x00f58aa8` | `CPVDataMgr::get()` → `+0x58` (`0x007e15dc`, `0x001bd5164`) — **the account's own pvid, not a parameter** |
| `otp` | `0x01d689ea` | `0x00f587ba` | `0x00f58aac` | `CPVDataMgr::GetOTP()` (`0x007e103e`) |
| **`src_rank`** | `0x01d8f7cb` | `0x00f58872` | `0x00f58ab4` | uint argument **#1** (`r1`→`sl`) |
| **`src_cnt`** | `0x01d6feba` | `0x00f5884a` | `0x00f58ab0` | uint argument **#2** (`r2`→`fp`) |
| **`target_rank`** | `0x01d6fe55` | `0x00f588c2` | `0x00f58abc` | uint argument **#3** (`r3`→`sb`) |
| **`target_cnt`** | `0x01d6f8f6` | `0x00f5889a` | `0x00f58ab8` | uint argument **#4** (incoming stack word 0) |
| **`price`** | `0x01d6aa71` | `0x00f588ea` | `0x00f58ac0` | uint argument **#5** (incoming stack word 1) |
| route | `0x01d8f7d4` | `0x00f589d4` | `0x00f58ac4` | `/gym/RankUpBundle` |

Frame arithmetic behind the two stack reads: `r7 = sp_entry − 8` (set at
`0x00f586e6` by `add r7,sp,#0xc`, *before* the `push.w {r8,sb,sl,fp}`), so
`[r7,#8] = sp_entry` and `[r7,#0xc] = sp_entry+4` are incoming stack words 0 and
1 — i.e. uints #4 and #5, with the `std::function` reference following at
`sp_entry+8`. All five string conversions go through the same helper
`0x001bd50dc` (uint → `std::string`). **`src_rank`, `src_cnt`, `target_rank`,
`target_cnt` and `price` are one-to-one with the five uints — no leftover
parameter.**

This **promotes `src_rank` from an adjacency candidate to [RECOVERED]**.
`batch-rankup-chucoin-2026-10-05.md` §1.1 point 3 called it a candidate only
because the pairing had never been run; it now is, and the other three
candidates (`target_rank`, `target_cnt`, plus the previously unlisted `price`)
are recovered with it. `price` was not in `gym.md` §4's candidate list at all.

Transport: `CPVHTTPRequest::Create<...>` (`0x007c9d60`) with
`CPVHTTPMapToEncodedURLFormTransformer` and a
`std::unordered_map<std::string, std::string>` (`0x0074f7e4`, 10 entries =
`movs r2,#0xa`), then `CPVHTTPManager::Enqueue` (`0x007e61dc`). **Every field is
a string-valued URL-form pair**, so all five uints are serialised as decimal
text. `RequestSellCard` uses the identical transport.

`this` argument #0 (`r0`, spilled to `sp+0x14`, `0x00f586ee`) is **not** a form
field: its only read is `0x00f589e8`, where it is stored into `sp+0xb0` beside a
global pointer — i.e. captured into the completion context.

### 1.2 `CSRSyncCard::ReqGroupRankUpCB` (`0x00f58da0`–`0x00f59380`) — **response shape recovered**

`this` in `r0`, `const std::function<void(int)>&` in `r1`, an `int` in `r2`,
`CPVHTTPRequest const*` in `r3`, `CPVHTTPResponse const*` in incoming stack word
0 (`ldr r4,[r7,#8]`, `0x00f58db0`). All `json` navigation is
`nlohmann::json::operator[](char const*) const&` = **`0x007930f8`**, and numeric
extraction is `FUN_01be3550` / `strtod` (`0x00621b48`) type-tag dispatch.

| key | `.rodata` | load site | literal slot | consumer |
|---|---|---|---|---|
| `result_code` | `0x01d6898e` | `0x00f58e10` | `0x00f590ec` | read as int; `cmp #1`, `bne 0x00f59288` → **native success is `1`** |
| `ret_data` | `0x01d689bb` | `0x00f58e6e` | `0x00f590f0` | response container (root of everything below) |
| `achievement` | `0x01d6ee96` | `0x00f58e78` | `0x00f590f4` | **null-guarded** (`ldrb`+`cbz`, `0x00f58e84`) → `CSRAchieve::ParseAchievementsElement` (`0x008481c4`) + `CSRAchieve::ParseLobbyEnter` (`0x00844918`) |
| `user` | `0x01d6ef58` | `0x00f58e9c` | `0x00f590f8` | **null-guarded** (`0x00f58ea6`–`0x00f58ea8`) |
| `gold` | `0x01d6edd6` | `0x00f58eaa` | `0x00f590fc` | `user.gold` |
| `cur` | `0x01d6eea2` | `0x00f58eb2` | `0x00f59100` | `→ str.w r5,[r0,#0x154]` where `r0 = CSRDataMgr::GetPlayData()` → **`PlayData+0x154`, absolute uint32** |
| `card` | `0x01d6eed7` | `0x00f58f08` | `0x00f59104` | cached to `sp+0x24`; **parent of both lists below** |
| `removed_inst_id_list` | `0x01d8f8b7` | `0x00f58f12` | `0x00f59108` | `card.removed_inst_id_list[]`, `operator[](size_t)` = `0x00721268`, each element → uint64 → **`CSRInventory::RemoveCard` (`0x00aebc44`)** with a constant `1` |
| `target_list` | `0x01d6a771` | `0x00f59008` | `0x00f5910c` | `card.target_list[]`, must be a non-empty array (type check `0x00f59014`–`0x00f5903c`, empty → callback with `r5=1`) |
| `inst_id` | `0x01d6eec9` | `0x00f59046` | `0x00f59364` | per element → uint64 |
| `rank` | `0x01d6fa90` | `0x00f5904c` | `0x00f59368` | `element.rank` (an **object**, not a number) |
| `cur` | `0x01d6eea2` | `0x00f59052` | `0x00f5936c` | `element.rank.cur` |
| `rank_up_cnt` | `0x01d6fa95` | `0x00f59140` | `0x00f59370` | `element.rank_up_cnt` (object) |
| `cur` | `0x01d6eea2` | `0x00f5914a` | `0x00f59374` | `element.rank_up_cnt.cur` |
| `exp` | `0x01d6ede1` | `0x00f59194` | `0x00f59378` | `element.exp` (object) |
| `cur` | `0x01d6eea2` | `0x00f5919e` | `0x00f5937c` | `element.exp.cur` |

Structural facts that constrain any future fixture (all **[RECOVERED]**):

1. **Nesting is `ret_data.card.*`, not `ret_data.*`.** `ret_data["card"]` is
   fetched once (`0x00f58f08`, cached `sp+0x24`) and *both* `removed_inst_id_list`
   and `target_list` are looked up on that node (`0x00f58f12` and `0x00f59008`
   both reload `sp+0x24`). A flat `ret_data.target_list` would never be read.
2. **Three of the four numeric payloads are `{cur}` objects, and there is no
   `prev` anywhere in this callback.** This is a *different* contract from the
   single `/gym/RankUp` path (`analysis/research/rank-up-contract.md`), which
   parses `rank`/`rank_up_cnt`/`exp` **prev/cur pairs** and `user.gold prev/cur`.
   Here each is a single nested `cur`, and `user.gold` is written as one absolute
   `uint32` at `PlayData+0x154`.
3. **`removed_inst_id_list` is consumed by the client, not by `SetCardRank`.**
   It is the only thing that erases inventory on this path
   (`CSRInventory::RemoveCard`, `0x00aebc44`), so an omission leaves consumed
   fodder visible client-side.
4. **`target_list[]` drives `CSRInventory::SetCardRank` (`0x00ae9c78`,
   called once per element at `0x00f5922e`)**, with `this` from
   `PlayData+0x11c`. The callee prologue (`0x00ae9c78`–`0x00ae9c9c`) takes `this`
   in `r0`, a 64-bit value in `r2:r3` and two incoming stack words, matching the
   `SetCardRank(unsigned long, unsigned, unsigned, unsigned)` demangle against the
   four recovered values (`inst_id`, `rank.cur`, `rank_up_cnt.cur`, `exp.cur`),
   which are read in exactly that order. (Per-slot AAPCS assignment is *inferred*
   from read order + the callee's `r7`-relative stack reads, not decompiled.)
5. **A missing or non-numeric `.cur` degrades to `0`, it does not throw.** Every numeric
   conversion has a `movs rX,#0` default arm (`0x00f59114`, `0x00f59168`,
   `0x00f591c6`, `0x00f5926c`), reached through the `tbb` type dispatch on
   `tag−3`. So `card.target_list[0] = {}` produces `SetCardRank(id, 0, 0, 0)`
   rather than a crash.
6. **Callback invocation** (`0x00f59288`–`0x00f59296`): `r0 = std::function`,
   `r1 = &int`, `blx invoker`. Exactly **one** int is materialised, and it is
   the **result code** (`r5`, forced to `1` on the success path at
   `0x00f5926c`). A non-zero `r2` argument short-circuits at `0x00f58dc2`
   (`cbnz r5`) and invokes the callback with that value without parsing.
7. **Zero direct `bl` callers.** A whole-`.text` scan for `bl`/`blx` targets
   equal to `0x00f58da0` returns **0** hits, so `ReqGroupRankUpCB` is reached
   *indirectly* (through its `std::function` thunk), not from
   `RequestGroupRankUp`. Consistent with the `void(int)` sink below.

### 1.3 `CSRSyncShop::RequestSellCard` (`0x00f8df98`–`0x00f8ed98`) — **request field recovered**

| key | `.rodata` | load site | slot | value |
|---|---|---|---|---|
| `app_code` / `app_ver` / `market` / `pvid` / `otp` | `0x01d689d0` / `…d9` / `…ee` / `0x01d686aa` / `0x01d689ea` | `0x00f8e024` / `0x00f8e04e` / `0x00f8e06c` / `0x00f8e09a` / **`0x00f8e0ca`** | `0x00f8e320`…`0x00f8e330` | same globals as §1.1 |
| **`inst_id_list`** | **`0x01d78609`** | `0x00f8e1dc` | `0x00f8e334` | **JSON-array-encoded string** |
| route | `0x01d9030a` | `0x00f8e358` | `0x00f8e6a8` | `/shop/SellCard` |

**`inst_id_list` encoding — [RECOVERED].** The input
`vector<uint64> const&` is walked at stride 8 (`ldrd r0,r1,[r5]` …
`adds r5,#8`, loop `0x00f8dfe6`–`0x00f8e00c`); each 64-bit element is built
into a `json` slot (`strd r0,r1,[sp,#0xc8]`) and appended with
`nlohmann::json::push_back(json&&)` (**`0x00720f14`**, at `0x00f8dffa`), i.e.
**numbers, not strings**. The array is then serialised with
`nlohmann::json::dump()` (**`0x0071f754`**, at `0x00f8e1d8`) into a
`std::string`, which is stored under the key `inst_id_list`
(`basic_string(const char*)` `0x006d5ff4` at `0x00f8e1e4`, request member
`r4+0x78`). So the wire form is
`inst_id_list=%5B1%2C2%5D`-style — **a JSON array serialised into a single form
string**, the same family as `id_list` on `supply/SpecialListReward`
(`AGENTS.md` §90) and `target_inst_id` (§45/§33). It is **not** a comma-joined
bare list like `/message/RemoveReceived`'s `target_list` (§88).

`otp` at `0x00f8e0ca` is another hardened-tool **false negative**: the `ldr` is
at +6 from its `add r1,pc` (intervening `add r4,r4,#8`), not immediately
preceding.

### 1.4 `CSRSyncShop::ParseSellCard` (`0x00f8ed98`–`0x00f8f1ac`) — **reward shape recovered**

`arg0 = vector<uint64> const&` (saved `r0`, restored at `0x00f8f040`), `arg1 =
json const&` (the response **envelope**, `mov r5,r1`). Exactly **one** direct
`bl` caller exists library-wide, at **`0x00f905f4`** (inside a function with no
retained dynsym symbol; nearest exported neighbours are nlohmann `__tree`
helpers at `0x00f8fd54` / `0x00f8ff02`).

| key | `.rodata` | load site | slot | consumer |
|---|---|---|---|---|
| `ret_data` | `0x01d689bb` | `0x00f8edb2` | `0x00f8f0d8` | type-tag checked (`cmp #0` → `beq 0x00f8f0b8`): **absent/null is tolerated** |
| `user` | `0x01d6ef58` | `0x00f8edc6` | `0x00f8f0dc` | **null-guarded** (`cbz`, `0x00f8edd2`) |
| `gold` | `0x01d6edd6` | `0x00f8edd4` | `0x00f8f0e0` | **null-guarded** (`cbz`, `0x00f8ede0`) |
| `cur` | `0x01d6eea2` | **`0x00f8edea`** | `0x00f8f0e4` | `→ str.w r0,[r8,#0x154]` = **`PlayData+0x154`, absolute uint32** — identical sink to §1.2 |
| `item` | `0x01d6eec4` | `0x00f8ee3c` | `0x00f8f160` | `ret_data.item[]`, null-guarded (`beq 0x00f8f044`); iterated with `iter_impl` `operator!=` (`0x0072af38`) and `operator*` (`0x0072aff0`) |
| `inst_id` | `0x01d6eec9` | **`0x00f8eeb8`** | `0x00f8f164` | per row → uint64 |
| `ref_id` | `0x01d6edf2` | `0x00f8eec4` | `0x00f8f168` | per row → **`std::string`** via `detail::from_json<string_t>` (`0x00728b08`) |
| `added` | `0x01d6eed1` | `0x00f8eeca` | `0x00f8f16c` | per row → uint32 |

Two sinks, in this order:

1. **`CSRInventory::AddItem`** (`0x00aec508`, called at `0x00f8efca`) with
   `(inst_id, ref_id, added)` — `r0 = PlayData+0x11c`, `r2:r3 = inst_id`,
   `r1 = &ref_id string`, `[sp] = added`
   (`strd r1,r4,[sp]`, `0x00f8efc6`). Demangle
   `AddItem(unsigned long, std::string const&, unsigned int)` matches.
2. **`CSRInventory::RemoveCard`** (`0x00aebc44`, called at `0x00f8f084`) once per
   id of **`arg0`** — the sold-id vector, walked as `ldrd r4,r6,[r5]` /
   `adds r4,#8` — with a constant `1`.

**Consequences (pure, and they change what a fixture must contain):**

* **The hunter-release reward arrives as ITEM rows, not as a coin count.**
  `ret_data.item[]{inst_id, ref_id, added}` is the only path into
  `AddItem` on this route. There is **no** literal, key or setter anywhere in this
  body for a Chu-coin / `coin`-style currency. This is the closest thing to a
  native answer `batch-rankup-chucoin-2026-10-05.md` §1.2.1 asked for, and it is
  a *negative* for the coin hypothesis: the client cannot display a coin total it
  has no field for.
* **The removal list is NOT read from the response.** It is taken from the vector
  the caller passed in, so a server response needs no "sold"/"removed" key —
  the client already knows what it asked to release. (Contrast §1.2, where
  `removed_inst_id_list` *is* a response key.)
* **`ret_data.user.gold.cur` is optional and absolute.** Both `user` and `gold`
  are null-guarded, and only `cur` is read — no `prev`, no `free_iap`/`iap`
  keys. This matches the Arena/`SyncUser` absolute-wallet pattern (`AGENTS.md`
  §122) rather than the `prev`/`cur` pair style.
* **Guards are asymmetric:** `ret_data`, `user`, `gold` and `item` are all
  checked; a non-object, non-null `ret_data` (e.g. an array) would still reach
  `operator[]` at `0x00f8edca`, so `ret_data` must be an object or absent.

### 1.5 Corrections to existing documentation (read-only — not edited here)

1. **`/gym/RankUpBundle`'s callback sink is `void(int)`, not `void(int,int,int)`.**
   Demangled type on both symbols is
   `_ZN11CSRSyncCard18RequestGroupRankUpEjjjjjRKNSt6__ndk18functionIFviEEE` /
   `…16ReqGroupRankUpCBERKNSt6__ndk18functionIFviEEE`. In Itanium mangling
   `IFviE` = `void(int)`; `void(int,int,int)` would be `IFviiE`. Cross-check
   inside the same library: `CPVAccount::RequestConfirmNickname` and
   `CPVPurchase::RequestIAPInfo` use the identical `IFviEEE`, and their
   `__function::__func<…FviSB_SE_EE…>::operator()` mangling is unambiguously
   `void(int, shared_ptr&, shared_ptr&)` — so `F v i E` = one `int` parameter.
   The same `function<void(int)>` sink is used by `RequestShopReset`,
   `RequestSellItem`, `RequestBuyItem`, `RequestShopRefresh` and
   `ReqOvercomeCB`. Runtime evidence agrees: exactly one int is materialised at
   the invoke site and it is the result code (§1.2 point 6).
   **Affected:** `analysis/systems/gym.md:97` and
   `batch-rankup-chucoin-2026-10-05.md` §1.1 (row "callback sink" and structural
   consequence 1, which argued the batch path has "no PARAM struct" — the
   *conclusion* survives, the type does not).
2. **`gym.md` §3/§4 statuses that this run promotes.** `src_rank` @
   `01d8f7cb` is now **[RECOVERED]** as a `/gym/RankUpBundle` request field, not
   adjacency; `target_rank` (`0x01d6fe55`), `target_cnt` (`0x01d6f8f6`) and
   `price` (`0x01d6aa71`) join it. `gym.md` §0's "request field names recovered:
   6 (adjacency only)" is now 6 register-matched + 5 more on this route.
3. **`inst_id_list` (`0x01d78609`) was absent from every route table consulted**
   by `batch-rankup-chucoin-2026-10-05.md` §1.2. It is now recovered, together
   with its JSON-array-in-a-string encoding.

### 1.6 Explicit negatives (searched, not found)

* **No `prev` key** anywhere in `ReqGroupRankUpCB` or `ParseSellCard`.
* **No `coin` / `chu` / `secret` / `market` key** in any of the four bodies — the
  §1.2.2 and §1.2.3 negatives of the earlier report are **confirmed** by direct
  body audit rather than table search.
* **No `removed_card`, `removed_inst_list`, `target_inst`, `skill_%u_level`,
  `card_list`, `item_list` or `detection` key** on either path. The batch
  rank-up path uses `card.removed_inst_id_list` + `card.target_list[]` instead of
  the single-path `target_inst` / `removed_inst_list` / `removed_card` family.
* **No `detect` / achievement-progress key** beyond the single optional
  `ret_data.achievement` handled by `CSRAchieve`.
* **No `inst_id` in the SellCard request** other than inside the
  `inst_id_list` array; no per-instance field names.
* **No response key on the requester side of either route** (expected: requesters
  only write form fields).

### 1.7 Limits of this pass

* Instruction-level audit only. **No decompilation** was performed (Ghidra is
  parent-owned), so per-slot AAPCS argument assignment inside
  `SetCardRank`/`RemoveCard`/`AddItem` is *inferred* from read order plus the
  callee prologues, and control-flow reconstruction inside `tbb` type-dispatch
  tables is partial (the tables themselves decode as garbage instructions, which
  is why the exhaustive pass is **not** exhaustive past the first `tbb`).
* Whether an exception thrown by `operator[]` is caught is **not established**.
  Both callbacks contain landing-pad blocks and `__stack_chk_fail`
  (`0x00621adc`), but the handler set was not audited.
* `ParseSellCard`'s single caller at `0x00f905f4` could not be named (no dynsym
  symbol covers it), so the identity of whoever supplies the sold-id vector is
  **unknown**.
* `RequestGroupRankUpCB`'s indirect call path (which thunk invokes it) is
  **untraced**; only the absence of direct `bl` targets is established.
* Request-side *values* are globals, not parameters — a server that expects
  different `pvid`/`market`/`otp` semantics is not contradicted by this audit,
  but nothing here pins the original envelope values beyond the keys.

---

## 2. UNPURE — numeric tokens (impure rebalance/context only, **no coverage credit**)

This audit recovered **no** hero, accessory or monster statistic. Every numeral
touched is protocol or code-level. Per the output rule they are all recorded here
as impure.

| Token | Value | Where | Meaning | Status |
|---|---|---|---|---|
| native success code | `1` | `0x00f58dc4` (`cmp r0,#1`), `0x00f5926c` (`movs r5,#1`) | `result_code` accepted value; also the value handed to the `void(int)` sink | [RECOVERED] protocol constant, **not** an economy value |
| removal flag | `1` | `0x00f58f58`/`0x00f58fcc` (`fp`), `0x00f8f04c`/`0x00f8f080` (`r8`) | constant written to the outgoing-arg area before `CSRInventory::RemoveCard` | [RECOVERED] code constant; exact parameter slot not pinned (§1.7) |
| REQ_METHOD | `2` | `0x00f589dc` (`movs r3,#2`) | argument to `CPVHTTPRequest::Create` | [RECOVERED] transport constant |
| form-field count | `10` (`0xa`) | `0x00f58910` (`movs r2,#0xa`) | `unordered_map` `initializer_list` of 10 string members | [RECOVERED] layout constant |
| json iterator sentinel | `-0x80000000` | `0x00f8ee4e`, `0x00f8ee7a` | nlohmann "end of object/array" marker | [RECOVERED] library constant |
| `PlayData` gold offset | `0x154` | `0x00f58f04`, `0x00f8ee38` | absolute gold wallet field | [RECOVERED] struct offset |
| `PlayData` inventory offset | `0x11c` | `0x00f58f6c`, `0x00f5920a`, `0x00f8efaa`, `0x00f8f062` | `CSRInventory*` handle used by all three sinks | [RECOVERED] struct offset |
| `CSRInventory` member probed by `RemoveCard`/`SetCardRank` | `0x74` | `0x00aebc5c`, `0x00ae9c9e` | hashed container length/capacity | [RECOVERED] offset |
| hash constant | `0x5bd1e995` | `0x00aebc62`–`0x00aebc68`, `0x00ae9ca6`–`0x00ae9cae` | MurmurHash3 finalizer constant | [RECOVERED] library constant |

Carried-forward economy tokens whose *mechanism* this audit constrains but whose
**amounts remain unproven** — restated from
`batch-rankup-chucoin-2026-10-05.md` §2, unchanged, with the new native status:

| Token | Value | Source | Native status **after** this audit |
|---|---|---|---|
| ★3 release yield | 8 Chu-coins | blustone.jp rank-up guide (POST 2019-11-13) | **Still no native key.** `ParseSellCard`'s only reward sink is `AddItem(inst_id, ref_id, added)` (§1.4) — the client has no field for a coin total. Do not implement a coin credit. |
| Trainer price | 4 coins/trainer via Secret Market | same | **Still no route and no key** in the four bodies. |
| Batch rank-up scope | ★1–★2 without max level | same | Route + **all five request fields** now recovered (§1.1), so the request is expressible; the response shape is recovered (§1.2) but **no client-side eligibility predicate** was found, so the "without max level" claim still has no mapped native check. |
| Rank-up preview prices | 8000 / 12000 (PRE 2018-12) | Caragublu screenshot | No price **parser** on either path; `price` is a client→server field, not a receipt (§1.1). Amounts remain visual-only. |
| Rank-up value pairs | 7,092→11,277; 1,417→2,389 | 2017 screenshots | Unrelated to these bodies; polluted progression only. |
| Local fixtures | 1000 gold/source rank-up; 100 gold/source raise | `server-ts` policy | Unchanged; mechanism partly recovered, amounts still fixture. |

Do not promote any row above into a server default or a "recovered price".

---

## 3. Files and coverage

* **This file (new):** `analysis/research/base-stats-visual-hunt/grouprankup-sellcard-bodies-2026-10-05.md`.
* `polluted-observations.md`: **deliberately NOT appended** — the parent will
  mirror §2, to avoid the concurrent-write incident.
* `analysis/systems/gym.md` and
  `batch-rankup-chucoin-2026-10-05.md`: **not edited** (read-only brief). The
  corrections and promotions they need are listed in §1.5 for the parent to apply.
* Helper scripts used for this audit live in the OS temp directory, not in the
  workspace. The original `libnative_core.so` was opened read-only and is
  unmodified; the Ghidra project was never opened.
* **Coverage unchanged:** heroes 1/113, accessories 1/100, monsters 0/22.