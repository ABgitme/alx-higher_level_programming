#!/usr/bin/python3
"""
This script queries and displays a list of cities
along with their corresponding states from a MySQL database.

It utilizes SQLAlchemy to connect to the database,
define models (`State` and `City`), and perform queries.

The script expects three command-line arguments:

- username (MySQL username)
- password (MySQL password)
- database (Name of the MySQL database)

It retrieves city data, orders them by ID, and prints each city's ID,
name, and the name of its corresponding state.
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

    cities = session.query(City).order_by(City.id).all()
    # Iterate over City objects
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()
