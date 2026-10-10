# Fishing hook touch cadence and tutorial thresholds

2026-10-07. Original ELF, public FISHING_SETTINGS.json and parent completed
ghidra-fishing-hook-input.txt plus retained tutorial-hook decomp. No device,
Ghidra, source/state changes, tuning, cast/catch/end or outcome assignment.

## Actual touch handler and cooldown

OnButtonClick **Gd043d4** and its thunkd043d6 are BXLR; they do not update the
gauge. Actual **OnProcessCursorPress Gd04490** requires nonzero press flag,
mode atpopup+65c>=0 and FLOATcooldown+78c<=0. Rejected inputs forward to
FramedScene. Accepted input sets+78c from **COMMON_INFO+0** (d04502/d0450c).
UpdateMode subtracts elapsed frame delta from+78c and clamps belowzero;
presses during that cooldown do not increment the gauge. Original common1
touch_delay is **"0.1"** in FISHING_SETTINGS.json. This supports100ms cooldown
in the game's elapsed-time coordinate, not a guaranteed acceptance rate for
Android events or host burst scheduling. No hold-duration condition was found
in the accepting gate; release events take the non-increment forwarding path.

Accepted inputs call **UpdatePercentd043d8 atd048f6**, then TouchDirTime and
animation/effect logic. Visual touch sparks do not quantify every gauge update
or prove threshold completion.

## Increment and original tutorial constants

UpdatePercent's mode1 path adds **popup+6ac** to current value+658. In other
inspected modes, direction/HOOK2 or3 chooses same/not-same ratio and uses
the FLOAT at **popup+6a8+mode*4**. Original common1 ratios are0.6 and1.2.
These are direction-sensitive native mechanics, not a generic tap-anywhere
fixed increment. No screen coordinate choice is prescribed by this report.

Original **TutorialMFishingHook.OnInit Gef20a0** overrides base hook settings:

- DAT **ef2350**, bytes decoded as float32 pair **(0,0)**, copied to
  popup+6a0/+6a4: both initial mode decay values arezero.
- DAT **ef2358**, float32 pair **(2,0)**, copied to+6a8/+6ac:
  initial direction-mode basis2 and initial mode1 direct increment0.
- popup+658 initial30 (0x41f00000); initial mode becomes-5.

These are original client constants, not proposed server balance. They also
prevent explaining a tutorial low gauge solely from ordinary-frame decay:
the INITIAL tutorial decay iszero. Later guide/controller callbacks may change
mode/settings; their live phase must be established before extending this
statement. Base UpdateMode ordinary modes0/1 add their respective decay value
once per update; that addition itself is not multiplied by frame delta.

## Completion and guide handoff

Base UpdateMode reads the visible progress bar's CurrentPercent. Its active
mode branch compares **100.0** (original literal Gd03e10): >=100 selects
ChangeMode(-3), <=0 selects ChangeMode(-2). These are controller transitions,
not proof of an HTTP End or server reward.

Tutorial OnRefresh **Gef24ec** has an additional exact phase boundary:
mode0 and byte+7c8==0, GetPercent>=**70.0** (DATef2bfc) invokes the controller
stored at **+7f8**, virtual+18. When byte+7c8==1 and GetPercent>=**100.0**
(DATef2c00), it selects ChangeMode(-3); otherwise delegates base OnRefresh.
Successful EndWithSell remains a later transition and parser contract.

The native100ms accepting gate means a12-event50ms burst cannot be counted as
12 successful increments. But neither an exact accepted-touch count nor a
minimum wall-clock win duration follows without current mode/direction/guide
phase and input-event observations. Four separated bursts are insufficient
evidence of an original tuning defect. Next narrow parent targets, if needed:
the tutorial +7f8 callback writer in OnInit, phase callbacks in OnRefresh and
ChangeModed02bb0; no repeated ineffective action or tuning override is proposed.

