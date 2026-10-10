# Ordinary campaign: current EXP and reward audit

2026-10-09. Read-only source review and sanitized game-state inspection. No UI,
ADB, Ghidra, runtime changes, save writes or auth-secret output. Native parser
evidence is retained in `mission-hunter-exp-contract.md`; this report audits the
current implementation rather than claiming original reward amounts.

## Expected receipt for the current four-Hunter party

Current main account formation is `[1000002,1000004,1000001,1000005,0]`.
Owned instance serials are separate from card reference IDs and account pvid.
The namespace base 1000000 is a local allocator policy preserving Episode's
small fixed actor serials. Never substitute ref IDs `001`..`004` in the receipt.

A newly accepted matching normal campaign win, with that formation snapshotted
by Start, should publish the following directly under `ret_data.card`:

```json
{
  "1000002": { "prev": 240, "cur": 250 },
  "1000004": { "prev": 240, "cur": 250 },
  "1000001": { "prev": 340, "cur": 350 },
  "1000005": { "prev": 840, "cur": 850 }
}
```

These are Mowgli/ref002, Nene/ref003, Lantern/ref001 and Tyltyl/ref004.
Current ranks are respectively 1,3,1,1; all awakening steps are 0. Published
ordinary curves have thresholds 0,100,...,2900 for every supported rank. Thus
these gains preserve levels 3,3,4,9. All four gains are expected even if a Hunter
died: equal participant reward is local policy; the original per-survivor rule
is unknown. No Karl or nonparty Hunter gains EXP.

Native ReqCompleteCB consumes decimal serial keys containing **absolute**
`prev`/`cur`, then SetCardExp recalculates level from the published rank curve.
No nested EXP object, delta-valued `cur`, or explicit receipt level is needed.
Backend code is `state.ts:1924` onward; there is no source module named
`mission-complete.ts` (that name belongs to tests).

## Eligibility, caps and reservation

Start snapshots up to four positive posted deck slots; with no positive posted
slot it uses type-1 saved formation. Namespace-1 requests reject any nonzero
posted ID not owned by the account. Zero slots are skipped. Complete requires
the active stage and, when supplied, battle ID to match. Wrong-stage and
duplicate/no-active requests return accepted=false and card={} without rewards
or discarding a different active attempt.

Complete deduplicates positive snapshot IDs, takes at most four, checks owned
membership and awakening=0, then uses trainingCurve. Unknown curves are omitted.
New cumulative EXP is `max(previous,min(2900,previous+10))`: at-cap entries return
unchanged pairs and existing over-cap EXP is preserved. The snapshot rather than
an edited saved formation governs backend EXP; native callback still enumerates
the native current deck, so avoid changing its deck during an active attempt.

Matching loss returns card={}, pays no first-clear reward or capsule, and refunds
only that attempt's recorded AP charge with overflow preservation. Complete
clears active_battle and persists ownership and reward changes together. Training
material consumption protects active snapshot members; all current Hunters are
also locked. A new same-stage Start within the configured idempotency window
replays the active attempt without a second AP charge; later fresh attempts
replace stale active attempts and charge anew.

## Other visible deltas

Baseline main account: gold11680, team EXP840, AP50, capsule inst7 qty36.
Start costs1 AP. A win does not refund; AP regeneration may independently change
the observed final counter. BP, Manda, VIP EXP, owned ranks/skills/decks and
Episode progress are not part of normal mission rewards.

An already-cleared stage replay should keep gold11680/team EXP840 while paying
the four +10 Hunter EXP gains and one capsule (`AIRSHIP_TICKET`, inst7, added1,
qty36→37). A previously uncleared normal stage adds gold10 and team EXP30,
marks clear and may create the victory notice and earned Special Supply entries.
`n_03_08` was uncleared at inspection; earlier stages through `n_03_07` were
cleared. These values are a baseline, not a post-play result.

Stars are independently derived from native clear_time/dead_cnt: index0 for win,
index1 for time<60s, index2 for dead_cnt<=1. Receipt achieve contains only newly
earned orders; a replay can add missing stars. Do not expect unconditional three
new stars or claim exact original condition evaluation from this local policy.

## Source limitations / discrepancies

Character reward10, gold10, team reward30, one-capsule-per-win and replay Hunter
EXP policy are local revival values, not recovered original server rewards.
Stage publication currently advertises `group_exp:10`, but Complete awards
first-clear user EXP30. This is an existing fixture inconsistency and should be
kept visible; it does not change the expected card EXP10 or prove any original
reward. Stage AP cost1 matches Start's fixed1 charge today.

The Hunter EXP tests cover caps, rank/awakening omissions, snapshot binding,
replays, duplicate/loss/stale isolation and restart using a legacy ID fixture.
That does not itself prove namespace-1 live response application or rendered
result/Gym consistency. Those require root's legitimate native win and sanitized
before/after save plus receipt evidence. No source bug in the four current
Hunter EXP calculation was identified by this review.
