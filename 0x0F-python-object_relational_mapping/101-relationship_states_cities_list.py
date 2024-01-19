#!/usr/bin/python3
"""
Module that creates a State object with the name "California" and a City object with the name "San Francisco".
It then associates the City object with the State object.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create a database engine using the provided arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Create a new State object with the name "California"
    newState = State(name='California')

    # Create a new City object with the name "San Francisco"
    newCity = City(name='San Francisco')

    # Associate the newCity object with the newState object
    newState.cities.append(newCity)

    # Add the newState object and the newCity object to the session
    session.add(newState)
    session.add(newCity)

    # Commit the changes to the database
    session.commit()
