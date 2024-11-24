import arcade
import pyglet
from home import GameHome
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

def main():
    """Main function"""
    window_icon = pyglet.image.load("icons8-coin-32.png")
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_icon(window_icon)
    window.set_location(0, 30)
    game_view = GameHome()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()
