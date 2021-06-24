"""
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 97.07% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
# Memory Usage: 14.2 MB, less than 76.57% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        last_index = [0] * 26
        for i in range(n):
            last_index[ord(s[i]) - ord('a')] = i

        st = []
        in_stack = set()
        for i in range(n):
            if s[i] in in_stack:
                continue
            while st and st[-1] > s[i] and last_index[ord(st[-1]) - ord('a')] > i:
                in_stack.remove(st[-1])
                st.pop()

            st.append(s[i])
            in_stack.add(s[i])

        return "".join(st)


tests = [
    ["bcabc", "abc"],
    ["cbacdcbc", "acdb"]
]

run_functional_tests(Solution().smallestSubsequence, tests)