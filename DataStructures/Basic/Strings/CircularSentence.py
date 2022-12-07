"""
https://leetcode.com/problems/circular-sentence/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.



Example 1:

Input: sentence = "leetcode exercises sound delightful"
Output: true
Explanation: The words in sentence are ["leetcode", "exercises", "sound", "delightful"].
- leetcode's last character is equal to exercises's first character.
- exercises's last character is equal to sound's first character.
- sound's last character is equal to delightful's first character.
- delightful's last character is equal to leetcode's first character.
The sentence is circular.
Example 2:

Input: sentence = "eetcode"
Output: true
Explanation: The words in sentence are ["eetcode"].
- eetcode's last character is equal to eetcode's first character.
The sentence is circular.
Example 3:

Input: sentence = "Leetcode is cool"
Output: false
Explanation: The words in sentence are ["Leetcode", "is", "cool"].
- Leetcode's last character is not equal to is's first character.
The sentence is not circular.


Constraints:

1 <= sentence.length <= 500
sentence consist of only lowercase and uppercase English letters and spaces.
The words in sentence are separated by a single space.
There are no leading or trailing spaces.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 62 ms
# Beats
# 32.57%
# Memory
# 13.9 MB
# Beats
# 59.77%
# class Solution:
#     def isCircularSentence(self, sentence: str) -> bool:
#         words = sentence.split(" ")
#         n = len(words)
#         for i in range(n):
#             j = (i+1) % n
#             if words[i][-1] != words[j][0]:
#                 return False
#         return True


# Runtime
# 64 ms
# Beats
# 26.18%
# Memory
# 13.8 MB
# Beats
# 59.77%
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        i, n = 0, len(sentence)
        while i < n:
            j = sentence.find(" ", i)
            if j == -1:
                break
            if sentence[j-1] != sentence[j+1]:
                return False
            i = j + 1
        return True


tests = [
    ["leetcode exercises sound delightful", True],
    ["eetcode", True],
    ["Leetcode is cool", False]
]

run_functional_tests(Solution().isCircularSentence, tests)
