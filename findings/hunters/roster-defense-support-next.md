# Lowest-ID Defense and Support additions

2026-10-04. Read-only catalogue/raw-table/filesystem research; live community metadata cross-check through MediaWiki API. No source/runtime/original edits.

**003 Nene and004 Tyltyl are the correct lowest-ID additions**, completing the four-role roster beside preserved001 Lantern/Bomber and002 Mowgli/Offense. Do not repurpose002 or remove its reference: persisted owned Mowgli instances depend on it.

##003 Nene — Ice/Defense

- Lookup id **003**, art prefix **C003**; title **Walking Disaster** [RECOVERED CHAR_STR_RO003|TITLE]. Display name Nene, native rarity3, Ice/Defense [COMMUNITY-SOURCED, live [Nene wiki](https://blustone.miraheze.org/wiki/Nene) API Infobox cross-check]. Local role text/tags corroborate Defense.
- Wire **attr2, role2** [RECOVERED native numeric enums, `analysis/research/card-enums.md`, SRAttribToString/SRGetRoleDesc].
- Active: **3 Rage**, direct damage to **frontline enemy** [RECOVERED `all-tables.json` ->SKILL_REF_RO keys003|1|0 and003|1|1]. Formula `-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000`; tag HARD_HIT fromSKILL_TAG_RO003|1.
- Follow-upslot2: enemy stun and own attack-speed buff. These are recovered descriptions, **not numeric effect-wire definitions**. Defense is a frontline skill role; this matches community role rules and contrasts Tyltyl's rear-only active.
- [VERIFIED files] C003.jet **1014062bytes**, C003_Q.jet50813, C003_EFT.jet1965295, C003_SND.jet133882. Base RW animation data contains exact **C003_SK1/C003_SK2** and **C003_E01..E05/C003_EC** references.

##004 Tyltyl — Fire/Support

- Lookup id **004**, art prefix **C004**; title **World's Best Cook** [RECOVERED CHAR_STR_RO004|TITLE]. Display name Tyltyl, native rarity1, Fire/Support [COMMUNITY-SOURCED, live [Tyltyl wiki](https://blustone.miraheze.org/wiki/Tyltyl) API Infobox cross-check]. Local role text/tags corroborate Support.
- Wire **attr1, role4** [RECOVERED numeric enums].
- Active: **4 Rage**, heals the **frontline teammate**; recovery increases with defense [RECOVERED SKILL_REF_RO004|1|0 and004|1|1]. Formula `stat*(value+value_up*skill_level)/100`; tag HEAL fromSKILL_TAG_RO004|1. Which stat/effect enum the native evaluator uses must be pinned separately; don't infer it only from variable name.
- Follow-upslot2 buffs frontline critical chance; slot4 has50% chance for four-second heal-over-time plus harmful-effect immunity [RECOVERED text]. These later slots must remain gated by supported reference/instance eligibility, not enabled merely because Tyltyl's active exists.
- [VERIFIED files] C004.jet **1246194bytes**, C004_Q.jet52685, C004_EFT.jet1656397, C004_SND.jet97064. Base animation data contains exact **C004_SK1/C004_SK2** and **C004_E02/C004_E03/C004_EC** references. No C004_E01 literal was found in that RW data; do not invent it from the adjacent hunter's naming.

## Availability and implementation boundaries

Preserved PAD root: `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets`. **Exact CUT_003.jet andCUT_004.jet are absent** in this root and the extracted base-APK asset root. Differently numbered CUT_E* files do not establish either hunter's cut-in binding. Base animation, portrait, effect and voice families exist, but **cut_in_id/icon_id bindings remain unknown**. Blank explicitly provisional cut-ins are preferable to naming nonexistent CUT_003/004; correct effects/rendering still require native control.

Original HP/ATK/DEF, damage/heal magnitude, cooldown and numeric follow-up buff values are unknown. The original skill proper names were not recovered in these local rows; truthful effect descriptions can be displayed without inventing named moves. Catalogue native rarity is distinct from the replica's current rank1 starter policy. Publishing rarity3 Nene as an owned rank3 card requires compatible rank3 stat/level fixtures; cloning rank1 rows does not silently establish original Nene balance.

For a subsequent additive implementation: keep001/002 references and existing inventory serials, add003/004 references/art and allocate any new ownership beyond all account-used serials. Preserve persisted starter_cards/decks rather than recreating starterInventory over an existing account. Actual grant/migration policy is a separate server decision. Serve only checked files; verify four distinct role cards in inventory and native training/party UI before claiming the four-role roster works.

Raw evidence is unchanged: `analysis/recovered-data/leveldb-tables/all-tables.json` ->CHAR_STR_RO/SKILL_REF_RO/SKILL_TAG_RO; EN projections `skill-ref.tsv`, `skill-tag.tsv`; dossiers `analysis/catalogue/cards/003.md`, `004.md`.
