# Review Record: Code of Milestone 002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [4d7cc33] |

---

## Artifact Under Review

- Instance reviewed: Python source code of milestone 002 (type `PY`): the Python files that this milestone added or changed, on branch `mil-002-square-and-dashed-line` at commit b3153b9
- Checklist used: [QC-PY-001] (`QC-PY-001`, Python Source Code)
- Milestone: [MIL-002], tasks 1 to 6 (#9 to #14); this record is the review task, issue #15
- Scope: full review of the 14 Python files this milestone added or changed: `src/turtle_challenges/__init__.py`, `src/turtle_challenges/__main__.py`, `src/turtle_challenges/cli.py`, `src/turtle_challenges/constants.py`, `src/turtle_challenges/dashed_line.py`, `src/turtle_challenges/pen.py`, `src/turtle_challenges/square.py`, `src/turtle_challenges/window.py`, `tests/fakes.py`, `tests/test_cli.py`, `tests/test_constants.py`, `tests/test_dashed_line.py`, `tests/test_square.py`, `tests/test_window.py`. 
- Toolchain at that commit, run in a clean checkout of the branch: `ruff format --check .` and `ruff check .` exit 0, `mypy` reports no issues in 16 source files, `pytest` reports 29 passed, and `doxygen Doxyfile` prints no warning.
- Language and domain: n/a (technical type)
- Language reviewer: none (n/a)
- Reviewer eligibility: S01 is the author of this code (the assistant wrote it for S01) and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. S01 accepted this deviation in chat on 2026-10-07; it is recorded in the traceability matrix.
- Status of this record: decided on 2026-10-08 by S01, the reviewer. The statuses and evidence are the assistant's assessment from the toolchain, an AST scan and a reading of the code, confirmed by S01.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules, functions and variables are `snake_case` (`draw_square`, `draw_dashed_line`, `create_window`, `build_parser`). The classes `Pen`, `Window`, `TurtleUnavailableError`, `FakePen` and `FakeWindow` are `PascalCase` and the exception ends in `Error`. Constants are `UPPER_SNAKE`. ruff `N` is clean. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`dash_count`, `gap_length`, `side_length`, `create_pen`); the scan finds no single-letter names. Short names: `pen`, `args`, `argv` (standard) and `tim`. `tim` in `cli.main` is the lecture's name for the turtle and nothing in the code explains it. Judgement call for the reviewer (see the action items). S01 accepted the name `tim` as the course's name on 2026-10-08. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check .` and `ruff check .` exit 0; no `# noqa`, no `# type: ignore`. Recorded exception: `window.py` imports `turtle` inside `create_window` and `create_pen` instead of at the top of the file, which the Python conventions ask for. The reason is stated in the module docstring (importing the package must not need Tk), and no linter rule flags it. S01 accepts the exception (see the action items). S01 accepted this exception on 2026-10-08. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every parameter and return is annotated (scan: none unannotated); mypy strict is clean. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `window.py` raises `TurtleUnavailableError` `from` the `ImportError` (2 raises, both with a cause) and `cli.main` handles it with `parser.exit`. The drawing functions raise `ValueError` for invalid lengths and counts. No bare or broad `except`; nothing is swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Scan of the changed files: no mutable default argument and no shadowed builtin (parameters, variables, functions, classes). |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened (scan: no `open(`). The turtle window is closed by `exitonclick`, the library's own mechanism. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Optional. Every public module, class and function in `src/` has a docstring (scan: none missing), and `doxygen Doxyfile` has 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` call (scan: 0) and no logging. `cli.main` reports a missing Tk on standard error through `parser.exit`. No secret is read. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No design class diagram exists, and the tasks are plain technical tasks. The only classes are the protocols `Pen` and `Window` and the test doubles `FakePen` and `FakeWindow`; each traces to a task row (MIL-002 tasks 1 and 2, issues #9 and #10). Judgement call: a strict reading would fail this criterion. S01 confirmed `N-A` on 2026-10-08. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 29 tests (26 new), named for the behaviour (for example `test_draw_square_rejects_a_side_that_is_not_positive`). They pass in file order, in reverse order and file by file, and no test imports a network module (scan). Gaps: the successful path of `create_window` and `create_pen` needs a display and has no automated test (only the missing-Tk path does), and `__main__.py` (two lines) has none. A script has run the challenges against the real `turtle` library without error. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Optional. mypy strict reports no issues in 16 source files; `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | N-A | Optional. No dependency changed in this milestone; see [RC-014]. |

## Overall Verdict

Go — all mandatory criteria of `QC-PY-001` pass or are `N-A`. S01 accepted the three points that needed judgement on 2026-10-08: the imports inside `create_window` and `create_pen` as a documented exception, the name `tim` as the course's name, and `N-A` for criterion 10 because the project has no design artifacts.

Reviewer eligibility: S01 is the author of this code and also its reviewer, which the review process does not allow; S01 accepted this deviation in chat on 2026-10-07 and it is recorded in the traceability matrix.

The row of the code in the traceability matrix is updated, and issue #15 closes through the commit message when the pull request that carries it merges into `main`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Decision (criterion 3): accept the imports inside `create_window` and `create_pen` as a documented exception to "imports at the top". Closed 2026-10-08: S01 accepted. | S01 | 2026-10-14 |
| Decision (criterion 2): rename `tim` to `pen` in `cli.py` and in the README example, or accept it as the course's name. Closed 2026-10-08: S01 accepted. | S01 | 2026-10-14 |
| Decision (criterion 10): confirm `N-A`, because the project has no design artifacts, or require a design class diagram. Closed 2026-10-08: S01 accepted. | S01 | 2026-10-14 |
| After the verdict `Go`: update the traceability matrix and close issue #15. Done 2026-10-08: the matrix is updated and the commit message carries `Closes #15`. | S01 | 2026-10-14 |

---

[MIL-002]: ../../milestones/mil-002-square-and-dashed-line.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[RC-014]: ./rc-014-code-mil-001.md
[4d7cc33]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4d7cc33cac2c090c663409abb1e7ab0a34d871f5
