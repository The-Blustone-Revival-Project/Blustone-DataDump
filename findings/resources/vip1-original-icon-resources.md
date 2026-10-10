# VIP1 receipt icon: original ICON_VE is in UI_SHOP.jet

2026-10-08. Read-only original material search following the native calendar
receipt that displays VIP1 quantity20 with a blank thumbnail. No adb, Ghidra,
Docker, physical-phone operations, source/client/state changes, generated art,
aliases or substitutions were performed. Only this research note was written.

**The exact final-client original sprite `ICON_VE` and its image are both
present in unchanged `UI_SHOP.jet`.** There is no additional package needed
to close this sprite's declared offline image dependency. This does not prove
that the package or these IDs are registered in the current native session.

## Original source and exact record identities

Final2.8 source:
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets/UI_SHOP.jet`.
Corroborating byte-identical copy: `analysis/extracted/assets/UI_SHOP.jet`.
Both are **1236254 bytes**, SHA256:
`89f3cc6750f01b3ca149ceece7c0798d963569bd8b6bb504c0c6be2b61162a09`.

The pack's24-byte outer-header walk has160 records and closes exactly at
1236254. Packed length is the uint32 at header+8; identity is the uint64 at
header+12. Named identity decoding uses the recovered native base38 alphabet
`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`. Kind is at header+22.

```text
ICON_VE  kindS2  header1233343  payload1233367  packed36
         outer identity55199036868
         inflated66bytes
         image reference at inflated+46 =3558866890 /0xd41fffca

image    kindI2  header850504   payload850528   packed313
         outer identity3558866890 /0xd41fffca
         inflated2155bytes
```

The image ID resolves to the actual I2 outer record in the same pack.
Both compressed bodies inflate successfully with zlib. The I2 inflated
SHA256 is `a9933c4b168cdb78a5fc353f1a0cb8a04f9f677ddbf02e42517dee0c026b17a8`.
Its entire unchanged outer record SHA256 is
`b128b42c4c8e35381a2caf98fc667cf38ce60cc3482c469acfe560b0c4d5d612`.

Existing `tools/jet-viewer/jet_decoder.py:decode_i2_texture` decodes the I2
successfully in memory as **14×17 RGBA**. It has131 nonzero-alpha pixels,
alpha range0..255 and alpha bounding box(0,0,14,17). It is not an entirely
transparent placeholder. No decoded image was saved or visually substituted.
The decoder's in-memory PNG hash is
`bbc28f0f70e052ae7f8dff538f69e9a92ed6dde130daa679a67d127e2e19347a`;
the unchanged original pack remains the source material.

## Coverage and binding limits

The header inventory covered **all774 JET files /33458 outer records** under
the final-client phone PAD assets directory, with **zero malformed or
incomplete walks**. Only `UI_SHOP.jet` contains the exact `ICON_VE` outer name.
No decoded outer record in that corpus has exact name `VIP1`, `IMT_VIP1` or
`IT_VIP1`. These exact negative checks are not a claim that every conceivable
IT-prefixed record is absent, nor that native UI bindings are package filenames.

`analysis/research/login-bonus-veteran-receipt.md` establishes the original
calendar's captured20 atGf49624 and the exact VIP1 thumbnail identity through
CSRItemThumb.GetItemThumbListGafa584. Root's separate native binding recovery
selects ICON_VE for this display. This material scan supplies the actual
original ICON_VE sprite/image graph; it does not independently re-derive that
VIP1→ICON_VE selection or imply that the original receipt uses an invented
IT_VIP1 alias. The material graph is directly **ICON_VE S2→hashed I2**, with
no AT animation or IT-prefixed intermediate declared by that S2.

The next runtime seam is unchanged original UI_SHOP delivery/registration and
successful lookup/attachment of these exact source IDs during native VIP1
receipt rendering. Offline availability, HTTP delivery and folded-package
selection each remain distinct from actual native residency and rendered pixels.
No reward quantity, inventory item, VIP EXP, wallet or resource profile was
changed in this research lane.
