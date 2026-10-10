# Cold recovery of existing Nougat32 — 2026-10-05

READ-ONLY investigation. No VM/media mutation, delete, restore, registration change, disk-chain edit, app install/clear, or physical-device operation was performed in this phase.

## Authoritative current state

HD-Player8352 is gone. `list runningvms` is empty. Existing VM UUID87bb8c18-a755-46c6-ba82-2a0deb17bac3 is inaccessible. Its config declares aborted=true; baseData.vhdx is attached while the media registry declares a differencing child. Exact access error:

> Hard disk Data.vhdx with UUIDa9d1a5d3-cd0c-4169-9284-69b19f57b517 cannot be directly attached to Nougat32 because it has1differencing child harddisks.

This is now a cold configuration/registry inconsistency, not a running VM needing force-stop. Earlier force-stop approval is obsolete.

## Complete child block-map proof

Read original child and preserved copy with File.ReadAllBytes. Parse packed VDIv1 header against upstream VDICore.h, not heuristic file size.

- Signature0xBEDA107F; version0x00010001; header400bytes; type4=differencing.
- ChildUUID6108aceb-02a1-4793-9b9e-1c0c07947977.
- ParentUUIDa9d1a5d3-cd0c-4169-9284-69b19f57b517.
- Virtualdisk137,438,953,472bytes; blocksize1,048,576bytes; blockextra0.
- Mapoffset1,048,576; dataoffset2,097,152; filelength2,097,152.
- Total131,072blockmap entries inspected individually.
- Headerallocated0; mapallocated0; mapFREE131,072; explicitZERO0.

FREE entries mean no child override: reads fall through to parent. ExplicitZERO entries would override parent sectors with zeroes, and must be counted separately; there are none. File length ends exactly at dataoffset, so no allocated block payload exists. This child contains no guest writes or zero-block overrides.

Original child and preserved copy SHA256 are identical:
`42F9D209AEFF8F83B347ED5CC1B8ED2B0E68C4C6B81A13FD5D770B901B56B0E0`.

Source layout: VDIPREHEADER72bytes; header fields offBlocks atfile340, offData344, cbDisk368, cbBlock376, cbBlockExtra380, cBlocks384, cBlocksAllocated388, uuidCreate392, uuidLinkage424. Entiremap checked, not a sample.

Primary specification/source:
https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Storage/VDICore.h
https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Storage/VDI.cpp

## Existing preservation

Local backup `recovered-assets/emulator-host-recovery-2026-10-05/` retains Data.vhdx and child plus pre-termination current/previous configs. Prior shared-read original/copy Data.vhdx SHA256 matched. That copy was taken while the VM was deadlocked and is preservation, not a verified consistent guest checkpoint. Current aborted config should be backed up separately before any approved metadata intervention, never overwrite prior copy.

## Supported options and their limit

Local CLI documents `closemedium disk <uuid|filename>` as removal from media registry; omission of --delete retains the image file. It requires media not attached to any VM. `unregistervm UUID` without eitherdeleteflag removes VM registration without deleting files.

Live COM exposes only fastboot and Root in HardDisks after inaccessible load. Data/child are not exposed as registered medium objects. Their offending relationship lives in the VM .bstk's MediaRegistry XML; its SATAattachment still points atData. Consequently closemedium is not demonstrated to repair the inaccessible config: opening a file could merely create a new medium record, and reloading the unchangedconfig would reintroduce the child declaration.

Primary MachineImpl.cpp confirms inaccessible machines can only be unregistered; its path uses CleanupMode_UnregisterOnly. Ordinary attach/detach/SaveSettings requires successful initialization. Unregister+reregister unchangedconfig therefore is not itself a repair.

https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Main/src-server/MachineImpl.cpp
https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Main/src-server/MediumImpl.cpp

## Concrete minimal repair proposal — NOT EXECUTED

No fully supported CLI-only repair is established for this inaccessible config. The smallest evidence-backed repair would be metadata only:

1. Preserve fresh aborted .bstk/global VM registry and verify allfiles remain; retain existing backups.
2. Supported unregistervm exactUUID, withoutdeleteflags.
3. While this VM is unregistered and noPlayer isrunning, remove ONLY the unusedchild HardDisk registryelement from its .bstk. Keep baseData attachment, diskfiles, UUIDs, aborted marker, otherhardware/accountstate unchanged. This is a manualconfig correction, not a supportedCLIoperation, and requires parentauthorization because currentphase prohibits mutations. Never editVDI/VHDX headers/maps or deletechildfile.
4. Supported registervm same .bstk; verify accessible VM and identical baseData attachment/settings before launchingexistingNougat32.
5. Launch sameinstance, verify explicitADBserial; inspect currentAndroiduser, then supported amswitch-user0 only if necessary. Do not clear/install/removeprofiles. Verify liveaccountownership/counts against preservedserverstate privately.

Because child contains zerooverrides, removing its registry declaration would not discard child guestdata. This proof does not make Android's unclean shutdown clean; filesystem/application integrity remains to be verified after boot. No restore/backfill or accountgrant is proposed.

