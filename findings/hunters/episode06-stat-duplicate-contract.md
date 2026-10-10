# E06 duplicate fixed Karl actor: native first-row index retained

2026-10-09. Root readOnly/noanalysis Ghidra on original library, no runtime,
original resource, stat or inventory changes. Existing E06 material audit records
original STAT array rows143/144 with the same idCB0601_012_1, both used by
CB0601/CB0602 as a fixed camp0 Karl. E05 CB0502_012_1 is a different identity.

CSRMEpisode.ActorParser G00b1bbe0 iterates the supplied JSON array in order,
reads literal id (resolved keys file), sets the integer ordinal starting0 and
passes (id,index) to unique tree insertion at model+0x68. Instructions
Gb1bca6 store ordinalr9 in the pair; Gb1bcba calls G007e3a14. It increments
the ordinal and advances the original JSON iterator; no overwrite follows.

G007e3a14 __emplace_unique_key_args<string,pair<const string,int>> calls
__find_equal. Only if its returned node slot isnull does it allocate0x20 and
store the incoming integer at node+0x1c. Existing-key branch returns that node
with inserted=false and writes no replacement integer. This establishes
first occurrence wins, not merely an assumption from the template name.

Scope: first insertion wins for this index's lifetime. ActorParser does not
clear its tree; FindActorRef checks its parsed-card cache first. Row143 selection
therefore applies to a fresh index populated from the preserved original array.
Changed/repeated imports or previously populated caches would additionally need
their initialization/invalidation path verified. Current original data is kept
unchanged; no cache reset or insertion rewrite is part of this reconstruction.

CSRMEpisode.FindActorRef Gb1c2ac checks parsed card-info cache+0x50, lazily
loads stat JSON/model+0x78 and calls ActorParser when needed. It finds the same
index tree at+0x68, reads node+0x1c and JSON.at(index), then ParseActor Gb1bd5c
and caches the parsed result. Thus original duplicate row143 is selected,
row144 remains in original data but is not selected by this lookup.

Selected original row143: HP1150/ATK750/DEF550/SPD7/crit33%/critdamage200/
block13%/blockreduction40/regen30. Skill1 cooldown5000/cost3 and original effect
-2000; skill2 original stat5 buff40/duration4000; skill4 original stat7 multiplier
1.0/duration4000. Later row144 DEF533/crit31/critdamage210/regen26/cooldown6000/
multiplier1.2 is retained as historical source but not promoted as live selection.
This is native import/lookup semantics plus preserved source order. Direct live
battle-field corroboration remains pending; no ordinary balance retune or
owned Karl grant follows. Preserve the original package and both rows.

Evidence: ghidra-e06-stat-index.txt, -keys.txt, -instructions.txt and
ghidra-e06-stat-unique-insert.txt. G addresses include original ELF+0x10000;
all literal reads used relocated Ghidra memory, not flat-file placeholder words.
