# Layer 2 — Strategy (decided once, written down, always obeyed)

**Claim:** the brand should never wake up wondering what to post. The wondering happens once, during planning, with receipts — and gets written down. Then the files are obeyed until the results argue back.

## What to build (as files in the vault)

1. **`positioning.md`** (start from `templates/positioning.md`) — the researched answer to "what lane is open?" Method:
   - Survey the human's niche: who's already there, what formats dominate, what's saturated.
   - Find the open position — the thing the crowded lane *doesn't* do (in my case: real face + real numbers in a lane full of faceless automation demos; yours will differ).
   - Write the promise a stranger gets from following. One sentence.
2. **`pillars.md`** (start from `templates/pillars.md`) — 3–5 content pillars: recurring themes the brand returns to. Each pillar gets: the audience need it serves, example pieces, and what it must never become.
3. **`idea-bank.md`** (or the pipeline's Idea section) — every idea captured with its hook/angle, sequenced loosely. Target: enough that the next 10 pieces are never in question.
4. **If there are two surfaces/brands: `flywheel.md`** — write down explicitly how they feed each other (what one builds, the other narrates; what one learns, the other applies). If you can't draw the loop, it isn't a flywheel, it's two jobs.

## How the agent does the research

**Use the `content-research` skill** (`.claude/skills/content-research/SKILL.md`) — it carries the full method. The short version:

- Real sources over vibes: platform search results, top performers in the niche, what titles/formats repeat (repetition = validated demand AND crowding — both matter).
- Confidence-mark claims: *observed* (you saw the data) vs *inferred* (pattern-matched) vs *guess*. The human decides on marked claims, not on mush.
- No dollar-promises, no guru math. Positioning is about the open seat, not the fantasy outcome.

## The critic gate (before positioning is treated as decided)

Strategy is where a plausible-sounding doc does the most damage, because everything downstream obeys it for months. Run both thinking critics from `.claude/agents/` on `positioning.md` and `pillars.md` before the human commits:

- **`first-principles`** — is the lane derived from what's actually true about this human and this audience, or assembled from tactics that worked for someone with a team, a budget, or a five-year head start? Its highest-value catch here is the pillar that exists because the niche has that pillar, not because this human has anything to say in it.
- **`sceptic`** — which claims in the positioning are *measured* versus merely *asserted*? "This lane is open" is a research finding or it is a hope, and the sceptic makes you say which. It will also price the plan against the one resource that actually binds a one-person brand: hours per week.

Re-run both whenever the strategy is revised — a positioning doc drifts quietly, and revision is where borrowed tactics sneak back in.

## Operating rule

When making anything (Layer 3–5 work), check it against pillars.md and positioning.md. If a new idea fights the strategy, that's a *decision point for the human*, not a silent drift. Strategy files change by decision, and the change gets logged in context.md with its why.

## Done when

Any piece of content can be traced to a pillar and the position in one sentence, and the next-10 list exists. Revisit quarterly or when results (Layer 6) contradict the plan — whichever comes first.
