# Recover actor-bound skill targeting before more coordinate attempts

Read-only exports and existing native/source reports; no Ghidra, ADB, runtime
or native calls/writes. All addresses below are Ghidra addresses (already
include image bias0x10000). Resolve actual Thumb call targets/virtual slots
from instructions before assuming a getter's return layout.

## First focused dump: actual icon hit rectangle and opacity

Start with `CSRGameUIIconSkill::OnProcessCursorPress` Ga3c178..a3c1d0. Existing
`active-skill-gesture-rage.md` proves press=true, enabled byte icon+6c, drawable
pointer icon+60, hit intersection and opacity-derived byte delivered through
event icon+44. At Ga3c18c..19e recover the exact bound getter/intersection call
and its return representation, not just a guessed rectangle field. At Ga3c1a4
recover the actual opacity getter and scaled-byte conversion. The symbol
`CMUpdatable::GetOpacityf` G78a372 is a relevant candidate, not yet established
as that call's exact target by this review. Dump only those actual callees.

Dump `CSRGameUIIconSkill::OnAttach` Ga3c1d0 and `OnDetach` Ga3c2ac to establish
what object icon+60 points at and how its lifetime/parent is retained. The
constructor Ga3b3c8, IsVisible Ga3b9b0, SetVisible Ga3b9b8 and SetAlpha Ga3bc00
are small cross-checks for enabled/visible/opacity state. Do not interpret the
bubble background's semi-transparency as the native opacity byte.

If the hit bound is cached world-space data, recover its finite fields and
dirty/validity flags and read that exact cache rather than executing a native
getter. If it is computed, root should follow the exact coordinate-space
callee first. Exported narrow candidates: CMUpdatable::GetArea G78aa5c,
CMDrawable::InvalidateBoundBox G70b0e0, CMUpdatable::CalcTransfWorld44 G78a6d0,
CalcAdditionalTrans G78a8ba, CMTestIntersection G78c9b4. These are investigation
targets, not already proved field layouts. Do not confuse actor body's
GetBound G99b322 or GetFrontBound G986638 with the icon hit rectangle.

## Second dump: associate the moving drawable with the exact actor

`CSRGameActor::SetInpuable` G985f8c is the ownership bridge: it finds/creates
the icon component and binds icon event+44 through thunk G98dcce to actor
event+8c4. The actor input/UI binding at+a6c is nonzero when IsInputable says
true, but its pointer must not be cast straight to CSRGameUIIconSkill without
recovering the stored type and ownership from this setter. Inspect the exact
shared/weak pair and any component host/parent offset adjustments.

Existing `ghidra-episode-front-actor-null-body.txt` proves MakeFrontActor
G9ddc3c obtains the UI skill-point through game UI+20c virtual+6c, calls
SetInpuable, and registers the actor event listener. Dump G985f8c plus the
listener closure G9f7604 for actor/role/target eligibility; G97d1f8 OnRefresh
and its small range G97d6c4..97d7ce explain skill icon positioning/visibility,
Rage affordability and role-dependent alpha128. Follow the exact position
setter/animation attachment from these bodies; do not fit a static screen box.

Read-only target snapshot must retain exact current scene/combat, bounded
actor serial/camp/ref identity, proven icon-component owner, drawable owner,
enabled/visible state, actual opacity byte, and valid finite hit rectangle.
Repeated owner/field checks prevent mixing two actor/icon registrations.
Native role getter G99aee8 and IsSkillEnabled G97ecba supply narrow fields;
SetSkillEnable G98669e's callers locate the source of disabled skills. No
heap scan, guessed type cast or writing an enable byte is justified.

## Third dump only if coordinate spaces remain unresolved

GameBase::OnProcessPress G9db1bc forwards root UI before ordinary attack
gates; UI component event processing is not identical to a raw screen pixel.
Trace CMUpdatable::ProcessCursorPress G787004 and CMScene::ProcessCursorPress
G754e94 for parent transform/hit-coordinate semantics, then the renderer
conversion pair `CRMRenderer4::GetLogicalPos` G10e0528 / `GetPhysicalPos`
G10e05cc. Exported CMScreenCoordUtil::GetCoordPos G758480 and `_RMGetLocalPos`
G110357c are secondary candidates if that exact path calls them. Recover
viewport/scale/origin and matrix order before converting an icon rectangle
to the1080x1920 capture. Reading CMUpdatable::GetPos G6d8170 alone is insufficient
because parent transform and actor animation move the icon.

## Fixed Karl is not proved ineligible merely because the thumb says level1

Original CB0602 uses fixed ally `CB0601_012_1`, thumb level1/rank4, skill
selection `[1,1,0,1,0]`; CB0601 uses the same identity with level10. The first
duplicate STAT row143 selected by native unique indexing has role1, active
skill type1/target_rank1/cost3/cooldown5000 and the original -2000 effect.
The thumb level is distinct from rank and the explicit skill selection; there
is no recovered rule here that level1 disables skill1. The selected row and
original source are retained; do not raise Karl's level or rewrite its skills.

