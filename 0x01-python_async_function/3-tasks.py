#!/usr/bin/env python3
"""
a function task_wait_random that takes an integer max_delay and
returns a asyncio.Task
"""

import asyncio


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Async function that returns a asyncio.Task"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.ensure_future(wait_random(max_delay))
    # return asyncio.create_task(wait_random(max_delay))
