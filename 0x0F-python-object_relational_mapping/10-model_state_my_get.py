#!/usr/bin/python3
""" prints the State object with the name passed as argument from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

# Create an engine that connects to the MySQL database
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

# Create the necessary tables in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session object
session = Session()

# Query the database for the State object with the specified name
instance = session.query(State).filter(State.name == (sys.argv[4],))

# Print the ID of the State object if it was found, or 'Not found' if not
try:
    print(instance[0].id)
except IndexError:
    print("Not found")
