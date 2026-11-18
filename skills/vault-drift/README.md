# Vault Drift

Six numbers that tell you whether your notes vault is getting messy.

I kept reorganizing my vault because it *felt* messy.  New top level, new folder scheme, a weekend gone, and a month later it felt messy again.  An agent can find its way through any mess.  My head can't.  So I stopped trusting the feeling and started measuring.  Now "is it a mess?" is a reading, not a mood.

## What it measures

| Number | Default ceiling |
|---|---|
| Folders per hundred notes | 10 |
| Notes nothing links to | 25 percent |
| Lines across your navigation files (`CONTROL PANEL.md`, `AGENTS.md`, `CLAUDE.md` by default) | 150 |
| Folders too small to earn their place (under fifteen notes) | 0 |
| Notes buried deeper than four levels | 0 |
| Archive folders parked inside live projects | 0 |

Under every ceiling: your filing is fine, go do real work.  Over one: it names the exact paths, you fix only those, you run it again.  **Over a ceiling is a cleanup, not a redesign.**

## Sample reading

Run against Obsidian's own public help vault:

```
### 2026-11-14 · 180 notes (180 live) · 22 of 22 folders counted

| Number | Reading | Ceiling | |
|---|---|---|---|
| Folders per hundred notes | 12 | 10 | over |
| Live notes with no inbound link | 4 percent | 25 percent | ok |
| Navigation lines | 0 | 150 | ok |
| Folders under 15 notes | 1 | 0 | over |
| Notes deeper than 4 levels | 0 | 0 | ok |
| Archive folders inside live projects | 0 | 0 | ok |
```

Then `--list thin` names the one folder behind that reading: `Bases/Layouts  (5)`.

## How to use it

Python 3.9 or later.  No packages, no network, read-only.  It never moves or deletes anything.

```bash
python3 audit_vault.py --vault ~/path/to/vault
python3 audit_vault.py --vault ~/path/to/vault --list orphans
python3 audit_vault.py --vault ~/path/to/vault --append ~/path/to/vault/"Health Log.md"
```

**As a skill:** put this folder at `~/.claude/skills/vault-drift/` for Claude Code (or upload it under Settings, Skills on Claude.ai) and ask for a vault drift reading.

Run it monthly, and after every step of a reorganization.  There it doubles as the test that the step is done.

## Make it yours

Every setting sits in one block at the top of `audit_vault.py`: the six ceilings, the size threshold, the depth cap, what counts as a top-level zone, your archive and attachment folders, your navigation files, and any folders you've deliberately made exceptions.

The defaults come from my vault.  They are a starting position, not a law.  Take a first reading, then set each ceiling where things actually started to hurt for you.  If a number stays over and every path it names is one you want, the ceiling was wrong for your vault.  Change it on purpose, and write down why.

It pairs with my [vault spec](../../architecture/VAULT-SPEC.md), a template for structuring the vault in the first place.  The spec says what shape to keep.  This tells you when you've drifted from it.

## License

MIT-0.  Use it however you like.  No credit needed.
