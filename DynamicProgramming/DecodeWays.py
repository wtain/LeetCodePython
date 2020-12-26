"""
https://leetcode.com/problems/decode-ways/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3581/

Runtime: 32 ms, faster than 63.92% of Python3 online submissions for Decode Ways.
Memory Usage: 14.4 MB, less than 26.32% of Python3 online submissions for Decode Ways.
"""


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