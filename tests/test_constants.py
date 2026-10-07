from turtle_challenges import constants


def test_color_mode_matches_the_largest_channel_value() -> None:
    assert constants.COLOR_MODE == constants.COLOR_CHANNEL_MAX == 255


def test_challenge_names_are_unique() -> None:
    assert len(set(constants.CHALLENGE_NAMES)) == len(constants.CHALLENGE_NAMES)


def test_walk_headings_are_the_four_compass_directions() -> None:
    assert constants.WALK_HEADINGS == (0, 90, 180, 270)


def test_palette_has_only_non_empty_names() -> None:
    assert constants.COLOR_PALETTE
    assert all(name for name in constants.COLOR_PALETTE)


def test_polygon_range_runs_from_triangle_to_decagon() -> None:
    assert constants.MIN_POLYGON_SIDES == 3
    assert constants.MAX_POLYGON_SIDES == 10
