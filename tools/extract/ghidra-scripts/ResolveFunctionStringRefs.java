// Resolve every PC-relative string reference inside a function.
//
// Thumb compilers materialise a string constant as a literal-pool word holding a
// displacement, added to PC at run time:
//
//     ldr  rX, [pc, #imm]     ; rX = word at the literal pool slot
//     add  rX, pc              ; rX += <address of this insn> + 4
//     mov  rY, rX
//
// Ghidra's C output renders that as `(char *)(DAT_xxxx + 0xyyyy)`, where the
// DAT label is the pool slot and the addend is the ADD's PC - but the pool word
// in the file is a pre-relocation placeholder, so reading it from disk gives
// garbage. Inside Ghidra the value is relocated and correct, which is what this
// script uses.
//
// Rather than reconstruct the exact ADD/ldr pairing (fragile, and the decompiler
// output loses operand detail), this brute-forces the function's own memory: for
// every aligned word W and for both plausible bases (slot, slot+4), it tests
// whether W+base lands on a printable NUL-terminated string. That finds every
// key name the function reads, with no need to model the addressing mode.
//
//   ResolveFunctionStringRefs.java <output-file> <function-name-fragment>

import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.FunctionManager;
import ghidra.program.model.mem.Memory;

public class ResolveFunctionStringRefs extends GhidraScript {

    private static final int MAX_STRING = 64;

    /** Printable ASCII string at address, or null. */
    private String str(long addressValue, int minLen) {
        try {
            Address address = toAddr(addressValue);
            if (!currentProgram.getMemory().contains(address)) return null;
            StringBuilder value = new StringBuilder();
            for (int i = 0; i < MAX_STRING; i++) {
                Address current = address.add(i);
                if (!currentProgram.getMemory().contains(current)) return null;
                int b = currentProgram.getMemory().getByte(current) & 0xff;
                if (b == 0) break;
                if (b < 0x20 || b > 0x7e) return null;
                value.append((char) b);
            }
            String s = value.toString();
            if (s.length() < minLen) return null;
            // Reject things that are obviously code or binary, not identifiers.
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                boolean ok = (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')
                        || (c >= '0' && c <= '9') || c == '_' || c == '.' || c == '/';
                if (!ok) return null;
            }
            return s;
        } catch (Exception ignored) {
            return null;
        }
    }

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException(
                "Usage: ResolveFunctionStringRefs.java <output-file> <name-fragment> [...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        FunctionManager fm = currentProgram.getFunctionManager();
        Memory memory = currentProgram.getMemory();

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            FunctionIterator it = fm.getFunctions(true);
            while (it.hasNext()) {
                Function f = it.next();
                boolean match = false;
                for (int i = 1; i < args.length; i++) {
                    if (f.getName().contains(args[i])) { match = true; break; }
                }
                if (!match) continue;

                out.println("===== " + f.getEntryPoint() + " " + f.getName() + " =====");
                Address start = f.getEntryPoint();
                Address end = f.getBody().getMaxAddress();
                out.println("range " + start + " .. " + end);

                long found = 0;
                for (long off = 0; off < 4096; off += 2) {
                    Address slot = start.add(off);
                    if (slot.compareTo(end) > 0) break;
                    if (!memory.contains(slot)) continue;
                    long word = Integer.toUnsignedLong(memory.getInt(slot)) & 0xffffffffL;
                    if (word == 0 || word > 0x7fffffffL) continue;
                    long[] bases = { slot.getOffset(), slot.getOffset() + 4 };
                    for (long base : bases) {
                        long candidate = (word + base) & 0xffffffffL;
                        if (candidate == 0) continue;
                        String s = str(candidate, 2);
                        if (s == null) continue;
                        out.println("slot 0x" + Long.toHexString(slot.getOffset())
                                + "  w=0x" + Long.toHexString(word)
                                + "  base=" + base
                                + "  -> 0x" + Long.toHexString(candidate)
                                + "  \"" + s + "\"");
                        found++;
                    }
                }
                out.println("candidates: " + found);
            }
        }
    }
}
