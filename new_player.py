
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
            start_y=SCREEN_HEIGHT - 30,
            color=arcade.color.YELLOW,
            font_size=40,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney Future"
        )

        self.new_player = arcade.Text(
            text="New Player",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 140,
            color=arcade.color.YELLOW,
            font_size=35,
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

        right_button_g = arcade.load_texture("textures/rightgreenarrow1.jpg", width=150, height=50)
        right_button_w = arcade.load_texture("textures/rightwhitearrow1.jpg", width=150, height=50)
        self.user_text_box = (arcade.gui.UIInputText
                              (width=250,
                               height=30,
                               font_size=10,
                               font_name="Arial",
                               anchor_x="center",
                               anchor_y="center",
                               multiline=False, text="Enter New User Name")
                            )
        user_text_box_border = arcade.gui.UIBorder(child=self.user_text_box, border_width=2)
        self.confirm_box_button = arcade.gui.UITextureButton(texture=right_button_g, texture_hovered=right_button_w, width=150)
        self.create_profile = arcade.gui.UIFlatButton(text="Create Profile", width=100)
        #self.v_box.add(self.user_text_box)
        self.v_box.add(user_text_box_border)
        self.v_box.add(self.confirm_box_button)
        self.r_box.add(self.create_profile.with_space_around(top=350, left=500))
        self.user_text_box.on_key_press = self.on_key_press
        self.user_text_box.on_mouse_press = self.on_mouse_press
        self.create_profile.on_click = self.new_user_open
        self.confirm_box_button.on_click = self.change_status
        self.key_pressed = False
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=1,
                child=self.r_box),
        )
        self.new_name_available = arcade.Text(
            text="Username Found!",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 330,
            color=arcade.color.COOL_GREY,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

        self.new_name_unavailable = arcade.Text(
            text="Username Not Found!",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 400,
            color=arcade.color.COOL_GREY,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.user_text_box.text = ""

    def change_status(self, event):
        available = False
        if available is True:
            self.new_name_available.color = arcade.color.GREEN
        elif available is False:
            self.new_name_unavailable.color = arcade.color.RED


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


    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.on_click_open(None)
        if key == arcade.key.ESCAPE:
            self.user_text_box.text = "Enter User Name"
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
        #self.text_angle = 10 * math.sin(self.time_elapsed * 2)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.rotation = self.text_angle
        self.heading_text.draw()
        self.new_player.draw()
        self.manager.draw()
        self.text_box_manager.draw()
        self.new_name_available.draw()
        self.new_name_unavailable.draw()



if __name__ == "__main__":
    window = GameHome()
    window.setup()
    arcade.run()