import arcade

class Obstacle(arcade.Sprite):
    """Class to represent obstacles. They do not move."""
    def __init__(self, x, y, image, scale=1):
        """Initialize the obstacle."""
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
