import arcade
import arcade.gui
import math
from game.settings import *
import globals.controller_manager as controller_manager
import globals.database_manager as database_manager

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class LooseGame(arcade.View):
    def __init__(self, lvl, num_coins):
        super().__init__()
        self.lvl = lvl
        self.leaderboard_data = database_manager.database.fetch_leaderboard(lvl, database_manager.username)
        self.saved_score = False

        self.time_elapsed = 0.0

        self.username_text = arcade.Text(
            text=database_manager.username,
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

        self.level_text = arcade.Text(
            text=f"Level {lvl.split('_')[1]}",
            start_x=SCREEN_WIDTH / 2,
            start_y=SCREEN_HEIGHT - 200,
            color=arcade.color.YELLOW,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
            bold=False,
            italic=True,
            font_name="Kenney Future"
        )

        self.underline_coin = arcade.Text(
            text=f"Num of Coins Collected:  + {num_coins}",
            start_x=SCREEN_WIDTH / 2,
            start_y=SCREEN_HEIGHT - 250,
            color=arcade.color.YELLOW,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
            bold=False,
            italic=True,
            font_name="Kenney Future"
        )

        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout(space_between=200, vertical=False)

        self.next_level_button = arcade.gui.UIFlatButton(text="Select Level", width=200)
        self.v_box.add(self.next_level_button.with_space_around(top=500, right=500))
        self.exit_button = arcade.gui.UIFlatButton(text="Exit", width=200)
        self.v_box.add(self.exit_button.with_space_around(top=500))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                child=self.v_box),
        )

        self.next_level_button.on_click = self.level_select_launch
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
    
    def draw_leaderboard(self):
        import colorsys
        """Draw the leaderboard rectangle and entries."""
        # Define the rectangle dimensions
        rect_x = SCREEN_WIDTH // 2
        rect_y = SCREEN_HEIGHT // 2 - 75
        rect_width = 600
        rect_height = 210

        hue = (self.time_elapsed * 0.1) % 1.0
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        color = (int(r * 255), int(g * 255), int(b * 255))

        # Draw the white rectangle
        arcade.draw_rectangle_filled(rect_x, rect_y, rect_width, rect_height, arcade.color.BLACK)
        arcade.draw_rectangle_outline(rect_x, rect_y, rect_width, rect_height, color, border_width=5)

        # Draw the leaderboard entries
        self.draw_leaderboard_entries(rect_x, rect_y, rect_width, rect_height)

    def draw_leaderboard_entries(self, rect_x, rect_y, rect_width, rect_height):
        """Draw leaderboard entries inside the rectangle."""
        padding = 20
        line_height = 30
        start_y = rect_y + (rect_height // 2) - padding
        start_x = rect_x - (rect_width // 2) + padding

        inserted = False  # Track whether self.time_elapsed has been added

        # Handle existing leaderboard data
        entries = len(self.leaderboard_data[:5])
        idx = 0
        while idx < entries:
            name, score = self.leaderboard_data[idx]
            entry_y = start_y - (idx * line_height + padding)
            
            arcade.draw_text(
                text=f"{idx + 1}. {name}: {score:.2f}",
                start_x=start_x,
                start_y=entry_y,
                color=arcade.color.WHITE,
                font_size=20,
                italic=True,
                anchor_x="left",
                font_name="Kenney Future"
            )

            idx += 1

        # Handle case where self.time_elapsed is worse than all top 5 scores
        if len(self.leaderboard_data) > 5:
            _, score = self.leaderboard_data[5]
            entry_y = start_y - (5 * line_height + padding)
            arcade.draw_text(
                text=f"Your best: {score:.2f}",
                start_x=start_x,
                start_y=entry_y,
                color=arcade.color.WHITE,
                font_size=20,
                bold=True,
                anchor_x="left",
                font_name="Kenney Future"
            ) 

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.username_text.draw()
        self.heading_text.draw()
        self.level_text.draw()
        self.underline_coin.draw()

        # Draw the leaderboard rectangle and content
        self.draw_leaderboard()

        # Draw the UI manager
        self.manager.draw()

    def load_sounds(self):
        self.background_music = arcade.load_sound("sounds/click.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)
