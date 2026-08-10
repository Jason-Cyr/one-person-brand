# Layer 1 — Memory (the second brain)

**Claim:** an AI's usefulness = leverage × memory. Everyone talks leverage; almost nobody builds the memory. This layer is the memory, and every other layer sits on it.

## What it is

A git repository of markdown files that the human and the agent both read and write:

- **`context.md` per project** — what we decided and why, work produced, next actions, open questions, session log. The agent reads it before doing anything. *The brief is the repository.*
- **`pipeline.md` per recurring-output project** — every piece of work and its stage.
- **PARA folders** (`0. Inbox` / `1. Projects` / `2. Areas` / `3. Resources` / `4. Archive`) so everything has exactly one home.

## Why git, specifically (not a synced folder)

A synced folder (Dropbox/iCloud) syncs *state*. Git syncs *change*. Because the vault is a git repo, every human edit is a commit with a diff — so the agent sees exactly what changed between sessions, unprompted. The version history is a shared changelog between human and agent. This is the single biggest reason the memory compounds: **the human can brief the agent by simply editing a file.**

## Operating rules (same as AGENTS.md — repeated because they ARE the layer)

1. Read the project's `context.md` in full before working.
2. Commit + push after every logical unit of work.
3. Write decisions/results back before ending a session.
4. Never overwrite substantial human-written text — append or propose.
5. Everything lives here; if it matters, it's a file.

## Failure modes to watch for

- **Context rot:** context.md grows but "Key decisions" stops being updated → sessions start re-litigating. Fix: every decision gets a numbered entry with its *why*.
- **Write-only memory:** the agent logs sessions but never reads old ones. Fix: the read-first rule is not optional.
- **Tracker drift:** work tracked in chat threads or external apps. Fix: pipeline.md is canonical; migrate strays into it on sight.
- **Giant files:** a context.md past ~300 lines gets skimmed, not read. Fix: move finished eras to an `archive` section or file; keep the living part tight.

## Done when

The human can open a fresh session on any device, name a project, and the agent continues mid-thought — no re-briefing. That usually takes an afternoon to set up and one week of habit.
