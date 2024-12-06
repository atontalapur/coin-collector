import arcade
import arcade.gui
import math
from game.settings import *
import globals.controller_manager as controller_manager
import globals.database_manager as database_manager

DEFAULT_LINE_HEIGHT = 45
DEFAULT_FONT_SIZE = 20

class WinGame(arcade.View):
    def __init__(self, lvl, time_taken):
        super().__init__()
        self.leaderboard_data = database_manager.database.fetch_leaderboard(lvl, database_manager.username)

        self.text_angle = 0
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
            text=f"You Won!",
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


        self.time_text = arcade.Text(
            text=f"Time Taken: {time_taken:.3f} seconds",
            start_x=SCREEN_WIDTH / 2,
            start_y=SCREEN_HEIGHT - 240,
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
        color1=arcade.color.SKY_BLUE
        color2=arcade.color.DARK_SLATE_GRAY
        background_color = self.interpolate_color(color1, color2, t)
        arcade.set_background_color(background_color)

    def draw_leaderboard(self):
        """Draw the leaderboard rectangle and entries."""
        # Define the rectangle dimensions
        rect_x = SCREEN_WIDTH // 2
        rect_y = SCREEN_HEIGHT // 2 - 75
        rect_width = 600
        rect_height = 210

        # Draw the white rectangle
        arcade.draw_rectangle_filled(rect_x, rect_y, rect_width, rect_height, arcade.color.WHITE)

        # Draw the leaderboard entries
        self.draw_leaderboard_entries(rect_x, rect_y, rect_width, rect_height)

    def draw_leaderboard_entries(self, rect_x, rect_y, rect_width, rect_height):
        """Draw leaderboard entries inside the rectangle."""
        padding = 20
        line_height = 30
        start_y = rect_y + (rect_height // 2) - padding
        start_x = rect_x - (rect_width // 2) + padding

        # Draw top 5 entries
        for idx, (name, score) in enumerate(self.leaderboard_data[:5]):  # Limit to top 5
            entry_y = start_y - (idx * line_height + padding)
            arcade.draw_text(
                text=f"{idx + 1}. {name}: {score:.3f}",
                start_x=start_x,
                start_y=entry_y,
                color=arcade.color.BLACK,
                font_size=20,
                anchor_x="left",
                font_name="Kenney Future"
            )

        # Draw "Your best" entry (if exists in leaderboard_data)
        if len(self.leaderboard_data) > 5:
            best_score_name, best_score = self.leaderboard_data[5]
            entry_y = start_y - (5 * line_height + padding)
            arcade.draw_text(
                text=f"Your best score: {best_score:.3f}",
                start_x=start_x,
                start_y=entry_y,
                color=arcade.color.BLACK,
                font_size=20,
                anchor_x="left",
                font_name="Kenney Future"
            )

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.username_text.draw()
        self.heading_text.draw()
        self.level_text.draw()
        self.time_text.draw()

        # Draw the leaderboard rectangle and content
        self.draw_leaderboard()

        # Draw the UI manager
        self.manager.draw()

    def load_sounds(self):
        self.background_music = arcade.load_sound("sounds/click.wav")

    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)
