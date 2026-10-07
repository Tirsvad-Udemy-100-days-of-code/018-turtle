# Review Record: Business Case success criteria, re-check on main

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-019 |
| CrossReference | [BC-001], [RC-018], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [03700b8] |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Verdict recorded: Go | pending |

---

## Artifact Under Review

- Instance reviewed: the delivered project on `main` at commit 7d2c9e3 (Gitea and GitHub), against the Success Criteria of [BC-001]
- Checklist used: the seven rows of the `## Success Criteria` table of [BC-001]; no `QC-*` checklist covers this check, the table is the checklist
- Scope: all seven success criteria, as a new record that names [RC-018] and re-checks its conditions; the evidence for the gate of [MIL-004]
- Language and domain: n/a (technical record)
- Language reviewer: none (n/a)
- Method: a fresh clone of `main` from the README's own GitHub URL into an empty folder, then the README's Windows PowerShell steps, run on the author's Windows machine; the real command started from that clone; read-only calls to the Gitea and GitHub APIs for continuous integration, settings, pull requests and issues.
- Reviewer eligibility: S01 is the author and the reviewer; S01 accepted that deviation in chat on 2026-10-07 (see the traceability matrix).
- Status of this record: decided on 2026-10-08 by S01, the reviewer, who recorded the verdict Go and accepted the assistant's runs as the measure for criteria 1 and 5. The statuses and evidence are the assistant's, from the runs described above.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Challenges are runnable. Target: 5 of 5 challenges start from the command line and draw to completion. Measure: S01 runs each on Windows PowerShell and records the result in the review of the milestone. | Pass | From a fresh clone of `main` (`7d2c9e3`), in PowerShell: (a) the real command `turtle-challenges <name>` was started five times and each time a window titled "Turtle Challenges" opened (square, dashed-line, shapes, random-walk, spirograph). (b) Each challenge was run through `cli.main` with real Tk, closing the window where the command would wait for a click, and each reached that point with exit 0: square 1.4 s, dashed-line 3.3 s, shapes 14.0 s, random-walk 9.6 s, spirograph 3.6 s (1.8 s with `--gap 10`). Not covered: the click that closes the window, and S01's own run, which the measure names. The code is unchanged since the run in [RC-018]. S01 accepted this run as the measure on 2026-10-08. |
| 2 | Automated tests pass. Target: 0 failures; at least one test for every public function. Measure: `python -m pytest` exits 0 locally and in continuous integration. | Pass | In the clone of `main`: `python -m pytest` printed `95 passed`, exit 0; `ruff check .`, `ruff format --check .` and `mypy` exit 0; the steps of the current workflow as written (`python -m ruff check src tests`, `python -m ruff format --check src tests`, `python -m mypy src tests`) pass too. Every public function and class still has a test (the code is unchanged since [RC-018]). Continuous integration on `main` at `7d2c9e3`: run 252 is `success` with the steps Install, Tests, Lint, Format check and Types. History: after #35 introduced `pip install --group dev` the workflow failed (six runs, 241 to 246); #36 fixed the install step and CI has been green since (runs 247, 249 and 252). The workflow no longer builds the documentation. |
| 3 | Runtime dependencies. Target: 0. Measure: `dependencies = []` in `pyproject.toml`. | Pass | `dependencies = []` in `pyproject.toml` (read with `tomllib`), and `python -m pip show turtle-challenges` in the clone of `main` prints an empty `Requires:`. |
| 4 | Source documentation builds. Target: 0 Doxygen warnings. Measure: `doxygen Doxyfile` output. | Pass | `doxygen Doxyfile` (Doxygen 1.15.0) in the clone of `main`: exit 0, no output, `build/html/index.html` generated. Continuous integration no longer runs this build, because the current workflow has no Doxygen step, so the evidence is the local run only; the README's "Continuous integration" section still says CI builds the documentation. |
| 5 | Set-up is reproducible. Target: A fresh clone runs the challenges and the tests following only the README on Windows PowerShell. Measure: S01 follows the README from an empty folder. | Pass | Met. The README's own clone URL, `https://github.com/Tirsvad-Udemy-100-days-of-code/018-turtle.git`, now gives the project: `main` at `7d2c9e3` with 60 tracked files and 12 package files (GitHub receives `main` from Gitea). In an empty folder under PowerShell every README step worked: `git clone`, `py -3.13 -m venv .venv` (Python 3.13.14), `Activate.ps1`, `python -m pip install --upgrade pip` (26.2.1), `python -m pip install -e ".[dev]"` (exit 0), `python -m pytest` (95 passed), `ruff check .`, `ruff format --check .` and `mypy` (all exit 0), `turtle-challenges --help` (exit 0) and `doxygen Doxyfile` (0 warnings). This closes the condition on criterion 5 of [RC-018]. The measure names S01 following the README, which has not happened. S01 accepted this run as the measure on 2026-10-08. |
| 6 | Repository is presented. Target: Non-empty description and at least 5 topics on each host. Measure: Repository settings page of each host. | Pass | Read from the host APIs today: Gitea and GitHub both have the description "Turtle graphics exercises from Udemy's 100 Days of Code Python bootcamp (day 18): square, dashed line, polygons, random walk and spirograph." and 11 topics each; the GitHub repository is public and its default branch is `main`. |
| 7 | Work is traceable. Target: 100 % of pull requests carry one `Closes #N` line per completed issue. Measure: Pull request descriptions. | Pass | Pull requests #30 to #33 each carry their `Closes #N` lines one per line and no comma form (#30: 1 to 6; #31: 9 to 14; #32: 16 to 21; #33: 23 to 26 and 8, 15, 22, 29). #34, #35 and #36 complete no issue and carry no `Closes` line. Only #34 says so explicitly; #35 and #36 do not, and the project-planning rule asks a pull request that finishes no issue to say so. 28 of the 29 issues are closed (#7 and #27 by hand, the others through the `Closes` lines); #28 is open. |

