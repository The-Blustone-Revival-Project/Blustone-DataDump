# First Episode story: original assets and remaining generated binding

2026-10-05. Read-only original public PAD assets and original ELF; no VM, Ghidra, source, account or original writes. Supersedes the earlier scoped unknown for dialogue entrypoint availability. Addresses use Ghidra coordinates.

## Positive first-story conversation

Original `DIAL-EN.jet` contains native header name **EP_0301A** at byte2425897, packed payload2961bytes, zlib-inflated41555bytes. Body is RW plus little-endian length and UTF8 BOM followed by **TalkerMakerProject XML**. Thus the original English dialogue exists; absence from UI_JSON_RO/UI_XML_RO was only a table-local finding. Same named record exists in JA(header2777240), KO(2681180), SC(2603009), TC(2593560). All5 dialogue files walked exactly to EOF.

The XML contains28 DialogEntry records and3 actor declarations: actor1 Name%user_name%, CardTypeChar, CardID009; actor2 Lana, CardTypeNPC, CardID001; actor3 Tyltyl, CardTypeChar, CardID004. Scripts open with `play-bgm res:BGM_LANA`, `play-env res:AMB_PLT`, `bg-add res: N001_BG`; request voice clips C009_20_1..7 and C004_20_1..3; end with `episode_clear` plus fade/wait. The first-story conversation actors are therefore distinct from catalog **res2=C003_DIALOG**. Do not treat res2 as the dialogue's sole actor dependency or rewrite original actors to currently owned hunters.

## Native loading and generated portrait identifier

Existing `ghidra-episode-dialogue-loader.txt/-keys.txt` prove CSRDlgContainer.Load G8c23a4 and TalkerMaker.LoadFile Gb59ba0; the latter expects TalkerMakerProject and calls normal LoadRawData. Debug .XML filename literals do not require inventing an HTTP endpoint. Resource identity EP_0301A is verified by the original header and its actual XML, not a catalog-only reference.

Outer resource **EP_DIA_4** is positively present in EPISODE.jet at header6526756, payload37bytes, kindS2. **C003_DIALOG is absent from all774 public PAD outer .jet record names**, with every file walking exactly to EOF. This is not proof the generated alias is missing at runtime.

Original **SRGetResDlgID2 G10ad60c** loads format `%s_DIALOG` via LDR G10ad614/headerliteralG10ad628 and ADD G10ad61c; input basic_string data is moved to format argument r2, then the string format helper is called at G10ad620. This positively proves native synthesis of C003_DIALOG from prefix C003. Original C003.jet has named RW records C003,C003_A,C003_AB,C003_B,C003_D,C003_DA,C003_DB; C003_DA contains C003_d.png atlas text and C003_DB binary animation/skeleton data. **Assignment of these records to the generated C003_DIALOG alias remains unproved**; res2 consumer/load-helper or resource-map registration must close it. A filename/name resemblance is insufficient for a server resource alias.

## Exhaustive bounded outer inventory and script dependency hits

Scope: exactly774 .jet files directly in preserved public PAD assets; original reads only; each24-byte header uses packed-size uint32 at+8 and name uint64 at+12, then advances24+packedsize. All774 ended exactly at filesize. Resource bodies can be zlib or raw I2/S2/AT/SN; the scan does not flatten nested/generated aliases.

