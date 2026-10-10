import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.Listing;
import ghidra.program.model.symbol.Reference;

public class ghidra_area_xrefs extends GhidraScript {
    @Override
    public void run() throws Exception {
        println("program=" + currentProgram.getName());
        println("imageBase=" + currentProgram.getImageBase());
        Listing listing = currentProgram.getListing();
        Address[] candidates = {
            toAddr("0x1d6c017"), toAddr("0x1d7c017"),
            toAddr("0x1d6c017"), toAddr("0x1d6c017"),
            toAddr("0xb73980"), toAddr("0xb73802")
        };
        for (Address target : candidates) {
            println("TARGET " + target + " defined=" + (listing.getDataAt(target) != null));
            Reference[] refs = getReferencesTo(target);
            for (Reference ref : refs) {
                Function function = listing.getFunctionContaining(ref.getFromAddress());
                println("REF " + ref.getFromAddress() + " type=" + ref.getReferenceType()
                    + " function=" + (function == null ? "<none>" : function.getName()));
            }
        }
    }
}
