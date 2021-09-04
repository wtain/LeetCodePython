"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.



Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10


Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104


Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
"""
import sys
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 59.65% of Python3 online submissions for Triangle.
# Memory Usage: 15.2 MB, less than 26.73% of Python3 online submissions for Triangle.
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         prevLevel = [triangle[0][0]]
#         min_cost = prevLevel[0]
#         for level in range(1, len(triangle)):
#             level_size = len(triangle[level])
#             current_level = [0] * level_size
#             min_cost = sys.maxsize
#             for i in range(level_size):
#                 min_cost_i = sys.maxsize
#                 if i > 0:
#                     min_cost_i = prevLevel[i-1]
#                 if i < level_size-1:
#                     min_cost_i = min(min_cost_i, prevLevel[i])
#                 current_level[i] = triangle[level][i] + min_cost_i
#                 min_cost = min(current_level[i], min_cost)
#             prevLevel = current_level
#         return min_cost

# Runtime: 52 ms, faster than 94.36% of Python3 online submissions for Triangle.
# Memory Usage: 15.2 MB, less than 26.73% of Python3 online submissions for Triangle
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_levels = len(triangle)
        for level in range(n_levels-2, -1, -1):
            for i in range(level+1):
                best_below = min(triangle[level+1][i], triangle[level+1][i+1])
                triangle[level][i] += best_below
        return triangle[0][0]


tests = [
    [
        [[2],[3,4],[6,5,7],[4,1,8,3]],
        11
    ],
    [
        [[-10]],
        -10
    ]
]

run_functional_tests(Solution().minimumTotal, tests)