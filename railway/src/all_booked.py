import sqlite3

def all_book():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    uid = 'kash'
    cursor.execute('SELECT book_id,trains.train_id,num_booked,source,destination,type,date FROM booking,trains where trains.train_id = booking.train_id and booking.uid=\'{uid}\''.format(uid=uid))
    rows = cursor.fetchall()
    conn.close()
    return rows