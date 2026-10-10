# Gem LevelUp action schema — 2026-10-05

**Lane:** BLUSTONE gem (jewel) polish-transaction wire schema (`/gem/LevelUp`).
**Status:** research only. Read-only native evidence; no server/APK changes, no
implementation, no new strict coverage credit (heroes 1/113, accessories 1/100,
monsters 0/22, jewel samples unchanged).
**Parent gap:** [`gem-polish-parsers-2026-10-05.md`](gem-polish-parsers-2026-10-05.md)
§1.6 (action symbols identified; request/response fields NOT recovered) +
`analysis/research/gem-reference-contract.md`.
**Impure ledger:** [`polluted-observations.md`](polluted-observations.md)
("Gem LevelUp action pass") — §2 below is duplicated there.

**Output rule for this file:** Section 1 is PURE (symbol/signature structure with
addresses, field-identity TYPES only where proved — no price, possibility, or
compensation AMOUNTS asserted). Section 2 is UNPURE (every cost/probability
numeral encountered, each marked impure; none counts toward any 70% threshold).

Code coordinates are **Ghidra addresses (ELF VA + 0x10000)** unless marked otherwise.
**Address-convention correction 2026-10-05:** this file previously said the 8-hex
keys in `analysis/native-all-strings.tsv` "are file-order tokens, NOT virtual
addresses". **That was wrong on both counts** — they *are* virtual addresses, and
they are in the **Ghidra image space**. The file's own example proves it:
`0024dea0` is the row

```
0024dea0  _ZN6CSRGem17RequestGemLevelUpEyjRKNSt6__ndk18functionIFvR…EEEEE
```

and that mangled name sits at **ELF VA `0x0023dea0`** (subtract `0x10000`), in
`.dynstr` (`0x000c4f20`–`0x0044af44`), which is in the first `PT_LOAD` where
`p_vaddr == p_offset`. So `0024dea0` is a *Ghidra* address of a *virtual* address.
`analysis/native-evidence.tsv` uses the **same** convention, not a different one.
See [`address-convention-2026-10-05.md`](address-convention-2026-10-05.md).
**Do not add `0x10000`** to either table's column — it is already applied.

---

## 1. PURE — action-side findings (no amounts)

### 1.1 Route + symbol inventory

| Symbol | Ghidra addr (`native-evidence.tsv`) | strings.tsv key + line | Decoded signature (Itanium, pure) |
|---|---|---|---|
| `/gem/LevelUp` route literal | — (string literal, not code) | `01d7862a`, l.443393 | route posted by `RequestGemLevelUp` |
| `CSRGem::RequestGemLevelUp` | **00a5811c** (l.12996) | `0024dea0`, l.21699 | `(uint64, uint32, cb)` — callback is raw triple `void(shared_ptr<CPVHTTPRequest> const&, CPVHTTPResponse const&, pair<int,int>)` |
| `CSRGem::FindGemLevelUpPrice` | **00a54f00** (l.12987) | `0024dfe8`, l.21701 | `(int, PRICE_TYPE)` — price-table lookup key is (level, price_type) |
| `CSRGem::ParseGemLevelUp` | **00a5e43c** (l.13012) | `0024db16`, l.21692 | `(json const&)` — response parser, single JSON param |
| `CSRPopUpGemLevelUp::RequestGemLevelUp` | **00bd0bf4** (l.15861) | `002a6396`, l.25264 | `(uint32)` — UI-side requester, single scalar |
| `CSRPopUpGemLevelUp::UpgradeCB` | **00bd2368** (l.15868) | `002a64e1`, l.25271 | standard triple `(shared_ptr req const&, response const&, pair<int,int> const&)` |

`PVHTTP::TASK_READY` template instantiations naming `RequestGemLevelUp`
(strings.tsv ll.458123–458126) prove the request goes through the standard
`TASK_READY` JSON pipeline. They encode no key names.

Sibling action signatures, for contrast (all pure, same two sources):

