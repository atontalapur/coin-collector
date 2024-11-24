import pytest
from coin import Coin
import arcade


def test_coin_initialization():
    coin = Coin(100, 200, 1, 1, ":resources:images/items/coinGold.png", 0.5)
    assert coin.center_x == 100
    assert coin.center_y == 200
    assert coin.change_x == 1
    assert coin.change_y == 1


def test_coin_update():
    coin = Coin(100, 200, 1, 1, ":resources:images/items/coinGold.png", 0.5)

    walls = arcade.SpriteList()
    wall_horizontal = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
    wall_horizontal.center_x = 110
    wall_horizontal.center_y = 200
    walls.append(wall_horizontal)
    wall_vertical = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", 0.5)
    wall_vertical.center_x = 100
    wall_vertical.center_y = 210
    walls.append(wall_vertical)

    coin.update(walls)

    assert coin.change_x == -1
    assert coin.center_x == 52

    assert coin.change_y == 1
    assert coin.center_y == 201
