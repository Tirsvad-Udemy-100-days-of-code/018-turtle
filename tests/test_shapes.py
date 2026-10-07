import random

import pytest

from tests.fakes import FakePen
from turtle_challenges.constants import (
    COLOR_PALETTE,
    FULL_TURN_DEGREES,
    MAX_POLYGON_SIDES,
    MIN_POLYGON_SIDES,
    POLYGON_SIDE_LENGTH,
)
from turtle_challenges.shapes import draw_shape, draw_shapes

SIDE_COUNTS = range(MIN_POLYGON_SIDES, MAX_POLYGON_SIDES + 1)


@pytest.mark.parametrize("num_sides", SIDE_COUNTS)
def test_draw_shape_draws_every_side_at_the_default_length(num_sides: int) -> None:
    pen = FakePen()

    draw_shape(pen, num_sides)

    assert pen.args_of("forward") == [(POLYGON_SIDE_LENGTH,)] * num_sides


@pytest.mark.parametrize("num_sides", SIDE_COUNTS)
def test_draw_shape_turns_a_full_lap_in_equal_steps(num_sides: int) -> None:
    pen = FakePen()

    draw_shape(pen, num_sides)

    expected_angle = FULL_TURN_DEGREES / num_sides
    assert pen.args_of("right") == [(expected_angle,)] * num_sides


def test_draw_shape_turns_72_degrees_for_a_pentagon() -> None:
    pen = FakePen()

    draw_shape(pen, 5)

    assert pen.args_of("right")[0] == (72,)


def test_draw_shape_uses_the_given_side_length() -> None:
    pen = FakePen()

    draw_shape(pen, 3, side_length=25)

    assert pen.args_of("forward") == [(25,)] * 3


@pytest.mark.parametrize("num_sides", [-1, 0, 1, 2])
def test_draw_shape_rejects_fewer_than_three_sides(num_sides: int) -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="num_sides"):
        draw_shape(pen, num_sides)

    assert pen.calls == []


def test_draw_shape_rejects_a_side_that_is_not_positive() -> None:
    pen = FakePen()

    with pytest.raises(ValueError, match="side_length"):
        draw_shape(pen, 4, side_length=0)


def test_draw_shapes_draws_a_triangle_up_to_a_decagon() -> None:
    pen = FakePen()

    draw_shapes(pen, random.Random(5))

    assert len(pen.args_of("forward")) == sum(SIDE_COUNTS)
    assert len(pen.args_of("color")) == len(SIDE_COUNTS)


def test_draw_shapes_sets_a_palette_color_before_each_shape() -> None:
    pen = FakePen()

    draw_shapes(pen, random.Random(6))

    colors = [args[0] for args in pen.args_of("color")]
    assert all(color in COLOR_PALETTE for color in colors)
    assert pen.names()[0] == "color"


def test_draw_shapes_works_without_a_generator() -> None:
    pen = FakePen()

    draw_shapes(pen)

    assert len(pen.args_of("color")) == len(SIDE_COUNTS)
