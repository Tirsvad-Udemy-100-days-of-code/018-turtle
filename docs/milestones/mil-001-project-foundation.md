# Milestone 001: Project Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-07 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

This milestone decides whether the repository has a working, documented and presentable base on which the five challenges can be built: project configuration, ignore rules, package and test skeleton, source documentation, continuous integration, README and repository description with topics.

## Deliverable

The `mil-001-project-foundation` branch, opened as one pull request, containing `pyproject.toml`, a Python `.gitignore`, `src/turtle_challenges/` with `constants.py`, a `tests/` folder with a passing smoke test, a `Doxyfile`, a continuous integration workflow, and a `README.md` that follows the agreed template. The repository description and topics are set on the Gitea host and on its GitHub mirror.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In a fresh `.venv` on Python 3.13, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed | Both exit 0 | Either fails |
| 2 | `dependencies = []` in `pyproject.toml`; `requires-python` is `>=3.13` | Both hold | A runtime dependency is declared, or the Python bound is missing |
| 3 | `python -m pytest` runs | Exit 0 with at least one test | Exit not 0, or no test collected |
| 4 | `ruff check .`, `ruff format --check .` and `mypy` | All exit 0 | Any exit not 0 |
| 5 | `doxygen Doxyfile` | 0 warnings | Any warning or error |
| 6 | `README.md` has the template sections in order, with no placeholder text | All sections present and filled | A section is missing or a `<placeholder>` remains |
| 7 | `.env` is not tracked and is listed in `.gitignore` | `git ls-files .env` prints nothing and `git check-ignore .env` prints `.env` | `.env` is tracked, or not ignored |
| 8 | Repository description and at least 5 topics | Set on the Gitea host and on GitHub | Missing on either host |
| 9 | The continuous integration workflow file exists and runs the install, lint, type check, test and Doxygen steps | All steps present | A step is missing |
| 10 | Review record against `QC-PY-001` | Verdict Go | Go-with-conditions or No-Go |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001, SA-001 and PP-001 accepted | The plan-first gate: no file goes under `src/` or `tests/` before the plan is accepted |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Reproducible set-up guide | O3 in [BC-001] |
| No runtime dependencies | O4 in [BC-001] |
| Source documentation | O5 in [BC-001] |
| Repository presentation | O6 in [BC-001] |
| One branch and pull request per milestone | O7 in [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-10 — the first of four milestones, leaving eleven days of the plan that ends 2026-10-21 (Constraints in [BC-001]).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Declare the project in one file: name, version, `requires-python = ">=3.13"`, an empty runtime `dependencies` list, a `dev` extra with pytest, ruff and mypy, the `src` layout, and the pytest (`pythonpath`, `testpaths`), ruff and mypy settings. Keeping runtime dependencies at zero is objective O4 of the Business Case. | No | |
| 2 | Add Python .gitignore | Add the standard Python ignore rules plus `.env`, `.venv/` and the Doxygen output folder `build/`, so virtual environments, caches, generated documentation and the personal token file are never committed. | No | |
| 3 | Create package and test skeleton | Create `src/turtle_challenges/__init__.py` and `constants.py` (color mode 255, window title) and a `tests/` folder with a smoke test that imports the package, so the test run is green from the first pull request. Constants live only in `constants.py`. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` for the Python source (`INPUT = src`, README as main page, Hypertext Markup Language (HTML) output to `build/doxygen`, warnings treated as errors) and check that `doxygen Doxyfile` reports 0 warnings. Source files use Doxygen commands in their docstrings (`@brief`, `@param`, `@return`). | No | |
| 5 | Add continuous integration workflow | Add `.github/workflows/ci.yml` (read by GitHub Actions and by Gitea Actions): set up Python 3.13, upgrade pip, install `.[dev]`, then run ruff, mypy, pytest and the Doxygen build. The workflow never opens a turtle window. | No | |
| 6 | Write README from the agreed template | Write `README.md` with the sections Requirements, Set up (Windows PowerShell, Linux Debian, MacOS), Run, Run the tests, Continuous integration, Build the source documentation, Project layout and License. The set-up shows how to create and use a local `.venv` and how to run `python -m pip install --upgrade pip`. The Run section is completed in milestone 004. | No | |
| 7 | Set repository description and topics | Set a one-sentence description and at least 5 topics on the Gitea repository and on its GitHub mirror, using the tokens in `.env`. That file is for S01's personal use: it is never imported, tested, printed or committed. | No | |
| 8 | Review milestone 001 against QC-PY-001 | Review the configuration and skeleton against `QC-PY-001`, record the result as an `RC-*` and add the instance to the traceability matrix. | No | |

---

[BC-001]: ../business-case.md
