"""
https://leetcode.com/problems/reformat-the-string/

Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.



Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:

Input: s = "ab123"
Output: "1a2b3"


Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 80 ms, faster than 5.60% of Python3 online submissions for Reformat The String.
# Memory Usage: 14.5 MB, less than 12.77% of Python3 online submissions for Reformat The String.
class Solution:
    def reformat(self, s: str) -> str:
        digits = [c for c in s if str.isdigit(c)]
        alphas = [c for c in s if str.isalpha(c)]
        if abs(len(digits) - len(alphas)) > 1:
            return ""
        i1 = i2 = 0
        turn_alpha = len(alphas) > len(digits)
        result = ""
        for i in range(len(s)):
            if turn_alpha:
                result += alphas[i1]
                i1 += 1
            else:
                result += digits[i2]
                i2 += 1
            turn_alpha = not turn_alpha
        return result


tests = [
    ["a0b1c2", "0a1b2c"],
    ["leetcode", ""],
    ["1229857369", ""],
    ["covid2019", "c2o0v1i9d"],
    ["ab123", "1a2b3"]
]


def customCheck(test, result) -> bool:
    if test[-1] == "":
        return result == ""
    if len(result) != len(test[-1]):
        return False
    if set(result) != set(test[-1]):
        return False
    for i in range(1, len(result)):
        if str.isdigit(result[i]) == str.isdigit(result[i-1]):
            return False
        if str.isalpha(result[i]) == str.isalpha(result[i-1]):
            return False
    return True


run_functional_tests(Solution().reformat, tests, custom_check=customCheck)