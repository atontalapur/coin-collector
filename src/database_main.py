import sqlite3

class LeaderboardDB:
    def __init__(self):
        # Initialize the database connection
        self.connection = sqlite3.connect("leaderboard.db")
        self.cursor = self.connection.cursor()
        self._setup_tables()

    def _setup_tables(self):
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

    def check_user_exists(self, username):
        """Check if a user exists in the database."""
        self.cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()[0] > 0

    def fetch_leaderboard(self, level, username=None):
        """
        Fetch the top 5 scores for a level.
        If the user is not in the top 5, fetch their best score.
        Return explicit format: [(level: int, username: str, score: float)].
        """
        # Get top 5 scores
        self.cursor.execute("""
        SELECT s.level, u.username, s.score 
        FROM scores s
        JOIN users u ON s.user_id = u.id
        WHERE s.level = ?
        ORDER BY s.score DESC
        LIMIT 5
        """, (level,))
        top_scores = self.cursor.fetchall()

        # Check if the user needs to be added separately
        if username and username not in [row[1] for row in top_scores]:
            self.cursor.execute("""
            SELECT s.level, u.username, MAX(s.score)
            FROM scores s
            JOIN users u ON s.user_id = u.id
            WHERE s.level = ? AND u.username = ?
            GROUP BY s.level, u.username
            """, (level, username))
            user_score = self.cursor.fetchone()
            if user_score:
                top_scores.append(user_score)

        return top_scores

    def save_score(self, level, username, score):
        """
        Save a score for a user in a specific level.
        Round scores to a thousandth of a second (3 decimal places).
        Clean up scores that are not in the top 5 or the user's high score.
        """
        # Ensure the user exists
        self.cursor.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
        self.connection.commit()

        # Get the user's ID
        self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_id = self.cursor.fetchone()[0]

        # Round the score to 3 decimal places
        rounded_score = round(score, 3)

        # Save the rounded score
        self.cursor.execute("INSERT INTO scores (user_id, level, score) VALUES (?, ?, ?)", (user_id, level, rounded_score))
        self.connection.commit()

        # Clean up non-top-5 and non-high scores
        self.cursor.execute("""
        DELETE FROM scores 
        WHERE id NOT IN (
            SELECT id FROM (
                SELECT s.id
                FROM scores s
                JOIN users u ON s.user_id = u.id
                WHERE s.level = ?
                ORDER BY s.score DESC
                LIMIT 5
            )
        )
        AND id NOT IN (
            SELECT id FROM (
                SELECT s.id
                FROM scores s
                JOIN users u ON s.user_id = u.id
                WHERE u.username = ? AND s.level = ?
                ORDER BY s.score DESC
                LIMIT 1
            )
        )
        """, (level, username, level))
        self.connection.commit()

    def delete_score(self, level, username, score=None):
        """
        Delete a specific score for a user in a given level.
        If no score is provided, delete all scores for the user in that level.

        Args:
            level (int): The level associated with the score.
            username (str): The username of the player.
            score (float, optional): The specific score to delete. If not provided, all scores for the user in the level are deleted.
        """
        # Ensure the user exists
        self.cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user_row = self.cursor.fetchone()
        if not user_row:
            print(f"User '{username}' does not exist.")
            return

        user_id = user_row[0]

        if score is not None:
            # Delete a specific score
            self.cursor.execute("""
            DELETE FROM scores 
            WHERE user_id = ? AND level = ? AND score = ?
            """, (user_id, level, score))
        else:
            # Delete all scores for the user in this level
            self.cursor.execute("""
            DELETE FROM scores 
            WHERE user_id = ? AND level = ?
            """, (user_id, level))
        
        self.connection.commit()
        print(f"Score(s) deleted for user '{username}' in level {level}.")

    def close(self):
        """Close the database connection."""
        self.connection.close()


# instance similar to Controller
leaderboard = LeaderboardDB()
