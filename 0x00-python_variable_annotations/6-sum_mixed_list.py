#!/usr/bin/env python3
"""_summary_"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (typing.Union[int, float]): _description_

    Returns:
        float: _description_
    """
    return sum(mxd_lst)
