#!/usr/bin/python3
"""
This script deletes all states from a MySQL
database whose names contain the letter 'a'.

It utilizes the SQLAlchemy library to connect
to a MySQL database and perform the deletion operation.

**Usage:**

python delete_states_containing_a.py <username> <password> <database>

- `<username>`: The username for accessing the MySQL database.
- `<password>`: The password for the provided username.
- `<database>`: The name of the MySQL database containing the states table.
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

    filtered_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()
    # Print the State objects
    for state in filtered_to_delete:
        session.delete(state)
    session.commit()
    session.close()
