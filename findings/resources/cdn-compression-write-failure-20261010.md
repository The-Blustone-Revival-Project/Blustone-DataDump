# CDN write failure: unsupported compressed bootstrap table

The live CDN LevelDB has a sticky Corruption status: `corrupted compressed
block contents`. Original ReadBlock G1b84948 rejects compression type1
(Snappy) unconditionally. The copied active table000005.ldb has one Snappy
data block and matches the packaged bootstrap seed exactly (1503bytes,
SHA256e2ae5a5d12dc208a0991e2435fcf8ae117cab4a64e02e45174220300e2ce100b).
Other active tables10/13/16 have uncompressed data/index/meta blocks. The
offline decoder successfully reads the Snappy bytes: the error reflects
unsupported compression, not proof that those compressed bytes are malformed.

The stronger live observer binds DBImpl vptrELF21a6ef4, sticky Status pointer
at+f0 and current header context. MakeRoomForWrite1b733b0 returns the stored
error before admitting writes; RecordBackgroundError1b7134c retains it.
Status constructor1b83336 stores uint32 length/code byte/message at+0/+4/+5.
Reader bounds message1024bytes and rechecks it; raw message stays private.
Only code/category/presence and public header integers appear in stdout.

Current in-memory header stamp1634683/cnt139/size212934524/item_count139,
while durable cache stamp1634661/cnt11/size24227690. Latest fully guarded
probe terminal0 on9308/8701, safeVillage. Native context wrapper+34/+38,
controlvptrELF213c8d8/rawstorage+c/allocation+10, context=allocation+10;
header JSONcontext+18. Rootmap<=8, itemcount<=256, named integerprojection
only; reread all inspected bytes and all owner links. Synthetic tests cover
object/array counts, secret isolation, invalid types/counts/numbers and races,
alongside existing marker tree/privacy tests. All3 saved gameStates exactsame
as pre-binding-state.json. No game inputs, cache mutation or native getters.

Queued PVC writer now closed: UnpackAsynTask7d121c registers primary vptr
G214ca94 at7d1862; invoke+18 odd7d6ecd -> Thumb7d6ecc. It writes PVC/name,
deletes pkg when traversing packs, and writes RES/filename entries. Neither
header callback nor this wrapper proves backend durability. The full original
symbol bodies for seven JSON/default/encrypted/embedded write functions match
the packaged+12 library, not just their prefixes. Source review found no
unconditional CDN reseeding. Active E_NEW package has one E_NEW.jet record;
served inventory contains no CDN.db overwrite. Recent bounded logcat tail
contains no relevant CDN errors; it is not a startup trace or absence proof.

Host tools now default to compression none for selective UI aliases/battle
delta, and merge-ui-leveldb-keys uses none. Explicit Snappy remains a research
option, but must not be deployed to native28010. These defaults prevent new
unsupported tables; they do not migrate existing compressed files.

tools/rebuild-cdn-cache-uncompressed.py reads source using pure table/WAL
replay, never opens source in LevelDB, creates a separate new private host
database with compressionNone, then compares every live raw key/value and
all source file hashes. Candidate uncompressed-candidate-002 preserves384
entries exactly, has one active table5 and seven checked uncompressed blocks.
Proof JSON is outside the database and written exclusively; destination creation refuses races/existing databases. The replay does not verify CRCs or preserve physical sequence/history. No candidate install/native claim yet.
Original clone cache remains intact; the candidate retains old11-package
metadata deliberately, so future native downloads must publish139 records.

Next: ship a narrowly gated one-time instrumented CDN migration with full
backup/preservation, replace the bundled compressed bootstrap seed, publish
the mandatory new APK release, then validate a normal bootstrap plus another
same-profile restart. Require no stored write error/current persisted header
and PVC records/expected package suppression, and unchanged game progress.
Do not clear the app, edit original/phone data, fabricate PVCs or suppress
cache integrity checks. The header-backslash mismatch may still fetch a
manifest; its existence alone does not require full package downloads.

Runtime50232/25392/client9308/139groups1634683/header1634683/+12 unchanged.
Repair is prepared, not applied; no APK rebuilt/release owed this unit. Goal
active: campaign43 speed star/Deep30 reward, E06S04 and other systems pending.
