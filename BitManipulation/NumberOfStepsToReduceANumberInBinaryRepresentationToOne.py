"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.



Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.
Step 5) 4 is even, divide by 2 and obtain 2.
Step 6) 2 is even, divide by 2 and obtain 1.
Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.
Example 3:

Input: s = "1"
Output: 0


Constraints:

1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numSteps(self, s: str) -> int:
#         result = 0
#         n = len(s)
#         i = n-1
#         carry = 0
#         while i > 0:
#             while i > 0 and s[i] == '0':
#                 i -= 1
#                 result += 1
#             if i == 0:
#                 break
#             i0 = i
#             while i >= 0 and s[i] == '1':
#                 i -= 1
#             m = i0 - i
#             result += m + 1
#             carry = 1
#         if carry:
#             result += 1
#         return result

# Runtime
# 29 ms
# Beats
# 88.43%
# Memory
# 13.9 MB
# Beats
# 14.88%
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/solutions/1184352/java-python-clean-concise-clear-explanation-o-n/
class Solution:
    def numSteps(self, s: str) -> int:
        result, carry = 0, 0
        n = len(s)
        for i in range(n-1, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                result += 2
            else:
                result += 1
        return result + carry


tests = [
    ["1100011101", 15],
    ["1101", 6],
    ["10", 1],
    ["1", 0],
]

run_functional_tests(Solution().numSteps, tests)
