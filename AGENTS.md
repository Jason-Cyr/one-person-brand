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

Write down anything that is true of the human rather than of one project — their voice, who they're for, standing rules — **once**, in `2. Areas/voice-and-audience.md`, and have each project's `context.md` link to it. People answer the voice question in prose, and copying that answer into three project files guarantees three drifting versions of it within a month.

For **each active project**, create `1. Projects/<name>/` (spaces and punctuation are fine; don't slugify). **People describe projects rather than naming them** — "an Instagram account", "a blog I've been neglecting". If they gave you a real name ("Slow Clay"), use it verbatim. If they only described it, propose a short obvious name, use it, and tell them in one line that folders are safe to rename whenever they like. Don't stall the bootstrap over naming, and don't invent something clever.
- `context.md` — from `templates/context.md`. Fill in everything you learned in the interview. This file is the project's living memory.
- `pipeline.md` — from `templates/pipeline.md`, if the project produces recurring pieces of work (videos, posts, releases). Skip it for one-shot projects; if it's genuinely borderline, create it — an unused tracker costs nothing, a missing one costs the habit. **Rename the template's default stages to the human's actual craft.** They ship as a video chain (`Researching → Packaging → Shipping`), which is nonsense for an email essay or a batch of pots. Ask yourself what steps *this* person's work passes through, and write those.

Then move this starter's teaching material out of the way so the vault is clean:
- Move `playbooks/` and `templates/` into `3. Resources/starter-kit/`.
- **Leave `design-system/` at the root.** It is a working part of the vault, not teaching material: `render.py` is executable, `RUBRIC.md` is where the human's taste accumulates over months, and `DESIGN.md` gets written into it later. Every reference to these files across the kit assumes the root path.
- Rewrite `README.md` to describe *their* vault in 5 lines (keep a link to this starter for credit).
- Keep `AGENTS.md` and `CLAUDE.md` at the root. In AGENTS.md, **delete the whole of Mode 1** — every step, not just its opening line — and leave in its place: *"This vault was bootstrapped on <date> for <name> — do NOT run bootstrap again. Operate in Mode 2."* Deleting only the first paragraph leaves the entire bootstrap procedure live under a heading that says not to run it, and removes the very condition that would have stopped a later agent from running it. In CLAUDE.md, change "how to bootstrap the human's second brain on first contact, and" to nothing — the rest of that file stays as-is.
- **Leave `.claude/` exactly where it is.** It holds the critic bench (see below) — those are working parts of the vault, not teaching material. Never move them into `3. Resources/`, and never delete them during tidy-up.
- **Paths after the move.** `playbooks/…` and `templates/…` are now under `3. Resources/starter-kit/`. The playbooks still refer to each other and to `templates/…` by their old root-relative paths — read those as `3. Resources/starter-kit/…`. `design-system/` and `.claude/` are unchanged. Note the moved path contains spaces: quote it in shell commands.

### 3. First commit

**Deal with the remote *before* you commit** — a commit made while `origin` still points at the starter kit is one accidental `git push` away from publishing a stranger's private memory.

- **If `origin` points at this starter kit or a fork of it** (any URL containing `one-person-brand`): `git remote remove origin`. The kit is a seed, not their upstream.
- **If any other remote exists, do not push to it until you have checked that it is private and not a fork.** `gh repo view --json visibility,isFork` if `gh` is available; otherwise ask the human directly, in one line: *"Is <url> a private repo you own?"* **A fork is public by default, and the README invites forking** — so a remote that merely isn't the starter kit is not yet safe. Refuse to push to anything public or forked, and say why in one sentence. When in doubt, don't push; a missing backup is recoverable, a published vault is not.
- **Otherwise the vault is complete as-is** — a local folder is the intended default. Mention once, in one line, as optional: a **private** remote (GitHub or similar) makes the vault follow them across devices; offer to set it up only if they want that. Never present a remote as required, and never suggest a public one — this is their memory, not content.

**Then check git can actually commit.** If `git config user.email` is empty, git aborts with *"Please tell me who you are"* — likely on a machine belonging to exactly the audience this kit targets. Set a repo-local identity from the interview (`git config --local user.name "<their name>"`, `git config --local user.email "<name>@localhost"`), mention it in one line so they can correct it, and move on. Do not fail the bootstrap over it, and do not commit under an invented identity without saying so.

Now `git add -A` and commit (`"bootstrap content brand vault: <projects>"`).

### 4. Tell them what happened

Three sentences, not a tour: what you built, the one habit that matters (*start every session by telling me which project we're on*), and the first next action you logged.

## Mode 2 — Operate (every session after)

These rules are non-negotiable. They are what makes the memory compound instead of rot.

1. **Read before you work.** At the start of any session, read the relevant project's `context.md` in full (and `pipeline.md` if present). Never start from zero; never ask the human to re-brief you on things the files already say. **If the project has no `context.md`, create one from `templates/context.md` before you do anything else** — fill in what you can from the folder's existing files and say in one line that you did. A project without memory is the exact failure this vault exists to prevent, so fix it on sight rather than working around it.
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

**How to run them — three tiers, in order of preference. Use the best one your environment allows, and always record which tier you used.**

1. **Subagent (full isolation — the real thing).** In Claude Code, dispatch by name (`art-director`, `copy-editor`, `first-principles`, `sceptic`) with the Task/Agent tool. Give it the file paths and nothing else — **never your reasoning for the choices**, because a critic that knows the intention stops seeing the artifact.
2. **Fresh human-opened session (full isolation, needs the human).** Open a new session with no history of this work, paste the critic file in as the instructions, hand it only the artifact. Offer this to the human when tier 1 isn't available and the stakes are high.
3. **Same-session second pass (degraded — say so out loud).** If you have neither, run the critic file yourself under strict discipline: re-read *only* the critic file and the artifact, do not re-read your own notes, plan, or rationale, and write the full review before you allow yourself to explain any choice. Then **label the result `TIER 3 — SELF-REVIEW, NOT INDEPENDENT`** wherever you log it.

**Be honest about the tier and never launder tier 3 as tier 1.** A subagent cannot spawn another subagent, so a critic invoked from inside another agent is always tier 3 at best — if you are yourself a subagent, report your findings up and let the orchestrator run the critic. Isolation is the mechanism; a critic that shares your context is a rubber stamp, and a rubber stamp recorded as a review is worse than no review, because it retires the doubt without earning it.

**Does bootstrap need a critic pass?** No — Mode 1 is scaffolding, not shipping, and blocking it on a review the environment may not support helps nobody. The gate starts the first time real work is committed to: a positioning doc, a plan, or anything with an audience. Don't run the bench on an empty vault.

**The rules that make this work:**

- **Every iteration, not just the first.** The defects these catch are the quiet kind — copy that repeats its own title, vocabulary the audience doesn't have yet, and *vestigial* layout decisions whose justification expired two revisions ago but whose values survived into a "final" file. Those appear *during* revision, so a first-draft-only pass misses them by design.
- **Pair them.** Anything with words on a picture gets `copy-editor` *and* `art-director` — they fail differently. Any plan worth writing down gets `sceptic` *and* `first-principles`: the sceptic asks "is this true and priced?", first-principles asks "is this even the right problem?"
- **Log the pass** in the project's `context.md` by default — one line with the score and the tier. If the pass is long enough to bury the memory file, put it in `<piece>-eval.md` next to the piece and link it from `context.md`. Either way record: scores, the tier you ran at, what you applied, and what you consciously rejected and why. A rejected finding with a stated reason is a decision; an ignored one is a defect you'll ship twice.
- **Feed them back.** Each critic file has a **`## Local failure log`** section (mid-file, not at the very end — append inside that section, never below it, or you'll corrupt the report spec that follows). When a piece underperforms, or the human catches something a critic missed, append there as a dated, testable rule. The critics ship generic and become this human's — same mechanic as the complaint log in `RUBRIC.md`. **This is the most valuable maintenance you do in this vault.** A critic bench that never learns is worth a fraction of one that does.

### The maker: `designer`

`.claude/agents/designer.md` is the one agent on the bench that *builds* rather than judges. It reads the design system, works only in tokens and templates, renders, and proofs the result at feed size — then stops and reports. **You** run `art-director` on what it produced and bring the findings back to it; `designer` cannot dispatch a critic itself, because a subagent cannot spawn one. Run that loop until the asset clears the ship bar. **`designer` never approves its own work**, and neither do you: a maker who also grades is the exact failure the bench exists to prevent. If no `design-system/DESIGN.md` exists yet, `designer` will tell you to run the `design-system-setup` skill first, and it's right to.

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
