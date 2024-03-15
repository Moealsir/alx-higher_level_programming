#!/usr/bin/python3
"""list states"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: script.py <username> <password> <database>")
        sys.exit(1)
    username, password, database = sys.argv[1:]
    username = 'root'
    password = '1111'
    database = 'hbtn_0e_0_usa'
    conn = MySQLdb.connect(
        host="localhost", user=username, password=password, db=database
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states \
            WHERE name LIKE 'N%' \
            ORDER BY id ASC LIMIT 2")
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
