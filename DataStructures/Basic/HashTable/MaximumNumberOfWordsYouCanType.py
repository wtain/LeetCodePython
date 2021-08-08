"""
https://leetcode.com/problems/maximum-number-of-words-you-can-type/

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.



Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.


Constraints:

1 <= text.length <= 104
0 <= brokenLetters.length <= 26
text consists of words separated by a single space without any leading or trailing spaces.
Each word only consists of lowercase English letters.
brokenLetters consists of distinct lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 77.10% of Python3 online submissions for Maximum Number of Words You Can Type.
# Memory Usage: 14.4 MB, less than 35.40% of Python3 online submissions for Maximum Number of Words You Can Type.
# class Solution:
#     def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
#         words = [w for w in text.split(" ")]
#         bw = set(brokenLetters)
#         cnt = 0
#         for w in words:
#             for c in w:
#                 if c in bw:
#                     cnt += 1
#                     break
#         return len(words) - cnt


# Runtime: 28 ms, faster than 91.63% of Python3 online submissions for Maximum Number of Words You Can Type.
# Memory Usage: 14.4 MB, less than 35.40% of Python3 online submissions for Maximum Number of Words You Can Type.
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum([len(set(w).intersection(set(brokenLetters))) == 0 for w in text.split(" ")])


tests = [
    ["hello world", "ad", 1],
    ["leet code", "lt", 1],
    ["leet code", "e", 0]
]

run_functional_tests(Solution().canBeTypedWords, tests)