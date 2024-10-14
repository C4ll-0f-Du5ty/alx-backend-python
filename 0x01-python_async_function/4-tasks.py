#!/usr/bin/env python3
"""_summary_
    """
import bisect
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_

    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
        list[float]: _description_
    """
    delays = []
    for _ in range(n):
        bisect.insort(delays, await task_wait_random(max_delay))

    return delays
