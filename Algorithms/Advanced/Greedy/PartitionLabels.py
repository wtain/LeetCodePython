"""
https://leetcode.com/problems/partition-labels/

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         parts = []
#
#         def split_partition(s: str, i0: int) -> int:
#             n = len(s)
#             j = s.rfind(s[i0], i0+1)
#             if j == -1:
#                 return 1
#             letters = set(s[i0:j+1])
#             for i in range(j+1, n):
#                 if s[i] in letters:
#                     return 0
#             return j-i0+1
#
#         i = 0
#         sz = split_partition(s, i)
#         while sz:
#             parts.append(sz)
#             i += sz
#             sz = split_partition(s, i)
#
#         return parts

# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         parts = []
#         c = Counter(s)
#         n = len(s)
#
#         def split_part(i0: int) -> int:
#             nonlocal s, n
#             i = i0
#             letters = set()
#             c[s[i]] -= 1
#             if c[s[i]] > 0:
#                 letters.add(s[i])
#             while letters and i+1 < n:
#                 i += 1
#                 c[s[i]] -= 1
#                 if c[s[i]] > 0:
#                     letters.add(s[i])
#                 elif s[i] in letters:
#                     letters.remove(s[i])
#             if i < n:
#                 return i-i0+1
#             return 0
#
#         i = 0
#         sz = split_part(i)
#         while sz and i < n:
#             parts.append(sz)
#             i += sz
#             sz = split_part(i)
#         return parts

# Runtime: 77 ms, faster than 20.21% of Python3 online submissions for Partition Labels.
# Memory Usage: 13.9 MB, less than 78.97% of Python3 online submissions for Partition Labels.
# https://leetcode.com/problems/partition-labels/solution/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        result = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                result.append(i - anchor + 1)
                anchor = i + 1
        return result


tests = [
    ["ababcbacadefegdehijhklij", [9, 7, 8]],
    ["eccbbbbdec", [10]]
]

run_functional_tests(Solution().partitionLabels, tests)
