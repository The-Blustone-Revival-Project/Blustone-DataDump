# Bounded visual battle skill-plan validation

Reviewed `tools/attack-battle-visual.ps1` with the scalar coordinate guard.
No controller, ADB, game input or live state inspection was run in this review.

The validation test executes the actual source prefix ending immediately
before `New-Item -ItemType Directory -Path $visualDir`, with a sentinel throw
at that boundary. The only substitution supplies the normal tools directory
for `$PSScriptRoot`, which is otherwise empty for an isolated ScriptBlock.
Test plan files are local review fixtures; none is a gameplay/evidence directory.
The controller runtime is absent from the executed prefix.

Historical initial validation: ten invalid cases all reject before the boundary, and none creates its requested
evidence directory: five attempts; duplicate milestones; spacing of three
ordinary bursts; fractional milestone; milestone0; milestone equal to MaxBursts;
non-whitelisted point; array, string and object coordinates. Array coordinates
previously passed PowerShell's collection equality; the new scalar integer check
rejects them before the coordinate whitelist. Integer front `(300,535)` and
moving-front `(450,535)`, plus rear support `(345,1385)`, are the whitelisted
caller-reviewed points. The moving-front point follows actual CB0602 retry004
frames019/033/041; it does not establish which icon is present on another frame.
After this addition, all ten invalid prefix cases still reject without creating
their requested evidence directories or entering the runtime.

Current code-review invariants: at most four opt-in attempts; unique integer milestones
from0 inclusive to MaxBursts exclusive, separated by at least four ordinary bursts;
milestones sorted before use. Every attempt occurs only after foreground/PID
inspection, a new captured frame and the existing passing HUD/all-enemy-X gate.
The single normal tap is logged as an attempt with native acceptance unproved.
It increments the attempt index then continues the loop, so no ordinary burst
occurs on that same frame. Further inputs require another fresh frame. Rejected
HUD/cut-in/result frames stay on the no-input waiting/stopping path.

This is normal button input, not a native-state bypass or an eligibility
classifier. The client still enforces enabled state, opacity-byte255, Rage cost,
cooldowns, roles and targets. A moved/absent/dim icon can reject or miss; neither
touch acceptance nor a scheduled milestone proves activation, healing, damage
or a Rage debit. See `episode06-front-skill-pixel-limits.md` for actual front and
rear geometry and the limits of white-pixel inference. Live attempt behavior
and outcomes require root's separate captured/runtime evidence.

## Current derived right-rear point and milestone0 validation

The historical milestone0 rejection above is superseded. Root now permits one
scheduled attempt at after_bursts0 on the first fresh passing HUD, before an
ordinary burst. In addition to the earlier exact front/support points, scalar
integer right-rear coordinates x800..1050/y1200..1550 inclusive are accepted.
This bounded region excludes the central door but is not an icon detector or
eligibility assertion. Caller must review the derived point and encounter.

The latest isolated actual-prefix checks reject14 invalid cases before directory
creation: milestone-1; milestoneMaxBursts; x799/x1051; y1199/y1551; array/string/
object coordinates; duplicate milestones; spacing3; fractional milestone;
five attempts; and central-door point550,1415. Milestone0 at937,1355 and the
inclusive right-rear corners800,1200 /1050,1550 pass validation to the sentinel
immediately before New-Item. Neither valid-prefix case enters runtime. All16
cases create no requested evidence directory and make no ADB/controller call.

Root's paused Karl diagnostic supplies a native cached rectangle centered near
564.965,816.457 and an independently observed renderer/layout mapping; these
motivate the caller-derived937,1355 candidate. The prefix test does not prove
that point hits a live icon, that ancestors remain unchanged after resume, or
that the native listener admits a skill. No allocation-class/full-admission
claim follows from accepting the coordinate region.

## Native retry005: attempts validated, activation unproved

Root's terminal controller run `episode06-cb0602-005` delivered33 ordinary bursts,
captured50 frames and logged four single attempts at016/023/032/040. Review of
the retained before/after screenshots supplies no verified player skill debit,
heal or player cut-in. All four remain attempts only.

