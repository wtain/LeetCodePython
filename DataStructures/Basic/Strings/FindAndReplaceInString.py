"""
https://leetcode.com/problems/find-and-replace-in-string/

You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.



Example 1:


Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"
Explanation:
"a" occurs at index 0 in s, so we replace it with "eee".
"cd" occurs at index 2 in s, so we replace it with "ffff".
Example 2:


Input: s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation:
"ab" occurs at index 0 in s, so we replace it with "eee".
"ec" does not occur at index 2 in s, so we do nothing.


Constraints:

1 <= s.length <= 1000
k == indices.length == sources.length == targets.length
1 <= k <= 100
0 <= indexes[i] < s.length
1 <= sources[i].length, targets[i].length <= 50
s consists of only lowercase English letters.
sources[i] and targets[i] consist of only lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 59 ms, faster than 36.09% of Python3 online submissions for Find And Replace in String.
# Memory Usage: 14.1 MB, less than 21.42% of Python3 online submissions for Find And Replace in String.
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = list([index, src, target] for index, src, target in zip(indices, sources, targets))
        replacements.sort(key=lambda replacement: -replacement[0])
        for index, src, target in replacements:
            if s[index:index+len(src)] != src:
                continue
            s = s[:index] + target + s[index+len(src):]
        return s


tests = [
    ["abcd", [0, 2], ["a", "cd"], ["eee", "ffff"], "eeebffff"],
    ["abcd", [0, 2], ["ab","ec"], ["eee","ffff"], "eeecd"]
]

run_functional_tests(Solution().findReplaceString, tests)
