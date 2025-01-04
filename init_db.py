# init_db.py
import sqlite3


def initialize_db():
    conn = sqlite3.connect("ai_sports_betting.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY,
            date TEXT,
            home_team TEXT,
            away_team TEXT,
            home_score INTEGER,
            away_score INTEGER,
            home_team_form REAL,
            away_team_form REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            team TEXT,
            goals INTEGER,
            assists INTEGER,
            xG REAL
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized.")


if __name__ == "__main__":
    initialize_db()