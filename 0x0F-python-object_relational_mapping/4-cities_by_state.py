#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    # Establish a connection to the MySQL server using the provided credentials
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Define the SQL query to retrieve all cities and their corresponding states
    query = """
        SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
    """

    # Execute the SQL query
    cur.execute(query)

    # Fetch all rows and print the city and state information
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
