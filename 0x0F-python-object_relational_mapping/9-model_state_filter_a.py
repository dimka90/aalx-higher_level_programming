#!/usr/bin/python3
"""
Script to list the first State objects
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def get_state(username, password, database_name):
    """
    Lists the first  State objects from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the MySQL database.
    """

    # Create the database connection URL
    DATABASE_URL = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    username, password, database_name)

    # Create the database engine
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    target_letter = 'a'

    # Query all State objects, sorted by id
    states = session.query(State).order_by(State.id).filter(
              State.name.like(f'%{target_letter}%')).all()

    # checking if there is any state in the table
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("""Usage: python script_name.py <username>
               <password> <database_name>""")
        sys.exit(1)

    # Extract command-line arguments
    username, password, database_name = sys.argv[1:4]

    # Call the function to list states
    get_state(username, password, database_name)
