#!/bin/usr/python3
from sqlachemy import Column, Integer, String, create_engine
from sqlachmy.ext.declarative import declarative_base

# creating the base model

if "__Name__ " == "__main__":
    Base = declarative_base()
    # creating class Model
    class State(Base):
        __tablename__ = "states"
        id = Column(Integer, nullable = False, primary_key = True)
        name = Column(String(128), nullable = False)

        # creating a connection to the database 
        # using the engine function