## Overall Verdict

Go — all seven success criteria of [BC-001] are met on `main` (`7d2c9e3`). The Business Case names S01 for the runs behind criteria 1 and 5; S01 accepted the assistant's runs in this record as that measure on 2026-10-08.

This closes the conditions of [RC-018]: criterion 5 is met by the README run from its own GitHub clone URL, GitHub receives `main` and the branches from Gitea, and the run of the five commands (criterion 1) is accepted. Go / No-Go criterion 6 of [MIL-004] ("every criterion met") is therefore met. No date moved, so the Project Plan needs no schedule change.

Reviewer eligibility: S01 is the author and the reviewer, which the review process does not allow; S01 accepted that deviation in chat on 2026-10-07 and it is recorded in the traceability matrix.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition (criteria 1 and 5): accept the runs in this record as the measure, or run the five commands yourself on Windows PowerShell (click the window to close it) and follow the README from an empty folder, and record the result. Closed 2026-10-08: S01 accepted the runs in this record as the measure. | S01 | 2026-10-21 |
| After the verdict `Go`: close issue #28. | S01 | 2026-10-21 |
| The README's "Continuous integration" section and its project layout still name `.github/workflows/ci.yml` and say CI builds the documentation; the workflow is now `.gitea/workflows/ci.yml` and has no Doxygen step. Correct the README, or restore the step. | S01 | 2026-10-21 |
| Decide whether continuous integration should build the documentation again; today criterion 4 rests on a local run only. | S01 | 2026-10-21 |
| Optional: add "No issue closed: <reason>" to the descriptions of #35 and #36. | S01 | 2026-10-21 |
| Optional: the Project Plan's open issues about the continuous integration host and the GitHub mirror are answered (a runner exists, CI is green on `main`, GitHub receives `main`); updating them needs a new Version History row on `PP-001`. | S01 | 2026-10-21 |

---

[BC-001]: ../../business-case.md
[RC-018]: ./rc-018-business-case-success-criteria.md
[MIL-004]: ../../milestones/mil-004-random-walk-and-spirograph.md
[03700b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/018-turtle/commit/03700b8de2568c3f50baf99422c3b47bb68975b3
