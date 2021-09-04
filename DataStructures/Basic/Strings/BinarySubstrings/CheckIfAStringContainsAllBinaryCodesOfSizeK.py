"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3669/
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.



Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
Example 2:

Input: s = "00110", k = 2
Output: true
Example 3:

Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1", it is clear that both exist as a substring.
Example 4:

Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and doesn't exist in the array.
Example 5:

Input: s = "0000000001011100", k = 4
Output: false


Constraints:

1 <= s.length <= 5 * 10^5
s consists of 0's and 1's only.
1 <= k <= 20
"""


# Runtime: 496 ms, faster than 38.40% of Python3 online submissions for Check If a Strings Contains All Binary Codes of Size K.
# Memory Usage: 23.6 MB, less than 65.82% of Python3 online submissions for Check If a Strings Contains All Binary Codes of Size K.
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         n = len(s)
#
#         if k > n:
#             return False
#
#         values = set()
#
#         def bitval(c: chr) -> int:
#             return 1 if c == '1' else 0
#
#         value = 0
#         for i in range(k):
#             value <<= 1
#             value += bitval(s[i])
#
#         values.add(value)
#
#         mask = (1 << (k-1)) - 1
#
#         for i in range(k, n):
#             value &= mask
#             value <<= 1
#             value += bitval(s[i])
#             values.add(value)
#
#         return len(values) == 2 ** k

# Runtime: 272 ms, faster than 89.87% of Python3 online submissions for Check If a Strings Contains All Binary Codes of Size K.
# Memory Usage: 27.4 MB, less than 41.35% of Python3 online submissions for Check If a Strings Contains All Binary Codes of Size K.
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len({s[i-k : i] for i in range(k, len(s)+1)}) == 1 << k


tests = [
    ("0101", 13, False),

    ("10010011", 2, True),

    ("00110110", 2, True),
    ("00110", 2, True),
    ("0110", 1, True),
    ("0110", 2, False),
    ("0000000001011100", 4, False)
]

for test in tests:
    result = Solution().hasAllCodes(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))