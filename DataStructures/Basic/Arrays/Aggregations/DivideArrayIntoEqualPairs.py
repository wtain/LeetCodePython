"""
https://leetcode.com/problems/divide-array-into-equal-pairs/

You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.



Example 1:

Input: nums = [3,2,3,2,2,2]
Output: true
Explanation:
There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation:
There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.


Constraints:

nums.length == 2 * n
1 <= n <= 500
1 <= nums[i] <= 500
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def divideArray(self, nums: List[int]) -> bool:
#         s = 0
#         for v in nums:
#             s ^= v
#         return s == 0


# Runtime: 161 ms, faster than 24.83% of Python3 online submissions for Divide Array Into Equal Pairs.
# Memory Usage: 13.9 MB, less than 99.11% of Python3 online submissions for Divide Array Into Equal Pairs.
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for v in nums:
            if v not in s:
                s.add(v)
            else:
                s.remove(v)
        return len(s) == 0


tests = [
    [[1,3,2,0], False],
    [[3,2,3,2,2,2], True],
    [[1,2,3,4], False]
]

run_functional_tests(Solution().divideArray, tests)
