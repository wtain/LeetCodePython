"""
https://leetcode.com/problems/consecutive-characters/

Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.



Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1


Constraints:

1 <= s.length <= 500
s contains only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 93.45% of Python3 online submissions for Consecutive Characters.
# Memory Usage: 14.2 MB, less than 43.18% of Python3 online submissions for Consecutive Characters.
class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        n = len(s)
        c_power = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                c_power += 1
            else:
                c_power = 1
            max_power = max(max_power, c_power)
        return max_power


tests = [
    ["leetcode", 2],
    ["abbcccddddeeeeedcba", 5],
    ["triplepillooooow", 5],
    ["hooraaaaaaaaaaay", 11],
    ["tourist", 1]
]

run_functional_tests(Solution().maxPower, tests)