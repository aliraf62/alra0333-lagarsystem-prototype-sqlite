from messages import messages as m
"""
This module is called by `main.py` for data storage.
"""

def store_data(conn, c, username, data,lang):
    try:
        c.execute("INSERT INTO data (username, stored_data) VALUES (?, ?)", (username, data))
        conn.commit()
        return True, m["s0"][lang]
    except sqlite3.Error as e:
        return False, m["error"][lang] +f" {e}"
