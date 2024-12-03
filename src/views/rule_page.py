import arcade
from game.settings import *
import globals.controller_manager as controller_manager

class Rule_Page(arcade.View):

    def __init__(self, level):
        self.level = level
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="atontalapur",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 20,
            color=arcade.color.YELLOW,
            font_size=15,
            anchor_x="center",
            anchor_y="center",
            font_name="Kenney Future"
        )

        self.new_player = arcade.Text(
            text="How to Play?",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 100,
            color=arcade.color.YELLOW,
            font_size=80,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )

        self.rule1 = arcade.Text(
            text="1) Collect all the coins in 60 seconds to win",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 200,
            color=arcade.color.YELLOW,
            font_size=30,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )

        self.rule2 = arcade.Text(
            text="2) Press escape to pause the game, play a different level, or restart the game",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 260,
            color=arcade.color.YELLOW,
            font_size=30,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )

        self.rule3 = arcade.Text(
            text="3) Use Up, Down, Left, and Right arrow keys or W,A,S,D keys to move the player",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 320,
            color=arcade.color.YELLOW,
            font_size=30,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High"
        )

        self.rule4 = arcade.Text(
            text="4) Have fun!",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 380,
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
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.play_button = arcade.gui.UIFlatButton(text="Play", width=200)

        self.v_box.add(self.play_button.with_space_around(top=300))
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )
        self.play_button.on_click = self.game_open

    def setup(self):
        click = arcade.load_sound("sounds/click.wav")
        click.play(loop=False)

    def game_open(self, event):
        controller_manager.controller.to_game(self.level)

    def on_update(self, delta_time):
        self.time_elapsed += delta_time

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.rotation = self.text_angle
        self.heading_text.draw()
        self.new_player.draw()
        self.manager.draw()
        self.rule1.draw()
        self.rule2.draw()
        self.rule3.draw()
        self.rule4.draw()
