"""
https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

Number Of Rectangles That Can Form The Largest Square

You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.



Example 1:

Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.
Example 2:

Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3


Constraints:

1 <= rectangles.length <= 1000
rectangles[i].length == 2
1 <= li, wi <= 109
li != wi
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 188 ms, faster than 51.96% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
# Memory Usage: 15 MB, less than 39.87% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
# class Solution:
#     def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
#         squares = [min(l, w) for l, w in rectangles]
#         side = max(squares)
#         return sum([side == sz for sz in squares])


# Runtime: 632 ms, faster than 5.17% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
# Memory Usage: 14.8 MB, less than 68.37% of Python3 online submissions for Number Of Rectangles That Can Form The Largest Square.
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = [min(l, w) for l, w in rectangles]
        return sum([max(squares) == sz for sz in squares])


tests = [
    [[[5,8],[3,9],[5,12],[16,5]], 3],
    [[[2,3],[3,7],[4,3],[3,7]], 3]
]

run_functional_tests(Solution().countGoodRectangles, tests)