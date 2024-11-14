import arcade
import pyglet
from player import Player
from level import Level
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class Game(arcade.Window):
    """Main application class."""
    def __init__(self):
        """Initialize the game window."""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # set window to open in top-left
        pyglet.window.Window.set_location(self, 0, 30)

        # all level components
        # temp -> hardcode level_1 for now
        self.level = Level("level_1")

    def on_update(self, delta_time):
        """Movement and game logic."""
        self.level.environment.update()

        # temp -> leaderboard will be drawn
        if len(self.level.environment.coin_list) == 0:
            self.exit()

    def on_draw(self):
        """Render the screen."""
        self.level.draw()

    def on_key_press(self, key, modifiers):
        """Keys that are pressed."""
        self.movement_press(key)

        # Quit
        if key == arcade.key.Q:
            self.exit()\
        # Restart level environment
        elif key == arcade.key.R:
            self.level.reset()

    def on_key_release(self, key, modifiers):
        """Keys that are released."""
        self.movement_release(key)
    
    def movement_press(self, key):
        """Checks if movement keys are pressed down. Supports arrow keys and WASD."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.level.environment.player.moving_up = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.level.environment.player.moving_down = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.level.environment.player.moving_left = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.level.environment.player.moving_right = True

    def movement_release(self, key):
        """Checks if movement keys were released. Supports arrow keys and WASD."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.level.environment.player.moving_up = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.level.environment.player.moving_down = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.level.environment.player.moving_left = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.level.environment.player.moving_right = False

    def exit(self):
        """Exit program."""
        self.close()
