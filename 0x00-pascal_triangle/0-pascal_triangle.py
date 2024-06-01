#!/usr/bin/python3
"""
    This module contians a function implementation that returns
    a pascal triagle as a lists of a list.
"""


def pascal_triangle(n):
    """
        This function returns a lists of a list of Pascal's Triangle
    """

    if n <= 0:
        return []

    trianlge_list = [[1]]  # I initialised the list with 1.

    for i in range(1, n):
        tri_row = [1]  # I set the first element of the row to 1.

        for j in range(1, i):
            tri_row.append(trianlge_list[i-1][j-1] + trianlge_list[i-1][j])
        tri_row.append(1)
        trianlge_list.append(tri_row)

    return trianlge_list
