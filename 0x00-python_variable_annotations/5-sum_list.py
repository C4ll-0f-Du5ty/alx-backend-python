#!/usr/bin/env python3
"""_summary_"""


def sum_list(input_list: list[float, int]) -> float:
    """_summary_

    Args:
        input_list (float): _description_

    Returns:
        float: _description_
    """
    counter = 0
    for i in input_list:
        counter += i
    return counter
