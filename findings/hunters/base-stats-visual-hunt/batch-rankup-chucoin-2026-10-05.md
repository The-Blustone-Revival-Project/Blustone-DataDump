# Batch rank-up + Chu-coin native parsers — 2026-10-05

**Lane:** audit native batch rank-up (`/gym/RankUpBundle`) and hunter-release /
Chu-coin (`/shop/SellCard`, Secret Market) parsers from symbol tables, literal
pools and existing decomp dumps. **Read-only:** no server/APK/state changes, no
Ghidra project writes, no new decompilation runs — only tables and files already
on disk were inspected.
**Coverage:** no change (heroes 1/113, accessories 1/100, monsters 0/22).
All numeric economy tokens in §2 are **impure rebalance context** — they never
count toward any 70% threshold.

**Sources consumed:**
- `analysis/research/base-stats-visual-hunt/training-rankup-rules-2026-10-05.md`
  rules 8–9 (the GAP / UNIMPLEMENTED verdicts this lane re-examines).
- `analysis/research/rank-up-contract.md`, `rank-up-partial-arithmetic.md`,
  `rank-up-implementation-audit.md` (ordinary single-target `/gym/RankUp`
  contract — the baseline the batch path is compared against).
- `analysis/systems/gym.md` §§2–4 (gym TU route/callback map + literal
  inventory; adjacency-is-not-proof warning applies throughout §1 below).
- `analysis/native-all-strings.tsv` (`.rodata` literal pool; **Ghidra image
  addresses = ELF VA + `0x10000`**, not file offsets — corrected 2026-10-05, see
  `address-convention-2026-10-05.md`), `analysis/native-evidence.tsv` (symbol
  table; Ghidra addresses).
- `analysis/ghidra-card-keys.txt`, `analysis/ghidra-enemycamp-refs-01.txt:57-79`
  (call-graph), `analysis/ghidra-fnlist14.txt`.

**Address convention:** `0x00xxxxxx` = Ghidra image address (ELF + `0x10000`);
`0x01dxxxxx` = Ghidra image address of a `.rodata` literal, as listed in
`native-all-strings.tsv` (**also** ELF + `0x10000` — corrected 2026-10-05; this
line previously left the literal column unlabelled, which invited reading it as
ELF VA. Verified: 15/15 literal pairs here match byte-exactly at
`address − 0x10000`, 0/15 at the address as printed). Definitive table:
`address-convention-2026-10-05.md`.

---

## 1. PURE — parser / callback findings (no numeric claims)

### 1.1 `/gym/RankUpBundle` IS the native batch rank-up path — requester, callback and sink recovered; wire shape NOT recovered

| Fact | Value | Provenance |
|---|---|---|
| Route literal | `/gym/RankUpBundle` @ `01d8f7d4` | `native-all-strings.tsv:448368` |
| Requester | `CSRSyncCard::RequestGroupRankUp(uint,uint,uint,uint,uint, function<void(int)>)` — **five uints, no instance vector** | `native-all-strings.tsv:26440` (`002ba6f7`), `native-evidence.tsv:22534` (`00f586e4`) |
| Callback | `CSRSyncCard::ReqGroupRankUpCB(function<void(int)>, int, CPVHTTPRequest const*, CPVHTTPResponse const*)` | `native-all-strings.tsv:34082` (`003539f1`), `native-evidence.tsv:22535` (`00f58da0`) |
| Callback sink | `void(int)` only — **no PARAM struct** | ⚠️ was wrongly `void(int,int,int)`; **corrected 2026-10-05**, see note below + `grouprankup-sellcard-bodies-2026-10-05.md` §1.5(1) |
| Model setter | `CSRInventory::SetCardRank` (`00ae9c78`) ← call `00f5922e` inside `ReqGroupRankUpCB` | `ghidra-enemycamp-refs-01.txt:63-66` |

> **⚠️ CORRECTION 2026-10-05 — the callback sink type in the row above was WRONG.**
> It is `void(int)`, **not** `void(int,int,int)`. Source:
> [`grouprankup-sellcard-bodies-2026-10-05.md`](grouprankup-sellcard-bodies-2026-10-05.md)
> §1.5(1). The demangled type on **both** symbols is
> `_ZN11CSRSyncCard18RequestGroupRankUpEjjjjjRKNSt6__ndk18functionIFviEEE` /
> `…16ReqGroupRankUpCBERKNSt6__ndk18functionIFviEEE`; in Itanium mangling
> `IFviE` = `void(int)`, whereas `void(int,int,int)` would be `IFviiE`.
> Cross-checked inside the same library (`CPVAccount::RequestConfirmNickname`,
> `CPVPurchase::RequestIAPInfo` use the identical `IFviEEE`), and confirmed by
> instruction audit: exactly **one** int is materialised at the invoke site and
> it is the **result code**. The *conclusion* in structural consequence 1 below
> survives (the batch path still has **no PARAM struct**); only the type was
> wrong. The same correction applies to `analysis/systems/gym.md:97`.

