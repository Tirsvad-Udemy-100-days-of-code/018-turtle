import pytest

from tests.fakes import FakePen
from turtle_challenges.constants import DASH_COUNT, DASH_LENGTH, GAP_LENGTH
from turtle_challenges.dashed_line import draw_dashed_line


def test_draw_dashed_line_alternates_dash_and_gap() -> None:
    pen = FakePen()

    draw_dashed_line(pen, dash_count=2)

    assert (
        pen.calls[:-1]
        == [
            ("pendown", ()),
            ("forward", (DASH_LENGTH,)),
            ("penup", ()),
            ("forward", (GAP_LENGTH,)),
        ]
        * 2
    )


def test_draw_dashed_line_draws_the_default_number_of_dashes() -> None:
    pen = FakePen()

    draw_dashed_line(pen)

    assert pen.names().count("pendown") == DASH_COUNT + 1
    assert pen.names().count("forward") == 2 * DASH_COUNT


def test_draw_dashed_line_leaves_the_pen_down() -> None:
    pen = FakePen()

    draw_dashed_line(pen, dash_count=3)

    assert pen.calls[-1] == ("pendown", ())


def test_draw_dashed_line_uses_the_given_lengths() -> None:
    pen = FakePen()

    draw_dashed_line(pen, dash_count=1, dash_length=4, gap_length=7)

    assert pen.args_of("forward") == [(4,), (7,)]


def test_draw_dashed_line_with_no_dashes_only_puts_the_pen_down() -> None:
    pen = FakePen()

    draw_dashed_line(pen, dash_count=0)

    assert pen.names() == ["pendown"]


def test_draw_dashed_line_rejects_a_negative_count() -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="dash_count"):
        draw_dashed_line(pen, dash_count=-1)

    assert pen.calls == []


@pytest.mark.parametrize(("dash_length", "gap_length"), [(0, 10), (10, 0), (-1, 10)])
def test_draw_dashed_line_rejects_a_length_that_is_not_positive(
    dash_length: float, gap_length: float
) -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="lengths"):
        draw_dashed_line(pen, dash_length=dash_length, gap_length=gap_length)

    assert pen.calls == []
