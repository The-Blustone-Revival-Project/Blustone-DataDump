# Manual actor exchange: contact identity, release and cleanup

Read original `ghidra-skill-input-coordinate-path.txt` OnProcessPress export,
RMFrameworkActivity.java and the retained native-manual-exchange-contract.md/
native symbols. No Ghidra, ADB, live gesture, game state or helper edits. This
report does not authorize a swipe or supply a physical exchange-zone point.

## Root UI receives the contact before the game gates

OnProcessPress G9db1bc first calls root CMUpdatable::ProcessCursorPress with
TOUCH identity+0, the timing argument+4, logical point+10/+14 and boolean
`TOUCH+20 == 1`. The game pause140 and state13c mask0x14 checks happen afterward.
Therefore game admission checks do not prove the root UI ignored a contact.
A press intersecting a native button can still dispatch that UI's callback.
Do not treat a paused/suppressed actor path as permission to touch an exit
control or infer that a skill/capture press exclusively targets an actor.

Admitted phase1 with no current catch tries CatchActor G9db698; a caught actor
or successful capture prevents the ordinary OnInputProcDash branch. CatchActor
records pointer identity at game+194, strong caught pair+198/+19c and initial
touch-position offsets+1a0/+1a4. These are gesture-local state, not inventory
IDs or a new deck selection. CanCatch/airship membership and body-specific
GetFrontBound are separately documented and must be verified before capture.

For non1 phase, the captured pointer identity must match TOUCH+0. Only that
branch calls ExchangeActor G9db990. If it returns0, processing falls into the
DropActor path; a successful return does not take that failure cleanup. A
different pointer's release skips this exchange/drop branch. The native code
thus requires one continuous contact identity across capture/move/release;
separate DOWN contacts or releasing the wrong ID are not a substitute.

## ACTION_CANCEL is not an unconditional native abort

Original RMFrameworkActivity.onTouchEvent maps ACTION_DOWN to TouchesBegan,
ACTION_UP to TouchesEnded and ACTION_CANCEL to the same TouchesEnded call.
Pointer IDs are transformed to pointerId+1. Pointer-specific down/up also use
those methods; move dispatch visits active pointers. The Java bridge does not
preserve a separate cancel reason into this Ended call.

Consequently an Android CANCEL can reach the same native same-ID non1 branch
as an ordinary release. If the door/target/current states admit ExchangeActor,
it may exchange rather than cancel. A CANCEL inside a valid open exchange
zone is not a proved no-op/drop mechanism. Close the exact JNI TouchesEnded→
TOUCH phase path before naming any native cancellation semantics; do not add
a native DropActor call or write caught state to force cleanup.

## What the retained drop path proves

The OnProcessPress export's tail-called DropActor body is entered when an
actor is caught and the pause/state gate suppresses input, or after matching
release when ExchangeActor fails. It resolves the named root UI node/component,
calls CSRGameBGDoorDraw::Close, obtains the destination area's bound, computes
a return/fall path and calls the caught actor's FallTo. It then sets
game+198/+19c to0 and releases the old strong control reference.

No retained store here proves game+194 or initial offsets+1a0/+1a4 are reset.
Those residual values can remain stale after a null caught pair; requiring
them to be zero would invent a cleanup contract. Conversely, a FallTo/Close
call alone does not prove the catch pair cleared or the return animation ended.
The geometry calculation has decompiler return-register artifacts, so this
report does not reconstruct a landing point or duration from that pseudocode.

## Narrow original targets root must close before dragging

1. Standalone DropActor G9db364 and its exact entry/tail-call instructions:
   verify Close/FallTo and caught pointer/control clearing on each path, without
   relying solely on the merged OnProcessPress decompilation.
2. OnProcessMove G9dbe00: retain root cursor forwarding, captured contact-ID
   comparison, caught-state rejection and every DropActor/Close return. The
   current summary says it repositions the actor with the stored offset and
   opens/closes DoorDraw based on intersection; it does not yet establish a
   guaranteed move-outside abort or canceled-contact cleanup.
3. ExchangeActor G9db990: distinguish failure returns from success, capture
   pointer clearing/retention, and protocol14 model callbacks OnProcExchange
   Ga0fc04 / OnProcExchangeComplete Ga0fe9c. Another lane owns cost/model effects;
   this report does not infer them from the UI sender.
4. TouchesEnded and native TOUCH construction: identify phase values and whether
   any existing pause/back/scene-removal path independently drops a catch.
   Ordinary Android Back queues key input, not necessarily OnProcessPress,
   so it cannot inherit this contact-gate cleanup without its own callback proof.
5. Root OnTouch G9d72fc and actual named exit/back/forfeit controls: distinguish
   their listeners from the actor-capture hit area and exchange-zone drawable.

