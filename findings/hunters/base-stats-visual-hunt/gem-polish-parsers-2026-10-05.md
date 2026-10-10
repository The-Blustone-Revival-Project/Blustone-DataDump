# Gem polish-price native parsers — 2026-10-05

**Lane:** BLUSTONE gem (jewel) polish-cost native parser contract.
**Status:** research only. Read-only native evidence; no server/APK changes, no
implementation, no new strict coverage credit (heroes 1/113, accessories 1/100,
monsters 0/22, jewel samples unchanged).
**Parent gap:** [`mining-costs-2026-10-05.md`](mining-costs-2026-10-05.md) §4
(open gap: rupee polish-cost table per stage = native `GetGemLevelUpPrice` rows,
values unknown; Manda mining price unisolated; res-1 CSV is tuning not costs).
**Impure ledger:** [`polluted-observations.md`](polluted-observations.md)
("Mining/polish impure cost tokens") — §2 numerals below are duplicated there.

**Output rule for this file:** Section 1 is PURE (parser/callback structure with
addresses; field identities and value TYPES only — no price, possibility, or
compensation AMOUNTS asserted). Section 2 is UNPURE (every cost/probability
numeral encountered, each marked impure with source/era/impurity reason; none
counts toward any 70% threshold).

Code coordinates are **Ghidra addresses (ELF VA + 0x10000)** unless marked ELF.

---

## 1. PURE — parser/callback findings (no amounts)

### 1.1 Reference route → callback → parser chain

| Route | Callback (Ghidra) | Parser (Ghidra) | Container key (Ghidra) |
|---|---|---|---|
| `/reference/GetGemLevelUpPrice` | `CSRSyncRef::ReqGemLevelUpPriceCB` **f84eba** | `CSRGem::ParseGemLevelUpPrices` **a54108** | `ret_data`, ADD **a5412c** |
| `/reference/GetGemSellPrice` | `CSRSyncRef::ReqGemSellPriceCB` **f84e98** | `CSRGem::ParseGemSellPrices` **a53e50** | `ret_data`, ADD **a53e7a** |
| `/reference/GetGemDisassemblePrice` | `CSRSyncRef::ReqGemDisassemblePriceCB` **f84edc** | `CSRGem::ParseGemDisassemblePrices` **a54528** | `ret_data`, ADD **a54546** |

Sources: `analysis/research/gem-reference-contract.md` §§"Five reference
responses"/"Price-row fields"; `analysis/ghidra-gem-reference-keys.txt`
ll.16–37; `analysis/native-evidence.tsv` ll.22757–22758 (callback symbols),
l.12980 (parser symbol); `analysis/native-all-strings.tsv` ll.21708, 34345,
34350 (mangled names).

Each callback passes the **full parsed envelope** into its parser, which
extracts `ret_data` and iterates rows. An honest empty reference reply is
`{result_code:1,ret_data:[]}` — no `gem[]`/`stat[]`/`price[]` wrappers
(gem-reference-contract.md §"Five reference responses").

### 1.2 Polish-price row fields with literal addresses (Ghidra)

From `analysis/ghidra-gem-reference-keys.txt` ll.23–31
(`00a54108 ParseGemLevelUpPrices` block, 7 resolved literals):

```text
ret_data            ADD a5412c   (container; ldr@00a54126)
level               ADD a541b2   (ldr@00a541aa)
price_type          ADD a541b8   (ldr@00a541b6)
price               ADD a541be   (ldr@00a541bc)
possibility         ADD a542d0   (ldr@00a542cc)
failed_compensation ADD a54328   (ldr@00a54324)
add_sub_ability     ADD a54374   (ldr@00a54370)
```

This is the complete row vocabulary: **six fields, no more**. Field identities
are proved by register-paired `ldr`/`ADD` literals; no original row VALUES were
recovered — the replica serves empty arrays (gem-reference-contract.md
§"Price-row fields"; gem-contract-implementation.md ll.5–8).

### 1.3 Per-field value types from `ParseGemLevelUpPrices` decompilation

Source: `analysis/ghidra-gem-reference.txt` ll.957–1327
(`a54108 ParseGemLevelUpPrices @ 00a54108`).

