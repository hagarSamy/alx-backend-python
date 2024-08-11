#!/usr/bin/env python3
"""
synchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay
seconds and eventually returns it.
"""

from typing import List


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Async function that returns a list of wait times"""
    task_wait_random = __import__('3-tasks').task_wait_random
    import asyncio
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
