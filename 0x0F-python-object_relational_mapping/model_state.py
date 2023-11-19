#!/usr/bin/python3
"""
Module: myscript.py

This module defines a SQLAlchemy model class, State,
for interacting with a MySQL database. It also creates
the necessary database table based on the model.

Usage:
    python myscript.py <username> <password> <database_name>

Arguments:
    <username> (str): MySQL username.
    <password> (str): MySQL password.
    <database_name> (str): Name of the MySQL database.

Example:
    python myscript.py john secret mydatabase
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine, MetaData

# Creating the base model
base_metadata = MetaData()
Base = declarative_base(metadata=base_metadata)


class State(Base):
    """
    Class: State

    SQLAlchemy model class representing the 'states' table in a MySQL database.

    Attributes:
        id (int): Primary key column.
        name (str): Column for storing state names.

    Usage:
        state = State(name='California')
    """

    __tablename__ = "states"

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
