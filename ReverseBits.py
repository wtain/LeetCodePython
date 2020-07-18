"""
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.


Follow up:

If this function is called many times, how would you optimize it?
"""
from typing import List

"""
Runtime: 32 ms, faster than 82.76% of Python3 online submissions for Reverse Bits.
Memory Usage: 13.9 MB, less than 23.44% of Python3 online submissions for Reverse Bits.
"""
class Solution:
    mapping: List[int]

    def __init__(self):
        self.mapping = [
            0,  # 0000 -> 0000   0
            8,  # 0001 -> 1000   1
            4,  # 0010 -> 0100   2
            12,  # 0011 -> 1100   3
            2,  # 0100 -> 0010   4
            10,  # 0101 -> 1010   5
            6,  # 0110 -> 0110   6
            14,  # 0111 -> 1110   7
            1,  # 1000 -> 0001   8
            9,  # 1001 -> 1001   9
            5,  # 1010 -> 0101  10
            13,  # 1011 -> 1101  11
            3,  # 1100 -> 0011  12
            11,  # 1101 -> 1011  13
            7,  # 1110 -> 0111  14
            15  # 1111 -> 1111  15
        ]

    def reverseBits8(self, b: int) -> int:
        a0 = b & 15
        a1 = (b >> 4) & 15
        a0 = self.mapping[a0]
        a1 = self.mapping[a1]
        return (a0 << 4) | a1

    def reverseBits(self, n: int) -> int:

        b0 = n & 255
        b1 = (n >> 8) & 255
        b2 = (n >> 16) & 255
        b3 = (n >> 24) & 255
        b0 = self.reverseBits8(b0)
        b1 = self.reverseBits8(b1)
        b2 = self.reverseBits8(b2)
        b3 = self.reverseBits8(b3)
        return b3 | (b2 << 8) | (b1 << 16) | (b0 << 24)


print("{0:032b}".format(Solution().reverseBits(0b00000010100101000001111010011100)))  # 00111001011110000010100101000000
print("{0:032b}".format(Solution().reverseBits(0b11111111111111111111111111111101)))  # 10111111111111111111111111111111
