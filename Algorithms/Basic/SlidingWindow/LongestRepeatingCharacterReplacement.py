"""
https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.



Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1032 ms, faster than 5.05% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 14.5 MB, less than 25.90% of Python3 online submissions for Longest Repeating Character Replacement.
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         n = len(s)
#         if k >= n:
#             return n
#         chars = set(s)
#         starts = dict()
#         max_len = 0
#         for c in chars:
#             starts[c] = 0
#         counts = defaultdict(int)
#         for i in range(n):
#             c = s[i]
#             for cc in chars:
#                 if cc == c:
#                     continue
#                 counts[cc] += 1
#             for c1 in chars:
#                 while counts[c1] > k and starts[c1] <= i:
#                     if s[starts[c1]] != c1:
#                         counts[c1] -= 1
#                     starts[c1] += 1
#                 l = max(0, i - starts[c1] + 1)
#                 # print(i, c, starts[c], counts[c])
#                 # print(s[starts[c]:i+1])
#                 max_len = max(max_len, l)
#         return max_len


# Runtime: 96 ms, faster than 92.97% of Python3 online submissions for Longest Repeating Character Replacement.
# Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Longest Repeating Character Replacement.
# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/1367596/C%2B%2B-SLIDING-WINDOW-SOLUTION-%3A-O(N)-AND-O(1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        i, j = 0, 0
        mp = defaultdict(int)
        result, mx = 0, 0
        while j < n:
            mp[s[j]] += 1
            mx = max(mx, mp[s[j]])
            ws = j - i + 1
            if ws - mx <= k:
                result = max(result, ws)
                j += 1
            else:
                mp[s[i]] -= 1
                i += 1
                j += 1
        return result


tests = [
    ["BAAAB", 2, 5],
    ["ABAB", 2, 4],
    ["AABABBA", 1, 4]
]

run_functional_tests(Solution().characterReplacement, tests)