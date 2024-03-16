#!/usr/bin/python3
"""list citys"""
import MySQLdb
import sys


def main():
    username, password, database, state = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", user=username, password=password, db=database
    )
    cur = conn.cursor()
    query = f"SELECT cities.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = {state} \
        ORDER BY cities.id ASC"
    cur.execute(query)
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
