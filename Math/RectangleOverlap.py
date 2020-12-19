"""
https://leetcode.com/problems/rectangle-overlap/
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.



Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false


Constraints:

rect1.length == 4
rect2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1[0] <= rec1[2] and rec1[1] <= rec1[3]
rec2[0] <= rec2[2] and rec2[1] <= rec2[3]

Runtime: 32 ms, faster than 44.86% of Python3 online submissions for Rectangle Overlap.
Memory Usage: 14.4 MB, less than 5.82% of Python3 online submissions for Rectangle Overlap.
"""
from typing import List


# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
#         def isPointInRectangle(rect: List[int], x: int, y: int) -> bool:
#             x1 = rect[0]
#             y1 = rect[1]
#             x2 = rect[2]
#             y2 = rect[3]
#             return x1 < x < x2 and y1 < y < y2
#         x1 = rec2[0]
#         y1 = rec2[1]
#         x2 = rec2[2]
#         y2 = rec2[3]
#         if isPointInRectangle(rec1, x1, y1) or \
#            isPointInRectangle(rec1, x2, y1) or \
#            isPointInRectangle(rec1, x1, y2) or \
#            isPointInRectangle(rec1, x2, y2):
#             return True

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x1 = rec1[0]
        r1y1 = rec1[1]
        r1x2 = rec1[2]
        r1y2 = rec1[3]
        r2x1 = rec2[0]
        r2y1 = rec2[1]
        r2x2 = rec2[2]
        r2y2 = rec2[3]
        if r1x1 == r1x2 or r1y1 == r1y2 or \
           r2x1 == r2x2 or r2y1 == r2y2:
            return False
        return (r2x1 < r1x1 < r2x2 or r2x1 < r1x2 < r2x2 or r1x1 < r2x1 < r1x2 or r1x1 < r2x2 < r1x2) and \
               (r2y1 < r1y1 < r2y2 or r2y1 < r1y2 < r2y2 or r1y1 < r2y1 < r1y2 or r1y1 < r2y2 < r1y2)


tests = [
    ([-1,0,1,1], [0,-1,0,1], False),

    ([0,0,2,2], [1,1,3,3], True),
    ([0,0,1,1], [1,0,2,1], False),
    ([0,0,1,1], [2,2,3,3], False)
]

for test in tests:
    result = Solution().isRectangleOverlap(test[0], test[1])
    if result ^ test[2]:
        print("FAIL")
    else:
        print("PASS")