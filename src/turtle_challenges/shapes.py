"""!
@file shapes.py
@brief Turtle Challenge 3: draw different shapes, each in a random color.
"""

import random

from turtle_challenges.colors import random_palette_color
from turtle_challenges.constants import (
    FULL_TURN_DEGREES,
    MAX_POLYGON_SIDES,
    MIN_POLYGON_SIDES,
    POLYGON_SIDE_LENGTH,
)
from turtle_challenges.pen import Pen


def draw_shape(
    pen: Pen, num_sides: int, side_length: float = POLYGON_SIDE_LENGTH
) -> None:
    """!
    @brief Draw a regular polygon.

    The turtle turns 360 divided by the number of sides after each side, so
    five sides turn 72 degrees and the shape closes after one lap.

    @param pen The turtle that draws.
    @param num_sides Number of sides; at least 3.
    @param side_length Length of each side, in turtle units.
    @exception ValueError If @p num_sides is below 3, or @p side_length is not
        positive.
    """
    if num_sides < MIN_POLYGON_SIDES:
        raise ValueError(
            f"num_sides must be at least {MIN_POLYGON_SIDES}, got {num_sides}"
        )
    if side_length <= 0:
        raise ValueError(f"side_length must be positive, got {side_length}")
    angle = FULL_TURN_DEGREES / num_sides
    for _ in range(num_sides):
        pen.forward(side_length)
        pen.right(angle)


def draw_shapes(pen: Pen, rng: random.Random | None = None) -> None:
    """!
    @brief Draw a triangle, square, pentagon and so on up to a decagon.

    Each shape gets a random color from the palette.

    @param pen The turtle that draws.
    @param rng Random generator for the colors; a shared one is used if omitted.
    """
    for num_sides in range(MIN_POLYGON_SIDES, MAX_POLYGON_SIDES + 1):
        pen.color(random_palette_color(rng))
        draw_shape(pen, num_sides)
