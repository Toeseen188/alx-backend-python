#!/usr/bin/env python3
"""
change the type annotation
"""
import typing
Lst = typing.Sequence[typing.Any]
Ret = typing.Union[typing.Any, None]


def safe_first_element(lst: Lst) -> Ret:
    """
    takes a list of any type  and return list or none
    """
    if lst:
        return lst[0]
    else:
        return None
