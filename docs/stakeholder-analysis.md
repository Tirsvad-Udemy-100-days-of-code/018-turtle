# Stakeholder Analysis: Turtle Challenges

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [4b3391b] |

---

## Purpose

This analysis identifies who has influence over, or interest in, the Turtle Challenges project, and fixes the stakeholder IDs (`S01` to `S03`) that every other artifact cites for ownership, review and RACI (responsible, accountable, consulted and informed) assignments. It uses a power/interest grid (Mendelow) to choose how closely each stakeholder is managed, and FURPS+ (functionality, usability, reliability, performance and supportability, plus constraints) to express each concern as a quality attribute.

The power and interest levels of S01 are given by S01. The levels of S02 and S03 are the author's classification from their stated deliverables; S01 confirms or corrects them in the sign-off.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad (personal project) | HIGH | HIGH | Manage Closely | Solve the five challenges and practise a complete, reviewed workflow |
| S02 | Udemy coursists | Course participants who share code and compare solutions | Udemy, *100 Days of Code* community | LOW | HIGH | Keep Informed | Readable, runnable code that keeps the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** S01 decides scope, writes the code, reviews every artifact and pull request, and is the only person who can accept a milestone. Power and interest are both high.
- **Keep Informed (S02):** S02 cannot change the project, but they use its result directly and compare it with their own. Their interest is high, so the README and the function names must serve them. Their power is low because no decision depends on them.
- **Monitor (S03):** S03 arrives from a search or a topic page and may never return. Their interest in any one repository is low and they have no influence on it. The repository description, topics and README are the only contact, so these must be correct without further attention.
- **Keep Satisfied:** no stakeholder is classified here; no one has high power and low interest.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Every step is planned, reviewed and traceable to a pull request | Supportability |
| S01 | The agreed constraints are met (Python 3.13 or later, venv, pytest, `constants.py`, `pyproject.toml`, Doxygen) | Design constraint |
| S01 | The tokens in `.env` stay private | Security (Functionality) |
| S02 | The five challenges run and draw what the lecture describes | Functionality |
| S02 | The code is readable and keeps the assignment's function names | Usability |
| S02 | The README shows how to set up and run on their operating system | Usability, Supportability |
| S03 | The repository states what it is through its description and topics | Usability |
| S03 | Cloning it needs nothing beyond the Python standard library | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat with the assistant and pull request review on the git host | At every milestone | Milestone document, review record, pull request | MIL-001, MIL-002, MIL-003, MIL-004 |
| S02 | `README.md` on the repository page | Updated when run instructions change; final at the last milestone | Set-up, run and test instructions | MIL-001, MIL-004 |
| S03 | Repository description, topics and `README.md` | Set once at the first milestone; checked at the last | Description, topics, overview | MIL-001, MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 expects the course's function names and call style; S01 needs the functions testable without a window, which requires passing the turtle as an argument | S01, S02 | Keep every assignment function name; add the turtle as an explicit parameter and document the difference in the README and in the Doxygen comments |
| S03 wants no runtime dependencies; S01 wants a formatter, linter, type checker and test runner | S01, S03 | Declare the tools only as development dependencies; `dependencies` stays empty |
| S01 holds tokens in `.env` for the git hosts; S03 can read everything that is committed | S01, S03 | `.env` is listed in `.gitignore`; no code imports or tests it; it is never committed |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Every step is planned, reviewed and traceable | O7 in [BC-001] |
| S01 | The agreed constraints are met | O3, O4 and O5 in [BC-001] |
| S01 | The tokens in `.env` stay private | O6 in [BC-001] and the Risks table |
| S02 | The challenges run and draw what the lecture describes | O1 in [BC-001] |
| S02 | Readable code with the assignment's function names | O1 and O2 in [BC-001] |
| S02 | The README shows how to set up and run | O3 in [BC-001] |
| S03 | Description, topics and README | O6 in [BC-001] |
| S03 | No runtime dependencies | O4 in [BC-001] |

## Sign-Off

Signed off by S01 on 2026-10-07, with the `Go` verdict of [RC-009].

---

[BC-001]: ./business-case.md
[RC-009]: ./sqa/reviews/rc-009-stakeholder-analysis-re-review.md
[4b3391b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4b3391b22626b49aca06a7c265c1d0be93d1155d
