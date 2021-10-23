"""
https://leetcode.com/problems/guess-number-higher-or-lower/
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
from Common.ObjectTestingUtils import run_functional_tests


def guess(num: int) -> int:
    if num > 6:
        return -1
    if num < 6:
        return 1
    return 0


"""
Runtime: 32 ms, faster than 56.25% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 13.8 MB, less than 63.88% of Python3 online submissions for Guess Number Higher or Lower.
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n+1
        while l < r:
            m = l + (r-l) // 2
            c = guess(m)
            if c == -1:
                r = m
            elif c == 1:
                l = m+1
            else:
                return m
        return l


run_functional_tests(Solution().guessNumber, [
    [10, 6]
])
