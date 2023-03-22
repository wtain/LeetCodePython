"""
https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.


Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.


Constraints:

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         dist = [[0] * n for _ in range(n)]
#         for a, b, d in roads:
#             dist[a][b] = dist[b][a] = d
#         distances = [[0] * n for _ in range(n)]
#         level = [0]
#         while level:
#             next_level = []
#             level = next_level
#         return distances[0][-1]


# Runtime
# 8742 ms
# Beats
# 5.3%
# Memory
# 58.6 MB
# Beats
# 96.31%
# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         BigValue = float('inf')
#         p, rank = list(range(n)), [BigValue] * n
#
#         def get(i):
#             while i != p[i]:
#                 i = p[i]
#             return i
#
#         def connect(i, j, dist):
#             i, j = get(i), get(j)
#             p[i] = j
#             rank[i] = rank[j] = min(rank[i], rank[j], dist)
#
#         for a, b, d in roads:
#             connect(a-1, b-1, d)
#
#         return rank[get(0)]

# TLE
# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         BigValue = float('inf')
#         p, rank = list(range(n)), [BigValue] * n
#
#         def get(i):
#             while i != p[i]:
#                 i = p[i]
#             return i
#
#         def connect(i, j, dist):
#             i, j = get(i), get(j)
#             p[j] = i
#             rank[i] = rank[j] = min(rank[i], rank[j], dist)
#
#         for a, b, d in roads:
#             connect(a-1, b-1, d)
#
#         return rank[get(0)]


# Runtime
# 8996 ms
# Beats
# 5.3%
# Memory
# 58.7 MB
# Beats
# 96.31%
# class Solution:
#     def minScore(self, n: int, roads: List[List[int]]) -> int:
#         BigValue = float('inf')
#         p, rank = list(range(n)), [BigValue] * n
#
#         def get(i):
#             while i != p[i]:
#                 i = p[i]
#             return i
#
#         def connect(i, j, dist):
#             i, j = get(i), get(j)
#             p[i] = j
#             rank[i] = rank[j] = min(rank[i], rank[j], dist)
#
#         for a, b, d in roads:
#             connect(a-1, b-1, d)
#
#         return rank[get(0)]


# Runtime
# 1603 ms
# Beats
# 95.64%
# Memory
# 58.7 MB
# Beats
# 87.58%
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        BigValue = float('inf')
        p, rank = list(range(n)), [BigValue] * n

        def get(i):
            while i != p[i]:
                i = p[i]
            return i

        def connect(i, j, dist):
            i, j = get(i), get(j)
            p[min(i, j)] = max(i, j)
            rank[i] = rank[j] = min(rank[i], rank[j], dist)

        for a, b, d in roads:
            connect(a-1, b-1, d)

        return rank[get(0)]


tests = [
    [4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]], 5],
    [4, [[1,2,2],[1,3,4],[3,4,7]], 2],
]

run_functional_tests(Solution().minScore, tests)
