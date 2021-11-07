"""
https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 219 ms, faster than 35.90% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.5 MB, less than 6.03% of Python3 online submissions for Find Pivot Index.
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         n = len(nums)
#         s1, s2 = [0] * n, [0] * n
#         s1[0], s2[-1] = nums[0], nums[-1]
#         for i in range(1, n):
#             s1[i] = s1[i - 1] + nums[i]
#             s2[-i - 1] = s2[-i] + nums[-i - 1]
#         for i in range(n):
#             left = s1[i - 1] if i > 0 else 0
#             right = s2[i + 1] if i < n - 1 else 0
#             if left == right:
#                 return i
#         return -1


# Runtime: 159 ms, faster than 60.44% of Python3 online submissions for Find Pivot Index.
# Memory Usage: 15.4 MB, less than 41.54% of Python3 online submissions for Find Pivot Index.
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s1, s2 = 0, sum(nums)
        for i in range(n):
            s2 -= nums[i]
            if s1 == s2:
                return i
            s1 += nums[i]
        return -1


tests = [
    [[1,7,3,6,5,6], 3],
    [[1,2,3], -1],
    [[2,1,-1], 0]
]

run_functional_tests(Solution().pivotIndex, tests)