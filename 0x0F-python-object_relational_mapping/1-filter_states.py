#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import sqlite3

def main():
    try:
        conn = sqlite3.connect('hbtn_0e_0_usa.db')
        cursor = conn.cursor()

        query = '''SELECT name FROM states'''
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state[0])

        cursor.close()
        conn.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
