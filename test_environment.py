import pytest
from environment import Environment
import arcade


def test_environment_initialization():
    environment = Environment("level_1")
    assert environment.level == "level_1"
    assert len(environment.coin_list) > 0
    assert len(environment.obstacle_list) > 0
    assert environment.player is not None


def test_environment_update():
    environment = Environment("level_1")
    initial_coin_count = len(environment.coin_list)
    environment.update()
    assert len(environment.coin_list) == initial_coin_count


def test_environment_collect():
    environment = Environment("level_1")
    initial_coin_count = len(environment.coin_list)
    environment.player.center_x = environment.coin_list[0].center_x
    environment.player.center_y = environment.coin_list[0].center_y
    environment.update()
    assert len(environment.coin_list) == initial_coin_count - 1
