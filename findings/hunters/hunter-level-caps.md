# Hunter rank, character-level caps and compatible fixture expansion

2026-10-04. Read-only local/native research references and live community-source verification. No source/runtime/original changes. **Character levels and skill levels are different tables.**

## New explicit character-cap evidence

[COMMUNITY-SOURCED] [Namu Hunter training section, footnote36](https://d.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0#fn-36) states **“등급에 상관없이 30레벨이 최대.”** Translation: maximum level30 regardless of grade. Footnote37 describes advancement materials and explicitly identifies the pictured target as a3-star Captain.

This gives the historical ordinary-hunter cap schedule **rank1/2/3/4/5 ->level30**, rather than incorrectly borrowing skill caps10/20/30/40/50. It is an explicit community claim, not an original server response. Page last-edit date2026-08-13 does not establish when the game balance originated or prove final2.8.0.1 compatibility. Awakening/awake-step-specific caps remain unresolved; ordinary30 should not silently become a claim about awakened progression.

Independent visual corroboration already recovered: [December5,2018 guide](https://www.caragublu.com/2018/12/blustone-game-guide.html) has **Natalia3★Lv30MAX** and **3★MAX ->4★Lv1** screenshots saved in `analysis/research/public-training/`. See `training-public-evidence.md` for exact image URLs/date. That visual anchor proves rank3 cap30 at that time; the Namu footnote is the newly found explicit all-grade statement.

No accessible official original GetLevel table or version-pinned cap-change notice was recovered. Previous community forum1260/192223 timed out; absence of an accessible source is not proof that archived official evidence cannot exist.

## Natural recruitment grades for001..004

[COMMUNITY-SOURCED, live MediaWiki Infobox and existing catalogue cross-check]:

- [001 Lantern](https://blustone.miraheze.org/wiki/Lantern): natural **3★**.
- [002 Mowgli](https://blustone.miraheze.org/wiki/Mowgli): natural **2★**.
- [003 Nene](https://blustone.miraheze.org/wiki/Nene): natural **3★**.
- [004 Tyltyl](https://blustone.miraheze.org/wiki/Tyltyl): natural **1★**.

These are the characters' community-documented birth rarities, **not an instruction to rewrite existing replica instances**. Owned001/002 currently use the documented rank1 fixture policy. New rank3Nene can use its natural rank only once compatible reference stats and network-level curves exist. Existing001XP100 must remain ownedrank1/Lv2 unless the user explicitly approves a separate progression migration.

## Native curve contract remains unchanged

[RECOVERED] `CSRUserLV::SetLevel`0x109f114 reads `/reference/GetLevel.ret_data.card` rows **rank,level,min_exp,upgrade_exp,sell_price**, all numeric. Rank selects a vector; each row stores level/min_exp/upgrade_exp/sell_price at offsets0/4/8/12, stride16. `training-raise-followup.md` pins the parser and getters:

- GetCardLevel0x10a0b2c walks rows in published order; first min_exp>exp returnsmax(1,row.level-1), otherwise lastrow.level.
- GetCardMaxLevel0x10a0c68 returns **lastrow.level**, not a fixed native30/50.
- GetCardMinExp/GetCardMaxExp index level-1/nextrow respectively; therefore curves must be denseorderedlevels1..30 with monotonically increasing cumulative min_exp.
- GetCardRaiseExp uses source rank/source level **upgrade_exp**. This is sacrifice contribution, not the target's cumulative threshold or skill-up price.

No original cumulativeXP thresholds, sourceXP yields, or per-rank training prices were recovered from LEVELING.jet/public sources. LEVELING power recommendations are not this network table.

## Coherent expansion without changing current owned level

A broader **[FIXTURE]** ordinary rank1..5 curve can target the community-supported30cap. Preserve rank1 **level1 min_exp0, level2 min_exp100** byte-for-byte; require every later threshold>100. Then existing owned001rank1/XP100 still resolves exactlyLv2 through the native getter. Keep existing XP and serials; do not change the instance to naturalrank3 as a side effect of publishing broader references.

Provide each supported rank a nonempty dense30-row vector, and reference stat coverage for that rank/awk_step tuple, before granting a card at it. Higher-rank XP curves/source contributions can remain plainly labeled fixtures; do not imply naturalrarity determines original HP/ATK/DEF. Ascending linear or another local curve is a policy decision, not recovered balance. Tests should pinXP99→Lv1,100→Lv2 for existingrank1; cap=30 per publishedrank; coherent maxExp; and no empty-vector/index faults.

Original cap evidence is now sufficient for a deliberately provenance-labeled ordinary30-level revival fixture. Original XP/gold/stat fidelity and awakening caps remain separate gaps.
