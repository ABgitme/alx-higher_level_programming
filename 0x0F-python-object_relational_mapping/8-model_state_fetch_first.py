#!/usr/bin/python3
"""
This script connects to a MySQL database, queries the `State` table,
and prints the first state record if it exists.

It takes the following arguments:
  1. username: Username for the MySQL database.
  2. password: Password for the MySQL database.
  3. database: Name of the MySQL database to connect to.

The script utilizes SQLAlchemy to establish a connection to the database,
create a session, and perform the query. The first state object is retrieved
and printed if found. Otherwise, a message indicating "Nothing" is printed.
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

    first = session.query(State).order_by(State.id).first()
    if first:
        # Print the State objects
        print("{}: {}".format(first.id, first.name))

    else:
        print("Nothing")
    session.close()
