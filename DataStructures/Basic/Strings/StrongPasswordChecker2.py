"""
https://leetcode.com/problems/strong-password-checker-ii/

A password is said to be strong if it satisfies all the following criteria:

It has at least 8 characters.
It contains at least one lowercase letter.
It contains at least one uppercase letter.
It contains at least one digit.
It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
Given a string password, return true if it is a strong password. Otherwise, return false.



Example 1:

Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.


Constraints:

1 <= password.length <= 100
password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 34 ms
# Beats
# 90%
# Memory
# 13.8 MB
# Beats
# 76.4%
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if all(password.find(c) == -1 for c in "abcdefghijklmnopqrstuvwxyz"):
            return False
        if all(password.find(c) == -1 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            return False
        if all(password.find(c) == -1 for c in "0123456789"):
            return False
        if all(password.find(c) == -1 for c in "!@#$%^&*()-+"):
            return False
        n = len(password)
        for i in range(1, n):
            if password[i] == password[i-1]:
                return False
        return True


tests = [
    ["IloveLe3tcode!", True],
    ["Me+You--IsMyDream", False],
    ["1aB!", False]
]

run_functional_tests(Solution().strongPasswordCheckerII, tests)
