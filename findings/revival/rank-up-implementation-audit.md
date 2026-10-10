# RankUp implementation audit and native acceptance controls

2026-10-04. Read-only current source review, existing exact contract reports, and an additional original-library Capstone check of CardRankUp. No server/client/original edits, adb, or Ghidra. Addresses below use Ghidra image coordinates.

## Recommended minimum and current implementation

The current `training.ts` and `state.ts::rankUpCard` already implement the most defensible playable minimum. Publish ordinary ranks1..4 with `src_cnt`1/2/3/4; rank5 has terminal `src_cnt:0`. Publish `stat_bonus:5` and `GetCardEnhancePrice.rank:[1000]` as **explicit local balance fixtures**. Five percent is not recovered original balance; my earlier ten-percent suggestion was equally arbitrary and need not replace this choice. Source-count equality with current star grade and ordinary maxlevel30 have historical/community support, not original server-response proof.

For rank r, credited p, required capacity C, and n new same-grade sources, retain the documented **inferred server policy**:

- Require ordinary supported rank, published max level, `0<=p<C`, and `1<=n<=C-p`.
- If p+n<C, retain rank and EXP, set credited count p+n.
- If p+n=C, increment rank once, reset credited count0 and EXP to the next rank's level1 threshold (currently fixture0).
- Refuse overflow, awake curves, unsupported grades, and terminal rank5; never infer multigrade promotion.

Native credited placeholders and the linear stat formula make this interpretation coherent, but no captured original partial-success response proves its EXP policy or promotion threshold. The preserved 2018 screenshot has **four-star destination badges in both previews**; its faded two-source preview is not proof of accepted partial advancement. Its historical8000/12000 prices should not become universal2.8.0.1 balance.

Current source checks own target/materials, unique numeric IDs, no target/self, locks, protected leader/deckcases1/2/4/5, active-battle participation, same grade, no awake source, enough gold, and resulting reference-stat/level coverage before mutation. It preserves owned skills, removes consumed starters and recruits, clears any consumed IDs from unprotected deckcase3, merges book history, and persists once. Normalization retains each card object and `ownedPartyProfile` copies rank/counter/EXP/skills back into launcher/lobby profile, so reload has no intentional promotion reset.

## Native-proved pieces the implementation must preserve

`RequestRankUp`0xf546f0 posts `/gym/RankUp` with target_inst_id, source_inst_list (JSON text of uint64 numbers), is_tuto (string0/1), and five account fields. There is **no recovered t/nonce** or requested desired rank. The resolver's apparent t was disproved by matching the actual PC-relative register pairs.

`ReqRankUpCB`0xf54fe8 consumes full envelope `ret_data.user.gold.{prev,cur}`, `user.deck`, and `card.target_inst` containing inst_id plus rank/rank_up_cnt/exp previous/current pairs. **`card.removed_inst_list` is bare numbers**, not LevelUp's inst_id objects. Target mutation calls SetCardRank0xae9c78 at0xf5553a; RemoveCard follows at0xf55686. Keep achievement omitted until its shape is independently recovered. A non1 result skips mutation parsing and supplies zeroed callback parameters;2001 is a local refusal code, not the original error map.

The native selected vector includes p synthetic serials0..p-1 (`SetCardPromotion`0x103b0fc). `GetSrcCnt`0x103aaac returns vectorlength-p, hence n newly selected sources. Capacity C is independent, loaded through GetCardRankUpSrcCnt at0x1039406 into scene+0x65c.

Cost is a **sum over new real material ranks**: UpdateRankupInfo0x1039c40 skips serial<C at0x1039c80..8a, calls GetCardRankUpPrice(source.rank)0x1039cec, applies guild sale benefit type3 at0x1039cf4..f6, and accumulates+0x690. Current same-grade1000-vector fixture therefore charges1000*n. Already credited materials incur no second charge. No modeled guild benefit is justified until its own data exists; native displayed price must be checked against response debit.

SetRank0x869c70 stores p before same-rank early return0x869c7c..86. On a rank change, GetCardRankUpBonus(rank) is divided by100 and cached at card+0x674. Validate0x86acd0 computes **1+(stat_bonus/100)*p**, multiplying three primary computed stats at0x86adfe/86aed4/86af92. It is not exponential scaling or divided by required capacity. With fixture5%, p1 means factor1.05 and p2 means1.10. This does not define the separate base-stat growth between ranks.

