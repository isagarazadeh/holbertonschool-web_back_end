#!/usr/bin/env python3
"""multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable"""
    def fun(num: float) -> float:
        """multiplying num by multiplier"""
        return (num * multiplier)
    return fun
