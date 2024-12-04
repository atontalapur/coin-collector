import pytest
import arcade
from unittest.mock import patch
from game.level import Level
from game.coin import Coin
from game.player import Player
from game.obstacle import Obstacle
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT

@pytest.fixture
def level_1():
    """Fixture to set up a Level object for testing."""
    # nullify set_background_color, as we don't have a window
    with patch.object(arcade, 'set_background_color'):
        level = Level('level_1')
        return level

def test_level_initialization(level_1):
    """Test level initialization and setup."""
    assert level_1.level == 'level_1'
    assert level_1.coin_list
    assert level_1.obstacle_list
    assert level_1.player is not None

def test_coin_generation(level_1):
    """Test if coins are generated with valid positions."""
    coin_list = level_1.coin_list
    assert len(coin_list) > 0
    for coin in coin_list:
        assert isinstance(coin, Coin)
        assert coin.center_x >= 0
        assert coin.center_x <= SCREEN_WIDTH
        assert coin.center_y >= 0
        assert coin.center_y <= SCREEN_HEIGHT

def test_player_spawn(level_1):
    """Test if the player spawns in the correct position."""
    player = level_1.player
    assert player.center_x == level_1.level_settings['PLAYER_SPAWN_X']
    assert player.center_y == level_1.level_settings['PLAYER_SPAWN_Y']

def test_obstacle_setup(level_1):
    """Test if obstacles are set up correctly in the level."""
    obstacle_list = level_1.obstacle_list
    assert len(obstacle_list) > 0
    for obstacle in obstacle_list:
        assert isinstance(obstacle, Obstacle)
        assert obstacle.center_x >= 0
        assert obstacle.center_x <= SCREEN_WIDTH
        assert obstacle.center_y >= 0
        assert obstacle.center_y <= SCREEN_HEIGHT

def test_update_method(level_1):
    """Test if update method performs correctly."""
    # mock update methods for Player and Coin
    with patch.object(Player, 'update') as mock_player_update, \
         patch.object(Coin, 'update') as mock_coin_update:

        level_1.update()

        # ensure update methods for Player and Coin are being called appropriately
        mock_player_update.assert_called_once()
        assert mock_coin_update.call_count == len(level_1.coin_list)

def test_collect_coins(level_1):
    """Test coin collection logic."""
    # create test coin
    coin_1 = Coin(100, 200, 0, 0, ":resources:images/items/coinGold.png", 1)
    level_1.coin_list.append(coin_1)

    # move player to test coin
    level_1.player.center_x = 100
    level_1.player.center_y = 200

    level_1._update_collect()

    # ensure test coin is not in coin_list
    assert coin_1 not in level_1.coin_list

def test_draw_method(level_1):
    """Test if the draw method works as expected (checks if sprite lists are drawn)."""
    with patch.object(level_1.coin_list, 'draw') as mock_coin_draw, \
         patch.object(level_1.obstacle_list, 'draw') as mock_obstacle_draw, \
         patch.object(level_1.player, 'draw') as mock_player_draw:
        
        level_1.draw()
        
        mock_coin_draw.assert_called_once()
        mock_obstacle_draw.assert_called_once()
        mock_player_draw.assert_called_once()
