"""
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.



Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
Example 3:

Input: n = 7
Output: "holasss"


Constraints:

1 <= n <= 500
"""
from collections import Counter


# Runtime: 36 ms, faster than 18.04% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
# Memory Usage: 14.3 MB, less than 41.46% of Python3 online submissions for Generate a String With Characters That Have Odd Counts.
class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n % 2 == 1 else "a" * (n-1) + "b"


tests = [
    4,
    2,
    7
]


def is_good(s: str, n: int) -> bool:
    c = Counter(s)
    return len([1 for v in c.values() if v % 2 == 0]) == 0 and sum(c.values()) == n


for test in tests:
    result = Solution().generateTheString(test)
    if is_good(result, test):
        print("PASS")
    else:
        print("FAIL")