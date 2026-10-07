# Traceability Matrix: Turtle Challenges

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | [SA-001] | [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [DICT-001] | [RC-008] (draft re-review of [RC-001], Go) |
| [SA-001] | SA | en | it | - | [BC-001], [DICT-001] | [RC-009] (draft re-review of [RC-002], Go) |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | - |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-007] (Go) |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-010] (draft re-review of [RC-003], Go) |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-011] (draft re-review of [RC-004], Go) |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | [MIL-004] | [RC-012] (draft re-review of [RC-005], Go) |
| [MIL-004] | MIL | en | it | [BC-001], [MIL-003] | - | [RC-013] (draft re-review of [RC-006], Go) |

## Coverage Notes

- `-` in Upstream means foundational ([SA-001] is the foundation of the stakeholder IDs); in Downstream it means nothing is built on it yet ([MIL-004] is the last gateway; the source code under `src/` is not an instance of this matrix); in Last Reviewed it means no `RC-*` exists.
- [PP-001] has no `RC-*` because the Project Plan has no QC checklist; the Product Owner accepts it directly.
- Each artifact lists its latest review record: the delta re-review ([RC-008] to [RC-013]) of the first review ([RC-001] to [RC-006]), or [RC-007] for [DICT-001]. All of them ended in `Go` on 2026-10-07.
- S01 is the author and also the reviewer of every artifact. The review process does not allow this; S01 accepted the deviation in chat on 2026-10-07 because the project has one person and no governance document (`GOV`) exists.
- No instance exists yet for the types KPI, RA, BMC, BPMN, UCD, US, UC, DM, SSD, OC, SD, DCD, ERD, ADR, GOV or TRR. One of them matters for the open reviews: GOV (the rule that the reviewer is not the author).

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-foundation.md
[MIL-002]: ../milestones/mil-002-square-and-dashed-line.md
[MIL-003]: ../milestones/mil-003-shapes-and-random-color.md
[MIL-004]: ../milestones/mil-004-random-walk-and-spirograph.md
[DICT-001]: ../dictionary.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-mil-001-project-foundation.md
[RC-004]: ./reviews/rc-004-mil-002-square-and-dashed-line.md
[RC-005]: ./reviews/rc-005-mil-003-shapes-and-random-color.md
[RC-006]: ./reviews/rc-006-mil-004-random-walk-and-spirograph.md
[RC-007]: ./reviews/rc-007-dictionary.md
[RC-008]: ./reviews/rc-008-business-case-re-review.md
[RC-009]: ./reviews/rc-009-stakeholder-analysis-re-review.md
[RC-010]: ./reviews/rc-010-mil-001-re-review.md
[RC-011]: ./reviews/rc-011-mil-002-re-review.md
[RC-012]: ./reviews/rc-012-mil-003-re-review.md
[RC-013]: ./reviews/rc-013-mil-004-re-review.md
