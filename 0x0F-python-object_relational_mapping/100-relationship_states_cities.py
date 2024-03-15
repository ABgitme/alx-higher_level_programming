#!/usr/bin/python3
"""
This script creates a new state ("California") and a city ("San Francisco") 
associated with that state in a MySQL database.

It takes the following arguments:

- username (str): MySQL username.
- password (str): MySQL password.
- database (str): Name of the MySQL database.

The script utilizes the SQLAlchemy library to connect to the database and 
manages the database session. It leverages models defined in separate modules 
(relationship_state.py and relationship_city.py) for representing states and cities.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Check if correct number of arguments provided

    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                username, password, database, pool_pre_ping=True
                )
            )
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State object for California
    california = State(name="California")

    # Create City object for San Francisco
    san_francisco = City(name="San Francisco", state=california)

    # Add State and City objects to session
    session.add(california)
    session.add(san_francisco)

    # Commit the session to save changes to the database
    session.commit()
    session.close()
