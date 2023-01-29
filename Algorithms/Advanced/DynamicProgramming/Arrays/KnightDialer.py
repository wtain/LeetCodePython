"""
https://leetcode.com/problems/knight-dialer/

The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.



Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
Example 3:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.


Constraints:

1 <= n <= 5000
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1037 ms
# Beats
# 70.21%
# Memory
# 13.8 MB
# Beats
# 94.26%
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9+7
        options = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4]
        ]
        counts = [1] * 10
        for i in range(1, n):
            new_counts = [0] * 10
            for d in range(10):
                for d1 in options[d]:
                    new_counts[d] += counts[d1]
                    new_counts[d] %= MOD
            counts = new_counts
        return sum(counts) % MOD


tests = [
    [1, 10],
    [2, 20],
    [3131, 136006598],
]

run_functional_tests(Solution().knightDialer, tests)
