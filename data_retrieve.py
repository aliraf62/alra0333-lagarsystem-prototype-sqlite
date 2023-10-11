from messages import messages as m
"""
This module is called by `main.py` for data retrieval.
"""    
def retrieve_data(c, username,lang):
    try:
        c.execute("SELECT stored_data FROM data WHERE username = ?", (username,))
        data = c.fetchall()
        if data:
            return True, data
        else:
            return False, m["r0"][lang]
    except sqlite3.Error as e:
        return False, m["error"][lang] +f"{e}"
