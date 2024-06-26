#!/usr/bin/env python3
"""Asynchronous"""
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Related to the function part"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total = time.time() - start

    return total/n
