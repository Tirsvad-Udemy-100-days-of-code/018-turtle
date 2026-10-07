"""!
@file spirograph.py
@brief Turtle Challenge 5: draw a spirograph.
"""

import random

from turtle_challenges.colors import random_color
from turtle_challenges.constants import (
    FASTEST_SPEED,
    FULL_TURN_DEGREES,
    SPIROGRAPH_GAP_DEGREES,
    SPIROGRAPH_RADIUS,
)
from turtle_challenges.pen import Pen


def draw_spirograph(
    pen: Pen,
    size_of_gap: float = SPIROGRAPH_GAP_DEGREES,
    radius: float = SPIROGRAPH_RADIUS,
    rng: random.Random | None = None,
) -> None:
    """!
    @brief Draw overlapping circles, turning a little after each one.

    After every circle the heading grows by @p size_of_gap, so the circles
    overlap into a spirograph once the heading has made a full turn. The number
    of circles is 360 divided by the gap, rounded down: `range` takes only an
    integer, and a float such as 72.0 would raise a `TypeError`.

    @param pen The turtle that draws.
    @param size_of_gap Degrees between two circles; must be positive.
    @param radius Radius of every circle, in turtle units.
    @param rng Random generator for the colors; a shared one is used if
        omitted.
    @exception ValueError If @p size_of_gap or @p radius is not positive.
    """
    if size_of_gap <= 0:
        raise ValueError(f"size_of_gap must be positive, got {size_of_gap}")
    if radius <= 0:
        raise ValueError(f"radius must be positive, got {radius}")
    pen.speed(FASTEST_SPEED)
    for _ in range(int(FULL_TURN_DEGREES / size_of_gap)):
        pen.color(random_color(rng))
        pen.circle(radius)
        pen.setheading(pen.heading() + size_of_gap)
