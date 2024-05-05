#!/usr/bin/env python3
"""Async func"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine called async_generator"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
