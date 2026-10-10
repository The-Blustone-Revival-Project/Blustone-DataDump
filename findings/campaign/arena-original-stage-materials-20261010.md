# Original Arena stage/material evidence

2026-10-10. Targeted read-only existing local JSON/CSV/native strings and curated
research. Only this report written. No runtime/ADB, Ghidra, network, new visual
stat hunt, account/source edits or fabricated stage row.

## Positive original b_00_01 evidence

Root's qualified current StageConfirm snapshot proves scene0x24 and scene+788
string **b_00_01**. This is current native selection, not an inferred ID from
art. The exact native literal also exists at ELF1d80650 in native-all-strings.

An original shipped numeric block already exists locally:
**analysis/in-game-stats/leveling-chunk09.json:127–133**, exported from
LEVELING.jet record9, contains:

    bonus.stage.b_00_01.value:
      hp=1.1, atk=1.1, def=1.1, ct_chance=1.0, ct_dmg=1.0
    bonus.stage.b_00_01.cards: ["051"]

catalogue-report.md sections4.2 and catalogue/INDEX.md section5.3 already
document this block and identify051 as Beckhen. This is an **actor-specific
stage bonus**, not a /reference/GetStage INFO row. It supplies no ap_cost,
environment/resource binding, title, drops, rewards, battle fee, base Hunter
stats or unconditional buff for every arena rival. Native application requires
the exact selected LEVELING mode and bonus consumer; copied numerical tuples
alone do not prove the current one-Mowgli fixture receives any multiplier.
Do not add Beckhen ownership or publish these coefficients as rival base stats.

The older catalogue recommendation to add a b_XX_YY stage list is speculative:
this positive corpus proves **one key b_00_01**, not an enumerated complete
b_* catalog. No standalone original GetStage record for b_00_01 was found in
the targeted existing recovered-reference/in-game-stats JSON/CSV search.
That scoped absence is not proof that no original source can recover it.

## Original arena scenery exists; selection binding is missing

Original environments.csv row99 is positively documented by
episode-first-combat-assets.md and episode04-entry-materials.md:

    99,배틀,STI099,111,-5,160,11,-10,273,111,20,648,111,30,840,111,-5,1000

The title means Battle and prefix is STI099. Original ST099.jet is
1,252,287bytes, SHA256
e99d2c7df04f4c32f539d4b79d44791a69f97046dd61b48d4a89211a72f50e81;
25 exact walked records include ST099_BG, STI099B_01, STI099_A01..E01 and
AT ST099BG/STI099B/STI099_A1..E1. Original AT-to-sprite graphs, rather than
guessed numeric suffixes, are recorded in episode04-entry-materials.md182–195.
AGENTS168 already verifies these genuine arena layers rendered during native
E04 CB0401. Current profile retains that material; no new arena art must be
invented merely to have a visually plausible background.

**No b_00_01→environment99 binding is established by these data.** The row's
human title and a b_* stage key are different namespaces. Original Episode
COMBAT.game_res_id99 independently binds Episode environments, but that does
not supply ordinary CSRGameBattle's environment selection. Root's separate
CSRGameBattle consumer investigation should close this before defining an
arena stage res_prefix or claiming Fight Club battle material completeness.

## Present practical boundary

Verified now: original Beckhen entrance/dialogue, Arena Waiting Room,
clock/rank/BP display, repaired deck5 Defense rendering and fixture rival
preparation. The preparation fee0 and selected b_00_01's absent reference row
still require consumer attribution; arena-confirm-fee-next-20261010.md records
the Stage INFO cost producer and separate positive-BP admission.

No original stage row or original economy should be synthesized from the
bonus block or E04 environment. Preserve missing fields explicitly; reuse
already recovered original art only after actual CSRGameBattle binding is
proved. If a local metadata adapter is later necessary, label its policy
separately from the recovered bonus/environment rows and retain the original
native lookup evidence. Do not silently copy an expedition row into b_00_01.

No web search was needed: exact internal bonus and environment evidence already
exists locally, whereas ordinary game footage does not expose encrypted
GetStage IDs/fields or their native ownership/binding. A fresh web/video search
would become useful for a specifically unresolved visible behavior, not for
manufacturing internal reference fields from arena-looking backgrounds.

## Exact LEVELING_B versus LEVELING_E follow-up

A fresh read-only walk of the original preserved PAD LEVELING.jet, using the
existing extract-jet-chunk.py walker and uint64 header+12 native base38 name
alphabet, verifies package18524bytes/SHA256
ba73fff17002cc94f7f1a98bf657be1bef042283051a5b92c395347006d3c57e.
Named records are:

- ENVIRONMENTS: record5/header6272, inflated SHA256
  4e686c594981eaa09af4dd4dbf45e7df883fd56ae8e8ccd6157cf6929c5e379c.
  CSV has51 lines including its header; exact row99 agrees with the row above.
- LEVELING_B: record9/header8350, inflated SHA256
  f2d787d0a5a1a28c698e314146b9677259497530979503d364387110d9b037ce.
  Parsed JSON exactly equals the existing leveling-chunk09.json export.
- LEVELING_E: record11/header10309, inflated SHA256
  9286d223afc9d7c781544bd649cb8934efb200ef704fd4dd97caa5d6a00af8a8.

**Neither B nor E JSON has an environment/bg key or envMap.** Both contain
combat timing/SP/fever/actor/left/right/waiting/bonus configuration. B supplies
the b_00_01/051 bonus; E's bonus.stage is empty. The occurrence of numeric99
elsewhere in configuration is not an environment identifier.

The environment map is global **CSRStaticData+150**, loaded separately from
ENVIRONMENTS CSV, not a per-mode leveling_b.envMap. environments-recovery.md
section3.2 traces OnInitBackground→CSRDataMgr.GetStaticData→map+150→find(key)
and original ENV_INFO prefix/layout. Thus original environment99 is available
to both mode consumers; no B/E environment-catalog difference explains or
recovers an Arena stage mapping.

Root's new CSRFC InitBeforeOpen G941518 exact leveling_b load closes mode
selection for that class. It does not make global environment99 a recovered
b_00_01 res_prefix. A separate unlinked b_00_01 GetStage adapter may use
original99 art under an explicitly **local binding policy** if required by
the native missing-stage path. AP cost1 must remain the existing labeled local
BP policy, identity modifiers local, zero rewards local absence; none is
recovered from the original B JSON. Do not put this adapter in campaign area
links, change its actor-specific bonus table, or clone expedition rewards.
