"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3699/
https://leetcode.com/problems/determine-if-string-halves-are-alike/

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
Example 3:

Input: s = "MerryChristmas"
Output: false
Example 4:

Input: s = "AbCdEfGh"
Output: true


Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 57.16% of Python3 online submissions for Determine if Strings Halves Are Alike.
# Memory Usage: 14.4 MB, less than 37.10% of Python3 online submissions for Determine if Strings Halves Are Alike.
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = str.lower(s)
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]

        def get_counts(ss: str):
            return sum([1 for c in ss if c in ["a", "e", "i", "o", "u"]])

        return get_counts(a) == get_counts(b)


tests = [
    ("book", True),
    ("textbook", False),
    ("MerryChristmas", False),
    ("AbCdEfGh", True)
]

run_functional_tests(Solution().halvesAreAlike, tests)