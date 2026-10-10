# M022 native battle material: complete original dependency chains

Scoped read-only diagnosis after root observed M022 thumbnails but an invisible
body in Story04 combat. Original final-client M008.jet only; no adb, Ghidra,
server/client/state changes, aliases, art generation or original writes.

**Every declared M022 AT→S2→I2 dependency is present in the same original
M008.jet.** The missing-body symptom is not explained by an absent additional
package in these chains. This is an offline material result; runtime resource
registration and the actual animation selected remain unverified here.

Source:
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/M008.jet`,
223669 bytes, SHA256
`04b37480c31248de3a2a23f09901961923441a9ba7524abae037a0eb805074f5`.
The134-record outer-header walk closes exactly. IDs decode with the recovered
base38 alphabet. All selected compressed bodies inflate successfully.

## Exact animation graph

AT payloads begin AT; frame count is uint32 at43, frames are14-byte entries
beginning47, each with a uint64 resource ID followed by float duration and
two bytes. These offsets reproduce every original selected frame without
name guessing. All referenced IDs match actual S2 outer-record IDs.

```text
M022_R1 / M022_R2 / M022_S:
  R01,R02,R01,R03,R04,R03,R04                 (7 frames)
M022_H1: H01,H02,H03,H04,H05                 (5 frames)
M022_H2: H06,H07,H08,H09,H10                 (5 frames)
M022_H3: H11,H12,H13,H14,H15                 (5 frames)
M022_DIE: H10                               (1 frame)
M022_AS1 / M022_AS2 / M022_AS3: M022_SHA     (1 frame each)
M022_SHADOW: M022_SHA                       (1 frame)
M022_TH: M022_THN                           (1 frame)
```

R01 etc. above are the full M022_R01-prefixed identities. Ordinary running,
standing, hit/attack and death chains contain body images. AS1..3 contain
only the shadow sprite. **That is original shipped content**, also true of
M023_AS1..3 and M024_AS1..3 in this package; it is not a missing-frame defect
to repair by aliasing AS to a body. Whether AS means an auxiliary shadow
layer is not independently recovered here.

## Sprite image closure and nonempty pixels

Each of21 selected S2 bodies has one image reference, uint64 at46. Every ID
resolves to a local I2 outer record in M008. Existing
`tools/jet-viewer/jet_decoder.py:decode_i2_texture` decodes every referenced
image successfully; in-memory alpha checks show nonempty pixels. No image
files were generated or original material modified.

```text
sprite family    image ID hex    image header   decoded dimensions
R01             7069cfc2        0              146×114
R02             fc3f33b4        6726           149×104
R03             edc3f35b        13013          153×120
R04             cc5b8333        19355          147×123
H01,H02         bdfd0d66        26091          159×104
H03,H04,H05     5fbe7dce        32204          141×107
H06,H07         231016d6        38686          144×164
H08,H09,H10     b60e5ee6        46972          139×160
H11,H12         b7f7b8e2        53983          123×112
H13,H14,H15     55803ed5        60922          121×105
SHA             f93af6a1        196991         157×31
THN             aeeca073        199218         90×94
```

Example R01's alpha bounding box is(0,0,146,111), THN's(0,0,90,93),
and SHA's(2,1,154,31). The body images are not transparent placeholders.
The ten body images plus shadow and thumbnail are12 unique I2 dependencies.
All IDs are unchanged source IDs, not new filename bindings.

## Native selection remains the unresolved seam

Existing actor/episode decomp text searches found no definitions of the
functions needed to prove the actual requested animation mapping. The symbol
registry supplies exact Ghidra addresses for root's exclusive later analysis:

- CSRGameActor::LoadRes, G00982e28.
- CSRGameActorState::Load, G009b521c.
- CSRGameActorState::CreateAnimData, G009b5430.
- CSRGameActorDraw::LoadActor, G009a00a8.

Do not infer native requested suffixes from the recovered AT names alone.
Thumbnail rendering proves at least the portrait path works; it does not prove
that the body resource IDs were registered, found, attached, or selected by the
current actor renderer. A wrong body prefix/state mapping, missing registration
of selected body IDs, or invisible draw placement remains possible. There is
no evidence here selecting one of those causes.

`server-ts/src/server.ts` folds the explicitly selected M008.jet unchanged into
E_NEW's PKGI1 payload; it does not rewrite named records or their image IDs.
Successful CDN delivery alone therefore cannot establish per-record residency.
No extra original package or invented alias is justified by this closed graph.
The next discriminating native check is the exact M022 body animation ID
requested by LoadRes/CreateAnimData and lookup/attachment result, compared with
this source graph. Root's reported loss and invisible-body screenshots do not
authorize a stat retune, host clear or simulated reward.

## Follow-up: original actor decomp narrows the selection seam

Root generated read-only
`analysis/ghidra-episode-m022-actor-materials.txt`; it contains the four
functions listed above. Their call structure establishes the following:

**LoadRes uses two different renderers.** It calls
SRIsSpineSDChar(GetResID()). Return1 creates CMSpineActor and loads the
names supplied by SRGetSpineAtlasName/SRGetSpineSkelName. Other returns create
CMComponentStateMachineImage. The renderer ptr/control are actor+a28/a2c.
Both branches attach their component through the same unresolved FindByPath
string, then populate states. The exact Spine classification for M022 is
not present in these four functions and must not be assumed.

**The M prefix changes preload behavior.** LoadRes explicitly tests the
first character of GetResID against byte0x4d, ASCII M. For M actors it skips
the block adding exchange cooldown, walk, idle, attack1/2/3 and catch
animations. It still adds run twice and hit three times to the primary
renderer, adds the shadow animation to a separate actor+a30 component,
selects the shadow there, then calls RunWithoutState and UpdateStat. These
are the resource-helper calls actually relevant to normal monster body
loading. The decompiler omits some ABI arguments, so repeated calls alone
do not prove both run invocations request an identical suffix.

**CreateAnimData is a state mapping, not a lookup result.** Its switch uses:

```text
state0      SRGetResIdle
state1..3   SRGetResAtk(number1..3)
state4..6   SRGetResHit
state7..8   SRGetResSkilAct
state9      SRGetResCatch
state10     SRGetResDead
state11     SRGetResWalkID
state12     SRGetResRunID
```

It constructs two ANIM_DATA entries per state. State::Load optionally binds
a supplied CMSpineNode and CMSpinePlayer, clears the map at+84, and rebuilds
it from CreateAnimData. That does not establish M022's active renderer or
whether a lookup succeeded. LoadActor's displayed idle resource call is a
separate card-draw path and cannot substitute for live battle LoadRes.

Exact helper definitions still needed to finish the native-to-source mapping:
G010ad34c SRGetResRunID, G010ad3a0 SRGetResIdle, G010ad43c SRGetResAtk,
G010ad528 SRGetResHit, G010b28c0 SRIsSpineSDChar and G010b26f8 its internal
_SRIsSpineSDCharacter. A positive Spine branch would require atlas/skeleton
material distinct from the AT/S2 graph; a negative branch makes run/hit name
resolution and component binding the immediate seam. This report does not
claim either branch for M022 yet. Resolve the helper's PC-relative string
pairs against relocated memory; DAT placeholders in decomp are not evidence
for a guessed resource name or a substitute alias.

## Follow-up: exact helper names match the original body namespace

Root supplied `analysis/ghidra-episode-m022-resource-helpers.txt` and exact
PC-relative resolution in `analysis/ghidra-episode-m022-resource-helper-keys.txt`.
These supersede suffix guessing:

- SRGetResRunID concatenates prefix with **_R1** for zero variant, **_R2**
  for nonzero variant. Literal targets are G01d8cd71/G01d8cd75.
- SRGetResHit concatenates prefix with **_H** plus the decimal unsigned
  number (literal G01d75f65).

With live prefix exactly M022 and hit numbers1..3, those requests are
M022_R1/M022_R2 and M022_H1/M022_H2/M022_H3. All five are declared original
AT records with complete nonempty image chains. Their offline availability
is established; this does not prove the live actor prefix, indices, residency
or successful draw attachment.

SRIsSpineSDChar first queries CRMResMap::IsExistingRes for prefix plus **S**,
with no underscore: **M022S**, not the present AT **M022_S**. If that lookup
does not return1 it calls _SRIsSpineSDCharacter. The internal helper handles
M/C-prefixed strings and checks prefix plus **_a** and **_b**. Original M008
does not declare M022S/M022_a/M022_b. These are distinct namespaces; do not
rename M022_S or fabricate those resources merely to satisfy classification.

Both classifier functions are decompiled with a **void return prototype**
even though LoadRes consumes a result. The internal lookup results are
discarded in that decomp. Consequently this text cannot prove the boolean
classification value or the combination of _a/_b checks. Assembly/ABI or
guarded live result evidence is required before asserting the Spine branch
for M022. No further material research is justified by the current closed
run/hit graph. The remaining check is live GetResID, actual selected renderer
and animation IDs, and their resource registration/attachment outcome.
