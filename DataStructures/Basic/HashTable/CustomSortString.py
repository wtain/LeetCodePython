"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3813/
https://leetcode.com/problems/custom-sort-string/

order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input:
order = "cba"
str = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.


Note:

order has length at most 26, and no character is repeated in order.
str has length at most 200.
order and str consist of lowercase letters only.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 62.80% of Python3 online submissions for Custom Sort Strings.
# Memory Usage: 14.1 MB, less than 81.58% of Python3 online submissions for Custom Sort Strings.
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        h = {}
        for i, c in enumerate(order):
            h[c] = i
        return "".join(sorted(str, key=lambda c: h.get(c, 2)))


tests = [
    ["cba", "abcd", "cbad"]
]

run_functional_tests(Solution().customSortString, tests)