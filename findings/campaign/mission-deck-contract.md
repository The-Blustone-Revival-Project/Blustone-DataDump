# Mission Build Team: save contract and persistent lobby deck

2026-10-03. Read-only original-library inspection with Capstone and the offline
literal resolver. No source edits, Ghidra, adb, client rebuild, or live capture.
All addresses below are Ghidra image addresses, ELF+0x10000.

## 1. The common Build Team save route is /world/SetDeck

**[RECOVERED]** `CSRDeckHandler::SaveEntry` starts at `0x8b8ddc`. It assembles
the selected party in a DECK_INFO structure and calls
`CSRSyncMStage::RegisterDeck(DECK_INFO const&,DECK_CASE,callback)` at
`0x8b93d4` (callee `0xb3dbb0`). The requester constructs its six-entry form map
with `deck_info` as a JSON-dumped string, then posts **/world/SetDeck**.

The JSON embedded in the form field is:

```json
[{"type":1,"list":[1,3,0,0,0]}]
```

The ids above are an example of two distinct owned instances, not original
instance ids. The ordered numeric array selects the party slots. Account/form
fields include app_code,app_ver,market,pvid,otp,deck_info.

Exact builder evidence:

- `0xb3dbd6..0xb3dc02`: finds DECK_INFO's map record for requested DECK_CASE.
- `0xb3dc22..0xb3dc32`: serializes each uint64 instance serial into JSON array.
  Array traversal uses stride8 in the native instance vector.
- `0xb3dc48`, literal slot `0xb3de14` + PC `0xb3dc58`: **type** at
  `0x1d669f5`; enum value is serialized into the object at `0xb3dc66`.
- `0xb3dc98..0xb3dc9e`: puts instance array under **list**.
- `0xb3dcda..0xb3dce2`: copies that object into JSON array element0. It is
  an array of deck records, not a bare object and not a bare instance array.
- `0xb3de6c`: JSON.dump; `0xb3de70..0xb3de78`: pairs the dumped string with
  form field **deck_info**.
- `0xb3df96..0xb3df9c`: literal **/world/SetDeck**.

There is also `RegisterDeck(json const&,callback)` (`0xb3d30c`) which dumps
the supplied JSON as deck_info and uses the same path. It is a generic
preconstructed JSON overload, not a distinct endpoint. Its direct caller
`0xe79866` belongs to `CSRSceneMStageEntrust`, a different use of the common
route; do not equate that caller with Build Team selection.

## 2. Save response: only success code is consumed

**[RECOVERED]** `CSRSyncMStage::ReqDeckCB` (`0xb3d95c`) checks transport
callback status and CPVHTTPResponse::GetResultCode. If successful it decrypts
and parses the JSON, then reads only **result_code** (`0xb3da02..0xb3da46`)
and passes that integer to the saved callback (`0xb3da66..0xb3da74`).
No ret_data field or returned deck is parsed in this callback.

```json
{"result_code":1,"ret_data":{}}
```

is sufficient for this native response reader. Server acceptance must mean the
new selection was persisted; otherwise the native locally updated selection
will revert on relaunch. A response echo alone cannot make persistence work.
The particular original business refusal codes are unknown.

## 3. Lobby deck shape is different from save request shape

**[RECOVERED]** `CSRPlayData::ParseDeckSetting` (`0xb67cc0`) accepts the deck
value already extracted from the response. It supports an array of rows,
each carrying **type** and **inst_id_1..inst_id_5**. Its array branch iterates
numeric row indices (`0xb67f6e..0xb67f7e`), reads type, creates the DECK_CASE
map, and reads all five slot fields:

```json
[
  {"type":1,"inst_id_1":1,"inst_id_2":3,
   "inst_id_3":0,"inst_id_4":0,"inst_id_5":0}
]
```

Exact read sites: type `0xb67d04`/`0xb67f78`; inst_id_1 `0xb68040`;
inst_id_2 `0xb68118`; inst_id_3 `0xb681f2`; inst_id_4 `0xb682cc`;
inst_id_5 `0xb683c0`. The single-record object branch separately reads the
same fields at `0xb6846a`, `0xb684da`, `0xb6854a`, `0xb685ba`, `0xb68632`.
The parsed array variant goes to `SetDeckInfo(DECK_INFO)` at `0xb68424`; the
single-record variant calls `SetDeckInfo(case,vector)` at `0xb686a2`.

