#!/usr/bin/python3
""" This module contains the use of an ORM to
get all the states in a given database table."""

if __name__ == '__main__':
    import sys
    import MySQLdb
    from sqlalchemy import create_engine, Table, MetaData
    sql_username = sys.argv[1]
    sql_password = sys.argv[2]
    db_name = sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=sql_username,
        passwd=sql_password, db=db_name, charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
