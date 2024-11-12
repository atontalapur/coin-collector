from environment import Environment

class Level:
    """Class to represent a level in the game."""
    def __init__(self):
        self.environment = Environment()

    def setup(self):
        """Set up the level's environment."""
        self.environment.setup_walls()
        self.environment.setup_coins()
        self.environment.setup_player()

    def update(self):
        """Update the environment's contents."""
        self.environment.update()
