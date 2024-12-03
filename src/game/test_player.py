import pytest
import arcade
from player import Player
from obstacle import Obstacle

@pytest.fixture
def player():
    """Fixture to create a Player instance."""
    return Player(x=100, y=100, speed=5, image=":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png", scale=1)

@pytest.fixture
def walls():
    """Fixture to create walls."""
    walls = arcade.SpriteList()
    wall1 = Obstacle(198, 100, ":resources:images/tiles/boxCrate_double.png", scale=1)
    walls.append(wall1)
    wall2 = Obstacle(101, -30, ":resources:images/tiles/boxCrate_double.png", scale=1)
    walls.append(wall2)
    return walls

def test_player_initialization(player):
    """Test player is initialized correctly."""
    assert player.center_x == 100
    assert player.center_y == 100
    assert player.player_speed == 5

def test_player_move_up(player):
    """Test player moves up when up is pressed."""
    player.moving_up = True
    player.update(arcade.SpriteList())  # no walls
    assert player.center_y == 105

def test_player_move_down(player):
    """Test player moves down when down is pressed."""
    player.moving_down = True
    player.update(arcade.SpriteList())  # no walls
    assert player.center_y == 95

def test_player_move_left(player):
    """Test player moves left when left is pressed."""
    player.moving_left = True
    player.update(arcade.SpriteList())  # no walls
    assert player.center_x == 95

def test_player_move_right(player):
    """Test player moves right when right is pressed"""
    player.moving_right = True
    player.update(arcade.SpriteList())  # no walls
    assert player.center_x == 105

def test_player_collision_with_wall(player, walls):
    """Test player stops at walls when moving."""
    # Player moving right and colliding with wall1
    player.moving_right = True
    player.update(walls)
    assert player.center_x == 101  # Player should stop at wall1

    # Player moving down and colliding with wall2
    player.moving_down = True
    player.update(walls)
    assert player.center_y == 99  # Player should stop at wall2