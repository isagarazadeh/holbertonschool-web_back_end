#!/usr/bin/env python3
"""Asynchronous"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """function"""
    for i in range (0, n):
        waits = [wait_random(max_delay)]
        dely = []
    for i in asyncio.as_completed(waits):
        delay = await i
        dely.append(delay)

    return delays
