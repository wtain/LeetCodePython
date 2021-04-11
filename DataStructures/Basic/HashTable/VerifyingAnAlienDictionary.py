"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3702/
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 20 ms, faster than 99.91% of Python3 online submissions for Verifying an Alien Dictionary.
# Memory Usage: 14.3 MB, less than 48.60% of Python3 online submissions for Verifying an Alien Dictionary.
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def get_order(order: str) -> Dict[str, int]:
            result = {}
            for i, c in enumerate(order):
                result[c] = i
            return result

        def is_less(s1: str, s2: str, ordd: Dict[str, int]) -> bool:
            n1 = len(s1)
            n2 = len(s2)
            n = min(n1, n2)
            for i in range(n):
                if ordd.get(s1[i]) > ordd.get(s2[i]):
                    return False
                if ordd.get(s1[i]) < ordd.get(s2[i]):
                    return True
            return n1 <= n2

        ordd = get_order(order)
        n = len(words)
        for i in range(1, n):
            if not is_less(words[i-1], words[i], ordd):
                return False

        return True


tests = [
    (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
    (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False)
]

run_functional_tests(Solution().isAlienSorted, tests)