// Decompile the function containing a given address, creating it if the
// auto-analysis never made one.
//
//   DecompileAtAddress.java <output-file> <hex-address> [<hex-address> ...]
//
// Some functions exist in the program but were never named, so the name-based
// decompiler cannot select them. This takes an address instead, calls
// createFunction if needed, and decompiles whatever it finds.

import java.io.File;
import java.io.PrintWriter;

import ghidra.app.decompiler.DecompInterface;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionManager;

public class DecompileAtAddress extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Usage: DecompileAtAddress.java <output-file> <hex-address> [...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        FunctionManager fm = currentProgram.getFunctionManager();
        DecompInterface decompiler = new DecompInterface();
        decompiler.openProgram(currentProgram);

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            for (int i = 1; i < args.length; i++) {
                long value = Long.parseLong(args[i].replace("0x", ""), 16);
                Address address = toAddr(value);
                Function f = fm.getFunctionContaining(address);
                if (f == null) {
                    f = createFunction(address, null);
                }
                if (f == null) {
                    out.println("===== " + args[i] + " <no function> =====");
                    continue;
                }
                out.println("===== " + args[i] + " " + f.getName()
                        + " @ " + f.getEntryPoint() + " =====");
                DecompileResults result = decompiler.decompileFunction(f, 120, monitor);
                if (result.getDecompiledFunction() == null) {
                    out.println("[DECOMPILATION FAILED] " + result.getErrorMessage());
                } else {
                    out.println(result.getDecompiledFunction().getC());
                }
            }
        } finally {
            decompiler.dispose();
        }
    }
}
