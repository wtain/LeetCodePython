"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3918/
https://leetcode.com/problems/sum-of-square-numbers/

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.



Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
Example 3:

Input: c = 4
Output: true
Example 4:

Input: c = 2
Output: true
Example 5:

Input: c = 1
Output: true


Constraints:

0 <= c <= 231 - 1
"""

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 372 ms, faster than 29.65% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 14.2 MB, less than 51.88% of Python3 online submissions for Sum of Square Numbers.
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         if not c:
#             return True
#         for i in range(c):
#             a = i ** 2
#             if a > c:
#                 return False
#             b = c - a
#             bs = int(math.sqrt(b))
#             if bs ** 2 == b:
#                 return True
#         return False


# Runtime: 6172 ms, faster than 5.02% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 14 MB, less than 98.52% of Python3 online submissions for Sum of Square Numbers.
# https://leetcode.com/problems/sum-of-square-numbers/solution/
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#
#         def binsearch(s: int, e: int, n: int) -> bool:
#             while s <= e:
#                 mid = s + (e-s) // 2
#                 mid2 = mid ** 2
#                 if mid2 == n:
#                     return True
#                 if mid2 > n:
#                     e = mid-1
#                 else:
#                     s = mid+1
#             return False
#
#         if not c:
#             return True
#         for i in range(c+1):
#             a = i ** 2
#             if a > c:
#                 return False
#             b = c - a
#             if binsearch(0, b, b):
#                 return True
#         return False


# Runtime: 44 ms, faster than 99.20% of Python3 online submissions for Sum of Square Numbers.
# Memory Usage: 14.2 MB, less than 74.34% of Python3 online submissions for Sum of Square Numbers.
# https://leetcode.com/problems/sum-of-square-numbers/solution/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if not c:
            return True
        i = 2
        while i**2 <= c:
            cnt = 0
            if c % i == 0:
                while c % i == 0:
                    cnt += 1
                    c //= i
                if i % 4 == 3 and cnt % 2:
                    return False
            i += 1

        return c % 4 != 3


tests = [
    [6, False],
    [5, True],
    [3, False],
    [4, True],
    [2, True],
    [1, True]
]

run_functional_tests(Solution().judgeSquareSum, tests)