# -*- coding: utf-8 -*-
"""Render namu.wiki pages with local headless Edge and dump the rendered DOM.

Read-only with respect to the workspace: writes only into a temp directory.
Positive control is run by the caller before any zero is recorded.
"""
import os
import re
import subprocess
import sys
import tempfile

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


def render(url, budget_ms=25000, profile=None, extra_args=()):
    prof = profile or tempfile.mkdtemp(prefix="namu-edge-")
    cmd = [
        EDGE,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--hide-scrollbars",
        "--window-size=1600,2400",
        "--user-agent=" + UA,
        "--user-data-dir=" + prof,
        "--virtual-time-budget=%d" % budget_ms,
        "--run-all-compositor-stages-before-draw",
        "--dump-dom",
    ]
    cmd.extend(extra_args)
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True, timeout=240)
    out = p.stdout.decode("utf-8", "replace")
    err = p.stderr.decode("utf-8", "replace")
    return out, err, p.returncode, prof


def visible_text(html):
    """Strip script/style then tags, so we can size the article cheaply."""
    body = html
    m = re.search(r"<body\b.*?>(.*)</body>", body, re.S | re.I)
    if m:
        body = m.group(1)
    body = re.sub(r"(?is)<(script|style|noscript)\b.*?</\1>", " ", body)
    body = re.sub(r"(?s)<[^>]+>", " ", body)
    body = (body.replace("&nbsp;", " ").replace("&amp;", "&")
                .replace("&lt;", "<").replace("&gt;", ">").replace("&#39;", "'")
                .replace("&quot;", '"'))
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n\s*\n+", "\n", body)
    return body.strip()


def main():
    url = sys.argv[1]
    out_path = sys.argv[2]
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else 25000
    html, err, rc, prof = render(url, budget_ms=budget)
    txt = visible_text(html)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(html)
    print("rc=%d html_bytes=%d visible_chars=%d tables=%d profile=%s"
          % (rc, len(html), len(txt), html.lower().count("<table"), prof))
    print("ERR_TAIL:", err.strip().replace("\n", " | ")[-800:])
    print("TEXT_HEAD:", txt[:600])


if __name__ == "__main__":
    main()
