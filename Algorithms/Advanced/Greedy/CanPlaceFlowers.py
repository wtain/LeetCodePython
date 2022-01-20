"""
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 210 ms, faster than 31.64% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 14.6 MB, less than 61.08% of Python3 online submissions for Can Place Flowers.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, cnt = 0, 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                i += 1
                cnt += 1
            if cnt >= n:
                return True
            i += 1
        return False


tests = [
    [[0,0,0,0,0,1,0,0], 0, True],
    [[1,0,0,0,1], 1, True],
    [[1,0,0,0,1], 2, False],
]


run_functional_tests(Solution().canPlaceFlowers, tests)
