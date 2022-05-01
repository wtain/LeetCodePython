"""
https://leetcode.com/problems/expressive-words/

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.



Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3


Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.
"""
from itertools import count
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 81 ms, faster than 33.93% of Python3 online submissions for Expressive Words.
# Memory Usage: 14.1 MB, less than 31.68% of Python3 online submissions for Expressive Words.
class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def is_stretch(s: str, w: str) -> bool:
            i1, i2 = 0, 0
            while i1 < len(s) and i2 < len(w):
                if s[i1] != w[i2]:
                    return False
                c1, c2 = 0, 0
                while i1+c1 < len(s) and s[i1] == s[i1+c1]:
                    c1 += 1
                while i2+c2 < len(w) and w[i2] == w[i2+c2]:
                    c2 += 1
                if c1 != c2 and (c1 < 3 or c2 > c1):
                    return False
                i1 += c1
                i2 += c2
            return i1 == len(s) and i2 == len(w)

        return sum(is_stretch(s, w) for w in words)


tests = [
    ["heeellooo", ["hello", "hi", "helo"], 1],
    ["zzzzzyyyyy", ["zzyy","zy","zyy"], 3],
    [
        "dddiiiinnssssssoooo",
        ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"],
        3
    ],
    [
        "aaa",
        ["aaaa"],
        0
    ]
]

run_functional_tests(Solution().expressiveWords, tests)
