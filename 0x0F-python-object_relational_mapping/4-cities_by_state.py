#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Get arguments from command line"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    """ Create a cursor to execute SQL queries"""
    cur = db.cursor()

    """ Execute SQL query to get all states ordered by id"""
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)

    """ Fetch all results and print them"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ Close cursor and connection"""
    cur.close()
    db.close()
