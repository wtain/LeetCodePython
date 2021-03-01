"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""


Constraints:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


# Runtime: 28 ms, faster than 90.07% of Python3 online submissions for Greatest Common Divisor of Strings.
# Memory Usage: 14.2 MB, less than 63.36% of Python3 online submissions for Greatest Common Divisor of Strings.
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        m = min(n1, n2)
        for l in range(m, 0, -1):
            if n1 % l != 0 or n2 % l != 0:
                continue
            prefix = str1[0:l]
            # print(prefix)
            m1 = n1 // l
            m2 = n2 // l
            if prefix * m1 == str1 and prefix * m2 == str2:
                return prefix
        return ""



tests = [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("LEET", "CODE", ""),
    ("ABCDEF", "ABC", "")
]

for test in tests:
    result = Solution().gcdOfStrings(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))