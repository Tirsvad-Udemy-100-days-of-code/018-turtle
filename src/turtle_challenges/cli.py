"""!
@file cli.py
@brief Command line: run one challenge in a turtle window.
"""

import argparse
from collections.abc import Callable, Sequence
from functools import partial

from turtle_challenges.constants import (
    CHALLENGE_DASHED_LINE,
    CHALLENGE_NAMES,
    CHALLENGE_SHAPES,
    CHALLENGE_SQUARE,
)
from turtle_challenges.dashed_line import draw_dashed_line
from turtle_challenges.pen import Pen
from turtle_challenges.shapes import draw_shapes
from turtle_challenges.square import draw_square
from turtle_challenges.window import (
    TurtleUnavailableError,
    create_pen,
    create_window,
)


def build_parser() -> argparse.ArgumentParser:
    """!
    @brief Build the argument parser of the command line.

    @return A parser with the challenge name.
    """
    parser = argparse.ArgumentParser(
        prog="turtle-challenges",
        description="Run one of the turtle challenges in a window. "
        "Click the window to close it.",
    )
    parser.add_argument(
        "challenge",
        choices=CHALLENGE_NAMES,
        help="the challenge to run",
    )
    return parser


def build_challenges(pen: Pen) -> dict[str, Callable[[], None]]:
    """!
    @brief Bind every challenge to a turtle.

    @param pen The turtle that draws.
    @return A mapping from the command line name to a function without
        arguments that draws the challenge.
    """
    return {
        CHALLENGE_SQUARE: partial(draw_square, pen),
        CHALLENGE_DASHED_LINE: partial(draw_dashed_line, pen),
        CHALLENGE_SHAPES: partial(draw_shapes, pen),
    }


def main(argv: Sequence[str] | None = None) -> int:
    """!
    @brief Run the challenge named on the command line.

    @param argv Arguments without the program name; `sys.argv` if omitted.
    @return The exit status: 0 on success.
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        window = create_window()
        tim = create_pen()
    except TurtleUnavailableError as error:
        parser.exit(1, f"{parser.prog}: error: {error}\n")
    build_challenges(tim)[args.challenge]()
    window.exitonclick()
    return 0
