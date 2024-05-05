#!/usr/bin/env python3
"""sum list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """summing lists"""
    summa = 0
    for i in mxd_lst:
        summa += i
    return summa
