from typing import List

from Common.Helpers.ConsoleHelpers import colored


def matrix_size(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    return len(matrix) * len(matrix[0])


def matrix_test_metric(test) -> int:
    return matrix_size(test[0])


def matrix_values_test_metric(test, v) -> int:
    return sum(sum(1 for c in row if c == '.') for row in test[0])


def make_matrix_values_test_metric(v):
    return lambda test: matrix_values_test_metric(test, v)


def printMatrix(board, **kwargs):
    if "highlight" in kwargs:
        highlight = kwargs["highlight"]
    else:
        highlight = set()
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            text = board[i][j]
            if (i, j) in highlight:
                text = colored(0, 255, 0, text)
            print(text, flush=True, sep=' ', end=' ')
        print()


def printGrid(grid: List[List[int]]):
    for row in grid:
        print(row)
    print()
