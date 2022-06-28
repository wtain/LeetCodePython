"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""
import heapq
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 184 ms, faster than 71.98% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 14.9 MB, less than 51.90% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# class Solution:
#     def minDeletions(self, s: str) -> int:
#         c = Counter(s)
#         result = 0
#         values = list([-v for v in c.values()])
#         heapq.heapify(values)
#         prev = -heapq.heappop(values)
#         while values:
#             value = -heapq.heappop(values)
#             if value == prev:
#                 result += 1
#                 value -= 1
#                 if value:
#                     heapq.heappush(values, -value)
#             else:
#                 prev = value
#         return result

# Runtime: 608 ms, faster than 5.71% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 14.8 MB, less than 51.90% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/solution/
class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - ord('a')] += 1
        freqs.sort(reverse=True)
        delcnt = 0
        max_freq = len(s)
        for freq in freqs:
            if freq > max_freq:
                delcnt += freq - max_freq
                freq = max_freq
            max_freq = max(0, freq-1)
        return delcnt



tests = [
    ["bbcebab", 2],
    ["abcabc", 3],
    ["aab", 0],
    ["aaabbbcc", 2],
    ["ceabaacb", 2]
]

run_functional_tests(Solution().minDeletions, tests)
