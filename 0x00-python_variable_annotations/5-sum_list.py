#!/usr/bin/env python3
import typing
"""
a function that accept a list of float
and return the sum
"""
Input_list = typing.List[float]


def sum_list(input_list: Input_list) -> float:
    """
    take inpu_list of float and
    return the sum
    """
    return sum(input_list)
