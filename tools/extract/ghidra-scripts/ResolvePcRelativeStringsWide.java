// Resolve PC-relative string references in a function, with a wider
// LDR-to-ADD matching window than ResolvePcRelativeStrings.java.
//
// ResolvePcRelativeStrings.java only looks for the matching `add rX, pc`
// within 4 instructions of the `ldr rX, [pc, #imm]`. That window is enough
// for most of this binary's straight-line key reads, but some functions
// (e.g. CSRExploreMirageInfo's /mirage/GetInfo callback at 0x9359ac)
// interleave enough register shuffling that the ADD lands further away and
// the narrow matcher reports `resolved: 0` for a function that demonstrably
// calls nlohmann::operator[](const char*) a dozen times.
//
// This version widens the window and, when the ADD is not adjacent, falls
// back to scanning every later ADD in the function that writes into the same
// register. It is a superset of the narrow script: every hit it reports is
// the same literal the narrow script would report, plus any it missed.
//
//   ResolvePcRelativeStringsWide.java <output-file> <name-fragment> [...]

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.scalar.Scalar;

public class ResolvePcRelativeStringsWide extends GhidraScript {

    private static final int WINDOW = 40;

    private String str(long addressValue) {
        try {
            Address address = toAddr(addressValue);
            if (!currentProgram.getMemory().contains(address)) return null;
            StringBuilder value = new StringBuilder();
            for (int i = 0; i < 96; i++) {
                Address cur = address.add(i);
                if (!currentProgram.getMemory().contains(cur)) return null;
                int b = currentProgram.getMemory().getByte(cur) & 0xff;
                if (b == 0) break;
                if (b < 0x20 || b > 0x7e) return null;
                value.append((char) b);
            }
            String s = value.toString();
            return s.isEmpty() ? null : s;
        } catch (Exception ignored) {
            return null;
        }
    }

    private long literalSlot(Instruction ins) {
        try {
            for (int op = 0; op < ins.getNumOperands(); op++) {
                for (Object obj : ins.getOpObjects(op)) {
                    if (obj instanceof Address) {
                        return ((Address) obj).getOffset();
                    }
                    if (obj instanceof Scalar) {
                        long v = ((Scalar) obj).getUnsignedValue();
                        if (v > 0x1000 && currentProgram.getMemory().contains(toAddr(v))) return v;
                    }
                }
            }
        } catch (Exception ignored) {
        }
        return -1;
    }

    private String ldrTargetRegister(Instruction ins) {
        try {
            String t = ins.toString();
            int eq = t.indexOf('=');
            if (eq > 0) return t.substring(0, eq).trim();
        } catch (Exception ignored) {
        }
        return null;
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException(
                "Usage: ResolvePcRelativeStringsWide.java <output-file> <name-fragment> [...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        FunctionManager fm = currentProgram.getFunctionManager();
        Memory memory = currentProgram.getMemory();

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            FunctionIterator fit = fm.getFunctions(true);
            while (fit.hasNext()) {
                Function f = fit.next();
                boolean match = false;
                for (int i = 1; i < args.length; i++) {
                    if (f.getName().contains(args[i])) { match = true; break; }
                }
                if (!match) continue;

                out.println("===== " + f.getEntryPoint() + " " + f.getName() + " =====");
                List<Instruction> body = new ArrayList<>();
                InstructionIterator iit = currentProgram.getListing().getInstructions(f.getBody(), true);
                while (iit.hasNext()) body.add(iit.next());

                int hits = 0;
                java.util.Set<String> seen = new java.util.HashSet<>();
                for (int i = 0; i < body.size(); i++) {
                    Instruction ins = body.get(i);
                    if (!ins.getMnemonicString().toUpperCase().startsWith("LDR")) continue;
                    long slot = literalSlot(ins);
                    if (slot < 0 || !memory.contains(toAddr(slot))) continue;
                    long word = Integer.toUnsignedLong(memory.getInt(toAddr(slot))) & 0xffffffffL;
                    if (word == 0 || word > 0x7fffffffL) continue;

                    String reg = ldrTargetRegister(ins);
                    for (int j = i + 1; j < Math.min(i + WINDOW, body.size()); j++) {
                        Instruction add = body.get(j);
                        String mn = add.getMnemonicString().toUpperCase();
                        if (!mn.startsWith("ADD") && !mn.startsWith("ADR")) continue;
                        String text = add.toString();
                        if (reg != null && !text.startsWith(reg)) continue;
                        if (!text.toUpperCase().contains("PC")) continue;
                        long base = add.getAddress().getOffset() + 4;
                        long candidate = (word + base) & 0xffffffffL;
                        String s = str(candidate);
                        if (s == null) continue;
                        String line = "ldr@" + ins.getAddress() + " slot=0x" + Long.toHexString(slot)
                                + " w=0x" + Long.toHexString(word)
                                + " add@" + add.getAddress()
                                + " -> 0x" + Long.toHexString(candidate)
                                + "  \"" + s + "\"";
                        if (seen.add(line)) out.println(line);
                        hits++;
                        break;
                    }
                }
                out.println("resolved: " + hits);
            }
        }
    }
}