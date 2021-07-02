"""
https://leetcode.com/problems/truncate-sentence/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.



Example 1:

Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".
Example 2:

Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation:
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".
Example 3:

Input: s = "chopper is not a tanuki", k = 5
Output: "chopper is not a tanuki"


Constraints:

1 <= s.length <= 500
k is in the range [1, the number of words in s].
s consist of only lowercase and uppercase English letters and spaces.
The words in s are separated by a single space.
There are no leading or trailing spaces.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 20 ms, faster than 98.89% of Python3 online submissions for Truncate Sentence.
# Memory Usage: 14.4 MB, less than 18.20% of Python3 online submissions for Truncate Sentence.
# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         return " ".join(s.split(" ")[:k])


# Runtime: 32 ms, faster than 56.16% of Python3 online submissions for Truncate Sentence.
# Memory Usage: 14.3 MB, less than 18.20% of Python3 online submissions for Truncate Sentence.
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ""
        wc = 0
        for c in s:
            if c == ' ':
                wc += 1
            if wc < k:
                result += c
        return result


tests = [
    ["Hello how are you Contestant", 4, "Hello how are you"],
    ["What is the solution to this problem", 4, "What is the solution"],
    ["chopper is not a tanuki", 5, "chopper is not a tanuki"]
]

run_functional_tests(Solution().truncateSentence, tests)