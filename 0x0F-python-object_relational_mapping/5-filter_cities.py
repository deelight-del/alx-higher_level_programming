#!/usr/bin/python3
""" This module contains the use of an ORM to
get all the states in a given database table."""

if __name__ == '__main__':
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_state = sys.argv[4]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=username,
        passwd=password, db=db_name, charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name\
        FROM cities INNER JOIN states\
        ON cities.state_id=states.id\
        WHERE states.name=%s\
        ORDER BY cities.id ASC", (search_state,)
        )
    query_rows = cur.fetchall()
    try:
        for row in query_rows[:-1]:
            print(row[0], end=", ")
        print(query_rows[-1][0])
    except (IndexError):
        print()
    cur.close()
    conn.close()
