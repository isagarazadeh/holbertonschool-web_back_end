#!/usr/bin/env python3
"""sum list"""
from typing import Union, List


def sum_list(imput_list: List[Union[float,int]]) -> float:
    """summing lists"""
    summa = 0
    for i in imput_list:
        summa += i
    return summa