## OnInit callback identity and phase writers recovered

Original literal pairs resolve primary function-object vtables, all with
offset-to-top0 and RTTI explicitly naming TutorialMFishingHook.OnInit:

- ef2374+ef213e → ELFVT2177d60/vptr2177d68, $_0 invoke **Gef2c64**.
- ef2378+ef217c → VT2177da0/vptr2177da8, $_1 invoke **Gef2ddc**.
- ef237c+ef21a8 → VT2177e20/vptr2177e28, $_2 invoke **Gef30d8**.
- ef2380+ef21d4 → VT2177e60/vptr2177e68, $_3 invoke **Gef325a**.
- ef2384+ef21fc → VT2177ea0/vptr2177ea8, $_4 touch-signature invoke
  **Gef32d6**. Invoke is VT+20, containing the odd ELF Thumb address.

The initial parent ghidra-fishing-hook-guide-callbacks.txt decoded the first4
as bad ARM instructions/software interrupts and truncated flow. Parent then
replaced it with proven-Thumb decomp, which corroborates the assignments below.
The initial invalid output is not used as evidence; exact original Thumb
independently established the function identities and stores.

$_0 captures scene+4, sets **+7c9=1** at ef2cfa, sets decay6a0/6a4 to
**-0.050000000745** (bitsbd4ccccd, STRDef2d06), and calls ChangeMode(-1)
at ef2d0c. Thus initial zero-decay assumptions stop at this phase writer.

$_1 changes mode to1 atef2df8; zeroes664/668; writes66c=1.0;
stores halfword1 at7c8 (7c8=1 and7c9=0), zeroes decay6a0/6a4. It schedules
a nested callback after1.0 via OnceImpl ef2e36: LDR ef2e22/ADD ef2e28 resolves
VT **ELF2177dd8**, RTTI OnInit$_1 nested lambda, invoke **Gef2eec**.
That nested callback constructs tutorial comments and SetNextEvent; its complete
guide text/next-event binding is the next exact decompile dependency.

$_2 captures scene+4 and uses base scene+668: sets7c9=1, sets
**inc at6ac=-5.0** (bitsc0a00000, STR ef3178), both decay values=-.05
(ef3182), **668=1.5 and66c=.5** (STRDef318a). Mode1 accepted touches therefore
reduce gauge5 in this phase; more tapping is not inherently progress.

$_3 writes both decays=-.05 at ef3264/68 and7c9=1 at ef326e.
$_4 only forwards input to base OnProcessCursorPress when7c9 is nonzero
(ef32de..ef32f8), explaining tutorial-overlay interception without a native
input-mask patch. Captured scene ownership/lifetime is not independently
validated here; these identities are decompile targets, not live reader guards.

The existing UpdateMode mode1 duration668 counts down then changes to mode0.
Consequently current mode/visible instruction matters: mode0 uses positive
direction increments while mode1 can penalize presses. The exact original
comment sequence should guide the native interaction. This report does not
infer live mode from sparks/low gauge, reset counters, retune constants or
recommend another undifferentiated burst. Correct Thumb decompile targets are
**ef2c64,ef2ddc,ef30d8,ef325a,ef32d6**, plus nested **ef2eec**.

At the70 handoff, $_1 sets mode1 with duration668=0, disables tutorial input
7c9=0, and schedules the nested comment callback after1second. UpdateMode's
automatic return to mode0 only decrements a strictly positive668 duration;
therefore this handoff waits for the guide event, not more rapid touches.
After $_2's guide dismissal, positive668=1.5 enables the normal time-driven
return from mode1 to mode0. Pressing during that mode1 demonstration reduces
the gauge5 each accepted touch. Waiting for the mode0/direction phase is the
mechanically supported action; current screenshot69 alone does not prove live
mode. Exact comment wording and nested SetNextEvent ownership remain pending
the ef2eec dump. No ignored instruction or completed phase is assumed.
