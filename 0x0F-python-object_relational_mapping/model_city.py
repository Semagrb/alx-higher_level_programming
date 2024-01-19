#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    Class that defines each city. 
    A city has a unique identifier, a name, and a foreign key that refers to the state in which the city is located.
    """
    __tablename__ = 'cities'

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    """
    Unique identifier for each city. 
    This column is defined as an Integer data type and it cannot be null.
    """

    name = Column(String(128), nullable=False)
    """
    Name of the city. 
    This column is defined as a String data type with a maximum length of 128 characters.
    The value for this column cannot be null.
    """

    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    """
    Foreign key that refers to the state in which the city is located. 
    This column is defined as an Integer data type and it is a foreign key that refers to the 'id' column of the 'states' table.
    The value for this column cannot be null.
    """
