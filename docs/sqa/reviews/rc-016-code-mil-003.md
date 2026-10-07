# Review Record: Code of Milestone 003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [4d7cc33] |

---

## Artifact Under Review

- Instance reviewed: Python source code of milestone 003 (type `PY`): the Python files that this milestone added or changed, on branch `mil-003-shapes-and-random-color` at commit c695c47
- Checklist used: [QC-PY-001] (`QC-PY-001`, Python Source Code)
- Milestone: [MIL-003], tasks 1 to 6 (#16 to #21); this record is the review task, issue #22
- Scope: full review of the 8 Python files this milestone added or changed: `src/turtle_challenges/__init__.py`, `src/turtle_challenges/cli.py`, `src/turtle_challenges/colors.py`, `src/turtle_challenges/constants.py`, `src/turtle_challenges/shapes.py`, `tests/test_colors.py`, `tests/test_constants.py`, `tests/test_shapes.py`. 
- Toolchain at that commit, run in a clean checkout of the branch: `ruff format --check .` and `ruff check .` exit 0, `mypy` reports no issues in 20 source files, `pytest` reports 66 passed, and `doxygen Doxyfile` prints no warning.
- Language and domain: n/a (technical type)
- Language reviewer: none (n/a)
- Reviewer eligibility: S01 is the author of this code (the assistant wrote it for S01) and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. S01 accepted this deviation in chat on 2026-10-07; it is recorded in the traceability matrix.
- Status of this record: decided on 2026-10-08 by S01, the reviewer. The statuses and evidence are the assistant's assessment from the toolchain, an AST scan and a reading of the code, confirmed by S01.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules `colors` and `shapes`, functions `random_color`, `random_palette_color`, `draw_shape` and `draw_shapes` and the tests are `snake_case`; constants such as `COLOR_PALETTE` and `MIN_POLYGON_SIDES` are `UPPER_SNAKE`. No class is defined. ruff `N` is clean. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`num_sides`, `side_length`, `random_palette_color`); no single-letter names (scan). Short names: `rng` (every docstring explains it as the random generator to draw from), `red`, `green`, `blue`, and `tim`, carried over from `cli.py` (see [RC-015]). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check .` and `ruff check .` exit 0; no `# noqa`, no `# type: ignore`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every parameter and return is annotated (scan: none unannotated); mypy strict is clean. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `draw_shape` raises `ValueError` for fewer than 3 sides or a side that is not positive; no code in this milestone catches an exception. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Scan of the changed files: no mutable default argument and no shadowed builtin (parameters, variables, functions, classes). |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened (scan: no `open(`). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Optional. Every public module and function in `src/` has a docstring (scan: none missing); `doxygen Doxyfile` has 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` call (scan) and no logging; no secret is read. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No class is defined and no design class diagram exists; the tasks are plain technical tasks (see [RC-015] criterion 10). S01 confirmed `N-A` on 2026-10-08. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 66 tests (37 new), named for the behaviour: type, range and seeded repeatability of `random_color`; the turn angle and the side count for each shape from 3 to 10 sides (parametrised); the `ValueError` cases; the palette use of `draw_shapes`. They pass in file order, in reverse order and file by file; no network imports (scan). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Optional. mypy strict reports no issues in 20 source files; `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | N-A | Optional. No dependency changed in this milestone; see [RC-014]. |

## Overall Verdict

Go — all mandatory criteria of `QC-PY-001` pass or are `N-A`. S01 confirmed `N-A` for criterion 10 on 2026-10-08, as in [RC-015].

Reviewer eligibility: S01 is the author of this code and also its reviewer, which the review process does not allow; S01 accepted this deviation in chat on 2026-10-07 and it is recorded in the traceability matrix.

The row of the code in the traceability matrix is updated, and issue #22 closes through the commit message when the pull request that carries it merges into `main`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decision (criterion 10): confirm `N-A` as in [RC-015]. Closed 2026-10-08: S01 accepted. | S01 | 2026-10-17 |
| After the verdict `Go`: update the traceability matrix and close issue #22. Done 2026-10-08: the matrix is updated and the commit message carries `Closes #22`. | S01 | 2026-10-17 |

---

[MIL-003]: ../../milestones/mil-003-shapes-and-random-color.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[RC-014]: ./rc-014-code-mil-001.md
[RC-015]: ./rc-015-code-mil-002.md
[4d7cc33]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4d7cc33cac2c090c663409abb1e7ab0a34d871f5
