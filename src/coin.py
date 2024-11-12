import arcade
import random

class Coin(arcade.Sprite):
    """Class to represent a moving coin."""
    def __init__(self, image, scale, c_x, c_y):
        super().__init__(image, scale)
        self.center_x = c_x
        self.center_y = c_y
        self.change_x = random.randrange(-4, 5)
        self.change_y = random.randrange(-4, 5)

    def update(self, walls):
        """Move the coin and bounce off walls."""
        self.center_x += self.change_x

        walls_hit = arcade.check_for_collision_with_list(self, walls)
        for wall in walls_hit:
            if self.change_x > 0:
                self.right = wall.left
            elif self.change_x < 0:
                self.left = wall.right
        if len(walls_hit) > 0:
            self.change_x *= -1

        self.center_y += self.change_y

        walls_hit = arcade.check_for_collision_with_list(self, walls)
        for wall in walls_hit:
            if self.change_y > 0:
                self.top = wall.bottom
            elif self.change_y < 0:
                self.bottom = wall.top
        if len(walls_hit) > 0:
            self.change_y *= -1
