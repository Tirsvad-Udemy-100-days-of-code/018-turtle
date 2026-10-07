import random

import pytest

from tests.fakes import FakePen
from turtle_challenges.constants import (
    FASTEST_SPEED,
    FULL_TURN_DEGREES,
    SPIROGRAPH_GAP_DEGREES,
    SPIROGRAPH_RADIUS,
)
from turtle_challenges.spirograph import draw_spirograph


def test_draw_spirograph_draws_one_circle_per_gap_in_a_full_turn() -> None:
    pen = FakePen()

    draw_spirograph(pen, rng=random.Random(1))

    expected = FULL_TURN_DEGREES // SPIROGRAPH_GAP_DEGREES
    assert pen.args_of("circle") == [(SPIROGRAPH_RADIUS,)] * expected


def test_draw_spirograph_turns_by_the_gap_after_each_circle() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=90, rng=random.Random(2))

    assert pen.args_of("setheading") == [(90,), (180,), (270,), (360,)]


def test_draw_spirograph_sets_a_color_before_each_circle() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=120, rng=random.Random(3))

    assert pen.names()[1:] == ["color", "circle", "setheading"] * 3


def test_draw_spirograph_gives_every_circle_an_rgb_color() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=30, rng=random.Random(4))

    for (color,) in pen.args_of("color"):
        assert isinstance(color, tuple)
        assert len(color) == 3


def test_draw_spirograph_sets_the_fastest_speed_first() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=180)

    assert pen.calls[0] == ("speed", (FASTEST_SPEED,))


def test_draw_spirograph_rounds_the_circle_count_down_for_an_uneven_gap() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=7)

    assert len(pen.args_of("circle")) == 51


def test_draw_spirograph_accepts_a_float_gap_without_a_type_error() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=2.5)

    assert len(pen.args_of("circle")) == 144


def test_draw_spirograph_uses_the_given_radius() -> None:
    pen = FakePen()

    draw_spirograph(pen, size_of_gap=180, radius=42)

    assert pen.args_of("circle") == [(42,), (42,)]


def test_draw_spirograph_is_repeatable_with_the_same_seed() -> None:
    first = FakePen()
    second = FakePen()

    draw_spirograph(first, size_of_gap=45, rng=random.Random(9))
    draw_spirograph(second, size_of_gap=45, rng=random.Random(9))

    assert first.calls == second.calls


@pytest.mark.parametrize("size_of_gap", [0, -5])
def test_draw_spirograph_rejects_a_gap_that_is_not_positive(
    size_of_gap: float,
) -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="size_of_gap"):
        draw_spirograph(pen, size_of_gap=size_of_gap)

    assert pen.calls == []


@pytest.mark.parametrize("radius", [0, -1])
def test_draw_spirograph_rejects_a_radius_that_is_not_positive(radius: float) -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="radius"):
        draw_spirograph(pen, radius=radius)

    assert pen.calls == []
