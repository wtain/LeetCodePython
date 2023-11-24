"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/?envType=daily-question&envId=2023-11-24

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.



Example 1:

Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.
Example 2:

Input: piles = [2,4,5]
Output: 4
Example 3:

Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18


Constraints:

3 <= piles.length <= 105
piles.length % 3 == 0
1 <= piles[i] <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 511
# ms
# Beats
# 86.77%
# of users with Python3
# Memory
# 28.99
# MB
# Beats
# 8.93%
# of users with Python3
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        result = 0
        n = len(piles)
        i, j = 0, n-1
        while i < j:
            result += piles[j-1]
            j -= 2
            i += 1
        return result


tests = [
    [[2,4,1,2,7,8], 9],
    [[2,4,5], 4],
    [[9,8,7,6,5,1,2,3,4], 18],
]

run_functional_tests(Solution().maxCoins, tests)
