
"""
This module is called by `main.py` for data retrieval.
"""

def retrieve_data(c, username):
    try:
        c.execute("SELECT stored_data FROM data WHERE username = ?", (username,))
        data = c.fetchall()
        if data:
            return True, data
        else:
            return False, "No data found"
    except sqlite3.Error as e:
        return False, f"An error occurred: {e}"
