#!/usr/bin/python3
""" Can only create firstname"""


class LockedClass:
    """
    Only the creation of obejct only if the attribute is firstname
    """
    __slots__ = ('first_name',)

    def __init__(self):
        """
           Create an instance of the Lockedclass
           Args:
              self(object) : instance of the newly created object
        """
        self.first_name = 'first_name'
