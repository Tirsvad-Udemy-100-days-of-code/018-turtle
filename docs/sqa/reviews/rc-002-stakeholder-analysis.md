# Review Record: Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001] (`QC-SA-001`, Stakeholder Analysis), together with [QC-LANG-001] because the type is written in the PO language
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (not confirmed at the time of this review; S01 confirmed it in [RC-009])
- Status of this record: closed on 2026-10-07. The statuses and evidence are the assistant's assessment of the first version of the document; the criteria that failed were re-reviewed in [RC-009], which ends in `Go`.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | Three stakeholders, each with Power, Interest and Quadrant. The levels of S02 and S03 are the author's classification, as the Purpose states; S01 confirms them (see the action items). |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | S01, S02 and S03 are unique and are the IDs used in [BC-001] and in the milestones. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Each row has Role/Title, Organization and explicit HIGH or LOW levels, and the Rationale section is consistent with the table. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Optional. The Communication Requirements table gives channel, frequency, deliverable and the milestone (MIL-001 to MIL-004) for each stakeholder. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Three conflicts, each with stakeholders and a mitigation (function names against testability, no runtime dependencies against development tools, tokens against a public repository). |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | The Business Goal Alignment table traces eight concerns to objectives O1 to O7 of [BC-001]. The concern "tokens in `.env` stay private" has no objective of its own; it is traced to O6 and to the Risks table, a weak but honest link. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Optional. The concerns table gives each concern in business language and a FURPS+ attribute. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Optional. Short sections and tables in plain language; the abbreviations FURPS+ and RACI are not explained (see language criterion 10). |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has a `Language` row (`en`) and a `Domain` row (`it`); neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. The author wrote it in English; the reviewer confirms by reading it. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives this type `IT Professional English`. Technical wording for a professional reader, as the registry intends. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Fail | No Domain Dictionary exists (`docs/dictionary.md` is absent), so the domain terms cannot be checked against one. `N-A` is not allowed for this criterion. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are English and unchanged from the template. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | One file per artifact: `find docs -name '*.*.md'` finds no translated twin. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Initial version: there is no earlier accepted version whose language could have changed. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Fail | Not yet confirmed. No record shows that the reviewer reads English and knows the IT domain (there is no reviewer training record, `TRR`). S01 confirms on this record or names a language reviewer. `N-A` is not allowed for this criterion. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Optional. Not spelled out on first use: FURPS+, RACI, README. |

## Overall Verdict

Go-with-conditions — the criteria of the type's checklist pass, and the language checklist fails criteria 5 and 9 (and 10 where listed), which the review process turns into conditions. The conditions were closed and re-reviewed in [RC-009], which ends in `Go` and covers the whole artifact.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition: accept or change the reviewer assignment. S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. Either record the deviation as accepted (this is a single-person project) or name another reviewer. | S01 | 2026-10-09 |
| Condition (language criterion 5): decide how the domain terms are checked: draft `DICT-001` (`docs/dictionary.md`) with the terms the documents use and review it against `QC-DICT-001`, or record an accepted deviation. | S01 | 2026-10-09 |
| Condition (language criterion 9): confirm on this record that the reviewer reads English and knows the IT domain, or name a language reviewer. | S01 | 2026-10-09 |
| Condition: confirm the Power and Interest levels of S02 (LOW, HIGH) and S03 (LOW, LOW), and replace the `Pending` text under `## Sign-Off` with the sign-off once the verdict is `Go`. | S01 | 2026-10-09 |
| Optional (language criterion 10): spell out on first use: FURPS+, RACI, README. | S01 | 2026-10-09 |

---

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/qc-stakeholder-analysis.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[BC-001]: ../../business-case.md
[RC-009]: ./rc-009-stakeholder-analysis-re-review.md
