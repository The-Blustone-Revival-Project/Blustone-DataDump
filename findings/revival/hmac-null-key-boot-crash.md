# Boot HMAC crash: null key input and protected-key locking window

2026-10-04. Offline original-library instruction inspection plus bounded crash
metadata; no secret/key bytes read or printed. No algorithm, hook or runtime edits.

## Exact fault interpretation

Crashloglogcat-timingcontrol-boot-crash.txt reports ELF PC1b25a2c,
LR1abeff0, fault0, r0=nonnull destination, r1=0, r2=48, r3=130(hex).
These Crypto++ functions are **ARM**, unlike most game-code Thumb functions.
Correct Ghidra PC1b35a2c decodes:

```asm
1b35a24 mov r1,r8
1b35a28 mov r2,r6
1b35a2c bl __aeabi_memcpy
```

HMAC_Base::UncheckedSetKey1b3590c saved its original key pointer into r8
at1b35924 and original key length into r6 at1b35920. The destination r0 comes
from StandardReallocate at1b359d0 and is nonnull. Thus **the failing memcpy
source is a null key pointer with nonzero length48**.

This is not a null hash vptr diagnosis: virtual hash/block/digest-size calls
have already succeeded at1b35968,1b35990 and1b359b0. The direct-copy arm was
selected because key length<=hash block size. The allocation size hex130
is consistent with128*2+48 SHA384 pad/digest storage, but the decisive evidence
is the exact key-register forwarding, not a inferred size label.

SimpleKeyingInterface::SetKey1aca900 preserves the passed key/len, validates
length, then dispatches virtual UncheckedSetKey at1aca930..93c. It does not
make a null pointer safe just because48 is an accepted key length.

## Native HTTP HMAC caller and key owner

CPVHTTPSharedSecret::ComputeMAC7f2850 creates a fresh stack HMAC<SHA384> at
7f2870 and uses CRMDefensedData2 at **sharedSecret+8**:

```text
7f287a Unlock(sharedSecret+8)
7f2880 GetData(sharedSecret+8) -> r1 key pointer
7f2888 reads length at sharedSecret+10 (owner+8)
7f2896 SimpleKeyingInterface.SetKey(keyptr,length)
7f289c Lock(sharedSecret+8)
```

The shared secret ctor7f6948 initializes this protected key object with48
bytes at7f6972..74. ExchangeKeysCB writes its computed48-byte data through
PutData at7f22be, clears its temporary buffer7f22c8 and locks the protected
object7f22ce before calling ComputeMAC7f22e4. Vector overload7f2cc0 forwards
to the same ComputeMAC7f2cd6. No original key material is needed for this trace.

## A concrete locking-window mechanism, not a proven interleaving

CRMDefensedData2 methods each use their own internal mutex:

- Unlock10c5690 locks at10c56a8, decrypts protected data in place and sets
  locked flag **owner+4=0** at10c56e6, then releases mutex10c56ea.
- GetData10c5470 locks at10c5476. If locked flag+4==1, it sets return pointer
  **null** at10c5482, logs the built-in warning, releases mutex10c5496 and
  returns. If unlocked it returns owner+10 at10c5492.
- Lock10c5608 locks at10c5620, encrypts data in place and sets flag+4=1
  at10c5678, then releases mutex10c5632.

The warning's verified literal is:
`[WRN] [DF] DefensedData is locked, unlock first. 0x%llx`
It describes a pointer/location, not a request to expose key bytes.

ComputeMAC itself does not hold a common outer mutex across Unlock -> GetData
-> SetKey -> Lock. Therefore a plausible interleaving is:

```text
threadA Unlock returns(flag0)
threadB uses the same key then Lock returns(flag1)
threadA GetData returnsnull; SetKey still receiveslength48
```

It exactly explains the observed null source. Even another Lock after a
successful GetData could re-encrypt its returned buffer before copying it.
The protected methods are individually synchronized; their combined use is
not automatically atomic.

EncryptMessage7f2f20 and DecryptMessage7f339c also use the same protected
key+8 through Unlock/GetData/Lock. They have their own surrounding shared-secret
mutex calls7f2f68/7f33e4, but ComputeMAC's inspected function does not acquire
that outer guard. Caller-level serialization outside these functions has not
been fully established. This is a **strong race candidate**, not a captured
proof that threadB performed the Lock in this particular boot.

## What the successful traffic establishes

Native GetCard and other secure traffic earlier in the same boot establish
that protocol/keys worked before this failure. They do not prove the protected
key object's unlocked state at the failing call. Conversely one null-key crash
does not establish persistent server key corruption, a bad shared-secret
algorithm, or a causal connection to new prices/is_main/reference definitions.
Those content changes cannot be blamed without an actual path/timing control.

A single controlled boot with the already-persisted app/account/session state
is justified to measure recurrence and return to the authorized gameplay test.
Do not regrant/recruit, wipe/reinstall, rotate preserved account credentials,
change AES/HMAC/ECDH, or mask memcpy/throw. If a response-spacing diagnostic is
used, label it a timing control, not a crypto fix. A successful control narrows
repeatability but does not erase the native locking-window finding.

If it repeats, collect only metadata: exact key-owner pointer/locked flag,
length, request/response ordering, built-in warning, PC/registers and threads.
Do not dump key bytes, decrypted account bodies or create new hooks. Distinguish
an observed null-key condition from the still-unobserved causal interleaving.
