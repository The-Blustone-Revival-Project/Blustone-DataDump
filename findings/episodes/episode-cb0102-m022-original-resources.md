# CB0102 M022 is embedded in original M008.jet

2026-10-08. Scoped header-only original package/name inventory, plus exact
package hashes. No adb, Ghidra, server/client/state edits, image decoding,
stat hunting, substitutions or original-file modification.

**Positive finding: the genuine shipped M022 sprite and animation namespace
is inside M008.jet.** The absent standalone M022.jet does not imply missing
M022 artwork. No M022=M008 or M022=M001 alias should be invented: serve the
unchanged original package and let its own named records register M022.

Exact final-client sources, both byte-identical:

- `recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/M008.jet`
- `analysis/extracted/assets/M008.jet`

Both are **223669 bytes**, SHA256
`04b37480c31248de3a2a23f09901961923441a9ba7524abae037a0eb805074f5`.
Their 24-byte outer-header walk has **134 records**, ends exactly at223669,
and contains **33 M022 named records**. Names decode from header+12 uint64
using the recovered native alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`.

Final-client original M022 record families:

```text
S2: M022_R01..M022_R04
    M022_H01..M022_H15
    M022_SHA M022_THN
AT: M022_AS1 M022_AS2 M022_AS3 M022_DIE
    M022_H1 M022_H2 M022_H3 M022_R1 M022_R2 M022_S
    M022_SHADOW M022_TH
```

Selected exact outer records (decimal header byte offsets and uint64 IDs):

```text
M022_R01  header217675 packed35 S2 id2517307526885
M022_DIE  header221585 packed31 AT id2517307507366
M022_H1   header221640 packed46 AT id66244934539
M022_TH   header222116 packed30 AT id66244935011
```

There is no standalone outer record named M022/M022_A/M022_B, nor a plain
M008 root, in this package. It contains named M022/M023/M024 families plus
hashed image IDs. This is a real original package grouping, not a new runtime
alias or an instruction to change the actor's original res_id.

Full final-client header-only negative coverage is explicit: **774 JET files,
33458 outer records, zero malformed/incomplete walks** for each of phone PAD
and analysis/extracted/assets. **Only M008.jet has M022-prefix names** in
either corpus. This scan does not claim an animation dependency graph is
complete or that the current native resource manager has registered the pack.

## Independent original1441 APK corroboration

Supplied source:
`analysis/VSFan/Extracted Assets (2026)/com-vshower-prd-sr-1441-39567016-ef64fd3f499bd158a709f4c380d3c06d.apk`,
ZIP entry **assets/M008.jet**. Read in memory without modifying/extracting.
It is **227791 bytes**, SHA256
`ed4b799f232024309e0dcc5200840d32900939617fe79d6ff2ab15f134eab261`,
135 complete outer records, and the same **33 M022-prefix record names/IDs**.
Older record headers end with00/00 and differ in packed sizes; do not use
their header kind bytes as a final-client S2/AT classifier.

Examples in1441:

```text
M022_R01 header217675 packed66  id2517307526885
M022_DIE header223722 packed61  id2517307507366
M022_H1  header223807 packed117 id66244934539
M022_TH  header224822 packed61  id66244935011
```

The supplied APK has61 assets/52 JET ZIP entries, includes assets/M008.jet,
and has no M022-named ZIP asset. VSFan's unpacked image tree has a M008
folder and no M022-named filenames; filename-only searches missed the
header namespace. **Prefer unchanged final-client M008.jet** for this final
client instead of mixing the older1441 serialization.

## Next native material check

Root can add the exact original M008 package through its existing local CDN
profile/resource registration and preserve original CB0102_M1 res_id M022,
then verify native requested names/rendering on the actual fight. Header
presence proves original availability; it does not establish current resident
registration, successful animation creation, actor defeat or combat win.
No source/profile change was performed here. Existing historical statements
that M022 has "no art anywhere locally" were based on standalone filenames
and are superseded by this positive original record evidence.
