"""!
@file dashed_line.py
@brief Turtle Challenge 2: draw a dashed line.
"""

from turtle_challenges.constants import DASH_COUNT, DASH_LENGTH, GAP_LENGTH
from turtle_challenges.pen import Pen


def draw_dashed_line(
    pen: Pen,
    dash_count: int = DASH_COUNT,
    dash_length: float = DASH_LENGTH,
    gap_length: float = GAP_LENGTH,
) -> None:
    """!
    @brief Draw a line of dashes: pen down for a dash, pen up for a gap.

    The pen is down again when the function returns, so that the caller can
    keep drawing.

    @param pen The turtle that draws.
    @param dash_count How many dashes to draw.
    @param dash_length Length of one dash, in turtle units.
    @param gap_length Length of the gap after each dash, in turtle units.
    @exception ValueError If @p dash_count is negative, or a length is not
        positive.
    """
    if dash_count < 0:
        raise ValueError(f"dash_count must not be negative, got {dash_count}")
    if dash_length <= 0 or gap_length <= 0:
        raise ValueError(
            f"lengths must be positive, got dash {dash_length} and gap {gap_length}"
        )
    for _ in range(dash_count):
        pen.pendown()
        pen.forward(dash_length)
        pen.penup()
        pen.forward(gap_length)
    pen.pendown()
