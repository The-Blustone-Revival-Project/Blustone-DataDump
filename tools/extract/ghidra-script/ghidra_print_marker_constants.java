import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.mem.Memory;
import ghidra.program.model.listing.Data;

public class ghidra_print_marker_constants extends GhidraScript {
    @Override
    public void run() throws Exception {
        Memory memory = currentProgram.getMemory();
        for (long raw = 0xda105c; raw <= 0xda1088; raw += 4) {
            Address address = toAddr(raw);
            int value = memory.getInt(address);
            Data data = currentProgram.getListing().getDataAt(address);
            println(String.format("CONST 0x%08x value=0x%08x signed=%d data=%s", raw, value, value, data == null ? "<none>" : data.toString()));
        }
        long[][] pairs = {
            {0xfe67b6L, 0xda0cf8L}, {0xfd8e28L, 0xda0d6cL}, {0xfd199fL, 0xda0ddcL},
            {0xfd52baL, 0xda0e50L}, {0xfd529eL, 0xda0e7eL}, {0xfd5268L, 0xda0eacL},
            {0xfd524eL, 0xda0edaL}, {0xfd523cL, 0xda0f0aL}, {0xfd51f9L, 0xda0f3cL},
            {0x013da430L, 0xda0f84L}, {0x013da444L, 0xda0fb0L}
        };
        for (long[] pair : pairs) {
            long target = pair[0] + pair[1];
            byte[] bytes = new byte[128];
            memory.getBytes(toAddr(target), bytes);
            int length = 0;
            while (length < bytes.length && bytes[length] != 0) length++;
            String value = new String(bytes, 0, length, java.nio.charset.StandardCharsets.UTF_8);
            println(String.format("STRING target=0x%08x value=%s", target, value));
        }
        long[] parseBases = {0xb65bb0L, 0xb65bb4L, 0xb65bb8L, 0xb65bbcL, 0xb65bc0L, 0xb65bc4L};
        long[] parseOffsets = {0xb65878L, 0xb65882L, 0xb65892L, 0xb658b6L, 0xb659b0L, 0xb659e2L};
        for (int i = 0; i < parseBases.length; i++) {
            long base = Integer.toUnsignedLong(memory.getInt(toAddr(parseBases[i])));
            long target = base + parseOffsets[i];
            byte[] bytes = new byte[128];
            memory.getBytes(toAddr(target), bytes);
            int length = 0;
            while (length < bytes.length && bytes[length] != 0) length++;
            println(String.format("PARSE_STRING base=0x%08x ptr=0x%08x target=0x%08x value=%s", parseBases[i], base, target,
                new String(bytes, 0, length, java.nio.charset.StandardCharsets.UTF_8)));
        }
    }
}
