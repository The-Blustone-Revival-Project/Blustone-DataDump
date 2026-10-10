# Native mail sender0 falls back to recipient

2026-10-07. Bounded original ELF, ghidra-mail-cell-init.txt and current mail.ts.
No Ghidra, device, source/account edits, messages, grants or new identities.
Code addresses use Ghidra coordinates.

Root verified Received list, actual Read request/persistence and full text/date.
Header/profile request used Captain1000001 despite DTO sender_pvid0 and
sender_nickname Local replica, receiver1000001, from_admin1. Original native
parser explains this without a mailbox direction/type hypothesis.

## Exact earlier selector

**CPVMsg.ParseMsgInfo G7ffd2c** allocates a shared-wrapper whose payload begins
atwrapper+0xc. It parses sender_pvid, stores its u64 at**wrapper+20**
(STRD7ffe40), and converts sender_nickname to STRING at7ffe58, storing that
string atwrapper+28 (7ffe84..8c).

At **7ffe90** LDRD loads that selected pvid; **7ffe94** ORRs its two words;
**7ffe96** branches to7fff30 when nonzero. When the sender iszero, it instead
indexes **receiver_pvid** (LDR7ffe98/ADD7ffe9a) and **overwrites the same pvid
slot at7ffee4**, then converts receiver_nickname at7ffefc and overwrites the
same string slot at7fff24..2c.

Only **after this fallback** does it parse **from_admin**
(LDR7fff30/ADD7fff32/call7fff36). Thus from_admin1 cannot prevent sender0
from selecting the recipient. This is a zero-pvid fallback, not a proved
received/sent TYPE override or a wrong CellMailPost checkbox argument.

## Native model and displayed name

**CSRMail.DATA ctor Gb4b4f8** projects the selected PV message information into
its DATA fields; it copies the selected nickname from PV payload+18 into
DATA+38 atb4b5ca..da. **CSRCellMailPost.Init G89e1c0** sets its name textbox
directly from **DATA+38** (retained decomp line211); its content text uses+44.
No sender/receiver/from_admin branch appears in the cell's name assignment.
The source DTO's recipient remains the real mailbox owner; swapping it would
falsify ownership rather than recover native protocol.

Current mail.ts publishes exactly the triggering sender0 fixture. A dedicated
display sender would need an explicitly local, nonzero identity and a coherent
relation/profile response; no original administrative sender ID was recovered.
This lane creates neither a profile nor account, and does not recommend
reusing an unrelated person's pvid. Keeping sender0 knowingly retains native
recipient fallback. Missing portrait is a separate profile/reference consumer
question and is not fixed merely by changing sender_nickname.

Parent's exact decompile target if fuller ownership/type behavior is needed:
**ParseMsgInfo7ffd2c**, particularly7ffe3e..7fff36, then DATA ctorb4b4f8.
Existing CellMailPost89e1c0 is already sufficient for the displayed-name sink.
No user-secret content was accessed; only public original binary/static DTOs.
