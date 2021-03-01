"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3649/
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
from typing import List


# Runtime: 100 ms, faster than 89.45% of Python3 online submissions for Longest Word in Dictionary through Deleting.
# Memory Usage: 16.6 MB, less than 87.46% of Python3 online submissions for Longest Word in Dictionary through Deleting.
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        words = {}
        for w in d:
            if words.get(w[0]) is None:
                words[w[0]] = []
            words[w[0]].append([w, 0])

        result = ""

        n = len(s)
        for i in range(n):
            # print(words)
            l = []
            ch = s[i]
            if words.get(ch) is None:
                words[ch] = []
            l, words[ch] = words[ch], l
            for wi, wil in l:
                wil += 1
                if wil == len(wi):
                    if len(wi) > len(result) or \
                       len(wi) == len(result) and wi < result:
                        result = wi
                else:
                    ch = wi[wil]
                    if words.get(ch) is None:
                        words[ch] = []
                    words[ch].append([wi, wil])

        return result


tests = [
    ("aaa", ["aaa","aa","a"], "aaa"),

    ("abpcplea", ["ale","apple","monkey","plea"], "apple"),
    ("abpcplea", ["a","b","c"], "a")
]

for test in tests:
    result = Solution().findLongestWord(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + result)