DoorDraw is an exchange visual/component on this path, while top exit/forfeit
buttons are separate root UI events. A shared word or visible central door
does not prove a safe dual-purpose hit target. Actor/body bounds are also
distinct from skill-icon bounds. Never use an exit-door press to force victory.

Before a future single ordinary capture gesture, root needs the owned actor,
CanCatch state, body-bound/coordinate conversion, exact drop target and an
evidence-backed ordinary release/cleanup path. No concurrent attack/skill
controller may reuse or interfere with the contact. Afterward inspect the
native caught pair and party/front serial state: a successful exchange, a
failed/drop cleanup and a still-caught actor are different outcomes. If cleanup
is unknown or the pair stays populated, stop new input and diagnose the exact
state rather than retrying another drag, injecting a native call or writing
the pointers. The currently verified skill-induced Karl exchange does not
prove the manual gesture or its failure cleanup.

## Fresh standalone exports close move/drop and name the zone

Read `ghidra-manual-exchange-ui.txt` and its `-keys.txt`, plus recovered original
KO/pristine27 `analysis/exchange-ui/INGAME_NM.xml`. These supersede the earlier
move/drop uncertainties where specified below; no live gesture was performed.

OnProcessMove G9dbe00 always forwards root cursor movement first. If caught
actor+198 exists but IsWaiting returns0, it immediately zeros+198/+19c, releases
the strong control and resolves/closes DOOR. This state-loss cleanup occurs
before the pointer-ID comparison, so it is not restricted to a matching-ID
move. If the actor is still Waiting, a wrong-ID move leaves it captured; the
matching-ID move sets its position from TOUCH coordinates minus saved offsets.
There is no unconditional DropActor call in the inspected move body.

Matching movement resolves DOOR_ROOT, then its DOOR component. If IsOpened is
true, it compares the caught actor's GetFrontBound rectangle against OUT and
closes when those rectangles do not intersect. If not opened, it compares
against IN and opens only on intersection. This is a two-zone hysteresis
contract, not simply whether the finger lies inside a drawn door. Neither
opening nor closing in this move branch clears the catch. IsOpened is still a
computed timer/interpolation predicate; an attempted move-away does not prove
the door has closed until its exact predicate/state is verified.

The original XML has transparent BG_BACK containing DOOR_ROOT size148x197,
bottom-centered pos0,-81. Its DOOR rect renders UI_IG_FT_DR; sibling IN is a
hidden rect size126x410, pos2,-240, center-aligned; OUT is transparent size160x500,
pos0,-41, center-aligned. These are plain rect/sprite nodes, not button event
declarations. Hidden IN remains a named geometry target of the native lookup;
its hidden rendering does not remove the explicitly consumed bound. Parent
screen scaling/alignment and resident transform are still necessary to recover
the actual physical drop geometry; these local sizes are not ADB coordinates.

Standalone DropActor G9db364 confirms the retained merged-body interpretation:
resolve/close DOOR, obtain return geometry, call caught actor FallTo, then set
198/19c to0 and release the strong owner. It does not reset194 or1a0/1a4 in this
export. The exact return animation and subsequent input-readiness observation
must not be equated with the immediate pointer stores.

ExchangeActor G9db990 resolves DOOR, checks computed IsOpened, caught actor raw
byte270==0 and background/state field278==0, finds current front group actor,
and checks front stun/exchange-stop and caught IsWaiting. Only the admitted
branch emits protocol14 with exact recovered JSON keys:
`to_runner = caught serial`, `to_waiting = current front serial`.
The fresh OnTouch G9d72fc literals cover PA_AUTO_ALL/DASH/OFF/LOCK and
PA_X1/X2/SPEED_LOCK, not a demonstrated exit/forfeit button. Thus these named
central exchange rects are distinguished from an exit control by actual
consumers; the exact separate exit listener remains unclosed here.

### Successful release cleanup still needs its exact store provenance

The fresh ExchangeActor decompilation is incorrectly typed void despite the
OnProcessPress caller using its result to select failure/drop. Its protocol14
branch goes to common return, and the inspected section contains no explicit
198/19c reset stores. This review therefore cannot attribute a direct successful
release reset to ExchangeActor solely from that decompilation. Root should
retain exact Thumb return/store evidence or the specific model callback that
clears the caught pair. A later move after IsWaiting becomes0 demonstrably
clears it, but this is a distinct path and not a proof every success promptly
clears without another movement event. Do not hide this distinction by saying
all releases drop or all protocol sends reset the catch.

Same-ID Ended processing still calls ExchangeActor and uses failure DropActor;
wrong-ID release does not obtain that cleanup. Java CANCEL still collapses to
Ended. No force reset, guessed callback, native invocation or exit-door tap is
proposed. Required remaining closure is the successful-release return/store
path, resident geometry/IsOpened state and an exact ordinary failure cleanup
gesture that cannot accidentally exchange. Model cost behavior belongs to the
separate model lane, and no live manual exchange has yet been verified.
