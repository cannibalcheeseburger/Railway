import sqlite3
from src import avail

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def main():
    avail.Avail(cursor)

if __name__ == "__main__":
    main()