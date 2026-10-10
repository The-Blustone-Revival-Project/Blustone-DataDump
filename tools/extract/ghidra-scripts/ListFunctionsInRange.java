// List every function whose entry point falls inside an address range.
//
//   ListFunctionsInRange.java <output-file> <start-hex> <end-hex> [<start-hex> <end-hex> ...]
//
// Ghidra's demangled names in this binary are truncated to the bare method name
// (e.g. "MakeCamp", "OnInit"), so name fragments cannot be used to tell members
// of one class apart from another. Ranges can: every method of a class lives in
// one contiguous block, so dumping the entry points in a range is how you
// enumerate a class before choosing addresses to decompile.

import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;

public class ListFunctionsInRange extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 3) {
            throw new IllegalArgumentException(
                "Usage: ListFunctionsInRange.java <output-file> <start-hex> <end-hex> [...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("PROGRAM\t" + currentProgram.getName());
            for (int i = 1; i + 1 < args.length; i += 2) {
                long start = Long.parseLong(args[i].replace("0x", ""), 16);
                long end = Long.parseLong(args[i + 1].replace("0x", ""), 16);
                out.println("RANGE\t0x" + Long.toHexString(start) + "\t0x" + Long.toHexString(end));
                Address low = toAddr(start);
                Address high = toAddr(end);
                FunctionIterator it = currentProgram.getFunctionManager().getFunctions(true);
                while (it.hasNext()) {
                    Function f = it.next();
                    Address entry = f.getEntryPoint();
                    if (entry.compareTo(low) < 0 || entry.compareTo(high) > 0) continue;
                    out.println("FUNC\t" + entry + "\t" + f.getName()
                            + "\tbody=" + f.getBody().getNumAddresses());
                }
            }
        }
        println("ListFunctionsInRange done");
    }
}