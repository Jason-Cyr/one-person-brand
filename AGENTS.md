# AGENTS.md — One-Person Brand · agent operating manual

You (the agent) are reading the starter kit for a one-person content brand. Its foundation is a **second brain**: a git repo of markdown files that you and your human both read and write, and that serves as your shared, compounding memory. Your job is to (1) build it for them, and (2) operate inside it correctly forever after.

This file is your manual. The human should never need to read it.

## Mode 1 — Bootstrap (first contact)

If this repo still contains `templates/` and `playbooks/` at the root and there is no `1. Projects/` folder yet, the vault has not been set up. When the human asks you to set it up (in any words — "set up my content brand," "set up my second brain," "get me started"), do this:

**URL-first setup (you are not inside the repo yet):** the human may simply hand you this repo's URL — *"set up my content brand from https://github.com/Jason-Cyr/one-person-brand"*, or just the link. That is a complete instruction; do not ask them to clone anything. Clone it yourself — `git clone https://github.com/Jason-Cyr/one-person-brand.git my-brand` — into a fresh `my-brand/` folder (or a name/location they gave you). Never scaffold a vault inside a directory that already contains unrelated work. Then work inside the clone and continue below exactly as if you had started there.

**No-git-history copies (ZIP download, copied folder):** if the working copy has no `.git`, run `git init` before anything else. The memory needs version history — the human's hand-edits between sessions reach you as diffs. Git is local; this does not require GitHub or any account.

### 1. Interview — short, not a form

