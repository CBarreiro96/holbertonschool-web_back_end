#!/usr/bin/env python3

"""
Exercise:
Complex types - mixed list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function sum of two diferent type of number
    :param mxd_lst:
    :return: sum as a float
    """
    return float(sum(mxd_lst))
