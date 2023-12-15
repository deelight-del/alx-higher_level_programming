#!/usr/bin/python3
""" This module contains the use of an ORM to
get all the states in a given database table."""

if __name__ == '__main__':
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost", port=3306, db=db_name,
        user=username, passwd=password, charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
