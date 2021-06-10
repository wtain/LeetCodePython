"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.



Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66


Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""
from functools import reduce
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 81.18% of Python3 online submissions for Sum of All Odd Length Subarrays.
# Memory Usage: 14.4 MB, less than 20.73% of Python3 online submissions for Sum of All Odd Length Subarrays.
# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         cs = reduce(lambda res, v: (res[0] + [res[1] + v], res[1] + v), arr, ([], 0))[0]
#         res = 0
#         for i in range(n):
#             for j in range(i, n):
#                 l1 = j-i+1
#                 if l1 % 2 == 0:
#                     continue
#                 res += cs[j]
#                 if i > 0:
#                     res -= cs[i-1]
#         return res


# Runtime: 64 ms, faster than 64.95% of Python3 online submissions for Sum of All Odd Length Subarrays.
# Memory Usage: 14.4 MB, less than 9.16% of Python3 online submissions for Sum of All Odd Length Subarrays.
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        cs = reduce(lambda res, v: (res[0] + [res[1] + v], res[1] + v), arr, ([], 0))[0]
        return sum(
            cs[j] - (cs[i-1] if i > 0 else 0)
            for i, j in product(range(n), range(n))
            if j >= i and (j-i+1) % 2
        )


tests = [
    [[1,4,2,5,3], 58],
    [[1,2], 3],
    [[10,11,12], 66]
]

run_functional_tests(Solution().sumOddLengthSubarrays, tests)