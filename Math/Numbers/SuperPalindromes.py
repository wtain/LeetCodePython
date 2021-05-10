"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3736/
https://leetcode.com/problems/super-palindromes/

Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].



Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1


Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018].
left is less than or equal to right.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1724 ms, faster than 34.61% of Python3 online submissions for Super Palindromes.
# Memory Usage: 14.2 MB, less than 67.95% of Python3 online submissions for Super Palindromes.
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        MAGIC = 10 ** 5

        def reverse(x):
            result = 0
            while x:
                result = 10 * result + x % 10
                x //= 10
            return result

        def is_palindrome(x):
            return x == reverse(x)

        result = 0

        for k in range(MAGIC):
            s = str(k)
            t = s + s[-2::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                result += 1

        for k in range(MAGIC):
            s = str(k)
            t = s + s[::-1]
            v = int(t) ** 2
            if v > R:
                break
            if v >= L and is_palindrome(v):
                result += 1

        return result


tests = [
    ["4", "1000", 4],
    ["1", "2", 1]
]

run_functional_tests(Solution().superpalindromesInRange, tests)