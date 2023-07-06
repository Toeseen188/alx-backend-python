#!/usr/bin/env python3
import typing
"""
a function that takes a list of int an and float
"""
Mxd_lst = typing.List[any]


def sum_mixed_list(mxd_lst: Mxd_lst) -> float:
    """
    take mixed type of value as parameter and return
    float
    """
    return sum(mxd_lst)
