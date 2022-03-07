#!/usr/bin/python3
"""
This module contains a function that safe filters cities by user input.
"""

import MySQLdb
from sys import argv

if __name__ == "__main":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
        FROM cities JOIN states ON cities.state_id = states.id\
        WHERE states.name LIKE %s ORDER BY cities.id ASC", (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print('{:d}, {:s}'.format(row[0], row[1]))
    cursor.close()
    db.close()
