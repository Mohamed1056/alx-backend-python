#!/usr/bin/env python3
'''using asyncio, random module in this function.'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    function to make async process.
    '''
    MyWait = random.uniform(0, max_delay)
    await asyncio.sleep(MyWait)
    return MyWait
