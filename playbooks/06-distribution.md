# Layer 6 — Distribution and the feedback loop (launch, measure, write it down)

**Claim:** what separates a *system* from a pile of tricks is that results go back into the memory. Decide → ship → measure → **write it down** → the machine is smarter next week. The last step is the whole trick.

## Shipping

Every launch runs against a checklist file (`templates/launch-checklist.md`), copied per piece. The gates that bite hardest, learned the expensive way:

- **Packaging is graded in roughly its first 24 hours.** Platforms test a new piece against a cold audience almost immediately; a bad title/thumbnail spends that audition and it doesn't come back. So packaging A/B starts *at publish*, not after the weekend.
- Captions/chapters built from the final export, not a draft.
- The end of the piece stays clean for end-screens/CTAs.
- A pinned comment/question ready at publish — the first hour's replies are yours to start.

## Measuring

Per piece, a tracking sheet (`templates/launch-tracking.md`): same checkpoints, same columns, every time. Rules:

- **Record what the screen says; interpret separately.** Never write the interpretation into the data row.
- Screenshots or exports get dated; rounded numbers get written as bounds.
- Comparability beats completeness — a sheet that matches the last piece's sheet is worth more than a perfect one-off.

## Writing it back (the loop)

After each launch review, the agent:

1. Extracts **one lesson** — a single sentence about what the next piece does differently (or "no change; the process held," which is also a finding).
2. Runs the **`sceptic`** critic (`.claude/agents/sceptic.md`) on that lesson before it becomes policy. One launch is n=1, and the most common failure in this whole loop is promoting a coincidence to a rule — the title and the thumbnail changed together, and the lesson credits whichever one you liked. The sceptic's job is to name what evidence would actually settle it.
3. Writes it into the project's `context.md` under Key decisions or as a session-log line — and, when the lesson concerns a visual or copy, also appends it as a dated, testable rule to the *local failure log* in `.claude/agents/art-director.md` or `.claude/agents/copy-editor.md`. That is how a launch result becomes a defect the critics catch *before* the next piece ships, instead of a note nobody rereads.
4. Applies it to the next pipeline row's plan *now*, while it's fresh — not "next time we remember."

That's why the human never has to re-teach the system: it was in the files.

## Honesty rule

The numbers get reported as they are — in the vault and, if the human publishes about their journey, in public. Underperformance analyzed plainly builds more durable trust than a highlight reel, and the analysis is only possible because the sheet is honest.

## Done when

Every published piece has a completed tracking sheet, every review produced exactly one written lesson, and you can point at a process change and name the launch that caused it.
