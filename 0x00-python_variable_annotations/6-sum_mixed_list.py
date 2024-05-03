#!/usr/bin/env python3
'''function to return the sum of int
and float and returns it as float.'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''returns the sum of the list as float.'''
    return sum(mxd_lst)