SetRank changes max hunter/skill level but does not call SetSkillLV; RankUpCB parses no owned skill levels. Preserve trained levels and omit invented unlock fields. A newly eligible slot's effective initial level remains an independent gap; do not claim the promotion callback unlocks0→1.

## Newly strengthened legacy-ID constraint

The low serial collision affects the **request**, not only its price. Original `CSRTableRankUp::CardRankUp`0x103aba8 reads selected begin/end+0x66c/+0x670, then at0x103abf4 reads each uint64 serial;0x103abf8 loads capacity+0x65c;0x103abfc..0x103ac02 compares unsigned serial<C and branches to the next entry. Only survivors are appended to request vector sp+0x4c/+0x50 at0x103ac04..0x103ac14. RequestRankUp is invoked at0x103ae7e.

Thus a real legacy inst1/2/3 can be omitted from a capacity2/3/4 promotion request because native code treats it as credited. Continue allocating real recruits at least5, keep the server's low-ID refusal for direct research requests, and **do not renumber existing ownership/decks**. Native use of such legacy sources is a documented compatibility limitation. Source inst_id==C survives; only less-than-C collides.

## Acceptance cases

These are required progression checks, not evidence that native control has already passed:

1. Ordinary rank1 max-level target plus one unlocked unused rank1 source with ID>=5: rank2/counter0/EXP0, debit1000, numeric source removal, unchanged owned skills, next-rank reference stats valid.
2. Rank3 max-level target plus one source: rank3/p1, same EXP, debit1000; inventory and flat profile agree. Relaunch/persisted reload retains p1 and consumed source absence. Finish with two fresh sources: rank4/p0/EXP0, debit2000. Charge total3000, never another fee for p1.
3. Native partial-stat control: load new reference table before inventory; inspect strength/stat before and after p1 and after reloading. Expected local promotion contribution5%, independently of base rank growth. Absence of full promotion animation is expected for same-rank callback, not proof of refusal.
4. Same-grade Lv1 materials work; source MAX is not required. Wrong grade/awake/locked/leader/current deckcase1/2/4/5/self/duplicate/unowned/material active in battle all refuse without gold/card/deck/book mutation. Case3 source may be consumed and its saved slot becomes0.
5. Underlevel target, rank5, malformed p, credited overflow, insufficient gold, missing next-rank stat/curve refuse before mutation. Accept id==C only if otherwise valid; reject id<C explicitly. UI cannot be relied upon to transmit low IDs.
6. Repeat the same consumed-source request: refuse with no second debit/promotion. There is no native request token supporting a claim of exact-response replay. A receipt ledger is optional only if a separately justified transport-replay contract is added.
7. After full promotion, reopen inventory/Gym and relaunch: ownership, book highest grade, leader/deck/profile rank/p/EXP and trained skills remain coherent; no restored consumed starters.

## Remaining native callback/UI risks

- `OnTrainingRankUpEnd`0x103b554 returns at0x103b570..576 when previous rank>=current rank. Sync callback has already applied state, but no promotion animation or subsequent UI refresh is proved for partial success. Test native selected-card controls after partial; do not fabricate a rank increase to force animation.
- Bonus coefficient is cached only when rank changes. Updating the reference table while an owned same-rank card remains loaded with old bonus0 can leave coefficient0; a clean inventory reconstruction/reference-before-inventory control is necessary. No fake EXP mutation or client mask is justified.
- Newly unlocked skill owned-level behavior remains unresolved; preserving levels is safe, claiming new active skills work is premature.
- Rank5 `src_cnt0` is a terminal local table policy. Backend refusal is clear; native selection/render path for this terminal row still requires a control. Earlier missing-table C0 did not itself prove all terminal UI paths safe.
- Wrong removal element shape, missing rank-stat rows, stale consumed deck IDs, or nonempty unknown achievement data can crash subsequent native parsing/analyzers. Current implementation avoids those known hazards; native success must still be observed before calling RankUp verified.

Detailed provenance: `rank-up-contract.md`, `rank-up-partial-arithmetic.md`, `hunter-level-caps.md`, `training-public-evidence.md`. This audit does not change source or assert original balance fidelity.
