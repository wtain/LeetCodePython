"""
https://leetcode.com/problems/maximum-running-time-of-n-computers/description/

You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.



Example 1:


Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation:
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:


Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation:
Initially, insert battery 0 into the first computer and battery 2 into the second computer.
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer.
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.


Constraints:

1 <= n <= batteries.length <= 105
1 <= batteries[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 487ms
# Beats 100.00%of users with Python3
# Memory
# Details
# 30.88mb
# Beats 22.89%of users with Python3
# https://leetcode.com/problems/maximum-running-time-of-n-computers/editorial/
# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries.sort()
#         extra = sum(batteries[:-n])
#
#         live = batteries[-n:]
#         for i in range(n-1):
#             if extra // (i+1) < live[i+1] - live[i]:
#                 return live[i] + extra // (i+1)
#             extra -= (i+1) * (live[i+1] - live[i])
#         return live[-1] + extra // n


# Runtime
# Details
# 1874ms
# Beats 46.99%of users with Python3
# Memory
# Details
# 30.59mb
# Beats 49.40%of users with Python3
# https://leetcode.com/problems/maximum-running-time-of-n-computers/editorial/
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 1, sum(batteries) // n
        while left < right:
            target = right - (right - left) // 2

            extra = 0
            for power in batteries:
                extra += min(power, target)

            if extra // n >= target:
                left = target
            else:
                right = target - 1
        return left


tests = [
    [2, [3,3,3], 4],
    [2, [1,1,1,1], 2],
]

run_functional_tests(Solution().maxRunTime, tests)
