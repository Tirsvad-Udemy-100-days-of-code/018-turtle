"""!
@file __init__.py
@brief Solutions to the turtle graphics challenges of day 18 of Udemy's
100 Days of Code.

The challenges so far are @ref turtle_challenges.square.draw_square and
@ref turtle_challenges.dashed_line.draw_dashed_line. Each takes the turtle as its
first argument, so it can be tested without a window.
"""

from turtle_challenges.colors import random_color, random_palette_color
from turtle_challenges.dashed_line import draw_dashed_line
from turtle_challenges.square import draw_square

__all__ = [
    "draw_dashed_line",
    "draw_square",
    "random_color",
    "random_palette_color",
]
