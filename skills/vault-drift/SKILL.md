---
name: vault-drift
description: Read six numbers that say whether a markdown vault's filing has drifted (folders per hundred notes, orphan share, navigation lines, thin folders, notes buried too deep, archives parked inside live work) and point at the exact paths to fix.  Use for a vault health check, folder sprawl, orphan notes, or as the acceptance test after a reorganization.
argument-hint: "[--list thin|deep|archives|orphans]"
---

# Vault Drift

An agent can navigate any mess.  Your head cannot.  So the mess needs to be a number you can read, not a feeling you get.

This skill walks a plain-markdown vault (Obsidian or anything else) and reports six numbers, each with a ceiling.  Under every ceiling: the filing is fine, go do real work.  Over one: it names the paths, you fix only those, you run it again.  **Over a ceiling is a cleanup, not a redesign.**

Python 3.9 or later, standard library only, no network, read-only.

## Run it

From the vault root:

```bash
python3 ${CLAUDE_SKILL_DIR}/audit_vault.py
python3 ${CLAUDE_SKILL_DIR}/audit_vault.py --list orphans
```

Or point at it: `--vault <path>`.  Add `--append <file>` to log the table to a note (a vault MAP or a health log), newest last, so readings build a history.

Run it monthly, and after every step of a reorganization, where it doubles as the acceptance test for that step.

## The six numbers

| Number | Default ceiling | What it counts |
|---|---|---|
| Folders per hundred notes | 10 | Folders (not `.Sources` / `.Specs` slots) divided by every note |
| Live notes with no inbound link | 25 percent | Share of live notes no other note links to |
| Navigation lines | 150 | Total length of your navigation files (`CONTROL PANEL.md`, `AGENTS.md`, `CLAUDE.md`) |
| Folders under fifteen notes | 0 | Folders too small to have earned their existence |
| Notes deeper than four levels | 0 | Anything below zone / project / slot / file |
| Archive folders inside live projects | 0 | `_Archive.*` folders that should have gone to the root `ARCHIVE/` |

**Definitions.**  *Live* means not under the root `ARCHIVE/` and not in any `_Archive.*` folder.  A *project* is a folder holding a `_<NAME> MAP.md`, or any direct child of a zone.  A *zone* is a numbered top-level folder (`00 SYSTEM`, `01 SELF`), plus `PARKED/`.  Folders holding code count as apps, so they and everything under them skip the size and depth rules.  Links resolve by filename, wikilinks and markdown links both, so two notes sharing a name are one target.  Top-level folders starting with `_` (an agent sandbox, a drafts folder) and attachment folders (`Attachments`, `assets`) skip the size rule.

## Make it yours

Everything tunable sits in one `SETTINGS` block at the top of `audit_vault.py`: the six ceilings, the size threshold, the depth cap, what counts as a zone, your archive names, your navigation files, data stores (folders queried like a database, such as a contact list, which sit outside the orphan count), and carve-outs (folders you have deliberately named as exceptions).

The defaults come from one person's vault, and they fit the vault spec this skill ships alongside.  They are a starting position, not a law.  Take a first reading, then set each ceiling where things actually started to hurt.  If a number stays over across runs and every path it names is one you want, the ceiling was wrong for your vault: change it on purpose, and write down why.

## When a number is over

1. Run `--list` for that number.
2. Fix only the paths it names: merge a thin folder into its parent, move an old archive to the root `ARCHIVE/`, link an orphan from its project MAP or delete it.
3. Run it again.

Never answer an over-ceiling reading by adding structure.  Subtract first.

## What This Skill Does NOT Do

- Move, rename, or delete anything.  It reads and reports; you fix.
- Judge content.  It measures filing, not whether a note is any good.
- Require Obsidian, plugins, or a database.  It walks plain folders.
- Make network calls or send your vault anywhere.

## Changelog

- **v1.0 (2026-11-14).**  First open edition.  The structure check from a private vault diagnostic, with the vault-specific names moved into one settings block.  Matches the private version's readings exactly on the source vault, and also resolves markdown-style and percent-encoded links.
