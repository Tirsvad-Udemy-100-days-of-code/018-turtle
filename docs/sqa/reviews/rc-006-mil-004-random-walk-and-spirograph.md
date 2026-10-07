# Review Record: Milestone 004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-006 |
| CrossReference | [MIL-004], [QC-MIL-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [4b3391b] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-MIL-001] (`QC-MIL-001`, Milestones / Gateways), together with [QC-LANG-001] because the type is written in the PO language
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (not confirmed at the time of this review; S01 confirmed it in [RC-013])
- Status of this record: closed on 2026-10-07. The statuses and evidence are the assistant's assessment of the first version of the document; the criteria that failed were re-reviewed in [RC-013], which ends in `Go`.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | The Deliverable section lists `random_walk`, `draw_spirograph`, their tests, the two commands and the final README. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Nine criteria with a Go and a No-Go condition. Checked on the finished working tree on 2026-10-07: criteria 1 to 4 and 8 hold. Criterion 5 (S01 runs both commands), 6 (all seven Business Case success criteria, of which 5 and 7 need S01's fresh-clone run), 7 (fresh clone from the README) and 9 (code review record) are not done yet. |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Optional. The Dependencies table names what must be accepted first. |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Maps to O1, O3, O6 and O7 of [BC-001]; all four exist. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner S01 and approving reviewer S01 are identified. They are the same person, which the first action item covers. |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | 2026-10-21 equals the Business Case deadline: consistent, with no slack. The Project Plan says what a No-Go does to this date. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has a `Language` row (`en`) and a `Domain` row (`it`); neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. The author wrote it in English; the reviewer confirms by reading it. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives this type `IT Executive English`. Judgement call for the reviewer: the Tasks table and the Go / No-Go criteria carry developer-level detail (function names, commands) although the registry gives milestones the executive register; the only reader is S01, who is also the developer. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Fail | No Domain Dictionary exists (`docs/dictionary.md` is absent), so the domain terms cannot be checked against one. `N-A` is not allowed for this criterion. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are English and unchanged from the template. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | One file per artifact: `find docs -name '*.*.md'` finds no translated twin. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Initial version: there is no earlier accepted version whose language could have changed. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Fail | Not yet confirmed. No record shows that the reviewer reads English and knows the IT domain (there is no reviewer training record, `TRR`). S01 confirms on this record or names a language reviewer. `N-A` is not allowed for this criterion. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Optional. Not spelled out on first use: README, RGB. |

## Overall Verdict

Go-with-conditions — the criteria of the type's checklist pass, and the language checklist fails criteria 5 and 9 (and 10 where listed), which the review process turns into conditions. The conditions were closed and re-reviewed in [RC-013], which ends in `Go` and covers the whole artifact.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition: accept or change the reviewer assignment. S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. Either record the deviation as accepted (this is a single-person project) or name another reviewer. | S01 | 2026-10-09 |
| Condition (language criterion 5): decide how the domain terms are checked: draft `DICT-001` (`docs/dictionary.md`) with the terms the documents use and review it against `QC-DICT-001`, or record an accepted deviation. | S01 | 2026-10-09 |
| Condition (language criterion 9): confirm on this record that the reviewer reads English and knows the IT domain, or name a language reviewer. | S01 | 2026-10-09 |
| Optional (language criterion 10): spell out on first use: README, RGB. | S01 | 2026-10-09 |

---

[MIL-004]: ../../milestones/mil-004-random-walk-and-spirograph.md
[QC-MIL-001]: ../../../framework/qc/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[BC-001]: ../../business-case.md
[RC-013]: ./rc-013-mil-004-re-review.md
[4b3391b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4b3391b22626b49aca06a7c265c1d0be93d1155d
