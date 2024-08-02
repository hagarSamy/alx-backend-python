#!/usr/bin/env python3
'''debugging'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''a function that takes a list of a sequence: tuple or list
    Returns: A list of tuples, each contains a sequence
    from the input list and its length.
    '''
    return [(i, len(i)) for i in lst]
