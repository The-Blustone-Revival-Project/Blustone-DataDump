"""Dump the full decoded text of LEVELING.jet's readable resources so any
level / equipment curve inside can be read verbatim.

Read-only.
"""

from __future__ import annotations

import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(HERE)))))
sys.path.insert(0, os.path.join(REPO, "tools", "extract", "jet-viewer"))

from jet_decoder import inflate_jet_resources  # noqa: E402

JET = os.path.join(REPO, "local", "inputs", "extracted", "assets", "LEVELING.jet")


def main() -> None:
    data = open(JET, "rb").read()
    resources = inflate_jet_resources(data)
    out = []
    for index, (offset, payload, chunks) in enumerate(resources):
        text = payload.decode("utf-8", errors="replace")
        printable = sum(1 for b in payload if 9 <= b <= 13 or 32 <= b <= 126)
        if printable / max(1, len(payload)) < 0.7:
            out.append("")
            out.append("### [%02d] +%08x  NON-TEXT (%d B, print ratio %.2f) head=%r"
                       % (index, offset, len(payload), printable / max(1, len(payload)), payload[:16]))
            continue
        out.append("")
        out.append("### [%02d] +%08x  %d B  (chunks=%d)" % (index, offset, len(payload), chunks))
        out.append(text[:16000])
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "leveling-jet-text.txt")
    with io.open(dest, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(out) + "\n")
    print("wrote", dest)


if __name__ == "__main__":
    main()
