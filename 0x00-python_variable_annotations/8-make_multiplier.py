#!/usr/bin/env python3

"""
Execise:
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument
    :param multiplier:
    :return: A function that multiplies a float by multiplier.
    """

    def multiplication_operation(n: float) -> float:
        """multiplies a float by multiplier"""
        return float(n * multiplier)

    return multiplication_operation
