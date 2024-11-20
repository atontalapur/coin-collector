import arcade

class Player(arcade.Sprite):
    """Sprite to represent the player."""
    def __init__(self, x, y, speed, image, scale):
        """Initialize the player."""
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.player_speed = speed

        # track key presses
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self, walls):
        """Move the player and stop at walls without bouncing. Speed determined by key input."""

        # set where player is going
        if self.moving_up and not self.moving_down:
            self.change_y = self.player_speed
        elif self.moving_down and not self.moving_up:
            self.change_y = -self.player_speed
        else:
            self.change_y = 0

        if self.moving_left and not self.moving_right:
            self.change_x = -self.player_speed
        elif self.moving_right and not self.moving_left:
            self.change_x = self.player_speed
        else:
            self.change_x = 0
        
        # update horiziontal movement
        self.center_x += self.change_x

        # if there are horizontal collisions, move player back
        if arcade.check_for_collision_with_list(self, walls):
            self.center_x -= self.change_x

        # update vertical movement
        self.center_y += self.change_y

        # if there are vertical collisions, move player back
        if arcade.check_for_collision_with_list(self, walls):
            self.center_y -= self.change_y
