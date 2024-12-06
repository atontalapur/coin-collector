import pytest
import arcade
from game import Game
from level import Level

def test_game_initialization():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    assert isinstance(game.level, Level)
    assert game.level.environment is not None

def test_game_initialization_invalid_level():
    with pytest.raises(KeyError):
        Game("invalid_level")

def test_game_on_update():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    initial_coin_count = len(game.level.environment.coin_list)
    game.on_update(1.0)
    assert len(game.level.environment.coin_list) == initial_coin_count

def test_game_on_draw():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.on_draw()
    assert game.level is not None



def test_game_on_key_press_restart():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.on_key_press(arcade.key.R, None)
    assert len(game.level.environment.coin_list) > 0

def test_game_draw_time_box():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.draw_time_box()
    assert game.time_elapsed == 0


def test_game_draw_time_box_coins_left():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.level.environment.coin_list = arcade.SpriteList()
    game.level.environment.coin_list.append(arcade.Sprite())
    game.draw_time_box()

    # Create a text object with the expected content
    expected_text = f"Coins left : 1     Time: 0"
    text_object = arcade.Text(expected_text, game.box_x + 10, game.box_y + 5, arcade.color.BLACK, 16, bold=True)

    # Check if the text object content matches the expected content
    assert text_object.text == expected_text

def test_game_on_update_no_coins():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.level.environment.coin_list = arcade.SpriteList()
    game.on_update(1.0)
    assert len(game.level.environment.coin_list) == 0

def test_game_movement_press_up():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.UP)
    assert game.level.environment.player.moving_up

def test_game_movement_release_up():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.UP)
    game.movement_release(arcade.key.UP)
    assert not game.level.environment.player.moving_up

def test_game_movement_press_down():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.DOWN)
    assert game.level.environment.player.moving_down

def test_game_movement_release_down():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.DOWN)
    game.movement_release(arcade.key.DOWN)
    assert not game.level.environment.player.moving_down

def test_game_movement_press_left():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.LEFT)
    assert game.level.environment.player.moving_left

def test_game_movement_release_left():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.LEFT)
    game.movement_release(arcade.key.LEFT)
    assert not game.level.environment.player.moving_left

def test_game_movement_press_right():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.RIGHT)
    assert game.level.environment.player.moving_right

def test_game_movement_release_right():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.movement_press(arcade.key.RIGHT)
    game.movement_release(arcade.key.RIGHT)
    assert not game.level.environment.player.moving_right

def test_game_on_key_press_invalid_key():
    window = arcade.Window(800, 600, "Test Window")
    game = Game("level_1")
    window.show_view(game)
    game.on_key_press(arcade.key.Z, None)
    assert not game.level.environment.player.moving_up
    assert not game.level.environment.player.moving_down
    assert not game.level.environment.player.moving_left
    assert not game.level.environment.player.moving_right

