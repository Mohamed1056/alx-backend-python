#!/usr/bin/env python3
'''function to return tuple containing
the first parameter: a string
the second parameter: a int/float
'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''returns a tuple.'''
    return (k, v ** 2)
