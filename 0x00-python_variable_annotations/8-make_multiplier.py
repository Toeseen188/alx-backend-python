#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier
"""
import typing
callback = typing.Callable[[float], float]


def make_multiplier(multiplier: float) -> callback:
    """
    takes a float as param and return
    a callable function that takes float and return float
    """
    def multiplier_function(num: float) -> float:
        """
        takes a float and multiplies with muliplier
        and returns a float
        """
        return num * multiplier

    return multiplier_function