At016 the rear support heart bubble has moved to approximately `(350,1475)`;
the scheduled `(345,1385)` point is above that actual bubble. Rage displays5 in
both016 and017. Nene's low-HP front disappears and Tyltyl becomes front in017;
this change of actor is not a heal. Earlier frame014's rear geometry was a
sample, not a universal fixed position.

At023 the front Tyltyl heart bubble centers near `(460,520)`, and the attempt
uses `(450,535)`. Rage remains8 in024 while Tyltyl disappears and Lantern takes
the front. No cost4 debit or heal is verified. Native role/opacity/target
rejection cannot be distinguished from a missed/timed-out icon by these frames.
At032 Captain's sword bubble is near `(295,520)`, so `(450,535)` misses the
captured icon;032/033 both display Rage8. At040 Karl's sword bubble is near
`(460,520)`, but040/041 both display Rage10, without a verified cost3 debit or
player skill cut-in. Ordinary enemy HP damage alone is not skill proof.

Reviewed035 active combat,036 Bibi cut-in,037 resumed combat,043 damaged Karl,
044 no visible friendly front, and049/050 loss-choice menu. The stored HUD gate
rejects036 and044..050; no false-positive cut-in/menu gate was found in these
samples. The Bibi cut-in is an enemy skill and must not be attributed to the
planned player attempts. Controller logs have no same-frame ordinary taps
artifact for the four skill-attempt frames. This evidence validates separation
of inputs, not native skill acceptance or a battle win.

## Derived Karl point: native visual skill evidence and new gate failure

Read `skill-ancestry-001/ancestry.stdout.txt` and resume001..004 plus guard/input
artifacts. The paused snapshot's bounded ancestor walk reaches a root for all
five icons, contains the corresponding owned actor and repeats parent weak
pairs/vptrs/control counts/flags after traversal. Depths7/10 and observed masks
0 are diagnostic evidence of these sampled chains. Exact unadjusted base-method
consumer guards support the flags reads; concrete ancestor allocations and
full input eligibility remain unproved, as the output explicitly states.

The normal derived937,1355 attempt occurs at after_bursts0 on fresh resume001.
001 shows rear Karl1150, front Nene664, first M024 HP1120 and displayed Rage3.
002 shows the diagonal player skill-view transition with Karl absent from the
rear. In003 Karl is front with HP1014, Nene is rear with HP617, the first enemy
portrait has a defeat X, Rage displays2, and AttackSpeed plus InvincibleDisabled
10sec indicators render. 004 continues Karl combat against the next M024.
Together these support native Karl skill activation and automatic exchange;
they do not measure the exact float Rage debit or isolate skill-only HP damage
from ordinary attacks, simultaneous enemy hits, kill recharge or regeneration.
This is stronger evidence than accepted touch injection. The later native loss
at036 is separate; activation did not complete or win CB0602.

**New false-positive gate:** resume002 is visibly a player skill transition,
but its retained guard says battle_hud=true with cyan3163 pixels and zero warm
pixels in both front badge boxes. A `002.taps.txt` artifact exists. The broad cyan
branch therefore admits this partially exposed HUD during a diagonal player
cut-in; existing negative tests for full-screen enemy cut-ins do not cover it.
Do not extend the earlier no-input-on-cut-ins claim to this frame. Root must
add this actual negative and calibrate a cut-in rejection before relying on
the gate for another skill sequence. This review changes only this report,
not the classifier/controller or live state.

### Captured diagonal cut-in regression fixed

The classifier now rejects the actual resume002 overlay using a coherent lower-
left diagonal black panel edge and bright inner face, sampled across both the
battle and airship regions. At least30 in-bounds samples,28 dark edge samples
(max channel<=35), and15 bright inner samples (minimum channel>=140) are required
along the bounded slope/intercept search. It keeps the existing timer, low-HP
red stripe, cyan/warm attribute and all-enemy-X controls; cyan was not removed
or globally tightened. Diagnostic `diagonal_skill_overlay` records the match.
The reason remains hud_not_confirmed so root's bounded no-input observation
path can handle the transition.

