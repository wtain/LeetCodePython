"""
https://leetcode.com/problems/remove-k-digits/

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 42 ms, faster than 78.53% of Python3 online submissions for Remove K Digits.
# Memory Usage: 14 MB, less than 98.88% of Python3 online submissions for Remove K Digits.
# https://leetcode.com/submissions/detail/338878250/
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = ""
        n = len(num)
        for i in range(n):
            while result and k > 0 and result[-1] > num[i]:
                k -= 1
                result = result[:-1]
            result += num[i]
            if result == "0":
                result = ""
        if k > 0:
            if len(result) >= k:
                result = result[0:-k]
            else:
                result = ""
        if not result:
            result = "0"
        return result


tests = [
    ["1432219", 3, "1219"],
    ["10200", 1, "200"],
    ["10", 2, "0"]
]

run_functional_tests(Solution().removeKdigits, tests)
