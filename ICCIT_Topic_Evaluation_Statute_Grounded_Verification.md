# Reviewer Evaluation Report
## Topic: "Statute-Grounded Verification: A Citation-Level Multi-Agent Framework for Auditable Bangla Legal Question Answering"

**Reviewer role simulated:** Senior PC member, ICCIT (International Conference on Computer and Information Technology, Bangladesh — 29th edition, IEEE Xplore-indexed, broad CS/IT scope, moderate selectivity)
**Verdict basis:** Literature search conducted July 2026, covering Bangla NLP, Bangla/South Asian legal AI, and international multi-agent/citation-verification trends.

---

## 0. Executive Summary (read this first)

This topic is **not as novel as it appears**. In the last 8 months, at least three papers have been published that occupy almost the exact same design space:

1. **MINA** (ACL 2026 Findings) — a multilingual LLM legal assistant for Bangladesh with a **two-stage Act/Section-level RAG pipeline** and **citation insertion**, evaluated on the Bangladesh Bar Council Exam.
2. **LegalRAG** (arXiv 2504.16121, 2025) — a hybrid multilingual RAG system explicitly built for **Bangla legal documents**, with an added relevance-check LLM to reduce hallucination.
3. **JusticeNetBD** and **UKIL-DB-EN/GPT2-UKIL-EN** — earlier Bangladesh-specific legal RAG assistants, plus a 2025 comparative study benchmarking LLM factual accuracy against licensed Bangladeshi lawyers on real Bengali legal questions.

None of these use an explicit **multi-agent adversarial/debate verification layer** with **citation-level precision/recall metrics** as the central contribution — that combination is the one genuinely defensible gap. But the proposal as titled reads as an incremental recombination of (a) statute-grounded RAG, which Bangladesh researchers have already built twice in 2025–2026, and (b) multi-agent hallucination verification, which is a hot but *already crowded* international trend (LegalHalluLens, ChatLaw, Debate-Feedback, CiteTracer, courtroom-debate frameworks). The paper is publishable for ICCIT **only if** it is repositioned around the citation-level auditability contribution and is explicitly benchmarked against MINA/LegalRAG rather than presented as if no Bangla legal RAG work exists.

---

## 1. Research Problem — Score: 7/10

**Problem stated:** Bangla legal QA systems answer fluently but cannot be trusted, because there is no mechanism to verify that a generated answer's claims are actually grounded in specific statute citations (sections/acts), and no auditable trail a lawyer or citizen could check.

**Is it important?** Yes, genuinely. Bangladesh has a large population, a pluralistic legal system (colonial common law + statutory + religious personal law), acute access-to-justice problems, and Bengali is a certified low-resource language for legal NLP. A 2025 comparative study sampling real questions from a 200,000-member Bangladeshi legal-help Facebook group found LLMs still show "notable gaps in legal accuracy and context-specific reasoning" and explicitly recommends RAG to reduce hallucination — confirming the problem is live, not hypothetical.

**Who benefits:** Citizens seeking preliminary legal information, legal-aid NGOs, paralegals, and researchers building auditable legal AI generally.

