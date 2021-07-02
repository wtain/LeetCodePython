"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/

There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).



Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1


Constraints:

1 <= nums.length <= 1000
-100 <= nums[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 67.24% of Python3 online submissions for Sign of the Product of an Array.
# Memory Usage: 14.4 MB, less than 65.51% of Python3 online submissions for Sign of the Product of an Array.
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if not n:
                return 0
            if n < 0:
                res = -res
        return res


tests = [
    [[-1,-2,-3,-4,3,2,1], 1],
    [[1,5,0,2,-3], 0],
    [[-1,1,-1,1,-1], -1]
]

run_functional_tests(Solution().arraySign, tests)