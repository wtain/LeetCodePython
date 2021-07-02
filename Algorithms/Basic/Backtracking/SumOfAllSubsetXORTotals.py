"""
https://leetcode.com/problems/sum-of-all-subset-xor-totals/

The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.



Example 1:

Input: nums = [1,3]
Output: 6
Explanation: The 4 subsets of [1,3] are:
- The empty subset has an XOR total of 0.
- [1] has an XOR total of 1.
- [3] has an XOR total of 3.
- [1,3] has an XOR total of 1 XOR 3 = 2.
0 + 1 + 3 + 2 = 6
Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
Example 3:

Input: nums = [3,4,5,6,7,8]
Output: 480
Explanation: The sum of all XOR totals for every subset is 480.


Constraints:

1 <= nums.length <= 12
1 <= nums[i] <= 20
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 152 ms, faster than 23.35% of Python3 online submissions for Sum of All Subset XOR Totals.
# Memory Usage: 14.1 MB, less than 82.02% of Python3 online submissions for Sum of All Subset XOR Totals.
# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         m = 1 << n
#         result = 0
#         for i in range(m):
#             xor = 0
#             for j in range(n):
#                 if i % 2:
#                     xor ^= nums[j]
#                 i //= 2
#             result += xor
#
#         return result


# Runtime: 36 ms, faster than 87.48% of Python3 online submissions for Sum of All Subset XOR Totals.
# Memory Usage: 14.1 MB, less than 82.02% of Python3 online submissions for Sum of All Subset XOR Totals.
# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         n = len(nums)
#         xors = [0, nums[0]]
#         for j in range(1, n):
#             m = len(xors)
#             for i in range(m):
#                 xors.append(xors[i] ^ nums[j])
#         return sum(xors)
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1305788/Python-Iterative-approach


# Runtime: 56 ms, faster than 78.69% of Python3 online submissions for Sum of All Subset XOR Totals.
# Memory Usage: 14.2 MB, less than 61.79% of Python3 online submissions for Sum of All Subset XOR Totals.
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1302492/C%2B%2B-Solution-oror-Recursion-oror-100-faster
# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         def impl(start: int, xor: int) -> int:
#             if start == len(nums):
#                 return xor
#             return impl(start+1, xor ^ nums[start]) + impl(start+1, xor)
#
#         return impl(0, 0)


# Runtime: 24 ms, faster than 99.38% of Python3 online submissions for Sum of All Subset XOR Totals.
# Memory Usage: 14.4 MB, less than 37.39% of Python3 online submissions for Sum of All Subset XOR Totals.
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        @lru_cache
        def impl(start: int, xor: int) -> int:
            if start == len(nums):
                return xor
            return impl(start+1, xor ^ nums[start]) + impl(start+1, xor)
        return impl(0, 0)
# https://leetcode.com/problems/sum-of-all-subset-xor-totals/discuss/1305788/Python-Iterative-approach



tests = [
    [[1,3], 6],
    [[5,1,6], 28],
    [[3,4,5,6,7,8], 480]
]

run_functional_tests(Solution().subsetXORSum, tests)