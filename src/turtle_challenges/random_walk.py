"""!
@file random_walk.py
@brief Turtle Challenge 4: generate a random walk.
"""

import random

from turtle_challenges.colors import random_color
from turtle_challenges.constants import (
    FASTEST_SPEED,
    WALK_HEADINGS,
    WALK_PEN_SIZE,
    WALK_STEP_DISTANCE,
    WALK_STEPS,
)
from turtle_challenges.pen import Pen


def random_walk(
    pen: Pen,
    steps: int = WALK_STEPS,
    distance: float = WALK_STEP_DISTANCE,
    rng: random.Random | None = None,
) -> None:
    """!
    @brief Walk in random directions, changing color at every step.

    Each step faces east, north, west or south at random and moves the same
    distance in a new random RGB color.

    @param pen The turtle that draws.
    @param steps Number of steps to take.
    @param distance Distance of one step, in turtle units.
    @param rng Random generator for headings and colors; a shared one is used
        if omitted.
    @exception ValueError If @p steps is negative, or @p distance is not
        positive.
    """
    if steps < 0:
        raise ValueError(f"steps must not be negative, got {steps}")
    if distance <= 0:
        raise ValueError(f"distance must be positive, got {distance}")
    generator = rng if rng is not None else random.Random()
    pen.pensize(WALK_PEN_SIZE)
    pen.speed(FASTEST_SPEED)
    for _ in range(steps):
        pen.color(random_color(generator))
        pen.setheading(generator.choice(WALK_HEADINGS))
        pen.forward(distance)
