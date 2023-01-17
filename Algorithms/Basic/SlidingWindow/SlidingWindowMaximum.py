"""
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
import heapq
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1993 ms
# Beats
# 58.61%
# Memory
# 39.5 MB
# Beats
# 6.12%
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         maxes = []
#         result = []
#         current_max = nums[0]
#         for i in range(k):
#             current_max = max(current_max, nums[i])
#             heapq.heappush(maxes, (-nums[i], i))
#         result.append(current_max)
#         n = len(nums)
#         for i in range(k, n):
#             while maxes and maxes[0][1] <= i-k:
#                 heapq.heappop(maxes)
#             heapq.heappush(maxes, (-nums[i], i))
#             result.append(-maxes[0][0])
#         return result


# Runtime
# 1760 ms
# Beats
# 85.88%
# Memory
# 31.4 MB
# Beats
# 12.28%
# https://leetcode.com/problems/sliding-window-maximum/solutions/3057730/simple-and-easy-to-understand-queue/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result, queue = [], []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)
            if i - k == queue[0]:
                queue.pop(0)
            if i + 1 >= k:
                result.append(nums[queue[0]])
        return result



tests = [
    [[1,-1], 1, [1,-1]],
    [[1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]],
    [[1], 1, [1]],
]

run_functional_tests(Solution().maxSlidingWindow, tests)
