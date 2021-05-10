"""
https://leetcode.com/problems/tuple-with-same-product/

Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.



Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valids tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
Example 3:

Input: nums = [2,3,4,6,8,12]
Output: 40
Example 4:

Input: nums = [2,3,5,7]
Output: 0


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

Note that all of the integers are distinct. This means that each time a product is formed it must be formed by two unique integers.
Count the frequency of each product of 2 distinct numbers. Then calculate the permutations formed.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 604 ms, faster than 59.52% of Python3 online submissions for Tuple with Same Product.
# Memory Usage: 42.9 MB, less than 94.05% of Python3 online submissions for Tuple with Same Product.
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        products = {}
        for i in range(n-1):
            for j in range(i+1, n):
                p = nums[i] * nums[j]
                products[p] = products.get(p, 0) + 1
        cnt = 0
        for k in products.keys():
            v = products[k]
            cnt += 4 * v * (v - 1)
        return cnt


tests = [
    [
        [2,3,4,6],
        8
    ],
    [
        [1,2,4,5,10],
        16
    ],
    [
        [2,3,4,6,8,12],
        40
    ],
    [
        [2,3,5,7],
        0
    ]
]

run_functional_tests(Solution().tupleSameProduct, tests)