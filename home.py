
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
            start_y=SCREEN_HEIGHT - 100,
            color=arcade.color.YELLOW,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            rotation=90
        )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.text_box_manager = arcade.gui.UIManager()
        self.text_box_manager.enable()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)

        right_button_g = arcade.load_texture("textures/rightgreenarrow1.jpg", width=150, height=50)
        right_button_w = arcade.load_texture("textures/rightwhitearrow1.jpg", width=150, height=50)
        self.user_text_box = arcade.gui.UIInputText(width=250, height=50, font_size=20, font_name="Arial", anchor_x="center",
            anchor_y="center", multiline=False, text="")
        user_text_box_border = arcade.gui.UIBorder(child=self.user_text_box, border_width=2)
        self.confirm_box_button = arcade.gui.UITextureButton(texture=right_button_g, texture_hovered=right_button_w, width=150)
        #self.v_box.add(self.user_text_box)
        self.v_box.add(user_text_box_border)
        self.v_box.add(self.confirm_box_button)
        self.confirm_box_button.on_click = self.on_click_open
        self.key_pressed = False
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )

    def on_click_open(self, event):
        if self.user_text_box.text == "" or not self.user_text_box.text:
            message_box = arcade.gui.UIMessageBox(
                message_text=(
                    "The User information was not found.\n"
                    "Please check the information and try again or register a new account."
                ),
                width=450,
                height=150,
                buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)
        else:
            message_box = arcade.gui.UIMessageBox(
                message_text=(
                    "The User information was found!.\n"
                ),
                width=450,
                height=150,
                buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)

    def start_game(self, event):
        game = Game()
        game.setup()
        arcade.run()

    def load_sounds(self):
        self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.collision_sound = arcade.load_sound("sounds/Collision.wav")
        self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=True)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        self.text_angle = 10 * math.sin(self.time_elapsed * 2)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.rotation = self.text_angle
        self.heading_text.draw()
        self.manager.draw()
        self.text_box_manager.draw()


if __name__ == "__main__":
    window = GameHome()
    window.setup()
    arcade.run()