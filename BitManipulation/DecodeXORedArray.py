"""
https://leetcode.com/problems/decode-xored-array/

There is a hidden integer array arr that consists of n non-negative integers.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

Return the original array arr. It can be proved that the answer exists and is unique.



Example 1:

Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
Example 2:

Input: encoded = [6,2,7,3], first = 4
Output: [4,2,0,7,4]


Constraints:

2 <= n <= 104
encoded.length == n - 1
0 <= encoded[i] <= 105
0 <= first <= 105
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 216 ms, faster than 96.00% of Python3 online submissions for Decode XORed Array.
# Memory Usage: 15.9 MB, less than 20.16% of Python3 online submissions for Decode XORed Array.
# class Solution:
#     def decode(self, encoded: List[int], first: int) -> List[int]:
#         n = len(encoded)
#         result = [0] * (n+1)
#         result[0] = first
#         for i in range(n):
#             result[i+1] = result[i] ^ encoded[i]
#
#         return result


# Runtime: 1976 ms, faster than 5.03% of Python3 online submissions for Decode XORed Array.
# Memory Usage: 16 MB, less than 20.16% of Python3 online submissions for Decode XORed Array.
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return reduce(lambda res, v: res + [v ^ res[-1]], encoded, [first])


tests = [
    [[1,2,3], 1, [1,0,2,1]],
    [[6,2,7,3], 4, [4,2,0,7,4]]
]

run_functional_tests(Solution().decode, tests)