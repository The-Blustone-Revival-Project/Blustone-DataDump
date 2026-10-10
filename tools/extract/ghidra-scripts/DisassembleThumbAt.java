// Transient branch disassembly for a -readOnly headless project.
// Usage: DisassembleThumbAt.java <G-address> [...]
import java.math.BigInteger;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.Address;
import ghidra.program.model.lang.Register;

public class DisassembleThumbAt extends GhidraScript {
    public void run() throws Exception {
        Register thumb = currentProgram.getRegister("TMode");
        if (thumb == null) throw new IllegalStateException("Missing ARM TMode context");
        for (String arg : getScriptArgs()) {
            Address address = toAddr(Long.parseLong(arg.replace("0x", ""), 16));
            if (currentProgram.getListing().getInstructionAt(address) == null)
                currentProgram.getProgramContext().setValue(thumb, address, address, BigInteger.ONE);
            println(address + " disassembled=" + disassemble(address));
        }
    }
}
