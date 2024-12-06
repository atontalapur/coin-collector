import pytest
from unittest.mock import patch
import arcade
import controller_manager
from loose_game import LooseGame


@pytest.fixture
def loose_page():
    return LooseGame(10)

def test_win_page_status() :
    window = arcade.Window(800, 600, "Test Window")
    view = LooseGame(10)
    window.show_view(view)
    win_page = LooseGame(10)
    assert win_page.heading_text != "You Lost :("

def test_coins_collected():
    window = arcade.Window(800, 600, "Test Window")
    view = LooseGame(10)
    window.show_view(view)
    win_page = LooseGame(10)
    assert win_page.coins_collected_text != "Num of Coins Collected:" + str(10)



def test_quit():
    window = arcade.Window(800, 600, "Test Window")
    view = LooseGame(10)
    window.show_view(view)

    with patch('arcade.exit') as mock_exit:
        view.exit_button.on_click(None)
        mock_exit.assert_called_once()

def test_open_level_view():
    window = arcade.Window(800, 600, "Test Window")
    view = LooseGame(10)
    window.show_view(view)

    with patch.object(controller_manager.controller, 'to_level_screen') as mock_to_level_screen:
        view.retry_button.on_click(None)
        mock_to_level_screen.assert_called_once()
