---
title: "Liability Risk Register — The Cognition Factory"
date: 2026-07-30
status: internal
owner: Phillip John Hekmati / The Cognition Factory
purpose: Internal risk map for dual-lane product (Adult SaaS + Enterprise). Not formal legal advice.
risks:
  - id: misrepresentation_implied_outcomes
    name: Misrepresentation / Implied Outcomes
    severity: 9
    likelihood: 7
  - id: data_privacy_security
    name: Data Privacy & Security
    severity: 9
    likelihood: 5
  - id: enterprise_contractual_readiness
    name: Enterprise Contractual / Readiness Exposure
    severity: 8
    likelihood: 4
  - id: ai_practice_feedback
    name: AI-Assisted Practice / Feedback
    severity: 7
    likelihood: 6
  - id: ip_shaped_like_curricula
    name: Intellectual Property — “Shaped Like” Curricula
    severity: 7
    likelihood: 3
  - id: secondary_vectors
    name: Secondary / Lower-Probability Vectors
    severity: 5
    likelihood: 4
notes: Scores are generalities for prioritization only (1 = lowest, 10 = highest). Severity = potential financial/reputational/regulatory impact if realized. Likelihood = estimated probability under current posture and scale.
---

# Liability Risk Register — The Cognition Factory

**Status:** Internal  
**Date:** 2026-07-30  
**Owner:** Phillip John Hekmati / The Cognition Factory  
**Scope:** Dual-lane product (Adult SaaS + Enterprise)  
**Disclaimer:** This is an internal risk map produced by the Council of Groks for product and operational prioritization. It is **not** formal legal advice. Consult qualified counsel for binding analysis, ToS drafting, and jurisdictional specifics.

## Ranking Summary (from YAML)

| Rank | Risk | Severity | Likelihood |
|------|------|----------|------------|
| 1 | Misrepresentation / Implied Outcomes | 9 | 7 |
| 2 | Data Privacy & Security | 9 | 5 |
| 3 | Enterprise Contractual / Readiness Exposure | 8 | 4 |
| 4 | AI-Assisted Practice / Feedback | 7 | 6 |
| 5 | IP — “Shaped Like” Curricula | 7 | 3 |
| 6 | Secondary / Lower-Probability Vectors | 5 | 4 |

---

## 1. Misrepresentation / Implied Outcomes
**Severity: 9 · Likelihood: 7**

### Description
Any public or sales language (site, app, decks, Gym off-ramps, enterprise proposals) that a reasonable user or buyer can characterize as promising:
- Exam pass rates, job placement, degree/credit equivalence, or career readiness
- “Skill that sticks,” “readiness,” or “alignment with curricula” as a guaranteed outcome
- Enterprise “bullshido detection” or readiness verification that later is claimed to have caused professional harm

This remains the highest everyday exposure because language drifts easily under sales pressure or feature enthusiasm, even when the locked claim discipline is strong.

### Why it applies to TCF
Adult lane markets dense, degree-plan-shaped cores to busy adults. Enterprise lane sells readiness under pressure. Both create natural opportunities for over-claiming.

### Mitigations (current + recommended)
- **Already locked:** Explicit no-affiliation, no-guarantee, no-pass-rate, no-credit, no-placement language across all surfaces.
- Dual-lane separation keeps Adult claims lighter than Enterprise.
- Kristi filter and “training wheels” Gym posture reduce expectations of professional-grade outcomes.
- **Recommended next:**
  - Quarterly claim-language audit of site, app, sales decks, and Gym copy.
  - Strong limitation-of-liability and “no educational/professional advice” clauses in ToS and enterprise MSAs.
  - Sales playbook that forbids outcome promises.
  - Version-controlled marketing language that cannot be edited without review.

---

## 2. Data Privacy & Security
**Severity: 9 · Likelihood: 5**

### Description
Unauthorized access, loss, or improper secondary use of:
- Household profiles, Save Place state, progress data, uploaded study materials
- Enterprise cohort, readiness, or scenario data
- Any data that could be linked to minors if household accounts are shared

Regulatory surface includes CCPA (and other state laws), potential GDPR exposure, and future federal privacy rules. A breach can produce fines, class actions, and lasting reputational damage even for a small operator.

### Why it applies to TCF
The product intentionally stores learning state and materials so the interruptible loop works. Enterprise adds higher-sensitivity readiness data.

### Mitigations (current + recommended)
- **Recommended baseline:**
  - Access controls, encryption at rest/transit, and least-privilege on Supabase/Postgres.
  - Clear data-retention and deletion policy (especially for household accounts).
  - Written breach-notification plan.
  - Separate data-handling rules for Adult vs Enterprise tenants.
  - Privacy Policy that matches actual practice and is linked from every surface.
  - Avoid collecting more data than the loop requires.
- If minors may ever use household seats, add age-gate and parental-consent logic early.