Name decoding reproduces native RM10to38 G10d2af4: repeatedly divide uint64 by38, convert remainder with alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`, reverse digits. This yields exact encoded names for descriptive records. Early image records also use numeric/hashed identifiers; their base38 renderings below are identifiers, **not claims of a human-readable original sprite assignment**.

Exact matching outer records for first XML script dependencies:

- AMB_PLT: SND_CDN.jet header1342263 packed165520.
- BGM_LANA: SND1.jet header4117114 packed585184.
- C003_DIALOG: no matching outer record; generated/nested binding not excluded.
- C004_20_1: VOICE_CDN6.jet header2325491 packed126265.
- C004_20_2: VOICE_CDN6.jet header2451780 packed83633.
- C004_20_3: VOICE_CDN6.jet header2535437 packed105785.
- C009_20_1: VOICE_CDN2.jet header3263029 packed128355.
- C009_20_2: VOICE_CDN2.jet header3391408 packed81544.
- C009_20_3: VOICE_CDN2.jet header3472976 packed102442.
- C009_20_4: VOICE_CDN2.jet header3575442 packed126265.
- C009_20_5: VOICE_CDN2.jet header3701731 packed18850.
- C009_20_6: VOICE_CDN2.jet header3720605 packed105785.
- C009_20_7: VOICE_CDN2.jet header3826414 packed76528.
- EP_0301A: DIAL-EN.jet header2425897 packed2961; DIAL-JA.jet header2777240 packed3474; DIAL-KO.jet header2681180 packed3363; DIAL-SC.jet header2603009 packed3187; DIAL-TC.jet header2593560 packed3149.
- EP_DIA_4: EPISODE.jet header6526756 packed37.
- N001_BG: N001_BG.jet header2282340 packed49.

## Complete header name inventories

EPISODE.jet: 128 records, complete EOF walk.

```text
10AKGB. O536DI 1048M78 L9YSRN _HKJW6 SKI7I4 K.TW7P 1QMVJC 72FU78 15PHV44 15ZYQ6T 1DKC34K 1D.3TXS ST1_5D TU_.R9 ASMZ5G SHP84L 2WGQHI 7BL.PE W7N932 2WSBPO 19825Z6 KJMHQH PZST18 132HYWM 1DHG0YE 1ET83I7 DO8GRW 1D9O28J 16_6_V3 12F9CZD U017IR PRRX7E OFTHP6 SKKMA2 197D00C SN7.OX 8KQN3. 15JH1H2 HDJDM. LOYN3M 1F4DCY3 10ZT_HB 5I5FSY 1D.DYQN 1CXMEZK 4T8QE7 7XMUHK QN208V PNUUCA 14ZZ70E 1CAOATA VKO2KH 1E.BOXT 3QW6ES 4MGG3. 1AY35AI J4XLLQ 1DWCKA5 4WBHPA 1DBDP.2 8IJGRP J191GX EP_DIA_ON EP_DIA_FIGHT EP_DIA_TALK EP_ST_FIX EP_DIA_EVENT EP_DIA_NOR EP_DIA_LV EP_CLEAR EP_NEW EP_DIA_BG EP_DIA_1 EP_DIA_2 EP_DIA_3 EP_DIA_4 EP_DIA_5 EP_MK_ON EP_MK_OFF EP_X_BTN EP_E_CLEAR EP_MAP EP_MAP_S EP_SEASON1 EP_SEASON2 EP_HLIGHT EP_CLEAR0 EP_CLEAR1 EP_CLEAR2 EP_CLEAR3 EP_CLEAR4 EP_CLEAR5 EP_CLEAR6 EP_CLEAR7 EP_CLEAR8 EP_CLEAR9 EP_E_CLEAR0 EP_E_CLEAR1 EP_E_CLEAR2 EP_E_CLEAR3 EP_E_CLEAR4 EP_E_CLEAR5 EP_E_CLEAR6 EP_E_CLEAR7 EP_DIA_6 EP_DIA_7 EP_DIA_8 EP_BTN_02 EP_BTN_01 EP_BTN_04 EP_BTN_03 EP_BTN_06 EP_BTN_05 EP_BTN_08 EP_BTN_07 EP_BTN_10 EP_BTN_09 EP_BTN_12 EP_BTN_11 EP_BTN_14 EP_BTN_13 EP_BTN_16 EP_BTN_15 EP_BTN_17 EP_BTN_18 E_CLEAR_ANI1 E_CLEAR_ANI2
```

R_EPISODE.jet: 66 records, complete EOF walk.

```text
EVENT SEASON_LIST SEASON1 STAT TUTO CB0001 CB0002 CB0003 CB0004 CB0101 CB0102 CB0103 CB0201 CB0202 CB0301 CB0302 CB0401 CB0501 CB0502 CB0601 CB0602 CB0701 CB0702 CB0801 CB0802 CB0901 CB0902 CB1001 CB1002 CB1101 CB1102 CB1201 CB1202 CB1301 CB1302 CB1303 CB1304 CB1305 CB1401 CB1402 CB1501 CB1502 CB1601 CB1602 CB1603 CB1604 CB1701 CB1702 CB1703 CB1704 CB1705 CB1706 EVCB0101 EVCB0102 EVCB0103 EVCB0104 EVCB0105 EVCB0201 EVCB0202 EVCB0203 EVCB0204 EVCB0205 EVCB0301 EVCB0302 EVCB0303 EVCB0304
```

## Next closure and promotion limits

The catalog and English conversation are recovered. The next parent-only check is the native **res2 consumer** and generated dialogue portrait/resource alias (SRGetResDlgID2 G10ad60c and its callers/registration), plus CardTypeChar009/004 and NPC001 portrait creation. All requested background/music/environment/voice names have positive original outer-record matches above: N001_BG.jet, SND1.jet, SND_CDN.jet, VOICE_CDN2.jet and VOICE_CDN6.jet. Those identify original dependency packs; successful pack download is separate from native resource binding.

An opt-in additive asset profile may use these original names/packs after parent validates dependencies. No default CDN advertisement, resource version change, reward grant, original-level substitution or claim of native playback was made. This report proves the first-story XML exists and distinguishes catalog marker art from conversation participants; it does not prove the live engine has loaded it.
