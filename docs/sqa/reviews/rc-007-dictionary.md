# Review Record: Domain Dictionary

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-007 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] (`QC-DICT-001`, Domain Dictionary), together with [QC-LANG-001] because the type is written in the PO language
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (S01 confirmed on 2026-10-07 that S01 reads English and knows the IT domain)
- Status of this record: decided on 2026-10-07 by S01, the reviewer. The statuses and evidence are the assistant's assessment, confirmed by S01.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All eight rows have a PO term, a language, an IT term and a definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Eight pairs, checked row by row: each PO term has one IT term and each IT term one PO term. For `challenge` the word is the same on both sides on purpose (the code uses it as a name). |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists: no use case was written (see the open issues of the Project Plan). |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists. The source code uses the IT terms and keeps the assignment's function names, as the Rules say. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Optional. Every definition is English and one sentence. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Optional. The artifact types named (BC, SA, PP, MIL, PY) all exist in the project. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | `Language` is `en` and `Domain` is `it`, as in the registry; every row's language is `en`. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has a `Language` row (`en`) and a `Domain` row (`it`); neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives this type `IT Professional English`; the Rules and definitions are short technical sentences. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | This document is the dictionary: the other documents are checked against it in the delta re-reviews [RC-008] to [RC-013]. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are English and unchanged from the template. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | One file per artifact: `find docs -name '*.*.md'` finds no translated twin. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Initial version: there is no earlier accepted version whose language could have changed. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | Confirmed by S01 in chat on 2026-10-07: S01 reads English and knows the IT domain. S01 is also the author (see the verdict). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Optional. PO is spelled out in the Purpose, and RGB in the table row where it first appears. The other short forms are artifact type names (BC, SA, PP, MIL, PY, DICT), which the artifact catalog defines. |

## Overall Verdict

Go — all 5 applicable criteria of `QC-DICT-001` pass (criteria 3 and 4 are `N-A` because no Domain Model or design artifact exists), and the language criteria pass, criterion 9 on S01's confirmation.

Reviewer eligibility: S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. S01 accepted this deviation in chat on 2026-10-07: the project has one person, and no governance document (`GOV`) exists to say otherwise.

Because this is a `Go`, criterion 5 of the six delta re-reviews, [RC-008] to [RC-013], stands. The latest Version History row of `DICT-001` is set to `Accepted`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition (language criterion 9): confirm on this record that the reviewer reads English and knows the IT domain, then change the status of row 9 to `Pass` (or name a language reviewer). Closed: S01 confirmed on 2026-10-07 and row 9 is `Pass`. | S01 | 2026-10-09 |
| Condition: accept or change the reviewer assignment. S01 is the author of this artifact and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. Record the deviation as accepted (single-person project) or name another reviewer. Closed: S01 accepted the deviation on 2026-10-07. | S01 | 2026-10-09 |
| After the verdict `Go`: set the latest Version History row of `DICT-001` to `Accepted` and update the traceability matrix. Done on 2026-10-07. | S01 | 2026-10-09 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[RC-008]: ./rc-008-business-case-re-review.md
[RC-009]: ./rc-009-stakeholder-analysis-re-review.md
[RC-010]: ./rc-010-mil-001-re-review.md
[RC-011]: ./rc-011-mil-002-re-review.md
[RC-012]: ./rc-012-mil-003-re-review.md
[RC-013]: ./rc-013-mil-004-re-review.md
