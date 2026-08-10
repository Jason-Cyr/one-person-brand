# One-Person Brand

**Point your AI agent at this repo, and one person — you — can run an entire content brand.**

It starts by building you the foundation: a second brain your AI reads and writes. Then it grows the rest of the system on top, layer by layer, as you need it.

This is the starter kit from my video *How I'd Build a Content Brand With AI in 2026 (The Full System)*. Everything in that video — the memory, the strategy docs, the design system as code, the repurposing engine, the feedback loop — sits on one foundation: **a folder of text files that you and your AI both read and write.**

**A heads-up before you start: this repo is written for your agent, not for you.** The instruction files, the playbooks, the templates — their reader is the AI. Your job is two minutes of setup and then answering a few questions. The agent's job is everything else. (You're welcome to read all of it — there are no tricks in here — it's just optimized for a machine that follows instructions literally.)

## How to use it (2 minutes)

1. **Clone this repo** (or fork it, or download it — any copy works):
   ```
   git clone https://github.com/Jason-Cyr/content-brand-starter.git my-brand
   cd my-brand
   ```
2. **Open your AI agent in the folder.** Claude Code, Cursor, or any agent that can read files and run git. It will find its instructions automatically (`CLAUDE.md` / `AGENTS.md`).
3. **Say:** *"Set up my content brand."*

## What to expect (so nothing surprises you)

When you say "set up my content brand," here's what your agent will do, in order:

1. **Interview you, briefly** — what you're working on, what you make, where it gets published, and how you like to sound. A few questions, not a form.
2. **Scaffold your vault** — a small folder structure (called PARA) plus a `context.md` memory file for each of your active projects, pre-filled with what you told it.
3. **Tidy this starter out of the way** — the teaching material moves into your Resources folder; the repo becomes *your* vault, not my starter.
4. **Commit everything with git** — and show you how to push it to a **private** repo of your own. (Fork/clone first for exactly this reason: your memory should be private; this repo is just the seed.)

From then on, every session starts with the agent reading your project's memory and ends with it writing back what you decided. You'll notice the difference within a week: **you stop re-briefing your own assistant.** Every conversation makes the next one smarter.

Later, when something starts to hurt — "my visuals are inconsistent," "editing eats my weekend," "I published, now what?" — ask about it. The agent has a playbook for each of the six layers and will build that layer inside your vault, with working templates to start from.

**What you need:** an agent that can read/write files and run git (Claude Code, Cursor, or similar), and git installed. That's it. No subscriptions.

## What's inside

| Path | What it is |
|---|---|
| `AGENTS.md` | The agent's operating manual — how to bootstrap and maintain your second brain. Your agent reads this, not you (but you can). |
| `CLAUDE.md` | Same instructions, at the filename Claude Code loads automatically. |
| `templates/` | Working scaffolds for every layer: memory (`context.md`, `pipeline.md`), strategy (`positioning.md`, `pillars.md`), production (`script.md`), repurposing (`repurposing-map.md`), distribution (`launch-checklist.md`, `launch-tracking.md`). |
| `playbooks/` | The six layers from the video, one playbook each — your agent uses these when you're ready to add a layer. |
| `design-system/` | A working "brand as code" starter: one HTML template + a render script that turns it into publishable PNGs, plus a rubric template for taste. |

## The six layers (the 30-second version)

1. **Memory** — a git repo of markdown files. The agent reads it before anything else; the brief *is* the repository. Start here. It costs an afternoon and pays forever.
2. **Strategy** — positioning, pillars, and an idea bank: decided once, written down, always obeyed.
3. **Design** — your brand as code: HTML templates that render every surface, so it can't drift.
4. **Production** — word-for-word scripts built for retention; the mechanical edit work automated.
5. **Repurposing** — nothing gets made once. One shoot → many surfaces, in a sequence that compounds.
6. **Distribution** — ship against a checklist, measure, and write the results back into the memory. That's the loop.

If you're one person: build **Layer 1** and **Layer 5** first. The rest you add as it hurts.

## The honest part

This system doesn't make the AI the creator. The ideas, the voice, the taste, the final call — those stay yours. What it changes is what you can *execute*. I run a real content brand this way, around a day job, and this repo is the same foundation I use — simplified so an agent can build it for anyone.

No subscriptions. No nine tools. Text files, git, and one AI.

— Jason Cyr

*Questions or improvements? Open an issue — I read them.*
