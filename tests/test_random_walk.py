import random

import pytest

from tests.fakes import FakePen
from turtle_challenges.constants import (
    COLOR_CHANNEL_MAX,
    COLOR_CHANNEL_MIN,
    FASTEST_SPEED,
    WALK_HEADINGS,
    WALK_PEN_SIZE,
    WALK_STEP_DISTANCE,
    WALK_STEPS,
)
from turtle_challenges.random_walk import random_walk


def test_random_walk_sets_pen_size_and_speed_before_the_first_move() -> None:
    pen = FakePen()

    random_walk(pen, rng=random.Random(1))

    assert pen.calls[0] == ("pensize", (WALK_PEN_SIZE,))
    assert pen.calls[1] == ("speed", (FASTEST_SPEED,))


def test_random_walk_takes_the_default_number_of_equal_steps() -> None:
    pen = FakePen()

    random_walk(pen, rng=random.Random(2))

    assert pen.args_of("forward") == [(WALK_STEP_DISTANCE,)] * WALK_STEPS


def test_random_walk_faces_only_the_four_headings() -> None:
    pen = FakePen()

    random_walk(pen, rng=random.Random(3))

    headings = {args[0] for args in pen.args_of("setheading")}
    assert headings <= set(WALK_HEADINGS)
    assert len(headings) > 1


def test_random_walk_gives_every_step_an_rgb_color() -> None:
    pen = FakePen()

    random_walk(pen, steps=30, rng=random.Random(4))

    colors = [args[0] for args in pen.args_of("color")]
    assert len(colors) == 30
    for color in colors:
        assert isinstance(color, tuple)
        assert len(color) == 3
        assert all(
            COLOR_CHANNEL_MIN <= channel <= COLOR_CHANNEL_MAX for channel in color
        )


def test_random_walk_picks_color_and_heading_before_each_move() -> None:
    pen = FakePen()

    random_walk(pen, steps=2, rng=random.Random(5))

    assert pen.names()[2:] == ["color", "setheading", "forward"] * 2


def test_random_walk_is_repeatable_with_the_same_seed() -> None:
    first = FakePen()
    second = FakePen()

    random_walk(first, steps=25, rng=random.Random(8))
    random_walk(second, steps=25, rng=random.Random(8))

    assert first.calls == second.calls


def test_random_walk_with_no_steps_only_sets_up_the_pen() -> None:
    pen = FakePen()

    random_walk(pen, steps=0)

    assert pen.names() == ["pensize", "speed"]


def test_random_walk_works_without_a_generator() -> None:
    pen = FakePen()

    random_walk(pen, steps=3)

    assert len(pen.args_of("forward")) == 3


def test_random_walk_rejects_negative_steps() -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="steps"):
        random_walk(pen, steps=-1)

    assert pen.calls == []


@pytest.mark.parametrize("distance", [0, -3])
def test_random_walk_rejects_a_distance_that_is_not_positive(distance: float) -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="distance"):
        random_walk(pen, distance=distance)

    assert pen.calls == []
