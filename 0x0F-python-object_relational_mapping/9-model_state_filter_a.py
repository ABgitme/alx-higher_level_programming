#!/usr/bin/python3
"""
This module queries and prints states from a MySQL database containing 'a'

It retrieves states whose names contain the letter 'a', orders them by their ID, and prints
their ID and name in a formatted manner.

To use this module, provide MySQL credentials and database name as command-line arguments:

python3 this_module.py <username> <password> <database_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    filtered = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    # Print the State objects
    for state in filtered:
        print("{}: {}".format(state.id, state.name))

    session.close()
