#!/usr/bin/python3
"""
This script updates the name of a specific state in a MySQL database
using SQLAlchemy.

It retrieves the state with the provided ID (2 in this case) and
updates its name.
The script expects the following command-line arguments:

1. Username: The username for accessing the MySQL database.
2. Password: The password for accessing the MySQL database.
3. Database name: The name of the database containing the states table.

The script utilizes the `model_state` module which defines the database model
for states.
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

    state_to_update = session.query(State).filter_by(id=2).first()
    # Check if State object with id = 2 exists
    if state_to_update:
        # Change the name of the State object
        state_to_update.name = "New Mexico"
        # Commit the session to save changes to the database
        session.commit()

    session.close()
