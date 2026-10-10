import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.symbol.Reference;

public class ghidra_marker_xrefs extends GhidraScript {
    @Override
    public void run() throws Exception {
        long[] targets = {0x1d874aeL, 0x1d79b94L, 0x1d7277bL, 0x1d7610aL, 0x1d7611cL, 0x1d76114L, 0x1d76128L, 0x1d76146L, 0x1d76135L, 0x1d7bec9L, 0x1d7bed3L, 0x1d7bee0L};
        for (long raw : targets) {
            Address target = toAddr(raw);
            println("TARGET " + target + "");
            for (Reference ref : getReferencesTo(target)) {
                Function function = currentProgram.getListing().getFunctionContaining(ref.getFromAddress());
                println("REF " + ref.getFromAddress() + " function=" + (function == null ? "<none>" : function.getName()));
            }
        }
    }
}
