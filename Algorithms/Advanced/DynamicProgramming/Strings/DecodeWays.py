"""
https://leetcode.com/problems/decode-ways/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3581/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3902/

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
Example 4:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""

# Runtime: 32 ms, faster than 63.92% of Python3 online submissions for Decode Ways.
# Memory Usage: 14.4 MB, less than 26.32% of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(1, n):
            dp[i+1] = 0 if s[i] == "0" else dp[i]
            if (ord(s[i-1]) - ord("0")) * 10 + ord(s[i]) - ord("0") <= 26 and s[i-1] != "0":
                dp[i+1] += dp[i - 1]
        return dp[n]


tests = [
    ("12", 2),
    ("226", 3),
    ("0", 0),
    ("1", 1)
]

for test in tests:
    result = Solution().numDecodings(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected), ", got " + str(result))