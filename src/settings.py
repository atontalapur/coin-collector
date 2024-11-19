from arcade import color

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640
SCREEN_TITLE = "Sprite Bouncing Coins and Player"

LEVEL_SETTINGS = {
    "level_1": {
        "BACKGROUND_COLOR" : color.SAND,
        "OBSTACLE_IMAGE" : ":resources:images/tiles/boxCrate_double.png",
        "OBSTACLE_PIXELS_X" : 128,
        "OBSTACLE_PIXELS_Y" : 128,
        "OBSTACLE_SCALING" : 0.5,

        "COIN_IMAGE" : ":resources:images/items/coinGold.png",
        "COIN_SCALING" : 0.375,
        "NUM_COINS": 40,
        "COIN_OFFSET": 50,
        "COIN_FROM_BORDER": 100,
        "COIN_MIN_SPEED": 2,
        "COIN_MAX_SPEED": 4,

        "PLAYER_IMAGE" : ":resources:images/animated_characters/robot/robot_walk0.png",
        "PLAYER_SPAWN_X": SCREEN_WIDTH // 2,
        "PLAYER_SPAWN_Y": SCREEN_HEIGHT // 2,
        "PLAYER_SCALING" : 0.625,
        "PLAYER_SPEED": 6,
    },
}