"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3709/
https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:

0 <= n <= 30
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 94.81% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.1 MB, less than 89.39% of Python3 online submissions for Fibonacci Number.
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         a2, a1 = 0, 1
#         for i in range(n-1):
#             a2, a1 = a1, (a1+a2)
#         return a1

# Runtime: 28 ms, faster than 83.28% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 14.1 MB, less than 89.39% of Python3 online submissions for Fibonacci Number.
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a2, a1 = 0, 1
        for i in range(n-1):
            a2, a1 = a1, (a1+a2)
        return a1


tests = [
    [2, 1],
    [3, 2],
    [4, 3],
    [0, 0],
    [1, 1]
]

# for i in range(10):
#     print(Solution().fib(i))

run_functional_tests(Solution().fib, tests)