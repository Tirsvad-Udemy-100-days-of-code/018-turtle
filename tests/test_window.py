import sys

import pytest

from turtle_challenges.window import (
    TURTLE_UNAVAILABLE_MESSAGE,
    TurtleUnavailableError,
    create_pen,
    create_window,
)


@pytest.fixture
def without_turtle(monkeypatch: pytest.MonkeyPatch) -> None:
    """Make `import turtle` fail, as on a Python without Tk."""
    monkeypatch.setitem(sys.modules, "turtle", None)


def test_create_window_reports_a_missing_turtle(without_turtle: None) -> None:
    with pytest.raises(TurtleUnavailableError) as error_info:
        create_window()

    assert str(error_info.value) == TURTLE_UNAVAILABLE_MESSAGE
    assert isinstance(error_info.value.__cause__, ImportError)


def test_create_pen_reports_a_missing_turtle(without_turtle: None) -> None:
    with pytest.raises(TurtleUnavailableError):
        create_pen()


def test_the_missing_turtle_message_names_the_debian_package() -> None:
    assert "python3-tk" in TURTLE_UNAVAILABLE_MESSAGE
