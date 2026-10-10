// Resolve the JSON key string for every nlohmann json::operator[] call inside a
// function, by following register dataflow instead of pairing a literal load
// with a nearby `add rX, pc`.
//
//   ResolveOperatorBracketKeys.java <output-file> <json-operator-bracket-hex> <fn-entry-hex>
//
// WHY THIS EXISTS
// ---------------
// `tools/resolve-literals-offline.py` pairs a literal load with the next
// `add rX, pc`. That heuristic has produced three WRONG string keys in this
// project (see analysis/research/ROOT-CAUSE-v4-nested-waves.md §3): a
// too-narrow window missed `wave_list`, and a too-wide window invented `_id`
// out of a stack-guard literal load. Both failure modes produce a plausible
// string, which is worse than producing nothing.
//
// This script does not pair anything. For each call to operator[] it walks
// backwards and asks: which pc-relative literal load most recently wrote the
// key register (r1 by the aapcs convention) before this call?
//
// For the Thumb idiom used throughout this binary:
//
//     ldr  r1, [pc, #imm]      ; r1 = (pc + imm) -> a word holding a relative offset
//     add  r1, pc               ; r1 += Align(PC, 4)
//     ...
//     bl   json::operator[]
//
// the literal address is
//     Align(addInstruction + 4, 4) + slotWord
// and the string lives there. Strings are read from Ghidra's RELOCATED memory,
// because the on-disk value at a literal slot is a pre-relocation placeholder.
//
// Every other pc-relative literal in the function is also printed with its
// distance to each call, so a key can be attributed by elimination as well as
// by dataflow.

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.symbol.Reference;

public class ResolveOperatorBracketKeys extends GhidraScript {

    private static final int MAX_LITERAL_DISTANCE = 64;

    private static final class Load {
        Address at;
        Address addAt;
        int reg = -1;
        Address slot;
        Address target;
        String value = "";
    }

    // Named readString, not `str`, because GhidraScript already declares `str`.
    private String readString(Address address, int limit) {
        if (address == null) return "<null>";
        StringBuilder value = new StringBuilder();
        Memory memory = currentProgram.getMemory();
        try {
            if (!memory.contains(address)) return "<unmapped>";
            for (int i = 0; i < limit; i++) {
                Address cur = address.add(i);
                if (!memory.contains(cur)) break;
                int b = memory.getByte(cur) & 0xff;
                if (b == 0) break;
                if (b < 0x20 || b > 0x7e) return "<non-ascii>";
                value.append((char) b);
            }
        }
        catch (Exception ignored) {
            return "<error>";
        }
        return value.toString();
    }

    private Address align4(Address address) {
        long v = address.getOffset() & ~0x3L;
        return address.getAddressSpace().getAddress(v);
    }

    // Strip the mnemonic, returning just the operand text ("r1, [0x00a0d500]").
    private String operands(String printed) {
        if (printed == null) return "";
        int idx = printed.indexOf(' ');
        return idx < 0 ? "" : printed.substring(idx + 1).trim();
    }

    // Extract the destination register number from a printed OPERAND list.
    // The caller must pass operands(printed), not printed: passing the whole
    // instruction ("ldr r0,[0x...]") makes this look at 'l' and return -1, which
    // is why an earlier version of this script found zero literals.
    private int parseReg(String text) {
        if (text == null || text.length() < 2) return -1;
        if (Character.toLowerCase(text.charAt(0)) != 'r') return -1;
        int i = 1;
        int value = 0;
        int digits = 0;
        while (i < text.length() && Character.isDigit(text.charAt(i))) {
            value = value * 10 + (text.charAt(i) - '0');
            i++;
            digits++;
            if (digits > 2) return -1;
        }
        if (digits == 0 || value > 15) return -1;
        if (i < text.length()) {
            char c = text.charAt(i);
            if (c != ',' && c != ' ' && c != ']' && c != ')') return -1;
        }
        return value;
    }

