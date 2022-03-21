"""
https://leetcode.com/problems/remove-duplicate-letters/

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 76.44% of Python3 online submissions for Remove Duplicate Letters.
# Memory Usage: 14.1 MB, less than 93.11% of Python3 online submissions for Remove Duplicate Letters.
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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


run_functional_tests(Solution().removeDuplicateLetters, tests)