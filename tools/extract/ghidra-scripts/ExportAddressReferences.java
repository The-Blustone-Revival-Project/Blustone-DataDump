// Read-only reference export for exact relocated addresses, avoiding ambiguous
// template names. Usage: <output-file> <hex-address> [...].
import java.io.File;
import java.io.PrintWriter;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;

public class ExportAddressReferences extends GhidraScript {
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) throw new IllegalArgumentException("output and addresses required");
        try (PrintWriter out = new PrintWriter(new File(args[0]), "UTF-8")) {
            for (int i = 1; i < args.length; i++) {
                Address target = toAddr(Long.parseLong(args[i].replace("0x", ""), 16));
                out.println("TARGET " + target);
                for (Reference ref : currentProgram.getReferenceManager().getReferencesTo(target)) {
                    Function caller = currentProgram.getFunctionManager().getFunctionContaining(ref.getFromAddress());
                    out.println("REF " + ref.getFromAddress() + " " + ref.getReferenceType() + " "
                        + (caller == null ? "<no-function>" : caller.getEntryPoint() + " " + caller.getName()));
                }
            }
        }
    }
}
