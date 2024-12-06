import sqlite3
import globals.database_manager as database_manager
from typing import List, Optional, Tuple


class LeaderboardDB:
    def __init__(self) -> None:
        # Initialize the database connection
        self.connection = sqlite3.connect("leaderboard.db")
        self.cursor = self.connection.cursor()
        self._setup_tables()

    def _setup_tables(self) -> None:
        """Setup database tables for users and scores."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            level INTEGER NOT NULL,
            score FLOAT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """)
        self.connection.commit()

    def check_user_exists(self, username: str) -> bool:
        """Check if a user exists in the database."""
        self.cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()[0] > 0

    def fetch_leaderboard(self, level: int, username: Optional[str] = None) -> List[Tuple[str, float]]:
        """
        Fetch the top 5 scores for a level.
        If the user is not in the top 5, fetch their best score.
        """
        self.cursor.execute("""
        SELECT u.username, s.score 
        FROM scores s
        JOIN users u ON s.user_id = u.id
        WHERE s.level = ?
        ORDER BY s.score
        LIMIT 5
        """, (level,))
        top_scores = self.cursor.fetchall()

        if username and username not in [row[0] for row in top_scores]:
            self.cursor.execute("""
            SELECT u.username, MAX(s.score)
            FROM scores s
            JOIN users u ON s.user_id = u.id
            WHERE s.level = ? AND u.username = ?
            GROUP BY u.username
            """, (level, username))
            user_score = self.cursor.fetchone()
            if user_score:
                top_scores.append(user_score)

        return top_scores

    def save_score(self, level: int, username: str, score: float) -> None:
        """
        Save a score for a user in a specific level.
        Round scores to a thousandth of a second (3 decimal places).
        """
        self.cursor.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
        self.connection.commit()

        self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_id = self.cursor.fetchone()[0]

        rounded_score = round(score, 3)

        self.cursor.execute("INSERT INTO scores (user_id, level, score) VALUES (?, ?, ?)", (user_id, level, rounded_score))
        self.connection.commit()

    def delete_score(self, level: int, username: str, score: Optional[float] = None) -> None:
        """Delete a specific score or all scores for a user in a level."""
        self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_row = self.cursor.fetchone()
        if not user_row:
            print(f"User '{username}' does not exist.")
            return

        user_id = user_row[0]

        if score is not None:
            self.cursor.execute("""
            DELETE FROM scores 
            WHERE user_id = ? AND level = ? AND score = ?
            """, (user_id, level, score))
        else:
            self.cursor.execute("""
            DELETE FROM scores 
            WHERE user_id = ? AND level = ?
            """, (user_id, level))
        
        self.connection.commit()

    def close(self) -> None:
        """Close the database connection."""
        self.connection.close()
