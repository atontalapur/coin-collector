import arcade
from player import Player
from level import Level
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE

class Game(arcade.Window):
    """Main application class."""
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # all level components
        self.level = Level()

    def setup(self):
        """Set up the game and initialize variables."""
        self.level.setup()

    def on_draw(self):
        """Render the screen."""
        self.clear()

        self.level.environment.wall_list.draw()
        self.level.environment.coin_list.draw()
        self.level.environment.player.draw()

    def on_update(self, delta_time):
        """Movement and game logic."""
        self.level.update()

        if len(self.level.environment.coin_list) == 0:
            self.close()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP:
            self.level.environment.player.up_pressed = True
        elif key == arcade.key.DOWN:
            self.level.environment.player.down_pressed = True
        elif key == arcade.key.LEFT:
            self.level.environment.player.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.level.environment.player.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.UP:
            self.level.environment.player.up_pressed = False
        elif key == arcade.key.DOWN:
            self.level.environment.player.down_pressed = False
        elif key == arcade.key.LEFT:
            self.level.environment.player.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.level.environment.player.right_pressed = False
