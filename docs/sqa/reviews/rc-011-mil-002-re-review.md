# Review Record: Milestone 002, delta re-review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-002], [RC-004], [DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [4b3391b] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-LANG-001] (`QC-LANG-001`, Language and Domain); the checklist of the type, `QC-MIL-001`, is not repeated
- Scope: delta re-review of criteria 5 and 9 of `QC-LANG-001`. Reason: the first review, [RC-004], failed these criteria; [DICT-001] now exists, and the prose of the document follows the dictionary. Earlier record: [RC-004]. The verdict covers the whole artifact only if the other rows of [RC-004] still hold: they do, because the changes since then are wording only (terms); the content, scope, criteria and conclusions of the document are unchanged.
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (S01 confirmed on 2026-10-07 that S01 reads English and knows the IT domain)
- Status of this record: decided on 2026-10-07 by S01, the reviewer. The statuses and evidence are the assistant's assessment, confirmed by S01.

## Checklist Results

Not repeated in this delta re-review: the 6 criteria of `QC-MIL-001` hold as recorded in [RC-004].

## Language and Domain Results

Only the criteria of the delta (5 and 9); the other rows of [RC-004] hold.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | [DICT-001] exists with eight terms. A scan of the prose of this document (outside code spans, fenced blocks and the template's own headings) finds none of the words the dictionary forbids: "pen" for the turtle, "gate", "gateway" or "phase". The turtle library's "pen up", "pen down" and "pen size" and the proper name "plan-first gate" remain, as the dictionary Rules allow. Holds only if [DICT-001] is accepted (see [RC-007]). |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by S01 in chat on 2026-10-07: S01 reads English and knows the IT domain. S01 is also the author (see the verdict). |

## Overall Verdict

Go — criteria 5 and 9 of `QC-LANG-001` pass (criterion 9 on S01's confirmation, criterion 5 because [DICT-001] is accepted in [RC-007]). The other rows of [RC-004] still hold, since the changes since then are wording only, so the verdict covers the whole artifact.

Reviewer eligibility: S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. S01 accepted this deviation in chat on 2026-10-07: the project has one person, and no governance document (`GOV`) exists to say otherwise.

The latest Version History row of the artifact is set to `Accepted` and the traceability matrix is updated.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition (language criterion 9): confirm on this record that the reviewer reads English and knows the IT domain, then change the status of row 9 to `Pass` (or name a language reviewer). Closed: S01 confirmed on 2026-10-07 and row 9 is `Pass`. | S01 | 2026-10-09 |
| Condition: accept or change the reviewer assignment. S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. Record the deviation as accepted (single-person project) or name another reviewer. Closed: S01 accepted the deviation on 2026-10-07. | S01 | 2026-10-09 |
| Condition (language criterion 5): `DICT-001` must be `Accepted`; this `Pass` stands only if its own review, [RC-007], ends in `Go`. Closed: [RC-007] ends in `Go`. | S01 | 2026-10-09 |
| After the verdict `Go`: set the latest Version History row of the artifact to `Accepted` and update its row in the traceability matrix. Done on 2026-10-07. | S01 | 2026-10-09 |

---

[MIL-002]: ../../milestones/mil-002-square-and-dashed-line.md
[RC-004]: ./rc-004-mil-002-square-and-dashed-line.md
[DICT-001]: ../../dictionary.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[RC-007]: ./rc-007-dictionary.md
[4b3391b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4b3391b22626b49aca06a7c265c1d0be93d1155d
