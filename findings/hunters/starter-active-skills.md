# Starter active skills: Lantern001 and Mowgli002

2026-10-04. Read-only local/public research. No server, APK, adb, Ghidra, or original asset changes. Native parser findings below are citations to existing native research, not a new effect-parser reconstruction.

## What the originals actually describe

**Lantern001** [RECOVERED shipped text]: active slot1 spends **4 Rage**, damages the **frontline enemy**, and **penetrates Immunity**. Slot2 adds a timed defense debuff; slot4 has a **50%** activation condition, adds another immunity-penetrating hit and persistent defense reduction. Slots3/5 are battle-start team attack/critical-chance passives, not extra player buttons. Original numeric damage/debuff magnitudes and durations are absent from these text tables.

**Name:** community Korean wiki labels Lantern's first special **성실한 지원 사격**; an English gloss is **Diligent Supporting Fire**, explicitly a translation, not a recovered English display string. [COMMUNITY-SOURCED] [Namu Bomber page, Lantern section](https://d.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0/%ED%8F%AD%EA%B2%A9%EC%88%98#s-2.3.1). The shipped SKILL_REF table has effect prose, not this named heading; SKILL_EFFECT_RO only supplies slot2/4 summary labels for001. English original name therefore remains [UNKNOWN].

**Mowgli002** [RECOVERED shipped text]: active slot1 spends **3 Rage** and applies **total bleeding damage over4 seconds to the frontline enemy**. Slot2 describes another4-second bleed; slot4 has **40%** activation probability and timed defense reduction. Slots3/5 are own attack buff at battle start and periodic immunity, not separate selectable specials. The3-second periodic immunity cadence is recovered text; its duration is a missing parameter.

