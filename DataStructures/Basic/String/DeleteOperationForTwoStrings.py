"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3734/
https://leetcode.com/problems/delete-operation-for-two-strings/

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.



Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 396 ms, faster than 19.05% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 14.3 MB, less than 94.58% of Python3 online submissions for Delete Operation for Two Strings.
# class Solution:
#
#     def commonSubsequence(self, word1: str, word2: str) -> int:
#         n1, n2 = len(word1), len(word2)
#         v = [[0] * (n2+1) for _ in range(2)]
#         longest = 0
#         for i in range(n1+1):
#             i1 = i % 2
#             for j in range(n2+1):
#                 if i == 0 or j == 0:
#                     v[i1][j] = 0
#                 elif word1[i-1] == word2[j-1]:
#                     v[i1][j] = v[1-i1][j-1] + 1
#                 else:
#                     v[i1][j] = max(v[1-i1][j], v[i1][j-1])
#                 longest = max(longest, v[i1][j])
#         return longest
#
#     def minDistance(self, word1: str, word2: str) -> int:
#         if len(word1) < len(word2):
#             word1, word2 = word2, word1
#         n = self.commonSubsequence(word1, word2)
#         return len(word1) - n + len(word2) - n


# Runtime: 304 ms, faster than 58.69% of Python3 online submissions for Delete Operation for Two Strings.
# Memory Usage: 14.3 MB, less than 94.58% of Python3 online submissions for Delete Operation for Two Strings.
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        v = [[0] * (n2 + 1) for _ in range(2)]
        for i in range(n1 + 1):
            i1 = i % 2
            for j in range(n2 + 1):
                if i == 0 or j == 0:
                    v[i1][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    v[i1][j] = v[1 - i1][j - 1]
                else:
                    v[i1][j] = 1 + min(v[1 - i1][j], v[i1][j - 1])
        return v[n1 % 2][n2]


tests = [
    ["sea", "eat", 2],
    ["leetcode", "etco", 4]
]

run_functional_tests(Solution().minDistance, tests)