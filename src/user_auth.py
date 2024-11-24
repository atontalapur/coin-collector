import sqlite3
from faker import Faker
import random

# Initialize the Faker library
fake = Faker()

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('game.db')
cursor = conn.cursor()

# Create the Users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL
);
''')

# Create the Scores table with a UNIQUE constraint on (user_id, level)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    level INTEGER NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES Users(id),
    UNIQUE(user_id, level)
);
''')

conn.commit()

# Function to register a new user
def register_user(username):
    try:
        cursor.execute('INSERT INTO Users (username) VALUES (?)', (username,))
        conn.commit()
        print(f"User '{username}' registered successfully.")
    except sqlite3.IntegrityError:
        print(f"Username '{username}' is already taken.")

# Function to get a user ID from the username
def get_user_id(username):
    cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    return result[0] if result else None

# Function to save or update a user's high score
def save_high_score(username, level, score):
    user_id = get_user_id(username)
    if user_id is None:
        print(f"User '{username}' does not exist.")
        return
    cursor.execute('''
        INSERT INTO Scores (user_id, level, score)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, level) DO UPDATE SET
          score = CASE WHEN EXCLUDED.score > score THEN EXCLUDED.score ELSE score END;
    ''', (user_id, level, score))
    conn.commit()
    print(f"High score of {score} saved for user '{username}' on level {level}.")

# Function to load the leaderboard for a specific level
def load_leaderboard(level, username=None):
    user_id = get_user_id(username) if username else None
    cursor.execute('''
        WITH RankedScores AS (
            SELECT s.user_id, u.username, s.score AS highscore,
                   RANK() OVER (ORDER BY s.score DESC) AS rank
            FROM Scores s
            JOIN Users u ON s.user_id = u.id
            WHERE s.level = ?
        )
        SELECT username, highscore, rank
        FROM (
            SELECT username, highscore, rank FROM RankedScores WHERE rank <= 5
            UNION ALL
            SELECT username, highscore, rank FROM RankedScores WHERE user_id = ? AND rank > 5
        )
        ORDER BY rank;
    ''', (level, user_id))
    results = cursor.fetchall()
    return results  # Return the leaderboard data for further processing

# Function to generate fake users and scores
def generate_fake_data(num_users=10, levels=5):
    for _ in range(num_users):
        username = fake.user_name()
        register_user(username)
        for level in range(1, levels + 1):
            score = random.randint(0, 1000)  # Adjust the score range as needed
            save_high_score(username, level, score)

# Remember to close the database connection when done
def close_connection():
    conn.close()

# Example usage
if __name__ == "__main__":
    # Generate fake data
    generate_fake_data(num_users=20, levels=5)

    # Load the leaderboard for Level 1
    leaderboard = load_leaderboard(level=1)
    print("\nLeaderboard for Level 1:")
    for entry in leaderboard:
        print(f"Rank {entry[2]}: {entry[0]} with {entry[1]} points")

    # Close the database connection
    close_connection()