- `level`, `price_type`, `price` — **unsigned 32-bit scalars** (`uVar17`,
  `uVar14`, `uVar18`). Each `switch(*pbVar3)` accepts JSON string (`0x3`,
  via `strtod`), bool-byte (`0x4`), uint (`0x5`/`0x6`), or double (`0x7`);
  default 0. Read at decomp ll.1067–1156.
- `possibility`, `failed_compensation` — **64-bit values** (`uVar23` at
  ll.1157–1182, `uVar22` at ll.1183–1206). Each `switch` accepts JSON string
  (`0x3`, via `strtod` into 64 bits), int64-thunk (`0x5`), uint64-thunk
  (`0x6`), or double (`0x7`). **There is no `0x4` (bool) arm** — both take
  the implicit-zero path for JSON booleans. Stored at record `+0x10`
  (possibility) and `+0x18` (failed_compensation) in both the slow-path
  (`operator_new`, ll.1260–1268) and fast-path (`*puVar9` writes, ll.1280–1285)
  stores.
- `add_sub_ability` — **boolean flag** (`bVar19`). `switch` at ll.1207–1234:
  `0x4`/`0x5`/`0x6` copy the raw byte directly; `0x7` (double) converts via
  `(0.0 < dVar24) * (char)(longlong)dVar24` (nonzero-positive → 1); `0x3`
  (string) via `strtod` with the same positive-nonzero test; default 0.
  Stored at record `+0x20` (ll.1262, ll.1280).

### 1.4 Record layout (STRUCTURE only, no values)

Both store paths write the same layout; stride is **`0x28` (40) bytes**
(`operator_new(uVar20 * 0x28)`, l.1258; fast-path advance `puVar9 + 10`
uint32 words = 40 bytes, l.1288):

```text
+0x00  level               uint32  (uVar14)
+0x04  price_type          uint32  (uVar17)
+0x08  price               uint32  (uVar18)
+0x10  possibility         uint64  (uVar23)
+0x18  failed_compensation uint64  (uVar22)
+0x20  add_sub_ability     bool    (bVar19)
```

Vector lives at `CSRGem+0x4c` (begin) / `+0x50` (end) / `+0x54` (capacity);
the parser first resets end=begin (`*(this+0x50) = *(this+0x4c)`, l.1026),
so each fetch **replaces** the table rather than appending.

### 1.5 What `possibility` / `failed_compensation` PROVE structurally

- `possibility` is a per-row 64-bit column sitting between the price columns
  and the failure column — consistent with the qualitative help rule "the
  higher the polish stage, the more difficult it becomes" (VSFan 1.4.4.1 EN
  help `CONTENTS11_6`, quoted in mining-costs §1), but its **units/scale are
  unproved** (percent? basis points? weight?). Do not assert units.
- `failed_compensation` is a per-row 64-bit column — consistent with a
  failure-compensation concept — but its **semantics are unproved** (currency
  amount? item? display-only?). The help prose says failing loses only the
  spent rupees with no further penalty, which suggests compensation may be
  zero/empty in practice; that is corroboration, not a parsed value.
- `add_sub_ability` is a per-row boolean flag — consistent with the POST-era
  "substat upgrades fixed at maximum" growth rule existing as a per-stage
  toggle, but that association is **inference, not a parsed binding**.

### 1.6 Polish ACTION side (request path, structure only)

Native symbols prove the polish transaction exists separately from the price
reference (all from `analysis/native-all-strings.tsv`):

- `CSRGem::RequestGemLevelUp` (`0024dea0`, l.21699) — posts **`/gem/LevelUp`**
  (`01d7862a`, l.443393). Request fields and response shape are **not
  recovered** in this pass; do not invent them.
- `CSRGem::FindGemLevelUpPrice(int, PRICE_TYPE)` (`0024dfe8`, l.21701) — the
  price-table lookup the client uses before requesting; proves the LevelUp
  price table is keyed by (level, price_type). Lookup miss/empty-table
  behavior is unproved.
- `CSRGem::ParseGemLevelUp` (`0024db16`, l.21692) — the LevelUp RESPONSE
  parser; its consumed fields are **not recovered** in this pass.
- `CSRPopUpGemLevelUp::RequestGemLevelUp` (`002a6396`, l.25264) and
  `::UpgradeCB` (`002a64e1`, l.25271) — the polish UI requester/callback.
  UI price/possibility display bindings are unproved.
