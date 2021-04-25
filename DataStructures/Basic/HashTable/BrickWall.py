"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3717/
https://leetcode.com/problems/brick-wall/

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.



Example:

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

Explanation:



Note:

The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.
"""
from collections import Counter
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 188 ms, faster than 38.48% of Python3 online submissions for Brick Wall.
# Memory Usage: 19.1 MB, less than 62.64% of Python3 online submissions for Brick Wall.
# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         d = {}
#         for row in wall:
#             pos = 0
#             for brick in row:
#                 pos += brick
#                 d[pos] = d.get(pos, 0) + 1
#         return len(wall) - (max([d[k] for k in sorted(d.keys())][:-1]) if len(d) > 1 else 0)


# Runtime: 188 ms, faster than 38.48% of Python3 online submissions for Brick Wall.
# Memory Usage: 19.1 MB, less than 62.64% of Python3 online submissions for Brick Wall.
# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         d = {}
#         max_pos = 0
#         for row in wall:
#             pos = 0
#             for brick in row:
#                 pos += brick
#                 d[pos] = d.get(pos, 0) + 1
#             max_pos = max(max_pos, pos)
#         d[max_pos] = 0
#         return len(wall) - max([v for v in d.values()])


# Runtime: 196 ms, faster than 20.13% of Python3 online submissions for Brick Wall.
# Memory Usage: 19 MB, less than 86.13% of Python3 online submissions for Brick Wall.
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        c = Counter()
        for row in wall:
            for brick in accumulate(row[:-1]):
                c[brick] += 1
        return len(wall) - max(c.values()) if c else len(wall)


tests = [
    [
        [[1,1],[2],[1,1]],
        1
    ],
    [
        [[1],[1],[1]],
        3
    ],
    [
        [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]],
        2
    ]
]

run_functional_tests(Solution().leastBricks, tests)