#!/usr/bin/python3
"""
This module establishes a connection to a MySQL database, retrieves all
'State' objects, and prints their names along with the names of their
associated 'City' objects.

The script expects three command-line arguments:
    1. MySQL username
    2. MySQL password
    3. Target database name
"""
import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

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
    session = Session(bind=engine)

    states = session.query(State).order_by(State.id)
    # Iterate over State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))
        # Iterate over State objects associated with each State
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
