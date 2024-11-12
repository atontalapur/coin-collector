import arcade
import random
from coin import Coin
from obstacle import Obstacle
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPRITE_SCALING, NUM_COINS

class Environment:
    """Class to represent the environment containing coins and obstacles."""
    def __init__(self):
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def setup_walls(self):
        """Set up the obstacles (walls) around the screen."""
        # obstacles on bottom and top
        for x in range(32, SCREEN_WIDTH, 64):
            wall = Obstacle(":resources:images/tiles/grass.png", SPRITE_SCALING, x, 32)
            self.wall_list.append(wall)

            wall = Obstacle(":resources:images/tiles/grass.png", SPRITE_SCALING, x, SCREEN_HEIGHT - 32)
            self.wall_list.append(wall)
        
        # obstacles on left and right
        for y in range(96, SCREEN_HEIGHT, 64):
            wall = Obstacle(":resources:images/tiles/grass.png", SPRITE_SCALING, 32, y)
            self.wall_list.append(wall)

            wall = Obstacle(":resources:images/tiles/grass.png", SPRITE_SCALING, SCREEN_WIDTH - 32, y)
            self.wall_list.append(wall)

        # obstacles in middle
        for x in range(128, SCREEN_WIDTH, 196):
            for y in range(128, SCREEN_HEIGHT, 196):
                wall = Obstacle(":resources:images/tiles/grass.png", SPRITE_SCALING, x, y)
                self.wall_list.append(wall)

    def setup_coins(self):
        """Create coins in random locations and add them to the coin list."""
        for _ in range(NUM_COINS):
            c_x = random.randrange(100, 700)
            c_y = random.randrange(100, 500)
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING / 2, c_x, c_y)
            self.coin_list.append(coin)
    
    def setup_player(self):
        """Set up the player in the center."""
        c_x = SCREEN_WIDTH // 2
        c_y = SCREEN_HEIGHT // 2
        self.player = Player(":resources:images/animated_characters/robot/robot_walk0.png", SPRITE_SCALING, c_x, c_y)

    def update(self):
        """Update the coins in the environment."""
        for coin in self.coin_list:
            coin.update(self.wall_list)
        
        self.player.update(self.wall_list)

        coins_collected = arcade.check_for_collision_with_list(self.player, self.coin_list)

        for coin in coins_collected:
            coin.remove_from_sprite_lists()

