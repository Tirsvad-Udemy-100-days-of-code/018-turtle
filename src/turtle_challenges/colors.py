"""!
@file colors.py
@brief Random colors for the challenges.

A color is either a name from the palette (challenge 3) or an RGB tuple
(challenges 4 and 5). A tuple is the right type for an RGB value: it is
immutable, so a color cannot change after it is made.
"""

import random

from turtle_challenges.constants import (
    COLOR_CHANNEL_MAX,
    COLOR_CHANNEL_MIN,
    COLOR_PALETTE,
)

## Generator used when a caller passes none; tests pass a seeded one instead.
_DEFAULT_RANDOM = random.Random()


def random_color(rng: random.Random | None = None) -> tuple[int, int, int]:
    """!
    @brief Pick a random RGB color.

    @param rng Random generator to draw from; a shared one is used if omitted.
    @return A tuple of red, green and blue, each from 0 to 255.
    """
    generator = rng if rng is not None else _DEFAULT_RANDOM
    red = generator.randint(COLOR_CHANNEL_MIN, COLOR_CHANNEL_MAX)
    green = generator.randint(COLOR_CHANNEL_MIN, COLOR_CHANNEL_MAX)
    blue = generator.randint(COLOR_CHANNEL_MIN, COLOR_CHANNEL_MAX)
    return (red, green, blue)


def random_palette_color(rng: random.Random | None = None) -> str:
    """!
    @brief Pick a random color name from the palette.

    @param rng Random generator to draw from; a shared one is used if omitted.
    @return One of the names in `COLOR_PALETTE`.
    """
    generator = rng if rng is not None else _DEFAULT_RANDOM
    return generator.choice(COLOR_PALETTE)
