import sqlite3
conn = sqlite3 . connect("urls.db")
cursor=conn.cursor()
cursor.execute(""" 
CREATE TABLE IF NOT EXISTS urls(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT,
    short_code TEXT
) 
""")
conn.commit()
##conn.close()

def save_url(original_url, short_code):
    cursor.execute("""
    INSERT INTO urls(original_url, short_code)
    VALUES(?, ?)
    """, (original_url, short_code))

    conn.commit()

##conn.close()