"""
https://leetcode.com/problems/delete-characters-to-make-fancy-string/

A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.



Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".


Constraints:

1 <= s.length <= 105
s consists only of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 712 ms, faster than 62.68% of Python3 online submissions for Delete Characters to Make Fancy String.
# Memory Usage: 16.4 MB, less than 50.60% of Python3 online submissions for Delete Characters to Make Fancy String.
# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         result = s[:2]
#         n = len(s)
#         for i in range(2, n):
#             if s[i] == s[i-1] == s[i-2]:
#                 continue
#             result += s[i]
#         return result


# Runtime: 852 ms, faster than 41.66% of Python3 online submissions for Delete Characters to Make Fancy String.
# Memory Usage: 16.9 MB, less than 13.78% of Python3 online submissions for Delete Characters to Make Fancy String.
class Solution:
    def makeFancyString(self, s: str) -> str:
        a = [c for c in s]
        n = len(a)
        w = 2
        for r in range(2, n):
            if a[r] == a[w-1] == a[w-2]:
                continue
            a[w] = a[r]
            w += 1
        return "".join(a[:w])



tests = [
    ["", ""],
    ["leeetcode", "leetcode"],
    ["aaabaaaa", "aabaa"],
    ["aab", "aab"]
]

run_functional_tests(Solution().makeFancyString, tests)