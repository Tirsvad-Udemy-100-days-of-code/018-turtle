import random

from turtle_challenges.colors import random_color, random_palette_color
from turtle_challenges.constants import (
    COLOR_CHANNEL_MAX,
    COLOR_CHANNEL_MIN,
    COLOR_PALETTE,
)


def test_random_color_is_a_tuple_of_three_integers() -> None:
    color = random_color(random.Random(1))

    assert isinstance(color, tuple)
    assert len(color) == 3
    assert all(isinstance(channel, int) for channel in color)


def test_random_color_channels_stay_in_range() -> None:
    rng = random.Random(2)

    for _ in range(500):
        assert all(
            COLOR_CHANNEL_MIN <= channel <= COLOR_CHANNEL_MAX
            for channel in random_color(rng)
        )


def test_random_color_is_repeatable_with_the_same_seed() -> None:
    first = [random_color(random.Random(7)) for _ in range(3)]
    second = [random_color(random.Random(7)) for _ in range(3)]

    assert first == second


def test_random_color_varies_between_calls() -> None:
    rng = random.Random(3)

    assert len({random_color(rng) for _ in range(20)}) > 1


def test_random_color_works_without_a_generator() -> None:
    assert len(random_color()) == 3


def test_random_palette_color_comes_from_the_palette() -> None:
    rng = random.Random(4)

    assert {random_palette_color(rng) for _ in range(100)} <= set(COLOR_PALETTE)


def test_random_palette_color_works_without_a_generator() -> None:
    assert random_palette_color() in COLOR_PALETTE
