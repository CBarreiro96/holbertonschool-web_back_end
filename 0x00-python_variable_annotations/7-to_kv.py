#!/usr/bin/env python3

"""
Exercise:
Complex types - string and int/float to tuple
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    takes a string k and an int OR float v as arguments
    :param k:
    :param v:
    :return: a tuple.
    """
    return k, v ** 2
