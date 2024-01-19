#!/usr/bin/python3
""" 
    Lists all states from the database hbtn_0e_0_usa 
    Functionality: 
        - Connects to the database using the provided credentials 
        - Executes a SQL query to select all cities from the specified state 
        - Prints the list of cities separated by commas 
        - Closes the database connection 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""
        SELECT cities.name 
        FROM cities 
        INNER JOIN states ON states.id=cities.state_id 
        WHERE states.name=%s 
    """, (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
