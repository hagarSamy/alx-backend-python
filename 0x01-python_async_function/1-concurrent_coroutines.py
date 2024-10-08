#!/usr/bin/env python3
"""
synchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
seconds and eventually returns it.
"""

from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Async function that returns a list of wait times"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    import asyncio
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []

    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        results.append(result)

    return results
