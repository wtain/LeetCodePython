"""
https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

You are given two integer arrays nums and multipliers of size n and m respectively, where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the ith operation (1-indexed), you will:

Choose one integer x from either the start or the end of the array nums.
Add multipliers[i] * x to your score.
Remove x from the array nums.
Return the maximum score after performing m operations.



Example 1:

Input: nums = [1,2,3], multipliers = [3,2,1]
Output: 14
Explanation: An optimal solution is as follows:
- Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
- Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
- Choose from the end, [1], adding 1 * 1 = 1 to the score.
The total score is 9 + 4 + 1 = 14.
Example 2:

Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
Output: 102
Explanation: An optimal solution is as follows:
- Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the score.
- Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
- Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
- Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
- Choose from the end, [-2,7], adding 7 * 6 = 42 to the score.
The total score is 50 + 15 - 9 + 4 + 42 = 102.


Constraints:

n == nums.length
m == multipliers.length
1 <= m <= 103
m <= n <= 105
-1000 <= nums[i], multipliers[i] <= 1000

At first glance, the solution seems to be greedy, but if you try to greedily take the largest value from the beginning or the end, this will not be optimal.

You should try all scenarios but this will be costy.

Memoizing the pre-visited states while trying all the possible scenarios will reduce the complexity, and hence dp is a perfect choice here.
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# 1) PASS, took: 0.000063 on size=3
# 2) PASS, took: 0.000245 on size=6
# 3) PASS, took: 24.355828 on size=50
# MLE/TLE
# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#
#         @lru_cache(None)
#         def dp(i1: int, i2: int, j: int, v: int) -> int:
#             if j == len(multipliers):
#                 return v
#             return max(dp(i1+1, i2, j+1, v+nums[i1]*multipliers[j]),
#                        dp(i1, i2-1, j+1, v+nums[i2]*multipliers[j]))
#
#         return dp(0, len(nums)-1, 0, 0)


# 1) PASS, took: 0.000052 on size=3
# 2) PASS, took: 0.000163 on size=6
# 3) PASS, took: 0.000332 on size=50
# MLE
# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#
#         @lru_cache(None)
#         def dp(i1: int, i2: int, j: int) -> int:
#             if j == len(multipliers):
#                 return 0
#             return max(nums[i1]*multipliers[j]+dp(i1+1, i2, j+1),
#                        nums[i2]*multipliers[j]+dp(i1, i2-1, j+1))
#
#         return dp(0, len(nums)-1, 0)

# INCOMPLETE
# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#
#         n, m = len(nums), len(multipliers)
#         dp = [[0] * n for _ in range(n)]
#
#         d = n - m
#         for i in range(n-d):
#             dp[i][i+d] =
#
#         for j in range(m):
#
#         return dp[0][n-1]


# Runtime: 9794 ms, faster than 5.03% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
# Memory Usage: 41.1 MB, less than 47.52% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/solution/
# class Solution:
#     def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
#
#         n, m = len(nums), len(multipliers)
#         dp = [[0] * (m+1) for _ in range(m+1)]
#
#         for op in range(m-1,-1,-1):
#             for left in range(op, -1, -1):
#                 dp[op][left] = max(multipliers[op] * nums[left] + dp[op+1][left+1],
#                                    multipliers[op] * nums[n-1 - (op - left)] + dp[op+1][left])
#
#         return dp[0][0]


# Runtime: 7117 ms, faster than 69.52% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
# Memory Usage: 23.2 MB, less than 97.48% of Python3 online submissions for Maximum Score from Performing Multiplication Operations.
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

        n, m = len(nums), len(multipliers)
        dp = [0] * (m+1)

        for op in range(m-1,-1,-1):
            next_row = dp.copy()
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left+1],
                             multipliers[op] * nums[n-1 - (op - left)] + next_row[left])

        return dp[0]


tests = [
    [[1,2,3], [3,2,1], 14],
    [[-5,-3,-3,-2,7,1], [-10,-5,3,4,6], 102],

    [[555,526,732,182,43,-537,-434,-233,-947,968,-250,-10,470,-867,-809,-987,120,607,-700,25,-349,-657,349,-75,-936,-473,615,691,-261,-517,-867,527,782,939,-465,12,988,-78,-990,504,-358,491,805,756,-218,513,-928,579,678,10], [783,911,820,37,466,-251,286,-74,-899,586,792,-643,-969,-267,121,-656,381,871,762,-355,721,753,-521], 6861161],


]

run_functional_tests(Solution().maximumScore, tests)