Structural consequences (pure — they constrain any future implementation):

1. **The batch callback contract differs in kind from single RankUp.**
   Ordinary `ReqRankUpCB` (`00f54fe8`) sinks `void(RANK_UP_PARAM)` **by value**
   and parses `user.gold prev/cur`, `user.deck`, `card.target_inst`
   (inst_id + rank/rank_up_cnt/exp prev/cur pairs) and bare-numeric
   `card.removed_inst_list` (`rank-up-contract.md`). The batch callback sinks
   **exactly one plain int — the result code** ⚠️ **corrected 2026-10-05** from
   "three plain ints"; see `grouprankup-sellcard-bodies-2026-10-05.md` §1.5(1) —
   and has **no PARAM struct at all** — so none of the single path's response keys
   (`target_inst`, `removed_inst_list`,
   `removed_inst_id_list`, `skill_%u_level`) can be assumed on the batch path.
   Reusing the single-RankUp response shape for `/gym/RankUpBundle` is
   unsupported by current evidence.
2. **The requester takes five scalar uints, not an instance list.**
   Compare: `RequestRankUp(inst:ulong, src:vector<ulong>, is_tuto:uchar)` vs
   `RequestGroupRankUp(uint × 5)`. A batch call therefore cannot be addressing
   individual fodder instances the way single RankUp does; it is plausibly a
   grade/count-parameterised bulk operation (consistent with a "rank up all
   ★1–★2 without max level" onboarding shortcut), but the five parameters'
   identities are **unproved**.
3. **⚠️ SUPERSEDED 2026-10-05 — `src_rank` is now [RECOVERED], not an adjacency
   candidate.** Source: `grouprankup-sellcard-bodies-2026-10-05.md` §1.1 and
   §1.5(2). The register-matched pairing this point said had "never been run"
   **has** now been run over `0x00f586e4:0x00f58da0`, and **all five** request
   fields are recovered, one-to-one with the five uints: `src_rank` @ `01d8f7cb`
   ← uint #1; `src_cnt` @ `01d6feba` ← uint #2; `target_rank` @ `01d6fe55` ← uint
   #3; `target_cnt` @ `01d6f8f6` ← uint #4; **`price`** @ `01d6aa71` ← uint #5 —
   `price` was not in `gym.md` §4's candidate list at all, and `card_cnt` from
   the old list does not appear (`src_cnt` does). The original wording
   ("`src_rank` remains a **candidate**") is superseded; see the §1.1 field table
   there for load sites, literal slots and frame arithmetic.
4. **No response-key evidence exists on disk for this path.** No decomp dump of
   `ReqGroupRankUpCB` (`00f58da0`) or `RequestGroupRankUp` (`00f586e4`) was
   found in `analysis/` (searched `*rank*`, `ghidra-enemycamp-*`,
   `ghidra-card-keys.txt`). `SetCardRankUp`'s resolved keys (`ret_data`, `e`,
   `src_cnt`, `stat_bonus` — `ghidra-card-keys.txt:75-80`) belong to the
   **reference** container (`/reference/GetCardRankUp`), not to either RankUp
   response. The batch response shape is therefore **[UNKNOWN]** in full.
    ⚠️ **CORRECTED 2026-10-05:** the body audit this point said was missing has
    since been done (`grouprankup-sellcard-bodies-2026-10-05.md` §1.2), so the
    batch response shape is **no longer [UNKNOWN]**: it is `ret_data.achievement?`
    / `ret_data.user.gold.cur` (absolute uint32 at `PlayData+0x154`) /
    `ret_data.card.{removed_inst_id_list, target_list[]}`, where each
    `target_list` element is `{inst_id, rank:{cur}, rank_up_cnt:{cur}, exp:{cur}}`
    — **single `{cur}` objects, no `prev` anywhere**, a *different* contract from
    the single `/gym/RankUp` path. The sentence above is retained as the state of
    knowledge *at the time of this pass*.
