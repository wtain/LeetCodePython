"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3766/
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.



Example 1:



Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:



Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9


Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 368 ms, faster than 6.94% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 33.5 MB, less than 5.19% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# class Solution:
#     def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
#         horizontalCuts = [0] + sorted(horizontalCuts) + [h]
#         verticalCuts = [0] + sorted(verticalCuts) + [w]
#         l1s = [x-y for x,y in zip(horizontalCuts[1:], horizontalCuts)]
#         l2s = [x - y for x, y in zip(verticalCuts[1:], verticalCuts)]
#         MOD = 10**9 + 7
#         return (max(l1s) % MOD) * (max(l2s) % MOD) % MOD


# Runtime: 424 ms, faster than 5.19% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
# Memory Usage: 27.1 MB, less than 75.60% of Python3 online submissions for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts.
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        def max_diff(arr: List[int]) -> int:
            max_diff = 0
            for i in range(1, len(arr)):
                max_diff = max(max_diff, arr[i] - arr[i-1])
            return max_diff

        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        MOD = 10**9 + 7
        return (max_diff(horizontalCuts) % MOD) * (max_diff(verticalCuts) % MOD) % MOD


tests = [
    [5, 4, [1,2,4], [1,3], 4],
    [5, 4, [3,1], [1], 6],
    [5, 4, [3], [3], 9]
]

run_functional_tests(Solution().maxArea, tests)