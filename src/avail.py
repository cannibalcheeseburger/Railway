import sqlite3

def Avail(day):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM trains where date=\''+ day+'\'')
    rows = cursor.fetchall()

    return rows