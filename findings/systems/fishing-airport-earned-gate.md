# Fishing Airport variant requires Red Rock stage7

2026-10-06. Offline native evidence; no unlock flag, state grant, client patch
or emulator input. G addresses refer to the relocated Ghidra program.

ApplyScene Gea6600 loads the scene type directly from its request at+8 and
dispatches TBH atGea673a (tableGea6744). Type0x83 entersGeace9a. Tutorial
type1/step0 state greater than1 entersGeadf40. The first normal check reads
PlayData marker `tuto_gacha`: exact relocated slotGeae28c plus ADDGeadf4e.
Nonzero takes TutorialNPCDlg with NPC0000; it is not the fishing unlock marker.

With that marker zero, Geafb6c puts0x1c inr1 and Geafb6e calls
CSRPlayData.GetStageAchieveCnt(TU_TYPE) G84e87c. That wrapper resolves the TU
through CSRStaticData.GetStageID Gf42820 before reading stage achievement count.
GetStageID's case0x1c selectsGf428b0; LDR/ADD atGf428b0/Gf428b2 resolve exactly
`n_03_07`. Thus at least one achievement/star on Red Rock7 selects the fishing
variant. No requirement for three stars or player level is present in this arm.

Nonzero count falls throughGeafb78 to ordinary NPCDlg. Its CREATE_INFO+4 string
is NPC0005: literalGeafc4c plus ADDGeafbd2. Zero branchesGeafe1a to ordinary
NPCDlg with NPC0000: literalGeb0014 plus ADDGeafe74. Both CREATE_INFO types83.
Original XML agrees: NPC0005 replaces Exit with Fishing (node6); NPC0000 has
Cruise/Missions/Talk/Exit. Fishing node6 dispatches scene0x46.

Current persisted account1000001 has no n_03_07 stars or clear, matching the
observed NPC0000 menu in fishing-001. Next native work is ordinary campaign
progress through remaining Glacier stages and Red Rock7, then revisit Airport.
Do not toggle fishing_open, tuto_gacha or stars to bypass the recovered gate.
Fish/bait IDs, pool probabilities/prices and scene settings acceptance remain
separate unknowns after entrance unlock.

Diagnostics: the prior ApplyScene instruction listing had only200lines because
its switch targets were not disassembled. Decompilation timeout and that partial
listing were not absence of the gate. DisassembleThumbAt performs transient
branch disassembly under-readOnly (changes discarded), and explicit relocated
ResolveLiteralPairs closes string references outside the original function body.
ELF/capstone jump-table arithmetic located candidates; Ghidra instruction and
relocated-memory outputs establish the specific branches and strings.
