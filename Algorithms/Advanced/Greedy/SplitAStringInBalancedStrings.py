"""
https://leetcode.com/problems/split-a-string-in-balanced-strings/
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.



Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'


Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


# Runtime: 32 ms, faster than 59.24% of Python3 online submissions for Split a Strings in Balanced Strings.
# Memory Usage: 14 MB, less than 88.78% of Python3 online submissions for Split a Strings in Balanced Strings.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        balanse = 0
        for c in s:
            if c == 'L':
                balanse -= 1
            else:
                balanse += 1
            if not balanse:
                cnt += 1
        return cnt


tests = [
    ("RLRRLLRLRL", 4),
    ("RLLLLRRRLR", 3),
    ("LLLLRRRR", 1),
    ("RLRRRLLRLL", 2)
]

for test in tests:
    result = Solution().balancedStringSplit(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))