#!/usr/bin/env python3
"""asynchronous"""
import asyncio
import time
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returning asynchronous """
    task = asyncio.create_task(wait_random(max_delay))
    return task
