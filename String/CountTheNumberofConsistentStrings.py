"""
https://leetcode.com/problems/count-the-number-of-consistent-strings/
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.



Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.


Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
Runtime: 240 ms, faster than 69.54% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 16.3 MB, less than 18.42% of Python3 online submissions for Count the Number of Consistent Strings.
"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def is_word_consistent(word: str) -> bool:
            for c in word:
                if c not in allowed:
                    return False
            return True
        cnt = 0
        for w in words:
            if is_word_consistent(w):
                cnt += 1
        return cnt


print(Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))  # 2
print(Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))  # 7
print(Solution().countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))  # 4
