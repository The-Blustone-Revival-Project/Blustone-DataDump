// Exact PC-relative string references for one function.
//
// Thumb materialises a string constant as:
//
//     ldr  rX, [pc, #imm]   ; rX = word from the literal pool slot
//     add  rX, pc            ; rX += (address of this instruction) + 4
//
// This walks the real instructions, takes the literal-pool address Ghidra
// resolves for each LDR, reads the relocated word there, finds the matching
// ADD rX, pc immediately after, and reads the string at word + (addAddr + 4).
// No guessing: the output is the exact key the function uses.
//
//   ResolvePcRelativeStrings.java <output-file> <function-name-fragment> [...]

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
import ghidra.program.model.lang.Register;
import ghidra.program.model.mem.Memory;

public class ResolvePcRelativeStrings extends GhidraScript {

    private String str(long addressValue) {
        try {
            Address address = toAddr(addressValue);
            if (!currentProgram.getMemory().contains(address)) return null;
            StringBuilder value = new StringBuilder();
            for (int i = 0; i < 64; i++) {
                Address cur = address.add(i);
                if (!currentProgram.getMemory().contains(cur)) return null;
                int b = currentProgram.getMemory().getByte(cur) & 0xff;
                if (b == 0) break;
                if (b < 0x20 || b > 0x7e) return null;
                value.append((char) b);
            }
            String s = value.toString();
            if (s.isEmpty()) return null;
            return s;
        } catch (Exception ignored) {
            return null;
        }
    }

    /** Literal-pool address an LDR operand points at, or -1. */
    private long literalSlot(Instruction ins) {
        try {
            for (int op = 0; op < ins.getNumOperands(); op++) {
                for (Object obj : ins.getOpObjects(op)) {
                    if (obj instanceof Address) {
                        return ((Address) obj).getOffset();
                    }
                    // Some Ghidra OSGi script caches omit Scalar's package
                    // export. Preserve its actual numeric operand via reflection
                    // rather than parse display text or guess a pool address.
                    if (obj.getClass().getName().equals("ghidra.program.model.scalar.Scalar")) {
                        long v = ((Number) obj.getClass().getMethod("getUnsignedValue").invoke(obj)).longValue();
                        // A pool slot lives inside the program's loaded image.
                        if (v > 0x1000 && currentProgram.getMemory().contains(toAddr(v))) return v;
                    }
                }
            }
        } catch (Exception ignored) {
        }
        return -1;
    }

    /** Require an actual destination register; display text contains no '='
     * in the normal Thumb listing and previously allowed unrelated ADDs. */
    private String ldrTargetRegister(Instruction ins) {
        try {
            Register reg = ins.getRegister(0);
            if (reg != null) return reg.getName();
        } catch (Exception ignored) {
        }
        return null;
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException(
                "Usage: ResolvePcRelativeStrings.java <output-file> <name-fragment> [...]");
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
                    if (args[i].startsWith("0x")) {
                        if (f.getEntryPoint().getOffset() == Long.parseUnsignedLong(args[i].substring(2),16)) { match = true; break; }
                    } else if (f.getName().contains(args[i])) { match = true; break; }
                }
                if (!match) continue;

                out.println("===== " + f.getEntryPoint() + " " + f.getName() + " =====");
                List<Instruction> body = new ArrayList<>();
                InstructionIterator iit = currentProgram.getListing().getInstructions(f.getBody(), true);
                while (iit.hasNext()) body.add(iit.next());

                int hits = 0;
                for (int i = 0; i < body.size(); i++) {
                    Instruction ins = body.get(i);
                    if (!ins.getMnemonicString().toUpperCase().startsWith("LDR")) continue;
                    long slot = literalSlot(ins);
                    if (slot < 0 || !memory.contains(toAddr(slot))) continue;
                    long word = Integer.toUnsignedLong(memory.getInt(toAddr(slot))) & 0xffffffffL;
                    if (word == 0 || word > 0x7fffffffL) continue;

                    String reg = ldrTargetRegister(ins);
                    if (reg == null) continue;
                    for (int j = i + 1; j < Math.min(i + 13, body.size()); j++) {
                        Instruction add = body.get(j);
                        String mn = add.getMnemonicString().toUpperCase();
                        if (add.getFlowType().isCall() || add.getFlowType().isJump()) break;
                        Register destination = add.getRegister(0);
                        boolean sameDestination = destination != null && destination.getName().equals(reg);
                        boolean usesPc = false;
                        for (int op = 1; op < add.getNumOperands(); op++) {
                            for (Object operand : add.getOpObjects(op)) {
                                if (operand instanceof Register && ((Register) operand).getName().equalsIgnoreCase("pc")) usesPc = true;
                            }
                        }
                        if (!mn.startsWith("ADD") || !sameDestination || !usesPc) {
                            boolean clobbered = false;
                            for (Object result : add.getResultObjects()) {
                                if (result instanceof Register && ((Register) result).getName().equals(reg)) clobbered = true;
                            }
                            if (clobbered) break;
                            continue;
                        }
                        long base = add.getAddress().getOffset() + 4;
                        long candidate = (word + base) & 0xffffffffL;
                        String s = str(candidate);
                        if (s == null) break; // the loaded value was already consumed by this ADD
                        out.println("ldr@" + ins.getAddress() + " slot=0x" + Long.toHexString(slot)
                                + " w=0x" + Long.toHexString(word)
                                + " add@" + add.getAddress()
                                + " -> 0x" + Long.toHexString(candidate)
                                + "  \"" + s + "\"");
                        hits++;
                        break;
                    }
                }
                out.println("resolved: " + hits);
            }
        }
    }
}
