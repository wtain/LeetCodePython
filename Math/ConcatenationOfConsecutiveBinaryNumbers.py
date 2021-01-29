"""
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618/
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.



Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1.
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.


Constraints:

1 <= n <= 105
"""
import math

"""
1  2  3   4   5   6   7
1 10 11 100 101 110 111
1  2  2   3   3   3   3

F(0) = 0
F(n) = F(n-1) * 2 ^ log2(n) + n


"""


# Runtime: 4588 ms, faster than 7.08% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# Memory Usage: 18.3 MB, less than 18.51% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         dp = [0] * (n+1)
#         mod = 10 ** 9 + 7
#         for i in range(1, n+1):
#             ndigits = int(math.log(i, 2)+1)
#             # print(i, ndigits)
#             dp[i] = dp[i-1] * (2**ndigits) + i
#             dp[i] %= mod
#         return dp[n]

# Runtime: 2196 ms, faster than 31.39% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# Memory Usage: 18.3 MB, less than 18.95% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         dp = [0] * (n+1)
#         mod = 10 ** 9 + 7
#         current_length = 0
#         for i in range(1, n+1):
#             if not i & (i-1):
#                 current_length += 1
#             dp[i] = dp[i-1] * (1 << current_length) + i
#             dp[i] %= mod
#         return dp[n]

# Runtime: 1332 ms, faster than 78.11% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# Memory Usage: 14.3 MB, less than 53.67% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result = 0
        mod = 10 ** 9 + 7
        current_length = 1
        for i in range(1, n+1):
            if not i & (i-1):
                current_length <<= 1
            result = (result * current_length + i) % mod
        return result



tests = [
    (1, 1),
    (3, 27),
    (12, 505379714),

    (10000, 356435599),
    (100000, 757631812)
]

for test in tests:
    result = Solution().concatenatedBinary(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))