Visible sword/cost3 in CB0602 retry005/frame040 corroborates an icon, but
Rage10 remains10 after the planned tap; it does not establish active eligibility
or success. Next exact fixed-actor path: hunter MakeBackEndActor G9ac2ac,
CSRMEpisode::ParseActor Gb1bd5c and the caller consuming COMBAT thumb/skill
array. Recover the rank/skill-selection arguments and SetSkillEnable G98669e
callers, then compare the guarded actual actor enabled byte+a7d, role,
selected skill1 and cooldown. Existing first-row proof is
`episode06-stat-duplicate-contract.md`; exact descriptors/rows are in
`episode06-entry-materials.md`. Native disabled flag, role state, target
intersection, cooldown or wrong touch coordinates remain alternatives.

Retry005 demonstrated the reason to stop fixed-point trials: rear support
bubble moved vertically to~1475, front icons alternate nearx295/x460, and four
normal attempts proved no debit/heal/player cut-in. Recover the actor-bound
screen rectangle and eligibility facts before the next targeted input.

## New root exports close ownership and cached bounds

Read `ghidra-skill-drawable-targeting.txt`,
`ghidra-skill-coordinate-contract.txt`, `ghidra-skill-bound-episode-gate.txt`
and `ghidra-skill-bound-refresh.txt`. These supersede the candidate getter
uncertainties above; no new runtime observation was performed in this lane.

SetInpuable stores the incoming weak SkillPoint at actor+a74/+a78. A component
lookup/dynamic cast or icon factory supplies the strong CSRGameUIIconSkill pair
at actor+a6c/+a70, followed by SetData(role,attribute,cost) and SetVisible(0).
Thus a6c's exact component type is now established by the producer, while a
future read must still verify the actual primary vptr/control/lifetime. The
constructor loads a view, finds CMDrawable by name and stores its strong pair
at icon+60/+64. These are distinct objects and distinct control pairs.
OnAttach copies that drawable pair and attaches it as a child; OnDetach detaches
its parent. The OnAttach decompiler loses/aliases its this/host parameters, so
its exact native host argument should be checked in Thumb before treating
drawable's parent pair as a proved direct actor owner.

OnPress's exact drawable virtual+90 uses CMDrawable::GetArea G70c810, whose
virtual+94 calls InvalidateBoundBox G70b0e0 before returning drawable+1bc.
CMUpdatable's non-refreshing GetArea G78aa5c returns the same offset but is not
a substitute for that virtual path. The point intersection is G78c90e (the
rectangle/point overload), not earlier candidate G78c9b4 (rectangle/rectangle).
It reads float xmin/ymin/xmax/ymax at drawable+1bc/+1c0/+1c4/+1c8 and compares
against signed integer CRMPoint x/y inclusively. This establishes field order,
not physical screenshot coordinate conversion.

InvalidateBoundBox first calls CalcTransfWorld44. Drawable byte+60 mask0x08
selects bound recomputation, using local size+78/+7c, anchor+7fc/+800, cached
world matrix+118 and cumulative scale+8c/+90. It writes the four hit fields and
invokes virtual+68 with8 to clear that dirty state. World transform byte+60
mask0x02 triggers inheritance recomputation through parent weak pair+54/+58;
the parent world matrix becomes inherited+158, and local+ d8 is multiplied
into result+118. The exact local-matrix dirty mask remains to be recovered
from CalcTransfLocal44 G787b28. A finite rectangle alone is insufficient:
read-only sampling must reject dirty/inconsistent caches or report unresolved
conversion, rather than call a getter that writes transforms/bounds.

Actual GetOpacityf G78a372 returns drawable floats b8*bc*b4. When drawable
byte+60 mask0x80 is dirty, it locks the parent weak pair+54/+58, recursively
obtains parent opacity (default1 when absent), stores b8 and clears mask0x80.
The current source therefore distinguishes cached inherited opacity b8 from
the two additional local factors bc and b4. Read all three finite factors and
dirty/lifetime state; do not label one factor as effective alpha or invoke this
lazy-writing getter. OnPress multiplies the effective product by its native
scale literal and converts to the event byte; the literal/rounding should be
verified from the retained instructions before reproducing exact byte255.
IsVisible/SetVisible close icon+6c as visibility/enabled state, and
IsSkillEnabled/SetSkillEnable close actor+a7d as the separate skill-enabled byte.

Remaining next actions are now narrow: recover CalcTransfLocal44's dirty mask,
exact component/drawable parent-host association in OnAttach, native opacity
scale literal/conversion, and physical-to-logical cursor conversion along the
actual UI dispatch path. Avoid a broad UI scan or another fixed-point trial.
The renderer GetLogicalPos/GetPhysicalPos pair remains a coordinate candidate
until root proves it is used by this cursor path. Root separately owns Episode
season entry CalsState/TableClick recovery; that entry gate does not establish
in-battle skill eligibility or authorize changing Karl's original descriptor.
