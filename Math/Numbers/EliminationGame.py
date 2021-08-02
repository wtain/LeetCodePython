"""
https://leetcode.com/problems/elimination-game/

You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
Given the integer n, return the last number that remains in arr.



Example 1:

Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 109
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 40 ms, faster than 83.84% of Python3 online submissions for Elimination Game.
# Memory Usage: 14.3 MB, less than 52.19% of Python3 online submissions for Elimination Game.
# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         steps = int(math.log2(n))
#         mul, a1, d, cnt = 1, 1, 1, n
#
#         # def dbg_print():
#         #     nonlocal mul, a1, d, cnt
#         #     print(sorted([a1 + v * d for v in range(cnt)]))
#
#         # dbg_print()
#         for s in range(steps):
#             mul *= 2
#             cnt //= 2
#             a1 += d + 2 * d * (cnt-1)
#             d *= -2
#             # dbg_print()
#         return a1


# Runtime: 72 ms, faster than 7.07% of Python3 online submissions for Elimination Game.
# Memory Usage: 14.4 MB, less than 21.21% of Python3 online submissions for Elimination Game.
class Solution:
    def lastRemaining(self, n: int) -> int:
        iterations = int(math.log2(n))
        a1, step, cnt = 1, 1, n
        for _ in range(iterations):
            cnt //= 2
            a1 += step + 2 * step * (cnt-1)
            step *= -2
        return a1


tests = [
    [9, 6],
    [1, 1]
]

run_functional_tests(Solution().lastRemaining, tests)