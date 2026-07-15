# BanLegit-Cite: Annotator Recruitment & Adjudication Protocol
### Owner: Ema (Researcher A)

This document formalizes the selection criteria, onboarding stages, compensation models, and outreach templates for recruiting two primary annotators and one senior adjudicator.

---

## 1. Selection Criteria & Qualifications

### A. Primary Annotators (2 Required)
- **Role:** Perform independent double-annotation of 100% of the corpus (~1,200–1,500 instances) to label citation category boundaries.
- **Qualifications:**
  - 3rd/4th-year LLB student, LLM student, or junior advocate in Bangladesh.
  - Completed courses and achieved high marks in: *The Penal Code*, *Code of Criminal Procedure*, *Code of Civil Procedure*, and *Special Criminal Laws* (Nari O Shishu Nirjatan Daman Ain).
  - High reading fluency in both English and Bangla.
  - Detail-oriented (critical for detecting volume, page, or statutory subsection mismatches).
  
### B. Senior Adjudicator (1 Required)
- **Role:** Arbitrate all annotation disagreements flagged by the C5 QA/IAA script and authorize final gold labels.
- **Qualifications:**
  - Practicing senior lawyer or full-time law faculty member at a reputable Bangladeshi university.
  - 5+ years of experience in criminal/civil litigation or legal research.
  - Published research in legal studies or prior experience with legal AI/NLP annotations is a plus.

---

## 2. Onboarding & Training Flow

```
Step 1: Recruitment outreach & CV screening
   ↓
Step 2: Sign NDA & confirm availability (target: ~10 hours over 3 weeks)
   ↓
Step 3: Distribute Annotation Guidelines v1.0 & run training briefing (30 mins)
   ↓
Step 4: Annotators take the 20-instance Self-Test in Label Studio
   ↓
Step 5: Review Self-Test results (Pass bar: ≥ 80% accuracy)
   ↓
Step 6: Certified for full Annotation Phase (Phase 3)
```

---

## 3. Compensation & Incentives
1. **Academic Recognition:** Annotators will be formally acknowledged in the final ICCIT paper's Acknowledgment section. If an annotator demonstrates exceptional contribution (e.g. assisting in taxonomy refinement/error analysis), they may be considered for a co-authorship slot.
2. **Research Certification:** A formal certificate of completion as a Legal Research Assistant from the sponsoring research lab/institution.
3. **Honorarium:** A target budget honorarium of BDT 5,000–8,000 per primary annotator, contingent on completing 100% of assigned annotations within the timeline.

---

## 4. Outreach Templates

### Template A: Student Annotator Recruitment (Email/WhatsApp)
```text
Subject: Invitation to join legal AI research project: BanLegit-Cite

Dear [Name],

Hope this email finds you well. 

We are currently building BanLegit-Cite, a publication-grade legal AI research benchmark evaluating citation reliability and fabrication in Bangladeshi law. The project is led by a research team preparing a submission for the ICCIT conference.

We are looking to recruit two Legal Research Assistants to help annotate and verify a dataset of ~1,200 statutory and case law citations. 

Requirements:
- Strong academic standing in Penal Code, CrPC, and CPC courses.
- Availability of approximately 8–10 hours of remote work over a 3-week period starting [Start Date].

What we offer:
- An honorarium of BDT [Amount] upon completion of the dataset annotation.
- A research assistant certificate and formal acknowledgment in the published paper (with possibilities for co-authorship for exceptional contributions).
- Hands-on experience working at the intersection of law and Artificial Intelligence.

If you are interested, please reply with your CV and a brief mention of your grades in CrPC/CPC by [Deadline].

Best regards,

Ema
Data & Legal Content Lead, BanLegit-Cite Project
```

### Template B: Senior Adjudicator Invitation (Email)
```text
Subject: Request for Academic Adjudication: Legal AI Benchmark (BanLegit-Cite)

Dear Dr./Mr./Ms. [Last Name],

I hope you are doing well.

I am writing to invite you to serve as the Senior Adjudicator for BanLegit-Cite, a research project building the first citation-fabrication evaluation benchmark for the Bangladeshi legal system.

As an expert in Bangladeshi law, your judgment will serve as the final arbiter for resolving annotation conflicts between our student annotators. The annotation corpus covers the Penal Code 1860, CrPC, CPC, and Nari O Shishu Nirjatan Daman Ain 2000.

Role & Commitment:
- Reviewing flagged disagreement cases (estimated 100–150 instances) generated from our double-annotation phase.
- Arbitrating disputed classifications (e.g., whether a citation represents a wrong Act attribution or content misstatement).
- Time commitment: ~3 hours in total, conducted asynchronously via a web-based portal in [Month].

Your expertise is vital to guaranteeing that the ground-truth legal dataset meets publication-grade rigor for IEEE/ICCIT indexing. We would be honored to include your name in the paper's acknowledgments and offer a token honorarium of BDT [Amount] for your time.

Please let us know if you would be available to support this initiative. We would be happy to share our current research roadmap and taxonomy v1 for your review.

Sincerely,

Ema
Data & Legal Content Lead, BanLegit-Cite Project
[University/Institution Name]
```
