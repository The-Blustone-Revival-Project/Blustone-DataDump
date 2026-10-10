// Dump the raw instruction listing of a function, or of an explicit address range.
//
//   DumpInstructions.java <output-file> <hex-address> [<hex-address> ...]
//
// Two modes:
//   * one address that lies inside a known function -> the whole function
//   * two addresses where the second is greater   -> the [first, second) range
//
// Why this exists: the decompiler prints a `this + N` offset for a struct
// member only when it has modelled the access. To prove that two functions
// touch the *same* member of a singleton (rather than the decompiler having
// silently dropped the offset in both), read the instructions: the same
// `add rX, r0, #imm` (or the same bare `mov rX, r0`) in both proves identity.
// A decompiled `this` alone proves nothing.

import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.listing.InstructionIterator;

public class DumpInstructions extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException(
                    "Usage: DumpInstructions.java <output-file> <hex-address> [<hex-address> ...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("PROGRAM\t" + currentProgram.getName());
            for (int i = 1; i < args.length; i++) {
                long value = Long.parseLong(args[i].replace("0x", ""), 16);
                Address start = toAddr(value);
                Address end = null;

                if (i + 1 < args.length) {
                    long next = Long.parseLong(args[i + 1].replace("0x", ""), 16);
                    if (next > value) {
                        end = toAddr(next);
                        i++; // consumed the range end
                    }
                }

                if (end == null) {
                    Function f = currentProgram.getFunctionManager().getFunctionContaining(start);
                    if (f == null) {
                        out.println("===== " + args[i] + " <no function> =====");
                        continue;
                    }
                    end = f.getBody().getMaxAddress().next();
                    out.println("===== " + args[i] + " " + f.getName()
                            + " @ " + f.getEntryPoint() + " =====");
                } else {
                    out.println("===== range " + start + " .. " + end + " =====");
                }

                InstructionIterator it = currentProgram.getListing().getInstructions(start, true);
                while (it.hasNext()) {
                    Instruction ins = it.next();
                    if (ins.getAddress().compareTo(end) >= 0) break;
                    out.println(ins.getAddress() + "  " + ins.toString());
                }
            }
        }
        println("DumpInstructions done");
    }
}
