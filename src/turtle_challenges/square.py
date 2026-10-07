"""!
@file square.py
@brief Turtle Challenge 1: draw a square.
"""

from turtle_challenges.constants import (
    RIGHT_ANGLE_DEGREES,
    SQUARE_SIDE_LENGTH,
    SQUARE_SIDES,
)
from turtle_challenges.pen import Pen


def draw_square(pen: Pen, side_length: float = SQUARE_SIDE_LENGTH) -> None:
    """!
    @brief Draw a square: move forward, turn right, four times.

    @param pen The turtle that draws.
    @param side_length Length of each side, in turtle units.
    @exception ValueError If @p side_length is not positive.
    """
    if side_length <= 0:
        raise ValueError(f"side_length must be positive, got {side_length}")
    for _ in range(SQUARE_SIDES):
        pen.forward(side_length)
        pen.right(RIGHT_ANGLE_DEGREES)
