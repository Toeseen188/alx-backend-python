#!/usr/bin/env python3
"""
a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0
and 10. Use the random module.
"""
import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """
    a function that takes no arg
    and yield from random number
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