5. **No max-level-bypass gate was found client-side.** The ordinary path's max
   level requirement is enforced server-side (local policy), not by a native
   check this lane could locate; no native batch-eligibility predicate
   (underlevel acceptance, grade filter) has been audited either. The guide's
   "★1–★2 without max level" claim has **no mapped native predicate** yet.

Related UI surface (symbols only, no behaviour audited):
`CSRPopUpGroupRankUpSel` / `CSRPopUpGroupRankUpStar` (Star ctor takes a `GRADE`
param) / `CSRPopUpGroupRankUpResult` (`native-evidence.tsv:16746-16769`,
`native-all-strings.tsv:26413-26452`); `CSRDlgRankUpIconDraw::SetPromotion`
family (`native-all-strings.tsv:17131-17164`); `CSRPlayData::IsTrainningRankUp`
(`00b6e5f4`); `CSRCard::GetJustRankUpRemainedTEl`. None of these were
decompiled in this lane; they are leads for the next audit, not findings.

**Verdict on rule 8:** the GAP stands and is now narrower — the batch route,
requester arity, callback sink type and shared `SetCardRank` sink are mapped,
but **zero request fields and zero response keys are proved**. Implementation
must wait on a `ReqGroupRankUpCB`-body audit (register-matched literal
resolution per `gym.md` §4), not on more table reads.

> **⚠️ CORRECTION 2026-10-05 — that audit has now been done and it closed most
> of the rule-8 GAP.** `grouprankup-sellcard-bodies-2026-10-05.md` §§1.1–1.2
> recover **all five request fields** (§1.1) and the **full response shape**
> (§1.2) for `/gym/RankUpBundle`, so "zero request fields and zero response
> keys are proved" is superseded. What remains open is narrower and unchanged in
> kind: the `void(int)` sink type was corrected (see the note above), and **no
> client-side batch-eligibility predicate** has been found, so the "★1–★2 without
> max level" guide claim still has no mapped native check. No server handler
> exists for this route; do not implement one from this file alone.

### 1.2 Hunter release / sell path exists as symbols; Chu-coin and Secret Market do NOT exist in native evidence

| Fact | Value | Provenance |
|---|---|---|
| Route literal | `/shop/SellCard` @ `01d9030a` | `native-all-strings.tsv:448518` |
| Requester | `CSRSyncShop::RequestSellCard(vector<ulong> const&, function<void(req, resp, int)>)` — **instance-ID vector** | `native-evidence.tsv:22813` (`00f8df98`), `native-all-strings.tsv:24748` (`0029d413`) |
| Parser | `CSRSyncShop::ParseSellCard(vector<ulong> const&, nlohmann::json const&)` | `native-evidence.tsv:22814` (`00f8ed98`), `native-all-strings.tsv:34411` (`003658ca`) |
| Neighbour literals | `target_order` @ `01d902e6`, `/shop/SellItem` @ `01d902d7`, `/shop/IAPAchieveReward` @ `01d902f3`, `ReqBuyItemCB` @ `01d90319`, `add_result` @ `01d90326` | `native-all-strings.tsv:448513-448520` |

Findings and explicit non-findings:

