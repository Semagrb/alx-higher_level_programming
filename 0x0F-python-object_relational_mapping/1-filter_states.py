import sys
import sqlite3


def get_states(cursor):
    cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    return cursor.fetchall()


def main():
    if len(sys.argv) != 5:
        print("Usage: python3 script.py db_name table_name user pass")
        return

    db_name, table_name, user, passwd = sys.argv[1:]
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    states = get_states(cursor)

    if states:
        for state in states:
            print(state)
    else:
        print("No states found")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
