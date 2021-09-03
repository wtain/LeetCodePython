"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3907/
https://leetcode.com/problems/rectangle-area-ii/

We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.



Example 1:


Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.


Constraints:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 109
The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# Runtime: 140 ms, faster than 16.58% of Python3 online submissions for Rectangle Area II.
# Memory Usage: 14.5 MB, less than 17.62% of Python3 online submissions for Rectangle Area II.
# https://leetcode.com/problems/rectangle-area-ii/solution/
# class Solution:
#     def rectangleArea(self, rectangles: List[List[int]]) -> int:
#         xvals, yvals = set(), set()
#         for rec in rectangles:
#             xvals.add(rec[0])
#             xvals.add(rec[2])
#             yvals.add(rec[1])
#             yvals.add(rec[3])
#
#         imapx, imapy = sorted(xvals), sorted(yvals)
#         mapx, mapy = {x: i for i, x in enumerate(imapx)}, {y: i for i, y in enumerate(imapy)}
#         m, n = len(imapx), len(imapy)
#         grid = [[False] * n for _ in range(m)]
#         for rec in rectangles:
#             for x in range(mapx[rec[0]], mapx[rec[2]]):
#                 for y in range(mapy[rec[1]], mapy[rec[3]]):
#                     grid[x][y] = True
#
#         result = 0
#         for x in range(m):
#             for y in range(n):
#                 if grid[x][y]:
#                     result += (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y])
#
#         return result % (10**9+7)


# Runtime: 56 ms, faster than 80.83% of Python3 online submissions for Rectangle Area II.
# Memory Usage: 14.1 MB, less than 99.48% of Python3 online submissions for Rectangle Area II.
# https://leetcode.com/problems/rectangle-area-ii/solution/
# class Solution:
#     def rectangleArea(self, rectangles: List[List[int]]) -> int:
#         OPEN, CLOSE = 0, 1
#         N = len(rectangles)
#         events = []
#         for rec in rectangles:
#             events.append([rec[1], OPEN, rec[0], rec[2]])
#             events.append([rec[3], CLOSE, rec[0], rec[2]])
#         events.sort()
#
#         active = []
#         cur_y, result = events[0][0], 0
#         for y, typ, x1, x2 in events:
#             query, cur = 0, -1
#             for xs in active:
#                 cur = max(cur, xs[0])
#                 query += max(xs[1] - cur, 0)
#                 cur = max(cur, xs[1])
#
#             result += query * (y - cur_y)
#
#             if typ == OPEN:
#                 active.append([x1, x2])
#                 active.sort()
#             else:
#                 for i, act in enumerate(active):
#                     if act[0] == x1 and act[1] == x2:
#                         del active[i]
#                         break
#
#             cur_y = y
#         return result % (10**9+7)


# Runtime: 88 ms, faster than 30.57% of Python3 online submissions for Rectangle Area II.
# Memory Usage: 14.5 MB, less than 34.72% of Python3 online submissions for Rectangle Area II.
# https://leetcode.com/problems/rectangle-area-ii/solution/
class Node:

    def __init__(self, start: int, end: int, X: List[int]):
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None
        self.X = X

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid, self.X)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end, self.X)
        return self._right

    def update(self, i: int, j: int, val: int) -> int:
        if i >= j:
            return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = self.X[self.end] - self.X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 1, -1
        events = []
        X = set()
        for x1, y1, x2, y2 in rectangles:
            if x1 < x2 and y1 < y2:
                events.append((y1, OPEN, x1, x2))
                events.append((y2, CLOSE, x1, x2))
                X.add(x1)
                X.add(x2)
        events.sort()
        X = sorted(X)
        x_index = {x: i for i, x in enumerate(X)}
        active = Node(0, len(X) - 1, X)
        ans = 0
        curr_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += curr_x_sum * (y - cur_y)
            curr_x_sum = active.update(x_index[x1], x_index[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)


tests = [
    [[[0,0,2,2],[1,0,2,3],[1,0,3,1]], 6],
    [[[0,0,1000000000,1000000000]], 49]
]

run_functional_tests(Solution().rectangleArea, tests)