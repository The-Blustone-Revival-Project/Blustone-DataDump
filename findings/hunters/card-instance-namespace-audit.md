# Owned card instance namespace audit

2026-10-08. Read-only source and retained native evidence audit; no server/device/state changes. Root supplied live proof that CB0102 generated right serials5/6/7 overlap owned left serial5, and the global serial map resolves5 to left C004. This report does not independently reproduce that live observation.

## Finding and preferred implementation

The smallest consistent server fix is an explicit, versioned **owned-instance identity migration**, coupled to the same namespace for new fixtures and future recruitment. Preserve every existing card record except its `inst_id`; apply a bijection to every stored card reference. This changes identifiers, not ownership, training, stats, rewards, or economy. It must not be an account reset or roster reconstruction from bootstrap defaults.

A modest reserved base such as1,000,000 is a local namespace policy, not a recovered production allocator. Map each legacy positive owned serial `id` to `base+id`, preserve0 as the empty sentinel, and reserve low generated Episode serials. This candidate stays below signed32 and the Search helper900,000,001 for the current small roster. Validate the entire mapping and allocator bound first; do not silently map already migrated IDs again. A persisted version marker distinguishes legacy and migrated saves. A base alone cannot prove that all future native actor allocators avoid collisions: prove CB0102 runtime after reload, then audit ordinary/Search/arena generated ranges.

This is preferable to a wire-only alias layer: that layer would need complete bidirectional translation of every request/response, numeric object keys, persisted replay receipts and defaults. A generic recursive `inst_id` replacement would corrupt **item instances**, which share the field name but have a separate inventory and allocator. Numeric arrays may be card IDs, item IDs, supply IDs or unrelated metrics. Missing any one edge creates silent ownership disagreement. Keeping aliases accepted forever also risks stale requests reaching newly assigned identities.

Changing only the fresh-account namespace leaves the current account broken. Changing only selected party IDs leaves low recruited IDs available for later parties and allocator collisions. Neither fulfills revival of existing progress.

## Complete stored card reference surface

Source `server-ts/src/game.ts` defines these identity-bearing fields:

- `starter_cards[].inst_id` and `recruited_cards[].inst_id`: preserve all other enumerable fields, including ref_id, EXP, rank, partial rank credits, locks, skills, skins and equipment.
- `leader_inst_id`: map by exact ownership; reject missing/unowned leaders rather than synthesizing one.
- `decks[].list`: all deck types, ordered five slots; preserve zeros, type and order.
- `active_battle.deck_inst_ids`: ordinary attempt snapshot, including retained completed snapshots. Preserve battle ID, times, AP spent/refund ceiling and outcome. Prefer activating migration while no battle is active; never drop an attempt to permit migration.
- `arena.active.deck_inst_ids` and `arena.last_result.receipt.card` **decimal object keys**. Preserve signature and all receipt pairs; signature currently hashes metrics, not card IDs, so identity rekeying does not require changing it.
- `search.active.deck_inst_ids` and `search.last.attempt.deck_inst_ids`: map both pending and historical snapshots. Search helper_id is a string identity and capsule_inst_id is an **item**, so neither is remapped.
- `next_card_inst_id`: move with the old monotone counter and enforce greater than every resulting owned serial. Preserve allocation gaps; taking only maxOwned+1 may reuse a consumed historical serial.

No further owned card serials occur in LocalGameState. `card_book` is keyed by **ref_id**, not instance; leave it untouched. Missions and progression use stage/reward IDs. Mail currently stores no card attachments or card instance references (`mail.ts` search found none). Special Supply `target_inst_id` arrays are supply entries, not cards. Item arrays, item receipt IDs, `next_item_inst_id`, account pvid/session/token/device identity and other state must remain byte-equivalent in value.

## Publication and mutation edges

`state.ts` inventory publication uses the stored owned arrays. `partyDeck` publishes ordered inst_id_1..5. `ownedPartyProfile` builds lobby and real-account `/world/GetUserDetail` flat profiles. It is also the material source for leader/party EXP fields. `user.leader_inst_id` is separately emitted in lobby.

Critical hardcoded defaults:

- `bootstrap.ts:259..274`: starterInventory uses1..PARTY_SIZE plus the recruit fixture; FIXTURE_GACHA_FIRST_INST_ID is length+1.
- `game.ts:258..282`: initialMembers and leader explicitly assume card1. These must select the namespace's actual captain instance. Changing only starterInventory leaves fresh leader/deck invalid.
- `bootstrap.ts:321`: partyProfile sets leader and all numbered serials to1.
- `state.ts:94..103`: ownedPartyProfile overrides leader and **positive** numbered deck slots only. Empty slots retain partyProfile's1. After migration this publishes a stale low serial with fixture ref_id001 rather than an owned leader fallback. Make every owned profile suffix resolve a real mapped owned card (positive slot or actual leader); keep authoritative deck zeros untouched. Nonowned compatibility profiles need their own explicit policy rather than accidentally adopting an account migration.

