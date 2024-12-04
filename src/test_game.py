import pytest
import arcade
from unittest.mock import MagicMock, patch
from game.game import Game
from game.level import Level
import globals.controller_manager as controller_manager
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_SETTINGS

@pytest.fixture(autouse=True)
def patch_set_background_color():
    """Fixture to patch arcade.set_background_color for all tests."""
    with patch.object(arcade, 'set_background_color'):
        yield

@pytest.fixture
def game_instance():
    """Fixture to set up a Game instance without initializing the window."""
    with patch.object(Game, '__init__', lambda game_instance, level: None):
        game = Game('level_1')
            
        game.lvl = 'level_1'
        game.box_x, game.box_y, game.box_width, game.box_height = SCREEN_WIDTH - 320, SCREEN_HEIGHT - 40, 285, 30
        game.game_view_screen = None
        game.setup()
            
        return game

def test_game_initialization(game_instance):
    """Test if the game initializes with the correct level."""
    assert game_instance.lvl == 'level_1'
    assert isinstance(game_instance.level, Level)
    assert game_instance.level.level == 'level_1'

def test_game_setup(game_instance):
    """Test the setup method to ensure level components are initialized."""
    game_instance.setup()
    assert game_instance.level
    assert game_instance.time_elapsed == 0
    assert game_instance.game_view_screen is None

def test_game_on_update(game_instance):
    """Test if the on_update method works as expected."""
    with patch.object(Level, 'update'), \
         patch.object(arcade, 'get_image'):

        original_controller = controller_manager.controller
        
        try:
            # Replace the controller methods with MagicMock, as the controller does not exist
            controller_manager.controller = MagicMock()
            controller_manager.controller.to_win = MagicMock()
            controller_manager.controller.to_loose = MagicMock()

            # time passing
            game_instance.on_update(0.5)
            assert game_instance.time_elapsed == 0.5
            game_instance.level.update.assert_called_once()

            # test game ending with win
            game_instance.level.coin_list = []
            game_instance.on_update(0.5)
            controller_manager.controller.to_win.assert_called_once_with(game_instance.time_elapsed)

            # test game ending with lose
            game_instance.level.coin_list = [1]
            game_instance.time_elapsed = 59.6 
            game_instance.on_update(0.5)
            controller_manager.controller.to_loose.assert_called_once_with(LEVEL_SETTINGS[game_instance.lvl]["NUM_COINS"] - len(game_instance.level.coin_list))
        finally:
            controller_manager.controller = original_controller

def test_game_on_draw(game_instance):
    """Test if the on_draw method works correctly."""
    with patch.object(game_instance.level, 'draw') as mock_level_draw, \
         patch.object(game_instance, 'draw_time_box') as mock_draw_time_box, \
         patch.object(arcade, 'start_render'):

        game_instance.on_draw()
        mock_level_draw.assert_called_once()
        mock_draw_time_box.assert_called_once()

def test_draw_time_box(game_instance):
    """Test if the draw_time_box method works correctly."""
    with patch.object(arcade, 'draw_text') as mock_draw_text, \
         patch.object(arcade, 'draw_lrtb_rectangle_filled') as mock_draw_rect_filled, \
         patch.object(arcade, 'draw_lrtb_rectangle_outline') as mock_draw_rect_outline:
        
        game_instance.draw_time_box()

        mock_draw_rect_filled.assert_called_once_with(game_instance.box_x, game_instance.box_x + game_instance.box_width, game_instance.box_y + game_instance.box_height, game_instance.box_y, arcade.color.LIGHT_GRAY)

        mock_draw_rect_outline.assert_called_once_with(game_instance.box_x, game_instance.box_x + game_instance.box_width, game_instance.box_y + game_instance.box_height, game_instance.box_y, arcade.color.BLACK, 2)
        
        mock_draw_text.assert_called_once_with(f"Coins left : {len(game_instance.level.coin_list)}     Time: {int(game_instance.time_elapsed)}", game_instance.box_x + 10, game_instance.box_y + 5, arcade.color.BLACK, 
        16, bold=True)

def test_key_press(game_instance):
    """Test if key presses are handled correctly."""
    # Initially set all movement flags to False
    game_instance.level.player.moving_up = False
    game_instance.level.player.moving_down = False
    game_instance.level.player.moving_left = False
    game_instance.level.player.moving_right = False

    game_instance.on_key_press(arcade.key.UP, None)
    assert game_instance.level.player.moving_up

    game_instance.on_key_press(arcade.key.DOWN, None)
    assert game_instance.level.player.moving_down

    game_instance.on_key_press(arcade.key.LEFT, None)
    assert game_instance.level.player.moving_left

    game_instance.on_key_press(arcade.key.RIGHT, None)
    assert game_instance.level.player.moving_right

    game_instance.on_key_press(arcade.key.W, None)
    assert game_instance.level.player.moving_up

    game_instance.on_key_press(arcade.key.S, None)
    assert game_instance.level.player.moving_down

    game_instance.on_key_press(arcade.key.A, None)
    assert game_instance.level.player.moving_left

    game_instance.on_key_press(arcade.key.D, None)
    assert game_instance.level.player.moving_right

def test_key_release(game_instance):
    """Test if key releases are handled correctly."""
    game_instance.level.player.moving_up = True
    game_instance.level.player.moving_down = True
    game_instance.level.player.moving_left = True
    game_instance.level.player.moving_right = True

    game_instance.on_key_release(arcade.key.UP, None)
    assert not game_instance.level.player.moving_up

    game_instance.on_key_release(arcade.key.DOWN, None)
    assert not game_instance.level.player.moving_down

    game_instance.on_key_release(arcade.key.LEFT, None)
    assert not game_instance.level.player.moving_left

    game_instance.on_key_release(arcade.key.RIGHT, None)
    assert not game_instance.level.player.moving_right

def test_toggle_pause(game_instance):
    """Test if the pause functionality is triggered."""
    original_controller = controller_manager.controller

    try:
        controller_manager.controller = MagicMock()
        controller_manager.controller.to_pause_menu = MagicMock()
        game_instance._toggle_pause()
        controller_manager.controller.to_pause_menu.assert_called_once_with(game_instance)
    finally:
        controller_manager.controller = original_controller

def test_exit_game_on_q_key(game_instance):
    """Test if the game exits when Q is pressed."""
    with patch.object(arcade, 'exit') as mock_exit:
        game_instance.on_key_press(arcade.key.Q, None)
        mock_exit.assert_called_once()
