#!/usr/bin/python3
"""
This script queries a MySQL database for a state based on a provided name.

It utilizes SQLAlchemy to create an engine, a session, and perform the query.

**Usage:**

./script.py <username> <password> <database> <state_name>

- `<username>`: MySQL username
- `<password>`: MySQL password
- `<database>`: Name of the MySQL database
- `<state_name>`: Name of the state to search for

**Output:**

The script prints the ID of the state if found, or "Nothing" if not found.
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
    state_name = sys.argv[4]

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

    filtered = session.query(State).filter(State.name == state_name).first()
    # Print the State objects
    if filtered:
        print("{}".format(filtered.id))
    else:
        print("Nothing")

    session.close()
