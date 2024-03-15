#!/usr/bin/python3
"""
This module provides functionality to connect
to a MySQL database, create a new state record,
and commit the changes to the database.

It leverages SQLAlchemy to interact with the database
and expects command-line arguments for
database credentials and database name.

Usage:
python <script_name> <username>
<password> <database_name> <state>

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

    new_state = State(name="Louisiana")
    # Add State object to session
    session.add(new_state)

    # Commit the session to save changes to the database
    session.commit()

    # Print the new State object's id
    print(new_state.id)

    session.close()
