import pytest
from obstacle import Obstacle

def test_obstacle_initialization():
    obstacle = Obstacle(100, 200, ":resources:images/tiles/boxCrate_double.png", 0.5)
    assert obstacle.center_x == 100
    assert obstacle.center_y == 200