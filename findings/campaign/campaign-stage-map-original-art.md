# Original campaign map resource audit

2026-10-09. Read-only audit of preserved final-client PAD assets. No emulator,
Ghidra project, runtime profile, reference data or save was modified.

## What the originals prove

`MAP_ZONE_1` is a package filename, not a named resource in that package.
Its original 6,129,328 bytes have SHA256
`258e21f9e203b4dd837cf8e4ba945c1a14f2834b52b3f1ccaa879da1c028ee11`.
Its named resources are **S2 sprites** `MS_MAP1`, `MS_MAP2` and
`MS_CLOUD1` through `MS_CLOUD6`; there is no named AT animation or RW
resource called `MAP_ZONE_1`. A scan of all 774 original PAD JET files likewise
found no header with that name. Therefore the current area-reference string
cannot be justified by the existence of the similarly named file.

Exact headers, packed body sizes and closed image references:

- `MS_MAP1`: header 6,128,362; packed 37; inflated S2 66 bytes;
  image ID `0xe81e0e52` at S2+46 resolves to I2 header 313,467.
- `MS_MAP2`: header 6,128,423; packed 37; inflated S2 66 bytes;
  image ID `0x1ab38547` resolves to I2 header 2,158,000.
- `MS_CLOUD1` through `MS_CLOUD6`: headers 6,128,484 / 6,128,634 /
  6,128,772 / 6,128,910 / 6,129,049 / 6,129,189; packed sizes
  126 / 114 / 114 / 115 / 116 / 115. All reference I2 ID `0x64427c8b`,
  header 0. The complete outer-header walk ends exactly at 6,129,328.

These are package-to-resource edges, **not recovered per-area assignments**.
No evidence here assigns `MS_MAP1` or `MS_MAP2` to Red Rock or Aurora.

## N001 through N005 are a different family

The following original files were walked to exact EOF:

- N001.jet: 869,436 bytes; SHA256
  `a54b3997bf8f2b60f4a0ae787d9a926c2a9188f0fb6661f1e153e3b4cc9cb6e8`.
  RW resources N001 / N001_A / N001_B / N0012. Atlas and Spine body/face/hair
  structures identify character art, not a campaign-map animation.
- N002.jet: 1,522,723 bytes; SHA256
  `cfd0b67b718d7ace8efa082b0fee9e1cc032aac5ca561aec32e6927ee3d88ae1`.
  N002_BG is AT at header 1,501,679; named S2 resources N002_B01..B08,
  N002_THN and N002_ST, plus character atlas/Spine N002_A/B.
- N003.jet: 1,547,587 bytes; SHA256
  `1aaea537f33eb780bce5b6a5f4592cf2d1242377af5e6677822fbaf7b616a27a`.
  RW N003 / N003_A / N003_B / N0032, including character atlas/Spine data.
- N004.jet: 1,651,492 bytes; SHA256
  `dac953f788f16936f95c664cb9fd28e628f24b3325a7dc241a19b658e86935bb`.
  N004_BG is AT at header 1,640,181; S2 N004_B01..B16, THN/ST and atlas/Spine.
- N005.jet: 1,982,053 bytes; SHA256
  `dd3899a3ee13dc3dc05e47f3add5f23646f5c7f591767d9cc3f472121f59ce56`.
  N005_BG is AT at header 1,941,237; S2 N005_B01..B08, THN/ST and atlas/Spine.

An `N00x_BG` name alone does not establish a campaign-stage-map binding.
Neither N001 nor N003 has such an AT in its bare pack; separate suffixed
packages and popup layouts must not be conflated with the stage map.

## Additional genuine mission UI assets

Original UI_TUTO.jet is 5,791,712 bytes; SHA256
`06e94376790ea5fcef72d597fe01ecc03a870ca4e4bbecdfc99e13461af9c99a`.
It contains S2 `MS_BG` at header 5,790,181 (packed 36, inflated 66;
SHA256 `a4d614dbcc995ddef74641144ad98eb2e693ce7a6bf8a529b06047aeb30390d5`),
and AT `MAP_ANI` at header 5,790,718 (packed 91, inflated 341;
SHA256 `62b001e5b66702f108d07aed613efdd7c5fc184c3ff3a35c6df3b2290fa14768`).
The AT frame count at+43 is 21; its complete frame walk from+47 reaches 341,
with exact S2 references MAP_ANI_01..21, each duration approximately 0.05s,
zero event length. All 21 S2 headers occur in the same original pack.

It also owns original **AT reward animations** `MS_RW_G`, `MS_RW_S`, `MS_RW_B`
at headers 5,791,193 / 5,791,289 / 5,791,388, packed 72 / 75 / 75 and
inflated 229 each. This corrects the old `map-backdrop.md` statement that their
owner package was unknown; that earlier plaintext search missed encoded names.
This does not prove that those assets are currently served or drawn.

## Native seam and remaining uncertainty

Retained `analysis/native-stage-map-scene.txt`, CreateArea at G00e91f0c,
passes the scene string at+0x874 directly through CMHashID to
CSRUIImageNode::LoadAnim. It also has a separate hardcoded LoadAnim near
G00e924d8. Root is resolving the original relocated string and reference
selection path; this audit does not substitute an inferred string for it.
LoadAnim resource-type acceptance is not established here.

The per-area original background mapping, the black-screen causal attribution,
and any rendered repair remain unproved. Do not invent MAP_ZONE_2..5 files,
assign NPC backdrops by filename similarity, or claim the original reference
catalog has been recovered.

## Follow-up: representative original pixels

Decoded original I2 dependencies with the existing `decode_i2_texture` and
saved unedited PNGs under `analysis/research/campaign-map-original-pixels/`.
The source originals were not modified. These files contain extracted pixels,
not generated replacement art.

- `MAP_ANI_01`, `_11`, `_21`: each S2 refers to a 133×47 I2 image.
  IDs `0x7bd67fbf`, `0xd499ba77`, `0x33d3b55f` at headers 1,335,868 /
  1,351,291 / 1,369,689 in UI_TUTO. Frames 01 and 21 are completely opaque
  black; frame 11 is a white elliptical ring against black. Visual inspection
  identifies a small ring/effect, **not campaign landscape scenery**.
- `MS_BG`: I2 `0xe50ff5d1`, three same-ID fragments at headers 5,657,974 /
  5,694,445 / 5,730,741. Combined decode is 2048×2732, every alpha value 8,
  a near-transparent pale patterned overlay. It is not a landscape background.
- `MS_MAP1` decodes to 685×1312 and `MS_MAP2` to 685×2790. Viewed PNGs depict
  a snowy overhead mountain/valley map; MAP1 includes a circular settlement and
  MAP2 contains repeating icy valley sections. This proves genuine map artwork
  exists, but not which area/reference should select it or whether LoadAnim
  accepts the S2 resource directly.

Do not select MAP_ANI or MS_BG as per-area background scenery merely because
their names sound relevant. The inspected dimensions and pixels rule that out.

## Method limits

All originals came from
`recovered-assets/phone-2026-09-18/extracted/split_PADResource/assets`.
Walk each 24-byte outer header using packed length uint32+8, identity uint64+12
and the native alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._` (base38).
Zero/opaque numeric I2 identifiers are not semantic names. S2 image IDs use+46.
RW/AT/S2 zlib bodies were inflated separately; large image containers can use
internal blocks. The initial header audit made no pixel claim; the follow-up
above specifically records the representative image dependencies decoded.
The older list-jet-entries display decoder reports several opaque I2 keys as
`0`; its output was not used to establish any identity.
