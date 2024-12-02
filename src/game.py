import time

import arcade
import arcade.gui
from PIL import ImageFilter
from level import Level
import controller_manager
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
            time.sleep(1)
            controller_manager.controller.to_win(self.time_elapsed)
        if self.time_elapsed > 60:
            time.sleep(1)
            controller_manager.controller.to_loose(LEVEL_SETTINGS[self.lvl]["NUM_COINS"] -
            len(self.level.environment.coin_list))

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
            self._toggle_pause()
        elif key == arcade.key.L:
            controller_manager.controller.to_level_screen()

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

    def _toggle_pause(self):
        pause_view = PauseView(self)
        self.window.show_view(pause_view)




class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.time_elapsed = 0
        self.game_view = game_view
        self.level_settings = LEVEL_SETTINGS[self.game_view.lvl]
        self.image = game_view.game_view_screen
        self.blur_image=None
        self.ui_manager = arcade.gui.UIManager()
        self.ui_manager.enable()
        self.pause_text = arcade.Text(
            "PAUSED",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2 + 80,
            arcade.color.YELLOW_ROSE,
            50,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney Future"
        )
        button_style = {
            "font_name": ("Arial",),
            "font_size": 20,
            "font_color": arcade.color.WHITE,
            "bg_color": (52, 152, 219),
            "bg_color_pressed": (31, 97, 141),
            "border_color": arcade.color.BLACK,
            "border_width": 2,
            "border_color_pressed": arcade.color.YELLOW,
            "padding": (10, 20, 10, 20)
        }
        self.resume_button=arcade.gui.UIFlatButton(
            text="Resume",
            width=180,
            style=button_style
            )
        self.restart_button=arcade.gui.UIFlatButton(
            text="Restart",
            width=180,
            style=button_style
            )
        self.levelSelect = arcade.gui.UIFlatButton(
            text="Select Level",
            width=180,
            style=button_style
        )

        self.b_box=arcade.gui.UIBoxLayout(space_between=15)
        self.b_box.add(self.resume_button)
        self.b_box.add(self.restart_button)
        self.b_box.add(self.levelSelect)

        self.ui_manager.add(arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            align_y=-55,
            child=self.b_box
        ))

        self.resume_button.on_click=self.resume
        self.restart_button.on_click=self.restart
        self.levelSelect.on_click = self.level



    def on_show_view(self):
        if self.image:
            self.blur_image = self.image.filter(ImageFilter.GaussianBlur(10))

    def on_draw(self):
        self.clear()

        if self.blur_image:
            bg_texture = arcade.Texture("blurred background", self.blur_image)
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, bg_texture)

        self.pause_text.draw()
        self.ui_manager.draw()

    def on_update(self, delta_time):
        import colorsys
        self.time_elapsed += delta_time
        hue = (self.time_elapsed * 0.1) % 1.0  # Cycle through hue values
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        self.pause_text.color = (
            int(r * 255),
            int(g * 255),
            int(b * 255)
        )


    def resume(self, event):
        self.window.show_view(self.game_view)
        background_color = self.level_settings["BACKGROUND_COLOR"]
        arcade.set_background_color(background_color)

    def restart(self, event):
        game = Game(self.game_view.lvl)
        self.window.show_view(game)

    def level(self, event):
        controller_manager.controller.to_level_screen()
