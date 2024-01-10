#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creates an Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        The Python data structure represented by the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
