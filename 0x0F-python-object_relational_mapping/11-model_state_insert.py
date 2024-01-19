#!/usr/bin/python3
""" This script connects to the specified database and retrieves the State object with the name passed as argument from the database.

   Steps:

   1. The necessary libraries (Base, State) and function (sessionmaker) are imported from the 'model_state' module.

   2. If the script is executed as the main module, it proceeds to connect to the database. The 'create_engine' function from 'sqlalchemy' library is used to establish a connection to the database. The function parameters are taken from the command line arguments.

   3. Once connected, the 'create_all' function from 'sqlalchemy.metadata' library is used to create all the tables defined in the 'Base' object.

   4. The 'sessionmaker' function is used to create a new session factory for the connection to the database.

   5. The 'Session' object is created by calling the session factory.

   6. A new state object is created and added to the session using the 'add' method.

   7. The newly added state object is retrieved from the database using the 'query' method.

   8. The ID of the retrieved state object is printed.

   9. The changes made in the session are committed to the database using the 'commit' method.

   Please note that this script should be run from the command line and the following arguments should be provided: username, password, and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    session.add(new_state)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print(new_instance.id)
    session.commit()
