#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def main():
    """ main function """

    # Check if the necessary arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    port = 3306

    # Establish a connection with the database
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=port)
    except MySQLdb.Error as e:
        print("An error occurred while trying to connect to the database:")
        print(str(e))
        sys.exit(1)

    # Create a cursor object
    cur = db.cursor()

    # Define the SQL query to fetch all states
    sql_query = """SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id"""

    # Execute the SQL query
    try:
        cur.execute(sql_query)
    except MySQLdb.Error as e:
        print("An error occurred while trying to execute the SQL query:")
        print(str(e))
        cur.close()
        db.close()
        sys.exit(1)

    # Fetch all the states from the query result
    rows = cur.fetchall()

    # Iterate over the states and print each state name
    for row in rows:
        print(row)

    # Close the cursor and the connection to the database
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
