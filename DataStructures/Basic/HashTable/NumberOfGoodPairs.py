"""
https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 44 ms, faster than 5.34% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.1 MB, less than 69.59% of Python3 online submissions for Number of Good Pairs.
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         c = Counter(nums)
#         result = 0
#         for k in c.keys():
#             cnt = c[k]
#             result += cnt * (cnt-1) // 2
#         return result


# Runtime: 68 ms, faster than 5.34% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 14.4 MB, less than 9.36% of Python3 online submissions for Number of Good Pairs.
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sum([c[v]*(c[v]-1)//2 for v in c])


tests = [
    [[1,2,3,1,1,3], 4],
    [[1,1,1,1], 6],
    [[1,2,3], 0]
]

run_functional_tests(Solution().numIdenticalPairs, tests)