---

## 3. Enterprise Contractual / Readiness Exposure
**Severity: 8 · Likelihood: 4**

### Description
- Failure to deliver hypercare, implementation, or retainer obligations as written
- Readiness or gap-exposure reports that an employee or contractor later claims damaged their career or reputation
- Scope creep that creates unstated obligations
- Client proprietary scenarios or performance data mishandled

Enterprise deals are fewer but higher-stakes; a single poorly scoped contract can create outsized liability.

### Why it applies to TCF
The Enterprise lane explicitly sells implementation, hypercare, and readiness verification (“bullshido detection”).

### Mitigations (current + recommended)
- Clear, written definitions of what “readiness,” “hypercare,” and “bullshido detection” do and do not include.
- MSAs with strong limitation-of-liability, indemnity, and dispute-resolution clauses.
- Never guarantee individual employment or promotion outcomes.
- Keep readiness reports factual and process-oriented; avoid diagnostic language about persons.
- Dual-lane separation ensures Adult product language does not leak into Enterprise contracts.

---

## 4. AI-Assisted Practice / Feedback
**Severity: 7 · Likelihood: 6**

### Description
Side-chat, closed-notes Practice engine, or Gym surfaces generating incorrect, incomplete, or harmful guidance that a learner relies on for academic or professional decisions. Hallucinations, over-confident feedback, or “honest pressure” that a user later characterizes as negligent.

### Why it applies to TCF
The product uses AI as a co-pilot inside the Learn–Practice–Save loop. Closed-notes Practice is designed to expose gaps; incorrect exposure is still a risk.

### Mitigations (current + recommended)
- Human-in-the-loop and closed-notes design already reduce pure generative risk.
- Clear product language that AI is a thinking aid, not an authority or tutor of record.
- Logging and review path for flagged feedback.
- ToS and in-product disclaimers that Practice and side-chat are not professional or academic advice.
- Prefer retrieval-augmented or structured feedback over open-ended generation where accuracy is critical.
- Regular evaluation of Practice quality against the measurement carts.

---

## 5. Intellectual Property — “Shaped Like” Curricula
**Severity: 7 · Likelihood: 3**

### Description
- Dense micro-cores that closely mirror specific university degree plans, textbooks, or proprietary curricula could be claimed as unauthorized derivatives.
- User-uploaded materials that infringe third-party copyright.
- Media assets (Higgsfield or other) with unclear provenance or license.

### Why it applies to TCF
The Adult content model deliberately shapes cores after aggregate regionally-accredited sequences for transfer value. User-loaded materials are part of the design.

### Mitigations (current + recommended)
- Author from first principles and public domain / original synthesis rather than copying any single institution’s syllabus or textbook structure.
- Document the “aggregate / typical sequence” methodology.
- Clear ToS that users grant necessary licenses for uploaded materials and warrant they have rights.
- DMCA / notice-and-takedown process for user content.
- License hygiene and provenance records for all generated or third-party media.
- Avoid using trademarked course names or exact proprietary phrasing.

---

## 6. Secondary / Lower-Probability Vectors
**Severity: 5 · Likelihood: 4**

### Description
- Accessibility claims if surfaces systematically exclude users with disabilities.
- Consumer-protection issues (auto-renewal, refunds, dark patterns, unfair practices).
- Platform outage or data-loss claims during high-stakes periods (exams, enterprise ramp).
- User-generated content moderation failures (offensive, regulated, or illegal material).
- Future public-store compliance once Flutter clients enter Microsoft Store / Google Play / App Store.

### Why it applies to TCF
Any consumer SaaS + multi-profile product carries these baseline risks. They are lower priority while the product remains sideloaded and claim-disciplined, but they grow with scale and store presence.

### Mitigations (current + recommended)
- Basic accessibility hygiene (semantic HTML, contrast, keyboard navigation) on web and Flutter surfaces.
- Transparent pricing, cancellation, and refund language in ToS.
- Uptime and backup expectations set realistically in enterprise agreements.
- Content-moderation policy and reporting path for user-uploaded material.
- Defer public-store presence until MRR can support ongoing compliance costs (already the plan).

---

## Recommended Next Hardening Actions (Priority Order)

1. **Claim-language audit** of all customer-facing surfaces against the locked discipline.
2. **ToS + Privacy Policy + limitation-of-liability** review (Adult SaaS and Enterprise MSA templates).
3. **Data hygiene baseline** on Supabase/Postgres (access, retention, breach plan).
4. **IP authoring guidelines** for new cores and cart promotion.
5. **Enterprise MSA checklist** that forces clear definitions of readiness, hypercare, and data handling.
6. **AI feedback evaluation loop** tied to measurement carts.

---

*Generated from Council of Groks discussion · 2026-07-30*  
*Scores are prioritization generalities only. Revisit as product scale, jurisdictions, or claim surface change.*
