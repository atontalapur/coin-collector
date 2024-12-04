import arcade
from random import randint, uniform
from game.coin import Coin
from game.obstacle import Obstacle
from game.player import Player
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, LEVEL_SETTINGS

import globals.music_player as music_player

class Level:
    """Class to represent the Level containing obstacles, coins, and the player."""
    def __init__(self, level):
        """Initialize the level. Goes into setup."""
        self.level = level

        self.level_settings = LEVEL_SETTINGS[self.level]
        self.coin_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()
        self.player = None

        self._setup_background()
        self._setup_sounds()
        self._setup_walls()

        self.setup()

    def setup(self):
        """Setup settings and all visible game parts. Allows Level to easilt restart."""
        self.coin_list.clear()
        self.player = None

        self._setup_coins()
        self._setup_player()
    
    def _setup_background(self):
        """Set background color."""
        background_color = self.level_settings["BACKGROUND_COLOR"]
        arcade.set_background_color(background_color)
    
    def _setup_sounds(self):
        """Set level sounds."""
        if music_player.player:
            arcade.stop_sound(music_player.player)

        music_player.music = self.level_settings['BACKGROUND_MUSIC']
        music = arcade.load_sound(f"sounds/{music_player.music}")
        music_player.player = music.play(loop=True)

        self.coin_sound = arcade.load_sound("sounds/coin.wav")

    def _setup_walls(self):
        """Create obstacles in a set order and add to sprite list."""
        obstacle_scaling = self.level_settings["OBSTACLE_SCALING"]
        obstacle_image = self.level_settings["OBSTACLE_IMAGE"]
        obstacle_width = int(self.level_settings["OBSTACLE_PIXELS_X"] * obstacle_scaling)
        obstacle_height = int(self.level_settings["OBSTACLE_PIXELS_Y"] * obstacle_scaling)

        if (self.level == "level_1"):
            # precomputed values
            half_obstacle_width = obstacle_width // 2
            half_obstacle_height = obstacle_height // 2
            width_from_border = obstacle_width * 2 + half_obstacle_width
            height_from_border = obstacle_height * 2 + half_obstacle_height
            width_step = int(obstacle_width * 2.1429)
            height_step = int(obstacle_height * 2.5)

            # obstacles on top and bottom
            for x in range(half_obstacle_width, SCREEN_WIDTH, obstacle_width):
                self.obstacle_list.append(Obstacle(x, half_obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(x, SCREEN_HEIGHT - half_obstacle_height, obstacle_image, obstacle_scaling))

            # obstacles on left and right
            for y in range(half_obstacle_height + obstacle_height, SCREEN_HEIGHT, obstacle_height):
                self.obstacle_list.append(Obstacle(half_obstacle_width, y, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - half_obstacle_width, y, obstacle_image, obstacle_scaling))

            # obstacles in the middle
            counter = 0
            for x in range(width_from_border, SCREEN_WIDTH - width_from_border + 1, width_step):
                if (counter == 2):
                    for y in range(height_from_border, SCREEN_HEIGHT - height_from_border + 1, obstacle_height):
                        self.obstacle_list.append(Obstacle(x, y, obstacle_image, obstacle_scaling))
                    counter = 0
                else:
                    for y in range(height_from_border, SCREEN_HEIGHT - height_from_border + 1, height_step):
                        self.obstacle_list.append(Obstacle(x, y, obstacle_image, obstacle_scaling))
                    counter += 1
        
        elif (self.level == "level_2"):
            obstacle_image_2 = self.level_settings["OBSTACLE_IMAGE_2"]
            obstacle_image_3 = self.level_settings["OBSTACLE_IMAGE_3"]
            obstacle_image_4 = self.level_settings["OBSTACLE_IMAGE_4"]

            # precomputed values
            half_obstacle_width = obstacle_width // 2
            half_obstacle_height = obstacle_height // 2
            width_from_border = obstacle_width * 2 + half_obstacle_width
            height_from_border = obstacle_height * 2 + half_obstacle_height

            # obstacles on top and bottom
            for x in range(half_obstacle_width, SCREEN_WIDTH, obstacle_width):
                self.obstacle_list.append(Obstacle(x, half_obstacle_height, obstacle_image_2, obstacle_scaling))
                self.obstacle_list.append(Obstacle(x, SCREEN_HEIGHT - half_obstacle_height, obstacle_image_2, obstacle_scaling))

            # obstacles on left and right
            for y in range(half_obstacle_height + obstacle_height, SCREEN_HEIGHT, obstacle_height):
                self.obstacle_list.append(Obstacle(half_obstacle_width, y, obstacle_image_3, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - half_obstacle_width, y, obstacle_image_4, obstacle_scaling))
            
            for i in range(0, 6):
                self.obstacle_list.append(Obstacle(width_from_border + 64 + i * obstacle_width, SCREEN_HEIGHT - height_from_border, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 64 + i * obstacle_width, height_from_border, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 576 + i * obstacle_width, SCREEN_HEIGHT - height_from_border, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 576 + i * obstacle_width, height_from_border, obstacle_image, obstacle_scaling))
            
            for i in range(0, 4):
                self.obstacle_list.append(Obstacle(width_from_border + 64, height_from_border + 64 + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - width_from_border - 64, height_from_border + 64 + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 192 + i * obstacle_width, height_from_border + 192, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 576 + i * obstacle_width, height_from_border + 192, obstacle_image, obstacle_scaling))
            
            for i in range(0, 2):
                self.obstacle_list.append(Obstacle(width_from_border + 448 + i * obstacle_width, height_from_border + 128,obstacle_image, obstacle_scaling))


        elif (self.level == "level_3"):
            obstacle_image_2 = self.level_settings["OBSTACLE_IMAGE_2"]
            obstacle_image_3 = self.level_settings["OBSTACLE_IMAGE_3"]
            obstacle_image_4 = self.level_settings["OBSTACLE_IMAGE_4"]

            # precomputed values
            half_obstacle_width = obstacle_width // 2
            half_obstacle_height = obstacle_height // 2
            width_from_border = obstacle_width * 2 + half_obstacle_width
            height_from_border = obstacle_height * 2 + half_obstacle_height

            # obstacles on top and bottom
            for x in range(half_obstacle_width, SCREEN_WIDTH, obstacle_width):
                self.obstacle_list.append(Obstacle(x, half_obstacle_height, obstacle_image_2, obstacle_scaling))
                self.obstacle_list.append(Obstacle(x, SCREEN_HEIGHT - half_obstacle_height, obstacle_image_2, obstacle_scaling))

            # obstacles on left and right
            for y in range(half_obstacle_height + obstacle_height, SCREEN_HEIGHT, obstacle_height):
                self.obstacle_list.append(Obstacle(half_obstacle_width, y, obstacle_image_3, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - half_obstacle_width, y, obstacle_image_4, obstacle_scaling))
            
            # left/right large diagonal patterns
            for i in range(0, 5):
                self.obstacle_list.append(Obstacle(width_from_border + i * obstacle_width, height_from_border + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - width_from_border - i * obstacle_width, height_from_border + i * obstacle_height, obstacle_image, obstacle_scaling))
            
            # middle diagonal patterns
            for i in range(0, 3):
                self.obstacle_list.append(Obstacle(width_from_border + 320 + i * obstacle_width, height_from_border + 64 + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 512 + i * obstacle_width, height_from_border + 192 - i * obstacle_height, obstacle_image, obstacle_scaling))
            
            # top pattern
            for i in range(0, 2):
                 self.obstacle_list.append(Obstacle(width_from_border + 448 + i * obstacle_width, height_from_border + 320, obstacle_image, obstacle_scaling))

        elif (self.level == "level_4"):
            obstacle_image_2 = self.level_settings["OBSTACLE_IMAGE_2"]
            obstacle_image_3 = self.level_settings["OBSTACLE_IMAGE_3"]
            obstacle_image_4 = self.level_settings["OBSTACLE_IMAGE_4"]

            # precomputed values
            half_obstacle_width = obstacle_width // 2
            half_obstacle_height = obstacle_height // 2
            width_from_border = obstacle_width * 2 + half_obstacle_width
            height_from_border = obstacle_height * 2 + half_obstacle_height
            
            # obstacles on top and bottom
            for x in range(half_obstacle_width + obstacle_width, SCREEN_WIDTH - obstacle_width, obstacle_width):
                self.obstacle_list.append(Obstacle(x, half_obstacle_height, obstacle_image_3, obstacle_scaling))
                self.obstacle_list.append(Obstacle(x, SCREEN_HEIGHT - half_obstacle_height, obstacle_image_4, obstacle_scaling))

            # obstacles on left and right
            for y in range(half_obstacle_height, SCREEN_HEIGHT, obstacle_height):
                self.obstacle_list.append(Obstacle(half_obstacle_width, y, obstacle_image_2, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - half_obstacle_width, y, obstacle_image_2, obstacle_scaling))
            
            # obstacles near edges
            for i in range(0, 3):
                self.obstacle_list.append(Obstacle(width_from_border + i * obstacle_width, height_from_border + 192 + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - width_from_border - 128 + i * obstacle_width, height_from_border + i * obstacle_height, obstacle_image, obstacle_scaling))
            
            # obstacles near middle
            for i in range(0, 6):
                self.obstacle_list.append(Obstacle(width_from_border + 64 + i * obstacle_width, height_from_border + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 320 + i * obstacle_width, height_from_border + i * obstacle_height, obstacle_image, obstacle_scaling))
                self.obstacle_list.append(Obstacle(width_from_border + 576 + i * obstacle_width, height_from_border + i * obstacle_height, obstacle_image, obstacle_scaling))
        
        elif (self.level == "level_5"):
            obstacle_image_2 = self.level_settings["OBSTACLE_IMAGE_2"]
            obstacle_image_3 = self.level_settings["OBSTACLE_IMAGE_3"]
            obstacle_image_4 = self.level_settings["OBSTACLE_IMAGE_4"]

            # precomputed values
            half_obstacle_width = obstacle_width // 2
            half_obstacle_height = obstacle_height // 2
            
            # obstacles on top and bottom
            for x in range(half_obstacle_width + obstacle_width, SCREEN_WIDTH - obstacle_width, obstacle_width):
                self.obstacle_list.append(Obstacle(x, half_obstacle_height, obstacle_image_3, obstacle_scaling))
                self.obstacle_list.append(Obstacle(x, SCREEN_HEIGHT - half_obstacle_height, obstacle_image_4, obstacle_scaling))

            # obstacles on left and right
            for y in range(half_obstacle_height, SCREEN_HEIGHT, obstacle_height):
                self.obstacle_list.append(Obstacle(half_obstacle_width, y, obstacle_image_2, obstacle_scaling))
                self.obstacle_list.append(Obstacle(SCREEN_WIDTH - half_obstacle_width, y, obstacle_image_2, obstacle_scaling))

            obstacle_positions = [
                (6, 1), (12, 1),
                (2, 2), (6, 2), (10, 2), (11, 2), (16, 2),
                (3, 3), (7, 3), (15, 3),
                (13, 4),
                (4, 5), (8, 5), (9, 5), (11, 5), (17, 5),
                (2, 6), (4, 6), (7, 6), (8, 6), (11, 6), (15, 6), (18, 6),
                (4, 7), (9, 7),
                (5, 8), (10, 8), (13, 8),
            ]

            # obstacles from grid positions
            for x_pos, y_pos in obstacle_positions:
                self.obstacle_list.append(Obstacle(x_pos * obstacle_width + 32, y_pos * obstacle_height + 32, obstacle_image, obstacle_scaling))


    def _setup_coins(self):
        """Create coins in random locations and add to sprite list."""
        coin_image = self.level_settings["COIN_IMAGE"]
        coin_scaling = self.level_settings["COIN_SCALING"]
        num_coins = self.level_settings["NUM_COINS"]
        coin_offset = self.level_settings["COIN_OFFSET"]
        coin_from_border = self.level_settings["COIN_FROM_BORDER"]
        coin_min_speed = self.level_settings["COIN_MIN_SPEED"]
        coin_max_speed = self.level_settings["COIN_MAX_SPEED"]
        player_spawn_x = self.level_settings["PLAYER_SPAWN_X"]
        player_spawn_y = self.level_settings["PLAYER_SPAWN_Y"]

        for _ in range(num_coins):
            while True:
                x = randint(coin_from_border, SCREEN_WIDTH - coin_from_border)
                if not (player_spawn_x - coin_offset <= x <= player_spawn_x + coin_offset):
                    break
            while True:
                y = randint(coin_from_border, SCREEN_HEIGHT - coin_from_border)
                if not (player_spawn_y - coin_offset <= y <= player_spawn_y + coin_offset):
                    break

            while True:
                change_x = uniform(-coin_max_speed, coin_max_speed)
                if abs(change_x) >= coin_min_speed:
                    break

            while True:
                change_y = uniform(-coin_max_speed, coin_max_speed)
                if abs(change_y) >= coin_min_speed:
                    break
            
            self.coin_list.append(Coin(x, y, change_x, change_y, coin_image, coin_scaling))

    def _setup_player(self):
        """Create the player in the center."""
        player_image = self.level_settings["PLAYER_IMAGE"]
        player_scaling = self.level_settings["PLAYER_SCALING"]
        player_spawn_x = self.level_settings["PLAYER_SPAWN_X"]
        player_spawn_y = self.level_settings["PLAYER_SPAWN_Y"]
        player_speed = self.level_settings["PLAYER_SPEED"]
    
        self.player = Player(player_spawn_x, player_spawn_y, player_speed, player_image, player_scaling)

    def update(self):
        """Update sprites in the Level."""

        # update coin movement (covers repositioning + bounce)
        for coin in self.coin_list:
            coin.update(self.obstacle_list)

        # update player movement (covers repositioning)
        self.player.update(self.obstacle_list)

        self._update_collect()

    def _update_collect(self):
        """Remove coins if the player collected them."""
        coins_collected = arcade.check_for_collision_with_list(self.player, self.coin_list)

        for coin in coins_collected:
            coin.remove_from_sprite_lists()
            self.coin_sound.play(loop=False)

    def draw(self):
        """Render game Level."""
        self.obstacle_list.draw()
        self.coin_list.draw()
        self.player.draw()
