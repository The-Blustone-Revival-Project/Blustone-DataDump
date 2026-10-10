# Character expansion: evidence and next implementation

Read-only investigation, 2026-10-03. No adb, Ghidra, server restart, private-state change, or client edit. Sources: current `AGENTS.md` §§15–17; `analysis/catalogue/INDEX.md`; `analysis/catalogue/data/cards.json`; `analysis/catalogue/stats/`; current `bootstrap.ts`, `game-routes.ts`, `state.ts`, `start-server.ps1`, and `patch-card-roster.py`. Asset existence and byte sizes checked directly against the preserved PAD copy.

## Most valuable next step

Fix the existing second-card art/reference integration first, then publish a small configurable base roster without automatically seating those cards in the working mission deck. The current server already publishes card **002 / Mowgli** beside **001**, but `tools/start-server.ps1` defaults to **C001*.jet**. Unless a caller explicitly widens assets, Mowgli's art is absent from the served set. This is a configuration/content mismatch, not evidence of a client parser defect.

A useful initial selectable roster is **001 Lantern, 002 Mowgli, 003 Nene, 004 Tyltyl, 005 Gerard**. All five have real base animation packages. It covers the four community-documented roles (Bomber, Offense, Defense, Support), though the **numeric wire enums remain unverified** and must not be guessed from ordinal order. Card **051 Beckhen** is the best sixth candidate for a separately identified stat-calibration experiment because it has a full level-30 historical stat observation.

## Exact identities and available base art

- **001 Lantern**: Bomber / Fire / rarity 3 [COMMUNITY-SOURCED]; title `First Ever Hunter` [RECOVERED]; prefix **C001**; `C001.jet` **1,054,905 bytes**. Current reference uses the name `%user_name%`, attr/role `1/1`, rank-1 fixture stats.
- **002 Mowgli**: Offense / Lightning / rarity 2 [COMMUNITY-SOURCED]; title `Forgotten Forest` [RECOVERED]; prefix **C002**; `C002.jet` **739,583 bytes**. Current server already has a reference and starter inventory instance; no deck seating.
- **003 Nene**: Defense / Ice / rarity 3 [COMMUNITY-SOURCED]; title `Walking Disaster` [RECOVERED]; prefix **C003**; `C003.jet` **1,014,062 bytes**.
- **004 Tyltyl**: Support / Fire / rarity 1 [COMMUNITY-SOURCED]; title `World's Best Cook` [RECOVERED]; prefix **C004**; `C004.jet` **1,246,194 bytes**.
- **005 Gerard**: Defense / Ice / rarity 2 [COMMUNITY-SOURCED]; title `Invincible One` [RECOVERED]; prefix **C005**; `C005.jet` **1,694,783 bytes**.
- **051 Beckhen**: Offense / Ice / rarity 3 [COMMUNITY-SOURCED, rarity also visually observed]; title `Guardian of Fight Club` [RECOVERED]; prefix **C051**; `C051.jet` **685,106 bytes**.

Each has `_Q.jet`, `_SND.jet`, `_EFT.jet` on disk. Alternate costume packages also exist for 001, 003, 004, 051. Base package + portrait is the narrowest inventory/art experiment; effects and sound families can be added deliberately for combat. Use exact families, not a broad wildcard that unexpectedly brings unrelated or costume content into E_NEW. Adding served assets changes package content and therefore requires a deliberate CDN refresh/test.

**Identity must stay separate from art:** `base.id/ref_id = "003"`, `res_prefix/thumb = "C003"`; not `id = "C003"`. This distinction is already explicit in current bootstrap comments and the recovered catalogue.

## What is recovered versus still missing

`cards.json` has 121 rows: **113 character rows**, **8 non-hunter string rows**. Exclude `901,902,903,904,912,913,914,x914` from playable inventory. All 113 character ids join directly across character and skill tables; each has five skill **slots**, even when the catalogue's `n_skill_slots` count is greater than five because it counts sub-effects.

