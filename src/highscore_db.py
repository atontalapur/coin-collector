import sqlite3
import random
from faker import Faker

fake = Faker()

# Connect to the SQLite database
conn = sqlite3.connect('game_scores.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_name TEXT NOT NULL,
        level INTEGER NOT NULL,
        score INTEGER NOT NULL
    )
''')
conn.commit()

def insert_score(player_name, level, score):
    cursor.execute('''
        INSERT INTO scores (player_name, level, score)
        VALUES (?, ?, ?)
    ''', (player_name, level, score))
    conn.commit()

def get_high_scores():
    cursor.execute('''
        SELECT level, player_name, MAX(score) as high_score
        FROM scores
        GROUP BY level
        ORDER BY level ASC
    ''')
    return cursor.fetchall()

def generate_fake_scores(num_players, num_levels, scores_per_player_per_level):
    players = [fake.name() for _ in range(num_players)]
    for player_name in players:
        for level in range(1, num_levels + 1):
            for _ in range(scores_per_player_per_level):
                score = random.randint(1000, 5000)
                insert_score(player_name, level, score)

# Generate fake data
generate_fake_scores(num_players=10, num_levels=5, scores_per_player_per_level=3)

# Retrieve and print high scores
high_scores = get_high_scores()
for level, player_name, high_score in high_scores:
    print(f'Level {level}: {player_name} has the high score of {high_score}')

# Close the connection
cursor.close()
conn.close()

