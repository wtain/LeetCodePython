"""
https://leetcode.com/problems/find-the-middle-index-in-array/

Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.



Example 1:

Input: nums = [2,3,-1,8,4]
Output: 3
Explanation:
The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4
Example 2:

Input: nums = [1,-1,4]
Output: 2
Explanation:
The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0
Example 3:

Input: nums = [2,5]
Output: -1
Explanation:
There is no valid middleIndex.
Example 4:

Input: nums = [1]
Output: 0
Explantion:
The sum of the numbers before index 0 is: 0
The sum of the numbers after index 0 is: 0


Constraints:

1 <= nums.length <= 100
-1000 <= nums[i] <= 1000


Note: This question is the same as 724: https://leetcode.com/problems/find-pivot-index/
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 56 ms, faster than 35.15% of Python3 online submissions for Find the Middle Index in Array.
# Memory Usage: 14.1 MB, less than 92.63% of Python3 online submissions for Find the Middle Index in Array.
# class Solution:
#     def findMiddleIndex(self, nums: List[int]) -> int:
#         n = len(nums)
#         s1, s2 = [0] * n, [0] * n
#         s1[0], s2[-1] = nums[0], nums[-1]
#         for i in range(1, n):
#             s1[i] = s1[i-1] + nums[i]
#             s2[-i-1] = s2[-i] + nums[-i-1]
#         for i in range(n):
#             left = s1[i-1] if i > 0 else 0
#             right = s2[i+1] if i < n-1 else 0
#             if left == right:
#                 return i
#         return -1


# Runtime: 40 ms, faster than 83.50% of Python3 online submissions for Find the Middle Index in Array.
# Memory Usage: 14.2 MB, less than 78.16% of Python3 online submissions for Find the Middle Index in Array.
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        s1, s2 = 0, sum(nums)
        for i in range(n):
            s2 -= nums[i]
            if s1 == s2:
                return i
            s1 += nums[i]
        return -1


tests = [
    [[2,3,-1,8,4], 3],
    [[1,-1,4], 2],
    [[2,5], -1],
    [[1], 0]
]

run_functional_tests(Solution().findMiddleIndex, tests)