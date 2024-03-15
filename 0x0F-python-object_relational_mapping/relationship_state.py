#!/usr/bin/python3
"""
This module defines a SQLAlchemy model for representing
states and their associated cities in a database.

The module utilizes the SQLAlchemy declarative
base class to create a model named `State`.
The `State` class represents a row in the `states` table of a database,
and it can have a relationship with multiple `City` objects.

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class represents a state entity in a database.

    It maps to the `states` table and has the following attributes:

    - id: (Integer, Primary Key, Not Null) The unique identifier for the state.
    - name: (String, Not Null) The name of the state
        (maximum length of 128 characters).
    - cities: (relationship) A relationship with the `City` class.
        It specifies a one-to-many relationship
        between a `State` and its associated `City` objects.
        The `back_populates` argument defines
        the backreference on the `City` model (usually a field named `state`).
        The `cascade` argument specifies that operations
        on a `State` object should also cascade
        to its related `City` objects
        (e.g., deleting a state also deletes its cities).
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete")
