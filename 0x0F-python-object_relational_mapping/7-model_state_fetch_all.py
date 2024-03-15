#!/usr/bin/python3
"""
This script queries a MySQL database for all states and prints them.

It utilizes SQLAlchemy to connect to the database and retrieve
data from the `State` model defined in the `model_state` module.

The script expects three command-line arguments:
- username: The username for accessing the MySQL database.
- password: The password for accessing the MySQL database.
- database: The name of the database containing the states table.
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

    states = session.query(State).order_by(State.id).all()

    # Print the State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
