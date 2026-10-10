# One ordinary manual-exchange plan: bounded validation review

Reviewed actual `tools/attack-battle-visual.ps1` source. No ADB, actual controller,
gesture, native call, game state or controller edit was performed. Only the
validation prefix before `New-Item -ItemType Directory -Path $visualDir` ran,
with a sentinel throw replacing entry into the runtime. `$PSScriptRoot` was
substituted with its normal tools directory for this isolated ScriptBlock.
Local ignored JSON fixtures are review inputs, not gameplay evidence directories.

Twenty-three cases were checked. Twenty invalid cases reject before the boundary:
empty/two exchange plans; array/string/object/fractional fields; milestones-1
andMaxBursts; each start/end coordinate one unit outside its lower/upper bound;
duration1999/2601; Begin+Resume together; and SkillPlan+ExchangePlan together.
Three valid cases reach only the pre-runtime sentinel: center940,1624→543,1185
with2400ms/after0; inclusive lower bounds850,1550→470,1000/2000ms; inclusive upper
bounds1040,1800→610,1250/2600ms with after19 under MaxBursts20. None of the23
creates its requested evidence directory or calls ADB/controller body.

Source validation requires exactly one exchange row and scalar integers for
after_bursts/start_x/start_y/end_x/end_y/duration_ms. Milestone range is0 inclusive
toMaxBursts exclusive. Capture coordinates are bounded to right-rear body
x850..1040/y1550..1800; drop coordinates are x470..610/y1000..1250; duration is
2000..2600ms. These are caller-reviewed research regions, not dynamically
detected actor/drop rectangles or proof of native admission.

Runtime review confirms ResumeBattle is explicit and mutually exclusive with
BeginBattle; caller must already identify the normal Paused screen. Skill and
exchange plans cannot coexist. Default behavior without ExchangePlan remains
unchanged. After Resume, current PID/foreground and a new captured passing HUD
are required before the single ordinary Android swipe. The attempt counter
increments once, logging acceptance/cleanup unproved, then continues the loop:
no ordinary burst is sent on that same frame. Further input requires a fresh
frame. No native catch, cooldown, actor state, door opening or pointer is forced.

The five-second helper wait accommodates the ordinary2400ms duration plus about
2600ms process/transport overhead; this is a bounded timeout, not a guarantee
the Android command completed. A timeout retains the exact local helper PID,
start time and operation in pending-helper.json and stops issuing new commands.
The already-started gesture can still be running after that observation timeout.
Root must inspect the exact handle before a retry or another controller; do not
kill/restart the app or infer that timeout canceled the contact. Terminal local
exit and a fresh UI/native cleanup observation are distinct requirements.

The caller's paused native actor/body/IN geometry and CanCatch sample motivate
the centers; they can change after resume. A passing pixel HUD after release
does not prove caught198/19c cleared, exchange success, SP preservation or a
drop/return completed. Confirm those through the qualified native/model/UI
evidence in manual-exchange-input-cleanup.md. CANCEL remains Ended in the Java
bridge, so it is not an unconditional native abort. No live manual exchange
success or failure is established by this validation report.

## Live attempt qualification and enemy-only visual gate

Root subsequently reports a successful normal actor exchange, sampled new
front Karl and reserve Nene, but caught198 remained populated after normal
Back. Cleanup reasoning continued while combat was active without prompt
attacks. This was an operational mistake, distinct from the drag acceptance.
The captured ending state does not prove prompt cleanup or that a later Move
alone cleared the catch; a zero caught pair after ending can have other causes.

Inspecting actual `exchange-geometry-001/08b-cleanup-hud.png` corrects the frame
description: Captain is still visible at the front with displayed HP1, while
all rear friendly hunters/bars have disappeared. `09-cleanup-pause.png` shows
enemy Bibi only with HP4000 and no friendly sprite/bar. Despite its filename,
that image has no Paused overlay. Timer/enemy red stripe/background cyan alone
were insufficient positive gameplay guards. Neither filename nor a keyevent
request proves the game paused or catch cleanup succeeded.

The visual classifier now requires visible friendly green health in its front
or airship health regions in addition to prior controls. Rear scanning excludes
the central illuminated exit panel, whose green decoration persists without
hunters. This preserves actual near2HP front-with-live-reserves (front0 pixels,
rear4066), and old CB0502/016's death/exchange frame via rear2956 pixels, while
rejecting actual enemy-only09 with zero friendly bar pixels. All eleven HUD
test methods pass, including all prior ten and the new enemy-only/near2HP
regression. Diff checks pass; historical captures remain unchanged.

Finite coverage limitation: CaptainHP1 in08b has no visible green fill and no
remaining rear bars, so this gate conservatively returns hud_not_confirmed
even though one friendly actor is still alive. That is not a loss claim. Other
subpixel-fill last-hunter states, altered bar geometry or green visual effects
can likewise defeat the pixel inference; complete native liveness/admission
is not proved. Root must preserve prompt battle control and verify paused/
terminal/catch state independently rather than leaving active combat idle
while reasoning about cleanup. Reviewer performed no live inputs or cleanup;
only guard implementation, tests and this report changed.

## Bounded source-normal follow-up movement option

Root added CleanupMoveAfterExchange requiring both ExchangePlanFile and
PauseAfterExchange. Isolated actual-prefix checks confirm missing plan and
missing pause reject before New-Item, while a valid row with both flags reaches
only the sentinel. All three checks create no requested evidence directory and
execute no ADB/controller body. Reviewer changed no controller source.

Control-flow review: after the single completed exchange swipe, the opt-in
branch sends one ordinary300ms swipe695,900→1000,500, records that input, then
sends normal Back and breaks. It cannot reach the RapidTouch burst branch
afterward. The normal OnProcessMove state-loss path (caught actor IsWaiting
false for states3/4/8) can clear the caught pair before its pointer-ID test.
A still-Waiting actor or other changed state may behave differently; the
gesture does not force/reset any native pointer. Paused-screen/caught-state
verification remains a separate root observation.

Zero post-gesture ordinary bursts must not be described as zero possible
ordinary attack events: the cleanup swipe begins with a normal DOWN at695,900.
If the exchange rejected and the catch already cleared, that DOWN can enter
the usual OnInputProcDash path. This is an ordinary-input side effect, not
proof the cleanup happened or a hidden native mutation. If native caught state
remains nonzero afterward, stop new inputs and qualify the source-normal
outside-OUT/matching-release behavior; do not assume CANCEL aborts or force
the pointer to0. Any caught0 sample after movement plus Back/ending must retain
the combined-action attribution limit. No live gesture was run by reviewer.
