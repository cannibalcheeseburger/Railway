def Avail(cursor):
    cursor.execute('SELECT * FROM trains')
    rows = cursor.fetchall()
    for row in rows:
        print("*******************")
        print('Train id: ',row[0])
        print('Source: ',row[1])
        print('Destination: ',row[2])
        print('Available Seats: ',row[3]-row[4])
        print('Type: ',row[5])
        print('Cost: ',row[6])
