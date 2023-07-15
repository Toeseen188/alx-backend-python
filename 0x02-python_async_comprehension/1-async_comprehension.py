#!/usr/bin/env python3
"""
Import async_generator from the previous task
and then write a coroutine called async_comprehension that takes
no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator
List = typing.List[float]


async def async_comprehension() -> List:
    """
    this function take no argument
    collect 10 random number from async_generator
    then return it
    """

    return [i async for i in async_generator()]
