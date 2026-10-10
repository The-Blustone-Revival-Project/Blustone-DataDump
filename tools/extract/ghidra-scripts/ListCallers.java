// List the callers of a function, given its entry address.
//
//   ListCallers.java <output-file> <hex-entry-address>
//
// Knowing the caller is what makes a failing assertion actionable: the caller
// shows which field supplies the value that is asserted empty, which in turn
// shows which response key the replica is getting wrong.

import java.io.File;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;
import ghidra.program.model.symbol.ReferenceIterator;

public class ListCallers extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Usage: ListCallers.java <output-file> <hex-address>");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        long target = Long.parseLong(args[1].replace("0x", ""), 16);
        Address addr = toAddr(target);
        Function callee = currentProgram.getFunctionManager().getFunctionContaining(addr);
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("target 0x" + Long.toHexString(target)
                    + "  function=" + (callee == null ? "<none>" : callee.getName()));
            List<String> callers = new ArrayList<>();
            ReferenceIterator it = currentProgram.getReferenceManager().getReferencesTo(addr);
            while (it.hasNext()) {
                Reference ref = it.next();
                Function from = currentProgram.getFunctionManager()
                        .getFunctionContaining(ref.getFromAddress());
                callers.add("  from 0x" + Long.toHexString(ref.getFromAddress().getOffset())
                        + "  " + (from == null ? "<no function>" : from.getName()));
            }
            for (String c : callers) out.println(c);
            out.println("callers: " + callers.size());
        }
        println("ListCallers done");
    }
}
