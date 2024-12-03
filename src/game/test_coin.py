import pytest
import arcade
from coin import Coin
from obstacle import Obstacle

@pytest.fixture
def coin():
    """Fixture to create a Coin instance."""
    coin = Coin(x=100, y=100, change_x=5, change_y=0, image=":resources:images/items/coinGold.png", scale=1)
    return coin

@pytest.fixture
def walls():
    """Fixture to create walls for collision testing."""
    walls = arcade.SpriteList()
    wall1 = Obstacle(198, 100, ":resources:images/tiles/boxCrate_double.png", scale=1)
    walls.append(wall1)
    wall2 = Obstacle(101, 2, ":resources:images/tiles/boxCrate_double.png", scale=1)
    walls.append(wall2)
    return walls

def test_coin_initialization(coin):
    """Test coin is initialized with correct attributes."""
    assert coin.center_x == 100
    assert coin.center_y == 100
    assert coin.change_x == 5
    assert coin.change_y == 0

def test_coin_move_right(coin):
    """Test coin moves right when update is called."""
    coin.update(arcade.SpriteList())  # no walls
    assert coin.center_x == 105

def test_coin_collision_with_wall(coin, walls):
    """Test coin bounces off walls when moving right."""
    coin.update(walls)
    assert coin.change_x == -5  # Coin should reverse x velocity
    assert coin.center_x == 102  # Coin should stop at wall1

def test_coin_bounce_vertical(coin, walls):
    """Test coin bounces vertically when colliding with wall."""
    coin.change_y = -5
    coin.update(walls)
    assert coin.change_y == 5  # Coin should reverse y velocity
    assert coin.center_y == 98  # Coins should stop at wall2

def test_coin_no_speed_change_after_bounce(coin, walls):
    """Coin's speed stays the same after bouncing off wall."""
    initial_change_x = coin.change_x
    initial_change_y = coin.change_y
    coin.update(walls)
    assert coin.change_x == -initial_change_x  # Speed should stay the same in magnitude
    assert coin.change_y == -initial_change_y  # Speed should stay the same in magnitude
