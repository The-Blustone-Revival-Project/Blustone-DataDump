"""Decode public CDN metadata from private host copies without opening LevelDB.

Only header stamp/count/size and stamp histograms leave the private directory.
No account fields, arbitrary decoded values, database writes, or app calls.
Live native provider binding must be established separately.
"""
from pathlib import Path
import importlib.util
import json
import sys

REPO = Path(__file__).resolve().parents[2]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, REPO / relative)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def audit(root):
    root = root.resolve()
    if not root.is_relative_to(REPO / "recovered-assets"):
        raise ValueError("Use a private recovered-assets host copy only")
    reader = module("cdn_readonly_tables", "analysis/research/episode-ui-audit.py")
    decoder = module("cdn_decode", "analysis/recovered-investigation-2026-09-19/scripts/decode_local_state.py")
    rows, manifest, files, current_log, previous_log = reader.read_database(root)
    key = decoder.btea_key()
    result = {"live_binding_required_separately": True, "live_keys": len(rows),
              "manifest": manifest, "active_sst": files, "current_log": current_log,
              "previous_log": previous_log, "header": {}, "item_stamp_histogram": {},
              "pvc_stamp_histogram": {}, "decode_errors": 0}
    for name in ("stamp", "cnt", "size"):
        payload = rows.get("CDN/header/" + name)
        if payload is None:
            result["header"][name] = {"value": None, "error": "missing"}
            continue
        value, error = decoder.decode_value(payload, key)
        if error is None and (type(value) is not int or value < 0):
            value, error = None, "not-unsigned-integer"
        result["header"][name] = {"value": value if error is None else None, "error": error}
    for prefix, field in (("CDN/header/items/", "item_stamp_histogram"),
                          ("CDN/PVC/", "pvc_stamp_histogram")):
        for name, payload in rows.items():
            if name.startswith(prefix) and name.endswith("/stamp"):
                value, error = decoder.decode_value(payload, key)
                if error or type(value) is not int or value < 0:
                    result["decode_errors"] += 1
                else:
                    label = str(value)
                    result[field][label] = result[field].get(label, 0) + 1
    result["backslash_header_stamp_present"] = "CDN/header\\stamp" in rows
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: audit-cdn-cache-metadata.py <private-host-copy>")
    print(json.dumps(audit(Path(sys.argv[1])), indent=2))
