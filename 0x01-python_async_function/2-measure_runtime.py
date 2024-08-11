#!/usr/bin/env python3
"""
a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and
returns total_time / n. The function should return a float.
"""

import asyncio
import time


def measure_time(n: int, max_delay: int = 10) -> float:
    """Async function that measures total wait time"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = (end_time - start_time)
    return total_time / n