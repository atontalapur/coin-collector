import pytest
import arcade
from game_home import GameHome
from level_screen import Level_Screen
import controller_manager
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from controller import Controller


def test_initial_state():
    window = arcade.Window(800, 600, "Test Window")
    game = GameHome()
    # window.show_view(game)
    assert game.text_angle == 0
    assert game.time_elapsed == 0.0
    assert game.user_text_box.text == "Enter User Name"

def test_on_mouse_press():
    window = arcade.Window(800, 600, "Test Window")
    game = GameHome()
    window.show_view(game)
    game.on_mouse_press(0, 0, arcade.MOUSE_BUTTON_LEFT, 0)
    assert game.user_text_box.text == ""

def test_on_click_open_empty_username():
    window = arcade.Window(800, 600, "Test Window")
    game = GameHome()
    window.show_view(game)
    game.user_text_box.text = ""
    game.on_click_open(None)
    assert len(game.text_box_manager.children) == 1

def test_on_click_open_valid_username():
    window = arcade.Window(800, 600, "Test Window")
    game = GameHome()
    window.show_view(game)
    game.user_text_box.text = "Thomas"
    game.on_click_open(None)
    assert(game.confirm_box_button.on_click())


def test_on_key_press_escape():
    window = arcade.Window(800, 600, "Test Window")
    game = GameHome()
    window.show_view(game)
    game.user_text_box.text = "Some User"
    game.on_key_press(arcade.key.ESCAPE, 0)
    assert game.user_text_box.text == "Enter User Name"