Ask only what you need to scaffold well (batch the questions; don't interrogate):
- What are you working on right now? (1–3 active projects)
- What do you make or want to make? (videos, a newsletter, a product, photography, code…)
- Where does it get published? (platforms, if any)
- What should I call you, and is there anything about your voice/style I should know?

### 2. Scaffold the vault

Create this structure (PARA — keep the names exactly, the numbering keeps them sorted):

```
0. Inbox/          ← capture anything unsorted; you triage it later
1. Projects/       ← active work; ONE FOLDER PER PROJECT
2. Areas/          ← ongoing responsibilities with no end date
3. Resources/      ← reference material, guides, research
4. Archive/        ← finished or shelved projects, moved whole
Daily Notes/       ← optional; one file per day if the human wants a log
Assets/            ← binaries (photos, exports). Already gitignored by the kit to keep the vault light.
```

Put a `.gitkeep` file in every folder that would otherwise be empty (except `Assets/` — it's gitignored) — git does not track empty directories, and without this the PARA skeleton silently vanishes from the first commit.

For **each active project** the human named, create `1. Projects/<name>/` (use their name for it verbatim — spaces and punctuation are fine; don't slugify):
- `context.md` — from `templates/context.md`. Fill in everything you learned in the interview. This file is the project's living memory.
- `pipeline.md` — from `templates/pipeline.md`, if the project produces recurring pieces of work (videos, posts, releases). Skip it for one-shot projects.

Then move this starter's teaching material out of the way so the vault is clean:
- Move `playbooks/`, `templates/`, and `design-system/` into `3. Resources/starter-kit/`.
- Rewrite `README.md` to describe *their* vault in 5 lines (keep a link to this starter for credit).
- Keep `AGENTS.md` and `CLAUDE.md` at the root. In AGENTS.md, replace Mode 1's first paragraph with: *"This vault was bootstrapped on <date> for <name> — do NOT run bootstrap again. Operate in Mode 2."* (CLAUDE.md needs no edit — it has no trigger line.)
- **Leave `.claude/` exactly where it is.** It holds the critic bench (see below) — those are working parts of the vault, not teaching material. Never move them into `3. Resources/`, and never delete them during tidy-up.

### 3. First commit

`git add -A`, commit (`"bootstrap content brand vault: <projects>"`). Then handle the remote — carefully:
- **If `origin` points at this starter kit or a fork of it** (any URL containing `one-person-brand`): `git remote remove origin`. The kit is a seed, not their upstream — never push a human's vault toward the starter repo or a public fork; that would publish their private memory.
- **If a remote the human owns exists**, push to it.
- **Otherwise the vault is complete as-is** — a local folder is the intended default. Mention once, in one line, as optional: a **private** remote (GitHub or similar) makes the vault follow them across devices; offer to set it up only if they want that. Never present a remote as required, and never suggest a public one — this is their memory, not content.

### 4. Tell them what happened

Three sentences, not a tour: what you built, the one habit that matters (*start every session by telling me which project we're on*), and the first next action you logged.

## Mode 2 — Operate (every session after)

These rules are non-negotiable. They are what makes the memory compound instead of rot.

1. **Read before you work.** At the start of any session, read the relevant project's `context.md` in full (and `pipeline.md` if present). Never start from zero; never ask the human to re-brief you on things the files already say.
2. **Commit every change** (and push, if a remote exists). After each logical unit of work — not just at session end — commit with a clear message. Never end a session with a dirty working tree. Never force-push; never rewrite history. The human may edit files by hand between sessions: **read the recent diffs** (`git log --stat`, `git diff HEAD~5`) — their edits are briefings you weren't in the room for.
3. **Write back before you finish.** Any session that changed anything updates the project's `context.md`: decisions made (with the *why*), work produced, next actions, open questions, and a dated session-log line. If the work moved a pipeline item's stage, update `pipeline.md` too.
4. **Non-destructive, always.** Never overwrite substantial human-written content — append, or propose the change and let them decide. Preserve their voice in anything you edit.
5. **The vault is the tracker.** No external to-do apps, no side channels. If it matters, it's in a file. `0. Inbox/` catches strays; empty it into the right places when asked to tidy.
6. **Next Action is always filled.** Every project's context.md ends with at least one concrete next action. A project with no next action is either blocked (say why) or done (propose archiving it).
7. **Never ship on your own judgment — run the critics.** Nothing visual, nothing public-facing, and no committed plan is "final" until the relevant critic in `.claude/agents/` has reviewed it. See the next section; this rule is not optional and it is not a first-draft-only rule.

## The critic bench (`.claude/agents/`)

You grade your own work too generously. Every agent does. The fix is structural: a second reviewer that sees the artifact and not the effort behind it. Four of them ship with this vault, and they are the difference between output and output worth publishing.

| Critic | Reviews | Run it before… |
|---|---|---|
| `art-director` | Anything rendered — thumbnails, carousels, stories, banners, print | any visual is called final |
| `copy-editor` | Any shipping text — titles, thumbnail copy, captions, scripts, emails, descriptions | any words reach an audience |
| `first-principles` | Strategy, architecture, process — is this reasoned, or borrowed and inherited? | any structural decision is committed |
| `sceptic` | Plans, analyses, recommendations — what's wishful, unpriced, or load-bearing-but-asserted | any plan or big call is committed |

**How to run them.** In Claude Code they are subagents: dispatch one with the Task/Agent tool by name (`art-director`, `copy-editor`, `first-principles`, `sceptic`), give it the file paths and nothing else — *never* your reasoning for the choices, because a critic that knows the intention stops seeing the artifact. If your tool doesn't support subagents, open a **fresh session with no history of this work**, paste the critic file as the instructions, and hand it the artifact. The isolation is the mechanism; a critic that shares your context is a rubber stamp.

**The rules that make this work:**

- **Every iteration, not just the first.** The defects these catch are the quiet kind — copy that repeats its own title, vocabulary the audience doesn't have yet, and *vestigial* layout decisions whose justification expired two revisions ago but whose values survived into a "final" file. Those appear *during* revision, so a first-draft-only pass misses them by design.
- **Pair them.** Anything with words on a picture gets `copy-editor` *and* `art-director` — they fail differently. Any plan worth writing down gets `sceptic` *and* `first-principles`: the sceptic asks "is this true and priced?", first-principles asks "is this even the right problem?"
- **Log the pass** in the piece's notes or the project's `context.md`: scores, what you applied, and what you consciously rejected and why. A rejected finding with a stated reason is a decision; an ignored one is a defect you'll ship twice.
- **Feed them back.** Each critic file ends with a *local failure log*. When a piece underperforms, or the human catches something a critic missed, append it there as a dated, testable rule. The critics ship generic and become this human's — same mechanic as the complaint log in `RUBRIC.md`. **This is the most valuable maintenance you do in this vault.** A critic bench that never learns is worth a fraction of one that does.

### The maker: `designer`

`.claude/agents/designer.md` is the one agent on the bench that *builds* rather than judges. It reads the design system, works only in tokens and templates, renders, and proofs the result at feed size — then hands off to `art-director`. **It never approves its own work**, and neither do you: a maker who also grades is the exact failure the bench exists to prevent. If no `design-system/DESIGN.md` exists yet, `designer` will tell you to run the `design-system-setup` skill first, and it's right to.

## Skills (`.claude/skills/`)

Skills are procedures you load and follow; the agents above are independent reviewers you dispatch. Three ship with this vault:

| Skill | Use it when |
|---|---|
| `content-research` | deciding what to make — lane checks, topic validation, audience-demand evidence, filling in `positioning.md` or the idea bank |
| `fact-check` | before recording, publishing, or sending anything with numbers, dates, quotes, attributions, or claims about how something works |
| `design-system-setup` | the human's visuals look inconsistent or slow, or any design work is asked for and no `DESIGN.md` exists yet |

`design-system-setup` is a skill rather than a subagent for a concrete reason: it has to **interview the human**, and a subagent can't ask them anything. Same test applies if you add your own — anything needing the human in the room is a skill.

**If your tool doesn't support skills** (they're a Claude Code convention): read the `SKILL.md` file directly and follow it. They're plain markdown with no special syntax, and nothing in them depends on being auto-loaded.

Two of the three exist because research is where confident-sounding work does the most damage. `content-research` marks every claim *observed / inferred / guess* so the human decides on marked claims rather than mush; `fact-check` runs before the record button, when a mistake is still free. Neither replaces the critics — anything that becomes positioning or a committed plan still goes to `sceptic` and `first-principles`.

## Mode 3 — Grow (adding layers)

The vault is Layer 1 of a six-layer system for running a content brand solo (see `playbooks/`, or `3. Resources/starter-kit/playbooks/` after bootstrap). When the human's need matches a layer, read its playbook first, then build it *inside the vault*:

| When the human says… | Read (post-bootstrap path) |
|---|---|
| "what should I make / who is this for" | `3. Resources/starter-kit/playbooks/02-strategy.md` |
| "my visuals look inconsistent / take forever" | `3. Resources/starter-kit/playbooks/03-design-system.md` |
| "scripting / editing takes too long" | `3. Resources/starter-kit/playbooks/04-production.md` |
| "I want more output from what I already make" | `3. Resources/starter-kit/playbooks/05-repurposing.md` |
| "I published — now what / did it work" | `3. Resources/starter-kit/playbooks/06-distribution.md` |

(Before bootstrap the playbooks are still at the repo root — same filenames.)

Each playbook names its starter templates (`templates/positioning.md`, `pillars.md`, `script.md`, `repurposing-map.md`, `launch-checklist.md`, `launch-tracking.md`) — copy and fill rather than inventing structure.

The critic bench is not a layer — it is a gate that applies to all of them. Layer 3 without `art-director` produces a consistent brand nobody can read at feed size; Layer 2 without `first-principles` and `sceptic` produces a confident strategy doc built entirely out of other people's tactics.

Don't push layers on the human. Layer 1 plus whichever layer currently hurts is the right amount of system. When results come back from the world (analytics, feedback), write them into the vault — that closes the loop, and it's the whole point.

## Voice and judgment

- Be honest over impressive. If something didn't work, the files say so plainly — the human's credibility is built on that.
- Numbers get sources. When you write a metric into the vault, note where it came from and when.
- When you're unsure whether something is worth a file, it goes in `0. Inbox/` — capture beats ceremony.
