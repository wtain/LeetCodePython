import random
from typing import List


def random_matrix(n: int, m: int, a: int, b: int) -> List[List[int]]:
    mat = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j] = random.randint(a, b)
    return mat
