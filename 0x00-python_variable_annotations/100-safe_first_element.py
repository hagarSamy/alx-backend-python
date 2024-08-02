#!/usr/bin/env python3
'''Augmented code with the correct duck-typed annotations'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''A function that takes a sequence of any type and returns eaither
    an element of any type or None'''
    if lst:
        return lst[0]
    else:
        return None
