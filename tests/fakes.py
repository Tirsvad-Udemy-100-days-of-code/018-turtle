"""Test doubles that stand in for the turtle and its window."""

from turtle_challenges.pen import Color


class FakePen:
    """A pen that records every call instead of drawing.

    The heading follows `setheading` and `right`, like a real turtle that
    starts facing east, so code that reads `heading()` behaves as in a window.
    """

    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[object, ...]]] = []
        self._heading = 0.0

    def _record(self, name: str, *args: object) -> None:
        self.calls.append((name, args))

    def args_of(self, name: str) -> list[tuple[object, ...]]:
        """Return the arguments of every call to `name`, in order."""
        return [args for call, args in self.calls if call == name]

    def names(self) -> list[str]:
        """Return the name of every call, in order."""
        return [call for call, _ in self.calls]

    def forward(self, distance: float, /) -> None:
        self._record("forward", distance)

    def right(self, angle: float, /) -> None:
        self._record("right", angle)
        self._heading = (self._heading - angle) % 360

    def penup(self) -> None:
        self._record("penup")

    def pendown(self) -> None:
        self._record("pendown")

    def color(self, color: Color, /) -> None:
        self._record("color", color)

    def circle(self, radius: float, /) -> None:
        self._record("circle", radius)

    def heading(self) -> float:
        return self._heading

    def setheading(self, to_angle: float, /) -> None:
        self._record("setheading", to_angle)
        self._heading = to_angle % 360

    def pensize(self, width: int, /) -> None:
        self._record("pensize", width)

    def speed(self, speed: int, /) -> None:
        self._record("speed", speed)


class FakeWindow:
    """A window that records whether it was told to wait for a click."""

    def __init__(self) -> None:
        self.waited_for_click = False

    def exitonclick(self) -> None:
        self.waited_for_click = True
