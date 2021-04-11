"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3701/
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.





Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 28 ms, faster than 81.79% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.1 MB, less than 86.13% of Python3 online submissions for Letter Combinations of a Phone Number.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        tr = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = [""]
        for d in digits:
            current = result
            result = []
            for s in current:
                for dd in tr.get(d):
                    result.append(s + dd)
        return result


tests = [
    ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
    ("", []),
    ("2", ["a","b","c"])
]

run_functional_tests(Solution().letterCombinations, tests)