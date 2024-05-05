#!/usr/bin/env python3
"""object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """iteration"""
    for i in lst:
        return [(i, len(i))]
