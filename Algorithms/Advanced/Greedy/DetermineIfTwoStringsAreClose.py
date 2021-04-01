"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3613/
https://leetcode.com/problems/determine-if-two-strings-are-close/
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.



Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
Example 4:

Input: word1 = "cabbba", word2 = "aabbss"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.


Constraints:

1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
"""
from collections import Counter


# Runtime: 128 ms, faster than 91.64% of Python3 online submissions for Determine if Two Strings Are Close.
# Memory Usage: 15.3 MB, less than 55.25% of Python3 online submissions for Determine if Two Strings Are Close.
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        return set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())


tests = [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
    ("cabbba", "aabbss", False),

    ("uau", "ssx", False)
]


for test in tests:
    result = Solution().closeStrings(test[0], test[1])
    if result == test[-1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))