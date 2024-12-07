import pytest
from globals.database import LeaderboardDB
import sqlite3

@pytest.fixture
def db():
    """Fixture to set up and tear down a fresh database for each test."""
    database = LeaderboardDB()
    database.cursor.execute("DELETE FROM users")  # Clear the users table
    database.cursor.execute("DELETE FROM scores")  # Clear the scores table
    database.connection.commit()
    yield database
    database.close()

# Test cases for `save_score`
def test_save_score_general_case(db):
    """Test saving a score for a user."""
    db.save_score(level=1, username="test_user", score=123.456)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("test_user", 123.456) in leaderboard

def test_save_score_edge_case(db):
    """Test saving a score with zero."""
    db.save_score(level=1, username="edge_user", score=0.0)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("edge_user", 0.0) in leaderboard

# Test cases for `fetch_leaderboard`
def test_fetch_leaderboard_general_case(db):
    """Test fetching the top 5 scores."""
    for i in range(1, 6):
        db.save_score(level=1, username=f"user_{i}", score=100 + i)
    leaderboard = db.fetch_leaderboard(level=1)
    expected_leaderboard = [
        ("user_1", 101.0),
        ("user_2", 102.0),
        ("user_3", 103.0),
        ("user_4", 104.0),
        ("user_5", 105.0),
    ]
    assert leaderboard == expected_leaderboard

def test_fetch_leaderboard_user_outside_top_5(db):
    """Test fetching a user's score if they're outside the top 5."""
    for i in range(1, 7):
        db.save_score(level=1, username=f"user_{i}", score=100 + i)
    leaderboard = db.fetch_leaderboard(level=1, username="user_1")
    assert ("user_1", 101.0) in leaderboard

# Test cases for `delete_score`
def test_delete_specific_score_general_case(db):
    """Test deleting a specific score for a user."""
    db.save_score(level=1, username="test_user", score=123.456)
    db.delete_score(level=1, username="test_user", score=123.456)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("test_user", 123.456) not in leaderboard

def test_delete_all_scores_for_user_edge_case(db):
    """Test deleting all scores for a user."""
    db.save_score(level=1, username="test_user", score=100.0)
    db.save_score(level=1, username="test_user", score=200.0)
    db.delete_score(level=1, username="test_user")
    leaderboard = db.fetch_leaderboard(level=1)
    assert not any(score[0] == "test_user" for score in leaderboard)

# Test cases for `check_user_exists`
def test_check_user_exists_general_case(db):
    """Test checking if an existing user exists."""
    db.save_score(level=1, username="test_user", score=100.0)
    assert db.check_user_exists("test_user")

def test_check_user_exists_edge_case(db):
    """Test checking if a non-existing user exists."""
    assert not db.check_user_exists("nonexistent_user")

# Test cases for user auto-creation
def test_user_auto_creation_general_case(db):
    """Test that a user is automatically created when saving a score."""
    username = "new_user"
    db.save_score(level=1, username=username, score=100.0)
    assert db.check_user_exists(username)

def test_user_auto_creation_edge_case(db):
    """Test that duplicate usernames are not created."""
    username = "duplicate_user"
    db.save_score(level=1, username=username, score=100.0)
    db.save_score(level=2, username=username, score=200.0)
    db.cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
    assert db.cursor.fetchone()[0] == 1

# Test cases for rounding scores
def test_rounding_scores_general_case(db):
    """Test rounding scores to three decimal places."""
    db.save_score(level=1, username="test_user", score=123.456789)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("test_user", 123.457) in leaderboard

def test_rounding_scores_edge_case(db):
    """Test rounding a score that is exactly at the boundary."""
    db.save_score(level=1, username="boundary_user", score=123.4500)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("boundary_user", 123.45) in leaderboard

# Test cases for closing the database connection
def test_close_connection_general_case(db):
    """Test closing the database connection."""
    db.close()
    with pytest.raises(sqlite3.ProgrammingError):
        db.cursor.execute("SELECT * FROM users")

