"""
https://leetcode.com/problems/maximum-total-importance-of-roads/description/?envType=daily-question&envId=2024-06-28

You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the values optimally.



Example 1:


Input: n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 43
Explanation: The figure above shows the country and the assigned values of [2,4,5,3,1].
- The road (0,1) has an importance of 2 + 4 = 6.
- The road (1,2) has an importance of 4 + 5 = 9.
- The road (2,3) has an importance of 5 + 3 = 8.
- The road (0,2) has an importance of 2 + 5 = 7.
- The road (1,3) has an importance of 4 + 3 = 7.
- The road (2,4) has an importance of 5 + 1 = 6.
The total importance of all roads is 6 + 9 + 8 + 7 + 7 + 6 = 43.
It can be shown that we cannot obtain a greater total importance than 43.
Example 2:


Input: n = 5, roads = [[0,3],[2,4],[1,3]]
Output: 20
Explanation: The figure above shows the country and the assigned values of [4,3,2,5,1].
- The road (0,3) has an importance of 4 + 5 = 9.
- The road (2,4) has an importance of 2 + 1 = 3.
- The road (1,3) has an importance of 3 + 5 = 8.
The total importance of all roads is 9 + 3 + 8 = 20.
It can be shown that we cannot obtain a greater total importance than 20.


Constraints:

2 <= n <= 5 * 104
1 <= roads.length <= 5 * 104
roads[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no duplicate roads.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1290
# ms
# Beats
# 35.25%
# Analyze Complexity
# Memory
# 45.55
# MB
# Beats
# 9.02%
# class Solution:
#     def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
#         degree = [0] * n
#         for a, b in roads:
#             degree[a] += 1
#             degree[b] += 1
#         degree = list((d, i) for i, d in enumerate(degree))
#         degree.sort()
#         importance = {}
#         for i in range(n):
#             importance[degree[i][1]] = i+1
#         total = 0
#         for a, b in roads:
#             total += importance[a]
#             total += importance[b]
#         return total


# Runtime
# 1193
# ms
# Beats
# 86.48%
# Analyze Complexity
# Memory
# 42.02
# MB
# Beats
# 60.66%
# https://leetcode.com/problems/maximum-total-importance-of-roads/editorial/?envType=daily-question&envId=2024-06-28
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        value, total = 1, 0
        for d in degree:
            total += value * d
            value += 1
        return total


tests = [
    [5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]], 43],
    [5, [[0,3],[2,4],[1,3]],20],
]

run_functional_tests(Solution().maximumImportance, tests)
