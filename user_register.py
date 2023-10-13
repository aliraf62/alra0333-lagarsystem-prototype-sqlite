from messages import messages as m
import sqlite3
"""
This module is called by `main.py` for user registration.
"""

import hashlib

def register_user(conn, c, username, password, lang):
    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True, m["reg"][lang] 
    except sqlite3.Error as e:
        return False, m["error"][lang] + f" {e}"
