# Review Record: Business Case success criteria

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-018 |
| CrossReference | [BC-001], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the delivered repository, branch `mil-004-random-walk-and-spirograph` at commit 575df4d, against the Success Criteria of [BC-001]
- Checklist used: the seven rows of the `## Success Criteria` table of [BC-001]; no `QC-*` checklist covers this check, the table is the checklist
- Milestone: [MIL-004], Go / No-Go criterion 6 and task 6 (issue #28)
- Scope: all seven success criteria
- Language and domain: n/a (technical record)
- Language reviewer: none (n/a)
- Method: a fresh clone of the branch into an empty folder, then the README's Windows PowerShell steps, run on 2026-10-08 on the author's Windows machine; the real command started from that clone; read-only calls to the Gitea and GitHub APIs for continuous integration, settings and pull requests.
- Reviewer eligibility: S01 is the author and the reviewer; S01 accepted that deviation in chat on 2026-10-07 (see the traceability matrix).
- Status of this record: draft. The statuses and evidence are the assistant's, from the runs described above; they are not a decision.

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Challenges are runnable. Target: 5 of 5 challenges start from the command line and draw to completion. Measure: S01 runs each on Windows PowerShell and records the result in the review of the milestone. | Pass | On the Windows machine, in PowerShell, from the fresh clone described under criterion 5: (a) the real command `turtle-challenges <name>` was started five times and each time a window titled "Turtle Challenges" opened (square, dashed-line, shapes, random-walk, spirograph). (b) Each challenge was run through the command line code (`cli.main`) with real Tk, closing the window where the command would wait for a click, and each reached that point and returned 0: square 1.4 s, dashed-line 3.2 s, shapes 14.0 s, random-walk 9.8 s, spirograph 4.2 s (1.9 s with `--gap 10`). Not covered: the click that closes the window, and S01's own run, which the measure names. |
| 2 | Automated tests pass. Target: 0 failures; at least one test for every public function. Measure: `python -m pytest` exits 0 locally and in continuous integration. | Pass | Fresh clone, README steps: `python -m pytest` printed `95 passed`, exit 0. Every public function and class in `src/` is referenced by at least one test (scan of 16 names: none missing); `create_window` and `create_pen` are tested only for the missing-Tk path. Continuous integration: the workflow `CI` ran on the host for each pull request head (runs 217, 218, 219, 220, 227 and 228, all `success`); the latest, run 228 on `575df4d`, passed all nine steps (checkout, Python 3.13, Doxygen, install, lint, formatting, types, tests, documentation). |
| 3 | Runtime dependencies. Target: 0. Measure: `dependencies = []` in `pyproject.toml`. | Pass | `dependencies = []` in `pyproject.toml` (read with `tomllib`), and `python -m pip show turtle-challenges` in the fresh clone prints an empty `Requires:`. |
| 4 | Source documentation builds. Target: 0 Doxygen warnings. Measure: `doxygen Doxyfile` output. | Pass | `doxygen Doxyfile` (Doxygen 1.15.0) in the fresh clone: exit 0, no output, `build/html/index.html` generated. The same build passed on the host in run 228 (step "Build the source documentation"), where warnings fail the build. |
| 5 | Set-up is reproducible. Target: A fresh clone runs the challenges and the tests following only the README on Windows PowerShell. Measure: S01 follows the README from an empty folder. | Fail | Not met as written yet. The README tells a reader to clone `https://github.com/Tirsvad-Udemy-100-days-of-code/018-turtle.git`, which holds only the initial commit because the code is still in the four open pull requests, so that clone has no project. With the Gitea branch URL substituted for that one line, every other README step worked in an empty folder under PowerShell: `py -3.13 -m venv .venv` (Python 3.13.14), `Activate.ps1`, `python -m pip install --upgrade pip` (26.2.1), `python -m pip install -e ".[dev]"` (exit 0), `python -m pytest` (95 passed), `ruff check .`, `ruff format --check .` and `mypy` (all exit 0), `turtle-challenges --help` (exit 0) and `doxygen Doxyfile` (0 warnings). The `framework/` submodule was not fetched and nothing needed it. The measure names S01 following the README, which has not happened. |
| 6 | Repository is presented. Target: Non-empty description and at least 5 topics on each host. Measure: Repository settings page of each host. | Pass | Description and topics read from the host APIs: Gitea has a description ("Turtle graphics exercises from Udemy's 100 Days of Code Python bootcamp (day 18) ...") and 11 topics; GitHub has the same description and 11 topics; the target is a non-empty description and at least 5 topics. |
| 7 | Work is traceable. Target: 100 % of pull requests carry one `Closes #N` line per completed issue. Measure: Pull request descriptions. | Pass | Pull requests #30, #31, #32 and #33: each description has its `Closes #N` lines one per line and no comma form (#30: 1 to 6; #31: 9 to 14; #32: 16 to 21; #33: 23 to 26 and 8, 15, 22, 29). Every issue those lines name is a task completed by the pull request. Issue #7 was completed on the host without a commit, so #30 only references it and it was closed by hand; #27 is only partly done, so #33 only references it. |

## Overall Verdict

Pending — a draft prepared for the reviewer (S01), who decides and replaces this line with the verdict. Proposed verdict: Go-with-conditions.

Rationale: six of the seven criteria are met with evidence (1 to 4, 6 and 7). Criterion 5 is not met as the README is written, because its clone URL points at a GitHub repository that does not hold the code until the pull requests are merged and GitHub has them. Nothing is broken in the project itself: the same steps work from the Gitea branch. Go / No-Go criterion 6 of [MIL-004] ("every criterion met") is therefore not yet met, and issue #28 stays open. No date moved, so the Project Plan needs no schedule change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Condition (criterion 5): after pull requests #30 to #33 are merged and GitHub has `main` with the code, repeat the README steps from an empty folder with the README's own clone URL and record the result in a new record that names this one. | S01 | 2026-10-21 |
| Condition (criterion 1): run each of the five commands once on Windows PowerShell, click the window to close it, and record the result, or accept this record's run as the measure. | S01 | 2026-10-21 |
| Decide how `main` reaches GitHub (a push mirror from Gitea, or a push by hand). Without it a visitor from GitHub clones an empty project. | S01 | 2026-10-21 |
| Optional: the Project Plan's open issue about a continuous integration runner is answered (a runner exists and run 228 passed); updating it needs a new Version History row on `PP-001`. | S01 | 2026-10-21 |

---

[BC-001]: ../../business-case.md
[MIL-004]: ../../milestones/mil-004-random-walk-and-spirograph.md
