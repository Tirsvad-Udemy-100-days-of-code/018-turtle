# Business Case: Turtle Challenges

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Day 18 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp* teaches Python through turtle graphics. This project turns its five challenges (draw a square, draw a dashed line, draw different shapes, generate a random walk, draw a spirograph) into one small, readable and tested Python repository. The repository has no runtime dependencies, installs into a local virtual environment, documents its source with Doxygen and runs its tests in continuous integration. It serves S01, S02 and S03 (see [SA-001]). The investment is a few days of S01's time; the return is a reference repository and practice of a complete engineering workflow. The recommendation is to proceed.

## Methodological and Standards Foundation

- **Methodology:** the software quality assurance (SQA) and quality control (QC) framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues, then code, each step reviewed before the next.
- **Quality standard:** characteristics of the standard of the International Organization for Standardization and the International Electrotechnical Commission (ISO/IEC), number 25010:2023, tag every quality control criterion.
- **Code conventions:** Python Enhancement Proposals (PEP) 8, 257 and 484 for Python, reviewed against `QC-PY-001` before each pull request.
- **Source documentation:** Doxygen comments in the source, built from a `Doxyfile`.

## Problem Statement

- Course exercises written in a single script are hard to read, hard to run on another machine and impossible to test, because drawing code is mixed with window setup.
- Without a stated environment, a participant who clones a solution does not know which Python version, which packages or which operating-system tools (for example Tk) it needs.
- A repository without a description, topics and README is not found, and gives a viewer no reason to open it.
- Work that is not planned in steps leaves no record of what was done and when.

## Business Opportunity

A compact, well-presented solution repository lets S02 compare solutions against runnable code that keeps the assignment's function names, and lets S03 judge the repository from its description, topics and README alone. It also gives S01 a template repository for the later days of the course: the same layout, tooling and workflow can be reused for each day.

## Objectives

| ID | Objective |
| --- | --- |
| O1 | Deliver the five challenges as runnable code: `draw_square`, `draw_dashed_line`, `draw_shape`, `random_walk` and `draw_spirograph`, with the lecture's `random_color` helper. |
| O2 | Separate drawing logic from window creation so that every function can be tested without a display. |
| O3 | Give a reproducible set-up and run guide for Windows PowerShell, Linux Debian and macOS, using a local `.venv` and an upgraded `pip`. |
| O4 | Keep the runtime dependency list empty; only the Python standard library is used at run time. |
| O5 | Document the source with Doxygen comments and provide a `Doxyfile` that builds without warnings. |
| O6 | Present the repository: description, topics, README with the agreed template, Python `.gitignore` and licence. |
| O7 | Keep a trail of the work: one branch and one pull request per milestone, each pull request closing the issues it completes. |

## Scope

### In Scope

- The five turtle challenges named in O1 and the `random_color` helper (tuples of red, green and blue (RGB) values, color mode 255).
- A `src/`, `tests/`, `docs/` folder structure, `constants.py` for constants, `pyproject.toml` for configuration.
- Tests with pytest; formatting and linting with ruff; type checking with mypy (development tools only).
- A continuous integration workflow that installs the project, runs the tests, linter and type checker, and builds the source documentation.
- A `Doxyfile` and a documented command to build the source documentation.
- A README that follows the agreed template, including set-up for Windows PowerShell, Linux Debian and macOS.
- Description and topics on the repository on the Gitea host and on its GitHub mirror.

### Out of Scope

- Other days of the course and any exercise that is not one of the five challenges.
- Packaging for or publishing to PyPI.
- Hosting the generated Doxygen output.
- A graphical menu or any interface other than a command line.
- Automated tests that open a turtle window (the window needs a display and cannot run in continuous integration).
- Committing, pushing or merging by the assistant; S01 does these steps.

## Expected Benefits

### Tangible Benefits

- A runnable repository with five challenges, a test suite and generated source documentation.
- A continuous integration workflow that shows at once whether the repository is healthy.
- A repository page that states what the project is and how to run it.

