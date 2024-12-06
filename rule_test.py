import pytest
from rule_page import Rule_Page
import arcade
import controller_manager
from controller import Controller

@pytest.fixture
def rule_page():
    return Rule_Page(1)


def test_initial_rule_page() :
    window = arcade.Window(1200,650,"Test Window")
    view = Rule_Page(1)
    window.show_view(view)
    assert view.text_angle == 0
    assert view.new_player.text == "How to Play?"

def test_rules() :
    window = arcade.Window(1200, 650, "Test Window")
    view = Rule_Page(1)
    window.show_view(view)
    assert view.rule1.text == "1) Collect all the coins in 60 seconds to win"
    assert view.rule2.text == "2) Press escape to pause the game, play a different level, or restart the game"
    assert view.rule3.text == "3) Use arrow keys to move the player"
    assert view.rule4.text== "4) Use space bar to jump"

def test_game_launch() :
    window = arcade.Window(1200, 650, "Test Window")
    view = Rule_Page(1)
    window.show_view(view)
    assert view.play_button.on_click == view.game_open()
