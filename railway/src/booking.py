import sqlite3

def book(train_id,num):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    uid = 'kash'
    password = '123'

    cursor.execute('SELECT * FROM trains where train_id='+train_id)
    row = cursor.fetchone()
    avail_seats = row[3]-row[4] 

    cursor.execute('SELECT balance FROM users where uid=\'{id}\' and pass = \'{password}\''.format(id=uid,password = password))

    balance = cursor.fetchone()[0]
    print("User Balance: ",balance)

    price = num*row[6]
    if num<= avail_seats:
        if  price<= balance:
            print("Booking seat please wait.....")
            cursor.execute('UPDATE users SET balance = {bal} WHERE uid=\'{id}\' and pass = \'{password}\''.format(bal = balance-price,id=uid,password = password))
            conn.commit()
            cursor.execute('insert into booking values(\'{uid}\',{train},{num})'.format(uid=uid,train=train_id,num=num))
            conn.commit()
            cursor.execute('UPDATE trains SET  seats_res = {seats} WHERE train_id={train}'.format(seats=row[4]+num,train=train_id))
            conn.commit()
            print("Remaining Balance: ",balance-price)
        else:
            print("Insufficient balance")
    else:
        print("\nOnly "+str(avail_seats)+' Seats are available')
    return row