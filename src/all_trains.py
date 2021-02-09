from prettytable import PrettyTable

table = PrettyTable()

def all_trains(cursor):
    cursor.execute("select * from trains limit 1")
    table.field_names = [col[0] for col in cursor.description]
    cursor.execute('SELECT * FROM trains')
    rows = cursor.fetchall()
    table.add_rows(rows)
    print(table)
    table.clear()