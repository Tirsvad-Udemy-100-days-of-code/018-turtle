import pytest

from tests.fakes import FakePen
from turtle_challenges.constants import RIGHT_ANGLE_DEGREES, SQUARE_SIDE_LENGTH
from turtle_challenges.square import draw_square


def test_draw_square_moves_forward_and_turns_right_four_times() -> None:
    pen = FakePen()

    draw_square(pen)

    assert (
        pen.calls
        == [
            ("forward", (SQUARE_SIDE_LENGTH,)),
            ("right", (RIGHT_ANGLE_DEGREES,)),
        ]
        * 4
    )


def test_draw_square_uses_the_given_side_length() -> None:
    pen = FakePen()

    draw_square(pen, side_length=40)

    assert pen.args_of("forward") == [(40,)] * 4


def test_draw_square_returns_the_turtle_to_its_start_heading() -> None:
    pen = FakePen()

    draw_square(pen)

    assert pen.heading() == 0


@pytest.mark.parametrize("side_length", [0, -5])
def test_draw_square_rejects_a_side_that_is_not_positive(side_length: float) -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="side_length"):
        draw_square(pen, side_length=side_length)

    assert pen.calls == []
