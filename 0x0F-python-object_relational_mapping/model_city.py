#!/usr/bin/python3
"""
This module defines a SQLAlchemy model for
representing cities in a database.

The module utilizes the SQLAlchemy declarative
base class to create a model named `City`.
The `City` class represents a row in the `cities` table of a database,
with a foreign key relationship to the `states` table.

"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    This class represents a city entity in a database.

    It maps to the `cities` table and has the following attributes:

    - id: (Integer, Primary Key) The unique identifier for the city.
    - name: (String) The name of the city (maximum length of
        128 characters, not nullable).
    - state_id: (Integer, Foreign Key) The foreign key referencing
        the `id` of the state this city belongs to (not nullable).
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
