#!/usr/bin/python3
""" Minimum Operations """

import math


def minOperations(n):
    """ 
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    if n % 2 == 0:
        return minOperations(n / 2) + 2
    else:
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return minOperations(n / i) + i
        return n