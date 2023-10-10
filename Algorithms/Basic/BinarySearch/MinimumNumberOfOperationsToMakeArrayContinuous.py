"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/editorial/?envType=daily-question&envId=2023-10-10

You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.



Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from bisect import bisect_right
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 714ms
# Beats 53.95%of users with Python3
# Memory
# Details
# 35.39MB
# Beats 51.32%of users with Python3
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/editorial/?envType=daily-question&envId=2023-10-10
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         n = len(nums)
#         result = n
#         new_nums = sorted(set(nums))
#
#         for i in range(len(new_nums)):
#             left = new_nums[i]
#             right = left + n - 1
#             j = bisect_right(new_nums, right)
#             count = j - i
#             result = min(result, n - count)
#
#         return result


# Runtime
# Details
# 721ms
# Beats 48.68%of users with Python3
# Memory
# Details
# 35.48MB
# Beats 38.82%of users with Python3
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/editorial/?envType=daily-question&envId=2023-10-10
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = n
        new_nums = sorted(set(nums))
        j = 0

        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1
            count = j - i
            result = min(result, n - count)

        return result


tests = [
    [[4,2,5,3], 0],
    [[1,2,3,5,6], 1],
    [[1,10,100,1000], 3],
]

run_functional_tests(Solution().minOperations, tests)
