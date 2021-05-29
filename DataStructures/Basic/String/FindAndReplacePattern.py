"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3750/
https://leetcode.com/problems/find-and-replace-pattern/

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]


Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 5.43% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 14.4 MB, less than 5.43% of Python3 online submissions for Find and Replace Pattern.
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def matches(w: str, pattern: str) -> bool:
            n = len(w)
            if len(pattern) != n:
                return False
            dict = {}
            matched = set()
            for c1, c2 in zip(w, pattern):
                if c1 not in dict:
                    if c2 in matched:
                        return False
                    dict[c1] = c2
                    matched.add(c2)
                elif dict[c1] != c2:
                    return False

            return True

        return [w for w in words if matches(w, pattern)]


tests = [
    [["abc","deq","mee","aqq","dkd","ccc"], "abb", ["mee","aqq"]],
    [["a","b","c"], "a", ["a","b","c"]]
]

run_functional_tests(Solution().findAndReplacePattern, tests)