| Symbol | Ghidra addr | Signature |
|---|---|---|
| `CSRGem::RequestGemSell` | 00a56ffc (evidence l.12995; strings `0024da7e` l.21691) | `(list<uint64> const&, cb)` — cb carries trailing `int`, NOT `pair<int,int>` |
| `CSRGem::ParseGemSell` | 00a5ddd8 (l.13010) | `(list<uint64> const&, json const&)` |
| `CSRGem::RequestGemEquip` | 00a557cc (l.12993; strings `0024dc8e` l.21694) | `(uint64, map<CSREquip::TYPE, list<uint64>> const&, PRICE_TYPE, cb)` |
| `CSRGem::ParseGemEquip` | 00a5c9ec (l.13006; strings `0024d765` l.21686) | `(uint64, json const&)` |

Note the callback-shape split, proved by mangling: `RequestGemLevelUp`'s
callback takes `pair<int,int>` (matching `UpgradeCB`'s third param), while
`RequestGemSell`/`RequestGemEquip` callbacks take a bare trailing `int`.
Do not invent meanings for the pair elements.

### 1.2 Structural contrasts (pure signature facts)

- The LevelUp request takes **scalars** `(uint64, uint32)`; Sell takes an ID
  **list**; Equip takes `(uint64, map, PRICE_TYPE)`. The LevelUp request has no
  list/map operand at the C++ boundary.
- The LevelUp response parser takes **JSON only** — no caller-supplied ID or
  ID-list parameter — unlike `ParseGemSell` (list) and `ParseGemEquip`
  (uint64). Whatever the response carries must therefore be self-describing
  with respect to the affected instance; the field names are still unproved
  (§1.3).
- The UI requester `CSRPopUpGemLevelUp::RequestGemLevelUp` takes a **single
  uint32**. ⚠️ **CORRECTED 2026-10-05:** its meaning is no longer open — it is
  the gem **`inst_id`**, and it is **not** a price-type selector:
  `gem-popup-bindings-2026-10-05.md` §1.6 falsified the `price_type` reading
  (`price_type` is absent from the request; `FindGemLevelUpPrice` is not called
  here; `max_tries` is an independent constant `7`).

### 1.3 NEGATIVE result — request/response wire fields NOT recovered

- **Request form keys: ⚠️ NO LONGER A NEGATIVE — now [RECOVERED],
  2026-10-05.** This bullet originally read "NOT recovered … no register-paired
  `ldr`/`ADD` literal block exists for the request body". That is superseded by
  [`gem-popup-bindings-2026-10-05.md`](gem-popup-bindings-2026-10-05.md) §1.6,
  which traced `CSRPopUpGemLevelUp::RequestGemLevelUp(uint)` (`00bd0bf4`) →
  `CSRGem::RequestGemLevelUp(uint64, uint, cb)` (`00a5811c`) through
  `CPVHTTPRequest::Create<…CPVHTTPMapToEncodedURLFormTransformer…>` (so the map
  keys *are* the form fields). **Seven keys recovered:**
  `app_code`, `app_ver`, `market`, `pvid`, `otp`, **`inst_id`**,
  **`max_tries`**, on route `/gem/LevelUp`.
  - `inst_id` = **the popup's `uint` argument** (`00bd0bf4` stores r1 to
    `[this+0x6bc]` and passes it as r2; `00a4827a` `mov r2, r11`).
  - `max_tries` = the **literal constant `7`** (`00a482d4` `movs r2,#0x7`) —
    **not** the same value, despite both being emitted from this path.
  - Also found on this path: a **client-side precondition gate** before any HTTP
    (`[this+0x7b8]+0x1c > 0xe` → bail, `00bd0c12`), a busy-flag test
    (`[this+0x65c]`), and a wallet check that Toasts the shipped KO literal
    `'루피가 부족합니다.'` (`00bd0c5a`) when funds are short.
  - **`/gem/LevelUp` response fields remain unrecovered** (see the next bullet).
    Do not build a response receipt from this.
- **Response consumed fields of `ParseGemLevelUp` (00a5e43c): NOT recovered.**
  No dump of its body; no literal block. Its envelope shape (`ret_data`
  direct vs. wrapped), mutated-instance echo, wallet receipt, and success/
  failure discrimination are all unproved.
