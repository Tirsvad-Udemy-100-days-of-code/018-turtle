import pytest

from tests.fakes import FakePen, FakeWindow
from turtle_challenges import cli
from turtle_challenges.constants import (
    CHALLENGE_NAMES,
    DASH_COUNT,
    SPIROGRAPH_GAP_DEGREES,
    SQUARE_SIDES,
)
from turtle_challenges.pen import Pen, Window
from turtle_challenges.window import TurtleUnavailableError


@pytest.fixture
def fake_pen_and_window(monkeypatch: pytest.MonkeyPatch) -> tuple[FakePen, FakeWindow]:
    """Replace the turtle window and pen of the command line with fakes."""
    pen = FakePen()
    window = FakeWindow()

    def create_fake_window() -> Window:
        return window

    def create_fake_pen() -> Pen:
        return pen

    monkeypatch.setattr(cli, "create_window", create_fake_window)
    monkeypatch.setattr(cli, "create_pen", create_fake_pen)
    return pen, window


def test_every_challenge_name_has_a_challenge() -> None:
    challenges = cli.build_challenges(FakePen(), SPIROGRAPH_GAP_DEGREES)

    assert set(challenges) == set(CHALLENGE_NAMES)


@pytest.mark.parametrize("name", CHALLENGE_NAMES)
def test_parser_accepts_every_challenge_name(name: str) -> None:
    args = cli.build_parser().parse_args([name])

    assert args.challenge == name
    assert args.gap == SPIROGRAPH_GAP_DEGREES


def test_parser_reads_the_spirograph_gap() -> None:
    args = cli.build_parser().parse_args(["spirograph", "--gap", "7.5"])

    assert args.gap == 7.5


def test_parser_rejects_an_unknown_challenge(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as exit_info:
        cli.build_parser().parse_args(["triangle"])

    assert exit_info.value.code == 2
    assert "invalid choice" in capsys.readouterr().err


def test_help_lists_every_challenge(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exit_info:
        cli.build_parser().parse_args(["--help"])

    assert exit_info.value.code == 0
    output = capsys.readouterr().out
    assert all(name in output for name in CHALLENGE_NAMES)


def test_main_runs_the_square_and_waits_for_a_click(
    fake_pen_and_window: tuple[FakePen, FakeWindow],
) -> None:
    pen, window = fake_pen_and_window

    status = cli.main(["square"])

    assert status == 0
    assert len(pen.args_of("forward")) == SQUARE_SIDES
    assert window.waited_for_click


def test_main_runs_the_dashed_line(
    fake_pen_and_window: tuple[FakePen, FakeWindow],
) -> None:
    pen, _ = fake_pen_and_window

    cli.main(["dashed-line"])

    assert len(pen.args_of("forward")) == 2 * DASH_COUNT


def test_main_passes_the_gap_to_the_spirograph(
    fake_pen_and_window: tuple[FakePen, FakeWindow],
) -> None:
    pen, _ = fake_pen_and_window

    cli.main(["spirograph", "--gap", "90"])

    assert len(pen.args_of("circle")) == 4


def test_main_reports_a_missing_turtle_and_exits_with_status_1(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    def fail() -> Window:
        raise TurtleUnavailableError("no Tk here")

    monkeypatch.setattr(cli, "create_window", fail)

    with pytest.raises(SystemExit) as exit_info:
        cli.main(["square"])

    assert exit_info.value.code == 1
    assert "no Tk here" in capsys.readouterr().err
