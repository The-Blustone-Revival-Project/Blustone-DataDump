# Episode 6 fixed-stat selection: duplicate closed; STAT rank overrides thumb rank

2026-10-10. Independent read-only audit of existing curated native exports and
bounded Thumb instructions from the original extracted ARM ELF. Only this note
was written. No Ghidra, ADB/UI, Docker, stat visual hunt, original-file changes,
server/account edits, balance retune or grants.

## What is already closed

`episode06-stat-duplicate-contract.md` and its native exports prove that a fresh
Episode index populated from the unchanged original STAT array selects Karl
`CB0601_012_1` row143. ActorParser G b1bbe0 inserts `(id, ordinal)` into a unique
tree without overwriting an existing key. FindActorRef G b1c2ac retrieves that
ordinal, parses the selected JSON row and caches its CardInfo. Row144 remains
source evidence, not the chosen replacement. There is no remaining first-versus-
last-row ambiguity on this fresh-index path.

Karl's selected source is HP1150, ATK750, DEF550, SPD7, crit33%, crit damage200,
regen30, active cooldown5000/cost3. Direct live default-state corroboration and
cache lifecycle remain separate from this source-level selection proof.

## Newly recovered rank selector

The previously unresolved fixed-data overload is `CSRCardAnalyzer::Load(ACTOR_INFO const&)`
at **G86cc60**, distinct from ordinary `Load(shared_ptr<Card>)` G86cf68.
`ghidra-episode-decomp-02.txt` / `ghidra-episode-first-combat.txt` show Episode
MakeStageInst G b23f60 setting flag0x08 and binding explicit CardInfo for fixed
actors. `ghidra-skill-construction-registration.txt` / enemycamp-decomp-02 show
Hunter MakeBackEndActor G9ac2ac invoking this overload when ACTOR_INFO+5c has
bit0x08. This does not depend on guessing class from the JSON `monster` string.

Bounded original-ELF Thumb disassembly now establishes:

- G86cc7a reads ACTOR_INFO+3c/+40 as the explicit CardInfo shared pair.
- G86ccc8 reads ACTOR_INFO+34/+38 as the Card shared pair.
- G86ccfc..cd02 calls CSRCard.Load G869818 with those two shared pairs into a
  newly constructed card.
- **G86cd5e..cd6a calls CardInfo.GetMaxRank G87b364 on the explicit CardInfo,
  moves its result to r1, sets r2=0 and calls CSRCard.SetRank G869c70.**
- G86cd6e..cd82 then copies the supplied card's default/awake overcome values;
  it does not restore the combat thumb rank afterward in the inspected body.

GetMaxRank G87b364 reads vector begin/end at CardInfo+a0/+a4. If nonempty and
the final element has a nonnull stat pointer, it reads that last shared pointer
at `end-8`, then returns its first uint32 field. Its empty/null case returns0.
The shared stat parser G886fc0 writes parsed JSON `rank` to stat+0, corroborated
by `ghidra-stat-parser-first-insn.txt` G88702c and relocated keys. Episode
ParseActor G b1bd5c calls `CSRCardStat.parse(statObject,1)` once and PushStat
once (`ghidra-episode-combat-actors.txt`, corresponding keys file). Therefore
the one fixed Episode STAT row supplies GetMaxRank's value.
This is **last vector element's rank**, not a scan for the numerically largest
rank. No ordering guarantee for a hypothetical multi-row unsorted stat vector
follows from the method name. The actual Episode parser contributes one stat,
so that distinction does not change the original E6 result.

Root subsequently exported `ghidra-fixed-actor-rank-selection.txt` through
read-only Ghidra. Independent review agrees with the ELF register findings:
Load G86cc60 lines31..32 loads explicit CardInfo+owner from ACTOR_INFO+3c/+40;
line70 loads the copied card with both pairs; lines103..104 explicitly call
GetMaxRank then SetRank(value,0). GetMaxRank lines209..227 reads end-8 and the
first stat word without any maximum-comparison loop. CSRCard.Load G869818
lines277..304 copies the supplied card and its rank first, so the later
fixed-overload SetRank is an actual override of that copied thumb-derived
rank. The source-level chain is now closed by both independent methods.
No runtime readback has been performed for this continuation.

Relevant normalized G-address instruction excerpts (branch targets below are
also G coordinates; raw Capstone run used ELF virtual addresses):

