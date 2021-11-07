"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 40 ms, faster than 43.48% of Python3 online submissions for Happy Number.
Memory Usage: 13.9 MB, less than 35.85% of Python3 online submissions for Happy Number.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNum(n: int):
            res = 0
            while n > 0:
                d = n % 10
                n //= 10
                res += d**2
            return res
        p1 = nextNum(n)
        if p1 == 1:
            return True
        p2 = nextNum(p1)
        if p2 == 1:
            return True
        while p1 != p2:
            p1 = nextNum(p1)
            p2 = nextNum(p2)
            p2 = nextNum(p2)
            if p2 == 1:
                return True
        return False


tests = [
    [19, True]
]

run_functional_tests(Solution().isHappy, tests)

