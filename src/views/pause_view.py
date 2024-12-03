import arcade
import arcade.gui
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_SETTINGS
from PIL import ImageFilter
import globals.controller_manager as controller_manager
import globals.music_player as music_player

class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.time_elapsed = 0
        self.game_view = game_view
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
        self.ui_manager.disable()
        self.window.show_view(self.game_view)

    def restart(self, event):
        self.ui_manager.disable()
        self.game_view.level.setup()
        self.window.show_view(self.game_view)

    def level(self, event):
        self.ui_manager.disable()
        controller_manager.controller.to_level_screen()