**Correction to current state.ts partyDeck comment:** `/mission/Start` having
only deck_inst_id_1..4 does not justify removing **inst_id_5 from lobby deck**.
The readers are different functions. Publish all five lobby fields, using0
for empty slots. A fifth empty field does not require a fifth cloned hunter.

The lobby's ordinary user parser feeds its deck into ParseDeckSetting; the
training response also feeds **ret_data.user.deck** into this reader
(`0xf541a4..0xf541ae`, documented in revival-systems-next.md). Keep both
responses coherent with persistent selection.

## 4. Deck case and leader scope

**[RECOVERED]** SaveEntry chooses a DECK_CASE from its handler context. At
`0x8b8df8..0x8b8e0c`, context values outside the mapped2..8 range default
to **case1**. The actual table at `0x1ddf410` contains integer entries
`[2,1,1,1,1,4,5]`, so contexts2..8 map to those cases respectively. Its
base is literal slot `0x8b9120` + add-PC `0x8b8e06`; these are integer
values, not unrelocated pointers. Mission's currently published case is1 and
previous request evidence uses deck_type1. **[UNKNOWN]** Every context's named
scene and the current Build Team handler context; do not assume all modes use1.

`CSRSceneStageConfirm::SetHavingHuntersToSetDeck` (`0xe8b9ac`) passes its
received case argument to `GetDeckInfo` at `0xe8b9d2`. This confirms mission
preparation uses the DECK_CASE-specific saved state. This lane did not perform
a fresh native save capture, so the exact Build Team request's current case
must be confirmed on the wire when exercising it.

Leader selection is a separate account/card-handler operation. No leader id
field is constructed in this save requester. Do not infer that slot1 is an
instruction to mutate `leader_inst_id`; preserve leader unless its own route
is recovered or an independently proven rule requires it.

### Empty slots and order

SaveEntry knows capacity at handler+4 and selected cell vector at+0x1c. It
counts empty cells, and when every cell is empty in the ordinary save mode it
toasts the localization key `덱에 최소 1명은 있어야 합니다.` (at least one
hunter in the deck) at `0x8b90e4..0x8b90fa`. The key resides at `0x1d71482`.
It then zero-fills the output vector to capacity at `0x8b9170..0x8b9186`,
walks selected cells, and **compacts nonempty cells in their iteration order**
into output slots0..N-1. The nonempty write and index increment are at
`0x8b91d4..0x8b91e0` (and non-reference-counted path
`0x8b9214..0x8b9220`). Empty tail slots remain0. No source role test or
duplicate-serial rejection was pinned in this save method; those may be enforced
by selection UI elsewhere. Server uniqueness rejection is a local integrity
policy until its client selection enforcement is independently recovered.

## 5. Mirage is a distinct path

`CSRExploreMirageInfo::RequestRegisterDeck` (`0x92fed0`) publishes **inst_list**
(`0x930090`) to **/mirage/RegisterDeck** (`0x9301e6`). This belongs to Mirage
mode's requester and does not replace the common Build Team SaveEntry path.
Implementing only /mirage/RegisterDeck would not persist the common mission
deck. Its full callback was not audited here and is deliberately outside this
first mission implementation.

## 6. Concrete server implementation and control

1. Persist a per-account map of deck case to ordered owned instance ids.
   Migrate the current existing party once; do not regenerate ids by leader+N.
2. Parse deck_info as an array of `{type,list}`; accept the recovered string
   representation and any already-decoded equivalent from server middleware.
   Require known owned nonzero ids, no duplicates, at least one hunter,
   bounded slot count. Preserve zero positions when relevant.
3. Persist atomically before result_code1. A replay of identical deck selection
   is naturally idempotent; no native nonce was found in this requester.
4. Publish each saved case as `{type,inst_id_1..inst_id_5}` in lobby and the
   training user.deck, and keep any profile/deck-derived battlefield data
   coherent with that selection. Protect selected instances from destructive
   training across persisted **cases1,2,4,5**, per the exact native
   `IsInactiveCard` filter in training-raise-followup.md. Presets must not
   silently disappear when training mutates a different current deck.
5. Native control: select **two distinct owned characters** in Build Team,
   save, capture actual /world/SetDeck deck_info, enter one battle, confirm two
   distinct rendered participants and successful return. Relaunch and verify
   the selection remains. Merely receiving a200 or rendering two duplicate
   clones cannot establish this outcome.

No actual server or native save test was performed by this research lane.
Battle actor role restrictions, minimum frontline requirements, and original
rejection codes remain unknown; extend validation only from fresh evidence.
