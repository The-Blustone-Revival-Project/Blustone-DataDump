# Starter skill resource bindings and verified JET names

2026-10-04. Read-only original-library Capstone, original package bytes, existing JET helpers and local skill reports. No source/runtime/Ghidra/original/tool edits. Addresses are Ghidra image addresses. No original cut_in_id/icon_id assignment is fabricated.

## Major inventory correction: resource names are encoded in headers

**CRMResMap::ExtractJETInfo0x10e5f58** reads a24-byte record header at0x10e6222, constructs a pointer to its **8-byte name id atheader+12** (0x10e6214..18), and calls **RM10to38(uint64 const&,char*)0x10d2af4** at0x10e6232. This proves names are not merely printable strings hidden in payloads.

RM10to38 divides the input64-bitinteger by38 (0x10d2b64..70), reverses digits, maps0..9 toASCII0..9 and10..35 toA..Z (0x10d2b94..9a), **36 to`.`**(0x10d2bb4) and37 to`_`(0x10d2bb8). Exactalphabet:

```text
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._
```

The base38 names below were read from those original header ids. Record traversal uses the header's packed-size field+8 and skips24+packedsize, inflating payloads with established zlib handling where appropriate. **All inspected files ended exactly at their byte size**, including raw S2/AT tailrecords the older list helper missed. No broad extraction/media export occurred.

Earlier starter-skill-art-inventory.md statements that CUT/Q names were unrecoverable through printable parsing are therefore **superseded as inventory conclusions**. The old attempts remain useful evidence of why payload-string scraping failed. Field+12 is a **uint64 encoded name**, not a plain CRC32; interpreting its low32bits alone loses identifier information.

## Genuine names inside original packs

### Skill icons in C001..C004_Q.jet

All four portrait/thumbnail packages include named **AT animation records**:

```text
C001_SI1 C001_SI2 C001_SI3 C001_SI4 C001_SI5
C002_SI1 C002_SI2 C002_SI3 C002_SI4 C002_SI5
C003_SI1 C003_SI2 C003_SI3 C003_SI4 C003_SI5
C004_SI1 C004_SI2 C004_SI3 C004_SI4 C004_SI5
```

Their associated **S2 sprite** records are C00x_SI01..SI05. Thus C00x_SI1 andC00x_SI01 are different resource records, not interchangeable formatting. Exact active-icon candidate AT offsets: C001_SI1 **50528**, C002_SI1 **48968**, C003_SI1 **50388**, C004_SI1 **52260**. These are fileheader offsets. All corresponding Qpacks exist and are small enough for narrow resource coverage.

**[VERIFIED]** Named AT records exist and match the LoadAnim resource kind used by skill-panel rendering. **[INFERRED]** SI1 corresponds to slot1, based on the five indexed icon families. **[UNKNOWN original assignment]** No original captured GetCard row has been found proving `skill[type1].icon_id == C00x_SI1`. This is an evidence-backed reconstruction candidate, not an original response-value claim.

### CUT pack filename is not character identity

**CUT_001.jet** contains AT **CUTIN002**, **CUTIN002A**, with S2sprites CUTIN_002, CUTIN_0021, CUTIN_0022, CUTIN_002A, CUTIN_002A1, CUTIN_002A2. AT offsets **622698**, **622839**. It does **not** establish a resource named CUT_001 or a Lantern-only cut-in.

**CUT_002.jet** contains AT **CUTIN003**, **CUTIN003EF**, **CUTIN005**, **CUTIN005EF**, at offsets **1937834,1938031,1938186,1938285**. Associated S2spritefamilies are CUTIN_003A/B/C/D/E/F/G andCUTIN_005A/B/D/E/F/G. Thefilename cannot be assigned as Mowgli's original cut_in_id.

These findings disprove the previously tempting filename-to-card/skill mapping. No CUT_003/CUT_004 files were found; the existing CUTpackgroups already contain independently numbered cut-in resources.

### Effect videos and sound records

Native-named SNvideo inventory (including alpha companions where present):

- **C001_EFT:** E01/E02/E03/E04/EC, each with_A companion (10records).
- **C002_EFT:** E01/E02/E03/E04/E05/EC, each with_A (12).
- **C003_EFT:** E01/E02/E03/E04/EC with_A, plusE05 without_A (11).
- **C004_EFT:** E02/E03/EC, each with_A (6); **noE01**.

Prefixes are their respective C00x, e.gC001_E01. The existing base RW animation eventreferences corroborate manyofthese exactnames; C004 lacksE01 in both baseevents andvideo inventory. These are **effect resource names**, not proof of `cut_in_id` field values.

SND inventories similarly decode exact C001_SND01..05, C002_SND01..05, C003_SND01..08, C004_SND01..03. Headerflags/tags vary between files; do not requireouterbytes22..23SN when inspecting all SNpayloads. The innerSNpayload startsat24; naming is the same nativeheader decoder.

## Parser and actual consumer evidence

