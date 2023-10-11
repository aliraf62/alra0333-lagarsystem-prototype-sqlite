
"""
This module is called by `main.py` to initialize the database.
"""

import sqlite3

def init_db():
    try:
        conn = sqlite3.connect('lagra_db.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL);")
        c.execute("CREATE TABLE IF NOT EXISTS data (username TEXT NOT NULL, stored_data TEXT NOT NULL, FOREIGN KEY (username) REFERENCES users (username));")
        conn.commit()
        return conn, c
    except sqlite3.Error as e:
        return None, f"An error occurred: {e}"
