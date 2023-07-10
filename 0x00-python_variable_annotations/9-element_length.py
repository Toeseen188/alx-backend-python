#!/usr/bin/env python3
"""
annotate the function
"""
import typing
Ret = typing.List[typing.Tuple[typing.Sequence, int]]
Lst = typing.Iterable[typing.Sequence]


def element_length(lst: Lst) -> Ret:
    """
    take a list and return the number of element
    in a list
    """
    return [(i, len(i)) for i in lst]
