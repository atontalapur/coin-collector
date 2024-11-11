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
        arcade.set_background_color(arcade.color.COOL_GREY)

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a box group to align the 'open' button in the center
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a button. We'll click on this to open our window.
        # Add it v_box for positioning.
        test_message_box_button = arcade.gui.UIFlatButton(text="Test PopUp", width=150)
        self.v_box.add(test_message_box_button)

        # Add a hook to run when we click on the button.
        test_message_box_button.on_click = self.on_click_open
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box),
        )


    def on_click_open(self, event):
        message_box = arcade.gui.UIMessageBox(
            message_text=(
                "The User information was not found.\n"
                "Please check the information and try again or register a new account."
            ),
            width=400,
            height=150,
            buttons=["Ok"]
        )
        self.manager.add(message_box)

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
        self.manager.draw()


if __name__ == "__main__":
    window = GameHome()
    window.setup()
    arcade.run()
