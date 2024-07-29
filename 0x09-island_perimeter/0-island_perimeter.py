#!/usr/bin/python3

""" This module contains a function that
    calculates the perimeter of a grid.
"""


def island_perimeter(grid):
    """This function calculates the perimeter of a grid.
       Args:
           grid(list of list of int): This represents the grid
                                 representation in lists.
       Returns:
            perimeter of the grid in integer.
    """

    grid_row = len(grid)
    grid_col = len(grid[0])

    grid_perimeter = 0
    # loop through the row and cols.
    for i in range(grid_row):
        for j in range(grid_col):
            # check for a matrix value of 1.
            if grid[i][j] == 1:
                grid_perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    grid_perimeter -= 2
                if i > 0 and grid[i][j - 1] == 1:
                    grid_perimeter -= 2

    return grid_perimeter
