"""
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.



Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10


Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 40 ms
# Beats
# 81.1%
# Memory
# 14 MB
# Beats
# 16.46%
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        cs = [0] * n
        cs[0] = arr[0]
        for i in range(1, n):
            cs[i] = cs[i-1] ^ arr[i]

        starts = defaultdict(list)
        starts[0].append(-1)
        for i in range(n):
            for j in starts[cs[i]]:
                result += i-j-1
            starts[cs[i]].append(i)

        return result


tests = [
    [[2,3,1,6,7], 4],
    [[1,1,1,1,1], 10],
]

run_functional_tests(Solution().countTriplets, tests)
