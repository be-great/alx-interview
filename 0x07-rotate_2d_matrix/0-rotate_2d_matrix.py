#!/usr/bin/python3
"""
Rotate the given n x n to 90 degress
"""


def rotate_2d_matrix(matrix):
    """
    Roate 2D Matrix
    """
    n = len(matrix)
    # first we swap rows and columns
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse each row
    for row in matrix:
        row.reverse()
