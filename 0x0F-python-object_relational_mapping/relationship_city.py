#!/usr/bin/python3
"""
This module defines a SQLAlchemy model for
representing cities in a database.

The module utilizes the SQLAlchemy declarative base
class (`Base`) from the `relationship_state` module
to create a model named `City`.

The `City` class represents a row in the `cities`
table of a database and has a foreign key relationship
with the `State` model.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    This class represents a city entity in a database.

    It maps to the `cities` table and has the following attributes:

    - id: (Integer, Primary Key, Not Null) The unique identifier for the city.
    - name: (String, Not Null) The name of the
        city (maximum length of 128 characters).
    - state_id: (Integer, Foreign Key)
        The foreign key referencing the id of the
        associated state (references the states.id column).
    - state: (Relationship) A relationship with the `State` model, allowing
        access to the related state object.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
