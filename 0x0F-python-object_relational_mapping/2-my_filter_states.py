#!/usr/bin/python3
""" This module contains the use of an ORM to
get all the states in a given database table."""

if __name__ == '__main__':
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=db_name, charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY name = '{}'\
        ORDER BY id ASC".format(search_name)
        )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
