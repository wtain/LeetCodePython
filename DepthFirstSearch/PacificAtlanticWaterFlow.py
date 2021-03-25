"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3684/
https://leetcode.com/problems/pacific-atlantic-water-flow/

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.


Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 3496 ms, faster than 5.00% of Python3 online submissions for Pacific Atlantic Water Flow.
# Memory Usage: 15.5 MB, less than 53.36% of Python3 online submissions for Pacific Atlantic Water Flow.
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        labels = [[0] * n for _ in range(m)]

        def markup(i: int, j: int, label_bit: int):
            nonlocal matrix, labels, n, m
            toVisit = [(i, j)]
            visited = set()

            def check_neighbour(p0, p1) -> bool:
                return 0 <= p1[0] < m and 0 <= p1[1] < n and matrix[p1[0]][p1[1]] >= matrix[p0[0]][p0[1]]

            while toVisit:
                p = toVisit.pop()
                labels[p[0]][p[1]] |= label_bit
                visited.add(p)
                p1 = (p[0] - 1, p[1])
                p2 = (p[0] + 1, p[1])
                p3 = (p[0], p[1] - 1)
                p4 = (p[0], p[1] + 1)
                if p1 not in visited and p1 not in toVisit and check_neighbour(p, p1):
                    toVisit.append(p1)
                if p2 not in visited and p2 not in toVisit and check_neighbour(p, p2):
                    toVisit.append(p2)
                if p3 not in visited and p3 not in toVisit and check_neighbour(p, p3):
                    toVisit.append(p3)
                if p4 not in visited and p4 not in toVisit and check_neighbour(p, p4):
                    toVisit.append(p4)

        for i in range(m):
            markup(i, 0, 1)
            markup(i, n-1, 2)
        for j in range(n):
            markup(0, j, 1)
            markup(m-1, j, 2)

        result = []

        for i in range(m):
            for j in range(n):
                if labels[i][j] == 3:
                    result.append([i, j])

        # print(labels)

        # return sorted(result)
        return result


tests = [
    ([], []),
    (
        [
           [1, 2, 2, 3, 5],
           [3, 2, 3, 4, 4],
           [2, 4, 5, 3, 1],
           [6, 7, 1, 4, 5],
           [5, 1, 1, 2, 4]
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    )
]

run_functional_tests(Solution().pacificAtlantic, tests)