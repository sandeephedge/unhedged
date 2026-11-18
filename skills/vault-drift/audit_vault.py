#!/usr/bin/env python3
"""
audit_vault.py: six numbers that say whether a markdown vault's filing has drifted.

Read-only, standard library only, no network.  Prints one markdown table.

    python3 audit_vault.py [--vault PATH] [--list thin|deep|archives|orphans] [--append FILE]

Every number has a ceiling.  Over a ceiling is a cleanup, not a redesign.
Change the SETTINGS block below to fit your vault, and write down why.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote

# ── SETTINGS: make these yours ──────────────────────────────────────────────

CEILINGS = {
    "folders_per_100": 10,   # folders per hundred notes
    "orphan_pct": 25,        # percent of live notes nothing links to
    "nav_lines": 150,        # total lines across your navigation files
    "thin_folders": 0,       # folders below THRESHOLD notes
    "too_deep": 0,           # notes deeper than MAX_DEPTH
    "embedded_archives": 0,  # archive folders inside live projects
}
THRESHOLD = 15               # notes a folder must hold to earn its existence
MAX_DEPTH = 4                # zone / project / slot / file
ZONE_PATTERN = r"^\d\d "     # top-level folders that count as zones ("00 SYSTEM", "01 SELF", ...)
EXTRA_ZONES = {"PARKED"}     # other top-level folders that hold projects
ARCHIVE_ROOT = "ARCHIVE"     # root folder for dead material
ARCHIVE_PREFIX = "_Archive." # archive folder names
EXEMPT_SLOTS = (".Sources", ".Specs")  # folder suffixes allowed at any size
EXEMPT_ROOTS_PREFIX = "_"    # top-level utility folders (_AGENT SANDBOX, drafts) skip the size rule
ATTACHMENT_DIRS = {"Attachments", "attachments", "assets", "_resources"}  # media folders: skip the size rule
CARVE_OUTS: tuple[str, ...] = ()  # name fragments of folders you have logged as exceptions (e.g. (".Transcripts.",))
DATA_STORES: set[str] = set()  # folders queried like a database, not linked (e.g. {"RELATIONSHIPS"})
NAV_FILES = ["CONTROL PANEL.md", "AGENTS.md", "CLAUDE.md"]
MAP_SUFFIX = " MAP.md"       # a folder holding "_<NAME> MAP.md" is a project
SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules"}
CODE_EXT = (".py", ".ts", ".js", ".sh", ".mjs")  # folders with code are apps: exempt from size and depth

# ────────────────────────────────────────────────────────────────────────────

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
MDLINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")


def is_archived(parts: tuple[str, ...]) -> bool:
    return bool(parts) and (parts[0] == ARCHIVE_ROOT or any(p.startswith(ARCHIVE_PREFIX) for p in parts))


def read(root: Path) -> dict:
    zone_re = re.compile(ZONE_PATTERN)
    folders, notes, code = [], [], set()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        rel = Path(dirpath).relative_to(root).parts
        if rel:
            folders.append(rel)
        notes += [rel + (f,) for f in filenames if f.endswith(".md")]
        if any(f.endswith(CODE_EXT) for f in filenames):
            code.add(rel)

    live = [n for n in notes if not is_archived(n[:-1])]
    stem = lambda n: n[-1][:-3].lower()

    inbound: dict[str, int] = {}
    for n in live:
        try:
            text = root.joinpath(*n).read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        targets = {t.strip().split("/")[-1].removesuffix(".md").lower() for t in WIKILINK.findall(text)}
        targets |= {unquote(t).split("/")[-1].removesuffix(".md").lower() for t in MDLINK.findall(text)}
        for t in targets - {stem(n)}:
            inbound[t] = inbound.get(t, 0) + 1

    graph = [n for n in live if not any(p in DATA_STORES for p in n[:-1])]
    orphans = [n for n in graph if stem(n) not in inbound]

    is_zone = lambda name: bool(zone_re.match(name)) or name in EXTRA_ZONES
    has_map = lambda f: any(p.name.startswith("_") and p.name.endswith(MAP_SUFFIX) for p in root.joinpath(*f).iterdir())
    projects = {f for f in folders if (len(f) == 2 and is_zone(f[0]) and "." not in f[1]) or has_map(f)}
    is_app = lambda f: any(f[:i] in code for i in range(1, len(f) + 1))
    notes_under = lambda f: sum(1 for n in notes if n[:len(f)] == f)

    live_folders = [f for f in folders if not is_archived(f)]
    thin = [f for f in live_folders
            if len(f) > 1 and not f[0].startswith(EXEMPT_ROOTS_PREFIX) and f[0] != ARCHIVE_ROOT
            and f not in projects and not f[-1].endswith(EXEMPT_SLOTS)
            and not any(c in f[-1] for c in CARVE_OUTS)
            and not any(p in ATTACHMENT_DIRS for p in f)
            and not is_app(f) and not any(p in DATA_STORES for p in f)
            and notes_under(f) < THRESHOLD]
    deep = [n for n in live if len(n) > MAX_DEPTH and not is_app(n[:-1])]
    embedded = [f for f in folders if f[0] != ARCHIVE_ROOT and f[-1].startswith(ARCHIVE_PREFIX)]
    counted = [f for f in folders if not f[-1].endswith(EXEMPT_SLOTS)]
    nav = sum(len((root / f).read_text(encoding="utf-8", errors="ignore").splitlines())
              for f in NAV_FILES if (root / f).exists())

    fmt = lambda f: "/".join(f) + f"  ({notes_under(f)})"
    return {
        "notes": len(notes), "live": len(live), "folders": len(folders), "counted": len(counted),
        "folders_per_100": round(100 * len(counted) / max(len(notes), 1)),
        "orphan_pct": round(100 * len(orphans) / max(len(graph), 1)),
        "nav_lines": nav, "thin_folders": len(thin), "too_deep": len(deep),
        "embedded_archives": len(embedded),
        "lists": {"thin": [fmt(f) for f in sorted(thin)],
                  "deep": ["/".join(n) for n in sorted(deep)],
                  "archives": [fmt(f) for f in sorted(embedded)],
                  "orphans": ["/".join(n) for n in sorted(orphans)]},
    }


def table(r: dict) -> str:
    rows = [("Folders per hundred notes", "folders_per_100", ""),
            ("Live notes with no inbound link", "orphan_pct", " percent"),
            ("Navigation lines", "nav_lines", ""),
            (f"Folders under {THRESHOLD} notes", "thin_folders", ""),
            (f"Notes deeper than {MAX_DEPTH} levels", "too_deep", ""),
            ("Archive folders inside live projects", "embedded_archives", "")]
    out = [f"### {date.today():%Y-%m-%d} · {r['notes']} notes ({r['live']} live) · "
           f"{r['counted']} of {r['folders']} folders counted", "",
           "| Number | Reading | Ceiling | |", "|---|---|---|---|"]
    for label, k, unit in rows:
        out.append(f"| {label} | {r[k]}{unit} | {CEILINGS[k]}{unit} | {'ok' if r[k] <= CEILINGS[k] else 'over'} |")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Six numbers for vault drift.  Read-only.")
    ap.add_argument("--vault", type=Path, default=Path.cwd(), help="vault root (default: current folder)")
    ap.add_argument("--list", choices=["thin", "deep", "archives", "orphans"], help="print the paths behind one number")
    ap.add_argument("--append", type=Path, help="also append the table to this markdown file")
    a = ap.parse_args()
    root = a.vault.resolve()
    if not root.is_dir():
        print(f"ERROR: {root} is not a folder", file=sys.stderr)
        return 1
    r = read(root)
    if a.list:
        print("\n".join(r["lists"][a.list]) or "(none)")
        return 0
    md = table(r)
    if a.append:
        with a.append.open("a", encoding="utf-8") as fh:
            fh.write("\n" + md)
        print(f"Appended to {a.append}", file=sys.stderr)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
