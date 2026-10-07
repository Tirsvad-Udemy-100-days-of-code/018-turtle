# Milestone 004: Random Walk and Spirograph

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This milestone decides whether the last two challenges (Turtle Challenge 4, generate a random walk, and Turtle Challenge 5, draw a spirograph) work and whether the whole repository is ready to be shared: all five challenges run, the README is complete and checked from a fresh clone, and every success criterion of the Business Case is met.

## Deliverable

The `mil-004-random-walk-and-spirograph` branch, opened as one pull request, containing `random_walk`, `draw_spirograph`, their tests, the `random-walk` and `spirograph` challenges in the command line, and the final `README.md` with the Run section for all five challenges.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `random_walk` takes the configured number of steps (200), each of the same distance, each in a heading from the north, east, south and west list, and each in an red, green and blue (RGB) color from `random_color` | Recorded moves match with a seeded generator | Any recorded move differs |
| 2 | `random_walk` sets the pen size and the speed from constants | Both are recorded before the first move | Either is missing |
| 3 | `draw_spirograph(pen, size_of_gap)` draws `int(360 / size_of_gap)` circles, each in an RGB color, turning the heading by the gap after each circle | Circle count, color and heading changes match | Any differs |
| 4 | `draw_spirograph` rejects a gap that is zero or negative with `ValueError` and never passes a float to `range` | The error is raised; a gap of 7 does not raise `TypeError` | A float reaches `range` |
| 5 | `python -m turtle_challenges random-walk` and `python -m turtle_challenges spirograph` open a window and draw to completion on Windows PowerShell | S01 confirms both in the review record | Either fails |
| 6 | Business Case success criteria 1 to 7 | Every criterion met, evidence in the review record | Any criterion not met |
| 7 | A fresh clone follows only the README (set-up, run, test, build the documentation) on Windows PowerShell | Every step works as written | A step fails or is missing |
| 8 | `python -m pytest`, `ruff check .`, `ruff format --check .`, `mypy` and `doxygen Doxyfile` | All exit 0 with 0 Doxygen warnings | Any fails or warns |
| 9 | Review record against `QC-PY-001` | Verdict Go | Go-with-conditions or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 accepted | Needs `random_color` and the command line entry point |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Challenges 4 and 5 run | O1 in [BC-001] |
| Set-up and run guide complete | O3 in [BC-001] |
| Repository ready to share | O6 in [BC-001] |
| Every pull request closes its issues | O7 in [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 — the last milestone, on the day the plan ends (Constraints in [BC-001]).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement random_walk | Implement `random_walk(pen, steps, distance, rng)`: set the pen size and speed, then for each of 200 steps choose a heading from the list of 0, 90, 180 and 270 degrees, give the line a `random_color` RGB value and move forward by a fixed distance. The directions are a tuple constant. | No | |
| 2 | Implement draw_spirograph | Implement `draw_spirograph(pen, size_of_gap, radius, rng)`: draw `int(360 / size_of_gap)` circles, each in a `random_color` RGB value, and after each circle set the heading to the current heading plus the gap. A zero or negative gap raises `ValueError`; the `int` conversion avoids the float error that `range` raises. | No | |
| 3 | Add tests for random_walk and draw_spirograph | Test the recorded moves of both functions with a seeded generator and the recording fake turtle: step count, distance, headings drawn from the list, RGB values in range, circle count, heading change and the `ValueError` for an invalid gap. | No | |
| 4 | Register random-walk and spirograph in the command line | Add `random-walk` and `spirograph` to the choices of `python -m turtle_challenges`, with a `--gap` option for the spirograph, and test the argument parsing. | No | |
| 5 | Complete the README Run section and verify it from a fresh clone | Document the command for each of the five challenges and the `--gap` option, then follow the README from an empty folder on Windows PowerShell and record the result. Debian and macOS steps are documented but not verified by S01; the README says so. | No | |
| 6 | Verify the Business Case success criteria | Check each of the seven success criteria of the Business Case, record the evidence (command output, repository page) in the review record, and update the Project Plan if a date moved. | No | |
| 7 | Review milestone 004 against QC-PY-001 | Review the code and tests against `QC-PY-001`, record the result as an `RC-*` and update the instance in the traceability matrix. | No | |

---

[BC-001]: ../business-case.md
