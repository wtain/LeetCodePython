"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3874/
https://leetcode.com/problems/rank-transform-of-a-matrix/

Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

The rank is an integer starting from 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.



Example 1:


Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
Example 2:


Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]
Example 3:


Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
Example 4:


Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
Output: [[5,1,4],[1,2,3],[6,3,1]]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
-109 <= matrix[row][col] <= 109

Hints
Sort the cells by value and process them in increasing order.
The rank of a cell is the maximum rank in its row and column plus one.
Handle the equal cells by treating them as components using a union-find data structure.
"""
import itertools
from collections import defaultdict
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         result = [[0] * m for _ in range(n)]
#         cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
#         rows = [0] * n
#         cols = [0] * m
#         vprev, rankprev = None, None
#         for v, i, j in cells:
#             if v == vprev:
#                 rank = rankprev
#             else:
#                 rank = max(rows[i], cols[j]) + 1
#             rows[i] = cols[j] = rank
#             result[i][j] = rank
#             vprev, rankprev = v, rank
#         return result

# WRONG
# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         result = [[0] * m for _ in range(n)]
#         cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
#         rows = [0] * n
#         cols = [0] * m
#
#         for v, g in itertools.groupby(cells, lambda x: x[0]):
#             rank = 0
#             g = list(g)
#             for v, i, j in g:
#                 rank_i = max(rows[i], cols[j]) + 1
#                 rank = max(rank, rank_i)
#
#             for v, i, j in g:
#                 rows[i] = cols[j] = rank
#                 result[i][j] = rank
#         return result



# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         result = [[0] * m for _ in range(n)]
#         cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
#         rows, cols = [0] * n, [0] * m
#
#         def group(cells):
#             return itertools.groupby(cells, lambda x: x[0])
#
#         for v, g in group(cells):
#             rank = 0
#             g = list(g)
#             for v, i, j in g:
#                 rank_i = max(rows[i], cols[j]) + 1
#                 rank = max(rank, rank_i)
#
#             for v, i, j in g:
#                 rows[i] = cols[j] = rank
#                 result[i][j] = rank
#         return result


# WRONG
# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         result = [[0] * m for _ in range(n)]
#         cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
#         rows, cols = [0] * n, [0] * m
#
#         def group(cells):
#             groups = defaultdict(list)
#             for v, i, j in cells:
#                 groups_v = groups[v]
#                 added = False
#                 for _, g_i, g_j in groups_v:
#                     if i in g_i:
#                         g_j.add(j)
#                         added = True
#                         break
#                     if j in g_j:
#                         g_i.add(i)
#                         added = True
#                         break
#                 if not added:
#                     groups_v.append((v, set([i]), set([j])))
#             return [(v, groups[v]) for v in groups]
#
#         groups = group(cells)
#
#         for v, g in groups:
#
#             for v, si, sj in g:
#                 rank = 0
#                 for i, j in product(si, sj):
#                     rank_i = max(rows[i], cols[j]) + 1
#                     rank = max(rank, rank_i)
#                 for i, j in product(si, sj):
#                     rows[i] = cols[j] = rank
#                     result[i][j] = rank
#
#         return result


# TLE
# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         result = [[0] * m for _ in range(n)]
#         cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
#         rows, cols = [0] * n, [0] * m
#
#         def group(cells):
#             return itertools.groupby(cells, lambda x: x[0])
#
#         groups = group(cells)
#
#         for v, g in groups:
#             g = list(g)
#             cnt = len(g)
#
#             parent = list(range(cnt))
#             rnk = [0] * cnt
#
#             def find(i: int) -> int:
#                 while parent[i] != i:
#                     i = parent[i]
#                 return i
#
#             def union(i: int, j: int):
#                 i, j = find(i), find(j)
#                 if i == j:
#                     return
#                 if rnk[i] < rnk[j]:
#                     parent[i] = j
#                 elif rnk[i] > rnk[j]:
#                     parent[j] = i
#                 else:
#                     parent[j] = i
#                     rnk[i] += 1
#
#             for gi in range(cnt):
#                 _, gi1, gj1 = g[gi]
#                 for gj in range(gi+1, cnt):
#                     _, gi2, gj2 = g[gj]
#                     if gi1 == gi2 or gj1 == gj2:
#                         union(gi, gj)
#             groups_clustered = defaultdict(list)
#             for gi in range(cnt):
#                 _, gi1, gj1 = g[gi]
#                 group_index = find(gi)
#                 groups_clustered[group_index].append((gi1, gj1))
#             for k in groups_clustered:
#                 idx_pairs = groups_clustered[k]
#                 si = set(i for i, j in idx_pairs)
#                 sj = set(j for i, j in idx_pairs)
#
#                 rank = 0
#                 for i, j in product(si, sj):
#                     rank_i = max(rows[i], cols[j]) + 1
#                     rank = max(rank, rank_i)
#                 for i, j in idx_pairs:
#                     rows[i] = cols[j] = rank
#                     result[i][j] = rank
#
#         return result
from DataStructures.Advanced.Graph.UnionFind.RankTransformOfAMatrix_test_case_huge1 import input_matrix


# Runtime: 2208 ms, faster than 52.87% of Python3 online submissions for Rank Transform of a Matrix.
# Memory Usage: 66.1 MB, less than 37.93% of Python3 online submissions for Rank Transform of a Matrix.
# class Solution:
#     def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
#         n, m = len(matrix), len(matrix[0])
#         result = [[0] * m for _ in range(n)]
#         # N*M*LOG(N*M)
#         # print("Sorting")
#         cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
#         # print("Done")
#         rows, cols = [0] * n, [0] * m
#
#         def group(cells):
#             return itertools.groupby(cells, lambda x: x[0])
#
#         # N*M
#         # print("Grouping")
#         groups = group(cells)
#         # print("Done")
#
#         # print("Main loop")
#         for v, g in groups:
#             g = list(g)
#             cnt = len(g)
#             # print(cnt)
#
#             parent = list(range(cnt))
#             rnk = [0] * cnt
#
#             def find(i: int) -> int:
#                 while parent[i] != i:
#                     i = parent[i]
#                 return i
#
#             def union(i: int, j: int):
#                 i, j = find(i), find(j)
#                 if i == j:
#                     return
#                 if rnk[i] < rnk[j]:
#                     parent[i] = j
#                 elif rnk[i] > rnk[j]:
#                     parent[j] = i
#                 else:
#                     parent[j] = i
#                     rnk[i] += 1
#
#             rr, cc = [-1] * n, [-1] * m
#
#             for gi in range(cnt):
#                 _, gi1, gj1 = g[gi]
#                 if rr[gi1] != -1:
#                     union(gi, rr[gi1])
#                 if cc[gj1] != -1:
#                     union(gi, cc[gj1])
#                 rr[gi1] = cc[gj1] = gi
#
#             # for gi in range(cnt):
#             #     _, gi1, gj1 = g[gi]
#             #     for gj in range(gi+1, cnt):
#             #         _, gi2, gj2 = g[gj]
#             #         if gi1 == gi2 or gj1 == gj2:
#             #             union(gi, gj)
#
#             groups_clustered = defaultdict(list)
#             for gi in range(cnt):
#                 _, gi1, gj1 = g[gi]
#                 group_index = find(gi)
#                 groups_clustered[group_index].append((gi1, gj1))
#             for k in groups_clustered:
#                 idx_pairs = groups_clustered[k]
#
#                 rank = 0
#                 for i, j in idx_pairs:
#                     rank_i = max(rows[i], cols[j]) + 1
#                     rank = max(rank, rank_i)
#                 for i, j in idx_pairs:
#                     rows[i] = cols[j] = rank
#                     result[i][j] = rank
#
#         return result


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        result = [[0] * m for _ in range(n)]
        # Sort matrix values and store indices
        cells = sorted([(matrix[i][j], i, j) for i, j in product(range(n), range(m))])
        rows, cols = [0] * n, [0] * m

        def group(cells):
            return itertools.groupby(cells, lambda x: x[0])

        # Group cells by values
        groups = group(cells)

        # Iterating through cell groups having the same value
        for v, g in groups:
            g = list(g)
            cnt = len(g)

            # Union-find structure
            parent = list(range(cnt))
            rnk = [0] * cnt

            def find(i: int) -> int:
                while parent[i] != i:
                    i = parent[i]
                return i

            def union(i: int, j: int):
                i, j = find(i), find(j)
                if i == j:
                    return
                if rnk[i] < rnk[j]:
                    parent[i] = j
                elif rnk[i] > rnk[j]:
                    parent[j] = i
                else:
                    parent[j] = i
                    rnk[i] += 1

            # Finding cell groups intersections by row or column
            rr, cc = [-1] * n, [-1] * m

            for gi in range(cnt):
                _, gi1, gj1 = g[gi]
                # If there is a group covering the same row, unite them
                if rr[gi1] != -1:
                    union(gi, rr[gi1])
                # If there is a group covering the same column, unite them
                if cc[gj1] != -1:
                    union(gi, cc[gj1])
                # Update rows and columns trackers with current group index
                rr[gi1] = cc[gj1] = gi

            # Clusterize groups using Union-Find structure built on previous step
            groups_clustered = defaultdict(list)
            for gi in range(cnt):
                _, gi1, gj1 = g[gi]
                group_index = find(gi)
                groups_clustered[group_index].append((gi1, gj1))
            # Going through value clusters
            for k in groups_clustered:
                idx_pairs = groups_clustered[k]
                # In each cluster find maximum rank value
                rank = 0
                for i, j in idx_pairs:
                    rank_i = max(rows[i], cols[j])
                    rank = max(rank, rank_i)
                rank += 1
                # Update occupied rows and columns along with the result
                for i, j in idx_pairs:
                    rows[i] = cols[j] = rank
                    result[i][j] = rank

        return result


tests = [
    [
        input_matrix,
        []
    ],
    [
        [
            [-5,-42,-39,-44,31,-46,13,-48,-5,30,1,48],
            [31,42,33,-44,-5,14,-47,48,7,-34,-19,-20],
            [11,2,37,24,39,-6,-27,20,-1,14,5,8],
            [7,38,29,-28,-1,10,13,12,3,26,9,16],
            [-49,38,-47,40,35,-42,-43,-8,-21,22,-39,-8],
            [-17,-38,-15,24,-41,-46,-19,16,3,-42,-39,24],
            [-9,-14,37,-40,-9,26,17,-28,3,38,-15,-28],
            [-21,-34,1,36,-37,18,25,16,39,6,-3,-20],
            [-9,46,25,24,-45,-26,-39,-16,-29,-2,-35,28],
            [43,18,37,4,-49,18,37,24,-9,-46,49,48],
            [43,-46,-39,-8,35,26,49,48,-29,-42,5,-44],
            [-5,18,9,-20,35,-18,-47,-4,-5,-14,-47,44]
        ],
        [
            [14,4,5,3,25,2,21,1,14,24,15,29],
            [21,28,26,3,14,20,1,29,17,4,10,9],
            [19,16,27,23,28,10,5,22,15,20,17,18],
            [17,27,25,5,15,19,21,20,16,23,18,22],
            [1,27,2,28,26,4,3,10,8,21,5,10],
            [9,6,10,23,4,2,7,21,16,3,5,23],
            [13,12,27,4,13,23,22,5,16,28,11,5],
            [8,7,13,24,5,22,23,21,25,15,12,9],
            [13,29,24,23,2,8,4,9,7,14,6,25],
            [28,22,27,10,1,22,27,23,9,2,30,29],
            [28,1,5,8,26,23,30,29,7,3,17,2],
            [14,22,16,6,26,9,1,15,14,10,1,27]
        ]
    ],
    [
        [
            [-24,-9,-14,-15,44,31,-46,5,20,-5,34],
            [9,-40,-49,-50,17,40,35,30,-39,36,-49],
            [-18,-43,-40,-5,-30,9,-28,-41,-6,-47,12],
            [11,42,-23,20,35,34,-39,-16,27,34,-15],
            [32,27,-30,29,-48,15,-50,-47,-28,-21,38],
            [45,48,-1,-18,9,-4,-13,10,9,8,-41],
            [-42,-35,20,-17,10,5,36,47,6,1,8],
            [3,-50,-23,16,31,2,-39,36,-25,-30,37],
            [-48,-41,18,-31,-48,-1,-42,-3,-8,-29,-2],
            [17,0,31,-30,-43,-20,-37,-6,-43,8,19],
            [42,25,32,27,-2,45,12,-9,34,17,32]
        ],
        [
            [4,11,10,9,25,21,2,14,20,12,24],
            [18,5,2,1,21,25,23,22,6,24,2],
            [8,2,5,11,6,18,7,4,10,1,20],
            [19,24,9,20,23,22,4,10,21,22,11],
            [23,20,6,22,2,19,1,3,7,8,26],
            [26,27,11,7,19,9,8,20,19,14,3],
            [3,6,21,8,20,17,24,25,18,13,19],
            [17,1,9,18,22,16,4,23,8,5,25],
            [2,4,16,5,2,15,3,13,9,6,14],
            [20,13,22,6,3,7,5,12,3,14,21],
            [25,16,23,21,12,26,13,11,24,15,23]
        ]
    ],
    [
        [
            [-37,-26,-47,-40,-13],
            [22,-11,-44,47,-6],
            [-35,8,-45,34,-31],
            [-16,23,-6,-43,-20],
            [47,38,-27,-8,43]
        ],
        [
            [3,4,1,2,7],
            [9,5,3,10,8],
            [4,6,2,7,5],
            [7,9,8,1,6],
            [12,10,4,5,11]
        ]
    ],
    [
        [
            [-37,-50,-3,44],
            [-37,46,13,-32],
            [47,-42,-3,-40],
            [-17,-22,-39,24]
        ],
        [
            [2,1,4,6],
            [2,6,5,4],
            [5,2,4,3],
            [4,3,1,5]
        ]
    ],
    [
        [
            [1,2],
            [3,4]
        ],
        [
            [1,2],
            [2,3]
        ]
    ],
    [
        [
            [7,7],
            [7,7]
        ],
        [
            [1,1],
            [1,1]
        ]
    ],
    [
        [
            [20,-21,14],
            [-19,4,19],
            [22,-47,24],
            [-19,4,19]
        ],
        [
            [4,2,3],
            [1,3,4],
            [5,1,6],
            [1,3,4]
        ]
    ],
    [
        [
            [7,3,6],
            [1,4,5],
            [9,8,2]
        ],
        [
            [5,1,4],
            [1,2,3],
            [6,3,1]
        ]
    ]
]

run_functional_tests(Solution().matrixRankTransform, tests)
# run_functional_tests(Solution().matrixRankTransform, tests, run_tests=[6])
