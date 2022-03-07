#!/usr/bin/python3
"""
This script will list all the cities from a given state
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlachemy.schema import Table
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    # Create engine and connect to database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, db), pool_pre_ping=True,
                           echo=True, future=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).\
            order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
