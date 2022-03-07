#!/usr/bin/python3
"""
Add "Louisiana" to state object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # Create engine and connect to the database
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

    # Add "Louisiana" to state object from the database hbtn_0e_6_usa
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the state
    print(new_state.id)

    # Close session
    session.close()
