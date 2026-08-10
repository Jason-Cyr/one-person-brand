# AGENTS.md — One-Person Brand · agent operating manual

You (the agent) are reading the starter kit for a one-person content brand. Its foundation is a **second brain**: a git repo of markdown files that you and your human both read and write, and that serves as your shared, compounding memory. Your job is to (1) build it for them, and (2) operate inside it correctly forever after.

This file is your manual. The human should never need to read it.

## Mode 1 — Bootstrap (first contact)

If this repo still contains `templates/` and `playbooks/` at the root and there is no `1. Projects/` folder yet, the vault has not been set up. When the human asks you to set it up (in any words — "set up my content brand," "set up my second brain," "get me started"), do this:

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
Assets/            ← binaries (photos, exports). Add to .gitignore if large.
```

For **each active project** the human named, create `1. Projects/<name>/`:
- `context.md` — from `templates/context.md`. Fill in everything you learned in the interview. This file is the project's living memory.
- `pipeline.md` — from `templates/pipeline.md`, if the project produces recurring pieces of work (videos, posts, releases). Skip it for one-shot projects.

Then move this starter's teaching material out of the way so the vault is clean:
- Move `playbooks/`, `templates/`, and `design-system/` into `3. Resources/starter-kit/`.
- Rewrite `README.md` to describe *their* vault in 5 lines (keep a link to this starter for credit).
- Keep `AGENTS.md` and `CLAUDE.md` at the root — update the Mode 1 trigger line so you never re-bootstrap.

### 3. First commit

`git add -A`, commit (`"bootstrap content brand vault: <projects>"`), push if a remote exists. If there's no remote, tell the human in one line how to create a private GitHub repo and push — private by default; this is their memory, not content.

### 4. Tell them what happened

Three sentences, not a tour: what you built, the one habit that matters (*start every session by telling me which project we're on*), and the first next action you logged.

## Mode 2 — Operate (every session after)

These rules are non-negotiable. They are what makes the memory compound instead of rot.

1. **Read before you work.** At the start of any session, read the relevant project's `context.md` in full (and `pipeline.md` if present). Never start from zero; never ask the human to re-brief you on things the files already say.
2. **Commit and push every change.** After each logical unit of work — not just at session end — commit with a clear message and push. Never end a session with a dirty working tree. Never force-push; never rewrite history. The human may edit files by hand between sessions: **read the recent diffs** (`git log --stat`, `git diff HEAD~5`) — their edits are briefings you weren't in the room for.
3. **Write back before you finish.** Any session that changed anything updates the project's `context.md`: decisions made (with the *why*), work produced, next actions, open questions, and a dated session-log line. If the work moved a pipeline item's stage, update `pipeline.md` too.
4. **Non-destructive, always.** Never overwrite substantial human-written content — append, or propose the change and let them decide. Preserve their voice in anything you edit.
5. **The vault is the tracker.** No external to-do apps, no side channels. If it matters, it's in a file. `0. Inbox/` catches strays; empty it into the right places when asked to tidy.
6. **Next Action is always filled.** Every project's context.md ends with at least one concrete next action. A project with no next action is either blocked (say why) or done (propose archiving it).

## Mode 3 — Grow (adding layers)

The vault is Layer 1 of a six-layer system for running a content brand solo (see `playbooks/`, or `3. Resources/starter-kit/playbooks/` after bootstrap). When the human's need matches a layer, read its playbook first, then build it *inside the vault*:

| When the human says… | Read |
|---|---|
| "what should I make / who is this for" | `playbooks/02-strategy.md` |
| "my visuals look inconsistent / take forever" | `playbooks/03-design-system.md` |
| "scripting / editing takes too long" | `playbooks/04-production.md` |
| "I want more output from what I already make" | `playbooks/05-repurposing.md` |
| "I published — now what / did it work" | `playbooks/06-distribution.md` |

Each playbook names its starter templates (`templates/positioning.md`, `pillars.md`, `script.md`, `repurposing-map.md`, `launch-checklist.md`, `launch-tracking.md`) — copy and fill rather than inventing structure.

Don't push layers on the human. Layer 1 plus whichever layer currently hurts is the right amount of system. When results come back from the world (analytics, feedback), write them into the vault — that closes the loop, and it's the whole point.

## Voice and judgment

- Be honest over impressive. If something didn't work, the files say so plainly — the human's credibility is built on that.
- Numbers get sources. When you write a metric into the vault, note where it came from and when.
- When you're unsure whether something is worth a file, it goes in `0. Inbox/` — capture beats ceremony.
