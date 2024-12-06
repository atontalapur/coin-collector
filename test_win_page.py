from unittest.mock import patch

import pytest
import arcade
from win_game import WinGame
import controller_manager

@pytest.fixture
def win_page():
    return WinGame(10)

def test_win_page_status() :
    window = arcade.Window(800, 600, "Test Window")
    view = WinGame(10)
    window.show_view(view)
    win_page = WinGame(10)
    assert win_page.heading_text != "You Win!"


def test_time_taken():
    window = arcade.Window(800, 600, "Test Window")
    view = WinGame(10)
    window.show_view(view)
    win_page = WinGame(10)
    assert win_page.time_text != "Time Taken: " + str(10) + " seconds"


def test_quit():
    window = arcade.Window(800, 600, "Test Window")
    view = WinGame(10)
    window.show_view(view)

    with patch('arcade.exit') as mock_exit:
        view.exit_button.on_click(None)
        mock_exit.assert_called_once()

def test_open_level_view():
    window = arcade.Window(800, 600, "Test Window")
    view = WinGame(10)
    window.show_view(view)

    with patch.object(controller_manager.controller, 'to_level_screen') as mock_to_level_screen:
        view.next_level_button.on_click(None)
        mock_to_level_screen.assert_called_once()
