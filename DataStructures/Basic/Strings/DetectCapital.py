"""
https://leetcode.com/problems/detect-capital/

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.



Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false


Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 69 ms, faster than 5.28% of Python3 online submissions for Detect Capital.
# Memory Usage: 14.3 MB, less than 46.33% of Python3 online submissions for Detect Capital.
# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         n = len(word)
#         if n <= 1:
#             return True
#         nl, nu = 0, 0
#         for c in word:
#             if str.islower(c):
#                 nl += 1
#             else:
#                 nu += 1
#         if nl * nu == 0:
#             return True
#         if nu == 1:
#             return str.isupper(word[0])
#         return nl == n


# Runtime: 32 ms, faster than 75.43% of Python3 online submissions for Detect Capital.
# Memory Usage: 14.3 MB, less than 13.27% of Python3 online submissions for Detect Capital.
# https://leetcode.com/submissions/detail/374362761/
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n <= 1:
            return True
        allow_upper, allow_lower = str.isupper(word[0]), str.islower(word[1])
        if not allow_upper and not allow_lower:
            return False
        if allow_lower:
            allow_upper = False
        for c in word[2:]:
            if not allow_upper and str.isupper(c):
                return False
            if not allow_lower and str.islower(c):
                return False
        return True


tests = [
    ["USA", True],
    ["FlaG", False]
]

run_functional_tests(Solution().detectCapitalUse, tests)
