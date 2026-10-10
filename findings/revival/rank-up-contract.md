# Hunter RankUp: native contract and promotion limits

2026-10-04. Read-only original-library Capstone/literal inspection, existing guide/screenshot evidence. No source/runtime/Ghidra/original changes. Addresses are Ghidra image addresses.

## Request

[RECOVERED] `CSRSyncCard::RequestRankUp`0xf546f0 posts **/gym/RankUp**. Eight form fields: app_code,app_ver,market,pvid,otp, **target_inst_id**, **source_inst_list**, **is_tuto**. Target is uint64 serial; source_inst_list is JSON text containing numeric source serials; is_tuto is the string0/1 selected from the request's boolean argument.

Target/source/path literals:0xf548da/0xf54964/0xf54b6e. is_tuto pairing: load0xf54972 ->slot0xf54a04; addPC0xf54982 ->0x1d7b2fb. The strict resolver's apparent **t** at0xf54798 is **false**: register-matched actual value pair is slot0xf549dc+PC0xf547a0 ->"0", slot0xf549e0+PC0xf547a2 ->"1". No desired new rank, expected current rank, or nonce was recovered.

## Complete success response

Recovered shape, with local example numbers:

```json
{"result_code":1,"ret_data":{
 "user":{"gold":{"prev":1000,"cur":0},
   "deck":[{"type":1,"inst_id_1":1,"inst_id_2":0,"inst_id_3":0,"inst_id_4":0,"inst_id_5":0}]},
 "card":{"target_inst":{"inst_id":1,
   "rank":{"prev":1,"cur":2},
   "rank_up_cnt":{"prev":0,"cur":0},
   "exp":{"prev":2900,"cur":0}},
   "removed_inst_list":[3]}
}}
```

All balance/XP/count values above are **[FIXTURE example]**, not original prices or curves.

`ReqRankUpCB`0xf54fe8 indexes ret_data, optional achievement, then **user.gold.prev/cur**, **user.deck**, **card.target_inst.inst_id**, **rank.prev/cur**, **rank_up_cnt.prev/cur**, **exp.prev/cur**, **card.removed_inst_list**. Parent ownership is proved by registers: ret_data r4 at0xf5516a; user retainedr6; deck indexed withr6 at0xf55264; card indexed withr4 at0xf55276 then retainedsb; target objectr4 at0xf55288; removed list indexed withsb at0xf5556c. User deck is passed to ParseDeckSetting0xf5526e; gold.cur replacesplaydata+0x154.

**Removed entries are BARE uint64 numbers**, unlike ordinary LevelUp's object rows. At0xf555f8 the iterator dereferences the entry;0xf5561e reads that entry's JSON scalar tag directly and converts it to uint64, with **no inst_id indexing call**. RemoveCard is called0xf55686. Therefore send **[3,4]**, not `[{inst_id:3},{inst_id:4}]`.

Target current rank/rank_up_cnt/exp are passed together to **CSRInventory::SetCardRank(uint64,unsigned,unsigned,unsigned)**0xae9c78 at0xf5553a. The rank-up callback does not consume optional skill-level fields. Omit achievement while unknown; no original reward branch/consumed-item schema was established for this promotion path.

## Refusal and retry

Nonzero transport status or response result_code!=1 branches0xf5500a/0xf55014 ->0xf5508a before mutation. That branch initializes the complete **RANK_UP_PARAM to zeros** and invokes its callback. ParsedJSON result_code!=1 similarly skips ret_data0xf55114..34. There is no success fake-shape requirement for refusal.

`CSRTableRankUp::OnTrainingRankUpEnd`0x103b554 compares parameter's first previous/current rank pair at0x103b570..576; **prev>=cur returns without promotion animation**, including allzero refusal. Original business refusal code is unknown; a local non1code is an implementation policy.

Consumed-source ownership is the strongest natural repeat protection: a retry naming already-consumed sources cannot spend/promote again. Persist a replay receipt if exact same-response transport replay is needed; no native nonce or expected version was recovered. Do not infer the phantomt as one.

## Native recalculation and newly unlocked skills

SetCardRank calls **CSRCard::SetRank(rank,rank_up_cnt)**0x869c70, then **SetExp(exp)**0x869ea4. On rank change, SetRank recalculates maximum hunter level via GetCardMaxLevel0x10a0c68 and maximum skill level via GetCardSkillMaxLevel0x10a1078 (calls0x869c96/0x869cb0), updates rank-bonus factor and recalculates current level from existingexp; final SetExp applies responsecurrentexp.

**SetRank does not call SetSkillLV** and RankUpCB does not parse individual skill fields. A newly rank-eligible reference slot may become visible, but no automatic0→1 owned skill-level mutation is proved here. Current neutral instance fixture uses0 for locked later skills; do not silently invent a response skill field to fix that. Need a specific native eligibility/initial-level rule or refreshed owned inventory/profile control. Preserve already-trained existing skill levels through promotion.

## Materials, max level and partial progress

[COMMUNITY-SOURCED] `hunter-level-caps.md` pins ordinary maximumlevel30 regardless grade (Namu footnote36). Namu footnote37 says advancement uses **same-grade hunters equal to the target's current star count**. Source level does not have to beMAX: the original3★→4★ screenshot contains Lv1 sources. All selected sources are consumed. Native source filtering `CSRTableRankUp::IsInactiveCard`0x103c1b8 protects deckcases1,2,4,5, nonzero inventory lock and leader; target/self exclusion and duplicate rejection remain necessary server integrity. The same-grade rule is community-supported here, not recovered from a server response.

Native `/reference/GetCardRankUp` rows **rank,src_cnt,stat_bonus** feed GetCardRankUpSrcCnt0x87f348. Empty/missing rank table yieldssourcecount0, so it is insufficient for a functioning native advancement screen. Load calls that getter0x1039406 and storesrequiredcapacity+0x65c. Rank prices come from the separate nonempty rank vector (`GetCardRankUpPrice`0x87f322), with ordinal selection/cap-to-last; source counts and price rows must agree with server policy.

**Partial promotion is a real gap to respect.** **Retraction:** both preserved2018 destinationbadges arefour-star; the two-sourcepreview is faded, notthree-star. The screenshotdoesnotproveacceptedpartialpromotion. Native creditedplaceholderconstruction andlinearbonus independently establish that `rank_up_cnt` tracks credited progress, not merely a number of completed promotion transactions. `CSRTableRankUp::GetSrcCnt`0x103aaac loads target.rank_up_cnt at0x103aafa and subtracts it from the source vector count0x103ab5a..60. The exactserverpartialtransition/EXPpolicy remains inferred; see `rank-up-partial-arithmetic.md` for exactfacts andproposedreconstruction.

A first implementation can deliberately support **full promotions only** (target atpublishedMAX,ordinaryrank1..4,rank_up_cnt0,exactsame-ranksourcecount,uniqueownedunlockedunusedsources,sufficientgold) and refuse partial requests. That is a narrower **local revival constraint**, not faithful full original advancement. Full promotion's newrank+1/EXP0 is corroborated by the right screenshot; a reset rank_up_cnt0 is an explicit local policy until an original response is found. Never treat rank_up_cnt as blindly+1.

Before success, validate new-rank reference-stat and GetLevel.card coverage. Persist targetrank/counter/EXP, source removals, gold and remaining decks atomically. Protect leader/current decks/active battle as for training, clear consumed ids from any unprotected preset, and send the corresponding native user.deck. Granting newrank with no reference stat row can fault in the next native analyzer.
