from prettytable import PrettyTable

table = PrettyTable()

def Avail(cursor):
    cursor.execute("select * from trains limit 1")
    table.field_names = [col[0] for col in cursor.description]
    
    day = input("Enter date (dd-mm-yyyy):")

    cursor.execute('SELECT * FROM trains where date=\''+ day+'\'')
    rows = cursor.fetchall()
    table.add_rows(rows)
    print(table)
    table.clear()