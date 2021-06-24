"""
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.



Example 1:

Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
Example 2:

Input: s = "10"
Output: 0
Explanation: s is already alternating.
Example 3:

Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".


Constraints:

1 <= s.length <= 104
s[i] is either '0' or '1'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 76 ms, faster than 19.53% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
# Memory Usage: 14.4 MB, less than 38.12% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
# class Solution:
#     def minOperations(self, s: str) -> int:
#         cnt1 = cnt2 = 0
#         for i, c in enumerate(s):
#             b = i % 2
#             if c != str(b):
#                 cnt1 += 1
#             if c != str(1-b):
#                 cnt2 += 1
#         return min(cnt1, cnt2)


# Runtime: 80 ms, faster than 15.88% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
# Memory Usage: 14.3 MB, less than 65.65% of Python3 online submissions for Minimum Changes To Make Alternating Binary String.
class Solution:
    def minOperations(self, s: str) -> int:
        return min(sum([c != str(i % 2) for i, c in enumerate(s)]), sum([c != str(1 - i % 2) for i, c in enumerate(s)]))



tests = [
    ["110010", 2],
    ["0100", 1],
    ["10", 0],
    ["1111", 2]
]

run_functional_tests(Solution().minOperations, tests)