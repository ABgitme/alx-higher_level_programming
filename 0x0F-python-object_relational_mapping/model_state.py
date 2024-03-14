#!/usr/bin/python3
"""
This module defines a SQLAlchemy model
for representing states in a database.

The module utilizes the SQLAlchemy declarative
base class to create a model named `State`.

The `State` class represents a row in the `states`
table of a database.

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class represents a state entity in a database.

    It maps to the `states` table and has the following attributes:

    - id: (Integer, Primary Key, Unique) The unique
        identifier for the state.
    - name: (String) The name of the state
        (maximum length of 128 characters, not nullable).
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
