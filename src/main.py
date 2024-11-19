import arcade
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

def main():
    """Main function"""
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.set_location(0, 30)
    game_view = Game()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()