[RECOVERED] Titles, summaries, victory text, three equipment names and descriptions; skill EN descriptions/formulas, tags, effect display names and rage costs. [COMMUNITY-SOURCED] Display names, rarity, element, race, gender and role vocabulary, with role independently corroborated by local text/tags. **Current bootstrap incorrectly labels Mowgli's name/rarity/element as originating in CHAR_STR_RO**; catalogue provenance explicitly says these are wiki Infobox fields. Preserve the accurate provenance when reusing the JSON.

[UNKNOWN] Numeric attr/role enums; level-1 HP/ATK/DEF for candidates; level/rank growth coefficients; server skill magnitudes/durations; equipment wire-entry shape; awakening/skin contract. Avoid using recovered prose/formulas as if they establish the native `skill[]` or `equipment[]` response shape. Read their parser before filling currently empty arrays.

`051` has visually cross-checked, **Lv30, 3-star, unequipped 2018–2019-era** stats: HP **2879**, ATK **1471**, DEF **1149**, attack speed **8.00**, crit chance **33.00**, crit damage **200.00**, penetration **0**, block chance **14.00**, block reduction **42.00**, elemental enhancement/resistance **5.00/5.00**, regeneration **42.00**. These are not a recovered level-1 row or final 2.8.0.1 balance. How display speed/percent units map onto native stat fields also needs checking. The ATK equipment delta contains **78 unaccounted points**; do not silently use it to derive a growth curve. `010_1` has partial Lv30 stats but requires the unresolved awakened-skin mapping, making it a worse first expansion candidate.

All 15 awakened `_1` rows lack corresponding `Cxxx_1.jet` art. A base-prefix/skin relationship is inferred, not proven. Defer awakened variants, unnamed costume rows, and twelve orphan C5xx art families until their contracts/identities are resolved.

## Existing helper and server pitfalls

**Do not run `tools/patch-card-roster.py`.** It is a historical textual rewrite tied to obsolete single-card markers. It invents `Cxxx` card lookup ids, random modulo role/attr values, invented stats and six starter instances. Its docstring attributes masked SetRefID assertions to empty deck slots, while the current milestone documents them as unexplained. It would either fail its string search against current bootstrap or regress namespace/provenance constraints. Replace its purpose with a normal reviewed implementation rather than adapting its replacement strings blindly.

`BLUSTONE_GACHA_CARD` currently changes only the id while **keeping Mowgli's name, C002 prefix, metadata and stats**. It is therefore not a valid generic selector for Nene or Beckhen. A real selector must resolve every metadata/art field from one catalogue row.

The current server has useful seams: `starterReference`, exported `cardInstance(instId, refId)`, `starterInventory`, gacha counters, and dynamic awarded-card persistence. Preserve the existing instance/deck identities and allocate new ids beyond all persisted inventory ids. `/lobby/GetCardBook` still returns only `{ref_id:001, rank:1}`; expanded ownership should produce corresponding book entries once its recovered shape is maintained. Gacha already routes through a dedicated recovered contract rather than generic fallback.

## Controlled acceptance workflow

1. Add a disabled/small roster setting driven by catalogue metadata with explicit fixture stats, preserving the working 001 reference and deck.
2. Derive or validate served card families from that roster; fail visibly for missing files; preserve all existing stage/battle resource assets.
3. Verify references, inventory, card book and gacha ids agree, and repeated rewards persist without colliding with existing inst_ids. Unit checks establish consistency, not native rendering.
4. Exclusive emulator owner performs one fresh-launch trace plus Build Team/recruitment visual check. Slice logs at the launch marker; no app wipe or original-device use. Roll back the roster dial if the prior six-card boot fault recurs.
5. Only after inventory/gacha art is verified, test user-driven deck changes and actual combat for each new role. Record recovered metadata separately from fixture balance and native verification.

No new public-web search was required for this scoped investigation: this report identifies the already-documented local evidence and its gaps. Prior searches only checked four gameplay videos; their negative result is not proof that additional public video evidence cannot exist. Likewise, documentation's statement that monster stats are unrecoverable from *any* public source is stronger than the limited search supports. Label original monster balance unknown and reconstructed balance fixtures; do not use that claim to forbid future evidence.
