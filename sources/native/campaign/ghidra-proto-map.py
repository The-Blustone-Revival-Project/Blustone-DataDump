#!/usr/bin/env python3
"""Resolve a Thumb literal-pool load inside a Ghidra instruction dump.

Reads `DumpInstructions.java` output and, for every `ldr rX,[0xSLOT]` followed
by `add rX,pc` and then `str rX,[sp,#N]`, prints

    <str insn>  slot=...  add_pc=...  -> word=...  [sp,#N]

so a `std::function` vtable / member-pointer table entry can be located without
opening Ghidra. `str [sp,#8]` is the offset `local_34` in
`CSRGameBase::OnInitHandle` (0x9cd8a0), which is the second field of the
`std::bind` closure handed to `AddHandle(SR_PROTOCOL, ...)` — i.e. the member
function pointer for that protocol.
"""
from __future__ import annotations

import re
import struct
import sys
from pathlib import Path

BIAS = 0x10000
SO = Path("analysis/extracted/lib/armeabi-v7a/libnative_core.so")

RE_LDR_SLOT = re.compile(r"^([0-9a-f]{8})\s+ldr\s+(r\d+),\[(0x[0-9a-f]+)\]")
RE_ADD_PC = re.compile(r"^([0-9a-f]{8})\s+add\s+(r\d+),pc")
RE_STR_SP = re.compile(r"^([0-9a-f]{8})\s+str\s+(r\d+),\[sp,#(0x[0-9a-f]+)\]")
RE_MOVS_IMM = re.compile(r"^([0-9a-f]{8})\s+movs\s+(r\d+),#(0x[0-9a-f]+)")


def main(dump: str, only_sp: int | None) -> int:
    data = SO.read_bytes()
    pend: dict[str, tuple] = {}
    for line in Path(dump).read_text(encoding="utf8", errors="replace").splitlines():
        m = RE_LDR_SLOT.match(line)
        if m:
            pend[m.group(2)] = ("slot", int(m.group(3), 16))
            continue
        m = RE_ADD_PC.match(line)
        if m and pend.get(m.group(2), ("",))[0] == "slot":
            pend[m.group(2)] = ("add", int(m.group(1), 16), pend[m.group(2)][1])
            continue
        m = RE_MOVS_IMM.match(line)
        if m:
            pend[m.group(2)] = ("imm", int(m.group(3), 16))
            continue
        m = RE_STR_SP.match(line)
        if not m or m.group(2) not in pend:
            continue
        kind = pend[m.group(2)]
        sp = int(m.group(3), 16)
        if only_sp is not None and sp != only_sp:
            continue
        if kind[0] == "add":
            slot = kind[2]
            table = slot + ((kind[1] & ~1) + 4)
            word = struct.unpack_from("<I", data, table - BIAS)[0]
            print(f"{m.group(1)}  slot=0x{slot:x} add=0x{kind[1]:x} "
                  f"-> table=0x{table:x} -> word=0x{word:x}  [sp,#0x{sp:x}]")
        elif kind[0] == "imm":
            print(f"{m.group(1)}  imm=0x{kind[1]:x}  [sp,#0x{sp:x}]")
        pend.pop(m.group(2))
    return 0


if __name__ == "__main__":
    dump = sys.argv[1]
    only = int(sys.argv[2], 0) if len(sys.argv) > 2 else None
    raise SystemExit(main(dump, only))