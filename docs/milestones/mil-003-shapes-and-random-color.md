# Milestone 003: Shapes and Random Color

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This milestone decides whether Turtle Challenge 3 (draw different shapes, triangle to decagon, in random colors) works and whether the `random_color` helper from the tuple lecture is correct, because the random walk and the spirograph of the last milestone both depend on it.

## Deliverable

The `mil-003-shapes-and-random-color` branch, opened as one pull request, containing `random_color` (an red, green and blue (RGB) tuple), the color palette constant, `draw_shape`, `draw_shapes`, their tests, and the `shapes` challenge in the command line.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `random_color` returns a tuple of three integers, each from 0 to 255 inclusive, and is repeatable with a seeded random generator | All three properties hold in tests | Any property fails |
| 2 | `draw_shape(pen, num_sides)` turns 360 / `num_sides` degrees after each of `num_sides` sides of 100 units | Recorded moves match for 3 to 10 sides | Any recorded move differs |
| 3 | `draw_shape` rejects fewer than 3 sides with `ValueError` | The error is raised | No error, or another exception type |
| 4 | `draw_shapes` draws the shapes with 3 to 10 sides, each in a color chosen from the palette in `constants.py` | Eight shapes, each with a palette color | Any shape missing or off palette |
| 5 | `python -m turtle_challenges shapes` opens a window and draws to completion on Windows PowerShell | S01 confirms in the review record | It fails |
| 6 | `python -m pytest`, `ruff check .`, `ruff format --check .`, `mypy` and `doxygen Doxyfile` | All exit 0 with 0 Doxygen warnings | Any fails or warns |
| 7 | Review record against `QC-PY-001` | Verdict Go | Go-with-conditions or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 accepted | Needs the `Pen` protocol, the fake turtle and the command line entry point |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Challenge 3 and the `random_color` helper run | O1 in [BC-001] |
| Drawing logic separate from the window | O2 in [BC-001] |
| Source documented with Doxygen | O5 in [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-17 — the third milestone, leaving four days for the last milestone before the plan ends on 2026-10-21 (Constraints in [BC-001]).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement random_color | Implement `random_color(rng)` in `colors.py`: three random integers from 0 to 255 returned as a tuple (immutable, so it is safe as a constant-like value). It accepts an optional `random.Random` so tests can seed it. The upper bound comes from `constants.py`. | No | |
| 2 | Add the color palette constant | Add the lecture's list of named colors to `constants.py` as a tuple (for example CornflowerBlue, DarkOrchid, IndianRed, DeepSkyBlue, LightSeaGreen, wheat, SlateGray, SeaGreen) and a helper that picks one with `random.choice`. | No | |
| 3 | Implement draw_shape | Implement `draw_shape(pen, num_sides, side_length)`: the turn angle is 360 divided by the number of sides, repeated for each side with a `for` loop. Fewer than 3 sides raises `ValueError`. | No | |
| 4 | Implement draw_shapes | Implement `draw_shapes(pen, rng)`: loop over 3 to 10 sides, choose a palette color for each shape and call `draw_shape`. The range bounds are constants. | No | |
| 5 | Add tests for random_color, draw_shape and draw_shapes | Test the tuple type and range of `random_color`, repeatability with a seed, the turn angle and side count for every shape from 3 to 10 sides, the `ValueError` for fewer than 3 sides, and the palette use of `draw_shapes`. | No | |
| 6 | Register the shapes challenge in the command line | Add `shapes` to the choices of `python -m turtle_challenges` and to the `--help` text, with a test of the argument parsing. | No | |
| 7 | Review milestone 003 against QC-PY-001 | Review the code and tests against `QC-PY-001`, record the result as an `RC-*` and update the instance in the traceability matrix. | No | |

---

[BC-001]: ../business-case.md
