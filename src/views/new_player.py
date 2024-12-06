import arcade
import arcade.gui
from game.settings import *
import globals.controller_manager as controller_manager
import globals.database_manager as database_manager

class New_Player(arcade.View):
    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="Catch the Coins",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 60,
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
            start_y=SCREEN_HEIGHT - 170,
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

        back_button_f = arcade.load_texture("textures/icons8-back-button-50.png", width=50, height=50)
        back_button_h = arcade.load_texture("textures/icons8-back-button-50 (1).png", width=50, height=50)
        self.user_text_box = (arcade.gui.UIInputText
                              (width=250,
                               height=30,
                               font_size=15,
                               font_name="Arial",
                               anchor_x="center",
                               anchor_y="center",
                               multiline=False, text="Enter New User Name")
                              )
        right_button_g = arcade.load_texture("textures/rightgreenarrow1.jpg", width=150, height=50)
        right_button_w = arcade.load_texture("textures/rightwhitearrow1.jpg", width=150, height=50)
        user_text_box_border = arcade.gui.UIBorder(child=self.user_text_box, border_width=2)
        self.confirm_box_button = arcade.gui.UITextureButton(texture=right_button_g, texture_hovered=right_button_w,
                                                             width=150)
        self.back_button = arcade.gui.UITextureButton(texture=back_button_h, texture_hovered=back_button_f, width=50,
                                                      height=50)
        # self.v_box.add(self.user_text_box)
        self.v_box.add(user_text_box_border)
        self.v_box.add(self.confirm_box_button)
        self.r_box.add(self.back_button.with_space_around(top=350, left=500))
        self.user_text_box.on_key_press = self.on_key_press
        self.user_text_box.on_mouse_press = self.on_mouse_press
        self.back_button.on_click = self.new_user_open
        self.confirm_box_button.on_click = self.change_status
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
            start_y=SCREEN_HEIGHT - 450,
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
            start_y=SCREEN_HEIGHT - 520,
            color=arcade.color.COOL_GREY,
            font_size=35,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT and self.user_text_box.text == "Enter New User Name":
            self.user_text_box.text = ""

    def change_status(self, event):
        if len(self.user_text_box.text) > 20:
            message_box = arcade.gui.UIMessageBox(
                    message_text=(
                        "Name is too long (Max 20 chars).\n"
                    ),
                    width=450,
                    height=150,
                    buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)
        elif not database_manager.database.check_user_exists(self.user_text_box.text):
            database_manager.username = self.user_text_box.text
            message_box = arcade.gui.UIMessageBox(
                    message_text=(
                        "User created.\n"
                    ),
                    width=450,
                    height=150,
                    buttons=["Ok"],
                    callback=self.on_ok_pressed
            )
            self.text_box_manager.add(message_box)
        else:
            message_box = arcade.gui.UIMessageBox(
                    message_text=(
                        "User already exists.\n"
                    ),
                    width=450,
                    height=150,
                    buttons=["Ok"]
            )
            self.text_box_manager.add(message_box)
    
    def on_ok_pressed(self, button_text: str):
        if button_text == "Ok":  # Check which button was pressed
            controller_manager.controller.to_level_screen()


    def new_user_open(self, event):
        self.text_box_manager.disable()
        self.manager.disable()
        controller_manager.controller.to_game_home()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.on_click_open(None)
        if key == arcade.key.ESCAPE:
            self.user_text_box.text = "Enter User Name"

    def setup(self):
        click = arcade.load_sound("sounds/click.wav")
        click.play(loop=False)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        # self.text_angle = 10 * math.sin(self.time_elapsed * 2)

    def on_draw(self):
        arcade.start_render()
        self.heading_text.draw()
        self.new_player.draw()
        self.manager.draw()
        self.text_box_manager.draw()
