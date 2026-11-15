# unhedged

The things I build for my own work with AI, cleaned up so they run for anyone: skills, workflows, and the architecture underneath them.

Everything here is a plain markdown file you can read in a few minutes.  No install step is required: paste a file into any AI chat and it works for that conversation.  Each one also explains how to install it properly if you want to keep it.

## Skills

| Skill | What it does |
|---|---|
| [feynman](skills/feynman/) | Teaches you anything one concept at a time.  You explain each one back with the source closed, and it patches only the exact spot you went vague. |

## Architecture

| File | What it is |
|---|---|
| [VAULT-SPEC.md](architecture/VAULT-SPEC.md) | A template for structuring a plain-markdown notes vault that you and your AI agents share.  Paste it into any AI and it interviews you, then writes your version. |

## Installing a skill

- **Any AI:** paste the skill's `SKILL.md` into a chat.
- **Claude Code:** copy the skill's folder to `~/.claude/skills/<name>/`, then run `/<name>`.
- **Claude.ai:** upload the folder under Settings, Skills.

## How this repo works

Each piece carries its own version and changelog at the bottom of the file.  I don't take pull requests.  The cores stay small on purpose.  Fork anything and bend it to your own work.

Longer write-ups on why each one exists live in my Field Notes at [digitalaleph.com](https://www.digitalaleph.com).

## License

MIT-0.  Use any of it however you like.  No credit needed.
