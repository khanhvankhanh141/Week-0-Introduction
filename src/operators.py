"""
Collection of the core mathematical operators used throughout the code base.
"""
import math

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    """Implement multiply operation for 2 number
    `f(x, y) = x * y`

    Args:
        x (float): first number
        y (float): second number

    Raises:
        NotImplementedError: Raise when function is not implemented
    """    

    return x * y
    raise NotImplementedError('Need to implement for Task 0.1')


def add(x, y):
    """Implement adding operation for 2 number
    `f(x, y) = x + y`

    Args:
        x (float): first number
        y (float): second number

    Raises:
        NotImplementedError: Raise when function is not implemented
    """    

    return x + y
    raise NotImplementedError('Need to implement for Task 0.1')


def neg(x):
    """Implement return negative version of a number
    `f(x, y) = -x`

    Args:
        x (float): first number
        y (float): second number

    Raises:
        NotImplementedError: Raise when function is not implemented
    """

    return -x
    raise NotImplementedError('Need to implement for Task 0.1')


def max(x, y):
    """Implement max operation for return the larger number of 2 number
    `f(x, y) = x if x is greater than y else y`

    Args:
        x (float): first number
        y (float): second number

    Raises:
        NotImplementedError: Raise when function is not implemented
    """
    if x > y :
        return x
    else:
        return y

    raise NotImplementedError('Need to implement for Task 0.1')
