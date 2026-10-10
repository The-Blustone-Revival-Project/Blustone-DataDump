# Persistent no-attachment mailbox, 2026-10-05

Mail transport is /message, not /mail. Fresh original decomp/relocated literals
confirm successful GetReceivedList/GetSentList ret_data{unread_count,list}.
Read/Archive requests serialize a SINGLE decimal ID under target_list; response
target_list is a numeric ID ARRAY. Common callbacks only apply success when
GetResultCode1. Full row: id/sender_pvid/sender_nickname/receiver_pvid/
receiver_nickname/from_admin/app_code/content/attachment/is_archived/is_read/
is_attachment_taken/created_datetime. attachment:null is explicitly guarded.
content is a plain string copied into CSRMail.DATA and rendered in USER_TALK;
no nested title/body JSON-text schema is required. content_result belongs to
attachment settlement, not an ordinary list row. created_datetime is uint32;
original epoch/unit remains unknown. Sources: ghidra-mail-contract*.txt,
ghidra-mail-content-render*.txt, ghidra-mail-cell-init*.txt and agent reports.

New account-owned MailState persists monotone local IDs/read/archive flags and
one notice marker. Only an explicit matching accepted normal campaign first
clear with a real earned capsule drop can create the LOCAL no-attachment
expedition notice. No bootstrap, replay, defeat or old-stage backfill. Message
truthfully says its rewards were already applied; it contains no new rewards.
Local timestamp Unix seconds and offset/ID-bound pagination are policy fixtures,
not original contract claims. Native date formatting remains unverified.

Received lists exclude archived rows; unread total excludes read/archived rows.
Sent list stays empty. Read/Archive validate owned ID, acknowledge idempotently
and persist only on flag change. Unknown IDs and unsupported attachment/send/
removal operations refuse rather than generic success. No network message or
human-recipient send was performed. Mail operations preserve wallets, energy,
hunters, items, party, stars and tutorials. Empty state migrates without creating
legacy notices. Clock/allocator/capacity problems skip notice creation rather
than reject or corrupt an earned battle settlement.

Full npm test/build pass: actual campaign handlers create one notice after a
defeat followed by victory; tests cover wrappers/row fields, flags and restart,
duplicate Read/Archive, ownership, invalid targets/pages and no grants/outbound
actions. Native UI remains pending; the emulator is untouched while forced-stop
approval is unresolved. No live messages or retroactive data changes occurred.
Promoted wrapper20456 with unchanged persisted state SHA and same resource
1634663/46assets/11packages; health endpoint true. No client patch/rebuild/release.

## Received deletion continuation, 2026-10-05

RemoveReceived now accepts the native trailing-comma decimal batch and replies
with numeric IDs/unread_count. Entire batch must belong to this account's active
or known-deleted mailbox. Durable deletion receipts support restart/retry;
unknown IDs refuse atomically. This is local policy, not recovered original
server restrictions. Deletion never claims attachments or changes rewards.
Sent deletion and bulk-clear remain unsupported. Tests cover archived/unread
batch deletion, mixed unknown refusal, owner isolation, migration and retry.
Full suite/build and focused final mail tests passed; agent review found no bug.
Native UI pending. No live deletion, APK rebuild or release. Replica33512 healthy;
persisted live state hash unchanged through restart.
