# Active CDN database binding and decoded metadata

The live CPVCDN2 object uses the copied clone CDN.db. Its persisted header and
package/PVC records are still stamp1634661/count11, while the current replica
advertises139 packages at1634683. This closes physical binding and encoding;
it does not yet explain why the newer records failed to persist.

Original native evidence:

- Constructor7cb524 calls CMLocalDB.Open("CDN",DIR2,MODE3).
- Open71cedc creates the default adapter. Open71cfd0 binds it at+18/+1c,
  derives namespaceCDN at+20 and calls SetMode3.
- Default adapter forwards Open to CRMEmbeddedDB.Init; its nested object is
  CRMEncryptedDB. The physical string is adapter+c, LevelDB pointer adapter+8,
  read-only flag adapter+18, mode adapter+1c. Values use the original BTEA
  transform; keys pass unchanged to LevelDB.
- Singleton get7d3e90 reads weak pairG21de7fc. Holder7d8c44 allocates a
  distinct0x40-byte CPVCDN2 and default-delete control whose+c points to it.
  Control vptrG214cc40+8; adapter/control vptrsG21473bc+8/G2147394+8;
  nested encrypted DB vptrG21981e0+8. Host probe converts Ghidra addresses
  to ELF by subtracting10000.

Host-only InspectNativeInput --cdn-current now checks live Village, all typed
owners, default adapter, open DB pointer, namespace, mode3 and read-only0.
It accepts only exact instrumented clone paths under /data/data or
/data/user/0, with optional native trailing slash. Uses the bound path rather
than assuming its spelling. Rechecks pointers, counts, type guards, path,
namespace and mode after bounded read-only copying. No native cache getter,
write, profile change, APK rebuild or release.

Initial strict spelling probes failed closed: actual native path is Android's
/data/user/0 instrumented files/local/CDN.db/ alias. Those failures resumed and
disposed the debugger; the path difference was not a different backing store.
Final strengthened probe terminal0 on client9308/JDWP8701 copied CURRENT16,
MANIFEST432242bytes and4SST+emptyWAL,61969bytes. Private output
current-3211482878508770196. The all3 gameStates comparison uses the actual
top-level gameStates array and is exact equal to pre-binding-state.json.

Pure read-only SST/MANIFEST/WAL replay and original offline value decoder:
384livekeys, header stamp1634661/count11/size24227690;11item stamps and11PVC
stamps all1634661, zero decoding errors. No CDN/header\\stamp key. Public
metadata only is in cdn-live-decoded-metadata-20261010.json. Reproduce with
audit-cdn-cache-metadata.py and a private host copy; never open a writable
LevelDB on evidence.

DownloadHeader's literal header\\stamp therefore does not match this store's
header/stamp through the default provider. That can explain a header fetch;
the repeated139 package requests also depend on PrepareDiff and PVC/files.
Neither finding alone proves the full restart-prompt cause. Next trace current
header-context assignment, callback execution, backend write status and PVC
registration. Do not seed fabricated PVCs, delete cache, suppress verification,
or repeat an unchanged header-only restart test.

Runtime unchanged50232/25392/client9308,139groups1634683/header1634683/same+12,
safeVillage/no active battle. Goal remains active; campaign43 speed star,
E06S04, more systems and missing original data remain outstanding.
