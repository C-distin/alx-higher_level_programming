#!/usr/bin/python3
"""
This module contains a function that safe filters cities by user input.
"""

import MySQLdb
from sys import argv

if __name__ == "__main":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
                FROM states
                INNER JOIN cities ON states.id = cities.state_id
                WHERE states.name LIKE %s
                ORDER BY cities.id ASC""", (argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
