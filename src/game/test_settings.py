import pytest
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, LEVEL_SETTINGS

def test_screen_settings():
    """Check for correct screen setting types."""
    assert isinstance(SCREEN_WIDTH, int), "SCREEN_WIDTH should be an integer"
    assert isinstance(SCREEN_HEIGHT, int), "SCREEN_HEIGHT should be an integer"
    assert isinstance(SCREEN_TITLE, str), "SCREEN_TITLE should be a string"

@pytest.mark.parametrize("level_name", LEVEL_SETTINGS.keys())
def test_level_settings(level_name):
    """Check for correct level setting types."""
    level = LEVEL_SETTINGS[level_name]

    # some levels may have more keys than this
    required_keys = [
        "BACKGROUND_COLOR",
        "BACKGROUND_MUSIC",
        "OBSTACLE_IMAGE",
        "OBSTACLE_PIXELS_X",
        "OBSTACLE_PIXELS_Y",
        "OBSTACLE_SCALING",
        "COIN_IMAGE",
        "COIN_SCALING",
        "NUM_COINS",
        "COIN_OFFSET",
        "COIN_FROM_BORDER",
        "COIN_MIN_SPEED",
        "COIN_MAX_SPEED",
        "PLAYER_IMAGE",
        "PLAYER_SPAWN_X",
        "PLAYER_SPAWN_Y",
        "PLAYER_SCALING",
        "PLAYER_SPEED",
    ]

    # All keys must be present
    for key in required_keys:
        assert key in level, f"'{key}' is missing in {level_name}"

    # Check for correct types
    assert isinstance(level["BACKGROUND_COLOR"], tuple), "BACKGROUND_COLOR should be a tuple"
    assert isinstance(level["BACKGROUND_MUSIC"], str), "BACKGROUND_MUSIC should be a string"
    assert isinstance(level["OBSTACLE_IMAGE"], str), "OBSTACLE_IMAGE should be a string"
    assert isinstance(level["OBSTACLE_PIXELS_X"], int), "OBSTACLE_PIXELS_X should be an integer"
    assert isinstance(level["OBSTACLE_PIXELS_Y"], int), "OBSTACLE_PIXELS_Y should be an integer"
    assert isinstance(level["OBSTACLE_SCALING"], float), "OBSTACLE_SCALING should be a float"
    assert isinstance(level["COIN_IMAGE"], str), "COIN_IMAGE should be a string"
    assert isinstance(level["COIN_SCALING"], float), "COIN_SCALING should be a float"
    assert isinstance(level["NUM_COINS"], int), "NUM_COINS should be an integer"
    assert isinstance(level["COIN_OFFSET"], int), "COIN_OFFSET should be an integer"
    assert isinstance(level["COIN_FROM_BORDER"], int), "COIN_FROM_BORDER should be an integer"
    assert isinstance(level["COIN_MIN_SPEED"], (int, float)), "COIN_MIN_SPEED should be a number"
    assert isinstance(level["COIN_MAX_SPEED"], (int, float)), "COIN_MAX_SPEED should be a number"
    assert isinstance(level["PLAYER_IMAGE"], str), "PLAYER_IMAGE should be a string"
    assert isinstance(level["PLAYER_SPAWN_X"], int), "PLAYER_SPAWN_X should be an integer"
    assert isinstance(level["PLAYER_SPAWN_Y"], int), "PLAYER_SPAWN_Y should be an integer"
    assert isinstance(level["PLAYER_SCALING"], float), "PLAYER_SCALING should be a float"
    assert isinstance(level["PLAYER_SPEED"], int), "PLAYER_SPEED should be an integer"