Alternative manual metadata correction: retain the full parent/child MediaRegistry and change only the SATA port1 attachment UUID from the parent to the already declared empty child. This aligns the attachment with the leaf, keeps all files and the complete chain, and permits subsequent writes in the existing differencing file. It is not a snapshot restore and does not establish a successful snapshot. It is also an offline manual config change, not a demonstrated supported CLI repair. The parent should choose one correction explicitly; do not combine registry removal with child attachment.

## Approved repair milestone — 2026-10-05 12:35 local

Human approved the prepared removal of only the empty child registry element. Revalidated no HD-Player process; current config exactly matched preserved SHA256 E3B6149D7190AC68950035B3D1877D3E45A0C47403A7C3B6D8CBE0047CBF4174. Prepared config SHA25622DF09EBFF46D61C73F1E318E1E3866FAC5547A9C5342FFCA2DC3DEB20FE289D differed only by that element. Supported unregistervm without delete, copied the exact approved config, then supported registervm succeeded. Same UUID is accessible again, state aborted, original Data.vhdx and parent UUID still attached. Every disk and backup retained.

Normal hidden start of the existing Nougat32 created HD-Player PID30388 at12:35:34. It did not power on the VM. Fresh Player.log at12:35:43 records AddRedirect E_INVALIDARG(-2147024809), configureMachine VmmgrVbox.cpp424, then VmmgrMachineConfigurationFailed. This supersedes an earlier tentative host-initialization-stall diagnosis. No guest boot, ADB listener, or account validation occurred.

The existing NAT mapping is tcp_5555_5555,tcp,,5555,,5555; BlueStacks config asks adb port5555. Primary NATEngineImpl.cpp confirms AddRedirect returns E_INVALIDARG for duplicate rule name or host-port/IP mapping. This supports, but does not independently prove, a duplicate redirect as the new startup blocker.

A narrow supported follow-up would close the failed-start player normally, preserve current config, remove only this NAT redirect via modifyvm --nat-pf1 delete=tcp_5555_5555, then retry normal existing-instance start so BlueStacks config recreates its mapping. This was not included in the prepared disk-registry repair approval and was not executed at this milestone. No app/user/account modification was made.

https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Main/src-server/NATEngineImpl.cpp

NAT follow-up status: parent authorized only supported reversible removal of the stale rule after normal close of the failed-start player, with no force if close failed. Preserved latest repaired config and global COM registry under recovered-assets/emulator-host-recovery-2026-10-05/pre-nat-20261005/ with SHA256 manifest. runningvms remains empty. Process30388.CloseMainWindow() returnedFalse and player remains present. Accordingly no force, NAT mutation, second start, guest switch, or account action was performed. A permitted normal UI-close path is required before this follow-up continues.

## Recovery complete — existing Owner0 baseline verified

Parent authorized termination of only the failed-start host wrapper after fresh proof that it had not powered the guest on. Rechecked PID30388 name HD-Player, PID-specific launch log for --instance Nougat32, VM aborted, runningvms empty, and no5555listener. Terminated only that wrapper; no running guest was force-stopped.

First NAT delete syntax delete=tcp_5555_5555 was rejected as invalid with no mutation. Correct locally documented syntax `modifyvm Nougat32 --nat-pf1 delete tcp_5555_5555` succeeded. All disk attachments were unchanged. Normal hidden start created HD-Player25528, VM running, and BlueStacks recreated the same tcp5555 redirect. Startup succeeding after this sole supported change confirms the previous stale duplicate redirect was the immediate configuration blocker.

Explicit adb serial127.0.0.1:5555 connected and reports device. sys.boot_completed=1; am get-current-user=0. Owner0 is running; user10 remains retained and not running. No Android user switch was performed. Existing instrumented package is installed under /data/app/...-1/base.apk, version2.8.0.1/code28010. No APK install/clear/rebuild was performed by this recovery lane.

Ordinary Owner0 launch resumed instrumented activity PID4133/u0. Accepted one standard54MB data-download confirmation, waited for completion, and verified village by eye. The same Search guide overlay remains; Airport31/150, AP50/50, BP10/10. This is village-with-guide, not an unrestricted village.

By-eye baseline: `analysis/testing/recovery-20261005-owner0-ready.png`.
Earlier screenshots record download prompt/progress; filenames ending village/baseline before ready must not be mistaken for village proof.

Private persisted account1000001 has fresh lastLoginAt1791193327 and still10 hunters (2starter+8recruited), party[2,4,1,5,0], Sylvestertrace2, AIRSHIP_TICKET0, gold10660, loginjournal day20731/eligible1/claimed[], and activebattle null. Parent independently checked14campaignclears and no visible game grants. No guide-progress edit, item/hunter grant, paid action, battle, user10switch, +9APK install, physical-phone action, delete, or restore occurred.

Held PID4133 at the verified safe village Search guide and returned exclusive VM/adb ownership to parent for the next authorized work.
