# Partial RankUp: recovered arithmetic and remaining server transition

2026-10-04. Read-only original-library Capstone, ELF vtable mapping, and re-viewed original2018 screenshot. No source/runtime/Ghidra/original changes. Ghidra addresses.

## Screenshot retraction — it does not prove successful partial advancement

**Both destination badges in caragublu-advance.jpg have four stars.** The left destination is faded while onlytwo sources are selected; the right is fully lit withthree. My intervening claim that the left badge wasthree-star was wrong. Original firstdescription was correct about itsstarcount. The8000/12000 prices remain visually verified, but a partial selection's changed previewstrength is **not** a captured server partialpromotion outcome.

## Native credited materials and newly selected materials

Let **p=owned rank_up_cnt**, **n=new real selectedsources**, **L=selected-vector length including credited placeholders**. `CSRTableRankUp::SetCardPromotion`0x103b0fc clears selectedvector (begin+0x66c/end+0x670), reads ownedcard+0x28 at0x103b152, then creates p synthetic progressentries indexed0..p-1. Thus **L=p+n** after selectingnewcards.

`GetSrcCnt`0x103aaac returns **L-p**, by reading the same vectorbegin/end and currentownedcounter, then0x103ab5a..60 subtracting p. Thus it is the count of **new** sourcecards, not recovered requiredcapacityC.

Requiredcapacity **C** separately comes from `GetCardRankUpSrcCnt(currentrank)`0x87f348 and is storedscene+0x65c by Load0x1039406..40c. Missing reference row yieldsC0. Publish an original/community-informed or explicitly fixture src_cnt table; do not replace C with GetSrcCnt's selectedcount.

## Exact price arithmetic

`UpdateRankupInfo`0x1039c40 walks selectedvector. Each serial smaller thanC is a synthetic placeholder and **skipped for cost** at0x1039c80..8a. Real sourcecard is found, its rank read+0x24, and rankprice obtained at0x1039cec (`GetCardRankUpPrice(source.rank)`). Guild sale-benefit type3 is applied at0x1039cf4..f6, then the result is accumulatedscene+0x690 at0x1039cfa..d00.

Therefore **cost=sum(discounted rankprice of each new actualsource)**. Previously credited p entries are not charged again. It is not target-rank flatcost, price×requiredcapacity regardlessselection, or an XP-based formula. A shared1000 rankprice vector gives localcost1000*n beforeany modeledguildbenefit; original values and guilddiscount remain unknown.

## Exact linear stat-bonus scaling

`CSRCard::SetRank(rank,p)`0x869c70 stores p atcard+0x28. When rank changes it calls GetCardRankUpBonus(rank) at0x869cbe, converts the returnedfloatusing literal **0.01** at0x869cc6..d4 and stores **b=stat_bonus/100** atcard+0x674. No percentage normalization is performed in the source table itself.

`CSRCard::Validate`0x86acd0 computes:

```text
promotion_factor = 1 + (stat_bonus / 100) * rank_up_cnt
```

Proof: s20=1.0 at0x86ad26; copytos22 at0x86ad50; read p+0x28 at0x86ad58 and convertuint32tofloat; readb+0x674 at0x86ad60; fusedmultiply/add0x86ad6a. This factor multiplies three primarycomputedstatfloats at0x86adfe/0x86aed4/0x86af92, storedinto temporary statresults+0x108/+0x10c/+0x104, before other modifiers. It is **linear per creditedmaterial**, not exponentiation, divisionbyC, or a tablefractionalreadyin0..1. Exactstat_bonus numbers remain originalserverdata unknown here.

Changing only p atsame rank still affects this Validate formula because SetRank storesp **before** its same-rankearlyreturn0x869c7c..86; the cached coefficientb remains thecurrentrank's coefficient. A reconstructed server can preserve EXP on a partialaction and let native Validate apply p's linearbonus, but that **EXP policy** is not independently recovered by this formula.

## Preview arithmetic is not the missing original server threshold

UpdateRankupInfo creates a cloned analyzer, calls **SetPromotion(L)**0x1039daa, then compares GetSrcCnt() withL at0x1039db0..b6. Its equalbranch resets promotion0, setslevel1, and increments previewrank0x1039db8..dd2. Based on the separately verified getter, equality reduces to **p==0**, not L==C. This unusual clientpreviewcondition must not be relabeled as a serverpromotion threshold. It can show a4-star previewbefore allthree sources are selected, matching the screenshot's fadedbadge.

OnButtonClick checks newsourcecountpositive at0x103a43a..440 and gold; no native maxlevel/sourcecapacity/server-grade transition is inferred merely from that earlycheck. RequestRankUp sends target+sourceids+is_tuto, while callback accepts explicit servercurrentrank/p/EXP. The **server owns the transition**, and no original partialresponse was captured.

## Best-supported reconstruction, with honest labels

**[INFERRED servermodel]** For same-grade sources, credited p is naturally advanced by n, and requiredcapacityC defines finishing thegrade:

```text
if p+n < C: rank stays r; rank_up_cnt=p+n; EXP preserved
if p+n == C: rank=r+1; rank_up_cnt=0; EXP resets tolevel1threshold
```

This is consistent with credited placeholders, linearbonus and total same-grade materialrequirement, but **not proved originalserverarithmetic**. Handlep+n>C by explicitlocalrefusal rather thaninventing overflow/multigradepromotion. Ordinarymaxlevel prerequisite, samegrade sourcepolicy andC=currentstarcount are communitysupported, while originalXP/prices/bonuses remainfixtures unlesscaptured.

This inference can support a broad playable revival with provenance, but it must not be presented as a recovered original partialwireoutcome. Preserveownedtrainedskills, ownership/decks and idempotent consumedsourceledger; return the exact recovered rank/p/EXP pairs and numericremovedIDs in `rank-up-contract.md`. Nativecontrol should compare p/strength/EXP afterone-sourcepartial, relaunch, then finishremainingmaterials; the two previewpictures alone cannot complete that verification.
