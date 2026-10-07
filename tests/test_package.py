import turtle_challenges
from turtle_challenges import constants


def test_package_can_be_imported_and_is_documented() -> None:
    assert turtle_challenges.__doc__


def test_color_mode_is_the_rgb_range_of_the_course() -> None:
    assert constants.COLOR_MODE == 255


def test_window_title_is_not_empty() -> None:
    assert constants.WINDOW_TITLE
