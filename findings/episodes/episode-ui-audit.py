"""Read-only active LevelDB Episode audit; writes only companion JSON evidence.

No LevelDB open/lock/compaction: SST/Snappy, active MANIFEST and WAL parsed in memory.
Run from any cwd with Python3. Original database files are never written.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import struct
import xml.etree.ElementTree as ET

REPO = Path(__file__).resolve().parents[2]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, REPO / relative)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


sst = module("episode_sst", "tools/inspect-leveldb.py")
log = module("episode_log", "tools/read-leveldb-log.py")


def snappy(data):
    length, pos = sst.varint(data, 0)
    out = bytearray()
    while pos < len(data):
        tag = data[pos]
        pos += 1
        kind = tag & 3
        if kind == 0:
            count = tag >> 2
            if count < 60:
                count += 1
            else:
                width = count - 59
                count = int.from_bytes(data[pos:pos + width], "little") + 1
                pos += width
            out.extend(data[pos:pos + count])
            pos += count
        else:
            if kind == 1:
                count = 4 + ((tag >> 2) & 7)
                offset = ((tag & 224) << 3) | data[pos]
                pos += 1
            else:
                width = 2 if kind == 2 else 4
                count = 1 + (tag >> 2)
                offset = int.from_bytes(data[pos:pos + width], "little")
                pos += width
            if offset <= 0 or offset > len(out):
                raise ValueError("Invalid Snappy copy")
            for _ in range(count):
                out.append(out[-offset])
    if len(out) != length:
        raise ValueError("Snappy length mismatch")
    return bytes(out)


def block(data, offset, size):
    compression = data[offset + size]
    payload = data[offset:offset + size]
    if compression == 0:
        return payload
    if compression == 1:
        return snappy(payload)
    raise ValueError(f"Unsupported SST compression {compression}")


def files_hash(root):
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.iterdir()) if p.is_file()}


def read_database(root):
    files, log_number, previous_log = set(), 0, 0
    manifest_name = (root / "CURRENT").read_text().strip()

    def field(data, pos):
        length, pos = sst.varint(data, pos)
        return data[pos:pos + length], pos + length

    for record in log.write_batches((root / manifest_name).read_bytes()):
        pos = 0
        while pos < len(record):
            tag, pos = sst.varint(record, pos)
            if tag == 1:
                _, pos = field(record, pos)
            elif tag in (2, 3, 4, 9):
                value, pos = sst.varint(record, pos)
                if tag == 2:
                    log_number = value
                if tag == 9:
                    previous_log = value
            elif tag == 5:
                _, pos = sst.varint(record, pos)
                _, pos = field(record, pos)
            elif tag == 6:
                _, pos = sst.varint(record, pos)
                number, pos = sst.varint(record, pos)
                files.discard(number)
            elif tag == 7:
                _, pos = sst.varint(record, pos)
                number, pos = sst.varint(record, pos)
                _, pos = sst.varint(record, pos)
                _, pos = field(record, pos)
                _, pos = field(record, pos)
                files.add(number)
            else:
                raise ValueError(f"Unknown MANIFEST tag {tag}")
    rows = {}
    for number in files:
        data = (root / f"{number:06}.ldb").read_bytes()
        footer = data[-48:]
        _, _, pos = sst.handle(footer, 0)
        offset, size, _ = sst.handle(footer, pos)
        for _, value in sst.block_entries(block(data, offset, size)):
            offset, size, _ = sst.handle(value, 0)
            for key, value in sst.block_entries(block(data, offset, size)):
                version = int.from_bytes(key[-8:], "little")
                user_key = key[:-8]
                if user_key not in rows or rows[user_key][0] < version:
                    rows[user_key] = (version, value)
    for number in {log_number, previous_log} - {0}:
        source = root / f"{number:06}.log"
        if not source.exists():
            continue
        for record in log.write_batches(source.read_bytes()):
            sequence = int.from_bytes(record[:8], "little")
            for index, (tag, key, value) in enumerate(log.batch_operations(record)):
                version = ((sequence + index) << 8) | tag
                if key not in rows or rows[key][0] < version:
                    rows[key] = (version, value)
    live = {key.decode("utf8"): value for key, (version, value) in rows.items()
            if version & 255}
    return live, manifest_name, sorted(files), log_number, previous_log


def dependencies(key, value, all_keys):
    """Exact XML attribute values which resolve to another database layout key.

    Also retain file/layout-looking attributes separately: motion/resource IDs
    are not automatically layout dependencies. Native dynamic loads remain external.
    """
    root = ET.fromstring(value.decode("utf-8-sig"))
    locale = key.split("/", 1)[0]
    parent = key.rsplit("/", 1)[0]
    links, candidates = [], []
    for element in root.iter():
        for attribute, raw in element.attrib.items():
            possible = {raw, f"{locale}/{raw}", f"{parent}/{raw}"}
            for target in sorted(possible & all_keys - {key}):
                links.append({"tag": element.tag, "attribute": attribute,
                              "value": raw, "dependency_key": target})
            if any(term in attribute.lower() for term in ("file", "view", "path", "layout", "include")):
                candidates.append({"tag": element.tag, "attribute": attribute, "value": raw})
    return links, candidates


def main():
    sources = [
        "recovered-assets/phone-2026-09-18/private/files/local/UI_XML_RO.db",
        "instrumentation/assets/instrumented-seed-complete-ui-delta-v2/UI_XML_RO.db",
        "instrumentation/assets/instrumented-seed-battle-full-clean/UI_XML_RO.db",
    ]
    result = {"method": "active MANIFEST SST + Snappy + current/previous WAL, tombstone-aware; no DB opens",
              "limits": "CRC checks not performed; dynamic native UI loads are separate from literal XML attributes",
              "sources": []}
    for relative in sources:
        source = REPO / relative
        before = files_hash(source)
        rows, manifest, active, current_log, previous_log = read_database(source)
        episode = []
        for key, value in sorted(rows.items()):
            if "EPISODE" not in key.upper():
                continue
            links, candidates = dependencies(key, value, set(rows))
            episode.append({"key": key, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest(),
                            "direct_dependency_keys": links, "layout_like_attributes": candidates})
        after = files_hash(source)
        if before != after:
            raise RuntimeError(f"Source changed during audit: {relative}")
        result["sources"].append({"path": relative, "live_key_count": len(rows),
                                  "manifest": manifest, "active_sst_numbers": active,
                                  "current_log": current_log, "previous_log": previous_log,
                                  "source_files_sha256_before": before,
                                  "source_files_sha256_after": after,
                                  "source_unchanged": True, "episode_records": episode})
    output = Path(__file__).with_name("episode-ui-layout-inventory.json")
    output.write_text(json.dumps(result, indent=2), encoding="utf8")
    print(output)
    for source in result["sources"]:
        print(source["path"], source["live_key_count"], "Episode records", len(source["episode_records"]),
              "direct XML layout links", sum(len(r["direct_dependency_keys"]) for r in source["episode_records"]))


if __name__ == "__main__":
    main()
