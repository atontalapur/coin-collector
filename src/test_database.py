import pytest
from globals.database import LeaderboardDB
import sqlite3

@pytest.fixture
def db():
    """Fixture to set up and tear down a fresh database for each test."""
    database = LeaderboardDB()
    database.cursor.execute("DELETE FROM users")  
    database.cursor.execute("DELETE FROM scores")  
    database.connection.commit()
    yield database
    database.close()

def test_user_creation_and_existence(db):
    """Test user creation and existence check."""
    db.save_score(level=1, username="test_user", score=100.0)
    assert db.check_user_exists("test_user")
    assert not db.check_user_exists("nonexistent_user")

def test_save_and_fetch_score(db):
    """Test saving and fetching scores."""
    db.save_score(level=1, username="test_user", score=123.456)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("test_user", 123.456) in leaderboard

def test_rounding_scores(db):
    """Test that scores are rounded to three decimal places."""
    db.save_score(level=1, username="test_user", score=123.456789)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("test_user", 123.457) in leaderboard

def test_fetch_top_5_scores(db):
    """Test fetching the top 5 scores."""
    for i in range(1, 7):
        db.save_score(level=1, username=f"user_{i}", score=100 + i)
    leaderboard = db.fetch_leaderboard(level=1)

    assert len(leaderboard) == 5
    expected_leaderboard = [
        ("user_6", 106.0),
        ("user_5", 105.0),
        ("user_4", 104.0),
        ("user_3", 103.0),
        ("user_2", 102.0),
    ]
    assert leaderboard == expected_leaderboard

def test_fetch_user_outside_top_5(db):
    """Test fetching a user's score if they're outside the top 5."""
    for i in range(1, 7):
        db.save_score(level=1, username=f"user_{i}", score=100 + i)
    leaderboard = db.fetch_leaderboard(level=1, username="user_1")
    assert ("user_1", 101.0) in leaderboard

def test_delete_specific_score(db):
    """Test deleting a specific score for a user."""
    db.save_score(level=1, username="test_user", score=123.456)
    db.delete_score(level=1, username="test_user", score=123.456)
    leaderboard = db.fetch_leaderboard(level=1)
    assert ("test_user", 123.456) not in leaderboard

def test_delete_all_scores_for_user(db):
    """Test deleting all scores for a user in a level."""
    db.save_score(level=1, username="test_user", score=100.0)
    db.save_score(level=1, username="test_user", score=200.0)
    db.delete_score(level=1, username="test_user")
    leaderboard = db.fetch_leaderboard(level=1)
    assert not any(score[0] == "test_user" for score in leaderboard)

def test_no_duplicate_usernames(db):
    """Test that usernames are unique."""
    db.save_score(level=1, username="test_user", score=123.456)
    db.save_score(level=2, username="test_user", score=200.0)
    db.cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'test_user'")
    assert db.cursor.fetchone()[0] == 1

def test_user_auto_creation(db):
    """Test that a user is automatically created when saving a score."""
    username = "new_user"
    assert not db.check_user_exists(username)  

    
    db.save_score(level=1, username=username, score=100.0)

   
    assert db.check_user_exists(username)

    
    leaderboard = db.fetch_leaderboard(level=1)
    assert (username, 100.0) in leaderboard

def test_close_connection(db):
    """Test closing the database connection."""
    db.close()
    with pytest.raises(sqlite3.ProgrammingError):
        db.cursor.execute("SELECT * FROM users")
