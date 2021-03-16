import sqlite3

def Reg(user,passwd):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('INSERT into users values(\'{}\',\'{}\',0)'.format(user,passwd))
    conn.commit()

