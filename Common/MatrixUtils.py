from typing import List


def matrix_size(matrix: List[List[int]]):
    if not matrix:
        return 0
    return len(matrix) * len(matrix[0])