`SRSKILL_INFO::parse`0xf219ac converts cut_in_id andicon_id fromstrings at0xf227b2/0xf227fe. Exact storage was rechecked: **cut_in_id std::string atrecord+0x54**, **icon_id std::string atrecord+4**. Thefields are not numeric packordinals and not encodednameids on the JSONwire.

**Skill-panel icon consumer:** `CSRPopUpCardInfo::SetSkillPanel`0xb9610c receives iconstringargument inr2 (retainedsb0xb96120), constructs CMHashID fromthatstring0xb9618c..90, and calls **CSRUIImageNode::LoadAnim0x7b071c** at0xb96198. It only null-checks the destinationnode at0xb9617e; this visible path has **no empty-string test/default-prefix substitution**. Empty icon may therefore attempt an emptyresource lookup; existinginstrumentedguards are not evidence of the original binding. The received animation candidates above fitits actual loader kind.

**Battle input icon layout is separate:** `CSRGameActorIconSkill::LoadLayout(role,scale)`0x9af778 uses role-based `_A/_D/_F/_M`, SPR_ICON,LY_COST andIG_SK_I_N identifiers. Do not assume the reference icon_id controls every battleinputpoint or that fixing a statpanelicon cures missingactorbinding.

**Cut-in consumer remains incompletely traced:** `CSRGameSkillView::Make(DATA const&)`0xa20e0c calls `_CPrologue::Load`0xa1df14 at0xa20e96 with DATAstrings+8/+0x14. Theirsemanticorigin must be matched from the DATAproducer before either is calledcut_in_id. Later Makebranches load role/airship graphics. The inspected prefix alone does not establish howempty cut_in_id is treated. `CSRGameBase::OnSkill(DATA const&,unsigned,char)`0x9e387c andfull Make/Prologue are the focused remainingconsumer targets. No empty-cut fallback orfailuregate is claimed without this complete dataflow.

## Smallest remaining observation

For icons, a fresh native reference control can project a verified ATname into the correctly selected icon field and verify that specific card/slot renders the matching original art, with no missing-resource log. It should be described as **reconstructed binding**, until an original response row independently confirms it. No mutationwasperformedbythislane.

For cut-in, the smallest decisive read-only native measurement is the **actual SRSKILL_INFO.cut_in_id value and loaderargument on one activatedskill**, plus the actualresource-map lookup/type. If missing telemetry makes that unavailable, parent-only focused decomp **GameSkillView::Make/Prologue::Load andthe DATAproducer** can pin where thefield goes andthe emptybranch, without a guessedserver assignment. Originalcatalog/local REFcontent would be stronger still if it contains untouched GetCardskillrows.

Actualskill activation still requires the independent input/cost/eligibility/effect path to pass. Genuine poolnames alone do not prove an active skill executed, its original metadata, or that a chosen CUTINgroup belongs to a specific hunter.

## Focused cut-in dataflow dump request

A read-only scan of executable Thumb BL encodings identifies the named DATA producer: **CSRGameBase::OnProcSkillRet(_ERROR,json const&) G9cf920** calls **OnSkill G9e387c** at **G9d00d6**. OnSkill calls **CSRGameSkillView::Make Ga20e0c** at **G9e389e**. Make passes DATA+8 and DATA+0x14 strings to **_CPrologue::Load Ga1df14** at **Ga20e96**, without an early string-empty branch in that prefix. This does not yet prove which string is cut_in_id or how Prologue handles it.

Parent-only focused dump list, in producer-to-consumer order:

1. G9cf920: OnProcSkillRet (DATA assignment from selected actor/skill, including reference cut string).
2. G9e387c: OnSkill (possible skip/role behavior).
3. Ga20e0c: Make (all role branches, empty/default behavior).
4. Ga1df14: _CPrologue::Load (full function to next retained symbol Ga1fb44, size0x1c30; actual resource name construction and loader type).
5. If DATA fields remain ambiguous, G9e3b44 constructor and G9e3c4c copy constructor.

A second direct call to OnSkill exists at G9f5ba6, in a retained-symbol gap following G9f5378. The nearest symbol is a vector/event emplace helper, so that nearest-symbol name is not reliable as a caller identity. The named OnProcSkillRet producer is the preferred first target. No original cut assignment or safe empty-cut behavior has been established by these call-site observations.

## Fresh focused decompile: cut data is actor identity, not a proven cut_id

Sources: `ghidra-active-skill-cut-flow.txt`, `ghidra-active-skill-cut-strings.txt`; read-only original bytes for getter/vtable checks.

OnProcSkillRet builds DATA as follows: +0 camp, +4 attribute, +8 actor GetRef(), +0x14 actor GetResID(), +0x20 actor GetResPrefix(); +0x2c additionally gets actor res prefix for SRCanUseSkillAirShip(role)==1. Default-stat +0x14/+0x1c feed DATA+0x38/+0x3c. Make passes DATA+8/+0x14 to Prologue. **These strings must not be labeled cut_in_id.** GetResID G99b342 returns actor+0x888; GetRef G99b33a returns default-stat+4. Any earlier assignment of actor+0x888 remains an indirect provenance question, not answered by this producer.

