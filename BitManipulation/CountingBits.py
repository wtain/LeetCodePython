"""
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= n <= 105


Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# https://leetcode.com/submissions/detail/345870953/
# Runtime: 101 ms, faster than 73.93% of Python3 online submissions for Counting Bits.
# Memory Usage: 21 MB, less than 20.83% of Python3 online submissions for Counting Bits.
class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0] * (n+1)
        for i in range(1, n+1):
            results[i] = results[i // 2] + i % 2
        return results


tests = [
    [2, [0,1,1]],
    [5, [0,1,1,2,1,2]]
]

run_functional_tests(Solution().countBits, tests)
