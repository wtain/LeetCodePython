"""
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.



Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 92 ms, faster than 22.95% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
# Memory Usage: 14.4 MB, less than 64.92% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
# class Solution:
#     def makeEqual(self, words: List[str]) -> bool:
#         n = len(words)
#         cnt = Counter()
#         for w in words:
#             for c in w:
#                 cnt[c] += 1
#         for c in cnt.keys():
#             if cnt[c] % n:
#                 return False
#         return True


# Runtime: 44 ms, faster than 98.75% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
# Memory Usage: 14.2 MB, less than 96.89% of Python3 online submissions for Redistribute Characters to Make All Strings Equal.
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = Counter("".join(words))
        return all(cnt[c] % n == 0 for c in cnt)



tests = [
    [["abc","aabc","bc"], True],
    [["ab","a"], False]
]


run_functional_tests(Solution().makeEqual, tests)