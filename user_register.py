
"""
This module is called by `main.py` for user registration.
"""

import hashlib

def register_user(conn, c, username, password):
    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True, "User registered successfully"
    except sqlite3.Error as e:
        return False, f"An error occurred: {e}"
