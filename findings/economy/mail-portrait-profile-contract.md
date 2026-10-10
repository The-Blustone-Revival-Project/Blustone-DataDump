# Mail portrait uses target brief profile and image URL

2026-10-07. Read-only original ELF, retained CellMailPost dump and current source.
No Ghidra/device/source/account actions, new accounts, messages or grants.
Code addresses use Ghidra coordinates; vtables explicitly use ELF coordinates.

## Actual consumer chain

**CellMailPost.Init G89e1c0** creates CSRUserProfileDraw at89e34e, loads the
selected message pvid from DATA+28 at89e392 and calls **SetPVID G10aa770
at89e396**, attaching the drawable under **USER_THUMB**. The displayed name
is independent DATA+38. USER_TALK is the content textbox, not the portrait DTO.

SetPVID calls **CSRUserPool.Get G10a397c at10aa850**, passing its result callback.
Original maker LDR10aa83e/ADD10aa844 resolves **ELFVT21878e8**, RTTI
CSRUserProfileDraw.SetPVID$_2, invoke **G10abd9a**. With a valid captured
drawable/nonnull target-user result, this callback passes **SRTARGET_USER+40**
to **LoadImageFromURL G10ab404 at10abdd4**. No leader card slot or hunter
ref_id lookup is used in that portrait call.

## Actual HTTP shape, distinct from detailed party profile

The relevant relation callback is **CPVRelation.ReqUserInfoCB G8227f0**.
Original literal/code proof extracts **fullJSON.ret_data**
(LDR8229d0/ADD8229d2/call8229d6), then **ret_data.list**
(LDR8229da/ADD8229dc/call8229de), iterates its rows and invokes
**CPVRelation.GetTargetInfo G822c54**. Thus this is neither a flat party
profile nor a bare ret_data array:

```text
ret_data: {list: [TARGET_BRIEF_ROW, ...]}
```

Exact row keys recovered by same-register PC-relative literal resolution:
**pvid, reg_utc, utc, nick_name, country_code, profile_url, profile_status,
like_cnt, is_like**. Identity/time/count/flag fields use scalar conversion;
nickname/country/URL/status use native string fields. Mandatory strict string
conversions require actual strings, including a valid URL for a real portrait.
Original detailed card-profile parser **CSRSyncGlobal.ParseUserDatailInfo
Gf6e240** belongs to a different consumer; its ref_id_leader/ref_id_1 etc do
not satisfy this brief target parser.

Current reserved-local-sender1 route returns a flat partyProfile with nickname
aliases, lacking both list and profile_url. This is a concrete mismatch with
the requested relation brief-profile callback, independent of sender-name
selection. The reserved sender is a local display identity, not an account
created by this research. Other callers/AI response grammar should be reviewed
against their own callback before broad alias replacement.

## Image requirements and bounded next implementation

LoadImageFromURL recognizes **http:** (ADD10ab45c) and **https:**
(ADD10ab486); it has URL prefix manipulation, not a proved card-art-name
fallback. Merely inserting001/C001_TH or a JET package URL as profile_url is
not a valid image binding. A real local portrait requires an actually served
image resource in the format accepted by that loader. No suitable endpoint
or original administrative avatar was recovered here.

The smallest coherent fix seam is reserved sender's **ret_data.list brief row**,
followed by a source-backed, real served local image URL. Preserve the mailbox's
actual recipient and do not invent an external person's profile/account.
Header-name success alone does not prove the image/cache result was accepted.
Exact remaining parent decompile targets: **8227f0,822c54,10a2ffc**
(UserPool.Update), **10abd9a**, **10ab404**. Native cache registration and
portrait rendering remain pending runtime proof; no source fix was made here.

## Fresh brief response still waits for detailed profile

Parent implemented a reserved sender1 brief list row and a genuine locally
served PNG URL; fresh native target request succeeded, but no image GET followed.
New parent decomp ghidra-mail-profile.txt/-image.txt/-url.txt closes the next
dependency, rather than proving a stale image cache.

**UserPool.Update G10a2ffc** has distinct cache branches. When no completed
DATA exists, it creates a SRTARGET_USER, copies the PV_TARGET_INFO brief row,
registers pending listeners in the request map atUserPool+4c, and calls
**AddQueueDetail G10a32a8** (retained decomp lines731..745). It does not yet
invoke the portrait listener. The completed DATA branch updates the brief
fields and can immediately invoke an explicitly supplied callback.

**UserPool.RequestDetail G10a2ca4** calls
**CSRSyncGlobal.AsyncRequestUserDetail Gf66944 at10a2db6**. Original requester
builds auth plus JSON-string **list** (ADDf66afa), posts exact
**/world/GetUserDetail** (ADDf66c7a/f66cd0). Its result callback is
**ReqUserDetailCB Gf671c0**, which calls **ParseUserDatailInfo Gf6e240 atf672be**
before forwarding the resulting map. This separate detailed receipt must bind
the same reserved pvid before an uncached target becomes complete.

Current source has no dedicated /world/GetUserDetail handler; it reaches the
generic successful metadata fallback. That is a concrete missing protocol seam.
A correct brief response and reachable PNG alone cannot finish this two-stage
cache operation. Parent should first check bounded fresh traffic for
/world/GetUserDetail list[1] and inspect **f671c0/f6e240** plus the
UserPool.RequestDetail completion closure. A normal reload is not justified as
the primary fix from the current evidence.

The image callback's fresh decomp confirms it uses SRTARGET_USER+40 profile_url
only after receiving a nonnull completed target. LoadImageFromURL additionally
compares the requested URL hash with its current hash before LoadImg; this is
an image-request deduplication guard, not proof the present blank image is cached.
No extra brief-row nesting or registration-time gate was identified in the
reviewed parser. Original detailed profile map/container grammar still needs
its own exact parser proof before implementation; do not copy flat party data
into the wrong response parent. No server/account/image edit was performed.

## World detailed container closed

Root's bounded native wire confirms /world/GetUserDetail at12:27:11.169Z with
list[1], receiving generic fallback. Fresh ghidra-mail-world-detail.txt confirms
ReqUserDetailCBf671c0 decrypts/parses a full envelope and forwards the map
returned by ParseUserDatailInfof6e240 to its success callback.

Original ParseUserDatailInfo input JSON is r2. It extracts **ret_data atf6e278**,
keeps it in sb, counts that collection and performs **numeric operator[](index)
atf6e300**. Therefore the exact detail wrapper is **ret_data:[DETAIL_ROW]**,
distinct from relation's ret_data.list. A flat detailed row or list wrapper is
not supported by this parser.

For reserved sender1, existing partyProfile(1) supplies the recovered fields:
pvid/group_exp/vip_exp/league_level/rating_point/awake; complete leader and
slots1..4 inst/ref/rank/rank-up/awake/overcome/EXP/skill/skin fields; stage_id,
prev_rank, win_message, lose_message. Known nonempty ref001 has existing
published reference/art; these transient presentation cards are not inventory
grants. Required string reads are populated by that fixture. No honor field
appears in the inspected41-key detailed parser, so it must not be invented as
a mandatory prerequisite. Relation's URL/name brief fields remain in the
pending target record and should not be confused with this detailed row.

This closes the immediate parser/container gap for a reserved-only reply; actual
detail-map/cache completion and image loading still need native proof. If valid
array detail produces no image request, next inspect UserPool.RequestDetail's
completion closure and pending callback drain rather than guessing new fields
or restarting solely from an absence of GET. No implementation was done here.
