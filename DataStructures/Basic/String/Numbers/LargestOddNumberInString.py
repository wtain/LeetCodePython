"""
https://leetcode.com/problems/largest-odd-number-in-string/

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.


Constraints:

1 <= num.length <= 105
num only consists of digits and does not contain any leading zeros.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 98.37% of Python3 online submissions for Largest Odd Number in String.
# Memory Usage: 15.3 MB, less than 58.41% of Python3 online submissions for Largest Odd Number in String.
class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2:
                return num[:i+1]
        return ""


tests = [
    ["52", "5"],
    ["4206", ""],
    ["35427", "35427"]
]

run_functional_tests(Solution().largestOddNumber, tests)