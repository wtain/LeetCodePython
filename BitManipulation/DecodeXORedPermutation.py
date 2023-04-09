"""
https://leetcode.com/problems/decode-xored-permutation/

There is an integer array perm that is a permutation of the first n positive integers, where n is always odd.

It was encoded into another integer array encoded of length n - 1, such that encoded[i] = perm[i] XOR perm[i + 1]. For example, if perm = [1,3,2], then encoded = [2,1].

Given the encoded array, return the original array perm. It is guaranteed that the answer exists and is unique.



Example 1:

Input: encoded = [3,1]
Output: [1,2,3]
Explanation: If perm = [1,2,3], then encoded = [1 XOR 2,2 XOR 3] = [3,1]
Example 2:

Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]


Constraints:

3 <= n < 105
n is odd.
encoded.length == n - 1
"""
from functools import reduce
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1125 ms
# Beats
# 48.19%
# Memory
# 33.7 MB
# Beats
# 40.96%
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        result = [0] * n
        xor_all = reduce(lambda r, s: r ^ s, range(1, n+1))
        xor_even = reduce(lambda r, s: r ^ s, encoded[::2])
        result[-1] = xor_even ^ xor_all
        for i in range(n-2, -1, -1):
            result[i] = result[i+1] ^ encoded[i]
        return result


tests = [
    [[3,1], [1,2,3]],
    [[6,5,4,6], [2,4,1,5,3]],
]

run_functional_tests(Solution().decode, tests)
