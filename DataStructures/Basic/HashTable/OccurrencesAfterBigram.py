"""
https://leetcode.com/problems/occurrences-after-bigram/

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.



Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]
Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]


Note:

1 <= text.length <= 1000
text consists of space separated words, where each word consists of lowercase English letters.
1 <= first.length, second.length <= 10
first and second consist of lowercase English letters.
"""
from typing import List


# Runtime: 32 ms, faster than 55.04% of Python3 online submissions for Occurrences After Bigram.
# Memory Usage: 14.4 MB, less than 22.75% of Python3 online submissions for Occurrences After Bigram.
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        words = text.split(' ')
        n = len(words)
        if n >= 3:
            w1 = words[0]
            w2 = words[1]
            for i in range(2, n):
                if w1 == first and w2 == second:
                    result.append(words[i])
                w1 = w2
                w2 = words[i]
        return result


tests = [
    ("alice is a good girl she is a good student", "a", "good", ["girl", "student"]),
    ("we will we will rock you", "we", "will", ["we", "rock"])
]

for test in tests:
    result = Solution().findOcurrences(test[0], test[1], test[2])
    if result == test[3]:
        print("PASS")
    else:
        print("FAIL - " + str(result))