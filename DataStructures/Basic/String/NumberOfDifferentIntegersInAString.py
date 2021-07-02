"""
https://leetcode.com/problems/number-of-different-integers-in-a-string/

You are given a string word that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

Return the number of different integers after performing the replacement operations on word.

Two integers are considered different if their decimal representations without any leading zeros are different.



Example 1:

Input: word = "a123bc34d8ef34"
Output: 3
Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
Example 2:

Input: word = "leet1234code234"
Output: 2
Example 3:

Input: word = "a1b01c001"
Output: 1
Explanation: The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.


Constraints:

1 <= word.length <= 1000
word consists of digits and lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 67.94% of Python3 online submissions for Number of Different Integers in a String.
# Memory Usage: 14.2 MB, less than 56.04% of Python3 online submissions for Number of Different Integers in a String.
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        word += "$"
        curr_v = 0
        has_digit = False
        for c in word:
            if str.isdigit(c):
                curr_v = 10 * curr_v + ord(c) - ord('0')
                has_digit = True
            else:
                if has_digit:
                    s.add(curr_v)
                curr_v = 0
                has_digit = False
        return len(s)


tests = [
    ["a123bc34d8ef34", 3],
    ["leet1234code234", 2],
    ["a1b01c001", 1],


    ["a0b01c00", 2]
]

run_functional_tests(Solution().numDifferentIntegers, tests)