"""
https://leetcode.com/problems/license-key-formatting/
You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.

Example 1:
Input: S = "5F3Z-2e-9-w", K = 4

Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:
Input: S = "2-5g-3-J", K = 2

Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
Note:
The length of string S will not exceed 12,000, and K is a positive integer.
Strings S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
Strings S is non-empty.
"""

"""
Runtime: 116 ms, faster than 27.19% of Python3 online submissions for License Key Formatting.
Memory Usage: 14 MB, less than 99.62% of Python3 online submissions for License Key Formatting.
"""
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        n = len(S)
        nd = S.count('-')
        m = n - nd
        nGroups = m // K
        firstSize = m - nGroups * K
        groupLeft = firstSize or K
        result = ""
        for c in S:
            if c == '-':
                continue
            if groupLeft == 0:
                result += '-'
                groupLeft = K
            result += str.upper(c)
            groupLeft -= 1
        return result


print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))  # "5F3Z-2E9W"
print(Solution().licenseKeyFormatting("2-5g-3-J", 2))  # "2-5G-3J"
