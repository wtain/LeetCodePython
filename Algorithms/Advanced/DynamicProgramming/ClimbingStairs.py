"""
https://leetcode.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 44 ms, faster than 15.79% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 42.91% of Python3 online submissions for Climbing Stairs.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        c1 = 1
        c2 = 2
        for i in range(3, n+1):
            res = c1 + c2
            c1 = c2
            c2 = res

        return c2


tests = [
    [2, 2],
    [3, 3],
    [10, 89],
    [45, 1836311903]
]

run_functional_tests(Solution().climbStairs, tests)
