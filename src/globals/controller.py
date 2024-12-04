import arcade
import pyglet

from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from views.game_home import GameHome
from views.new_player import New_Player
from views.level_screen import Level_Screen
from views.rule_page import Rule_Page
from views.pause_view import PauseView
from game.game import Game
from views.win_game import WinGame
from views.loose_game import LooseGame

import globals.controller_manager as controller_manager

class Controller(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.set_location(0, 30)
        self.set_icon(pyglet.image.load("textures/icons8-coin-128.png"))

        self.to_game_home()
    
    def to_game_home(self):
        view = GameHome()
        view.setup()
        self.show_view(view)
    
    def to_new_player(self):
        view = New_Player()
        view.setup()
        self.show_view(view)

    def to_level_screen(self):
        view = Level_Screen()
        view.setup()
        self.show_view(view)
    
    def to_rule_page(self, level):
        view = Rule_Page(level)
        view.setup()
        self.show_view(view)
    
    def to_game(self, level):
        view = Game(level)
        self.show_view(view)
    
    def to_pause_menu(self, game_view):
        view = PauseView(game_view)
        self.show_view(view)

    def to_win(self, time_taken):
        view = WinGame(time_taken)
        view.setup()
        self.show_view(view)

    def to_loose(self, num_coins):
        view = LooseGame(num_coins)
        view.setup()
        self.show_view(view)
