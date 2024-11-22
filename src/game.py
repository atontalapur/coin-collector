import arcade
from level import Level
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game(arcade.View):
    """Main application class."""
    def __init__(self, level):
        """Initialize the game window."""
        super().__init__()
        self.lvl = level
        self.paused = False

        self.box_x, self.box_y, self.box_width, self.box_height = SCREEN_WIDTH - 320, SCREEN_HEIGHT - 40, 285, 30
        
        self.setup()
    
    def setup(self):
        # all level components
        self.level = Level(self.lvl)

        self.time_elapsed = 0  # Initialize the timer

    def on_update(self, delta_time):
        if not self.paused:
            self.time_elapsed += delta_time
            """Movement and game logic."""
            self.level.environment.update()

            # temp -> leaderboard will be drawn
            if len(self.level.environment.coin_list) == 0:
                self._exit()

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
        text = f"Coins left : {len(self.level.environment.coin_list)}     Time: {int(self.time_elapsed) if self.time_elapsed < 1000 else 999}"
        arcade.draw_text(text, self.box_x + 10, self.box_y + 5, arcade.color.BLACK, 16, bold=True)

    def on_key_press(self, key, modifiers):
        """Keys that are pressed."""
        self._movement_press(key)

        # Quit
        if key == arcade.key.Q:
            self._exit()
        # Restart level environment
        elif key == arcade.key.R:
            self.setup()
        elif key == arcade.key.ESCAPE:
            self._toggle_pause()

    def on_key_release(self, key, modifiers):
        """Keys that are released."""
        self._movement_release(key)
    
    def _movement_press(self, key):
        """Checks if movement keys are pressed down. Supports arrow keys and WASD."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.level.environment.player.moving_up = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.level.environment.player.moving_down = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.level.environment.player.moving_left = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.level.environment.player.moving_right = True
    
    def _exit(self):
        arcade.exit()

    def _toggle_pause(self):
        self.paused = not self.paused

    def _movement_release(self, key):
        """Checks if movement keys were released. Supports arrow keys and WASD."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.level.environment.player.moving_up = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.level.environment.player.moving_down = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.level.environment.player.moving_left = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.level.environment.player.moving_right = False
