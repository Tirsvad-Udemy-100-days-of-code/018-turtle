# Milestone 002: Square and Dashed Line

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [4b3391b] |

---

## Purpose

This milestone decides whether the first two challenges (Turtle Challenge 1, draw a square, and Turtle Challenge 2, draw a dashed line) work, are tested without a display and can be started from the command line, and whether the turtle abstraction that every later challenge relies on is sound.

## Deliverable

The `mil-002-square-and-dashed-line` branch, opened as one pull request, containing the `Pen` protocol and window helpers, `draw_square`, `draw_dashed_line`, a recording fake turtle for tests, tests for both functions, and the `turtle-challenges` command with the `square` and `dashed-line` challenges.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `draw_square` draws four sides of 100 units, turning 90 degrees after each, as shown by the recording fake turtle | The recorded moves match | Any recorded move differs |
| 2 | `draw_dashed_line` draws the configured number of dashes of 10 units, each followed by a gap of 10 units, with the pen down for each dash and up for each gap, and leaves the pen down when it returns | The recorded moves match | Any recorded move differs |
| 3 | Every number and name used by the two functions comes from `constants.py` | No magic number in the function bodies | A literal constant is found in a function body |
| 4 | `python -m turtle_challenges square` and `python -m turtle_challenges dashed-line` each open a window and draw to completion on Windows PowerShell | S01 confirms both in the review record | Either fails |
| 5 | No test opens a window | The test run passes with no display available | A test needs a display |
| 6 | `python -m pytest`, `ruff check .`, `ruff format --check .`, `mypy` and `doxygen Doxyfile` | All exit 0 with 0 Doxygen warnings | Any fails or warns |
| 7 | Review record against `QC-PY-001` | Verdict Go | Go-with-conditions or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 accepted | Needs the project configuration, package skeleton, test setup and continuous integration |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Challenges 1 and 2 run | O1 in [BC-001] |
| Drawing logic separate from the window | O2 in [BC-001] |
| Source documented with Doxygen | O5 in [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — the second milestone, after the foundation milestone of 2026-10-10 and before the plan ends on 2026-10-21 (Constraints in [BC-001]).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the `Pen` protocol and window helpers | Add `pen.py` with a `Pen` protocol listing the turtle methods the challenges use, and helpers that create the `Screen` (color mode 255) and the `Turtle` named `tim`. The drawing functions take a `Pen`, so tests can pass a fake. The Doxygen comments also explain the import styles of the lecture (`import turtle`, `from turtle import Turtle`, `import turtle as t`) and why the wildcard import is avoided. | No | |
| 2 | Add a recording fake turtle for tests | Add a fake in `tests/` that implements the `Pen` protocol and records every call (move, turn, pen up, pen down, color), so tests assert on the drawing without a window. | No | |
| 3 | Implement draw_square | Implement `draw_square(pen, side_length)`: four times move forward by the side length (100) and turn right 90 degrees, using a `for` loop. The default side length is a constant in `constants.py`. | No | |
| 4 | Implement draw_dashed_line | Implement `draw_dashed_line(pen, dash_count, dash_length)`: for each dash put the pen down and move forward 10, then put the pen up and move forward 10 for the gap. The number of dashes (50) and the lengths are constants; see the open issue on 50 versus 15 in the Project Plan. | No | |
| 5 | Add tests for square and dashed line | Test both functions against the recording fake turtle: number of moves, lengths, turn angles, pen up and pen down order, and rejection of a non-positive length. | No | |
| 6 | Add the command line entry point | Add `cli.py` with `main(argv)` and `__main__.py` so that `python -m turtle_challenges <challenge>` creates the window, runs the named challenge and waits for a click. Register `square` and `dashed-line`; the choices are listed by `--help`. Declare the `turtle-challenges` command in `pyproject.toml`, since it points at `cli.py`. | No | |
| 7 | Review milestone 002 against QC-PY-001 | Review the code and tests against `QC-PY-001`, record the result as an `RC-*` and update the instance in the traceability matrix. | No | |

---

[BC-001]: ../business-case.md
[4b3391b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4b3391b22626b49aca06a7c265c1d0be93d1155d
