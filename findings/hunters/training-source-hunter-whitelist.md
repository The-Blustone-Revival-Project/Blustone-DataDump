# Native training-source hunter whitelist

2026-10-04. Original library, read-only Ghidra constructor101f9bc and
predicate d3dac0. No reference publication, client patch, grant or UI action.

CSRPopupSearchStuff constructor makes two rank-keyed string vectors:

- Rank1:006,007,011,014,016,017,018,019,020 (nine strings, map key1).
- Rank2:005,013,015,021,024,025,030,032 (eight strings, map key2).

Exact relocated strings and vector/key insertion appear in
ghidra-search-stuff-whitelist.txt / literals.txt / instructions.txt. Its
remove_if predicate removes a reference not present in the requested vector.
All currently published IDs001..004 are excluded. This is sufficient to
explain their absence from the two training-source lists; do not add guessed
base.rank fields to fix it.

The earlier rank filter is CSRCardInfo.GetMinRank (minimum published stat rank),
cached at info+44 by SetCard; it is not owned-instance grade or recruitBirthRanks.
A new rank2 source reference therefore needs its stat map's supported minimum
at2. Existing legacy references/owned grades must not be changed for this.

Recovered catalogue matches the native groups:006 Sylvester is one-star Fire
Offense;005 Gerard is two-star Ice Defense. Both have recovered C005/C006 art
families. Publishing these two references with corresponding item/source data
is a small prospective first/second-group expansion; no new ownership grant is
needed to define a catalogue reference. Combat magnitudes/skills remain missing.

Recovered GetItem contract: ret_data.trace[] has item_id,order,type,source_id,
thumb_id. Type3 performs normal campaign navigation through actual stage/area
links. It requires existing stars on source_id, so a stage8 row cannot enable
the first stage8 win. An already-cleared stage7 row can lead to the existing
campaign map and normal stage8 selection. Such an item/drop association would
be an explicit local fixture unless independent original drop evidence is found.
Empty thumb_id has a positive native guard; no new art is required for that
trace-row thumbnail. Item-detail entry, trace ownership/collection behavior and
native source navigation still need implementation/runtime validation.

Next step is coherent reference/art/source expansion with preserved originals,
not whitelist mutation, a forced scene jump or a fake stage/tutor completion.
