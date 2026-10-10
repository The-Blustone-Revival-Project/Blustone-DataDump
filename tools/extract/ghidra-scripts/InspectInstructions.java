// InspectInstructions.java <output-file> <hex-address> [...]
//
// Prints, for each address: the raw program bytes, the length Ghidra thinks the
// instruction is, and the mnemonic Ghidra produced.
//
// Why this exists: a project note claimed Ghidra = ELF + 0x10000 and a hand
// re-decode of the same halfwords disagreed. This script puts the program's own
// bytes and the disassembler's own answer side by side, so the disagreement can
// be attributed to the file or to the reader instead of being argued about.

import java.io.File;
import java.io.PrintWriter;

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.listing.Instruction;
import ghidra.program.model.mem.Memory;

public class InspectInstructions extends GhidraScript {
    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException(
                    "Usage: InspectInstructions.java <output-file> <hex-address> [...]");
        }
        File outputFile = new File(args[0]);
        if (outputFile.getParentFile() != null) outputFile.getParentFile().mkdirs();

        Memory memory = currentProgram.getMemory();
        try (PrintWriter out = new PrintWriter(outputFile, "UTF-8")) {
            out.println("PROGRAM\t" + currentProgram.getName());
            out.println("IMAGE_BASE\t" + currentProgram.getImageBase());
            for (int i = 1; i < args.length; i++) {
                long value = Long.parseLong(args[i].replace("0x", ""), 16);
                Address address = toAddr(value);
                StringBuilder hex = new StringBuilder();
                int len = 0;
                Instruction ins = currentProgram.getListing().getInstructionAt(address);
                if (ins != null) len = ins.getLength();
                if (len == 0) len = 4;
                for (int b = 0; b < len; b++) {
                    hex.append(String.format("%02x", memory.getByte(address.add(b)) & 0xff));
                }
                String mnem = ins == null ? "<no instruction>" : ins.toString();
                out.println("ADDR\t" + address + "\tbytes=" + hex + "\tlen=" + len + "\t" + mnem);
            }
        }
        println("InspectInstructions: wrote " + (args.length - 1) + " rows");
    }
}