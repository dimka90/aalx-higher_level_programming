#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)
    print("Object count",Base.get_ob_count())
    b2 = Base()
    print(b2.id)
    print("Obeject count",Base.get_ob_count())

    b3 = Base(12)
    print(b3.id)
    print("Object count", Base.get_ob_count())
    b4 = Base()
    print(b4.id)
    print("Object count", Base.get_ob_count())
    b5 = Base()
    print(b5.id)
    print("Object count", Base.get_ob_count())
