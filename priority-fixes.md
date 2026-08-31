Given you're two days out, here's a prioritized fix list — ordered by what would sink the paper vs. what's polish. I'm also flagging one thing in the Bangla planning doc you may not have noticed, because it changes the whole plan.

## Tier 0 — Stop and resolve before anything else

**1. Tense mismatch on model claims.** Your Bangla planning doc describes Gemini, Claude, and GPT-4o evaluation in **future tense** — "করা হবে" ("will be done"). But the LaTeX already states, in past tense, that these models "were evaluated." If those runs haven't actually happened yet, the paper is currently claiming completed experiments that don't exist. With 2 days left, you have two honest paths:
   - Only report models you have **actual, timestamped result logs** for, and cut the rest from the paper now.
   - If you can genuinely run GPT-4o/Claude before Aug 31, do it today, save the raw output JSON, and only then update the tables.
   
   There's no version of "write it as if it's done and backfill later" that's compatible with submitting an honest paper. I'd rather help you ship a smaller, fully-true paper than a bigger one with placeholder numbers.

**2. Annotator identity conflict.** Your earlier document named annotator $A_1$ as "Bushra." The Bangla planning doc names $A_1$-equivalent as "শাকিলা শারমিন" (Shakila Sharmin) — a different person. Before submission you need to confirm: is this the same person under two names, a genuine second annotator, or a documentation error? This matters independent of anonymization — your internal records (annotation logs, signed adjudication forms) need to consistently identify who actually did the work, even though the paper itself won't name them.

## Tier 1 — Numeric consistency (mechanical, but must be exhaustive)

Pick the **one true set of numbers** from your actual run logs, then grep the whole document for every instance of the old values:

| Quantity | Conflicting values still in the doc | Fix |
|---|---|---|
| Dataset N | 150 (most places) vs 90 (Limitations, Conclusion) vs 150 total but 75/75 in Bangla doc | One number, everywhere |
| Real/Fabricated split | 74/76 (LaTeX) vs 75/75 (Bangla doc) | Match actual file count |
| Kappa | 0.9733 vs 0.9327 vs 0.9351 vs "≈0.93" | One number |
| Standard accuracy | 74.67% vs 78.89% | One number |
| McNemar χ² | 36.0263 vs 6.86 | Recompute from logs, use one value |

Concretely: open your actual results JSON/CSV, recompute every stat fresh, and only then edit the LaTeX — don't patch numbers section-by-section from memory, since that's exactly how you got here.

## Tier 2 — Real methodological gap (needs a decision, not just an edit)

Gemini 3.5 Flash and GLM-5.2 **generated** the fabricated citations (Section III-B) and are also **evaluated as verifiers** on the same dataset. A model catching its own fabrications isn't a clean test. With limited time, the fastest defensible fix is adding one sentence to Limitations acknowledging this as a known confound and, if possible, a small cross-check (e.g., "excluding self-generated items, accuracy was X%") — even a partial ablation is better than silence, since a reviewer will spot this.

## Tier 3 — Anonymization (mechanical, do last so it doesn't get overwritten by edits)

- Blank `\author{}` block, or use ICCIT's anonymous-submission template if they provide one.
- Remove `github.com/shakeraema` and `github.com/ZahidHasan7` from the author block.
- Replace the abstract-footnote repo link with an anonymized mirror or "code in supplementary material," and add the real link back only at camera-ready.

## Tier 4 — Verify the repo is actually reachable

Confirm in an incognito window it loads, since reviewers will click the link in the submitted PDF.

---

Given the timeline, my suggestion: do Tier 0 first — it determines whether Tier 1's numbers even need reconciling against 3 models or fewer. If you paste your actual result log files (or even just the raw accuracy/kappa numbers per model, per run), I can help you rewrite every affected paragraph in one pass so nothing drifts again.