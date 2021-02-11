import sqlite3

def all_trains():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trains')
    rows = cursor.fetchall()
    conn.close()
    return rows