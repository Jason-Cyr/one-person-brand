---
name: design-system-setup
description: Build the vault's design system from scratch — interview the human about their taste, then generate DESIGN.md with real tokens, a type scale, and surface templates. Use when the human says their visuals look inconsistent, take too long, or when any design work is requested and no DESIGN.md exists yet.
---

# Design system setup (Layer 3, first run)

This produces `design-system/DESIGN.md` — the file every later render obeys. It runs **once**, with the human in the room. After it, the `designer` agent builds and the `art-director` critic judges; neither invents style.

This is a skill and not a subagent for one reason: **it requires interviewing the human.** A subagent can't ask them anything.

## Why this exists

An AI has no taste. It has an average of everything it has seen, which is what "AI-generated design" looks like. The only way it produces work that looks like *this human* is if their taste is written down as constraints. That is what you are building here — not a mood board, a set of rules that later work cannot violate.

## Step 1 — Interview (short, concrete, visual)

Do not ask "what's your brand personality." That produces adjectives, and adjectives don't render. Ask for artifacts and reactions:

- **"Name 2–3 creators, brands, or publications whose visuals you'd be happy to be mistaken for."** Then: *what specifically* — the type, the color, the restraint, the photography?
- **"Name one whose look you actively dislike."** The negative is more informative than the positives and people answer it faster.
- **"What do your assets have to work as?"** (YouTube thumbnails, square posts, 9:16 stories, a newsletter header, print?) This decides the template set.
- **"Is your face part of the brand?"** Changes layout rules fundamentally — a face owns a side of the frame and everything else arranges around it.
- **"Any colors, fonts, or a logo you're already committed to?"** Existing equity beats a clean-sheet palette.

Batch these. It's one message, not an interrogation.

## Step 2 — Write `DESIGN.md`

Small and decisive. A large design system nobody obeys is worth less than five rules that hold.

- **Palette as CSS custom properties** — ground, ink, one accent, and at most two supports. Name them by *role* (`--ink-primary`), never by hue (`--dark-blue`); roles survive a rebrand, hues don't.
- **Type: 2 typefaces maximum**, with stated roles (display vs. body). Prefer widely-available or open fonts so renders don't break on another machine.
- **A fixed type scale — 4 to 6 sizes, listed explicitly.** This is the highest-leverage line in the file. Write: *"never invent a size between these."* Scale contrast is what reads as confidence; in-between sizes are what makes work look homemade.
- **One spacing unit** and multiples of it. Nothing else.
- **Is / is not** — two short lists. "Is: high-contrast, one loud element, generous margins. Is not: gradients, drop shadows, more than one accent per asset." The *is not* list does more work than the *is*.
- **Safe areas per surface** — where platform chrome lands (YouTube's duration badge bottom-right, story UI top and bottom).

## Step 3 — Templates and the render path

- Start from `design-system/slide-template.html`; make one template per surface the human named, all sharing the token block.
- Confirm `design-system/render.py` runs end to end and produces an exact-size PNG. **A design system that can't render is a document, not a system.**
- Render one real asset — something they actually need — and show it to them at feed size. Do not ship the setup on a lorem-ipsum sample.

## Step 4 — Seed the rubric, then get out of the way

Have them rate that first real render honestly. Expect a 5 or 6; that is the correct outcome and worth saying out loud, because a first system that scores 9 means they were being polite. **Turn every specific complaint into a line in `RUBRIC.md`** — testable, not aspirational ("marks must be earned; max 2–3 per asset" beats "use marks tastefully").

Then log the decisions and their *why* in the project's `context.md`, and hand ongoing work to the `designer` agent.

## Done when

The human can say "make the announcement post for X" and get an on-brand, rubric-passing PNG without opening a design tool — and a stranger could not tell which asset came first.

## Don't

- Don't generate a palette from a color-theory lecture. Derive it from the references they named.
- Don't build all six surfaces up front. Build what they need this month; the system grows by logged decision.
- Don't let this run long. An afternoon, not a project. The rubric is where the real taste accumulates, and that only happens against real work.
