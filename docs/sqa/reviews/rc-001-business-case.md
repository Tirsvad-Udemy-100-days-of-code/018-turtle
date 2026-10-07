# Review Record: Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-001 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001] (`QC-BC-001`, Business Case), together with [QC-LANG-001] because the type is written in the PO language
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (not confirmed at the time of this review; S01 confirmed it in [RC-008])
- Status of this record: closed on 2026-10-07. The statuses and evidence are the assistant's assessment of the first version of the document; the criteria that failed were re-reviewed in [RC-008], which ends in `Go`.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | The Cost–Benefit Assessment states that it is qualitative and why: no revenue, licence or hosting cost, so a monetary return would be invented. The only cost is S01's time, which is not estimated in hours. |
| 2 | Risks are identified with documented impact and mitigation | Pass | Six risks, each with an Impact and a Mitigation; none without a mitigation. Impact is described, not rated. |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | Seven success criteria, each with a Target and a Measure that is a number or a command (for example criterion 2: 0 failures, `python -m pytest` exits 0). |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` and `### Out of Scope` under `## Scope`. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | The Stakeholders table cites S01, S02 and S03 and states interests, not roles; the Executive Summary cites [SA-001]. The Assumptions line "S01 is the only contributor and is the reviewer" states a project fact by ID, which is acceptable. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | Optional. Methodological and Standards Foundation names the framework, ISO/IEC 25010:2023, PEP 8, PEP 257, PEP 484 and Doxygen. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Assumptions (four items) and Constraints (nine items) are separate lists. The deadline 2026-10-21 is a constraint, which the milestones trace to. |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | `## Recommendation`: "Proceed", with a one-sentence rationale. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has a `Language` row (`en`) and a `Domain` row (`it`); neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. The author wrote it in English; the reviewer confirms by reading it. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives this type `IT Executive English`. Plain sentences for a decision maker. Tool names (pytest, ruff, mypy, Doxygen) appear in Scope and Constraints because the brief fixes them; this is a judgement call for the reviewer. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Fail | No Domain Dictionary exists (`docs/dictionary.md` is absent), so the domain terms cannot be checked against one. `N-A` is not allowed for this criterion. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are English and unchanged from the template. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | One file per artifact: `find docs -name '*.*.md'` finds no translated twin. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Initial version: there is no earlier accepted version whose language could have changed. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Fail | Not yet confirmed. No record shows that the reviewer reads English and knows the IT domain (there is no reviewer training record, `TRR`). S01 confirms on this record or names a language reviewer. `N-A` is not allowed for this criterion. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Optional. Not spelled out on first use: API, ISO/IEC, PEP, README, RGB, SQA. |

## Overall Verdict

Go-with-conditions — the criteria of the type's checklist pass, and the language checklist fails criteria 5 and 9 (and 10 where listed), which the review process turns into conditions. The conditions were closed and re-reviewed in [RC-008], which ends in `Go` and covers the whole artifact.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition: accept or change the reviewer assignment. S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. Either record the deviation as accepted (this is a single-person project) or name another reviewer. | S01 | 2026-10-09 |
| Condition (language criterion 5): decide how the domain terms are checked: draft `DICT-001` (`docs/dictionary.md`) with the terms the documents use and review it against `QC-DICT-001`, or record an accepted deviation. | S01 | 2026-10-09 |
| Condition (language criterion 9): confirm on this record that the reviewer reads English and knows the IT domain, or name a language reviewer. | S01 | 2026-10-09 |
| Optional (language criterion 10): spell out on first use: API, ISO/IEC, PEP, README, RGB, SQA. | S01 | 2026-10-09 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[SA-001]: ../../stakeholder-analysis.md
[RC-008]: ./rc-008-business-case-re-review.md
