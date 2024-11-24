import arcade

class Coin(arcade.Sprite):
    """Sprite to represent a moving coin."""
    def __init__(self, x, y, change_x, change_y, image, scale):
        """Initialize the coin."""
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.change_x = change_x
        self.change_y = change_y

    def update(self, walls):
        """Move the coin and bounce off walls. Speed never changes."""

        # update horizontal movement
        self.center_x += self.change_x

        # if there are horizontal collisions, move coin and negate velocity in the x direction
        walls_hit = arcade.check_for_collision_with_list(self, walls)
        for wall in walls_hit:
            if self.change_x > 0:
                self.right = wall.left
            elif self.change_x < 0:
                self.left = wall.right
        if len(walls_hit) > 0:
            self.change_x *= -1

        # update vertical movement
        self.center_y += self.change_y

        # if there are vertical collisions, move coin and negate velocity in the y direction
        walls_hit = arcade.check_for_collision_with_list(self, walls)
        for wall in walls_hit:
            if self.change_y > 0:
                self.top = wall.bottom
            elif self.change_y < 0:
                self.bottom = wall.top
        if len(walls_hit) > 0:
            self.change_y *= -1
