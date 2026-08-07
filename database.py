import sqlite3


DATABASE = "talentlens.db"


def get_connection():

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():

    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            target_role TEXT NOT NULL,
            skills TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()


def save_candidate(name, email, target_role, skills):

    connection = get_connection()

    connection.execute("""
        INSERT INTO candidates (
            name,
            email,
            target_role,
            skills
        )
        VALUES (?, ?, ?, ?)
    """, (
        name,
        email,
        target_role,
        skills
    ))

    connection.commit()

    connection.close()