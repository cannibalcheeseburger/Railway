import sqlite3
from src import avail,all_trains,booking,all_booked,cancel

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def main():
    ans=True
    while ans:
        print ("""
*****Main Menu*****
1.See all trains
2.Available trains
3.Booking seats
4.See all bookings
5.Cancelling seats
0.Exit/Quit
        """)
        ans=input("Enter Selection: ") 
        if ans=="1": 
            all_trains.all_trains(cursor)
        elif ans=="2":
            avail.Avail(cursor)
        elif ans=="3":
            booking.book(conn,cursor)
        elif ans=="4":
            all_booked.all_book(conn,cursor)
        elif ans=="5":
            cancel.Cancelling(conn,cursor)
        elif ans=="0":
            print("\n Goodbye")
            ans = False 
        else:
            print("\n Not Valid Choice Try again")

if __name__ == "__main__":
    main()

