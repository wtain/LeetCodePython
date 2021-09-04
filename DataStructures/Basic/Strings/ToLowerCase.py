"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3754/
https://leetcode.com/problems/to-lower-case/

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.



Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"


Constraints:

1 <= s.length <= 100
s consists of printable ASCII characters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 40.32% of Python3 online submissions for To Lower Case.
# Memory Usage: 14.2 MB, less than 63.92% of Python3 online submissions for To Lower Case.
class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([str.lower(c) for c in s])


tests = [
    ["Hello", "hello"],
    ["here", "here"],
    ["LOVELY", "lovely"]
]

run_functional_tests(Solution().toLowerCase, tests)