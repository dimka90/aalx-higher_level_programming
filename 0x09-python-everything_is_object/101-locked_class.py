#!/usr/bin/python3
""" Can only create firstname"""


class LockedClass:
    """
    Only the creation of obejct only if the attribute is firstname
    """
    __slots__ = ('firstname',)
