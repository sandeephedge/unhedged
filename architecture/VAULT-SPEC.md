---
created: 2026-11-10
updated: 2026-11-14
---

# VAULT SPEC (public template)

*A canonical structure for a plain-markdown knowledge vault, the operating contract for any agent that reads or writes it, and the rebuild artifact for reconstructing it from scratch.  This file obeys its own invariants: it is the format it prescribes.*

This is a template, not a product.  It is the compiled result of Sandeep Ramesh's personal knowledge vault restructure, with the personal naming stripped out but the reasoning left in.  Do not adopt it as-is.  The parts that make it work are the parts you decide for yourself.

## How to use this.

Paste this whole file into an LLM with a prompt like:

> Here is a vault spec template.  Interview me about my actual life and work, then rewrite it as MY spec.  Ask me about: (1) the zones, what the six to eight top-level divisions of my world actually are, by relationship to me; (2) what I already have, how many notes, where the mess is; (3) what I build versus what I only think about; (4) which agents or tools touch my files.  Then hand me back the filled-in spec plus a migration plan.  Challenge the defaults where my situation differs.  Do not keep a placeholder I have not answered for.

Five decisions are yours and nobody else's.  Everything marked **DECIDE** below is one of them.

1. **Your zones.**  The six names here are placeholders.  The invariant is the shape (a small, frozen set of top-level divisions keyed to your relationship to the thing), never the words.
2. **Your folder threshold.**  Fifteen is a dial, set by one operator's note counts.  Yours may be eight or forty.
3. **Your slot names.**  Three worked here after a count showed the others sat near-empty.  Run the count on your own vault before you trust the number three.
4. **Your house format.**  The frontmatter minimalism, the punctuation rules, the casing: these are taste with a reason attached.  Keep the reason, change the taste.
5. **Your carve-outs.**  Every real vault has one or two places where the grammar does not fit.  Name them explicitly in the decisions log rather than letting them spread.

What you should probably not change on day one: the invariant/extension distinction, the raw-versus-derived split, the agent quarantine surface, and the substrate/runtime boundary.  Those are the key ideas.  The folder names are decoration.

## The Motivation.

Files outlive apps.  Plain markdown you own, synced across every device and every operating system you use, is the one substrate that survives every tool change; the editor (Obsidian, or whatever you prefer) is just the current lens on it.

Most personal systems drift into a Frankenstein: overlapping specs, stale conventions, a top level that keeps getting re-cut.  The cost is human cognitive overload, not machine failure.  An agent navigates any mess; your head cannot.  So the fix is a canonical top-level spec: a minimal core that never moves, plus rules for growing by leaves.

The vault holds settled state, the compiled present, alongside the sanctioned capture surfaces that stage raw inflow toward it.  A loop does the compiling: it turns raw material (sources, transcripts, calls) into that state.  What the vault does not become is a parallel task manager that duplicates state across checkbox files (see Non-Goals).

## The Core (invariant, do not reorganize).

Six invariants.  This is the trunk.  If a proposed change touches any of them, it is an overhaul, not an extension, and the default answer is no.  The point of writing them down is to give the tear-it-down reflex something to push against.

