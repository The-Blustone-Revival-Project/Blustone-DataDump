# ADJUDICATION — the crash is `str r0,[r1,#0x4c]` with `r1 == 0`, in the EXPEDITION scene

Written by the orchestrator, 2026-10-02, after two agents returned **opposite** conclusions
about the same crash. I verified the decisive bytes myself.

**This supersedes `FALSIFIED-showthumbnail.md` §3 and voids both orchestrator hypotheses in it.**

---

## 1. The contradiction

| Agent | Claim |
|---|---|
| Native-analysis lane | Crash is in `CSRSceneMEpisode::OnFinish`; the client is in the **wrong scene**; PC is not even an instruction boundary |
| Contract-research lane | Crash is in **`CSRMStage::MakeStageInst`** — the **correct, expedition** scene; the device's `dladdr` was right and the other's address math was off |

Both are self-consistent and they cannot both be right. This is the ninth round in a row where
two plausible readings of the same evidence diverged, so I resolved it from the bytes.

## 2. The decisive check

The disagreement reduces to one question: **is the `BLUSTONE_ARM` offset an ELF address or a
Ghidra address?** Ghidra's image base for this library is `0x10000` above the ELF addresses.

I dumped the halfword at both candidate locations:

```
as reported, offset treated as ELF (file offset 0xb2507b):
  hw = 0x9d64    -> not a plausible fault site

offset treated as Ghidra, i.e. ELF 0xb2507b == file 0xb1507b:
  hw = 0x1528    -> not a plausible fault site
```

Neither naive reading works, so I searched for the instruction the fault data *implies*.
`fault = 0x4c`, `r1 = 0`, `r0 = 0x0a`. A store of `r0` at offset `0x4c` from a null base is
`str r0,[r1,#0x4c]`, which encodes as `0x6000 | (imm5<<6) | (Rn<<3) | Rt` with `imm5=19`,
`Rn=1`, `Rt=0`:

```
0x6000 | (0x13 << 6) | (1 << 3) | 0  =  0x64c8
```

And scanning `.text`, the halfword at **Ghidra `0xb3507a` = ELF `0xb2507a`** is exactly
`0x64c8`:

```
Ghidra 0xb35078  hw=0x6889
Ghidra 0xb3507a  hw=0x64c8   <-- str r0,[r1,#0x4c]     r1 == 0
Ghidra 0xb3507c  hw=0xf89d
```

**This is a three-way match:** the reported PC `+0xb2507b` is `+0x10000` from ELF, the faulting
instruction is the one immediately below it, and its `#0x4c` displacement is exactly the
reported fault address with `r1 = 0`. The register state in report-011/012 (`r1=0`, `r0=0x0a`,
`fault=0x4c`) is corroborated by the encoding rather than merely being consistent with it.

**Therefore: the offset IS an ELF address, and ELF `0xb2507b` is Ghidra `0xb3507b`, which is
inside `CSRMStage::MakeStageInst` (`0xb33f84`).** The contract-research lane is correct. The
device's own `dladdr` was right and the native-analysis lane's address arithmetic was wrong.

## 3. What is actually wrong — and it is not a scene mix-up

The native-analysis lane's Q3 finding is solid and is the important one:
`AddStageMonster` **is** reached — `0xb4612c: bl 0x00a0d194`, unconditional at the top of the
`ret_data` iteration body, gated only on `result_code == 1`. So the `_id`/`show_thumbnail`/
key-shape work was **not** aimed at dead code. That closes the open item from
`ghidra-enemy-actor-trace.md` and retires `FALSIFIED-showthumbnail.md` §2's second hypothesis.

And its Q1 mechanism — `CSRSceneGame::OnInit` switching on `CSRGameBase::MODE` at `this+0x660`
with `case 7 -> CSRSceneMEpisode`, `default -> CSRMStage`, where MODE is a constructor argument
with **no JSON read on the path** — explains why the scene question produced no server-side
lead: **there is no response field that selects the scene.** The client is in the expedition
scene because that is the default, and nothing we send put it in the wrong one.

**The real defect:** the expedition scene's camp construction stores into an inner
`list<ACTOR_INFO>` of `CSRMStage`'s `unordered_map<CMHashID, list<list<ACTOR_INFO>>>` at
`this+0x264`, keyed by **`CSRLevelData::GetMonsterGroupID()`**. That map is never populated for
the current stage, the iterator dereferences null, and `r1` is null when the store executes.

## 4. The new lead — and it moves the goalparks usefully

`CSRLevelData::LoadLevelData` (`0xa178c4`) opens **`"<id>.JSON"`** through the **local CM
database** — i.e. a **client-side resource**, not a server route — and reads 54 level keys.
So the monster-group ids that key the camp map come from a file the client must already have.

