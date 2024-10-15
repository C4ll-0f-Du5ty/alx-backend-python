#!/usr/bin/env python3
"""_summary_

    Yields:
        _type_: _description_
    """
import random
import typing
import asyncio


async def async_generator() -> typing.Generator[float, None, None]:
    """_summary_

    Returns:
        asyncio.Generator[float, None, None]: _description_

    Yields:
        Iterator[asyncio.Generator[float, None, None]]: _description_
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
