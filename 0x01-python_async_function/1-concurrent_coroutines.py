#!/usr/bin/env python3
"""_summary_
    """
import bisect
# from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    delays = []
    for _ in range(n):
        bisect.insort(delays, await wait_random(max_delay))

    return delays
