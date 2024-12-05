import time

import arcade
import arcade.gui
from game.level import Level
import globals.controller_manager as controller_manager
import globals.database_manager as database_manager
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_SETTINGS


class Game(arcade.View):
    """Main application class."""
    def __init__(self, level):
        """Initialize the game window."""
        super().__init__()
        self.lvl = level

        self.box_x, self.box_y, self.box_width, self.box_height = SCREEN_WIDTH - 320, SCREEN_HEIGHT - 40, 285, 30
        self.game_view_screen=None
        self.setup()
    
    def setup(self):
        # all level components
        self.level = Level(self.lvl)

        self.time_elapsed = 0  # Initialize the timer

    def on_update(self, delta_time):
        self.time_elapsed += delta_time
        self.level.update()
        self.game_view_screen = arcade.get_image()

        if len(self.level.coin_list) == 0:
            time.sleep(1)
            database_manager.database.save_score(self.lvl, database_manager.username, self.time_elapsed)
            controller_manager.controller.to_win(self.lvl, self.time_elapsed)
        if self.time_elapsed > 60:
            time.sleep(1)
            controller_manager.controller.to_loose(self.lvl, LEVEL_SETTINGS[self.lvl]["NUM_COINS"] -
            len(self.level.coin_list))

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
        self.level.draw()
        self.draw_time_box()
    
    def draw_time_box(self):
        # Draw the box
        arcade.draw_lrtb_rectangle_filled(self.box_x, self.box_x + self.box_width, self.box_y + self.box_height, self.box_y, arcade.color.LIGHT_GRAY)

        # Draw the outline
        arcade.draw_lrtb_rectangle_outline(self.box_x, self.box_x + self.box_width, self.box_y + self.box_height, self.box_y, arcade.color.BLACK, 2)

        # Draw the text inside the box
        text = f"Coins left : {len(self.level.coin_list)}     Time: {int(self.time_elapsed) if self.time_elapsed < 1000 else 999}"
        arcade.draw_text(text, self.box_x + 10, self.box_y + 5, arcade.color.BLACK, 16, bold=True)

    def on_key_press(self, key, modifiers):
        """Keys that are pressed."""
        self.movement_press(key)

        # Quit
        if key == arcade.key.Q:
            arcade.exit()
        # Pause Menu - resume, restart, or select level
        elif key == arcade.key.ESCAPE:
            self._toggle_pause()
        elif key == arcade.key.R:
            self.level.setup()

    def on_key_release(self, key, modifiers):
        """Keys that are released."""
        self.movement_release(key)
    
    def movement_press(self, key):
        """Checks if movement keys are pressed down. Supports arrow keys and WASD."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.level.player.moving_up = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.level.player.moving_down = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.level.player.moving_left = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.level.player.moving_right = True

    def movement_release(self, key):
        """Checks if movement keys were released. Supports arrow keys and WASD."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.level.player.moving_up = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.level.player.moving_down = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.level.player.moving_left = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.level.player.moving_right = False

    def _toggle_pause(self):
         controller_manager.controller.to_pause_menu(self)
