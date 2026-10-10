import java.io.File;
import java.io.PrintWriter;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.symbol.Symbol;
import ghidra.program.model.symbol.SymbolIterator;
import ghidra.program.model.address.Address;

/** Read relocated primary Itanium vtable slots; never modifies program memory. */
public class ExportVtableSlots extends GhidraScript {
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 3) throw new IllegalArgumentException("output exact-vtable-symbol-or-0x-address slot-hex [...]");
        Address requested = args[1].matches("0x[0-9a-fA-F]+") ? toAddr(Long.parseLong(args[1].substring(2),16)) : null;
        File file = new File(args[0]);
        if (file.getParentFile() != null) file.getParentFile().mkdirs();
        try (PrintWriter out = new PrintWriter(file, "UTF-8")) {
            SymbolIterator symbols = currentProgram.getSymbolTable().getAllSymbols(true);
            int matches = 0;
            java.util.Set<Address> seen = new java.util.HashSet<>();
            while (symbols.hasNext()) {
                Symbol symbol = symbols.next();
                String name = symbol.getName(true);
                if (!(requested != null ? symbol.getAddress().equals(requested) :
                    (name.equals(args[1]) || symbol.getName().equals(args[1]))) ||
                    !(symbol.getName().equals("vtable") || symbol.getName().startsWith("_ZTV"))) continue;
                if (!seen.add(symbol.getAddress())) continue;
                if (++matches > 10) throw new IllegalStateException("Ambiguous vtable fragment");
                Address table = symbol.getAddress();
                out.println(name + " table=" + table + " primary-address-point=" + table.add(8));
                for (int i = 2; i < args.length; i++) {
                    int slot = Integer.parseInt(args[i].replace("0x", ""), 16);
                    if (slot < 0 || slot > 0x400 || slot % 4 != 0) throw new IllegalArgumentException("Bounded aligned slot required");
                    Address at = table.add(8 + slot);
                    long raw = Integer.toUnsignedLong(currentProgram.getMemory().getInt(at));
                    Address target = toAddr(raw & ~1L);
                    out.println("slot=" + Integer.toHexString(slot) + " at=" + at + " raw=" + Long.toHexString(raw) +
                        " function=" + currentProgram.getFunctionManager().getFunctionAt(target));
                }
            }
            out.println("matches=" + matches);
        }
    }
}