**Is it narrow enough for ICCIT?** Reasonably — ICCIT (Bangladesh) is a broad, IEEE-indexed, moderate-bar venue that regularly accepts applied Bangla NLP systems papers. A single-conference-paper scope (build framework + evaluate on Q&A/citation metrics) fits the typical 6–8 page ICCIT format if the evaluation is kept tight (i.e., don't also promise full legal reasoning, multi-hop case law analysis, and deployment — pick one).

**Weakness:** The problem statement conflates two different things that need separating in the writing: (1) grounding — retrieving the correct statute/section, and (2) verification — checking after generation that the claim matches the retrieved citation. Most of the "auditability" value proposition depends on (2), but the title foregrounds (1), which is already solved reasonably well by MINA and LegalRAG.

---

## 2. Novelty — Score: 4.5/10

This is the critical section, and where the topic is weakest.

**What already exists (2024–2026), found via search:**

| Work | Year | Overlap with proposal |
|---|---|---|
| MINA (ACL Findings 2026) | 2026 | Bangla/English legal assistant, **two-stage Act→Section RAG** specifically designed to prevent statute conflation, **citation insertion into answers**, evaluated on BD Bar Council MCQ/written/viva. This is the closest prior work and largely pre-empts the "statute-grounded" half of the title. |
| LegalRAG | 2025 (arXiv 2504.16121) | Multilingual RAG for **Bangla** government/legal documents, adds an LLM relevance-checker and query refinement step specifically to raise retrieval precision and reduce hallucination — i.e., already a rudimentary verification agent. |
| JusticeNetBD | 2025 | RAG-based Bangla legal assistant (domain: women's legal rights), context-aware retrieval. |
| UKIL-DB-EN / GPT2-UKIL-EN | 2024 (arXiv 2410.17210) | First structured Bangladesh legal-AI assistant; establishes that this space has been active for 2 years already, not brand new. |
| Bengali legal reliability study | 2025 (arXiv 2511.05627) | LLM-as-judge + licensed lawyer evaluation of factual accuracy on real Bengali legal questions; explicitly flags hallucination/citation-accuracy as the open problem the field needs to solve. |
| LegalHalluLens | 2026 (ICML workshop) | Typed hallucination auditing + **calibrated multi-agent debate** specifically for legal AI trustworthiness, with a Risk Direction Index and per-category verification. Methodologically extremely close to "multi-agent verification for auditable legal AI" — but domain is English contracts (CUAD), not statutes/Bangla. |
| ChatLaw | 2024 | Multi-agent + knowledge-graph MoE legal assistant explicitly built to reduce hallucination — establishes multi-agent legal verification as an existing paradigm, not new. |
| Debate-Feedback / Courtroom-style multi-agent debate frameworks | 2025–2026 | Multi-agent debate applied to legal judgment prediction and controversial claim verification — confirms "multi-agent debate for legal trustworthiness" is now a recognized subfield with multiple 2025–2026 entries. |
| CiteTracer / "Source or It Didn't Happen" | 2026 | General-purpose multi-agent, taxonomy-based **citation hallucination detection** — shows citation-level, field-level (not just binary) verification is an active, sophisticated research direction the proposal should benchmark its metric design against. |

**Assessment:**
- The **Bangla + legal + RAG** combination is *not* new — it has at least four prior systems (MINA, LegalRAG, JusticeNetBD, UKIL-DB-EN) as of mid-2026, two of them from 2026 itself.
- The **multi-agent verification for legal hallucination/citation trust** combination is *not* new internationally — LegalHalluLens, ChatLaw, Debate-Feedback, and CiteTracer all occupy this space, with LegalHalluLens being methodologically almost identical in spirit (typed, calibrated debate for legal trustworthiness).
- What is **not yet published**, as far as this search found: a framework that does **citation-level** (statute/section-level, not just document-level) verification, with **formal citation precision/recall/faithfulness metrics**, using a **multi-agent adversarial/debate architecture**, specifically for **Bangla** statutory law. That is a real, narrow gap — but it is a *combination* novelty (stacking existing components onto a new language/jurisdiction), not a *methodological* novelty. Reviewers familiar with the 2025–2026 legal-AI literature (increasingly likely at ICCIT given how much Bangladeshi legal-NLP work now exists) will ask "how is this different from MINA + LegalHalluLens?" and the current title gives no answer.
- Risk: if the authors did not deliberately search for MINA/LegalRAG (both very recent, MINA published essentially concurrently), an ICCIT/IEEE reviewer doing due diligence will find them immediately, as this search did in under ten queries.

**Verdict on novelty:** Application-level novelty (new language + new architecture combination), not methodological novelty. Moderate-low score reflecting real but narrow differentiation, contingent on explicit repositioning.

---

## 3. Research Gap — Score: 6/10

Legitimate gaps that remain even after accounting for prior work:
- No existing Bangla legal QA system reports **citation-level** faithfulness/hallucination metrics (evidence precision/recall at the statute-section granularity) — existing Bangla systems report answer-level accuracy or exam scores, not citation-grounding metrics.
- No existing Bangla legal system uses an explicit **adversarial verifier/debate agent** whose sole job is to check generated claims against retrieved statute text and either confirm, flag, or reject the citation — MINA and LegalRAG both improve retrieval quality upfront but do not verify after generation.
- No public **audit trail / traceability** artifact (a machine-checkable claim-to-citation mapping) exists for Bangla legal AI outputs, which matters for a jurisdiction with active judicial interest in AI governance (a 2026 Bangladeshi legal-AI roadmap piece explicitly calls for an AI ethics committee and algorithm evaluation for judiciary use).

These are real but **incremental** gaps — closing them is valuable engineering, not a new scientific insight. Score reflects "meaningful for a systems/applications paper, not for a top-tier methods paper."

---

## 4. ICCIT Relevance — Score: 8.5/10

ICCIT (Bangladesh) is exactly the right venue for this: Bangla-language NLP systems, applied AI for national problems, and IEEE Xplore-indexed proceedings with a track record of accepting exactly this kind of applied-legal/Bangla-NLP work. The technical bar is moderate (not ACL/EMNLP-level), so the novelty concerns in Section 2 are less fatal here than they would be for a top-tier NLP venue — but ICCIT reviewers in 2026 are increasingly likely to include people aware of MINA (a Bangladeshi-authored ACL paper), so the omission of directly competing work would still be flagged.

---

## 5. Current Research Trend — Score: 8/10 — **Emerging, bordering on Stable/Crowded internationally, still Emerging for Bangla specifically**

- **Citation-grounded, verifiable RAG and hallucination auditing** is one of the most active 2025–2026 themes across ACL/EMNLP/ICML workshops, evidenced by FActScore, HaluBench, HalluLens, PHANTOM, and the CiteTracer citation-hallucination taxonomy work found in this search, plus venue-level "citation hallucination" desk-reject policies at ICLR/ACM CCS 2026 — the wider field cares intensely about exactly this problem right now.
- **Multi-agent debate for factuality/legal trustworthiness** is likewise an active 2025–2026 subfield (LegalHalluLens, Debate-Feedback, courtroom-style debate, ChatLaw), meaning the *methodological* piece of this proposal is riding an already well-populated wave, not opening one.
- **Low-resource/Bangla legal NLP** specifically is younger and still emerging — most of the Bangladesh-specific work is from 2024–2026 and thin (four systems total found). This is the part of the proposal that is genuinely on-trend and comparatively under-crowded.

---

## 6. Future Relevance — **High**

- Scientific importance: auditable, citation-grounded legal AI is likely to remain a governance requirement, not a fad — legal, medical, and financial domains all converge on "cite your source, verifiably" as a baseline trust requirement.
- Industry/civic demand: Bangladesh's own AI-readiness assessment and judiciary roadmap documents explicitly call for legal-research AI and ethics oversight, suggesting institutional appetite exists.
- Extension potential: the framework (if genuinely modular) generalizes to other statutory low-resource-language jurisdictions (e.g., Vietnamese — see VLQA — Indonesian, Urdu, Swahili legal systems), and to non-legal high-stakes citation-grounding domains (health guidelines, regulatory compliance).

---

## 7. Utility (Cross-Domain Adaptability) — Score: 7/10

| Domain | Adaptability |
|---|---|
| Healthcare | High — clinical guideline citation grounding is a near-identical problem (cite the guideline, not just answer). |
| Finance | Medium — regulatory-citation grounding (SEC rules, central bank circulars) maps directly. |
| Education | Medium — grounding answers in curriculum/textbook sources. |
| Government | High — policy/circular citation grounding for e-governance chatbots. |
| Cybersecurity | Low — less naturally a "citation grounding" problem. |
| Enterprise AI | Medium — internal policy/compliance-document grounding. |
| Scientific Research | Medium-High — overlaps directly with the citation-hallucination-detection literature already found (CiteTracer), which is itself now a distinct subfield. |

The core *architecture* (retrieve → generate → verify-against-source → flag/abstain) is domain-general; the *value* of publishing it as a "legal" paper is that legal citation correctness has unusually strict, checkable ground truth (an Act/Section number either exists and says X, or it does not), which makes it a clean evaluation testbed.

---

## 8. Technical Difficulty — **Hard**

- **Data availability:** Moderate difficulty. Bangladesh statute text exists in structured/scrapeable form (used by MINA, LegalRAG, UKIL-DB-EN), so building a statute corpus is feasible but non-trivial (OCR/formatting of gazettes, colonial-era archaic Bangla, mixed Bangla/English/Farsi-influenced legal terminology).
- **Computational requirements:** Moderate — Bangla-capable multilingual embeddings + a mid-size open LLM backbone (as used in MINA: Gemma/Llama/Qwen scale) is achievable without frontier-model budgets, especially since LegalHalluLens shows a 4B-parameter backbone can match commercial APIs with the right debate calibration.
- **Engineering complexity:** High — multi-agent orchestration, citation-span alignment, and a verifier that must reliably parse Bangla statute references is a substantial systems-engineering lift, especially for a single-team ICCIT submission timeline.
- **Evaluation complexity:** High — this is the real bottleneck. Citation-level precision/recall requires either (a) expert legal annotation (expensive, needs licensed Bangladeshi lawyers, as the 2025 reliability study did) or (b) an oracle-based proxy dataset (harder to construct for statutes than for contracts like CUAD).

**Estimated completion time:**
- One researcher: 8–12 months to a defensible ICCIT-quality paper (assuming statute corpus reuse from prior open work rather than building from scratch).
- Small team (3–4, with at least one legal domain expert): 4–6 months.

---

## 9. Dataset Availability — Feasibility: **Moderate**

- **Existing relevant resources:** Bangladesh Labor Act QA dataset (Mendeley), MINA's 595-Act/18,023-section corpus (not confirmed public), LegalRAG's Bangladesh Police Gazette QA set (168 pairs — small), UKIL-DB-EN corpus, LegalQ (multi-jurisdiction legal question generation, not Bangla), BanglaQuAD/UDDIPOK/BanglaRQA/NCTB-QA (general Bangla QA, not legal).
- **Gap:** No public, citation-annotated Bangla statute QA benchmark with gold citation spans currently found. Additional annotation work is required — likely the single largest project risk.
- Recommendation: partner with law faculty (as MINA and the 2025 reliability study both did) rather than attempting solo annotation.

---

## 10. Baseline Availability

Recommended baselines, in order of priority:
1. **Vanilla RAG** (single-pass retrieve+generate) — the standard floor.
2. **MINA-style two-stage Act→Section RAG** — the closest prior Bangla-legal baseline; must be reimplemented or compared against if code/data available.
3. **LegalRAG's relevance-check RAG** — closest prior verification-adjacent Bangla baseline.
4. **Single-agent self-critique / chain-of-verification** — cheap ablation showing multi-agent adds value over single-agent self-checking.
5. **Generic LLM-as-judge citation checker** (à la HaluBench/FActScore adapted to statute citations).

Fair comparison is achievable **only if** the authors reproduce or obtain MINA/LegalRAG rather than comparing solely against a strawman vanilla-RAG baseline — reviewers will notice if the closest prior Bangladeshi work is absent from the comparison table.

---

## 11. Evaluation Metrics — Recommended

- **Task performance:** Exact Match / F1 on Bar-exam-style or curated Bangla legal QA (comparable to MINA's Bar Council evaluation).
- **Faithfulness:** claim-to-citation entailment rate (does the generated claim follow from the cited section text?).
- **Hallucination:** rate of citations to non-existent Acts/Sections, and rate of unsupported factual claims (typed, à la LegalHalluLens's numeric/temporal/obligation/factual taxonomy — strongly recommend adopting a similar typed breakdown rather than one aggregate number).
- **Citation correctness:** exact-match Act+Section identification accuracy.
- **Evidence precision / recall:** of retrieved statute chunks against gold-relevant chunks.
- **Trustworthiness / auditability:** proportion of answers with a fully traceable, human-checkable citation chain.
- **Latency and cost:** multi-agent pipelines multiply inference calls — report tokens/cost per query, since this is a real deployment concern for a low-resource-budget jurisdiction.
- **Human evaluation:** licensed Bangladeshi lawyers rating accuracy/appropriateness (follow the 2025 reliability-study protocol).

---

## 12. Publication Potential

| Venue | Probability | Rationale |
|---|---|---|
| ICCIT | High (70–80%) | Right scope, moderate bar, strong local relevance; main risk is novelty pushback if MINA/LegalRAG aren't addressed. |
| IEEE conference (regional/applied) | Medium-High (55–65%) | Similar profile to ICCIT. |
| ACM conference (general) | Medium (40%) | Depends on positioning as a systems/trust paper. |
| Q3 Journal | Medium (45–55%) | Feasible with more rigorous evaluation and human study. |
| Q2 Journal | Low-Medium (25–35%) | Needs stronger novelty framing and larger-scale evaluation than a conference-length study. |
| Q1 Journal / top-tier NLP venue (ACL/EMNLP) | Low (10–15%) | The methodological novelty bar at these venues is high, and the closest analog (LegalHalluLens) already occupies similar territory; would need a genuinely new verification mechanism, not just a new language application, to compete. |

---

## 13. PhD Value — Score: 6/10

- **Research depth:** Moderate — a solid systems contribution but not deep new theory.
- **Novelty:** As above, application-level not methodological — reduces PhD-application weight somewhat.
- **Long-term potential:** Good if extended into a genuine research program (typed hallucination taxonomies for statutory law, cross-jurisdictional low-resource legal AI, formal verification of LLM legal citations) rather than a one-off system paper.
- **Interdisciplinary value:** Strong — spans NLP, legal informatics, human-AI trust, and social-impact/access-to-justice framing, which is attractive for PhD narratives.

---

## 14. Risks (ranked by likelihood × impact)

| Risk | Likelihood | Impact | Note |
|---|---|---|---|
| Insufficient novelty vs. MINA/LegalRAG | **High** | **High** | Single biggest threat to acceptance; must be addressed head-on in related work. |
| Weak/absent citation-annotated benchmark | High | High | No off-the-shelf gold dataset found; annotation burden is real. |
| Reviewer familiarity with LegalHalluLens/ChatLaw/CiteTracer | Medium | Medium-High | International reviewers in the loop (IEEE Xplore submission) may know this literature. |
| Overly broad scope (retrieval + generation + verification + auditability + multilingual) | Medium-High | Medium | Classic ICCIT-paper failure mode — needs to pick one strong contribution. |
| Evaluation complexity / cost of legal-expert annotation | High | Medium | Mitigate via partnership with law faculty, as prior Bangladesh work has done. |
| Multi-agent pipeline cost/latency undermines "practical access to justice" framing | Medium | Medium | Needs explicit cost analysis (as MINA did) or the practical-impact claim rings hollow. |
| Rapidly moving field (multi-agent legal verification changing monthly in 2025–2026) | Medium | Medium | Timeline risk — competing papers likely to appear before submission. |

---

## 15. Opportunities

- **Journal extension:** typed hallucination taxonomy for Bangla statutory claims (numeric penalties, deadlines, jurisdictional scope, obligations) — directly extending LegalHalluLens's taxonomy to a new jurisdiction/language would be a genuinely citable methodological contribution.
- **Benchmark creation:** a citation-annotated Bangla statute QA benchmark would itself be a strong, independently citable artifact (comparable in spirit to CUAD for English contracts) — arguably more valuable than the system paper itself.
- **Multilingual generalization:** extend to other South/Southeast Asian low-resource statutory systems (cf. VLQA for Vietnamese) as a comparative study.
- **Additional domains:** healthcare-guideline or government-circular citation grounding, reusing the same verifier architecture.
- **Deeper verification:** move from citation-existence checking toward formal entailment/contradiction detection between claim and statute text.

---

## 16. Improvement Suggestions

**Better titles (to signal the actual contribution, not just the buzzword combination):**
- "Typed Citation Verification for Bangla Statutory QA: A Multi-Agent Auditing Framework"
- "Beyond Retrieval: Adversarial Citation Auditing for Trustworthy Bangla Legal AI"
- "CiteGuard-BD: Citation-Level Faithfulness Auditing for Bangla Legal Question Answering"

**Scope refinement:**
- Do not re-solve statute retrieval — build on/benchmark against MINA's Act→Section retrieval rather than reinventing it, and spend the paper's novelty budget entirely on the post-generation verification/debate layer.

**Stronger research questions:**
- RQ1: Does an adversarial multi-agent verifier reduce fabricated statute citations beyond what improved retrieval alone achieves?
- RQ2: Do typed citation-error categories (wrong section, right act; nonexistent section; misquoted obligation) reveal failure patterns aggregate accuracy hides — mirroring LegalHalluLens's typed-profile argument?
- RQ3: What is the cost/latency trade-off of multi-agent verification relative to accuracy gained, for a resource-constrained deployment context?

**Stronger contributions:**
1. A citation-annotated Bangla statute QA benchmark (the most durable contribution).
2. An explicit head-to-head comparison against MINA and LegalRAG, not just vanilla RAG.
3. A typed hallucination taxonomy adapted to Bangladeshi statutory claim types.

**Evaluation strategy:** add licensed-lawyer human evaluation (follow the 2025 reliability-study protocol) — a purely automatic-metric paper will be less convincing given how much recent Bangla-legal work already uses lawyer evaluation.

**Ways to increase novelty:** foreground the *verification/auditing* mechanism and its typed-error diagnostics as the contribution; treat statute-grounded retrieval as necessary infrastructure, not the novelty claim.

**Ways to improve acceptance probability at ICCIT:** be explicit and generous in related work about MINA/LegalRAG/JusticeNetBD — proactively acknowledging and differentiating from them will read as rigor, not weakness, and preempts the most likely reviewer objection.

---

## 17. Overall Weighted Score

| Criterion | Weight | Score (/10) | Weighted |
|---|---|---|---|
| Research Problem | 10% | 7 | 0.70 |
| Novelty | 20% | 4.5 | 0.90 |
| Research Gap | 10% | 6 | 0.60 |
| ICCIT Relevance | 10% | 8.5 | 0.85 |
| Research Trend | 10% | 8 | 0.80 |
| Future Relevance | 10% | 8 (High) | 0.80 |
| Utility | 10% | 7 | 0.70 |
| Technical Feasibility | 10% | 5.5 (Hard → moderate feasibility) | 0.55 |
| Publication Potential | 5% | 7 | 0.35 |
| PhD Value | 5% | 6 | 0.30 |
| **Total** | **100%** | | **≈ 65.5 / 100** |

**Justification:** The topic scores well on relevance, trend-alignment, and future importance, but is meaningfully penalized on novelty (heavily weighted at 20%) because the two halves of the proposal — Bangla statute-grounded RAG and multi-agent legal-hallucination verification — each already have close, recent (2025–2026) published analogs. Technical feasibility is capped by the difficulty of building a citation-annotated gold benchmark from scratch.

---

## 18. Final Verdict

**Good Topic (Needs Refinement).**

The underlying problem is real, well-motivated, and on-trend, and ICCIT is an appropriate venue. But as currently titled and scoped, the proposal reads as a recombination of two already-populated 2025–2026 research threads (Bangla legal RAG: MINA, LegalRAG, JusticeNetBD; multi-agent legal hallucination verification: LegalHalluLens, ChatLaw, Debate-Feedback) rather than a new contribution. It is **not** "Weak/Not Recommended" — the gap around citation-level, typed, auditable verification specifically for Bangla statutes is real and unclaimed as of this search. But it is also **not** "Strong/Excellent" until the authors (a) explicitly benchmark against MINA and LegalRAG, (b) reposition the contribution around the verification/auditing layer and its typed error taxonomy rather than the retrieval/grounding layer, and (c) commit to building a citation-annotated evaluation set with legal-expert involvement.

---

## 19. Action Plan (prioritized, if pursuing)

1. **Literature audit first:** obtain and read MINA (ACL Findings 2026), LegalRAG (arXiv 2504.16121), JusticeNetBD, and LegalHalluLens in full before writing another line — the related-work section must directly confront these.
2. **Reframe the contribution** around citation-level, typed verification/auditing (not statute retrieval, which is already solved reasonably well).
3. **Design the typed error taxonomy** for Bangla statutory claims (adapt LegalHalluLens's approach: numeric/temporal/obligation/factual → possibly add "wrong-section-right-act" and "colonial-terminology-misinterpretation" categories specific to Bangladeshi law).
4. **Secure a legal-expert partnership** (law faculty, as MINA and the 2025 reliability study both did) for annotation and human evaluation — do this early, it is the critical-path bottleneck.
5. **Build/reuse a statute corpus** — check whether MINA's 595-Act corpus or UKIL-DB-EN's corpus can be obtained or replicated rather than scraping from scratch.
6. **Implement baselines first** (vanilla RAG, single-agent self-critique) before the full multi-agent verifier, to have a credible ablation story.
7. **Run a cost/latency analysis** from the start — multi-agent pipelines are expensive, and this must be justified quantitatively for the "practical access to justice" framing to hold up.
8. **Draft with a narrower title** reflecting the verification-centric contribution (see Section 16) before submission.

