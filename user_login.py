from messages import messages as m
"""
This module is called by `main.py` for user login.
"""

import hashlib

def login_user(c, username, password, lang):
    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        stored_password = c.fetchone()
        if stored_password and stored_password[0] == hashed_password:
            return True, m["l0"][lang] 
        else:
            return False, m["l1"][lang]
    except sqlite3.Error as e:
        return False, m["error"][lang] + f" {e}"
