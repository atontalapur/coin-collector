import arcade
import arcade.gui
import math
from game.settings import *
import globals.controller_manager as controller_manager

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20


class LooseGame(arcade.View):
    def __init__(self, num_coins):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0

        self.username_text = arcade.Text(
            text="atontalapur",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 20,
            color=arcade.color.YELLOW,
            font_size=15,
            anchor_x="center",
            anchor_y="center",
            font_name="Kenney Future"
        )
        self.heading_text = arcade.Text(
            text="You Lost :(",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 100,
            color=arcade.color.YELLOW,
            font_size=70,
            anchor_x="center",
            anchor_y="center",
            bold=False,
            italic=False,
            font_name="Kenney Future"
        )
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.underline_coin = arcade.Text(
            text="Num of Coins Collected:" + str(num_coins),
            start_x = SCREEN_WIDTH / 2,
            start_y = SCREEN_HEIGHT - 250,
            color = arcade.color.YELLOW,
            font_size = 20,
            anchor_x = "center",
            anchor_y = "center",
            bold = False,
            italic = True,
            font_name = "Kenney Future"
        )

        self.leaderboard_text = arcade.Text(
            text="LEADERBOARD TBD",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 330,
            color=arcade.color.YELLOW,
            font_size=70,
            anchor_x="center",
            anchor_y="center",
            bold=False,
            italic=True,
            font_name="Kenney Future"
        )

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=200, vertical=False)


        self.retry_button = arcade.gui.UIFlatButton(text="Select Level", width=200)
        self.v_box.add(self.retry_button.with_space_around(top=200, right=500))
        self.exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)
        self.v_box.add(self.exit_button.with_space_around(top=200))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )
        self.retry_button.on_click = self.level_select_launch

        self.exit_button.on_click = self.quit

    def interpolate_color(self, color1, color2, t):
        return (
            int(color1[0] * (1 - t) + color2[0] * t),
            int(color1[1] * (1 - t) + color2[1] * t),
            int(color1[2] * (1 - t) + color2[2] * t)
        )

    def level_select_launch(self, event):
        controller_manager.controller.to_level_screen()

    def quit(self, event):
        arcade.exit()

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        self.heading_text.font_size = 70 + 10 * math.sin(self.time_elapsed * 2)
        t = (math.sin(self.time_elapsed * 2) + 1) / 2
        self.heading_text.color = (
            int(255 * (1 - t) + 50 * t),
            int(255 * (1 - t) + 150 * t),
            int(0 * (1 - t) + 50 * t)
        )
        color1=arcade.color.REDWOOD
        color2=arcade.color.DARK_RED
        background_color = self.interpolate_color(color1, color2, t)
        arcade.set_background_color(background_color)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.username_text.draw()
        self.heading_text.draw()
        self.underline_coin.draw()

        self.leaderboard_text.draw()
        self.manager.draw()

    def load_sounds(self):
        # self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("sounds/click.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)





