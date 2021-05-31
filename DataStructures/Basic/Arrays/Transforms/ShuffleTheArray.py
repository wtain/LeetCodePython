"""
https://leetcode.com/problems/shuffle-the-array/

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].



Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]
Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]


Constraints:

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 68 ms, faster than 9.22% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.3 MB, less than 74.85% of Python3 online submissions for Shuffle the Array.
# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         i1, i2 = 0, n
#         result = [0] * (2*n)
#         for j in range(2*n):
#             if j % 2 == 0:
#                 result[j] = nums[i1]
#                 i1 += 1
#             else:
#                 result[j] = nums[i2]
#                 i2 += 1
#         return result


# Runtime: 112 ms, faster than 5.76% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.5 MB, less than 15.61% of Python3 online submissions for Shuffle the Array.
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return reduce(lambda res, rg: res + rg, [[x, y] for x, y in zip(nums[:n], nums[n:])], [])


tests = [
    [[2,5,1,3,4,7], 3, [2,3,5,4,1,7]],
    [[1,2,3,4,4,3,2,1], 4, [1,4,2,3,3,2,4,1]],
    [[1,1,2,2], 2, [1,2,1,2]]
]

run_functional_tests(Solution().shuffle, tests)