#!/usr/bin/env python3
"""
synchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
seconds and eventually returns it.
"""


async def wait_random(max_delay: int = 10) -> float:
    """Async function that returns a random number after waiting """
    from random import uniform
    import asyncio

    random_float = uniform(0, max_delay)
    # generating a random floating-point number between 0 and max_delay
    await asyncio.sleep(random_float)
    return random_float
