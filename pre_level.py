
import arcade
import arcade.gui
import math
from settings import *

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class GameHome(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=False)
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="Catch the Coins",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 40,
            color=arcade.color.YELLOW,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney Future"
        )

        self.new_player = arcade.Text(
            text="Level 1",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 260,
            color=arcade.color.YELLOW,
            font_size=80,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )

        self.difficulty = arcade.Text(
            text="Difficulty: Easy",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 360,
            color=arcade.color.YELLOW,
            font_size=30,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.text_box_manager = arcade.gui.UIManager()
        self.text_box_manager.enable()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.new_profile_button = arcade.gui.UIFlatButton(text="Play", width=200)





        self.v_box.add(self.new_profile_button.with_space_around(top=200))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )

        self.high_score = arcade.Text(
            text="high score: 0",
            start_x=SCREEN_WIDTH - 1140,
            start_y=SCREEN_HEIGHT - 170,
            color=arcade.color.GOLD,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

        self.trophy = arcade.load_texture("assets/trophy.jpeg")

    def new_user_open(self, event):
            message_box = arcade.gui.UIMessageBox(
                message_text=(
                    "Created Profile"
                ),
                width=150,
                height=150,
                buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)

    def load_sounds(self):
        #self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("sounds/Collision.wav")
        #self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        #self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        self.heading_text.angle = 6 * math.sin(self.time_elapsed * 2)
        self.heading_text.color = (
            int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 3))),
            int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 2))),
            int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 4))),
        )
        self.heading_text.font_size = 70 + 5 * math.sin(self.time_elapsed * 2)
        self.heading_text.start_y = SCREEN_HEIGHT - 60 + 10 * math.sin(self.time_elapsed * 2)


    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.rotation = self.text_angle
        self.heading_text.draw()
        self.new_player.draw()
        self.manager.draw()
        self.trophy.draw_scaled(55, 550, 0.2, 0.2)
        self.high_score.draw()
        self.difficulty.draw()



if __name__ == "__main__":
    window = GameHome()
    window.setup()
    arcade.run()