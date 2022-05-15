"""
https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.



Example 1:

Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
Example 2:

Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
Example 3:

Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".


Constraints:

2 <= number.length <= 100
number consists of digits from '1' to '9'.
digit is a digit from '1' to '9'.
digit occurs at least once in number.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 59 ms, faster than 18.11% of Python3 online submissions for Remove Digit From Number to Maximize Result.
# Memory Usage: 13.9 MB, less than 67.61% of Python3 online submissions for Remove Digit From Number to Maximize Result.
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        i = 0
        n = len(number)
        result, ri = "", 0
        while i < n:
            i = number.find(digit, i)
            if i == -1:
                break
            res = number[:i] + number[i+1:]
            resi = int(res)
            if resi > ri:
                result, ri = res, resi
            i += 1
        return result


tests = [
    ["123", "3", "12"],
    ["1231", "1", "231"],
    ["551", "5", "51"]
]

run_functional_tests(Solution().removeDigit, tests)
