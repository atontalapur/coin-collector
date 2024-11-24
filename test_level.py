import pytest
from level import Level

def test_level_initialization_level_1():
    level = Level("level_1")
    assert level.environment is not None

def test_level_setup_level_1():
    level = Level("level_1")
    level.setup()
    assert len(level.environment.coin_list) > 0

def test_level_initialization_level_2():
    level = Level("level_2")
    assert level.environment is not None

def test_level_setup_level_2():
    level = Level("level_2")
    level.setup()
    assert len(level.environment.coin_list) > 0

def test_level_initialization_level_3():
    level = Level("level_3")
    assert level.environment is not None

def test_level_setup_level_3():
    level = Level("level_3")
    level.setup()
    assert len(level.environment.coin_list) > 0

def test_level_initialization_level_4():
    level = Level("level_4")
    assert level.environment is not None

def test_level_setup_level_4():
    level = Level("level_4")
    level.setup()
    assert len(level.environment.coin_list) > 0

def test_level_initialization_level_5():
    level = Level("level_5")
    assert level.environment is not None

def test_level_setup_level_5():
    level = Level("level_5")
    level.setup()
    assert len(level.environment.coin_list) > 0

