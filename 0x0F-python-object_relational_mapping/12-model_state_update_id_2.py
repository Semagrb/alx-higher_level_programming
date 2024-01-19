#!/usr/bin/python3
""" This script connects to the specified database and retrieves a State object from the database. The name of the State object is then updated and the changes are committed to the database.

   Steps:

   1. The necessary libraries (Base, State) and function (sessionmaker) are imported from the 'model_state' module.

   2. If the script is executed as the main module, it proceeds to connect to the database. The 'create_engine' function from 'sqlalchemy' library is used to establish a connection to the database. The function parameters are taken from the command line arguments.

   3. Once connected, the 'create_all' function from 'sqlalchemy.metadata' library is used to create all the tables defined in the 'Base' object.

   4. The 'sessionmaker' function is used to create a new session factory for the connection to the database.

   5. The 'Session' object is created by calling the session factory.

   6. The State object with ID 2 is retrieved from the database using the 'query' method.

   7. The name of the retrieved state object is updated to "New Mexico".

   8. The changes made in the session are committed to the database using the 'commit' method.

   Please note that this script should be run from the command line and the following arguments should be provided: username, password, and database name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
