import arcade
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SHIP_SPEED, ENEMY_FREQ, CLOUD_FREQ



class GameHome(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
            pass

    def on_draw(self):
            self.clear()

    # def main(self):
    #     window = Game()
    #     window.setup()
    #     arcade.run()

if __name__ == "__main__":
    window = GameHome()
    window.setup()
    arcade.run()
    a
