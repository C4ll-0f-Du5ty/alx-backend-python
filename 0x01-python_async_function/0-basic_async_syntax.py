#!/usr/bin/env python3
"""_summary_
    """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> int:
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        int: _description_
    """
    time: float = random.random() * max_delay
    # await asyncio.sleep(time)
    return time
