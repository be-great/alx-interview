#!/usr/bin/python3

"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    function that returns the perimeter of the island
    described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # add 4 sides of the land cell
                perimeter += 4
                if j < cols - 1 and grid[i][j + 1] == 1:

                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
    return perimeter
