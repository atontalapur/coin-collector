import arcade
from settings import *
import controller_manager

class Level_Screen(arcade.View):

    def __init__(self):
        super().__init__()
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.heading_text = arcade.Text(
            text="atontalapur",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT - 20,
            color=arcade.color.YELLOW,
            font_size=15,
            anchor_x="center",
            anchor_y="center",
            font_name="Kenney Future"
        )
        arcade.set_background_color(arcade.color.COOL_GREY)

        self.manager = arcade.gui.UIManager()
        self.text_box_manager = arcade.gui.UIManager()
        self.text_box_manager.enable()
        self.manager.enable()

        self.level_1_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_2_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_3_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_4_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)
        self.level_5_box = arcade.gui.UIBoxLayout(space_between=10, vertical=False)

        one_white = arcade.load_texture("../textures/levelOneWhite132.jpg")
        one_black = arcade.load_texture("../textures/levelOneBlack150.jpg")
        self.level_one = arcade.gui.UITextureButton(texture=one_black, texture_hovered=one_white, width=300, height=114)


        self.level_1_box.add(self.level_one)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=-400,
                align_y=200,
                child=self.level_1_box),
        )

        two_white = arcade.load_texture("../textures/Level2_White.png")
        two_black = arcade.load_texture("../textures/Level2_Black.png")
        self.level_two = arcade.gui.UITextureButton(texture=two_black, texture_hovered=two_white, width=300, height=114)

        self.level_2_box.add(self.level_two)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=0,
                align_y=200,
                child=self.level_2_box),
        )

        three_white = arcade.load_texture("../textures/Level3_White.png")
        three_black = arcade.load_texture("../textures/Level3_Black.png")
        self.level_three = arcade.gui.UITextureButton(texture=three_black, texture_hovered=three_white, width=300, height=114)

        self.level_3_box.add(self.level_three)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=400,
                align_y=200,
                child=self.level_3_box),
        )

        four_white = arcade.load_texture("../textures/Level4_White.png")
        four_black = arcade.load_texture("../textures/Level4_Black.png")
        self.level_four = arcade.gui.UITextureButton(texture=four_black, texture_hovered=four_white, width=300, height=114)

        self.level_4_box.add(self.level_four)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=-200,
                align_y=-100,
                child=self.level_4_box),
        )

        five_white = arcade.load_texture("../textures/Level5_White.png")
        five_black = arcade.load_texture("../textures/Level5_Black.png")
        self.level_five = arcade.gui.UITextureButton(texture=five_black, texture_hovered=five_white, width=300,
                                                     height=114)

        self.level_5_box.add(self.level_five)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                align_x=200,
                align_y=-100,
                child=self.level_5_box),
        )
        self.level_one.on_click = self.level_click_1
        self.level_two.on_click = self.level_click_2
        self.level_three.on_click = self.level_click_3
        self.level_four.on_click = self.level_click_4
        self.level_five.on_click = self.level_click_5


        self.high_score = arcade.Text(
            text="high score: 0",
            start_x=SCREEN_WIDTH - 1140,
            start_y=SCREEN_HEIGHT - 170,
            color=arcade.color.GOLD,
            font_size=20,
            anchor_x="center",
            anchor_y="center",
            bold=True,
            italic=True,
            font_name="Kenney High Square"
        )

        self.trophy = arcade.load_texture("../textures/trophy.jpeg")


    def load_sounds(self):
        # self.background_music = arcade.load_sound("sounds/Apoxode_-_Electric_1.wav")
        self.background_music = arcade.load_sound("../sounds/Collision.wav")
        # self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav")
        # self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav")


    def level_click_1(self, event):
        # get the current level of user
        #if the level ID is greater than the current level of user, then show a message box
        # that the user has not reached that level yet
        #else, open the rules page
        print("Need to add logic to restrict the levels")
        controller_manager.controller.to_rule_page("level_1")
    

    def level_click_2(self, event):
        # get the current level of user
        #if the level ID is greater than the current level of user, then show a message box
        # that the user has not reached that level yet
        #else, open the rules page
        print("Need to add logic to restrict the levels")
        controller_manager.controller.to_rule_page("level_2")
    

    def level_click_3(self, event):
        # get the current level of user
        #if the level ID is greater than the current level of user, then show a message box
        # that the user has not reached that level yet
        #else, open the rules page
        print("Need to add logic to restrict the levels")
        controller_manager.controller.to_rule_page("level_3")
    

    def level_click_4(self, event):
        # get the current level of user
        #if the level ID is greater than the current level of user, then show a message box
        # that the user has not reached that level yet
        #else, open the rules page
        print("Need to add logic to restrict the levels")
        controller_manager.controller.to_rule_page("level_4")
    

    def level_click_5(self, event):
        # get the current level of user
        #if the level ID is greater than the current level of user, then show a message box
        # that the user has not reached that level yet
        #else, open the rules page
        print("Need to add logic to restrict the levels")
        controller_manager.controller.to_rule_page("level_5")


    def setup(self):
        self.load_sounds()
        self.background_music.play(loop=False)



    def on_update(self, delta_time):
        self.time_elapsed += delta_time


    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.heading_text.draw()
        # self.new_player.draw()
        self.manager.draw()
        #self.trophy.draw_scaled(55, 550, 0.2, 0.2)
        #self.high_score.draw()
        # self.difficulty.draw()