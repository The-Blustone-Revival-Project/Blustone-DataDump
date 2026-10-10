# Stage4 replacement guide: gesture and completion contract

2026-10-04. Offline native read-only; no adb/Ghidra/client/source edits.

The stage4 guide does not complete because a drag ghost exists or an enemy
reaches0 HP. It waits for the **runner exchange callback**.

`CSRTutorialMStageSkill::OnRunnerExchange f0101c` checks game+408==4 and
byte+426==0 (f01032..40), updates the guide UI, stores426=1 atf011aa and
calls ResumeGame(10) atf011b2. It does not check a particular incoming card
ID or role in this callback. OnExchange f00d6c has the same stage/flag gate.
Thus Nene is a candidate because she can supply an actual reserve actor,
not because the guide explicitly names Nene or requires Defense2.

## Normal gesture: capture a reserve, drag into the entrance, release

Common OnProcessPress9db1bc first passes the pause gate (mask0 or bit10 is
allowed) and checks game-state13c bits14. For a press (touch+20==1),
CatchActor9db698 iterates **waiting actors game+188/+18c**, checks CanCatch,
and tests the touch against each actor's FrontBound at9db6e2..ee. It saves
its actor pointer to game+198 and touchID to+194.

OnProcessMove9dbe00 only handles that saved caught actor and matching touch.
It moves the caught visual and tests its FrontBound against the named door
region. Intersection at9dc0ac..c0 opens the door at9dc0c8. A ghost by itself
therefore proves capture/movement, not a legal exchange.

On release (touch+20!=1), OnProcessPress9db2dc compares the same touchID and
calls **ExchangeActor9db990 at9db2e8**. ExchangeActor requires the door's
IsOpened9be692=true (9dba04..0a), caught actor+270==0 (9dba10..1e),
a current front actor in the same group, no front stun, no ExchangeStop,
and caught actor IsWaiting=true. It then sends native protocol0e via
GameNet virtual+48 at9dbc60..6c. Release after the door opens is therefore
material; repeated battlefield taps are not equivalent to this gesture.

## Eligibility and what role2 does—and does not—prove

CanCatch9864d2 requires:

```text
actor_clock(+228) - last_exchange_time(+a58) >= GetExchangeCool()
input_binding(+a6c) != null
actor_byte(+270) == 0
```

It contains **no role comparison**. Common CanExchange99b34e also requires
HP>0, no exchange-stop buff+a4 and exchange-cool count+a0<1. The group's
ExchageKeys9a3a88 verifies CanExchange on outgoing and incoming actors,
and checks outgoing stun; role is not directly compared in the inspected
part of that routine.

IsWaiting97e70e returns false for native actor states3,4,8, true for other
states. A visually rendered reserve must actually satisfy that state predicate.
Roles3 Bomber and4 Support are classified as airship-skill roles by
SRCanUseSkillAirShip10ae4b0 (role-3 unsigned<2); actor IsSupport97ecc0 uses
that exact helper. Role2 is outside this classification. **A complete native
role1/2-only exchange selection predicate has not been located by this report.**
Do not present role2 alone as sufficient, or claim all role3/4 objects are
unconditionally rejected by CanCatch. Placement/state/binding are decisive.

The narrow verification for added Nene003/Defense2 is:

1. Confirm owned instance is in the saved mission deck and instantiated as a
   live waiting actor, with HP>0, binding+a6c nonzero and270=0.
2. Press her actual reserve portrait/body bound, drag it into the entrance
   until the door opens, then release the same touch.
3. Confirm protocol0e exchange succeeds and the front actor changes, followed
   by native OnRunnerExchange: guide426 becomes1 and pause10 clears.
4. Only then use battle Complete/victory as the end-to-end result.

If this candidate still fails, a bounded reader can inspect waiting-list
sentinel game+188, first pointer+18c, actor at node+8/shared-control+c,
next node+4, and the already-proven guarded actor fields above. Respect the
same vptr, mapped-read, maximum-node and cycle guards as the live reader.
