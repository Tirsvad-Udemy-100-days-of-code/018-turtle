"""!
@file pen.py
@brief The turtle methods the challenges use, as protocols.

The drawing functions take a @ref turtle_challenges.pen.Pen instead of creating
a turtle themselves. A real `turtle.Turtle` fits the protocol, and so does the
recording fake of the tests, which lets every challenge be tested without a
window.
"""

from typing import Protocol

## A color as the turtle accepts it here: a name or an RGB tuple of 0 to 255.
Color = str | tuple[int, int, int]


class Pen(Protocol):
    """!
    @brief The part of `turtle.Turtle` that the challenges call.
    """

    def forward(self, distance: float, /) -> None:
        """!
        @brief Move forward, drawing if the pen is down.

        @param distance How far to move, in turtle units.
        """
        ...

    def right(self, angle: float, /) -> None:
        """!
        @brief Turn clockwise.

        @param angle Degrees to turn.
        """
        ...

    def penup(self) -> None:
        """!
        @brief Lift the pen: moves leave no line.
        """
        ...

    def pendown(self) -> None:
        """!
        @brief Lower the pen: moves draw a line.
        """
        ...

    def color(self, color: Color, /) -> None:
        """!
        @brief Set the pen and fill color.

        @param color A color name or an RGB tuple of 0 to 255.
        """
        ...

    def circle(self, radius: float, /) -> None:
        """!
        @brief Draw a circle that starts at the turtle and curves left.

        @param radius Radius of the circle, in turtle units.
        """
        ...

    def heading(self) -> float:
        """!
        @brief Return the direction the turtle faces, in degrees.
        """
        ...

    def setheading(self, to_angle: float, /) -> None:
        """!
        @brief Face a direction.

        @param to_angle Degrees: 0 is east, 90 is north.
        """
        ...

    def pensize(self, width: int, /) -> None:
        """!
        @brief Set the thickness of the line.

        @param width Thickness in pixels.
        """
        ...

    def speed(self, speed: int, /) -> None:
        """!
        @brief Set the animation speed.

        @param speed 0 is fastest (no animation); 1 to 10 run from slow to fast.
        """
        ...


class Window(Protocol):
    """!
    @brief The part of the turtle screen that the command line calls.
    """

    def exitonclick(self) -> None:
        """!
        @brief Keep the window open until it is clicked, then close it.
        """
        ...
