# Layer 4 — Production (scripts to edits)

**Claim:** the mechanical parts of production — structuring for retention, cutting flubs, assembling the edit — are automatable. The creative cut stays human. The human's time goes to performing and deciding, not scrubbing timelines.

## Scripts built for retention

Write video scripts **word-for-word**, engineered, not improvised:

- **The first 30 seconds carry the biggest audience drop.** Open on the result/promise/tension. Never open with introductions.
- **A re-engagement beat at ~25–30%** of runtime — a turn, a reveal, "here's where it gets interesting."
- **A pattern interrupt roughly every 90 seconds** — visual change, a number, a question. Pacing variation predicts retention more than clever wording.
- **One engagement ask** at a natural pause, not stacked on the value.
- **An outro that points at a specific next piece,** then gets out of the way.
- Mark delivery and on-screen cues inline in the script (e.g. `[graphic: timeline]`) — the script doubles as the edit plan.

Store scripts in the project (`scripts/<piece>.md`, start from `templates/script.md`), and keep an estimated runtime (~140 spoken words ≈ 1 minute).

**Before the human records, two passes on the script** — both cheap in a text file and expensive after a shoot:

1. **`fact-check`** (`.claude/skills/fact-check/SKILL.md`) on every number, date, quote, attribution and mechanism claim, including the human's own results. A wrong claim caught here costs a line edit; caught after publishing it costs credibility, and the correction reaches a fraction of the people who saw it. It also marks the live numbers that need a re-pull on publish day.
2. **`copy-editor`** (`.claude/agents/copy-editor.md`) on the script — and on the title and thumbnail copy in the same pass, because the failure it catches most often is relational: a thumbnail that repeats its own title has spent two surfaces on one job.

Re-run both after every rewrite, not just the first draft.

## The one-take assembly trick

The human records everything in one take, flubs included. Then a script:

1. Transcribes the master with word-level timestamps (Whisper or the platform of your choice).
2. Matches spoken lines against the written script (fuzzy match — people never say exactly what they wrote).
3. Where a line was said more than once, keeps the **last clean take** (people re-say a line until they nail it).
4. Emits an edit — FCPXML/EDL/cut-list — that a human editor (or the human) opens and finishes.

The agent can build this pipeline in a few hundred lines for the human's specific editor. Build it *when editing time actually hurts* — it pays off fastest on talking-head formats. Log the receipts in context.md (raw length → assembly length, number of cuts) — those numbers are also content (see Layer 5).

## Captions and the finish

- Captions generate from the FINAL export, then get proofread (names always break).
- The human makes the final creative pass. The system's job is that this pass starts at 90% done.

## Done when

Raw footage in → reviewable assembly out with no timeline-scrubbing by the human; script structure holds retention (check against Layer 6 data, not feelings).
