from environment import Environment

class Level:
    """Class to represent a level in the game. Includes environment and leaderboard."""
    def __init__(self, level):
        """Initialize level."""
        self.environment = Environment(level)
    
    def setup(self):
        """Reset environment."""
        self.environment.setup()
    
    def draw(self):
        """Only draw, as leaderboard will not update during game."""
        self.environment.draw()

