import arcade
from constants import PLAYER_SPEED

class Player(arcade.Sprite):
    def __init__(self, image_file, scale, c_x, c_y):
        """Initialize the player sprite with a given image and scale."""
        super().__init__(image_file, scale)
        self.center_x = c_x
        self.center_y = c_y

        # track key presses
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def update(self, walls):
        """Move the player and stop at walls without bouncing."""

        # set where player is going
        if self.up_pressed and not self.down_pressed:
            self.change_y = PLAYER_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.change_y = -PLAYER_SPEED
        else:
            self.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.change_x = -PLAYER_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_x = PLAYER_SPEED
        else:
            self.change_x = 0
        
        # update horiziontal movement
        self.center_x += self.change_x

        # if there are horizontal collisions, move player
        walls_hit = arcade.check_for_collision_with_list(self, walls)
        for wall in walls_hit:
            if self.change_x > 0:
                self.right = wall.left
            elif self.change_x < 0:
                self.left = wall.right

        # update vertical movement
        self.center_y += self.change_y

        # if there are vertical collisions, move player
        walls_hit = arcade.check_for_collision_with_list(self, walls)
        for wall in walls_hit:
            if self.change_y > 0:
                self.top = wall.bottom
            elif self.change_y < 0:
                self.bottom = wall.top
