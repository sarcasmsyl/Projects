import sqlite3

def setup_database():
    conn = sqlite3.connect('DiscordBot/database/user_data.db')
    c = conn.cursor()

    # Create tables if they don't exist
    c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        user_id INTEGER PRIMARY KEY,
        data TEXT,
        PlayerLevel INT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS player_data (
        user_id INTEGER PRIMARY KEY,
        Class TEXT,
        HitPoints INT,
        Strength INT,
        Intelligence INT,
        Agility INT,
        Speed INT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS user_balances (
        user_id INTEGER PRIMARY KEY,
        balance INTEGER DEFAULT 0,
        last_daily TIMESTAMP
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS user_streaks (
        user_id INTEGER PRIMARY KEY,
        winning_streak INTEGER DEFAULT 0,
        streak_bonus INTEGER DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()