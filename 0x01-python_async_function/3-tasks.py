#!/usr/bin/env python3
"""
Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function,
use the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random
# Task = asyncio.Task[typing.Callable[..., typing.Coroutine]]


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    a normal func that take an int and
    returns an asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
