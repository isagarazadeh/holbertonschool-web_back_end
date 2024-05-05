#!/usr/bin/env python3
"""Asynchronous"""
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task"""
    waits = [task_wait_random(max_delay) for i in range(0, n)]
    delays = []
    for i in asyncio.as_completed(waits):
        delay = await i
        delays.append(delay)

    return delays
