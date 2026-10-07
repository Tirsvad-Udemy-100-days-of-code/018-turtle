# Review Record: Code of Milestone 001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [MIL-001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [4d7cc33] |

---

## Artifact Under Review

- Instance reviewed: Python source code of milestone 001 (type `PY`): the Python files that this milestone added or changed, on branch `mil-001-project-foundation` at commit d38f114
- Checklist used: [QC-PY-001] (`QC-PY-001`, Python Source Code)
- Milestone: [MIL-001], tasks 1 to 3 (#1 to #3), plus the configuration of tasks 1 and 2 (`pyproject.toml`, `.gitignore`); this record is the review task, issue #8
- Scope: full review of the 4 Python files this milestone added or changed: `src/turtle_challenges/__init__.py`, `src/turtle_challenges/constants.py`, `tests/__init__.py`, `tests/test_package.py`. `pyproject.toml` and `.gitignore` are reviewed as the milestone's configuration.
- Toolchain at that commit, run in a clean checkout of the branch: `ruff format --check .` and `ruff check .` exit 0, `mypy` reports no issues in 4 source files, `pytest` reports 3 passed, and `doxygen Doxyfile` prints no warning.
- Language and domain: n/a (technical type)
- Language reviewer: none (n/a)
- Reviewer eligibility: S01 is the author of this code (the assistant wrote it for S01) and also its reviewer, which `framework/process/review-checklist-process.md` does not allow. S01 accepted this deviation in chat on 2026-10-07; it is recorded in the traceability matrix.
- Status of this record: decided on 2026-10-08 by S01, the reviewer. The statuses and evidence are the assistant's assessment from the toolchain, an AST scan and a reading of the code, confirmed by S01.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | The package and modules (`turtle_challenges`, `constants`, `test_package`) are `snake_case`, the constants `WINDOW_TITLE` and `COLOR_MODE` are `UPPER_SNAKE`, the test functions are `snake_case`. The ruff naming rules (`N`) are on and report nothing. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | `WINDOW_TITLE` and `COLOR_MODE` say what they hold, and each constant has a comment that says what it is for. The scan finds no single-letter and no short names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check .` and `ruff check .` exit 0 with the rules `ANN`, `B`, `E`, `F`, `I`, `N`, `SIM`, `UP` and `W`; `pyproject.toml` commits the configuration. No `# noqa` and no `# type: ignore` (scan). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | The only functions are the three smoke tests, annotated `-> None`; ruff `ANN` and mypy strict report nothing. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | No code in this milestone raises or catches an exception. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | Scan of the changed files: no mutable default argument and no shadowed builtin (parameters, variables, functions, classes). |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened (scan: no `open(`). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Optional. `__init__.py` and `constants.py` have module docstrings and every constant has a Doxygen comment. `doxygen Doxyfile` has 0 warnings, and a warning fails the build. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` call (scan) and no logging; nothing reads `.env` or any other secret. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No class or operation is defined, and no design class diagram exists: the milestone's tasks are plain technical tasks (`Needs its own Use Case/User Story?` is No). S01 confirmed `N-A` on 2026-10-08. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_package.py` has 3 smoke tests named for the behaviour (the package imports and is documented, the color mode, the window title). They pass alone and in reverse order and use no network (scan). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Optional. `mypy` (strict, set in `pyproject.toml`) reports no issues in 4 source files; `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Fail | Optional. `pyproject.toml` declares `mypy>=1.13`, `pytest>=8.3`, `ruff>=0.8` and the build backend `setuptools>=77` with lower bounds only; nothing is pinned and there is no lockfile or constraints file. The runtime dependency list is empty, so no dependency is unused. S01 accepted lower bounds on 2026-10-08, so this optional failure stays recorded and needs no action. |

## Overall Verdict

Go — all mandatory criteria of `QC-PY-001` pass or are `N-A`. The optional criterion 13 fails (lower bounds only); S01 accepted that on 2026-10-08, so it needs no action.

Reviewer eligibility: S01 is the author of this code and also its reviewer, which the review process does not allow; S01 accepted this deviation in chat on 2026-10-07 and it is recorded in the traceability matrix.

The row of the code in the traceability matrix is updated, and issue #8 closes through the commit message when the pull request that carries it merges into `main`.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Optional (criterion 13): pin the development tools (exact versions or a constraints file), or record that lower bounds are accepted. Closed 2026-10-08: S01 accepted lower bounds. | S01 | 2026-10-10 |
| After the verdict `Go`: update the traceability matrix and close issue #8. Done 2026-10-08: the matrix is updated and the commit message carries `Closes #8`. | S01 | 2026-10-10 |

---

[MIL-001]: ../../milestones/mil-001-project-foundation.md
[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[4d7cc33]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/4d7cc33cac2c090c663409abb1e7ab0a34d871f5
