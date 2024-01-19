#!/usr/bin/python3
"""
The following code creates a State object with the name "California" and a City object with the name "San Francisco".
It then associates the City object with the State object. The updated code for each part of the code is provided below.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """
    This section of the code establishes a connection to the MySQL database. The database connection details, such as
    the username, password, and database name, are provided as command-line arguments when the script is run.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """
    The sessionmaker function is used to create a session factory, which can be used to create Session objects.
    The Session object is a Python object that represents a single database transaction.
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    The following lines of code create a new State object and a new City object. The newState object has the name
    "California", and the newCity object has the name "San Francisco".
    """
    newState = State(name='California')
    newCity = City(name='San Francisco')

    """
    The following line of code associates the newCity object with the newState object. The newCity object is then
    added to the newState object's 'cities' relationship, which represents the many cities that belong to this state.
    """
    newState.cities.append(newCity)

    """
    The following lines of code add the newState object and the newCity object to the session. This effectively
    tells SQLAlchemy that these objects need to be saved to the database. Finally, the session.commit() method is
    called to save the changes to the database.
    """
    session.add(newState)
    session.add(newCity)
    session.commit()
