from turtle_challenges import constants


def test_challenge_names_are_unique() -> None:
    assert len(set(constants.CHALLENGE_NAMES)) == len(constants.CHALLENGE_NAMES)
