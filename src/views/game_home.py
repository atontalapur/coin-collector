import arcade
import arcade.gui
import math
from game.settings import *
import globals.controller_manager as controller_manager

import globals.music_player as music_player

class GameHome(arcade.View):

    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="Catch the Coins",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 70,
            color=arcade.color.YELLOW,
            font_size=70,
            anchor_x="center",
            anchor_y="center",
            bold=False,
            italic=True,
            font_name="Kenney Future"
        )

        self.returning_users = arcade.Text(
            text="Returning  Users",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 215,
            color=arcade.color.YELLOW,
            font_size=50,
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
        self.r_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        #self.text_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)

        right_button_g = arcade.load_texture("../textures/rightgreenarrow1.jpg", width=150, height=50)
        right_button_w = arcade.load_texture("../textures/rightwhitearrow1.jpg", width=150, height=50)
        self.user_text_box = (arcade.gui.UIInputText
                              (width=250,
                               height=30,
                               font_size=15,
                               font_name="Arial",
                               anchor_x="center",
                               anchor_y="center",
                               multiline=False, text="Enter User Name", text_color=arcade.color.BLACK,
                               # Set text color to black
                               color=arcade.color.BLACK)
                              )
        user_text_box_border = arcade.gui.UIBorder(child=self.user_text_box, border_width=2)
        self.confirm_box_button = arcade.gui.UITextureButton(texture=right_button_g, texture_hovered=right_button_w,
                                                             width=150)
        self.new_profile_button = arcade.gui.UIFlatButton(text="Create Profile", width=200)
        # self.v_box.add(self.user_text_box)
        self.v_box.add(user_text_box_border)
        self.v_box.add(self.confirm_box_button)

        self.r_box.add(self.new_profile_button.with_space_around(top=340))
        self.user_text_box.on_key_press = self.on_key_press
        self.user_text_box.on_mouse_press = self.on_mouse_press
        self.confirm_box_button.on_click = self.on_click_open
        self.new_profile_button.on_click = self.new_user_open

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=3,
                child=self.v_box),
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=2,
                child=self.r_box),
        )
        self.new_users = arcade.Text(
            text="New  Users",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 425,
            color=arcade.color.YELLOW,
            font_size=50,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT and self.user_text_box.text == "Enter User Name":
            self.user_text_box.text = ""

    def on_click_open(self, event):
        if self.user_text_box.text == "" or self.user_text_box.text == "Enter User Name":
            message_box = arcade.gui.UIMessageBox(
                message_text=(
                    "Enter a username and try once again."
                ),
                width=450,
                height=150,
                buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)
        elif self.user_text_box.text == "Thomas":
            self.prior_game_open(None)
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

    def new_user_open(self, event):
        controller_manager.controller.to_new_player()

    def prior_game_open(self, event):
        controller_manager.controller.to_level_screen()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.on_click_open(None)
        if key == arcade.key.ESCAPE:
            self.user_text_box.text = "Enter User Name"

    def setup(self):
        self.background_music = arcade.load_sound("../sounds/click.wav")

        if music_player.music != "opening.wav":
            music_player.music = "opening.wav"
            music = arcade.load_sound(f"../sounds/{music_player.music}")
            music_player.player = music.play(loop=True)

    def on_update(self, delta_time):
            self.time_elapsed += delta_time
            radius = 10
            self.heading_text.start_x = SCREEN_WIDTH // 2 + radius * math.cos(self.time_elapsed * 2)
            self.heading_text.start_y = SCREEN_HEIGHT - 60 + radius * math.sin(self.time_elapsed * 2)
            self.heading_text.color = (
                int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 3))),
                int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 2))),
                int(255 * (0.5 + 0.5 * math.sin(self.time_elapsed * 4))),
            )
            self.heading_text.rotation = 3 * math.sin(self.time_elapsed * 2)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.draw()
        self.returning_users.draw()
        self.manager.draw()
        self.text_box_manager.draw()
        self.new_users.draw()