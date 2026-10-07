"""!
@file constants.py
@brief Every constant of the project, in one place.

Numbers and names used by the challenges live here and nowhere else, so a
challenge can be tuned (for example the number of dashes) without touching its
drawing code.
"""

## Title of the turtle window.
WINDOW_TITLE = "Turtle Challenges"

## Largest value of one color channel; also the turtle color mode, so that
## colors can be given as RGB tuples from 0 to 255.
COLOR_MODE = 255

## Smallest value of one color channel.
COLOR_CHANNEL_MIN = 0

## Largest value of one color channel.
COLOR_CHANNEL_MAX = COLOR_MODE

## Degrees in a full turn.
FULL_TURN_DEGREES = 360

## Degrees in a right angle.
RIGHT_ANGLE_DEGREES = 90

## Challenge 1: number of sides of a square.
SQUARE_SIDES = 4

## Challenge 1: length of one side of the square, in turtle units.
SQUARE_SIDE_LENGTH = 100

## Challenge 2: number of dashes in the dashed line.
DASH_COUNT = 50

## Challenge 2: length of one dash, in turtle units.
DASH_LENGTH = 10

## Challenge 2: length of the gap after each dash, in turtle units.
GAP_LENGTH = 10

## Challenge 3: fewest sides of a polygon (a triangle).
MIN_POLYGON_SIDES = 3

## Challenge 3: most sides of a polygon drawn in a row (a decagon).
MAX_POLYGON_SIDES = 10

## Challenge 3: length of one side of a polygon, in turtle units.
POLYGON_SIDE_LENGTH = 100

## Challenge 3: named colors a polygon is drawn in.
COLOR_PALETTE: tuple[str, ...] = (
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
)

## Command line name of challenge 1.
CHALLENGE_SQUARE = "square"

## Command line name of challenge 2.
CHALLENGE_DASHED_LINE = "dashed-line"

## Command line name of challenge 3.
CHALLENGE_SHAPES = "shapes"

## Names of the challenges on the command line, in the order of the course.
CHALLENGE_NAMES: tuple[str, ...] = (
    CHALLENGE_SQUARE,
    CHALLENGE_DASHED_LINE,
    CHALLENGE_SHAPES,
)
