#!/usr/bin/env python3
"""
This module contains a function to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): A list of ints/floats.
        arr2 (list): A list of ints/floats.

    Returns:
        list: A new list with the element-wise sum of arr1 and arr2.
        None: If arr1 and arr2 are not the same shape.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
