"""
https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/?envType=daily-question&envId=2023-10-22

You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.



Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length
"""
import bisect
from math import inf
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 1238ms
# Beats 5.10%of users with Python3
# Memory
# Details
# 27.58MB
# Beats 10.20%of users with Python3
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/editorial/?envType=daily-question&envId=2023-10-22
# class Solution:
#     def maximumScore(self, nums: List[int], k: int) -> int:
#         def solve(nums, k):
#             n = len(nums)
#             left = [0] * k
#             curr_min = inf
#             for i in range(k-1, -1, -1):
#                 curr_min = min(curr_min, nums[i])
#                 left[i] = curr_min
#             right = []
#             curr_min = inf
#             for i in range(k, n):
#                 curr_min = min(curr_min, nums[i])
#                 right.append(curr_min)
#             result = 0
#             for j in range(len(right)):
#                 curr_min = right[j]
#                 i = bisect.bisect_left(left, curr_min)
#                 size = (k+j) - i + 1
#                 result = max(result, curr_min * size)
#             return result
#         return max(solve(nums, k), solve(nums[::-1], len(nums) - k - 1))


# Runtime
# Details
# 1113ms
# Beats 26.02%of users with Python3
# Memory
# Details
# 26.87MB
# Beats 77.04%of users with Python3
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/editorial/?envType=daily-question&envId=2023-10-22
# class Solution:
#     def maximumScore(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         left = [-1] * n
#         stack = []
#
#         for i in range(n-1, -1, -1):
#             while stack and nums[stack[-1]] > nums[i]:
#                 left[stack.pop()] = i
#             stack.append(i)
#
#         right = [n] * n
#         stack = []
#         for i in range(n):
#             while stack and nums[stack[-1]] > nums[i]:
#                 right[stack.pop()] = i
#             stack.append(i)
#         result = 0
#         for i in range(n):
#             if left[i] < k < right[i]:
#                 result = max(result, nums[i] * (right[i] - left[i] - 1))
#         return result



# Runtime
# Details
# 1029ms
# Beats 67.86%of users with Python3
# Memory
# Details
# 27.36MB
# Beats 46.94%of users with Python3
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/editorial/?envType=daily-question&envId=2023-10-22
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = right = k
        result = nums[k]
        curr_min = nums[k]
        while left > 0 or right < n-1:
            if (nums[left-1] if left else 0) < (nums[right+1] if right < n-1 else 0):
                right += 1
                curr_min = min(curr_min, nums[right])
            else:
                left -= 1
                curr_min = min(curr_min, nums[left])
            result = max(result, curr_min * (right - left + 1))
        return result


tests = [
    [[1,4,3,7,4,5], 3, 15],
    [[5,5,4,5,4,1,1,1], 0, 20],
]

run_functional_tests(Solution().maximumScore, tests)
