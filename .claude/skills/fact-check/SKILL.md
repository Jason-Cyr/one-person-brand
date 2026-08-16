---
name: fact-check
description: Verify factual claims before they ship — in a script, post, newsletter, thumbnail, or anything public. Checks each claim against primary sources and reports what holds, what needs softening, and what must be cut. Use before recording, publishing, or sending anything containing numbers, dates, quotes, attributions, or statements about how something works.
---

# Fact-check (before it ships, not after)

A published mistake costs credibility, and credibility is the whole asset for a one-person brand. Correcting it later reaches a fraction of the people who saw it. This runs **before** the record button or the send button — that is the only time it's cheap.

This is a different job from `content-research`. Research asks *what should we make?* This asks *is what we're about to say true?*

## Step 1 — Extract the claims

Read the piece and list every checkable assertion. Checkable means it could be false:

- **Numbers** — statistics, prices, counts, percentages, dates, durations, version numbers.
- **Attributions** — "X said," "Y announced," "according to Z." Includes paraphrases, which is where most errors live.
- **Mechanism claims** — "this works by…", "the platform does…", "the algorithm…". These are the most confidently wrong category, because the plausible explanation and the true one are both fluent.
- **Superlatives and firsts** — "the only," "the first," "nobody else." A single counterexample kills these, and someone in the comments owns that counterexample.
- **Implied claims** — a thumbnail reading "10x faster" is a claim even if the script hedges it. Check what the piece *promises*, not just what it states.

Also list what is **not** a claim: opinion, prediction, and personal experience are exempt — but flag anything phrased as fact that is actually one of those. "This is the best tool" is opinion wearing a fact's clothes.

## Step 2 — Verify against primary sources

- **Primary beats secondary, always.** Official docs, the actual announcement, the original paper, the platform's own help page. An article summarizing a change is not the change.
- **Follow the citation chain to the end.** A widely-repeated statistic often traces to one blog post citing another blog post citing nothing. If the chain doesn't terminate in a primary source, the claim is unsupported no matter how many places repeat it.
- **Check the date on the fact, not just the source.** Software behaviour, pricing, and platform rules change. A correct 2024 statement is a wrong 2026 statement, and this is the single most common failure mode in tech and creator content.
- **Quotes get checked verbatim.** Paraphrase drift is how people get misquoted in good faith. If you can't find the exact wording, report it as unverified rather than approximating.
- **If a source is unreachable, say so.** "Could not verify — page blocked from this environment" is an honest, useful result. Never fill an unreachable source with a plausible guess; that is how a fabrication enters a script.

## Step 3 — Report, with a verdict per claim

```
CLAIM: <as written in the piece>
VERDICT: verified / needs-softening / unverified / false
SOURCE: <primary source + date checked>
FIX: <the exact replacement line — for anything not "verified">
```

Then a summary:

```
MUST FIX BEFORE SHIPPING: <false claims, and any unverified claim that is load-bearing>
SOFTEN: <true-but-overstated — the honest version of each>
LIVE NUMBERS: <claims that will drift — re-pull these on publish day>
VERIFIED: <what holds, so the list above carries weight>
```

## Rules

- **Give the replacement line, not a warning.** "This is overstated" is not a fix. "Change to *'roughly 57% as of 2026-06'* and re-pull on publish day" is.
- **Softening is usually better than cutting.** Most failures are a true thing said too strongly. The precise version is nearly always more persuasive to a skeptical audience anyway.
- **Load-bearing beats interesting.** Rank by what the piece collapses without. A wrong minor detail is a note; a wrong central claim is a gate failure.
- **Flag live numbers explicitly.** Anything that changes — follower counts, platform statistics, pricing, "currently" statements — gets marked for a re-pull on publish day, with the date it was checked.
- **The honesty rule applies to the human's own numbers too.** If the piece cites their own results, check them against the vault's tracking files. Rounded-up self-reporting is the failure nobody else will catch, and it costs the most when found.

## Then

Write the verdicts into the piece's notes or the project's `context.md` — what was fixed, what was consciously kept, and which numbers need a publish-day re-pull. A fact-check nobody logged gets re-run from scratch on the next revision.
