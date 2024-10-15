#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
    """


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        typing.List[float]: _description_
    """
    l: list = []
    async for i in async_generator():
        l.append(i)
    return l
