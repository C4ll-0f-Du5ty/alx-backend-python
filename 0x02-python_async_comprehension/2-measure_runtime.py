#!/usr/bin/env python3


import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension

async def measure_runtime() -> float:
    now = time.time()
    temp = await asyncio.gather(async_comprehension,
                   async_comprehension,
                   async_comprehension)
    
    then = time.time()
    return (then - now)
