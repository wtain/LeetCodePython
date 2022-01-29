"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3773/
https://leetcode.com/problems/jump-game-vi/

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:

 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]
#         for i in range(1, n):
#             mx = -math.inf
#             for j in range(max(0, i-k), i):
#                 mx = max(mx, dp[j])
#             dp[i] = mx + nums[i]
#         return dp[-1]


# Runtime: 1196 ms, faster than 18.60% of Python3 online submissions for Jump Game VI.
# Memory Usage: 36.1 MB, less than 10.13% of Python3 online submissions for Jump Game VI.
# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         h = [[-nums[0], 0]]
#         v = nums[0]
#         for i in range(1, n):
#             while h[0][1] < i-k:
#                 heapq.heappop(h)
#             v = nums[i] + -h[0][0]
#             heapq.heappush(h, [-v, i])
#         return v

# https://leetcode.com/problems/jump-game-vi/discuss/1260696/Python-Monotonic-deque-explained
# Runtime: 1232 ms, faster than 15.65% of Python3 online submissions for Jump Game VI.
# Memory Usage: 28.3 MB, less than 29.47% of Python3 online submissions for Jump Game VI.
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        d, n = deque([0]), len(nums)
        for i in range(1, n):
            while d and d[0] < i - k:
                d.popleft()
            nums[i] += nums[d[0]]
            while d and nums[i] >= nums[d[-1]]:
                d.pop()
            d.append(i)
        return nums[-1]



tests = [
    [[-123], 10, -123],
    [[1,-1,-2,4,-7,3], 2, 7],
    [[10,-5,-2,4,0,3], 3, 17],
    [[1,-5,-20,4,-1,3,-6,-3], 2, 0]
]


run_functional_tests(Solution().maxResult, tests)