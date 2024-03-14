#!/usr/bin/python3
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

    states = session.query(State).order_by(State.id).all()
    # Iterate over State objects
    for state in states:
        print(f"{state.id}: {state.name}")
        # Iterate over City objects associated with each State
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