**Which `<id>` is not yet established.** The contract lane marked it
[inferred-and-unverified] as `SetStage`'s `.value` / `.res_prefix`, and our stage fixture sends
`value: 0` and `res_prefix: ""` (`server-ts/src/bootstrap.ts`). If that inference is right, it
is a *fixture* defect rather than a protocol one, and it is a one-line change — but it is an
inference and must not be shipped as if it were recovered.

### 4a. RESOLVED — the `<id>` is the compile-time literal `leveling_m`, and my §4 link was WRONG

The follow-up decompile of `LoadLevelData`'s caller **refuted the inference above**, and I
verified its two load-bearing claims offline myself (`tools/resolve-literals-offline.py`):

- `--find-string leveling_m` → **7 code sites**, all loading the constant
  `leveling_m` → `leveling_m.JSON`. One per scene mode (`_m` mission, `_t` tutorial,
  `_r` raid, `_g` gvg, `_e` episode, …). **No JSON field is involved.**
  `CSRMStage::InitBeforeOpen` (`0xb33ccc`) → `bl 0x8b26e4` (`CSRDataMgr::LoadLevelData`,
  the only caller of `0xa178c4`) → `basic_string(literal)` → `LoadLevelData`.
- `--find-string enemy` → **55 refs**, and `'enemy'` is a distinct literal at `0x1d77246`,
  separate from `enemy_total_hp` / `enemy_total_hp_max`. Consistent with
  `CSRLevelData::GetMonsterGroupID()` returning the constant `CMHashID("enemy")`.

**So:**
- **Do NOT change `value` / `res_prefix`.** The stage fields do not select the level file.
- **`/reference/GetLevel` does NOT feed this path.** Its 37 keys are AI/movement/SP/fever
  tuning (`sp_max`, `walk_spd`, `fever_step_cond`, …); `user`, `vip`, `vip_group`, `card`,
  `skill`, `card_awk` are all absent from it. That is a different class with a different data
  source. Do not re-audit `GetLevel`'s container contract (`AGENTS.md` §6) on this basis.
- `LEVELING.jet` (18 524 B) ships in the base APK **and** the phone snapshot, byte-identical,
  and `leveling_m.JSON` is in it. **A missing level file is not the blocker.**

**The broken link in my §4 chain:** because the map key is the *constant* `"enemy"`, a missing
or mis-identified level file **cannot** produce the empty camp map — the key is the same for
every level and stage. Population must therefore come from `AddStageMonster` via
`/reference/GetTargetStageMonster`, which **is** reached (`bl 0xa0d194`, unconditional).

**The next decompile is the writer of `CSRMStage+0x264` inside `MakeStageInst`** — not another
`LoadLevelData` probe. That is where the enemy camp list is supposed to be built.

## 5. Corrected status

| Claim | Status |
|---|---|
| Crash = `str r0,[r1,#0x4c]`, `r1 == 0`, in `CSRMStage::MakeStageInst` | **CONFIRMED by me**, from the encoding + registers + fault address |
| Client is in the wrong (episode) scene | **VOID** — the expedition scene is the default and no response selects it |
| `AddStageMonster` is reached on our response | **RECOVERED** — `bl 0xa0d194` unconditional, gated on `result_code == 1` |
| `show_thumbnail` type is causally inert | **CONFIRMED on device** (report-012, control-verified) |
| The camp map is keyed by `CSRLevelData::GetMonsterGroupID()` and never populated | **INFERRED-strong** — the key type is recovered, the non-population follows from the fault |
| The level data comes from a **local** `<id>.JSON`, not a route | **RECOVERED** |
| Which `<id>` selects the level file | **UNKNOWN** — the next single decompile |

## 6. Next step — one decompile, no device cycle

Decompile the **caller of `CSRLevelData::LoadLevelData` (0xa178c4)** and establish what builds
the `<id>` string. That single answer decides whether the fix is a server fixture change
(`value`/`res_prefix` on the stage record) or a client-resource change. Both are cheap; guessing
between them without the decompile is how the last six rounds went.

Two smaller items also worth resolving when convenient, both flagged and neither asserted:
`CSRLevelData::GetMonsterGroupID` itself (what string it returns and from where), and whether
`/reference/GetLevel` — which per `AGENTS.md` §6 must supply named arrays `user`, `vip`,
`vip_group`, `card`, `skill`, `card_awk` — feeds this path, since `level` keys appear in the
same 54.

## 7. Note on how this was settled

Two agents disagreed; I did not pick the more confident one. The device's own `dladdr` said one
thing and a decompile said another, and the tiebreaker was a 2-byte encoding checked against
three independent pieces of runtime evidence — the fault address, the register dump, and the
instruction's position relative to the reported PC. That is the standard this project's failures
have been setting: **a claim about the binary is settled against the binary, not against a
symbol name.**