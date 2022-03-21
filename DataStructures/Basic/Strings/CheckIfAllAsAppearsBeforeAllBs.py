"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.



Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.


Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 47 ms, faster than 42.46% of Python3 online submissions for Check if All A's Appears Before All B's.
# Memory Usage: 13.8 MB, less than 67.32% of Python3 online submissions for Check if All A's Appears Before All B's.
class Solution:
    def checkString(self, s: str) -> bool:
        return s.find("ba") == -1


tests = [
    ["aaabbb", True],
    ["abab", False],
    ["bbb", True]
]

run_functional_tests(Solution().checkString, tests)
