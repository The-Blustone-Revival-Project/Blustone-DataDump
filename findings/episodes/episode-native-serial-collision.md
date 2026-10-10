# CB0102 native front-actor serial collision

Current original profile:28 groups/47 folded assets/stamp1634668, unchanged
M008.jet and original CB0102 descriptors. Same instrumented+12 APK.

Original GetSerial G99abb8 reads actor+880/+884. MakeFrontActor G9ddc3c
looks up that serial in game tree root+400; map node serial+10/+14 and actor/
control+18/+1c. GetResID G99b342 returns actor+888. Bounded --episode-materials
reader verifies scene/model/COMBAT owners, group membership and exact Hunter/
body emplace owners, then repeats identity fields before publishing results.
Group-control branch retains repeated pair/nonexpired checks as documented.

## Native collision proof

Snapshot82 in episode-006: owned party source serials4(C003),5(C004),1(C001),
2(C002). Original generated opponent source serials5(M022),6(M022),7(C005).
Looking up enemy source5 returns C004/camp0/sameSource=no. Lookup of6 and7
returns their own right-camp source actors. The map therefore resolves an enemy
front request to an owned Hunter. This is direct native identity evidence,
not a guess from invisible pixels or a missing filename.

Both M022 group-source bodies were null; C005 and owned sources had Spine
bodies. Null alone does not prove loader failure: original LoadRes always
constructs image or Spine body and returns1 normally; its old void decomp
lost return semantics. MakeFrontActor may simply never load the intended
source because the serial lookup chose another actor. Original MakeCamp puts
the same actor into group membership and the serial map; do not assume a
separate clone without checking pointers.

## Native UI experiment

Build Team deselected Nene3/inst4 and Diana9/inst5, selected the already-owned
Nene1/inst17, Captain4/inst1 and Lantern3/inst2. Native panel strength272,
no ownership/training/economy edits. Earlier proposed IDs1/2/3 were wrong:
the selected existing level1 Nene is17, proven by snapshot91/persisted roster.
This experiment avoids the observed serial5 overlap; it is not a general fix.

Screenshot90 shows original M022 penguin body rendered opposite Nene in the
native READY scene. Snapshot91 confirms M022 serial5 now resolves to itself,
camp1, and owns image renderer primary21363d4 (control2149a04, object+10).
M022 serial6 also resolves correctly, body stillnull after this loss; successful
render/loader activation of the second actor was not proved. Original C005
still maps to itself/Spine. No asset aliases, substituted sprites, stats retune,
client patch or server state mutation were used. The weaker lineup lost before
the next guarded burst; no win/clear/claim is inferred. Ended at native E01menu.

## Input guards corrected and measured

--frame uses the unique original com.vshower.rann.b.onDrawFrame callback,
with no diagnostic touch. Native menu/loss rejection supplies zero input.
An earlier tap-trigger guard reopenedStory04 on menu; that path is superseded.

Original OnRefresh compares both remain counters to0, not positivity. -1/-1
is legal during started combat. StartGame byte+3d1=1, state+13c mask14 clear,
pause0/catch198=0, exact expectedCOMBAT, no modal and a bounded live camp0
Hunter/input binding now gate bursts. No symbolic enum guess or cooldown bypass.

Native retry3 accepted four12/50ms bursts (48 paired inputs). Start timestamps
11158043/11160527/11162953/11165301: intervals2484/2426/2348ms; each burst
557..560ms. Then pause2/state4 correctly prevented input during original skill
animation (screen79). Source now polls temporary unarmed/pause without input
within its finite iteration budget; that updated waiting/resume cadence remains
pending. Loss later confirmed0/1; no continuous-injection/hit-count/win claim.

## Next server fix

Read card-instance-namespace-audit.md: versioned bijective owned-card ID
migration plus fresh fixture/allocator namespace is preferred to a pervasive
wire alias. Preserve every Hunter field and remap leader/all decks/snapshots/
receipt keys/allocator gaps; leave item instances/pvid/references untouched.
Validate raw ownership graph before migration, retain private snapshot, prove
non-identity state equal, persist atomically, then normal native cache reload.
Policy base is local, not recovered production numbering. No migration has
been applied. Existing server/IDs/roster/progression remain authoritative.
