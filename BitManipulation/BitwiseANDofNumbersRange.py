"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.



Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0


Constraints:

0 <= left <= right <= 231 - 1
"""
import math

from Common.ObjectTestingUtils import run_functional_tests



# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         # 101 110 111
#         # 01..111 - 10..000
#         result = 0
#         for bit in range(32):
#
#         return result


# Runtime: 60 ms, faster than 70.68% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 14 MB, less than 99.62% of Python3 online submissions for Bitwise AND of Numbers Range.
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/1514191/Bit-mask-(Java)
# class Solution:
#     def rangeBitwiseAnd(self, left: int, right: int) -> int:
#         if left == right:
#             return right
#         mask = int(math.log2(right-left)) + 1
#         return right & left >> mask << mask


# Runtime: 72 ms, faster than 40.97% of Python3 online submissions for Bitwise AND of Numbers Range.
# Memory Usage: 14.3 MB, less than 55.95% of Python3 online submissions for Bitwise AND of Numbers Range.
# https://leetcode.com/submissions/detail/348088723/
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        M, N = left, right
        result = 0
        mask = 1 << 31
        while mask > M:
            mask >>= 1

        mask_c = 0
        while mask:
            mask_c |= (mask << 1)
            if mask & M and mask & N:
                x = (M & mask_c) + (mask << 1)
                if x > N or x < M:
                    result |= mask
            mask >>= 1
        return result


tests = [
    [5, 7, 4],
    [0, 0, 0],
    [1, 2147483647, 0]
]

run_functional_tests(Solution().rangeBitwiseAnd, tests)