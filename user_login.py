
"""
This module is called by `main.py` for user login.
"""

import hashlib

def login_user(c, username, password):
    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        stored_password = c.fetchone()
        if stored_password and stored_password[0] == hashed_password:
            return True, "Logged in successfully"
        else:
            return False, "Invalid username or password"
    except sqlite3.Error as e:
        return False, f"An error occurred: {e}"
