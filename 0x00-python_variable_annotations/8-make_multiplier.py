#!/usr/bin/env python3
'''a type-annotated function make_multiplier that
takes a float multiplier as argument and
returns a function that multiplies a float by multiplier'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''A function that returns a function'''
    def innerMul(multiplier2: float) -> float:
        '''A function that takes a multiplier2'''
        return multiplier2 * multiplier
    return innerMul    
