#!/usr/bin/python3
"""
Script to edit  an objects using the Id of the object
in  the database hbtn_0e_6_usa.
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

    # variable to stored the id of the state to edit
    state_id = 2

    # Query to search for the id
    query = session.query(State).filter_by(id=tate_id).first()

    # checking if a result was return
    if query:
        query.name = "New Mexico"
    # commiting the new state
    session.commit()

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