New captured regression asserts002 still passes the old timer/stripe/cyan
thresholds but now rejects specifically with the overlay signature; ordinary
001 and004 remain accepted. All seven HUD unittest methods pass, including
the retained >=24 annotated frames, low-HP positives, enemy cut-in/menu/loss
negatives and portrait-X controls. Diff checks pass. Historical002.guard.json
and its taps artifact remain unchanged as evidence of the earlier false positive.

This detector is calibrated for the observed lower-left diagonal panel style
and1080x1920 view. Other transition directions, colours or partial overlays
are not universally covered; it does not prove native pause/skill state.
No live inputs/controller changes or replay were performed by this reviewer.

### Actual horizontal speed-line skill-view rejection

`episode06-heal-001/resume/002.png` visibly shows a dark horizontal blue/yellow
speed-line skill view around Bibi, with timer and enemy HP still exposed.
Its historical guard accepted cyan561/timer1544/red2538 and a taps artifact
exists, so the diagonal-panel fix alone did not cover this second actual style.
No nearest-asset identity inference was used to label the captured appearance.

The classifier now also samples upper-battle y300..650 and requires at least
70% dark backdrop together with three long cyan streak rows spanning at least
80px vertically. Cyan hits must have dark neighbours12px above/below, so broad
ordinary cyan snow scenery does not satisfy the streak shape. Observed002 has
dark ratio0.831 and qualifying rows412/416/564/616; normal001/003/004 have near-
zero dark ratio and no such rows. Retained dark arena positives (~0.56/0.58)
have no qualifying streak rows and remain accepted. This style is reported by
`speed_line_skill_overlay`, leaving the reason hud_not_confirmed for bounded
no-input observation. Existing cyan/low-HP/timer/warm/X tests remain unchanged.

All eight HUD test methods pass, including this actual002 negative, normal
001/003/004 positives, the previous diagonal002 negative and all prior captured
regressions. Diff checks pass. Historical guard/taps artifacts are retained.
This is calibrated recognition of the observed speed-line view, not universal
skill/pause detection; other shapes and colours require separate evidence.
Only guard implementation, tests and this report changed; no ADB or runtime.

### Right-side diagonal panel captured and rejected

The subsequent actual `episode06-heal-002/finish/002.png` shows an enemy skill
portrait panel entering from the lower right, with its black edge descending
leftward as y increases. The historical guard accepted its still-exposed
timer1352/red592/cyan1372 and root reports an ordinary taps artifact. This
opposite direction was outside the first diagonal calibration.

The same bounded long-edge detector now checks both orientations. Right-side
panels reflect the tested edge horizontally and sample the bright inside at
x+25, while left panels keep x-25. Thresholds remain unchanged; the actual
right panel has a matching candidate with29 dark samples and19 bright inside
samples. `diagonal_skill_overlay_side` reports the recognized direction without
claiming native skill identity. The new captured negative rejects002, preceding
ordinary finish001 remains accepted, and all earlier regressions still pass.

All nine HUD test methods and diff checks pass. Original guard/taps artifacts
remain historical evidence. Both captured diagonal directions and the captured
speed-line style are covered; other angles, crops, colours or transitions are
not universally proved safe. No ADB, live input or controller change by reviewer.

## Derived left-rear point: current prefix boundary checks

Root expanded caller-provided coordinates to bounded left-rear x250..390 and
y1300..1550 inclusive, retaining the earlier front/right-rear regions, scalar
integer validation, milestone0..MaxBursts-exclusive, four-attempt limit and
four-ordinary-burst spacing. The central door550,1415 remains outside accepted
regions. A valid region still does not detect an icon or establish admission.

