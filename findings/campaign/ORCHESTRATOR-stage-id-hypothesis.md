# ORCHESTRATOR FINDING 2 — the stage-lookup key is probably EMPTY (`/lobby/Enter` sends no `stage_id`)

Written by the orchestrator, 2026-10-02. Companion to `ORCHESTRATOR-arity-constraint.md`.
**[INFERRED]** from a source reading plus the measured invariant, but it is cheap to test and it
explains every prior negative at once. **Ranked #1 testable hypothesis.**

---

## 1. The observation

`CSRUserDB::GetCurStageID()` appears **in the crash chain**:

```
+0x9c3df1  CSRGameBase::MakeCamp(std::list<CSRGameActor::ACTOR_INFO> const&, TEAM_DIR, CMHashID const&)
+0x96cea7  CSRGameActor::OnInit()
+0x108a8cf CSRUserDB::GetCurStageID()          <-- obtains the current stage id
+0x8a34f3  CMSingleton<CSRDataMgr>::get()
```

It is a **`CSRUserDB`** method. `CSRUserDB` is the client-side mirror of the lobby user payload,
and the only thing that fills it is `/lobby/Enter`.

Now read what the replica actually sends. `server-ts/src/state.ts:349-355`, the `user` object:

```ts
user: {
  ap, bp, gdp, max_ap, max_bp, max_gdp,
  gold, honor, group_exp, vip_exp, card_inven_max,
  ap_charge_time, bp_charge_time, leader_inst_id,
  is_newbiew, is_dailyquest_newbie, is_shared, pm_key,
  tuto: tutorial,
  area_achieve: areaAchieve,
},
```

**There is no `stage_id` in it.** The only `stage_id` strings anywhere in the `/lobby/Enter`
response are *nested inside the `area_achieve[]` array* (`state.ts:340-343`), which is a
per-area progress list, not the current-position field.

## 2. Why this explains the arity invariant

`report-009.md` §7 recorded `stage_id : PRESENT` in `/lobby/Enter` — but that is a substring
match against a **flattened** view, and it matched the `stage_id` **inside `area_achieve[]`**.
Nobody has checked the **path**. This distinction is the whole ballgame.

If `GetCurStageID()` returns `""`, then every downstream stage-keyed lookup runs under the empty
key:

1. The client cannot resolve which stage it is fighting, so it instantiates its **fixed
   five-slot** enemy formation — the party size is not data-driven at all, which is precisely
   why the count stayed at 5 through a party of 1, a party of 4, wave-id variants and profile
   variants.
2. Each of the five slots resolves its monster id through a stage-keyed table. Key `""` finds
   nothing, so each id is a **default-constructed empty `std::string`**.
3. Hence `GET /reference/GetMonster {"list":"[\"\",\"\",\"\",\"\",\"\"]"}` — five empties, which
   is *exactly* what is observed, byte-identical, in all seven runs.
4. Hence five `CSRCard::SetRefID` assertions (`sRefID.length() > 0`, `SRCard.cpp(731`).
5. Hence one `CSRGameMob::GetMonsterData` miss (`SRGameMob.cpp(38`) on the derived empty id.
6. Hence the `CSRGameMob::INFO` copy constructor emplacing into an absent
   `std::tree<SRSKILL_INFO>` and faulting at `+0x10`.

**This is the crucial part: under this hypothesis, the contents of `wave_list` cannot matter,
because the key used to find it is wrong.** That is not a guess about which field to populate —
it is a statement that *every* field-level experiment run so far was addressing a table the
client never successfully indexed. It is the mechanical reason five well-reasoned fixes in a row
each produced zero change.

## 3. The corroborating smell in the existing code

`server-ts/src/game-routes.ts:127-132` contains this, with a comment reading:

```ts
if (requestedStageId.length <= 1) {
  // `stage_id=""` - seen when the client had not yet resolved a node. Give
  // it the recovered entry under the empty key so the stage builder can
  // still find a wave.
  return state.envelope({ "": wavesFor("n_01_01") });
}
```

Someone already saw an empty `stage_id` in the wild and worked around it **on the request
side** by registering waves under the `""` key. That is a strong hint that the empty stage id
is real and systemic rather than a one-off. It also means the `""`-keyed fallback path has
already been exercised without effect — which is consistent with the *internal* lookup using a
different key again, or with the waves simply not being what fills the five slots.

## 4. The test — trivial, and it is the highest-value experiment available

Add a `stage_id` to the `/lobby/Enter` `user` object carrying the stage the client is actually
on, e.g. `stage_id: "N003"`, and keep it consistent with what `/mission/Start` is sent
(`"N003"`) and with the `stage[]` progress list already emitted at `state.ts:388`.

**Predictions if the hypothesis is right:**
- `GetMonster list` stops being five empty strings. That is the single observable. It has never
  moved in seven runs, so any movement at all is decisive.
- `SRCard.cpp(731)` drops below 5.
- The `GetMonsterData` miss may clear.

**Predictions if it is wrong:** nothing changes, and we have cleanly eliminated the user-DB
stage identity in one run — which is itself worth having, because it retires the whole family.

This costs one field. It is cheaper than every experiment that has failed so far.

## 5. Verification that must accompany the test — do not skip it

The change must be verified **on the wire**, not by eyeballing the source, because the whole
finding turns on a key *path*:

- Confirm with `BLUSTONE_DUMP_RESPONSES=1` that `/lobby/Enter`'s response has `stage_id` at the
  **top level of `user`**, not merely somewhere inside `area_achieve[]`.
- Confirm the client echoes it: the `stage_id` in `/mission/Start` and in
  `/reference/GetTargetStageMonster` should agree with it.
- **Check whether the native field is even named `stage_id`.** `GetCurStageID()` has been
  assumed to read `stage_id`; that is an assumption, not a recovered fact. The Ghidra agent
  should decompile `CSRUserDB::GetCurStageID` at `+0x108a8cf` and read the **actual** member
  offset and the **actual** JSON key it was parsed from. Guessing the name and guessing right
  would be a lucky result we could not trust; the decompile makes it knowledge.

## 6. Honest status

- The **absence** of `stage_id` from the `user` object is a **direct source reading** and is
  solid — `state.ts:349-355` says so.
- The **conclusion** that this causes the five empty ids is **[INFERRED]**. It rests on the
  arity invariant plus the presence of `GetCurStageID()` in the crash chain. It is not proven.
- The competing explanation remains live: the five slots may be filled by a source outside the
  stage-monster table entirely (the `/mirage/GetInfo` `inst_enemy` lead, or the opponent
  profile). If the `stage_id` test moves nothing, that lead becomes the priority.
- Both are cheap. Run the `stage_id` test **and** the `mirage/GetInfo` fixture in the same
  round, so one device cycle tests both and they cannot be confused for one another. Make each
  independently switchable by environment variable so a negative result is attributable.
