"""
https://leetcode.com/problems/can-i-win/

In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.

Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.



Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true
Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true


Constraints:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300
"""
from functools import lru_cache

import Common
from Common import ObjectTestingUtils


# WRONG
# class Solution:
#     def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
#         N = 1 << maxChoosableInteger-1
#
#         @lru_cache(200000)
#         def dp(mask: int, total: int) -> bool:
#             nonlocal maxChoosableInteger
#             for i in range(1, maxChoosableInteger+1):
#                 bit = 1 << (i-1)
#                 if bit & mask:
#                     continue
#                 if total - i <= 0:
#                     return True
#                 if not dp(mask | bit, total - i):
#                     return True
#             return False
#
#         return dp(0, desiredTotal)


# Runtime: 3892 ms, faster than 74.24% of Python3 online submissions for Can I Win.
# Memory Usage: 194.4 MB, less than 24.05% of Python3 online submissions for Can I Win.
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        N = 1 << maxChoosableInteger-1

        if (maxChoosableInteger + 1) * maxChoosableInteger // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def dp(mask: int, total: int) -> bool:
            nonlocal maxChoosableInteger

            if total <= 0 and mask:
                return False

            for i in range(1, maxChoosableInteger+1):
                bit = 1 << (i-1)
                if bit & mask:
                    continue
                if total - i <= 0:
                    return True
                if not dp(mask | bit, total - i):
                    return True
            return False

        return dp(0, desiredTotal)


tests = [
    [20, 152, False],
    [5, 50, False],
    [20, 100, True],
    [10, 11, False],
    [10, 0, True],
    [10, 1, True]
]

ObjectTestingUtils.run_functional_tests(Solution().canIWin, tests)
