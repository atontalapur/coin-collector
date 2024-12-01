import arcade
from PIL import ImageFilter
from level import Level
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_SETTINGS

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
        self.level.environment.update()
        self.game_view_screen = arcade.get_image()
        # temp -> leaderboard will be drawn
        if len(self.level.environment.coin_list) == 0:
            arcade.exit()

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
        self.movement_press(key)

        # Quit
        if key == arcade.key.Q:
            arcade.exit()
        # Restart level environment
        elif key == arcade.key.R:
            self.setup()
        elif key == arcade.key.ESCAPE:
            pause_view = PauseView(self)
            self.window.show_view(pause_view)

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




class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.level_settings = LEVEL_SETTINGS[self.game_view.lvl]
        self.image = game_view.game_view_screen
        self.blur_image=None

    def on_show_view(self):
        if self.image:
            self.blur_image = self.image.filter(ImageFilter.GaussianBlur(5))

    def on_draw(self):
        self.clear()

        if self.blur_image:
            bg_texture = arcade.Texture("blurred background", self.blur_image)
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, bg_texture)

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        #player_sprite = self.game_view.level.environment.player
        #player_sprite.draw()

        # draw an orange filter over him
        #arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          #right=player_sprite.right,
                                          #top=player_sprite.top,
                                          #bottom=player_sprite.bottom,
                                          #color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to return",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to reset",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 30,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:   # resume game
            self.window.show_view(self.game_view)
            background_color = self.level_settings["BACKGROUND_COLOR"]
            arcade.set_background_color(background_color)
        elif key == arcade.key.ENTER:  # reset game
            game = Game(self.game_view.lvl)
            self.window.show_view(game)