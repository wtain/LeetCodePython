"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3816/
https://leetcode.com/problems/4sum/

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 148 ms, faster than 73.01% of Python3 online submissions for 4Sum.
# Memory Usage: 14.3 MB, less than 78.23% of Python3 online submissions for 4Sum.
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         result = []
#         n = len(nums)
#         nums.sort()
#         i = 0
#         while i < n-3:
#             if nums[i] * 4 > target:
#                 return result
#             j = n-1
#             while j > i+2:
#                 if nums[j] * 4 < target:
#                     break
#                 lo, hi = i+1, j-1
#                 t = target - nums[i] - nums[j]
#                 while lo < hi:
#                     s = nums[lo] + nums[hi]
#                     if s < t:
#                         lo += 1
#                     elif s > t:
#                         hi -= 1
#                     else:
#                         result.append([nums[i], nums[lo], nums[hi], nums[j]])
#                         lo += 1
#                         while lo < hi and nums[lo-1] == nums[lo]:
#                             lo += 1
#                         hi -= 1
#                         while lo < hi and nums[hi+1] == nums[hi]:
#                             hi -= 1
#                 while j > i+2 and nums[j-1] == nums[j]:
#                     j -= 1
#                 j -= 1
#             while i < n-3 and nums[i+1] == nums[i]:
#                 i += 1
#             i += 1
#         return result


# Runtime: 92 ms, faster than 89.78% of Python3 online submissions for 4Sum.
# Memory Usage: 14.4 MB, less than 28.76% of Python3 online submissions for 4Sum.
# https://leetcode.com/problems/4sum/solution/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def ksum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            if k == 2:
                return two_sum(nums, target)
            res = []
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for _, set in enumerate(ksum(nums[i+1:], target-nums[i], k-1)):
                        res.append([nums[i]] + set)
            return res

        def two_sum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s.add(nums[i])
            return res

        nums.sort()
        return ksum(nums, target, 4)


tests = [
    [[1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]],
    [[2,2,2,2,2], 8, [[2,2,2,2]]]
]

run_functional_tests(Solution().fourSum, tests)