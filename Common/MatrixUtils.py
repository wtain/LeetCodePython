from typing import List


def matrix_size(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    return len(matrix) * len(matrix[0])


def matrix_test_metric(test) -> int:
    return matrix_size(test[0])