All implemented card mutation handlers look up numeric IDs against stored ownership: SkillUp, MultiSkillUp, RegisterDeck, CardLock, LevelUp and RankUp. Their receipts publish actual IDs; level/rank consumption removes source IDs and cleans presets. Protected references include leader, selected deck types, ordinary active battle, arena active and Search active. They work with high IDs after a complete state migration. RankUp intentionally refuses legacy real source IDs below rank capacity because native treats them as synthetic credits; raising the namespace removes this accidental small-ID edge without changing rank rules.

GachaPremium allocates at max(next_card_inst_id,maxOwned+1), publishes identical inventory/result IDs and persists the counter. Its current allocator lacks a safe-end/reserved-helper bound before debiting currency. Add the same capacity guard as trace exchange **before** currency mutation if the namespace introduces an upper bound. `trace-exchange.ts` already checks safe next/end and crossing SEARCH_HELPER_SERIAL before consuming traces. Both allocators must share the namespace limits rather than diverge.

MissionStart stores optional deck_inst_id_1..4 directly after safe-positive parsing; it does not verify ownership there. For migration, quiesce the existing client and reload the native account cache so old request IDs cannot be accepted as current party snapshots. Strengthening ownership checks is appropriate separately; do not introduce a permanent low-ID alias without defining rejection behavior for stale packets.

Arena deck publication, auto-copy from case1 and completion EXP object keys are derived from migrated state. Arena's rival is a separate nonowned fixture **9,000,001,001** and pvid9,000,001; neither should be mapped. Search helper serial **900,000,001** is separate. Search's Begin guard already rejects ownership/helper overlap and maxOwned-based generated range overlap; preserve it and keep the owned allocator below the reserved helper.

## Persistence and validation traps

`normalizeLocalGameState` currently accepts positive safe integer card IDs, all positive safe deck slots, leader as a safe integer (no owned-leader validation), and next_card_inst_id>=1. It filters malformed owned records instead of throwing; do not use that filtering to justify a lossy migration. Validate raw roster identity first so malformed cards cannot vanish during migration.

`ServerState.restore` normalizes, calls assertOwnedCardCompatibility, then sets gameByPvid. Compatibility checks actual duplicate IDs/reference existence and deck ownership; its initial bootstrap-ID set additionally rejects recruits colliding with configured starter IDs, independent of stored starters. It does not validate leader ownership, active/historical snapshots or upper namespace capacity. Put migration at a clearly defined restore boundary before compatibility validation, then validate the full transformed graph. `pendingGameMigrations` currently marks missing legacy fields and persists on `gameFor`; extend this mechanism explicitly or atomically persist a validated schema migration before serving account responses. Do not rely on restart to implicitly rewrite IDs through fallback defaults.

Persist uses a single writer and rename snapshot strategy. Root should retain the private pre-migration file, stop the verified replica writer before any offline operation, and compare pre/post state with card IDs erased/remapped to prove every other field unchanged. A pure migration function with no file access is easiest to test. Tests should cover idempotence, legacy/high mixed ambiguity refusal, consumed-ID allocator gaps, zeros, all deck types, arena receipt keys, Search historical snapshots, invalid owned references, overflow/helper collision, and write-failure behavior.

## Native numeric contract and evidence limits

Retained `analysis/native-card-inventory.txt:35..66` shows CSRCard::parse G8680a4 reads inst_id, accepts native integer64 JSON values directly, uses strtod for string/float alternatives, and stores eight bytes at card+10. `analysis/research/mission-deck-contract.md:28` records uint64 instance serialization; `episode-actor-material-owner.md` records GetSerial G99abb8 low/high words and global-map serial low/high key. JSON numbers must remain positive exact JavaScript safe integers. A candidate below2^31 is conservatively easier to validate than relying on all consumers handling near2^53 correctly.

Existing source deliberately uses Search helper900,000,001 and arena rival9,000,001,001, demonstrating author intent for wider IDs, **not native validation of every high-ID path**. No original server card-inventory export with actual production serials was located in the bounded retained evidence lookup; catalogue cards.json is reference data, not owned inventory. This report does not claim production allocation policy or inspect private account/cache bodies.

After implementation, root must verify native inventory/leader/deck reload, exact global CB0102 front-map pair/camp/resource identity and rendered M022 body, then real battle inputs/outcome. High-ID server tests alone do not prove the invisible-body defect fixed. Preserve original Episode descriptor, stats and resource graph.