    // Extract the 0x... operand address from a printed instruction, e.g.
    // "LDR R1, [0x00a0d4f4]" -> 0x00a0d4f4. Returns -1 if there is none.
    private long parseHexOperand(String text) {
        if (text == null) return -1;
        int idx = text.indexOf("0x");
        if (idx < 0) return -1;
        long value = 0;
        int digits = 0;
        for (int i = idx + 2; i < text.length(); i++) {
            char c = Character.toLowerCase(text.charAt(i));
            int digit = Character.digit(c, 16);
            if (digit < 0) break;
            value = value * 16 + digit;
            digits++;
            if (digits > 8) return -1;
        }
        return digits == 0 ? -1 : value;
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 3) {
            throw new IllegalArgumentException(
                    "Usage: ResolveOperatorBracketKeys.java <output-file> <operator[]-hex> <fn-entry-hex>");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        long operatorBracket = Long.parseLong(args[1].replace("0x", ""), 16);
        Address entry = toAddr(Long.parseLong(args[2].replace("0x", ""), 16));
        Function function = currentProgram.getFunctionManager().getFunctionContaining(entry);
        if (function == null) function = createFunction(entry, null);
        if (function == null) throw new IllegalStateException("no function at " + entry);

        Memory memory = currentProgram.getMemory();
        Address begin = function.getBody().getMinAddress();
        Address end = function.getBody().getMaxAddress().next();

        // ---- pass 1: every pc-relative literal load in the function ----
        List<Load> loads = new ArrayList<>();

        InstructionIterator instructions = currentProgram.getListing().getInstructions(begin, true);
        while (instructions.hasNext()) {
            Instruction ins = instructions.next();
            Address a = ins.getAddress();
            if (a.compareTo(end) >= 0) break;
            Instruction nextIns = ins.getNext();
            String mnemonic = ins.getMnemonicString();

            // A Thumb-2 pc-relative literal load looks like
//     ldr rD, [0xSLOT]      ; the slot word is a RELATIVE offset
//     ...                   ; other instructions may intervene
//     add rD, pc             ; <-- must write the SAME register
// The `add rD,pc` is NOT always the immediately following instruction: at
// 0xa0d1b0 the sequence is `ldr r1,[0xa0d4f4]` / `add r2,sp,#0x80` /
// `add r0,pc` / `movs r4,#0` / `add r1,pc`, so a strict "next instruction"
// rule misses the real `add r1,pc` entirely and then pairs the load with the
// wrong `add` -- which is how `_id` was invented from the stack-guard load.
            //
            // The disambiguator is REGISTER MATCHING: only the `add rD,pc` that
            // writes the same register as the `ldr` belongs to it. That is
            // unambiguous, and it is what this script uses.
            // No getLength() filter: in this Thumb image Ghidra reports len=2 for every
            // literal `ldr rX,[0xNNNNNNNN]`, so a "must be a 4-byte Thumb-2
            // instruction" test rejects all of them. The `add rD,pc` register
            // match below is the real discriminator.
            boolean ldrLiteral = mnemonic.equalsIgnoreCase("ldr")
                    && parseHexOperand(ins.toString()) >= 0;

            if (ldrLiteral) {
                int ldrReg = parseReg(operands(ins.toString()));
                if (ldrReg < 0) continue;
                // Scan forward a few instructions for `add r<ldrReg>, pc`.
                // Bounded so an unrelated `add rX,pc` many instructions later
                // cannot be adopted by this load.
                Instruction addIns = null;
                Instruction probe = ins;
                for (int hops = 0; hops < 6 && probe != null; hops++) {
                    probe = probe.getNext();
                    if (probe == null) break;
                    if (probe.getMnemonicString().equalsIgnoreCase("add")
                            && parseReg(operands(probe.toString())) == ldrReg
                            && probe.toString().toLowerCase().contains("pc")) {
                        addIns = probe;
                        break;
                    }
                }
                if (addIns == null) continue;
                // The slot address comes from the printed operand ("LDR R1, [0x00a0d4f4]"),
                // not from getReferencesFrom(): auto-analysis does not always
                // create a data reference into a Thumb literal pool.
                long slotValue = parseHexOperand(ins.toString());
                Address slot = slotValue < 0 ? null
                        : a.getAddressSpace().getAddress(slotValue);
                if (slot != null && memory.contains(slot)) {
                    Load load = new Load();
                    load.at = a;
                    load.addAt = addIns.getAddress();
                    load.reg = ldrReg;
                    load.slot = slot;
                    long offset = Integer.toUnsignedLong(memory.getInt(slot));
                    // PC for add rD,pc is the instruction address + 4, with only
                    // bit 0 cleared -- NOT rounded down to a word. Rounding to 4
                    // lands 2 bytes early for half the call sites and yields a
                    // plausible but wrong string: at 0xa0d50e it gives 0x01d76beb
                    // (the tail of next_spawn_ms) instead of 0x01d76bed
                    // (show_thumbnail). Hand-checked against the raw pool bytes in
                    // analysis/ghidra-ids-11-pool-showthumbnail.txt, where only
                    // 0x01d76bed is preceded by a NUL.
                    Address pc = addIns.getAddress().add(4);
                    pc = pc.getAddressSpace().getAddress(pc.getOffset() & ~0x1L);
                    load.target = pc.getAddressSpace().getAddress(pc.getOffset() + offset);
                    load.value = readString(load.target, 96);
                    loads.add(load);
                }
            } else if (mnemonic.equalsIgnoreCase("adr")) {
                int reg = parseReg(operands(ins.toString()));
                long adrValue = parseHexOperand(ins.toString());
                if (reg >= 0 && adrValue >= 0) {
                    Address target = a.getAddressSpace().getAddress(adrValue);
                    if (target != null) {
                        Load load = new Load();
                        load.at = a;
                        load.reg = reg;
                        load.target = target;
                        load.value = readString(target, 96);
                        loads.add(load);
                    }
                }
            }
        }

        // ---- pass 2: attribute a key to each operator[] call ----
        PrintWriter out = new PrintWriter(outputFile, "UTF-8");
        out.println("PROGRAM\t" + currentProgram.getName());
        out.println("FUNCTION\t" + function.getName() + "\tentry=" + function.getEntryPoint()
                + "\tbody=" + function.getBody().getNumAddresses());
        out.println("OPERATOR_BRACKET\t0x" + Long.toHexString(operatorBracket));

        int callIndex = 0;
        InstructionIterator calls = currentProgram.getListing().getInstructions(begin, true);
        while (calls.hasNext()) {
            Instruction ins = calls.next();
            Address a = ins.getAddress();
            if (a.compareTo(end) >= 0) break;

            // A direct call is exactly `getFlowType().isCall()` plus a single flow
            // whose target is the function we were asked about. Matching on the
            // flow target alone is sufficient and avoids depending on the FlowType
            // constant names, which differ between Ghidra releases.
            if (ins.getFlows().length == 1
                    && operatorBracket == ins.getFlows()[0].getOffset()) {
                callIndex++;
                out.println();
                out.println("--- call #" + callIndex + " @ " + a + "  " + ins);
                for (int keyReg : new int[] { 1, 0 }) {
                    Load best = null;
                    for (Load load : loads) {
                        if (load.reg != keyReg) continue;
                        if (load.at.compareTo(a) >= 0) continue;
                        if (a.subtract(load.at) > MAX_LITERAL_DISTANCE) continue;
                        if (best == null || load.at.compareTo(best.at) > 0) best = load;
                    }
                    if (best == null) {
                        out.println("    r" + keyReg + ": <no pc-relative load within "
                                + MAX_LITERAL_DISTANCE + " bytes>");
                    } else {
                        out.println("    r" + keyReg + ": " + best.value
                                + "   [literal@" + best.target
                                + "  ldr@" + best.at
                                + "  slot=" + best.slot
                                + "  add@" + best.addAt
                                + "  dist=" + a.subtract(best.at) + "]");
                    }
                }
                out.println("    all pc-relative literals within " + MAX_LITERAL_DISTANCE
                        + " bytes above this call:");
                for (Load load : loads) {
                    if (load.at.compareTo(a) >= 0) continue;
                    long distance = a.subtract(load.at);
                    if (distance > MAX_LITERAL_DISTANCE) continue;
                    out.println("        r" + load.reg + "  " + load.value + "   @" + load.at
                            + "  dist=" + distance);
                }
            }
        }
        out.close();

        // ---- the full literal inventory, in its own file section ----
        PrintWriter inv = new PrintWriter(new File(outputFile.getParent(),
                "ghidra-ids-07b-inventory-" + function.getName() + ".txt"), "UTF-8");
        inv.println("PROGRAM\t" + currentProgram.getName());
        inv.println("FUNCTION\t" + function.getName() + "\tentry=" + function.getEntryPoint());
        inv.println("PC_RELATIVE_LITERALS\t" + loads.size());
        for (Load load : loads) {
            inv.println("    r" + load.reg + "\t" + load.value + "\t@" + load.at
                    + "\tslot=" + load.slot + "\t-> " + load.target);
        }
        inv.close();

        println("ResolveOperatorBracketKeys done, calls=" + callIndex + " loads=" + loads.size());
    }
}
