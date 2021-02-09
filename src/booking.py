from prettytable import PrettyTable

table = PrettyTable()

def book(conn,cursor):

    uid = 'kash'
    password = '123'

    cursor.execute("select * from trains limit 1")
    table.field_names = [col[0] for col in cursor.description]
    
    train_id = input("Enter train id: ")

    cursor.execute('SELECT * FROM trains where train_id='+train_id)
    row = cursor.fetchone()
    table.add_row(row)
    print(table)
    avail_seats = row[3]-row[4] 
    print("Total available seats: ",avail_seats)

    cursor.execute('SELECT balance FROM users where uid=\'{id}\' and pass = \'{password}\''.format(id=uid,password = password))

    balance = cursor.fetchone()[0]
    print("User Balance: ",balance)

    num =int(input("Enter number of seats to book: "))
    price = num*row[6]
    if num<= avail_seats:
        if  price<= balance:
            print("Booking seat please wait.....")
            cursor.execute('UPDATE users SET balance = {bal} WHERE uid=\'{id}\' and pass = \'{password}\''.format(bal = balance-price,id=uid,password = password))
            conn.commit()
        else:
            print("Insufficient balance")
    else:
        print("\nOnly "+str(avail_seats)+' Seats are available')

    print("Remaining Balance: ",balance-price)
    table.clear()