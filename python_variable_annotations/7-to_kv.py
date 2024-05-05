#!/usr/bin/env python3
"""Tuples"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returning tuples"""
    return (k, v ** 2)