### Intangible Benefits

- Practice of a full workflow (plan, branch, review, pull request) on a small safe project.
- A reusable template for later course days.
- A reference that other participants can read and compare with their own solutions.

## Strategic Alignment

The project supports S01's goal of completing the 100 Days of Code course with professional habits, not only working scripts. It also supports sharing: S02 and S03 are the audience of the course's community, and the repository is written for them.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Challenges are runnable | 5 of 5 challenges start from the command line and draw to completion | S01 runs each on Windows PowerShell and records the result in the review of the milestone |
| 2 | Automated tests pass | 0 failures; at least one test for every public function | `python -m pytest` exits 0 locally and in continuous integration |
| 3 | Runtime dependencies | 0 | `dependencies = []` in `pyproject.toml` |
| 4 | Source documentation builds | 0 Doxygen warnings | `doxygen Doxyfile` output |
| 5 | Set-up is reproducible | A fresh clone runs the challenges and the tests following only the README on Windows PowerShell | S01 follows the README from an empty folder |
| 6 | Repository is presented | Non-empty description and at least 5 topics on each host | Repository settings page of each host |
| 7 | Work is traceable | 100 % of pull requests carry one `Closes #N` line per completed issue | Pull request descriptions |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Tk is missing on Linux Debian, so turtle cannot open a window | A reader cannot run any challenge | The README names the `python3-tk` package in the Debian section and shows how to check that `tkinter` imports |
| Continuous integration has no display | Tests that draw would fail there | Drawing functions take the turtle as an argument; tests use a recording fake turtle; no test opens a window |
| The reader's Python is older than 3.13 | Install or run fails with an unclear error | `requires-python` is declared; the README shows how to check the version first |
| The access tokens in `.env` end up in the repository | Credentials are exposed publicly | `.env` is listed in `.gitignore`; no code imports or tests it; it is used only by S01's own tooling |
| Scope grows beyond the five challenges | The deadline is missed and the template loses focus | The Out of Scope list and the plan-first gate: no code without a milestone task |
| Function names drift from the assignment | S02 cannot compare solutions | The names in O1 are fixed in the milestone tasks and checked in review |

## Assumptions

- Python 3.13 with Tk is available on S01's machine (3.13.14 is installed).
- The five lecture summaries supplied by S01 are the specification of the challenges.
- S01 is the only contributor and is the reviewer of every document and pull request.
- The repositories on the Gitea host and on GitHub already exist and S01 holds a token for each.

## Constraints

- Python 3.13 or later, with a `venv` virtual environment.
- pytest for tests; `constants.py` for constants; `pyproject.toml` for configuration; a Python `.gitignore`.
- Doxygen comments in the source and a `Doxyfile`.
- Folder structure `src/`, `tests/`, `docs/`.
- The README follows the agreed template and documents the local `.venv` and `python -m pip install --upgrade pip`.
- No runtime dependency unless it is needed.
- The assistant does not commit, push or open a pull request unless S01 asks.
- The token file `.env` is for S01's personal use: it is not imported, not tested and not committed.
- The work is complete by 2026-10-21.

## Cost–Benefit Assessment

The assessment is qualitative: the project has no revenue, no licence cost and no hosting cost, so a monetary return on investment cannot be calculated and would be invented. The only cost is S01's time.

| Costs | Benefits |
| --- | --- |
| S01's time across four milestones | A reviewed, runnable solution repository |
| Time to maintain the planning documents | A reusable template for later course days |
| No licence, hosting or tooling cost (Python, pytest, ruff, mypy, Doxygen and both git hosts are free) | A visible repository for S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants the five challenges solved and a complete workflow practised, with every step reviewed |
| S02 | Wants readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | Wants a clear repository description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the cost is only S01's time and every success criterion can be measured.

---

[SA-001]: ./stakeholder-analysis.md
