"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3597/
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.



Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true


Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
Runtime: 52 ms, faster than 6.74% of Python3 online submissions for Check If Two Strings Arrays are Equivalent.
Memory Usage: 14 MB, less than 99.83% of Python3 online submissions for Check If Two Strings Arrays are Equivalent.

Runtime: 40 ms, faster than 19.73% of Python3 online submissions for Check If Two Strings Arrays are Equivalent.
Memory Usage: 14.3 MB, less than 33.14% of Python3 online submissions for Check If Two Strings Arrays are Equivalent.
"""
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))  # True
print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))  # False
print(Solution().arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))  # True

