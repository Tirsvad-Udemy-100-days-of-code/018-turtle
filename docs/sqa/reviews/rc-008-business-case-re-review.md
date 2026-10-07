# Review Record: Business Case, delta re-review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [BC-001], [RC-001], [DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-LANG-001] (`QC-LANG-001`, Language and Domain); the checklist of the type, `QC-BC-001`, is not repeated
- Scope: delta re-review of criteria 5, 9 and 10 of `QC-LANG-001`. Reason: the first review, [RC-001], failed these criteria; [DICT-001] now exists, the abbreviations are spelled out on first use, and the prose of the document follows the dictionary. Earlier record: [RC-001]. The verdict covers the whole artifact only if the other rows of [RC-001] still hold: they do, because the changes since then are wording only (terms and abbreviations); the content, scope, criteria and conclusions of the document are unchanged.
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (S01 confirmed on 2026-10-07 that S01 reads English and knows the IT domain)
- Status of this record: decided on 2026-10-07 by S01, the reviewer. The statuses and evidence are the assistant's assessment, confirmed by S01.

## Checklist Results

Not repeated in this delta re-review: the 8 criteria of `QC-BC-001` hold as recorded in [RC-001].

## Language and Domain Results

Only the criteria of the delta (5, 9 and 10); the other rows of [RC-001] hold.

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | [DICT-001] exists with eight terms. A scan of the prose of this document (outside code spans, fenced blocks and the template's own headings) finds none of the words the dictionary forbids: "pen" for the turtle, "gate", "gateway" or "phase". The turtle library's "pen up", "pen down" and "pen size" and the proper name "plan-first gate" remain, as the dictionary Rules allow. Holds only if [DICT-001] is accepted (see [RC-007]). |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by S01 in chat on 2026-10-07: S01 reads English and knows the IT domain. S01 is also the author (see the verdict). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Optional. Spelled out on first use, checked by a scan of the document: SQA, QC, ISO/IEC, PEP, RGB. No other abbreviation remains except file names (README) and artifact IDs. |

## Overall Verdict

Go — criteria 5, 9 and 10 of `QC-LANG-001` pass (criterion 9 on S01's confirmation, criterion 5 because [DICT-001] is accepted in [RC-007]). The other rows of [RC-001] still hold, since the changes since then are wording only, so the verdict covers the whole artifact.

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

[BC-001]: ../../business-case.md
[RC-001]: ./rc-001-business-case.md
[DICT-001]: ../../dictionary.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[RC-007]: ./rc-007-dictionary.md