1. **The Spine.**  A fixed, small set of top-level zones, keyed to your relationship to what they hold.  Frozen in count and meaning once chosen.  **DECIDE:** the template uses six: `00 SYSTEM` (the vault's own governance, templates, agent instruction files) / `01 SELF` (identity, values, evidence) / `02 PERSONAL` (admin, health, family, relationships) / `03 VENTURES` (things you own or co-own) / `04 PROSPECTS` (deals, partnerships, pursuits not yet owned) / `05 CRAFT` (skill and creative work with no external stakeholder).  Yours will differ.  Keep it under eight, make the ordering mean something, and never add a zone casually.
2. **The Grammar.**  A tiny closed set of slot names, used everywhere, joined to the project name: `<Project>.Sources` (raw, authoritative, never overwritten; firsthand records are date-first by name, external references are not), `<Project>.Docs` (derived, read-first, published or not; a published piece keeps its copy here and links the render out), `<Project>.Specs` (build specs, only when a build exists).  A slot is created only when the threshold number of files needs it; below that the container is flat, map plus files.  `.Specs` and `.Sources` are exempt from the threshold, because build truth and raw material are kept apart from your own writing at any count.  Nothing sits deeper than zone / container / slot / file.  Superseded material goes to root `ARCHIVE/_Archive.<Project>/`, never to a folder inside the live container.  No other folder word, ever, except carve-outs you name in the log.  Unvetted agent generation goes to the root `_AGENT SANDBOX/`, never into a project.  The one `_`-prefixed spec is the vault's own governance spec, and it lives in `00 SYSTEM/VAULT/`.
3. **The Project Map.**  Each project carries one required floated root file, the **MAP** (the one-stop recall checkpoint: what content exists here and where it stands; near-blank out of the box, growing sections from a fixed vocabulary as the project earns them), and, when it has a build, a **`<Project>.Specs/`** folder holding one or more fit-for-purpose build specs.  Governed in full by **Project Files** below.  Note what this supersedes: the common single-master-file-per-project model.  State goes in the MAP; buildable truth goes in a spec.
4. **The Control Panel.**  One screen, `CONTROL PANEL.md`.  It points, stores nothing, regenerates freely.  Nothing that needs deciding lives here.
5. **The Waterline.**  Active zones sit in the numbered spine.  Dormant zones drop to `PARKED/` and stay fully searchable.  Reactivate by moving back up.  Human judgment overrides any staleness clock.
6. **Frontmatter.**  Two lines only: `created:` and `updated:`, both `YYYY-MM-DD`.  `created` is static; `updated` is auto-stamped on save, never hand-kept.  Two carve-outs, nothing else.  First: structured data stores (a contact store, and anything else built to be queried like a database) may carry typed fields such as `status`, `last_touched`, `tags`, because being sorted IS their function.  Second: the agent-writable surfaces (the root `_AGENT SANDBOX/`, plus `.Sources` and the raw records filed flat beside a MAP) may carry one optional line, `source_agent:`, naming the agent that dropped the file; its absence means you authored it, so the human never stamps themselves, and the field never appears on the compiled surface.  Beyond these, prose notes carry only the two lines.  **DECIDE:** if you genuinely query by tag, say so here and build the schema deliberately.  Tag fields added "just in case" rot into noise.

## The Tree, or the Canonical Map.

The six invariants rendered as one directory: root scaffolding, zone spine, per-project skeleton, waterline.  Rename freely; keep the shape.

```
VAULT/                                vault root
│
├── AGENTS.md                         the doorway: spine, MAP list, rules (CLAUDE.md imports it)
├── CONTROL PANEL.md                  the control panel: points, stores minimally
│
├── 00 SYSTEM/                        the vault's own governance, templates, agent identity files
├── 01 SELF/                          identity, values, evidence
├── 02 PERSONAL/                      admin, body, family, relationships (contact store)
├── 03 VENTURES/                      owned: equity or co-ownership
├── 04 PROSPECTS/                     deals, partnerships, pursuits not yet owned
├── 05 CRAFT/                         skill and creative, no external stakeholder
│
├── _AGENT SANDBOX/                   quarantine: the sole surface where agents generate; flat, swept, promote or delete
├── _MY DRAFTS-CONTENT/               your own seeds, content-bound: drafts before they graduate into a project
├── _MY DRAFTS-BUILD/                 your own seeds, build-bound: drafts before they graduate into a project
├── PARKED/                           below the waterline: dormant, still searchable
└── ARCHIVE/                          dead: holds _Archive.<Project>/ folders
```

`_AGENT SANDBOX/` is a root utility folder, sibling to `PARKED/` and `ARCHIVE/`, not an extra spine zone (invariant 1 stays frozen).  It is the single quarantine surface for agent and LLM-generated content: any unvetted generation (drafts, digests, half-ideas, loose notes) lands here, never straight into a project's `.Docs`, MAP, or `.Specs`.  Flat by design (no grammar folders inside), swept regularly, every file either promoted up into the project where its subject lives or deleted.  Files carry the two-line frontmatter plus a `source_agent:` line and a `YYYY-MM-DD_<agent>_<slug>.md` name so origin is always legible.  Two carve-outs stay outside the sandbox: raw factual captures (calls, transcripts, records) still go to `.Sources`, or flat in the container below the threshold (agent-as-scribe, authoritative), and sanctioned agent-owned curated files (a contact store, a specific project MAP an agent maintains) stay in place under their project.

The drafts folders are the human-curated twin of the sandbox, split by destination, siblings to the sandbox rather than spine zones.  **The boundary is ownership-by-curation: the drafts folders hold what you own, the sandbox holds what agents generate.**  Two intakes: your own draft-mode seeds, and items you triage up out of the sandbox once you claim them for a destination.  Pulling a drop up into a drafts folder is an act of curation, so you own what lands there.  Agents do not write to it.  The split is a triage layer on top of the sandbox: content-bound and build-bound matter earns an elevated home, and anything not yet claimed for either stays in the sandbox.  There is deliberately no third "other" folder, so the unclaimed backlog stays visible rather than swept under a bin.  Both drafts folders are flat, swept (promote or delete), and stay off the Control Panel review list; a draft earns a Control Panel entry only once promoted.

Each zone holds projects.  Each project is flat by default: the MAP plus its files.  A slot from the three-name menu appears only when the threshold needs it (invariant 2):

```
<ZONE>/
└── <PROJECT>/
    ├── _<PROJECT> MAP.md        required; the only stamp
    ├── <files>                  flat until the threshold needs a slot
    ├── <Project>.Sources/       raw, from the first source
    ├── <Project>.Docs/          derived, on pressure
    └── <Project>.Specs/         builds only
ARCHIVE/_Archive.<PROJECT>/      the one archive
```

The vault's own governance is a project too, dogfooding the skeleton.  The spec that defines the structure lives inside it:

```
00 SYSTEM/
└── VAULT/
    ├── _VAULT MAP.md               index, decisions log in full, structure readings
    ├── _VAULT SPEC.md              the buildable truth (this file, once you fill it in)
    └── <files>                     flat: migration record, sources and marginalia
```

A new project stamps only the MAP; everything else is a file beside it until the threshold earns a slot.  The three names are a menu, not a template: invent nothing, pull a slot only under pressure.  Anything that fits no slot stays flat in the container, never a new folder word.

**File naming (inside the slots).**  Folders carry the grammar; files inside them are named for what they are, human-readable, with nothing repeated that the folder or frontmatter already says.  Four rules.

1. **Descriptive Title Case, spaces between words** (`Positioning Thesis.md`); never bake in the type or status, since `.Docs` already says the type and the MAP already says the status.
2. **`_` prefix is reserved for structural files only:** the map `_<PROJECT> MAP.md` and `_Archive.<Project>/`, plus the one governance spec.  It floats them to the top and marks them as scaffolding, not content.  Build specs are not `_`-prefixed: they live inside `.Specs/` and are named plainly for what they build (`<Build> Spec.md`), Title Case like any other slot file.
3. **Date-first only where the file IS an event:** firsthand records (calls, sessions, structured notes), in `.Sources` or flat, read `YYYY-MM-DD Who-or-What.md`, because the date is their identity and they sort chronologically.  Nowhere else does a date enter a name; it lives in frontmatter.  The one legitimate exception is a folder whose whole purpose is chronological ordering, where every file carries a date prefix.
4. **No `v2` / `final` / `draft` in names.**  Version is the decisions log plus git, lifecycle is a status field, and derived files are overwritten, not accumulated.  People are the case already settled: `Firstname Lastname.md`, the person and nothing else.

Three separators, three jobs: `.` joins a project to its slot (`<Project>.Docs`), `_` prefixes a structural file, a space separates words in a human-readable name.  No slot ever subdivides, except a carve-out you name in the log.  Casing: the project token is CAPS on its folder and structural files (`VAULT/`, `_VAULT MAP.md`), matching the ALL-CAPS zones, and Title Case on its slots (`Vault.Docs`).  Caps marks the container and its anchor; Title Case marks the artifact folders under it.

**DECIDE:** two house-format rules here are pure local taste with a local reason.  One vault bans em dashes in filenames because they caused sync errors on its particular sync chain, and uses two spaces after every period as a prose convention.  Test your own sync before copying the first; ignore the second if you do not care.

**Single-project zones collapse.**  When a zone holds one project, the zone *is* the project: the MAP and slots sit at the zone root, no wrapper folder.  A second project splits it into subfolders.  Multi-category zones (a personal zone holding `ADMIN` / `BODY` / `FAMILY` / `RELATIONSHIPS`) nest one level, then hit the skeleton at the leaf.

**The relationship store (a contact store, a data store not prose).**  `02 PERSONAL/RELATIONSHIPS/` is one file per contact, named plainly as the person and nothing else: `Firstname Lastname.md`.  No prefix, no date, no status in the name, so the folder reads like a contact list at a glance and adds no visual load.  Each file carries typed frontmatter (the invariant 6 carve-out), so whichever agent owns the store can sort and query it through an index, scanning this one folder instead of hunting fragments across projects.  Typed fields live in frontmatter; the two long fields, context and relevance, are prose in the body.

```
<First Last>.md   (one contact: typed frontmatter + prose body)
────────────────────────────────────────────
---
created: 2026-04-22            # first logged
updated: 2026-05-01            # auto-stamped
status: warm                   # warm | cooling | cold | dormant | archived  (hot = manual keep)
tags: [venture, consulting]    # your own vocabulary; keep it short and closed
channel: in-person             # text | email | call | social | messaging | in-person
company: <Company>
email:
phone:                         # E.164, e.g. +1 555 000 0000
last_touched: 2026-05-01       # date of last meaningful interaction; drives status
next_action: one concrete next step, free text
source_agent: <agent>          # which agent created the record
---

# <First Last>

## Context
how you met, who they are

## Relevance
why they matter right now
```

Status is derived from `last_touched`, not hand-kept: warm within 14 days, cooling 15 to 30, cold 31 to 60, dormant 60+.  **DECIDE:** those windows encode one person's cadence; set your own.  The `status` line is the manual override lane: a deliberate `hot` keep, or `archived` to drop a contact from active rotation.

Substrate over runtime: these markdown files are the source of truth; any query index a runtime builds over them (a SQLite table, a vector store, whatever the swapped-in tool uses) is derived and rebuilt from the files, never the reverse.

Snowflakes (folders that diverge from the grammar) are normalized in one migration pass, container by container, not on next touch.  Specs are not root artifacts: the one governance spec lives in `00 SYSTEM/VAULT/`; every other build spec lives inside its project's `<Project>.Specs/` folder, not at the root and not as a `.Docs` file.

## The Canonical Layouts (control panel + MAP + instruction file).

Two pointing surfaces, both point and neither hoards.  CONTROL PANEL is the vault-level roll-up (invariant 4); the MAP is the project-level tracker (invariant 3).  The control panel links only to MAPs; each MAP maps down to its own slots.

```
CONTROL PANEL.md
────────────────────────────────────────────
# CONTROL PANEL

## Weekly Focus
- [ ] the one to three moves that matter this week

## Maps
- [[_<PROJECT> MAP]]      03 VENTURES
- [[_<PROJECT> MAP]]      01 SELF
- [[_<PROJECT> MAP]]      05 CRAFT

## Someday
- parked ideas, not yet active
```

```
_<PROJECT> MAP.md   (the one required file: the recall checkpoint; this is the WHOLE file out of the box, then grown as earned)
────────────────────────────────────────────
---
created: 2026-07-15
updated: 2026-07-15
---

# _<PROJECT> MAP
> Frame (optional): one line, what this is and why it exists.  Rarely edited.

--- everything below is grown on demand, never stamped empty, from this fixed vocab ---

## STATE
**Now.**   The compiled present: where it actually stands today, edited in place.
**Next.**  The live edge: the one thread currently in motion, already decided and moving.
**Open.**  One line for an unresolved question; added only when a real thread is open.

## MAP
- [[<File>]]  one line per file, grouped; every note linked from here or a sibling

## PIPELINE
- raw idea inflow bin; add when ideas start arriving

## DECISIONS LOG
- 2026-07-15  newest on top, append-only; add on the first decision worth remembering
```

The MAP is defined by its purpose, a one-stop recall checkpoint: what content exists in the project and where it stands.  Out of the box it is only the two-line frontmatter plus the `# _<PROJECT> MAP` title (and, optionally, a one-line Frame); every section below is grown on demand, never stamped empty, so no blank field invites vigilance.  Sections are drawn from a fixed vocabulary to stay consistent across projects: **STATE** (Now / Next / opt-in Open, the compiled present you read instead of the pile), **MAP** (the index down to the slots), **PIPELINE** (raw idea inflow), **DECISIONS LOG** (the dated changelog), plus a bespoke body where a project genuinely needs one.  Most projects converge on **STATE + MAP**, the two halves of the recall job; heavy content projects grow the pipeline, governance projects grow the log.  Where STATE appears it carries three time horizons: the durable Frame, the mutable Now, the single active Next.  This keeps the MAP a state-and-index surface, not a task tracker: nothing here needs deciding.

The instruction file is the doorway any agent reads first: the spine, the list of every MAP, the project shape and the short rule list, deferring everything deeper to this spec.  It lives at the vault root as `AGENTS.md`, the name most coding agents and open-source harnesses read by convention.  `CLAUDE.md` holds one line, `@AGENTS.md`, so Claude Code loads the same bytes.  No symlinks, since most file-sync services do not carry them.  Keep the doorway short: a page, not a manual.  It should fit in a context window beside real work.

## Project Files (MAP universal, Specs optional).

**The one required file: the MAP.**  Every project carries a **`_<PROJECT> MAP.md`** at its folder root (leading `_` floats it to the top).  It is the one file every project has and the project's one-stop recall checkpoint: **what content exists here, and where it stands.**  It is defined by that purpose, not a fixed template.  Out of the box it is only the two-line frontmatter plus the title; sections are grown only as the project earns them, drawn from the fixed vocabulary above so they stay consistent across projects.  The MAP carries the project's state directly; state is never offloaded to a spec.

**The optional slot: `.Specs/`.**  A **`<Project>.Specs/`** folder is added only when a project has a build: something built toward a definition of done, detailed enough to hand an agent to execute.  Most projects (a person, a practice, a reference store, a running log) never need one.  Specs are for builds, and a build can have several, each fit for its purpose, so the home is a folder holding zero-to-many specs, not one preloaded file.  Each spec inside is the source of truth for the thing it builds, and when the MAP and a spec disagree on that build, the spec wins.  The folder is created on demand, never stamped empty; a spec starts as the build demands and is deleted with the build.  State stays in the MAP; only buildable truth lives here.

**The Build scaffold (opt-in).**  A build spec may adopt a six-section outline: **1. Frontline** (thesis, outcome, status, last updated), **2. Definition of Done** (concrete acceptance criteria), **3. Context** (background, constraints, prior art, non-goals), **4. The Build** (the requirements core), **5. Handoff Prompt** (the copy-paste, self-contained payload an agent executes in one pass), **6. Open Questions** (unresolved decisions blocking a clean one-shot).  `status` runs draft to refining to one-shot-ready.  This is a scaffold for the Build workspace type, not a universal form; a spec that needs a different shape takes whatever shape fits its build.

**Naming and order.**  MAP is `_<PROJECT> MAP.md`, ALL CAPS on the project token, floated to the folder top.  Build specs live inside `<Project>.Specs/` and are named plainly for what they build (`<Build> Spec.md`), Title Case, no `_` prefix, no repeated project token (the folder already carries it).  One MAP per project; the `.Specs/` folder holds as many specs as the project has builds.

**Bespoke exception.**  A few projects will carry a non-standard body that fits neither the standard MAP nor the Build scaffold (a belief ladder, a multi-lane weekly practice rep).  Their bespoke bodies stay intact.  Do not force them into the template.  Do name them in the decisions log, so "bespoke" stays a short list rather than a drift.

**Filing doctrine.**  Register any new doc in its project's MAP under the MAP section (one line), add a dated line to its DECISIONS LOG (creating either section if not yet present), and queue it nowhere else.  The MAP is the source of truth for the project; a spec in `.Specs/`, when present, is the source of truth for its build.  No MAP yet: leave the doc in its container, never on the desk.  Nothing leaves the sandbox or the drafts folders without one link out and one link in.

**Reversible.**  The files are additive.  If they fail, delete them and the supporting docs are untouched in their subfolders.

## The Project Skeleton (repeatable, on-demand).

The grammar IS the menu: pull from it as needed, invent nothing, add a slot only when it has content to hold.  The Frankenstein is divergence from it: bespoke folder names, split or duplicated config, projects with no MAP at all.  One grammar applied everywhere, drawn from on demand, is the whole fix.

It maps onto the generic freelancer and consultant templates that circulate online:

| Generic template | This spec |
|---|---|
| `CONTEXT.md` | `_<PROJECT> MAP.md` (richer: holds state, not just a description.  Do not add a separate CONTEXT.md) |
| `intake/` | `.Sources/`, or flat date-first files below the threshold |
| `deliverables/` | `.Docs/`, published or not, the link out in the body |
| `communications/` | flat files in the container |

Artifact-type names, not lifecycle names (`intake / delivery / follow-up`).  Lifecycle naming is client-work-specific and breaks the moment you point the same skeleton at a personal practice, a craft project, or your own identity work.  Artifact-type names are what keep one skeleton universal.

### The Workspace Types (load patterns, not new trees).

One grammar, three load patterns.  A "type" is which slots fill and where the output lands, never a new folder vocabulary.  Lifecycle stages (idea/draft/final, brief/build/output, scheduled/posted) are status in the MAP, never folders.

| Type | Profile | Where the artifact ends |
|---|---|---|
| **Knowledge** | all File | `.Docs` or flat, stays in vault |
| **Content** | File copy + Split render | script in `.Docs`; render in a media store; link back |
| **Build** | thin File MAP + App | code in a repo; MAP + breadcrumb in vault |

Same three slots for all.  A content project is not `script-lab / production / distribution`; it is the skeleton with a Split render lane pointing out.

## Rules of engagement (for any agent: local mesh, CLI, or other).

The operating contract.  Any runtime that reads or writes the vault follows these, no exceptions.  They are the invariants above, compiled into imperatives.  This is the section to hand an agent verbatim.

- **Read before write.**  Load the MAP first, then only the specific slot file you need.  Do not slurp whole zones.
- **Route by the spine.**  Place work by relationship to the operator.  Never invent a zone, never invent a subfolder word.  Doesn't fit a slot: flat in the container, beside the MAP.
- **One project, one MAP.**  Update `_<PROJECT> MAP.md` in place; never spawn parallel checkbox or status files.  State lives in one place.
- **Raw is authoritative; never overwrite it.**  `.Sources`, and the date-first records filed flat, are the source of truth.  Write derived output to `.Docs` or the MAP, and backlink it to the raw it compiled from.
- **Guard raw, prune derived.**  Derived is regenerable, so delete stale digests freely.  Provenance is raw plus backlinks, never a pile of dead derivatives.
- **Promote, do not contaminate.**  Loose agent-generated ideas drop into the root `_AGENT SANDBOX/`, the quarantine surface; your own seeds, and sandbox drops you claim, land in the drafts folders split by destination.  Only proven artifacts get promoted up into a project's named slot or MAP, sourced and on purpose.
- **Honor polarity.**  File stays in the vault; App lives in a repo or media store with a breadcrumb back; Split keeps the copy in the vault and links the render out.  The back-reference is mandatory.
- **New project ceremony.**  Folder + `_<PROJECT> MAP.md` + one line in the MAP list of `AGENTS.md`.  That is the entire ritual.  `AGENTS.md` is the only registry; the control panel points to it.
- **Subtraction first.**  Clutter is a signal to delete or park, never to add architecture.
- **Threshold before a folder.**  No slot until the threshold number of files needs it.  Flat is the default, not the exception.
- **No note without a link.**  Promotion requires one link out and one link in.  An orphan is unfinished.
- **Three numbers, periodically.**  Folders per hundred notes, orphan share, navigation lines.  Any one over its ceiling is a cleanup, not a redesign.
- **Never migrate state into a runtime.**  The vault is the substrate; the agent is swappable.  Read context from it, never become it.
- **Match the format.**  Frontmatter is two lines.  Plain markdown.  In names: `.` joins project to slot, `_` prefixes structural files, spaces separate words.

## The Settled Tradeoffs (why these numbers, not which numbers).

These are one vault's resolved decisions, kept because the reasoning transfers even when the number does not.  Your own decisions log starts empty and starts at 1.  Keep it in your vault MAP, newest on top, append-only, one line per decision with the date and the evidence.  That log, not this file, is what makes the system yours.

1. **Slots on demand, never stamped empty.**  An empty folder is an open question that nags every time you see it.  The earlier version of this spec stamped the full skeleton into every new project; it was reversed after the blank slots turned into guilt.
2. **A number, not a vibe, for when a folder is earned.**  "Fifteen before a folder" started as fifteen files of one kind.  Pick a number so the judgment call happens once, in the spec, instead of every time you file something.  **DECIDE:** count your own vault's biggest flat container and set the number where scanning it actually got painful.
3. **Raw gets its own slot from file one.**  The exemption to the threshold: raw material is kept apart from your own writing at any count, so a project's first source opens `<Project>.Sources`.  Mixing a transcript in beside your thinking costs more than an extra folder does.
4. **Three slot names, after a count.**  An earlier grammar carried six: a catch-all, a "public" slot, and a primary/secondary split on sources.  A file count killed them: the catch-all was empty in 12 of 13 projects, secondary sources in 11 of 12, the public slot in 8 of 12.  **DECIDE:** run this count on your own vault before trusting three.  The lesson is the method (count, then cut), not the number.
5. **A depth cap.**  Nothing deeper than zone / container / slot / file.  Four levels is enough for a personal vault, and the cap is what stops a slot from quietly growing a sub-slot.
6. **One archive, at the root.**  Superseded material moves to `ARCHIVE/_Archive.<Project>/` when it is superseded, not when the whole project dies.  Per-container embedded archives drain into it.  One place to not look is better than twenty.
7. **The link rule.**  Nothing is promoted out of the sandbox or the drafts folders without one link out and one link in from its MAP or a sibling.  An orphan is unfinished.
8. **One agent drop zone, with a legible name.**  Agent generation consolidates into a single root quarantine folder rather than a per-project scratch slot.  One known blast radius beats scratch space scattered across every project.
9. **Three numbers with ceilings, read periodically.**  Folders per hundred notes (not counting the slots the threshold rule requires), live notes with no inbound link, and total navigation lines across the control panel and the doorway file.  Example ceilings from one vault: 10, 25 percent, 150.  Over a ceiling is a cleanup, not a redesign.  **DECIDE:** these are the three cheapest proxies for drift; set your own ceilings from a first reading, then hold them.
10. **Migration is one pass.**  Container by container in pain order, each done to its acceptance numbers before the next starts, version control as rollback.  Explicitly strikes "normalize on next touch," which in practice means never.
11. **One doorway, every runtime.**  The doorway file carries the MAP list; the editor-specific instruction file only imports it.  Agents find their MAP there, not on the control panel.
12. **The drafts layer splits by destination.**  A single drafts folder became an elevated triage layer above a crowded sandbox, then split in two by where a seed is headed (content or build).  Deliberately no third "other" folder: anything not yet claimed stays in the sandbox, so the unclaimed backlog stays visible rather than hidden behind a bin that never empties.
13. **Carve-outs are named, not tolerated.**  Exactly one project in one vault needed a slot family the grammar does not allow, because its transcript volume genuinely demanded subdivision.  It is written down as a numbered exception.  A named exception stays one exception; an unnamed one becomes the new grammar.

## The Loop (what runs over the structure).

The folders are inert.  The value is the loop across them: **ingest** raw sources, **compound** them into the MAP and digests, **lint** for contradictions.  Agents compile, state accretes, the human reads the compiled surface instead of the raw pile.  The structure is only where the loop sets things down.

If you take one idea from this document, take this one: the structure is worth very little without something that regularly turns raw material into compiled state.  A spec with no loop is just tidier.

## The Clean Vault, Messy Scratch (the contamination boundary).

High signal-to-noise, every atom with a known origin: that is what makes search, backlinks, and the graph a faithful mirror of *your* thinking rather than a slurry.

The boundary is a dedicated surface: agents drop unvetted generation (half-ideas, loose notes, drafts, digests) into the root `_AGENT SANDBOX/`, and raw factual captures into `.Sources`, but never into `.Docs` or the MAP, which carry only compiled material, sourced and on purpose.  The sandbox is the quarantine surface; promotion means triaging a drop up into the project where its subject lives once it proves useful, or discarding it.  The compiled surface stays clean and the project slots stay human-legible while the generated stuff sits in one known blast-radius folder.

Mixing generation into the compiled surface fills the vault with ideas you cannot source and breaks the mirror.  Separation is not tidiness, it is provenance.  This matters more every month, not less: the volume of plausible text an agent can add to your vault is effectively unbounded, and a vault you cannot source is a vault you cannot trust.

## The Polarity: file / app / split.

What is canonical is set by representational completeness: does plain text carry the whole value, or is there irreducible form (style, render, execution) it cannot hold?  Three states:

- **File.**  Text is the whole thing (spec, note, decision log, config).  Lives in the vault.  *Text that IS the thing.*
- **App.**  Text only feeds the thing; value appears on run or render (source code, a video pipeline).  Lives in a repo or media store; only a breadcrumb returns.  *Text that BUILDS the thing.*
- **Split.**  Text is the meaning, the shipped artifact adds irreducible form (a blog post, a designed deck).  Copy stays in the vault; rendered form lives outside; a two-way back-reference links them.  *Keep the words in, link the render back.*

The back-reference is non-negotiable.  Connection lives in the file, never in human memory.

## Authority vs Salience (raw vs derived).

Two rankings, not one.  **Authority:** raw wins (sources, transcripts), the source of truth, curated and kept.  **Salience:** derived wins (the MAP, digests), what you read first.  Derived is high-salience, low-authority, and **backlinks to the raw it was compiled from**.  Same primitive as split, pointed inward.

This settles archive fever: derived is regenerable from raw, so prune old derivatives freely.  Hoarding them is pure cost (clutter for you, context confusion for agents, zero provenance gain).  Guard raw, prune derived.  Provenance is raw plus backlinks, never a pile of dead derivatives.  `.Sources` and flat date-first records are raw; `.Docs`, the MAP, and digests are derived.

## Substrate vs Runtime (the boundary that stops the reflex).

This spec governs the **substrate**: durable plain-text state, Layer 1.  It is decoupled from the **runtime** that reads and acts on it, Layer 2 (whatever agent mesh, CLI agent, or coding agent you run today, and whatever replaces it next year).  Runtimes are the churny layer, meant to be swapped; the substrate outlives all of them.

"Am I on an old setup?" is a runtime question wearing a substrate costume: plain markdown in folders is not the old thing, it is the stable thing.  Never migrate state into a runtime.  Code-first agents operate on repos and belong to the building lane only; they read context from the vault, they never become it.

File over app on the storage side; CLI over app on the query side.  A CLI agent operates on the files natively, with no import or integration layer between.  When a question outgrows hand-navigation, hand the whole folder to an LLM through the terminal and let it read.

## The Environment (editor plugins).

Layer 3 is the editor.  This section is written for Obsidian because that is what the source vault runs; translate freely.  Plain markdown needs none of it, but the spec's automation (auto-stamped `updated`, the contact store, the copy-paste skeleton) needs a few.  Each is tied to the invariant it serves, so a rebuild installs only what earns its place.

**Required.**
- **Linter.**  Enforces invariant 6 and the house format: auto-stamps `updated:` on save, holds frontmatter to the two fields, normalizes format.  Without it, `updated` rots and format drifts.  This is the one plugin the spec genuinely depends on.

**Recommended.**
- **Templater.**  Makes "copy the skeleton, invent nothing" one command: stamps a new project folder and MAP with `created` and `updated` prefilled.  The built-in Templates core plugin is a lighter fallback.

**Optional (usage-dependent).**
- **Dataview.**  Convenience for the control panel roll-up and stale-date lint.  Note that the contact store runs on an agent plus an index, not on Dataview.
- **Git.**  Version history.  Optional if you already run scheduled snapshot backups.
- **QuickAdd.**  One-key new-project and capture macros; pairs with Templater.
- **Homepage.**  Opens the control panel on launch.
- **Omnisearch / Recent Files.**  Navigation aids; core search usually suffices.

**Avoid.**
- **Kanban, Calendar, Projects, Tasks.**  They reintroduce parallel checkbox surfaces and lifecycle-as-folders, both Non-Goals.  State lives in the MAP, not a plugin database.

## Non-Goals.

- No parallel checkbox files.  State lives in the MAP.
- No per-project bespoke folder schemes.  One grammar.
- No top-level churn.  The spine is the fixed thing the overhaul reflex bounces off.
- Not a task manager, not a second brain in the maximalist sense, not a place to store what an agent can regenerate.

## Provenance (sources, on point, built in the open, no course funnels).

- **Andrej Karpathy, "LLM Knowledge Bases" (Apr 2026).**  The LLM is a compiler, raw material is source code, the wiki is a persistent compounding artifact: "compiled once and kept current, not re-derived on every query."  Basis for the loop and for the MAP as compiled state.  https://x.com/karpathy/status/2039805659525644595
- **Steph Ango (kepano), on clean vault vs agent scratch (2026).**  Keep the personal vault high signal-to-noise with known origins; give agents a separate messy vault; only promote agent artifacts in once they prove useful, so search, backlinks, and the graph stay scoped to your own knowledge.  Basis for the contamination boundary above.  This spec keeps that model in substance but in-vault, as one quarantine folder rather than a second vault.  https://x.com/kepano/status/2039831289533227446
- **Mario Zechner (badlogic), pi coding agent / agent-tools (2025).**  Minimal core, context on demand: each capability is a plain file the agent reads only when needed, and model output is surfaced into annotatable markdown rather than trapped in chat.  Basis for the thin core and load-only-what-you-need.  https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- **Steph Ango (kepano), "File over app."**  Own durable plain-text files that outlive any tool.  Basis for plain `.md` and no lock-in.  https://stephango.com/file-over-app

## Reversible by Design.

This spec is additive and descriptive.  It codifies what already works and names the trunk explicitly so the tear-it-down reflex has something to push against.  The one migration it calls for is a single pass with acceptance numbers and version control as rollback.  If a rule fails, strike the line; the files underneath are untouched.

## The Rebuild Sequence (scaffold, fill, deprecate).

How an agent reconstructs the vault from this document, major restructure or minor.  Fresh scaffold then fill, never in-place mutation: the old tree stays whole and working until the new one is populated, so every step is reversible.

1. **Install the environment.**  The editor plus the Required plugin.  Configure the linter to auto-stamp `updated` and hold frontmatter to the two fields.
2. **Render the tree empty.**  Create the spine and the canonical map from "The Tree" exactly, all folders, no files.  Collapse single-project zones per the rule.  This is the completeness test: if the spec cannot produce the scaffold, the spec is incomplete.
3. **Fill from the old vault.**  Move material in container by container: files flat beside the MAP, a slot only where the threshold needs it.  Raw lands untouched, firsthand records date-first; derived lands in `.Docs`, flat, or the MAP; superseded material goes to root `ARCHIVE/`.  Normalize frontmatter to the two lines on the way in.
4. **Seat the control panel and MAPs.**  Write `_<PROJECT> MAP.md` for each project and the control panel roll-up.  State reads from the filled slots, not from memory.
5. **Deprecate the old.**  Once a source folder is drained and its material verified in place, park it under `ARCHIVE/`, then delete when the new tree is trusted.  The old vault is the rollback until this step.

## Afterword: the part that does not transfer.

Everything above is structure, and structure is the cheap part.  What makes a vault like this work is a decisions log with real dates and real evidence in it, a loop that runs whether or not you feel like it, and the willingness to delete.

So treat this file as a starting position to argue with, not a system to install.  Fill in the placeholders, change the numbers, keep your own log, and the spec becomes yours in about a month.  Copy it verbatim and you have inherited someone else's cognitive load, which was the problem it was written to solve.

==Shared freely.  Use it, fork it, strip the attribution if you like.  No paywalls, no email captures, no courses on the horizon.==
