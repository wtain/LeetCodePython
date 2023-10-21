"""
https://leetcode.com/problems/constrained-subsequence-sum/description/?envType=daily-question&envId=2023-10-21

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.



Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import heapq
from collections import deque
from typing import List

from sortedcontainers import SortedList

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 1750ms
# Beats 20.69%of users with Python3
# Memory
# Details
# 36.32MB
# Beats 20.69%of users with Python3
# https://leetcode.com/problems/constrained-subsequence-sum/editorial/?envType=daily-question&envId=2023-10-21
# class Solution:
#     def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
#         heap = [(-nums[0], 0)]
#         result = nums[0]
#
#         for i in range(1, len(nums)):
#             while i - heap[0][1] > k:
#                 heapq.heappop(heap)
#             curr = max(0, -heap[0][0]) + nums[i]
#             result = max(result, curr)
#             heapq.heappush(heap, (-curr, i))
#         return result



# Runtime
# Details
# 2227ms
# Beats 11.21%of users with Python3
# Memory
# Details
# 31.41MB
# Beats 28.45%of users with Python3
# https://leetcode.com/problems/constrained-subsequence-sum/editorial/?envType=daily-question&envId=2023-10-21
# class Solution:
#     def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
#         window = SortedList([0])
#         dp = [0] * len(nums)
#
#         for i in range(len(nums)):
#             dp[i] = nums[i] + window[-1]
#             window.add(dp[i])
#             if i >= k:
#                 window.remove(dp[i-k])
#
#         return max(dp)


# Runtime
# Details
# 1263ms
# Beats 95.26%of users with Python3
# Memory
# Details
# 30.07MB
# Beats 71.12%of users with Python3
# https://leetcode.com/problems/constrained-subsequence-sum/editorial/?envType=daily-question&envId=2023-10-21
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()
            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()

            if dp[i] > 0:
                queue.append(i)
        return max(dp)


tests = [
    [[10,2,-10,5,20], 2, 37],
    [[-1,-2,-3], 1, -1],
    [[10,-2,-10,-5,20], 2, 23],
]

run_functional_tests(Solution().constrainedSubsetSum, tests)