- `level_up_failed` is an owned-instance field consumed by
  `CSRGem::parse a5d3dc` (gem-reference-contract.md §"Owned inventory"),
  proving the client tracks per-jewel polish failures — but its increment/
  reset semantics are unproved.

### 1.7 Sibling price tables (structure only, for disambiguation)

- `ParseGemSellPrices` rows: `rank, level, price_type, price` — all uint32,
  16-byte records (`__push_back` of 4×uint32; ghidra-gem-reference.txt
  ll.679–954; keys ll.16–22).
- `ParseGemDisassemblePrices` rows: `level, price_type, price` — all uint32,
  12-byte records (`operator_new(uVar20 * 0xc)`; ghidra-gem-reference.txt
  ll.1330–1602; keys ll.32–37).
- Neither sibling has `possibility`/`failed_compensation`/`add_sub_ability`;
  those three columns are **unique to the LevelUp (polish) table**. Do not
  copy polish semantics onto sell/disassemble rows.

### 1.8 Mining price: NEGATIVE result (no native route isolated)

No dedicated mining-price reference route or Manda-mining-cost parser was
found in native evidence. `CSRLotteryX10Card::Check10GatchOverGemMineLimit`
(`00275bf9`, native-all-strings.tsv l.27966) references a gem-mine LIMIT
check, not a price. The `/gem/PaidGacha`, `/gem/MileageGacha`,
`/gem/DailyFreeGacha` routes (`01d78643`–`01d78664`) are gacha routes, not
mining-price tables. The Manda mining price / advanced-mining price remains
**unisolated** — unchanged from mining-costs §4.

### 1.9 Res-1 CSV exclusion (restated as structural fact)

`LEVELING.jet` res-1 is a polish-PROBABILITY tuning CSV (ranks 2–15,
base/attempt values) with no cost columns. It is never a substitute for the
`GetGemLevelUpPrice` reference rows. Sources: mining-costs §1;
`old-apk-2026-10-05.md` §3; `jewel-economy-2026-10-05.md` §5.

---

## 2. UNPURE — every cost/probability numeral (rebalance leads only, NO coverage)

None of the following counts toward any 70% threshold. Preserved verbatim from
[`mining-costs-2026-10-05.md`](mining-costs-2026-10-05.md) §2; see that file for
full source locators.

- **Jewel removal footer: `40000` (gold icon) / `40` (second currency icon,
  identity unknown).** Visual panel evidence (FAQ image22 footer) confirmed on
  image22 ONLY. ERA-UNKNOWN. REMOVAL fee, not a mining or polish price.
- **Community refine budget: "at least 600k rupees"; fail risk rises "after
  level 9+".** TEXT-SOURCE (FAQ L426 prose, author/date/build unknown,
  ERA-UNKNOWN). Player budget recommendation, NOT a per-attempt price.
- **Honor-medal trace rates: ★4 trace = 700 medals per 8 traces; ★3 trace =
  350 per 8.** TEXT-SOURCE (Namu item page, ERA-UNKNOWN). Trace-exchange
  context, not mining/polish costs.
- **Post-threshold polish growth (official text, POST era, TapTap 2019-09-04):
  ★1–★3 mains +30%, ★4–★5 mains +50%, all substats +50%, substat upgrades
  fixed at maximum.** Growth multipliers, not prices or success rates.
- **Namu equipment upgrade rupee/toolbox tables: NOT transcribed.** Column
  alignment ambiguous; equipment-upgrade costs in any case, not jewel costs.
- **Namu item page §4.4.3 결정 (Crystal): empty header** (negative result).
- **Fresh web searches (EN + KR) in the mining-costs pass: no game cost
  screenshot found** (name collides with jeweler/building-stone; KR returns
  unrelated game guides and the Namu item page with only adjacent fuel/shop
  figures: Manda 5 → 60 fuel; market rupee corner 6,000 → 60 per 4h).

## 3. Remaining open gap (unchanged)

Still missing: the **rupee polish-cost table per stage** (native schema §1.2
proves where it would live; §1.3–1.4 prove the value types to expect when
original rows surface), the **Manda/advanced mining price** (§1.8 negative
result), and any **per-stage success-rate values with proved units**. The most
promising leads remain archival captures of the in-game polish panel and the
original `GetGemLevelUpPrice` reference rows — not further web search.