- ~~**`UpgradeCB` (00bd2368) display bindings: unproved.** Popup helpers
  `SetBaseInfo(string const&, uint32)`, `UpgradeEvent(int,int,int)`,
  `StatusUpdate`, `SetUpgradeComment` exist as symbols (strings.tsv
  ll.25258–25265) but their call sites/operands were not traced in this pass.~~
  **[CLOSED 2026-10-05 per
  [`gem-popup-bindings-2026-10-05.md`](gem-popup-bindings-2026-10-05.md), whose
  header names this exact bullet as the pass it closes: §1.2 reachability (it is a
  `.got` function pointer reachable only through a `std::bind`), §1.3
  `UpgradeCB` 0x0bc2368 operand derivation — the third `pair<int,int>` is the
  display discriminator, fed by `FindGemInst`, and the function reads **no JSON**
  and has zero `.rodata` literals — and §1.4 `UpgradeEvent` as its inlined twin.
  So the display bindings are recovered; the popup's own response contract is not,
  and §1.3's `ParseGemLevelUp` bullet below still stands.]**
- **Why the offline resolver was NOT run:** `tools/resolve-literals-offline.py`
  is UNPROVEN with known false-key failure modes (false negatives hiding real
  keys, false positives inventing `_id`-class keys, 32-bit `BL` acceptance —
  AGENTS.md §16.7 lesson 1). Publishing resolver output as wire fields would
  reproduce exactly that failure mode. The Ghidra project is parent-owned and
  locked; no new headless dump was taken to avoid contention.

Constraining (not closing) pure facts:

- Owned-instance vocabulary includes `level_up_failed`
  (`analysis/ghidra-gem-inventory-keys.txt` l.13, `ldr@00a5d6c6`), so the client
  tracks per-jewel polish failures — increment/reset semantics unproved.
- Reference price rows (`level, price_type, price, possibility,
  failed_compensation, add_sub_ability`) and `FindGemLevelUpPrice(int,
  PRICE_TYPE)` prove the client resolves cost client-side keyed by
  (current level, price_type) before requesting.

**Explicitly unproved hypotheses — DO NOT implement from these:** ⚠️
**2026-10-05: the second one is now FALSIFIED, and the first is REFINED — see
[`gem-popup-bindings-2026-10-05.md`](gem-popup-bindings-2026-10-05.md) §1.6 and
its §3 retractions 1–2.** Original text retained:

- ~~the request `uint64` is plausibly the target gem `inst_id`~~ → **REFINED, not
  confirmed**: the popup passes a single `uint` which becomes `inst_id`, but the
  same value also flows into the popup's own `[this+0x6bc]`, and the `uint64`
  parameter is exercised as a 32-bit value only.
- ~~the request/popup `uint32` is plausibly `price_type`~~ → **RETRACTED /
  POSITIVELY FALSIFIED.** `price_type` **does not appear** as a `/gem/LevelUp`
  form field (exhaustive literal list, `gem-popup-bindings` §1.6), and
  `FindGemLevelUpPrice(int, PRICE_TYPE)` @ `00a54f00` is **not called** on this
  path. The popup's `uint` is the gem `inst_id`; `max_tries` is an independent
  constant `7`. **Any `price_type`-keyed request schema is wrong.**

The remaining, still-open items from this section are unchanged: do not publish
a **response** receipt, and do not lift the existing authenticated `/gem/*`
refusal on the basis of this section.

### 1.4 What would close it

A register-guarded `ResolvePcRelativeStrings` pass (same-register `ldr` +
immediately-following PC `ADD`, 32-bit branch rejection, verified against
known `bl operator[]` sites) over `00a5811c` (request form keys), `00a5e43c`
(response keys), and `00bd0bf4`/`00bd2368` (popup request/display keys) — or a
read-only headless decompilation of those four bodies (coordinate with the
Ghidra owner; do not contend for the lock).

---

## 2. UNPURE — cost/probability numerals (rebalance leads only, NO coverage)

**No new numeral surfaced in this pass.** No price, possibility,
failed-compensation, or success-rate value was recovered; no per-stage polish
fee, no Manda mining price, no success display binding. The impure set is
unchanged from
[`gem-polish-parsers-2026-10-05.md`](gem-polish-parsers-2026-10-05.md) §2
(removal footer 40000/40, 600k refine budget, ★4/★3 trace rates 700/350 per 8,
POST-era growth +30%/+50%, untranscribed Namu equipment tables). None counts
toward any 70% threshold. Strict coverage unchanged.
