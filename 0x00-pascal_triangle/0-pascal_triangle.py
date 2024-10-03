#!/usr/bin/python3
"""
a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of
"""


def pascal_triangle(n):
    """
    args:
        n : level of the triangle
    """
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        # update the row if it's not the first row
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
