# Layer 3 — Design system as code (the brand can't drift)

**Claim:** if the brand's design system is code — HTML/CSS templates plus a render script — then every surface (social carousels, video thumbnails, banners, even print) comes out of the same file, and consistency stops being discipline and becomes physics.

## What to build

1. **`design-system/DESIGN.md`** — the brand's rules as a document the agent reads before designing anything: palette (as CSS tokens), 2–3 typefaces with roles, spacing unit, what the brand *is/is not*. Start small; evolve it by rendered A/B, and log each change with its why.
2. **Templates** — one HTML file per surface, sharing the same tokens. Start from `design-system/slide-template.html` here. Typical surfaces: square/4:5 social post, 9:16 story/reel frame, 16:9 thumbnail. Add print later (it needs inverted ground + darker inks — screen colors print weak).
3. **`design-system/render.py`** — turns templates into exact-size PNGs with headless Chrome. Already in this kit; it renders any `.slide` element at the size its class declares.

## The taste loop (this is the part people skip)

The AI doesn't have taste; it borrows the human's — **if you write it down.**

1. Human rates an early render honestly (mine was a 5/10).
2. Turn every specific complaint into a line in **`RUBRIC.md`** (starter in `design-system/`).
3. Before anything ships, the **`art-director` critic** (`.claude/agents/art-director.md`) scores it against the rubric. It runs as an independent agent that sees only the render, never the effort — that isolation is the whole mechanism. If the asset carries words, run **`copy-editor`** on them in the same pass.
4. Set a ship bar (e.g. nothing under 8) and honor it.
5. **Re-run the critics on every revision, not just the first draft.** The defects that survive to publication are the ones introduced *during* revision — the scrim that was there for a face you later cropped out, the alignment whose reason expired two versions ago. A first-draft-only critique misses them by construction.
6. When a shipped asset underperforms, write the lesson into two places: a testable line in `RUBRIC.md`, and the *local failure log* at the bottom of the critic file. That is how the critic stops being generic and starts being yours.

Rules that keep renders honest:
- **Proof at feed size.** Judge the render at the pixel size the audience sees (~380px post, ~168px thumbnail) — not full-screen. If the words don't survive, it fails.
- **Empty space is a feature.** If a layout feels full, cut content — don't shrink type.
- **Fixed type scale.** Pick 4–6 sizes; never invent in-betweens. Scale contrast is what reads as confidence.

## Operating rule

New surface = new template *in the same token file*, never a one-off in a design app. If a render fights the system, either the system grows (logged decision) or the render loses.

## Done when

The human can say "make the announcement post for X" and get an on-brand, rubric-passing PNG without opening a design tool — and a stranger could not tell which asset came first.
