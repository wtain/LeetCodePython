"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 206 ms
# Beats
# 49.95%
# Memory
# 17.3 MB
# Beats
# 14.59%
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        def is_vowel(c):
            return c in "aeiou"

        current_count = max_count = sum(1 for c in s[:k] if is_vowel(c))
        for i in range(k, len(s)):
            if is_vowel(s[i-k]):
                current_count -= 1
            if is_vowel(s[i]):
                current_count += 1
            max_count = max(max_count, current_count)
        return max_count


tests = [
    ["tryhard", 4, 1],
    ["abciiidef", 3, 3],
    ["aeiou", 2, 2],
    ["leetcode", 3, 2],
]

run_functional_tests(Solution().maxVowels, tests)
