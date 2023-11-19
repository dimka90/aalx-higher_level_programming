#!/usr/bin/python3
"""
Script to add an objects of type State
to  the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def get_state(username, password, database_name):
    """
    Add a State object to the specified database.

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

    # Create an Instance of a state
    new_state = State(name="Louisiana")

    # adding to session
    session.add(new_state)

    # commiting the new state
    session.commit()
    # printing the id of the newly created state
    print(f"{new_state.id}")

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