```text
86cd5e mov r0, sl             ; sl = explicit CardInfo from ACTOR_INFO+3c
86cd60 bl 87b364              ; CSRCardInfo.GetMaxRank
86cd64 mov r1, r0
86cd66 mov r0, r4             ; new card
86cd68 movs r2, #0
86cd6a bl 869c70              ; CSRCard.SetRank(rank, 0)

87b368 ldrd r2, r1, [r0, #0xa0] ; stat vector begin/end
87b36c cmp r2, r1
87b370 ldrne r0, [r1, #-0x8]    ; last stat raw pointer
87b374 cmpne r0, #0
87b378 movs r4, #0               ; empty/null result
87b394 ldr r4, [r0]             ; returned last stat rank

869c7a ldr r0, [r0, #0x24]
869c7c str r2, [r4, #0x28]
869c7e cmp r0, r1
869c8a str r1, [r4, #0x24]       ; new card rank when changed
```

The temporary shared-owner increments/releases surrounding these instructions
remain intact. These are observations, not instructions to invoke setters.

## Consequence for the original E6 encounter

Original CB0602's Bibi `CB0602_040_1` has **combat thumb rank4 but STAT rank5**.
On this fixed-data construction path the new card's effective rank becomes5,
matching the sole parsed STAT. The ordinary CSRCardInfo.GetStat G87acc8 scans
for exact rank/awakening; it must not be applied to the thumb4 as evidence of a
missing rank4 stat row. Karl's STAT and thumb are both4, so this selector leaves
Karl at4. CB0602's four M024 rows are STAT4/thumb4 as well.

This closes a concrete construction ambiguity and explains why original Bibi's
fifth skill selection `[1,1,1,1,1]` is not disproven merely by the rank4 thumb.
Actual fifth-skill enable/application still requires the native skill-list
consumer; do not claim that every listed effect fired in a lost battle.
Preserve original Bibi STAT5, thumb4 and Karl's duplicate rows unchanged.

This evidence does **not** establish that CB0602 losses arose from a stat bug,
or that a rank change on the server would improve the game. It instead removes
one guessed repair from consideration. Live scalar attribution remains missing.

## Next root-owned evidence targets

1. Completed: root exported G86cc60, G87b364 and G869818 with relocated Ghidra;
   independent review found agreement with the original-ELF register evidence.
   Retain both for any SRET decompile ambiguity. Fresh disassembly covered G86cc60..86cf68,
   G869818..869bb8, G87b364..87b3ec and G869c70..869d24 through PT_LOAD mapping.
2. Follow fixed card arithmetic into Analyzer.CalcDmg G86dbe0 and
   CSRCard.GetDmg G86a278, retaining actual Card.GetStat selection and native
   rank factor. `fixed-actor-skill-scalar-contract.md` already closes the
   `8+2*rank` construction factor and integer-defense-quotient boundary; do not
   replace that with `wireATK * skillCoefficient`.
   Earlier scalar/mechanics prose calls G86a278 CalcDmg; native-evidence.tsv
   identifies its exported symbol as CSRCard.GetDmg. The address is the same.
3. If root chooses a paused, bounded runtime corroboration, its existing typed
   actor/state ownership path can sample Karl serial5/camp0 and Bibi
   serial10/camp1 default+14 rank, +38 attack, +40 defense and the corresponding
   buff multipliers. These are direct combat scalars, not another visual card
   stat hunt. Do not start a battle merely for this read unless prompt fighting
   and safe pause are already managed. No getters, writes or memory gate clears.
4. Only a typed active effect/source/target sample plus isolated application
   evidence could attribute the observed damage/heal limits. Existing Karl
   activation, Tyltyl heal361 and prompt-fight losses prove participation, not
   which original passive/DOT/regen paths caused defeat.

## Evidence and limits

Existing sources: episode06-stat-duplicate-contract.md; episode06-entry-materials.md;
ghidra-e06-stat-index.txt / unique-insert.txt; ghidra-episode-combat-actors.txt
and keys; ghidra-episode-first-combat.txt; ghidra-episode-decomp-02.txt;
ghidra-skill-construction-registration.txt; ghidra-card-stat-level-detail.txt;
ghidra-fixed-actor-rank-selection.txt (root-exported, independently reviewed);
ghidra-stat-parser-first-insn.txt / keys; fixed-actor-skill-scalar-contract.md;
episode06-support-skill-application.md. Symbol identities were cross-checked in
native-evidence.tsv. Original bytes read from
`analysis/extracted/lib/armeabi-v7a/libnative_core.so` with Python struct ELF32
program headers and installed Capstone Thumb; G=ELF+0x10000.

No source corpus, current private profile, save or runtime state was modified.
The Bibi rank selector is source-level evidence; no fresh live E6 observation
was performed by this audit.
