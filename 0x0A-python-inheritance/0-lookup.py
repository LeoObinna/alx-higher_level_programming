#!/usr/bin/python3
"""This defines an object attribute lookup function."""


def lookup(obj):
    """Here it returns a list of an object's available attributes"""
    return (dir(obj))
