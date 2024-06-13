#!/usr/bin/python3

"""This module contains a function that calculates
   minimum operations.
"""


def minOperations(n):
    """This function calculates and returns
       number of minimum operations.

       Args:
          n (int): number of operations to be perfromed.
       Returns:
          total number of minimum operation possible.
    """

    n_factor = 2

    num_of_operation = 0

    if n <= 1:
        return 0
    
    while n > 1:
        while n % n_factor == 0: # check if n is factorisable.
            num_of_operation += n_factor
            n = n // n_factor
        
        n_factor += 1

    return num_of_operation

    