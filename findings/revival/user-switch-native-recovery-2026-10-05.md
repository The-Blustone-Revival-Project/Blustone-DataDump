# Existing Nougat32 recovery audit — 2026-10-05

Recovery remains incomplete. No app reinstall, clear, profile removal, disk restore, snapshot delete, client patch, or physical-phone operation was performed.

## Verified target and failure

Existing VM `Nougat32`, UUID `87bb8c18-a755-46c6-ba82-2a0deb17bac3`, host HD-Player PID8352. BstkVMMgr/COM version6.1.36. `list runningvms` identifies this VM; all adb calls explicitly target `127.0.0.1:5555`.

Public Player.log records user-switch-adjacent gcal allocation fatal at06:35:52 and urgent shutdown request, without actual shutdown. Instance-specific `Engine/Nougat32/Logs/BstkCore.log` is92KB (not the stale zero-byte public log), last written07:10:09 before cancellation. It records live snapshot start, RUNNING→RUNNING_LS, and repeated NEM GVA translation/MMIO parsing failures.

## Supported cancellation

Parent sent one Ctrl+C to its session74279. CLI exited1 with no output; conditional ACPI did not execute. VM remained LiveSnapshotting, so CLI exit did not prove cancellation.

COM `VirtualBox.VirtualBox` resolves to the BlueStacks6.1.36 service and correct VM. PowerShell table formatting initially hid ProgressOperations output; JSON inspection recovered exact progress:

- ID `bb579d3f-16d5-4f08-a3cd-8a1934e94bfc`
- Description `Taking a snapshot of the virtual machine`
- Cancelable1, Completed0, Canceled0, Percent2

Calling this exact object's supported `Cancel()` returned successfully and changed Canceled to1. Core log added `SSM: Cancelled pending operation`. Completed remained0, VM remainedLiveSnapshotting. This is cancellation acceptance, not completed unwind.

Primary upstream source confirms online snapshot progress is cancelable and its callback uses CancelSaveStateWithReason; VBoxManage SIGINT invokes IProgress.Cancel only for cancelable operations:

- https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Main/src-server/SnapshotImpl.cpp
- https://github.com/VirtualBox/virtualbox/blob/main/src/VBox/Frontends/VBoxManage/VBoxManage.cpp

These are upstream source, not proof every BlueStacks fork detail is identical. Live COM cancellation and SSM log establish the actual local behavior.

## Orderly shutdown probe

After the old CLI ended, supported `controlvm Nougat32 acpipowerbutton` returned0. After15seconds, VM remainedLiveSnapshotting, no shutdown log, adbget-state returned deviceoffline. This does not justify claiming shutdown.

## Disk-chain preservation

Snapshot list still reports no snapshots. `.sav` remains0bytes; live diffVDI2MB. Runtime showvminfo attaches diff `6108aceb-02a1-4793-9b9e-1c0c07947977`, parent `a9d1a5d3-cd0c-4169-9284-69b19f57b517`; persistent .bstk still attaches originalData.vhdx. This is an incomplete transaction and must not be manually rewritten.

Read-only FileShare.ReadWrite copying preserved local originals under:
`recovered-assets/emulator-host-recovery-2026-10-05/`

- Data.vhdx29,746,003,968bytes
- incomplete diffVDI2,097,152bytes
- Nougat32.bstk11,356bytes
- Nougat32.bstk-prev10,670bytes

This is precautionary host preservation from a deadlocked running VM, not a verified consistent guest checkpoint. Source files were not modified. Ordinary Get-FileHash could not open the lockedsource; shared-read SHA256 validation completed: originalData.vhdx and copy match exactly (manifest.json). The initial ordinary hash command failed to open source and therefore its mismatch error was an unavailable-source result, not evidence of a corrupted copy. No restore is proposed.

## Remaining decision

Native save cancellation has reached SSM but not unwound; orderly guest shutdown has not worked. A supported cold powerdown or ultimately forced HD-Player termination may be required, with risk to unflushed Android state. Before any forced stop, retain the copied chain/config and report the exact authorization and result. Owner0 and adb are not yet recovered.

Additional orderly guest shutdown API probe: controlvm Nougat32 shutdown returned1 / Could not open guest session: VERR_HGCM_SERVICE_NOT_FOUND (VBOX_E_IPRT_ERROR0x80bb0005). Guest-control service is unavailable, consistent with RunLevel1. No force flag was used.

