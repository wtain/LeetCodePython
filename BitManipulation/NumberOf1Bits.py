"""
https://leetcode.com/problems/number-of-1-bits/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.


Follow up:

If this function is called many times, how would you optimize it?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 24 ms, faster than 95.76% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 13.8 MB, less than 58.04% of Python3 online submissions for Number of 1 Bits.
"""
class Solution:
    counts: List[int] = [
        0,  # 0000
        1,  # 0001
        1,  # 0010
        2,  # 0011
        1,  # 0100
        2,  # 0101
        2,  # 0110
        3,  # 0111
        1,  # 1000
        2,  # 1001
        2,  # 1010
        3,  # 1011
        2,  # 1100
        3,  # 1101
        3,  # 1110
        4   # 1111
    ]

    def hammingWeight8(self, b: int) -> int:
        a0 = b & 15
        a1 = (b >> 4) & 15
        return self.counts[a0] + self.counts[a1]

    def hammingWeight(self, n: int) -> int:
        return self.hammingWeight8(n & 255) + \
               self.hammingWeight8((n >> 8) & 255) + \
               self.hammingWeight8((n >> 16) & 255) + \
               self.hammingWeight8((n >> 24) & 255)


tests = [
    [0b00000000000000000000000000001011, 3],
    [0b00000000000000000000000010000000, 1],
    [0b11111111111111111111111111111101, 31]
]

run_functional_tests(Solution().hammingWeight, tests)