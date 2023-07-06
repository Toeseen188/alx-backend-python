#!/usr/bin/env python3

import math
from typing import NewType

"""
a function that take n (float) as a parameter
and return floor of it
"""
floor = NewType("floor", int)


def floor(n: float) -> floor:
    """
    takes n(float) as arg and return int
    """
    return math.floor(n)
