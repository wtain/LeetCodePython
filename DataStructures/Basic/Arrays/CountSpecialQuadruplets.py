"""
https://leetcode.com/problems/count-special-quadruplets/

Given a 0-indexed integer array nums, return the number of distinct quadruplets (a, b, c, d) such that:

nums[a] + nums[b] + nums[c] == nums[d], and
a < b < c < d


Example 1:

Input: nums = [1,2,3,6]
Output: 1
Explanation: The only quadruplet that satisfies the requirement is (0, 1, 2, 3) because 1 + 2 + 3 == 6.
Example 2:

Input: nums = [3,3,6,4,5]
Output: 0
Explanation: There are no such quadruplets in [3,3,6,4,5].
Example 3:

Input: nums = [1,1,1,3,5]
Output: 4
Explanation: The 4 quadruplets that satisfy the requirement are:
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5


Constraints:

4 <= nums.length <= 50
1 <= nums[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1544 ms, faster than 51.89% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 14.2 MB, less than 76.16% of Python3 online submissions for Count Special Quadruplets.
# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         cnt, n = 0, len(nums)
#         for i in range(n-3):
#             for j in range(i+1, n-2):
#                 for k in range(j+1, n-1):
#                     for l in range(k+1, n):
#                         if nums[i] + nums[j] + nums[k] == nums[l]:
#                             cnt += 1
#         return cnt


# https://leetcode.com/problems/count-special-quadruplets/discuss/1513868/O(n2)-Approach
# Runtime: 72 ms, faster than 96.55% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 14.3 MB, less than 51.01% of Python3 online submissions for Count Special Quadruplets.
# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         cnt, n = 0, len(nums)
#         mp = [0] * 600
#         for i in range(2, n):
#             for j in range(i+1, n):
#                 mp[nums[j]-nums[i]+101] += 1
#
#         for i in range(1, n):
#             for j in range(i):
#                 s = nums[i] + nums[j]
#                 cnt += mp[s + 101]
#             for j in range(i+2, n):
#                 mp[nums[j] - nums[i+1] + 101] -= 1
#         return cnt


# Runtime: 70 ms, faster than 96.65% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 14 MB, less than 97.82% of Python3 online submissions for Count Special Quadruplets.
# class Solution:
#     def countQuadruplets(self, nums: List[int]) -> int:
#         cnt, n = 0, len(nums)
#         mp = [0] * 301
#         for i in range(2, n):
#             for j in range(i+1, n):
#                 mp[nums[j]-nums[i]+100] += 1
#
#         for i in range(1, n):
#             for j in range(i):
#                 s = nums[i] + nums[j]
#                 cnt += mp[s + 100]
#             for j in range(i+2, n):
#                 mp[nums[j] - nums[i+1] + 100] -= 1
#         return cnt


# Runtime: 89 ms, faster than 94.60% of Python3 online submissions for Count Special Quadruplets.
# Memory Usage: 14.1 MB, less than 76.16% of Python3 online submissions for Count Special Quadruplets.
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt, n = 0, len(nums)
        mp = [0] * 300
        for i in range(2, n):
            for j in range(i+1, n):
                mp[nums[j]-nums[i]+99] += 1

        for i in range(1, n):
            for j in range(i):
                s = nums[i] + nums[j]
                cnt += mp[s + 99]
            for j in range(i+2, n):
                mp[nums[j] - nums[i+1] + 99] -= 1
        return cnt


tests = [
    [[1,2,3,6], 1],
    [[3,3,6,4,5], 0],
    [[1,1,1,3,5], 4],
    [[8,73,11,9,28,92,52], 2],
    [[78,22,23,66,7,64,22,15,87,100,8,1,43,46,53,87,14,85,21,86,100,65,34,3,32,7,95,96,31], 79]
]

run_functional_tests(Solution().countQuadruplets, tests)