**Name:** [UNKNOWN] actual first-special display name in English/Korean. Live [Mowgli community wiki](https://blustone.miraheze.org/wiki/Mowgli) has an activation/effect table without named skills. The [Namu Offense page](https://d.namu.moe/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0/%EA%B3%B5%EA%B2%A9%EC%88%98#s-2.2.3) also has blank skill heading fields for Mowgli. It describes rapid slashing/bleeding, but does not establish an original name. “Bleeding attack” would be an honest local description, not a recovered proper name.

## Exact immutable local source records

Primary raw source: `analysis/recovered-data/leveldb-tables/all-tables.json`, `tables.SKILL_REF_RO`. These records use the original wrapper **`{key, json}`**, with JSON payload fields **SUB_SERIAL, FORMULAR, IS_FLOAT, EN** plus locale fields. The existing EN-only TSV projection is `analysis/recovered-data/leveldb-tables/skill-ref.tsv` with columns `skill_id,row,col,FORMULAR,IS_FLOAT,SUB_SERIAL,EN`. Literal `nan` is source text, not a usable numeric magnitude.

Relevant records (EN projection, preserving original field spelling/types):

```json
[
  {"key":"001|1|0","json":{"SUB_SERIAL":"0","FORMULAR":"nan","IS_FLOAT":"1","EN":"Uses 4 Rage Gauge when using a skill."}},
  {"key":"001|1|1","json":{"SUB_SERIAL":"0","FORMULAR":"-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000","IS_FLOAT":"0","EN":"Deals [value] damage to the frontline enemy.\\nThis damage penetrates Immunity."}},
  {"key":"002|1|0","json":{"SUB_SERIAL":"0","FORMULAR":"nan","IS_FLOAT":"1","EN":"Uses 3 Rage Gauge when using a skill."}},
  {"key":"002|1|1","json":{"SUB_SERIAL":"0","FORMULAR":"(-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000)*5","IS_FLOAT":"0","EN":"Deals a total of [value] Bleeding Damage to the frontline enemy for 4 seconds."}}
]
```

`rank`, `stat`, `value`, `value_up`, `skill_level` are **variables**. No original numeric `value`/`value_up` is present here; what stat the formula's evaluator supplies is not established by its name alone. The negative sign and scale10000 belong to the shipped formula. Mowgli's multiplier5 establishes a total-formula multiplier; it **does not independently prove five runtime ticks or an0.8-second tick interval**.

Additional exact keys:

- `tables.SKILL_TAG_RO`, `001|1`: `{"TAG_KEY":"HARD_HIT,INVIN_BREAK"}`.
- `tables.SKILL_TAG_RO`, `002|1`: `{"TAG_KEY":"BLEED"}`.
- `tables.SKILL_REF_RO`, `001|2|0`, `001|4|0..2`, `002|2|0`, `002|4|0..1`: follow-up effect formulas/conditions described above.
- `tables.SKILL_EFFECT_RO`, `001|2`: NORMAL/ANGRY both **C001_DLG01**, EN **Penetrate Invincible\\nDefense▼**. `001|4` similarly has Extra Damage/Defense summary. These are **dialogue/effect labels**, not proof that C001_DLG01 is a cut-in id.
- `tables.SKILL_EFFECT_RO`, `002|2`: NORMAL/ANGRY **nan**, EN **Bleed Damage**; `002|4` EN **Defense▼**. No slot1 proper-name row exists in the extracted records.

Derived readable card dossiers: `analysis/catalogue/cards/001.md`, `002.md`. Raw originals were not modified.

## Eligibility, costs and timing: established versus missing

[RECOVERED] Native role mappings (`analysis/research/card-enums.md`): Lantern Bomber=**3**, Mowgli Offense=**1**; native `SRCanUseSkillAirShip` returns true for roles3/4. This establishes Lantern as an airship-skill role. It does not establish every skill activation predicate.

[COMMUNITY-SOURCED firsthand preserved guide] `recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md`, early glossary **Bomber** states a bomber cannot use its special from the frontline. The **Support** glossary says the same for healer support. Therefore Lantern must be available from the rear/airship, while Mowgli is the ordinary frontline attacker. The current starter lineup can support that division; treating Lantern as another frontline Offense would contradict its recovered role.

[RECOVERED costs] Lantern4 and Mowgli3 are directly supported by shipped EN text. Current reference `cost:0` is a neutral fixture, not an original value. Rage maximum10 is also recovered in LEVELING data (`catalogue/INDEX.md`); the exact player's current Rage/gain rate remains runtime state.

[UNKNOWN originals] Active special `cool_time` for either hunter; original target_rank values; complete predicates concerning rank/skill level, stun/hold, current camp and tutorial restrictions; effect enum/target enum values and wire resource bindings. `base.cool_time:1000` is an existing fixture, not evidence of a1-second original special cooldown. Native division by1000 in the hunter backend path proves units for that path (`stage3-input-gate.md`), not either hunter's original active cooldown.

[FIXTURE current source] `fixtureSkillSlots()` gives types1..5, target_rank1..5, skill1 instance level1, remaining skill levels0, cost/cool_time0, empty effect arrays and empty cut-in/icon strings. The five rank gates are a local unlock convention. No original ability damage is implemented by these neutral rows.

## Native-compatible record versus original gameplay effect

`analysis/research/card-stat-panel-crash.md` recovers `SRSKILL_INFO::parse` and SetCard's skill-map insertion. Parser-compatible **outer record** requires:

```json
{"target_rank":1,"type":1,"name":"...","desc":"...","effect":[],
 "cool_time":0,"cost":4,"crt_chance":0,"cut_in_id":"","icon_id":""}
```

This illustrates shape only: **target_rank1, cool_time0, crt_chance0, blank resources, empty effects are fixtures**, cost4 is recovered for Lantern. `type` is the map key (parsed object+0x28); `target_rank` is separate metadata. All five types must remain present even when locked because the info popup resolves all five. String fields are converted unconditionally.

`effect:[]` structurally skips the nested effect parser. It does **not** implement either active. Shipped SKILL_REF prose/formulas and TAG_KEY strings are not a recovered substitute for native `effect_type`, `target_type`, `target_stat`, repeat/proc timing, values and target selection. Do not paste raw text-table objects into `effect[]` or guess integer enums.

## Available art and actual binding gap

Filesystem verified under `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets`:

- Lantern: **C001.jet**1054905bytes, **C001_Q.jet**50808, **C001_EFT.jet**1383938, **C001_SND.jet**148313, **CUT_001.jet**622980.
- Mowgli: **C002.jet**739583bytes, **C002_Q.jet**49298, **C002_EFT.jet**5001859, **C002_SND.jet**128477, **CUT_002.jet**1938440.

Base animation prefix C001/C002 is established for the cards. CUT_001/CUT_002 are **candidate special cut-in packs by filename/identity**, not proven `cut_in_id` values. The existing JET listing helper returned numeric/unresolved entry names for CUT packs and no EFT names; byte-faithful chunk probing also showed mismatched length interpretation on some CUT chunks. This pass therefore does **not** claim a valid internal animation resource name. Find the resource-map binding before publishing a nonempty cut_in_id/icon_id. Filename existence alone is insufficient.

Live MediaWiki API (`/w/api.php?action=parse&page=Lantern|Mowgli&prop=wikitext&format=json`) supplies demo links: [Lantern video](https://www.youtube.com/watch?v=1vv6xcA-3WQ), [Mowgli video](https://www.youtube.com/watch?v=eVBF9JNP5QY). YouTube fetch was throttled/unavailable in this pass; neither video was visually verified. These are leads, not evidence for numeric damage/cooldown or exact cut-in resources.

## Tutorial implication

The current native mode5 is `CSRTutorialMStageSkill`; existing `stage3-input-gate.md` establishes that its press override still forwards to ordinary input. A “Tap anywhere” overlay does not identify which hunter's skill it expects or whether a special was activated. This lane did not recover the mode5 active-skill tutorial selector; systems research must pin that gate and actor role/camp at runtime.

For a coherent first reconstruction, Lantern's requested active behavior is rear/airship immunity-penetrating damage spending4 Rage; Mowgli's is frontline bleeding over4 seconds spending3 Rage. Original damage magnitudes, cooldown, enum encoding, target eligibility, and validated resource ids remain the exact blockers to claiming either works. Descriptive fidelity and parser-compatible metadata are useful progress, but neutral effect arrays cannot complete a tutorial that requires a real skill effect.
