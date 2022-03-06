#!/usr/bin/python3
"""
Return `states.id` sorted in ascending order
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connect to the database
    db = MySQLdb.connect("localhost",
                         3306,
                         argv[1],
                         argv[2],
                         argv[3])
    # Create a cursor
    cursor = db.cursor()
    # Execute a query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows from the query
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close the cursor
    cursor.close()
    # Close the database connection
    db.close()
