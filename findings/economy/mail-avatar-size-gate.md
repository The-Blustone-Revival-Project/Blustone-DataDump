# Mail profile image: exact100x100 callback requirement

2026-10-07. Parent image-loader/URL decomp and bounded original ELF only.
No Ghidra, device, source/asset edits or image conversion. Root observed valid
brief/detail and PNGGET200 with level/like controls rendered, while portrait
pixels remained blank; supplied source image is169x166.

## Decisive completion guard

LoadImageFromURL's result callback is identified by maker literal
DAT **G10ab6f4 + G10ab5fc**, resolving **ELFVT2187928**,
RTTI CSRUserProfileDraw.LoadImageFromURL$_3, invoke **G10ac1ec**.
Original Thumb checks the returned image node pointer, then:

```text
10ac216 V LDR s2,[imageNode,+78]
10ac21a V CMP s2,100.0
10ac222 BNE cleanup10ac314
10ac224 V LDR s2,[imageNode,+7c]
10ac228 V CMP s2,100.0
10ac230 BNE cleanup10ac314
```

The constant load10ac212 resolves **G10ac404**, original bytes0000c842,
exact float32 **100.0**. Only the passing branch eventually calls
**CSRUserProfileDraw.OnSync G10aad2c at10ac2c6**. The unequal-size branch
releases references and exits; no original image-size coercion is done there.

This proves a **loaded image-node100x100 requirement**, not a JPEG-only theory.
The169x166 source does not meet that requirement unless some prior loader
normalization exists; none was proved in this lane. Parent's next precise
corroboration is **Thumb10ac1ec**, then LoadFromRawImage's size propagation if
needed. Preparing a derived100x100 local avatar can be justified by this guard,
but this report performs no conversion and does not claim it is the historical
administrative portrait or a native-rendering success.

## Earlier stages and remaining limits

Network task maker DAT7da808+7da4b4 resolves **ELFVT213cfcc**, invoke
**G7de838**. It checks **GetResultCode==1 at7de85c**, opens a local file,
copies GetBody bytes, writes via RMFileWrite10c97a4 at7de88e and closes.
HTTP200 alone does not separately measure each of those outcomes.

Completion maker DAT7da80c+7da5b8 resolves **ELFVT213d00c**, invoke
**G7dec58**. It creates CSRUIImageNode and calls
**LoadFromRawImage7b0e34 at7ded3c**. Only a nonzero load result registers file
metadata and emits the image completion event7defc0 at7ded5c.

LoadFromRawImage opens the downloaded file and calls
**CRMResourceMgr4.LoadImage2(FST)10e98bc at7b0eac**, which invokes
**MakeImage2FromFile10e9a0c at10e993a**. That function uses
**CRMFFmpeg.Init1107468** and **Decode1107cd0**, then CRMImage2.Init/BitBlt.
No exclusive PNG/JPEG support restriction or required format conversion was
recovered. Native decode result, hash-match/OnSync and final pixels remain
separate runtime validations. Target dumps: **7de838/7dec58/10e9a0c** if
diagnosis remains necessary after respecting the proven size requirement.
