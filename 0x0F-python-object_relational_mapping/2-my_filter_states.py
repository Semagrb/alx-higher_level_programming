#!/usr/bin/python3

"""
Module that lists all states from the h_0e_0_usa database.
"""

import sys
import MySQLdb

if __name__ == "__main__":

    # Get MySQL credentials and search name from command-line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],  # MySQL user
        passwd=sys.argv[2],  # MySQL password
        db=sys.argv[3]  # Database name
    )

    # Create a cursor object to interact with the database
    c = db.cursor()

    # Define the SQL query to retrieve states with the specified name
    query = """
        SELECT *
        FROM `states`
        WHERE BINARY `name` = %s
    """

    # Execute the SQL query with the specified name as a parameter
    c.execute(query, (sys.argv[4],))

    # Fetch all rows and print the states
    [print(state) for state in c.fetchall()]
