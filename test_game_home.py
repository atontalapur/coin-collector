import arcade
import pytest
from home import GameHome, New_Player, Prior_Game, Rule_Page
from game import Game

# Test GameHome class
def test_game_home_initialization():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    assert game_home.heading_text.text == "Catch the Coins"
    assert game_home.returning_users.text == "Returning  Users"
    assert game_home.new_users.text == "New  Users"
    assert game_home.user_text_box.text == "Enter User Name"

def test_game_home_on_mouse_press():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.user_text_box.text = "Enter User Name"
    game_home.on_mouse_press(0, 0, arcade.MOUSE_BUTTON_LEFT, 0)
    assert game_home.user_text_box.text == ""

def test_game_home_on_click_open_empty():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.user_text_box.text = ""
    game_home.on_click_open(None)
    assert isinstance(game_home.text_box_manager.children[0][0], arcade.gui.UIMessageBox)

def test_game_home_on_click_open_valid_user():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.user_text_box.text = "Thomas"
    game_home.on_click_open(None)
    assert isinstance(window.current_view, Prior_Game)

def test_game_home_on_click_open_invalid_user():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.user_text_box.text = "InvalidUser"
    game_home.on_click_open(None)
    assert isinstance(game_home.text_box_manager.children[0][0], arcade.gui.UIMessageBox)

def test_game_home_new_user_open():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.new_user_open(None)
    assert isinstance(window.current_view, New_Player)

def test_game_home_prior_game_open():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.prior_game_open(None)
    assert isinstance(window.current_view, Prior_Game)

def test_game_home_on_key_press_enter():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.user_text_box.text = "Thomas"
    game_home.on_key_press(arcade.key.ENTER, None)
    assert isinstance(window.current_view, Prior_Game)

def test_game_home_on_key_press_escape():
    window = arcade.Window(800, 600, "Test Window")
    game_home = GameHome()
    window.show_view(game_home)
    game_home.user_text_box.text = "SomeUser"
    game_home.on_key_press(arcade.key.ESCAPE, None)
    assert game_home.user_text_box.text == "Enter User Name"

# Test New_Player class
def test_new_player_initialization():
    window = arcade.Window(800, 600, "Test Window")
    new_player = New_Player()
    window.show_view(new_player)
    assert new_player.heading_text.text == "Catch the Coins"
    assert new_player.new_player.text == "New Player"

def test_new_player_on_mouse_press():
    window = arcade.Window(800, 600, "Test Window")
    new_player = New_Player()
    window.show_view(new_player)
    new_player.user_text_box.text = "Enter New User Name"
    new_player.on_mouse_press(0, 0, arcade.MOUSE_BUTTON_LEFT, 0)
    assert new_player.user_text_box.text == ""

def test_new_player_change_status_available():
    window = arcade.Window(800, 600, "Test Window")
    new_player = New_Player()
    window.show_view(new_player)
    new_player.change_status(None)
    assert new_player.new_name_available.color == (0, 255, 0, 255)

def test_new_player_change_status_unavailable():
    window = arcade.Window(800, 600, "Test Window")
    new_player = New_Player()
    window.show_view(new_player)
    new_player.change_status(None)
    assert new_player.new_name_unavailable.color == (255, 0, 0, 255)

def test_new_player_new_user_open():
    window = arcade.Window(800, 600, "Test Window")
    new_player = New_Player()
    window.show_view(new_player)
    new_player.new_user_open(None)
    assert isinstance(window.current_view, GameHome)

# Test Prior_Game class
def test_prior_game_initialization():
    window = arcade.Window(800, 600, "Test Window")
    prior_game = Prior_Game()
    window.show_view(prior_game)
    assert prior_game.heading_text.text == "Thomas"

# Test Rule_Page class
def test_rule_page_initialization():
    window = arcade.Window(800, 600, "Test Window")
    rule_page = Rule_Page("level_1")
    window.show_view(rule_page)
    assert rule_page.heading_text.text == "Thomas"
    assert rule_page.new_player.text == "How to Play?"

def test_rule_page_game_open():
    window = arcade.Window(800, 600, "Test Window")
    rule_page = Rule_Page("level_1")
    window.show_view(rule_page)
    rule_page.game_open(None)
    assert isinstance(window.current_view, Game)
