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
    cursor.execute("SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON state_id = cities.states.id\
        WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))
    rows = cursor.fetchall()
    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))
    cursor.close()
    db.close()
