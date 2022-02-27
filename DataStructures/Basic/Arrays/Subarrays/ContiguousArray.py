"""
https://leetcode.com/problems/contiguous-array/

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.



Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1213 ms, faster than 33.34% of Python3 online submissions for Contiguous Array.
# Memory Usage: 19.3 MB, less than 20.79% of Python3 online submissions for Contiguous Array.
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         balanse, n, index, maxlen = 0, len(nums), {0: -1}, 0
#         for i in range(n):
#             if nums[i] == 1:
#                 balanse += 1
#             else:
#                 balanse -= 1
#             if balanse in index:
#                 maxlen = max(maxlen, i - index.get(balanse))
#             else:
#                 index[balanse] = i
#         return maxlen


# Runtime: 1932 ms, faster than 5.04% of Python3 online submissions for Contiguous Array.
# Memory Usage: 17.4 MB, less than 98.93% of Python3 online submissions for Contiguous Array.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balanse, n, maxlen = 0, len(nums), 0
        index = [-2] * (2*n+1)
        index[n] = -1
        for i in range(n):
            if nums[i] == 1:
                balanse += 1
            else:
                balanse -= 1
            if index[n + balanse] != -2:
                maxlen = max(maxlen, i - index[n + balanse])
            else:
                index[n + balanse] = i
        return maxlen


tests = [
    [[0,1], 2],
    [[0,1,0], 2]
]

run_functional_tests(Solution().findMaxLength, tests)
