import pytest
from coin import Coin
import arcade
from obstacle import Obstacle


def test_coin_initialization():
    coin = Coin(100, 200, 1, 1, ":resources:images/items/coinGold.png", 0.5)
    assert coin.center_x == 100
    assert coin.center_y == 200
    assert coin.change_x == 1
    assert coin.change_y == 1

def test_coin_update_no_walls():
    coin = Coin(100, 200, 1, 1, ":resources:images/items/coinGold.png", 0.5)
    walls=arcade.SpriteList()
    coin.update(walls)
    assert coin.center_x == 101
    assert coin.center_y == 201

def test_coin_update_with_walls():
    coin = Coin(100, 200, 1, 1, ":resources:images/items/coinGold.png", 0.5)
    walls=arcade.SpriteList()
    wall = Obstacle(110, 200, ":resources:images/tiles/boxCrate_double.png", 0.5)
    walls.append(wall)
    coin.update(walls)
    assert coin.change_x == -1
    assert coin.center_x == 62

def test_coin_update_with_multiple_walls():
    coin = Coin(100, 200, 1, 1, ":resources:images/items/coinGold.png", 0.5)
    walls=arcade.SpriteList()
    wall1 = Obstacle(110, 200, ":resources:images/tiles/boxCrate_double.png", 0.5)
    wall2 = Obstacle(90, 200, ":resources:images/tiles/boxCrate_double.png", 0.5)
    walls.append(wall1)
    walls.append(wall2)
    coin.update(walls)
    assert coin.change_x == -1
    assert coin.center_x == 42

def test_coin_update_no_movement():
    coin = Coin(100, 200, 0, 0, ":resources:images/items/coinGold.png", 0.5)
    walls=arcade.SpriteList()
    coin.update(walls)
    assert coin.center_x == 100
    assert coin.center_y == 200
