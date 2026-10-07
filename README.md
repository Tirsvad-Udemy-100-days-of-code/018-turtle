# Turtle Challenges

Solutions to the five turtle graphics challenges of day 18 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: draw a square, draw a dashed line, draw different shapes, generate a random walk and draw a spirograph. The code is small, readable and tested, keeps the function names of the assignment, and needs nothing beyond the Python standard library to run.

## Requirements

- Python 3.13 or later, with Tk (`tkinter`), which the `turtle` module draws with. The Windows and macOS installers include it; on Debian it is the `python3-tk` package.
- `git`, to clone the repository.
- No runtime dependencies. The development tools (pytest, ruff, mypy) are installed by the `dev` extra in the steps below.
- Doxygen, only to build the source documentation.

## Set up

The same four steps on every system: clone, create a local virtual environment named `.venv`, upgrade `pip` inside it, and install the project in editable mode with its development tools. The virtual environment keeps the project's packages apart from every other Python project on the machine; do not install them system-wide.

The Windows PowerShell steps are the ones the author has run. The Debian and macOS steps use the same Python commands but have not been verified.

### Windows PowerShell

```powershell
git clone https://github.com/Tirsvad-Udemy-100-days-of-code/018-turtle.git
cd 018-turtle
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run `Activate.ps1` because scripts are disabled, allow scripts for this window only and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

The prompt starts with `(.venv)` while the environment is active. Type `deactivate` to leave it. Activate it again in every new terminal before you run the project.

### Linux Debian

```bash
sudo apt update
sudo apt install --yes git python3 python3-venv python3-tk
git clone https://github.com/Tirsvad-Udemy-100-days-of-code/018-turtle.git
cd 018-turtle
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Check that `python3 --version` prints 3.13 or later. If the package manager offers an older Python, install 3.13 another way (for example with `pyenv`) before creating the environment.

### MacOS

```bash
brew install git python@3.13 python-tk@3.13
git clone https://github.com/Tirsvad-Udemy-100-days-of-code/018-turtle.git
cd 018-turtle
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

With the virtual environment active, run one challenge by name. A window opens, the turtle draws, and the window closes when you click it.

```bash
turtle-challenges square
python -m turtle_challenges dashed-line
```

| Challenge | Command | Function |
| --- | --- | --- |
| 1. Draw a square | `turtle-challenges square` | `draw_square` |
| 2. Draw a dashed line | `turtle-challenges dashed-line` | `draw_dashed_line` |

Challenges 3 to 5 are added by milestones 003 and 004.

`turtle-challenges --help` lists the challenges. If the command prints that the turtle module needs Tk, install Tk as described under Requirements.

To use the functions in your own code, create a window and a turtle, then pass the turtle as the first argument. The assignment's functions use one global turtle; here the turtle is a parameter, which is what lets the tests run without a window:

```python
from turtle_challenges import draw_square
from turtle_challenges.window import create_pen, create_window

window = create_window()
tim = create_pen()
draw_square(tim)
window.exitonclick()
```

## Run the tests

The tests never open a window: they pass a recording fake in place of the turtle and check the moves it recorded. With the virtual environment active:

```bash
python -m pytest
```

The same checks as in continuous integration:

```bash
ruff check .
ruff format --check .
mypy
```

## Continuous integration

`.github/workflows/ci.yml` runs on every push to `main` and on every pull request. It is read by both GitHub Actions and Gitea Actions. It sets up Python 3.13, upgrades `pip`, installs the project with its development tools, then runs ruff (lint and format check), mypy, pytest and the Doxygen build. No step opens a turtle window.

## Build the source documentation

The source carries Doxygen comments, and the `Doxyfile` builds them, with this README as the main page. Install Doxygen first (`winget install DimitriVanHeesch.Doxygen` on Windows, `sudo apt install doxygen` on Debian, `brew install doxygen` on macOS), then run from the repository root:

```bash
doxygen Doxyfile
```

Open `build/html/index.html` in a browser. Any Doxygen warning fails the build, so every module, function and constant has to stay documented.

## Project layout

```text
.
├── .github/workflows/ci.yml   continuous integration
├── docs/                      project documents: business case, plan, milestones
├── src/turtle_challenges/     the package
│   ├── constants.py           every constant of the project
│   ├── pen.py                 the Pen and Window protocols the challenges use
│   ├── window.py              opens the turtle window and creates the turtle
│   ├── square.py              challenge 1: draw_square
│   ├── dashed_line.py         challenge 2: draw_dashed_line
│   └── cli.py                 the turtle-challenges command
├── tests/                     pytest tests and the recording fake pen
├── Doxyfile                   Doxygen configuration
├── pyproject.toml             project, tool and dependency configuration
└── LICENSE
```

The `framework/` folder is a git submodule with the quality framework that the documents in `docs/` follow. The project does not need it to run, test or build.

## License

GNU Affero General Public License version 3. See the [LICENSE](LICENSE) file.
