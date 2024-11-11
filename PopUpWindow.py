"""
Example code showing how to use the OKMessageBox
"""
import arcade
import arcade.gui
class MyWindow(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "OKMessageBox Example", resizable=True)
        arcade.set_background_color(arcade.color.COOL_GREY)

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Create a box group to align the 'open' button in the center
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a button. We'll click on this to open our window.
        # Add it v_box for positioning.
        test_message_box_button = arcade.gui.UIFlatButton(text="Test PopUp", width=150)
        self.v_box.add(test_message_box_button)

        # Add a hook to run when we click on the button.
        test_message_box_button.on_click = self.on_click_open
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box),
        )

    def on_click_open(self,event):
        message_box = arcade.gui.UIMessageBox(
            message_text=(
                "The User information was not found.\n"
                "Please check the information and try again or register a new account."
            ),
            width=400,
            height=150,
            buttons=["Ok"]
        )
        self.manager.add(message_box)

    def on_draw(self):
        self.clear()
        self.manager.draw()


window = MyWindow()
arcade.run()
