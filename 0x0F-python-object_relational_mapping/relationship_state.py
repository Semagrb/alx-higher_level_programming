#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative\_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative\_base
from sqlalchemy.orm import relationship

mymetadata = MetaData()
Base = declarative\_base(metadata=mymetadata)

class State(Base):
    """
    The State class represents a state in the database. It has an integer id, which is the primary key, and a string name.
    It also has a relationship to the City class, which is represented by the 'cities' attribute. This attribute is a relationship to
    the City class, and the 'backref' argument is used to create a 'states' attribute on the City class, which can be used to access
    the State object associated with a City object.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary\_key=True)
    name = Column(String(128), nullable=False)

    # The 'cities' relationship represents the many cities that belong to this state.
    cities = relationship("City", backref="states")
