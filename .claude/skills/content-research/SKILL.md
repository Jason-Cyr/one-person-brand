---
name: content-research
description: Find and validate what to make — competitive lane checks, topic and idea validation, audience-demand evidence — with sources and confidence marks. Use when the human asks what to post, whether an idea is worth making, who else covers a topic, or when filling in positioning.md, pillars.md, or an idea bank.
---

# Content research (find the open seat, with receipts)

Research for a one-person brand answers one question: **is there an audience for this, and is the seat open?** Everything else is trivia. Your output is a decision input for the human — not an essay.

## The two findings that matter

Every lane check produces two numbers-with-evidence, and they pull in opposite directions:

1. **Demand** — do people want this? Evidence: the same topic recurring across creators, high view counts relative to channel size, questions repeating in comments and forums, search suggestions completing themselves.
2. **Crowding** — is it already served? Evidence: how many strong pieces already exist, how recent, and how well-made.

**Repetition proves demand *and* crowding simultaneously.** This trips people up constantly. Ten similar videos with big numbers is not "a dead lane" and not "an easy win" — it means the demand is real and the differentiator has to be sharp. Report both, always. A research note that gives one without the other is half a finding.

The open seat is the intersection: demand present, crowd doing something specific that this human can credibly do differently. Name the *specific thing the crowd doesn't do*, not a vague "better quality."

## Method

1. **Search the way the audience searches**, not the way the human describes their work. Their internal vocabulary is not the query. If they say "documentary photography workflow," the audience is typing "how to find something to shoot."
2. **Go to the platform, not to blog posts about the platform.** Actual search results, actual titles, actual view counts, actual comment sections. SEO articles *about* a topic prove the topic sells ads, not that an audience wants it.
3. **Read the comments on the top 3 results.** This is the highest-value ten minutes available. The complaints under a successful piece are a spec for the next one — what it failed to cover, what people asked that went unanswered. **If your environment blocks page fetches, this step produces nothing** — say so at the top of the note rather than letting search snippets stand in for it, and tell the human it's ten minutes they could spend themselves to get the best evidence in the whole exercise.
4. **Check dates.** A lane that was crowded in 2023 and quiet since is a different opportunity from one crowded last month. Note the recency of the strongest work.
5. **Look for the format gap, not just the topic gap.** Often the topic is saturated in one format (listicle, tutorial) and empty in another (teardown, honest post-mortem, on-camera experiment).

## Confidence marking — non-negotiable

Every claim you write into the vault carries a mark. The human decides on marked claims; they cannot decide on mush.

- **`observed`** — you opened the source and saw the data yourself. Include the source and the date you looked.
- **`cited (unopened)`** — it came from a search-result summary, a snippet, or someone else's citation, and **you did not open the page**. Use this whenever a fetch was blocked, rate-limited, or you simply worked from search results. It is not `observed` (you didn't see it) and it is not `guess` (something real said it). Sandboxed and proxied environments block a lot of fetches, so expect to use this mark often and honestly — a research note that is entirely `cited (unopened)` is search-snippet-deep, and the human deserves to know that before deciding on it.
- **`inferred`** — reasoning from something you observed or cited. State the reasoning in the same breath.
- **`guess`** — plausible, unverified, nothing behind it. Allowed, but never load-bearing. If a recommendation rests on a guess, say that explicitly.

Live numbers (view counts, follower counts, platform statistics) get the date attached and a note to re-pull them if they're going on camera or into a published claim. A number without a date is a number that will be wrong later and nobody will notice.

## Hard rules

- **No dollar-promises, no guru math.** Positioning is about the open seat, not a fantasy outcome.
- **Keep counter-evidence.** If you find something that argues against the human's idea, it goes in the write-up with equal prominence. Research that only confirms is not research, and the `sceptic` critic will find the omission anyway — better it's already there.
- **Cite what you actually opened.** Never attribute a claim to a source you didn't read. If a page was unreachable, say it was unreachable and mark the claim accordingly — that is a normal, honest outcome, not a failure to hide.
- **Say when the answer is "don't."** The most valuable research finding is often that a well-loved idea has no audience or an unbeatable incumbent. Deliver it plainly.

## Output

Write findings into the vault as a file (`research/<topic>.md` in the project, or straight into `positioning.md` / the idea bank), never only into chat — chat is not memory. Structure:

```
QUESTION: <what was being decided>
DEMAND: <evidence, each marked observed / inferred / guess>
CROWDING: <who's already there, how strong, how recent>
THE OPEN SEAT: <the specific thing the crowd doesn't do — or "none found", said plainly>
COUNTER-EVIDENCE: <what argues against this>
RECOMMENDATION: <one call, with the confidence level of the weakest claim it rests on>
SOURCES: <what you opened, with dates>
```

## Then hand it to the critics

Anything that will become `positioning.md` or a committed content plan goes to **`sceptic`** (which claims are measured vs. asserted?) and **`first-principles`** (is this lane derived, or borrowed from someone with a team and a budget?) before the human commits. Research is exactly where a confident-sounding document does the most downstream damage.
