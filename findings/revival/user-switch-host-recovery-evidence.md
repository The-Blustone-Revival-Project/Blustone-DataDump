# Host-only evidence after Android foreground-user switch

2026-10-05, read-only host log tail and directory/file metadata. No adb, VM control commands, kills, disk contents, Android userdata, Ghidra or source changes. Parent owns recovery and its running live-snapshot CLI.

## Concrete host failure

Public host log C:/ProgramData/BlueStacks_nxt/Logs/Player.log records:

```text
06:35:52.180+0300 vmsgPciWrite: Unable to allocate cid for service gcal
06:35:52.180+0300 FATAL DEBUG BREAK ... Vmsg.cpp:138 vmsgPciWrite()
06:35:52.935+0300 The VM is about to shut down due to an unhandled exception!
06:35:52.935+0300 Sent an urgent shutdown event to the VM, result=success
06:35:52.935+0300 Waiting the VM to shut down
07:10:03.703+0300 OnStateChanged: LiveSnapshotting
```

The reported gcal transport failure is stronger evidence than treating this as merely an expected adb disconnection on an Android user switch. It does not prove the exact guest or host deadlock location. Later log lines remain tagged Ready before LiveSnapshotting; an urgent-shutdown success message means the event was sent, not that the VM stopped.

## Snapshot is not verified

At07:16:33 local (04:16:33UTC), host metadata shows:

```text
Snapshots/{6108aceb-02a1-4793-9b9e-1c0c07947977}.vdi
  length2097152, lastwrite07:10:03
Snapshots/2026-10-05T04-10-03-714763300Z.sav
  length0, lastwrite07:10:03
Player.log length4280748, lastwrite07:10:03
```

Two bounded metadata observations showed no change. BstkCore.log is zero bytes with stale last-write Oct4; rotations are historical. No current snapshot success/error or unsupported SaveState evidence appears in these logs. Zero-byte memory state and a newly created differencing disk do not constitute a recoverable complete snapshot. Approximately6m30s of unchanged metadata/log state supports reporting a stalled operation, while not proving it can never finish.

## Safest next action

Keep the parent-owned live-snapshot operation intact until its actual completion/error is obtained or a documented supported cancellation is established. Do not run another snapshot, restore, SaveState or shutdown concurrently merely because the CLI reports0%. The already queued ACPI shutdown should remain conditional on successful snapshot completion as parent planned. If the parent operation reports failure, preserve its exact error and these metadata observations before deciding the next VM-control step. This lane cannot prove a safe cancellation or unsupported SaveState from the available evidence and performed no control command.

Original user0 account and durable host game state preservation are parent-reported; this lane deliberately did not inspect their contents. No active battle is parent-reported. A stalled snapshot alone does not justify disk rollback or app-data clearing.