1. **SellCard takes a hunter instance list** (same `vector<uint64>` shape as
   `RequestSellCard`'s sibling paths), so the client *can* name released
   hunters — but the request field name, the response keys, and **what the
   player receives in return** (rupees? coins? nothing parsed?) are all
   unrecovered: no decomp of `00f8df98`/`00f8ed98` exists on disk.

   > **⚠️ CORRECTED 2026-10-05 — both bodies have now been audited, and the
   > Chu-coin hypothesis is a NATIVE NEGATIVE.** Source:
   > `grouprankup-sellcard-bodies-2026-10-05.md` §§1.3–1.4.
   >
   > - **Request [RECOVERED]:** the field is **`inst_id_list`** @ `01d78609`,
   >   a `vector<uint64>` walked at stride 8, appended with
   >   `nlohmann::json::push_back` (**numbers, not strings**), then
   >   `dump()`ed into a single form string — i.e.
   >   `inst_id_list=%5B1%2C2%5D`-style (a JSON array inside one form field),
   >   **not** a comma-joined bare list.
   > - **Response [RECOVERED]:** `ParseSellCard` reads only
   >   `ret_data.user.gold.cur` (optional, **absolute** uint32 → `PlayData+0x154`;
   >   no `prev`, no `free_iap`/`iap`) and `ret_data.item[]{inst_id, ref_id,
   >   added}` → `CSRInventory::AddItem(inst_id, ref_id, added)`.
   > - **The reward arrives as ITEM rows, not as a coin count.** There is **no**
   >   literal, key or setter anywhere in the body for a Chu-coin / `coin`-style
   >   currency. The client **cannot display a coin total it has no field for**,
   >   so the Chu-coin reading of §1.2.2 below is now a **native negative**, not
   >   merely an unproven archive text.
   > - **The removal list is not read from the response** — it comes from the
   >   caller's own `arg0` vector, so no "sold"/"removed" response key is needed.
   > - **Guards are asymmetric:** `ret_data`, `user`, `gold` and `item` are all
   >   checked, so `ret_data` must be an object or absent.
   >
   > **Do not implement a Chu-coin credit on this route.** The two archive coin
   >   rates in §2 remain historical text with no native key.
2. **No Chu-coin literal exists in the native tables.** Case-insensitive search
   for `chu`, `chuu`, `チュウ` over `native-all-strings.tsv` returns nothing
   game-related; the 37 `coin` hits are IAP bundle refs (`FindCoinRefsByBundleID*`),
   battle drop FX (`SpawnCoin`, `coin_drop_cnt_by_boss`, `coin_rwd_ratio_boss`)
   and UI anim tags (`BT_COIN`, `TX_COIN`, `coin_ani`) — none is a hunter-release
   currency. The Chu-coin is therefore **archive-text-only**; no native currency
   key can be attached to it today.
   ⚠️ **UPGRADED 2026-10-05 — table-search negative → native negative.** Direct
   body audit of `RequestSellCard`/`ParseSellCard` confirms there is no
   `coin`/`chu`/`secret`/`market` key anywhere in either body
   (`grouprankup-sellcard-bodies-2026-10-05.md` §1.6). This is no longer "absent
   from the tables"; it is **absent from the code**.
3. **No Secret Market route exists in the native tables.** The `/shop/*`
   literal run (`01d90246…01d9030a`: BuyItem, Reset, BuyGlobalItem,
   PieceExchange, Refresh, SellItem, IAPAchieveReward, SellCard) contains no
   market route; the only `secret` symbol is `CSRSupplySecretQuiz` (a quiz
   feature, unrelated). `SHOP` / `SHOP_ACHIEVE` (`01d90490`, `01d904e8`) are
   tutorial-type enums, not routes.
4. **`sell_price` / `sell_result` are false friends — excluded.** `sell_price`
   @ `01d7a107` sits in the item-TU beside `use_type`, `thumbnail_id`,
   `GetItemData` (item reference/sell display, not hunter release).
   `sell_result` @ `01d7aff5` sits beside `b_price`/`s_price`/`g_price` and the
   `FISHING/*` scene keys (fishing-sale result). Neither is adjacent to, or
   callable from, `ParseSellCard` on current evidence. Do not cite them as the
   release-reward parser.
5. `CSRGem::SELL_PRICE` vector (`native-all-strings.tsv:21749`) is the only
   proved sell-price **container** seen in this lane, but its parsers/callers
   were not audited here and it belongs to the jewel system, not hunter
   release. Recorded as a lead, not a finding.

**Verdict on rule 9:** UNIMPLEMENTED stands, unchanged in substance but with a
concrete next target — `ParseSellCard` (`00f8ed98`) takes the sold-ID vector
plus a JSON body, so a body audit can establish the reward keys (if any). Until
then there is no native Chu-coin credit, no release rate, and no market
purchase to implement.

> **⚠️ CORRECTION 2026-10-05 — the body audit named above is DONE, and it
> settles the Chu-coin question negatively.** `grouprankup-sellcard-bodies-2026-10-05.md`
> §§1.3–1.4 recover the request field (`inst_id_list`) and the whole response
> shape. **Rule 9 remains UNIMPLEMENTED, and for a firmer reason: the route pays
> ITEM rows (`ret_data.item[]` → `CSRInventory::AddItem`) plus an optional
> absolute `user.gold.cur`; there is no Chu-coin field for a server to answer
> with.** No release rate, no market purchase, and above all **no coin credit**
> should be implemented on this route.

### 1.3 What was NOT done (limits of this pass)

- No Ghidra project session, no new decompilation, no Thumb-literal
  re-resolution; `tools/resolve-literals-offline.py` was not run (read-only
  brief, and the gym TU needs the register-matched resolver per AGENTS §16.7,
  not a re-read of tables).
- ~~`ReqGroupRankUpCB`, `RequestGroupRankUp`, `RequestSellCard`, `ParseSellCard`
  bodies remain unaudited — these four functions are the entire remaining native
  work for rules 8–9.~~ **[stale item closed 2026-10-05: all four bodies are now
  audited in `grouprankup-sellcard-bodies-2026-10-05.md` (§1.1 `RequestGroupRankUp`
  request fields, §1.2 `ReqGroupRankUpCB` response shape, §§1.3–1.4
  `RequestSellCard`/`ParseSellCard`, §1.6 the coin-key negative). Rule 8's GAP is
  largely closed and rule 9 is a firmer UNIMPLEMENTED — see the ⚠️ CORRECTION
  blocks in §1.1 and §1.2 of this file. What genuinely remains is narrower and is
  stated there: no client-side batch-eligibility predicate, and `ParseSellCard`'s
  single caller could not be named.]**
- Server `openapi.ts:324-326` documents only single `/gym/RankUp`; no
  `/gym/RankUpBundle` or `/shop/SellCard` handler exists server-side (searched
  `server-ts/src` — RankUpBundle/SellCard appear only in generated
  `openapi.json` route stubs). Correct: nothing to change under a read-only
  brief.

---

## 2. UNPURE — numeric economy tokens (impure rebalance context, NO coverage credit)

Every token below is supplementary economy context only. None counts toward any
70% threshold. Era tags use the 2019-09-05 rebalance threshold. "Native status"
records whether any parser above can receive the token — in every case the
answer is currently **no proved key**.

| Token | Value | Source | Era | Native status |
|---|---|---|---|---|
| ★3 release yield | 8 Chu-coins (チュウコイン) | blustone.jp rank-up guide (POST 2019-11-13) via `training-rankup-rules-2026-10-05.md` §2a | POST | No Chu literal in native tables (§1.2.2) |
| Trainer price | two ★3 trainers per 8 coins → 4 coins/trainer, Secret Market | Same | POST | No market route in native tables (§1.2.3) |
| Batch rank-up scope | ★1–★2 without max level | Same | POST | Route mapped, fields/keys unknown (§1.1) |
| Rank-up preview prices | 8000 / 12000 (both destination badges four-star; faded two-source preview is NOT partial-promotion proof) | Caragublu Dec-2018 guide screenshot; retraction in `rank-up-partial-arithmetic.md` | PRE (2018-12) | No price parser on batch path; single-path price getter is rank-vector fixture |
| Rank-up value pair | 7,092 → 11,277 (generic Middle→Advanced Hunter, LvMAX→Lv1, new additional-damage skill) | FreeGame Mugen 2017-09-13 rank-up image | PRE (2017) | Field likely Power-rating; polluted progression only |
| Rank-up value pair | 1,417 → 2,389 + Block Chance Up (generic Amateur→Novice) | GameAppCH review image 16 | PRE (2017) | Polluted progression only |
| Trace-side coin rate | Lily&Lala traces 12 coins → 5 | Namu hunter mirror §1.3 (ERA-UNKNOWN) | UNKNOWN | Direction corroboration for a coin loop only; no native key |
| Sell-rule direction | 1–2★ sell for rupees; 3★+ give secret-corner (첨쥐) coins | Namu hunter mirror §1.3 | UNKNOWN | Reward keys **[RECOVERED 2026-10-05]** (§1.2.1 correction, `grouprankup-sellcard-bodies-2026-10-05.md` §§1.3–1.4): request `inst_id_list` = JSON array inside **one** form field; response is `user.gold.cur` (absolute uint32) + `item[]{inst_id, ref_id, added}`. **NO coin/currency key — native negative.** So the 3★+ coin reading has no field to arrive on; the archive direction stays archive text |
| Local rank-up fixture | 1000 gold/source; +5% stat bonus per credited material | `server-ts` openapi/fixture policy | NO era (not original) | Mechanism recovered, amounts fixture |
| Local raise fixture | 100 gold/source; source XP 100×level | Same | NO era | Mechanism recovered, amounts fixture |

Do not promote any §2 row into a server default, a reference-table value, or a
"recovered price". The two archive coin rates (8/release, 12→5 traces) describe
the same loop from opposite ends but share no native key; treating either as a
settlement rule today would be fixture invention.

---

## 3. Files written

- This file (new): `analysis/research/base-stats-visual-hunt/batch-rankup-chucoin-2026-10-05.md`.
- `polluted-observations.md`: appended §"Batch rank-up / Chu-coin impure economy tokens (2026-10-05)" summarising §2 with source URLs + era tags.
- No coverage-count change; no server/APK change.