Prologue always loads `SR_INGAME/SKILL_EFT`. It uses ref identity to FindCardByID and GetSkillInfo for title; portrait helpers SRCreateSpinePortrait/SRGetResDlgID operate on actor ResID. Static skill-text overrides may choose portrait/emotion values. No empty-cut_id default or failure branch is present because the direct reference cut field is not consumed here. Missing portrait animation can assert `Anim Not found %s`; first loop handles failed LoadAnim with assertion and null drawable, while a later portrait branch loads animation without an equivalent result check. Do not substitute a guessed CUT pack name to satisfy this path.

Make reads the native user option `battle_skill_effect` after Prologue. Zero jumps to Ga21ece, skipping heavy body assets including WAG_C1_A/WAG_C2_A/WAG_C3_A and BG_LIGHT, but **does not bypass Prologue/portrait layout**. This is a possible narrowed control setting, not proof that activation is safe. Actor motion fallback uses SRGetResSkilAct G10ad78c; portrait identifier helper G10ad5e8 and spine portrait G10af47c are focused candidates if actual resource names are required.

OnSkill registers two events then plays skill view and pauses game reason2. The four dumps do not contain callback bodies. Original vtable decoding identifies precise follow-ups: event at view+0xb4 vtable G215b9a0 operator() slot0x18 is **G9f5198**; finish event at view+0x44 vtable G215b9e8 operator() is **G9f5610**. Dump these plus GameSkillView OnUpdate Ga22a80, OnPlay Ga23d08, OnEffectFinish Ga24340 if return/application hangs. No safe whole-program blank-cut conclusion, original assignment, or completed native activation is claimed.

## Skill completion callback proof

`ghidra-active-skill-return.txt` G9f5610 is coherent: it locks the scene weak pointer, finds the captured operator serial in airship actor list, returns that actor via EnterAirship and SetVisible(true), or handles back-end actor exchange cooldown; then **ResumeGame(reason2)**, invokes model virtual event0x11, and **DeactiveSkill**. No extra server HTTP response field is parsed in this finish callback. This establishes the intended visual completion return path, not that its event is reached live.

The other decompile G9f5198 is **unusable wrong-mode output**. Original bytes read with Thumb Capstone show valid push/register loads and vector<string>::assign at G9f51cc, scene FindByName G9f51e2, FindComponentForce<CSRGameUISkillTip> G9f51ea, then **CSRGameUISkillTip::Push Ga2f9f8 at G9f51f2**. Inputs are captured GameBase pointer, TEAM_DIR from *r1, flag byte from *r2, copied vector<string> from r3. It is a skill-tip display event, not a proved combat-effect mutation callback. Correct TMode=1 or Thumb instruction listing over G9f5198..G9f529a suffices; ignore the prior software-interrupt/coprocessor C output.

## One bounded stage5 native control recommendation

Use **Tyltyl Support heal once**, with the already authorized party [2,4,1,5]. Before input identify actual owned-instance→ref mapping, ensure the front ground hunter is visibly/native measurably below max HP, and read actual battle Rage/SP >=4 (recovered active cost4). Do not substitute lobby expedition AP for battle SP, do not change battle_skill_effect, and do not assign cut ids from filenames. If no damaged target or insufficient actual SP occurs, record unmet prerequisites instead of claiming a failed heal.

Capture native SP and target HP immediately before the gesture. Use the established support activation input exactly once and observe: skill accepted/critical-or-normal branch, prologue/character portrait and skill name, Rage/SP debit, one healing effect on the expected front teammate, view finish callback ResumeGame(2)/DeactiveSkill, and continuing battle timer/actions. Record exact HP delta and cost as fixture-run observations; missing original numeric formula coefficients remain fixtures. A rising HP frame alone can be confused with passive recovery, so pair it with accepted activation and SP debit. Stop/revert to normal play after this single control; record any exact missing-resource lookup rather than adding broad packages speculatively.

Verified resource inventory for this control:

- Preserved UI_XML_RO has KO/SR_INGAME/SKILL_EFT (6369bytes). Game UI loader retries KO when selected-language lookup is empty. Live template presence still needs runtime observation.
- Original WAG_PUB.jet contains genuine WAG_C1_A at434147, WAG_C2_A at434344, WAG_C3_A at434499. Record walk ends exactly434810bytes. Make explicitly loads these names.
- Original INGAME_EFT.jet contains genuine BG_LIGHT record at442517; walk ends exactly7341359bytes. Make explicitly loads it as video.
- Tyltyl C004 family is included in default four-family CDN folding. Genuine C004_E02/E03/EC(+alpha) exist; no invented C004_E01 is required by inventory evidence.
- WAG_PUB, INGAME_EFT and SKILL_EFT are **not additional explicitly folded entries in current11+38 profile** (tools/start-server.ps1:8stage+30cardfamilies). They do exist in original APK/PAD bundled assets, so omitted CDN names do not imply missing native resources. Current native lookup is the discriminator.

This is a validation checklist, not a completed native test or guaranteed-safe blank-cut claim. No server/runtime changes were made by this lane.
