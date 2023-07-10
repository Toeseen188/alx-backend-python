#!/usr/bin/env python3
"""
this module contain a function that
takes a str 'k' and int/float 'v' as arguments
and return a tuple
"""
import typing

Tuple_ = typing.Tuple[str, float]


def to_kv(k: str, v: typing.Union[int, float]) -> Tuple_:
    """
    this function takes a string k and int or float k
    and return a tuple(int, float)
    """
    return (k, v*v)
