from prettytable import PrettyTable

table = PrettyTable()

def all_book(conn,cursor):

    uid = 'kash'
    #cursor.execute("select * from trains limit 1")
    #table.field_names = [col[0] for col in cursor.description]
    table.field_names=['Booking id','Train id','Booked tickets','Source','Destination','Type','Date']

    cursor.execute('SELECT book_id,trains.train_id,num_booked,source,destination,type,date FROM booking,trains where trains.train_id = booking.train_id and booking.uid=\'{uid}\''.format(uid=uid))
    rows = cursor.fetchall()
    table.add_rows(rows)
    print(table)
    table.clear()