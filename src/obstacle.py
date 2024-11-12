import arcade

class Obstacle(arcade.Sprite):
    """Class to represent obstacles (walls)."""
    def __init__(self, image, scale, c_x, c_y):
        super().__init__(image, scale)
        self.center_x = c_x
        self.center_y = c_y
