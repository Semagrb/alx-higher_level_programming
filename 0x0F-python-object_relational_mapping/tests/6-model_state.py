#!/usr/bin/python3
"""This script creates a link from the Python class to the database table.

It uses the SQLAlchemy library to create an engine that connects to the MySQL
database specified in the command line arguments, and then creates the necessary
tables in the database using the Base.metadata.create_all() method.

Usage:
  $ python3 script.py <username> <password> <database_name>
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create the necessary tables in the database
    Base.metadata.create_all(engine)
