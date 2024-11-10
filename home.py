import arcade
import arcade.gui
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SHIP_SPEED, ENEMY_FREQ, CLOUD_FREQ


DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


class GameHome(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.text_angle = 0
        self.time_elapsed = 0.0
        arcade.set_background_color(arcade.color.SKY_MAGENTA)

    def load_sounds(self):
        self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.collision_sound = arcade.load_sound("sounds/Collision.wav")
        self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):


        self.load_sounds()

        # start background music and loop
        self.background_music.play(loop=True)

    def on_draw(self):

        self.clear()



    # def main(self):
    #     window = Game()
    #     window.setup()212
    #     arcade.run()

if __name__ == "__main__":
    window = GameHome()
    window.setup()
    arcade.run()
