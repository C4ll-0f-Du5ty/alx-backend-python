#!/usr/bin/env python3
"""_summary_"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """_summary_

    Args:
        input_list (float): _description_

    Returns:
        float: _description_
    """
    counter: float = 0
    for i in input_list:
        counter += i
    return counter
