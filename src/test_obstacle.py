import pytest
import arcade

# Assuming the class Obstacle is defined in a module called "game"
from game.obstacle import Obstacle  

@pytest.fixture
def obstacle():
    """Fixture to create an obstacle instance for tests."""
    return Obstacle(100, 200, ":resources:images/tiles/boxCrate_double.png", scale=1)

def test_obstacle_initialization(obstacle):
    """Test the initialization of the Obstacle class."""
    assert isinstance(obstacle, Obstacle)  # Check that the obstacle is an instance of Obstacle
    assert obstacle.center_x == 100  # Check if the x-coordinate is set correctly
    assert obstacle.center_y == 200  # Check if the y-coordinate is set correctly
    assert obstacle.texture is not None  # Check if the texture is properly loaded (i.e., the image)
    assert obstacle.scale == 1  # Check if the scale is set correctly
