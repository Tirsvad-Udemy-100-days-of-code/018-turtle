"""!
@file window.py
@brief Creates the turtle window and the turtle that draws in it.

This is the only module that touches the `turtle` library. The lecture on
imports shows these styles, and this project uses the second one:

- `import turtle` then `turtle.Turtle()`: clear, but long when used often.
- `from turtle import Screen, Turtle`: short, and names exactly what is used.
- `import turtle as t` then `t.Turtle()`: an alias for a long module name.
- `from turtle import *`: avoided, because it hides where a name comes from.

The import sits inside the functions so that importing the package (for
example to run the tests) does not need Tk; only opening a window does.
"""

from turtle_challenges.constants import COLOR_MODE, WINDOW_TITLE
from turtle_challenges.pen import Pen, Window

## Hint shown when Tk is missing, the usual reason `turtle` cannot be imported.
TURTLE_UNAVAILABLE_MESSAGE = (
    "the turtle module needs Tk (tkinter), which this Python does not provide; "
    "on Debian run: sudo apt install python3-tk"
)


class TurtleUnavailableError(RuntimeError):
    """!
    @brief Raised when the `turtle` module cannot be imported.
    """


def create_window() -> Window:
    """!
    @brief Open the turtle window with RGB colors from 0 to 255.

    @return The window, ready for drawing.
    @exception TurtleUnavailableError If `turtle` (Tk) cannot be imported.
    """
    try:
        from turtle import Screen
    except ImportError as error:
        raise TurtleUnavailableError(TURTLE_UNAVAILABLE_MESSAGE) from error
    screen = Screen()
    screen.colormode(COLOR_MODE)
    screen.title(WINDOW_TITLE)
    return screen


def create_pen() -> Pen:
    """!
    @brief Create the turtle that draws in the window.

    Call @ref turtle_challenges.window.create_window first, so that the turtle
    draws in the window that has the right color mode.

    @return A new turtle.
    @exception TurtleUnavailableError If `turtle` (Tk) cannot be imported.
    """
    try:
        from turtle import Turtle
    except ImportError as error:
        raise TurtleUnavailableError(TURTLE_UNAVAILABLE_MESSAGE) from error
    return Turtle()
