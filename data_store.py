
"""
This module is called by `main.py` for data storage.
"""

def store_data(conn, c, username, data):
    try:
        c.execute("INSERT INTO data (username, stored_data) VALUES (?, ?)", (username, data))
        conn.commit()
        return True, "Data stored successfully"
    except sqlite3.Error as e:
        return False, f"An error occurred: {e}"
