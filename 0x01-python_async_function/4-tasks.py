#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without
using sort() because of concurrency.

from 0-basic_async_syntax import wait_random
"""
import random
import asyncio
import typing
task_wait_random = __import__('3-tasks').task_wait_random

List = typing.List[float]


async def task_wait_n(n: int, max_delay: int) -> List:
    """
    function takes n: int and max_delay: int as args
    and return a list
    """
    lst = []
    delay = []
    for i in range(n):
        task = task_wait_random(max_delay)
#        new = await asyncio.gather(task)
        lst.append(task)

    for ls in lst:
        dely = await ls
        delay.append(dely)

    return sorted(delay)
