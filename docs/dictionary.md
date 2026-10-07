# Domain Dictionary: Turtle Challenges

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [4b3391b] |

---

## Purpose and Scope

This dictionary maps each term the Product Owner (PO) uses in the project documents to the professional IT term used in the source code. The PO language is English (`en`) and the domain is software and IT (`it`), as the `Languages` section of `docs/artifact-registry.md` says. It covers the terms of [BC-001], [SA-001], the Project Plan, the milestones and the review records, and the names in `src/` and `tests/`. It lists only the terms that have a different word on each side, plus the central term "challenge", whose word is the same on both sides because the code uses it as a name.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| challenge | en | `challenge` | One of the five exercises of the course, started by name from the command line. | BC, SA, PP, MIL | PY |
| turtle | en | `Pen` | The thing that draws on the screen: it moves, turns and leaves a line behind it. | BC, SA, PP, MIL | PY |
| window | en | `Window` | The window on the screen in which the turtle draws. | BC, SA, MIL | PY |
| shape | en | regular polygon | A closed figure with equal sides, such as a triangle or a decagon, that the turtle draws in challenge 3. | BC, MIL | PY |
| random color | en | RGB (red, green, blue) tuple | A color picked at random and kept as three whole numbers from 0 to 255 for red, green and blue. | BC, MIL | PY |
| milestone | en | gateway | A reviewed step of the plan that ends with a Go or No-Go decision, kept in one `MIL-*` document. | BC, SA, PP, MIL | PP, MIL |
| task | en | issue | One row of the task table of a milestone, which becomes one issue on the git host. | BC, PP, MIL | PP |
| source documentation | en | Doxygen output | The web pages that Doxygen builds from the comments in the source code. | BC, MIL | PY |

## Rules

- The PO term is used in the prose of the documents that are written in the PO language (BC, SA, PP, MIL, DICT). The IT term is used in names inside the source code and the tests, and in the text of those documents only where it is written as a code name between backticks (for example `Pen`).
- One IT term per PO term and one PO term per IT term; no synonyms. In prose, say "turtle", not "pen"; say "milestone", not "gate", "gateway" or "phase".
- The headings and table headers that come from the framework templates keep the framework's words (`Gateway Schedule`, `Phase / Milestone`, `Open Issues`). Structural vocabulary stays English and unchanged, because the scripts read it.
- The names of the assignment's functions (`draw_square`, `draw_dashed_line`, `draw_shape`, `draw_shapes`, `random_color`, `random_walk`, `draw_spirograph`) stay exactly as the course gives them, even where the name uses the PO term (for example `draw_shape` for a regular polygon), because the people who compare solutions look for these names.
- The turtle library's own words "pen up", "pen down" and "pen size" name the line state of the turtle. They stay in prose and do not mean the turtle. The code's `Pen` is the turtle itself; this homonym is recorded here on purpose.
- Names of tools and of git host objects (pull request, branch, Doxygen, pytest, ruff, mypy, Gitea, GitHub) and the framework's rule "plan-first gate" are proper names, not terms of this dictionary.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[4b3391b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4b3391b22626b49aca06a7c265c1d0be93d1155d