The actual source prefix was isolated again at the pre-New-Item sentinel.
Derived center346,1437 at milestone0 and inclusive corners250,1300 /390,1550
pass to that sentinel. Fifteen invalid cases reject first: x249/x391,
y1299/y1551, array/string/object coordinates, fractional/string milestones,
negative milestone, milestoneMaxBursts, duplicate, spacing3, five attempts and
the central-door point. All17 cases create no requested evidence directory and
execute no ADB/controller body. These checks do not run or change gameplay.

Root's separate paused support snapshot motivates the center: native Tyltyl
rectangle140.7135,800.7485..276.7135,930.7485, actual SP4.4809 and sampled
stun0. Those facts establish that pause sample, not the moment of the later
press. The prefix validation does not claim a heal, a native cost debit,
unstunned state at press time or a battle outcome. No source/controller/guard
edits were made in this review; only this report was updated.

### Actual support heal and partial speed-line wipe coverage

The derived346,1437 support attempt in `support-stun-001/heal-resume` has
stronger native visual evidence than prior misses. Frame001 displays Rage4;
002 contains a mixed Tyltyl diagonal panel and full speed-line enemy skill view;
003 renders a green361 healing number, CriticalChance indicator and Rage0.
The combination supports native support skill acceptance/healing. It does not
isolate the exact float cost debit or net HP gain amid simultaneous bleeding/
enemy damage. Root's sampled stun0 before the press remains a pause-time fact.

002 was correctly rejected without input, but003 retains a visible left-side
speed-line transition and its historical guard accepted it; a `003.taps.txt`
artifact exists. Therefore not all cut-in input was avoided. The previous
whole-scene dark threshold missed this partially completed wipe:003 has dark
ratio0.400 overall but0.787 in its left half, with long streak rows356/376/380/
556. These are directly inspected captured pixels, not guessed resource IDs.

The speed-line detector now applies the same dark-backdrop, long-cyan-streak
and vertical-spread requirements independently to whole/left/right upper scene
regions, calculated in one pixel pass. Diagnostic speed_line_overlay_regions
reports which regions match. Captured003 rejects specifically through left,
not whole;002 also stays rejected, and ordinary001/004 remain accepted. All ten
HUD test methods pass, including all prior annotated samples and previous
diagonal/full-speed-line negatives. Diff checks pass. Historical guards/input
artifacts remain unchanged.

This expands finite pixel coverage to the captured half-wipe style. Narrower
partial strips, other screen layouts/colours, or unobserved transition shapes
still lack proof. No universal pause/skill predicate or cut-in avoidance claim
is made. Reviewer changed only guard implementation, tests and this report,
with no ADB, controller input or runtime action.

### Normal-row green stripe proposal rejected by actual positives

The new actual `support-stun-001/finish/003.png` contains a short lower-left
skill-panel transition and floating front HP307 near y620, while normal-row
enemy HP stays exposed. The existing pixel gate accepted it and an ordinary
input artifact remains historical evidence. The current long-edge and speed-
line calibrations therefore still have this captured gap.

A proposed positive green front-health stripe at x100..580/y1020..1050 with
minimum one pixel was evaluated offline and not implemented. A permissive
antialiased-green test (G65..240, R<=185, B<=170, G-R>=15, G-B>=20) rejects
finish003, but also finds zero on actual near2HP heal-resume004 and retained
CB0502/016 (Nene death while Karl remains alive). Ordinary finish001/004 have
1524/2863 qualifying pixels and older28HP E04 positive has48. Even the much
looser G>R and G>B test finds zero on the near2HP frame; it produces66 ambient
pixels on the unwanted finish003. Lowering the numeric count cannot restore
the near2HP positive while rejecting that transition.

Native green fill can vanish below pixel width, and the ordinary death/exchange
path can temporarily omit a front stripe. A required visible-green stripe would
regress the retained gameplay contract and risk stopping attacks at precisely
these states. Per root's edit boundary, no guard/test changes were made for
this proposal; only this documented rejection and remaining gap were added.
The existing test suite's earlier passes do not prove the new finish003 safe.
