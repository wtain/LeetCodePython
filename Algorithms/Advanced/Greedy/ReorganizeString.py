"""
https://leetcode.com/problems/reorganize-string/description/

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
import heapq
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests

# Runtime
# Details
# 44ms
# Beats 64.10%of users with Python3
# Memory
# Details
# 16.39MB
# Beats 46.15%of users with Python3
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)

        q = []
        for c in cnt:
            heapq.heappush(q, (-cnt[c], c))

        result = ""
        while q:
            num, char = heapq.heappop(q)
            num = -num
            if not result or result[-1] != char:
                result += char
                num -= 1
                if num:
                    heapq.heappush(q, (-num, char))
            else:
                if not q:
                    return ""
                num2, char2 = heapq.heappop(q)
                num2 = -num2
                result += char2
                num2 -= 1
                if num2:
                    heapq.heappush(q, (-num2, char2))
                heapq.heappush(q, (-num, char))
        return result


tests = [
    ["aab", "aba"],
    ["aaab", ""],
]

run_functional_tests(Solution().reorganizeString, tests)
