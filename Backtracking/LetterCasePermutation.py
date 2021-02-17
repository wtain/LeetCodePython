"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/
https://leetcode.com/problems/letter-case-permutation/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.



Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: S = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: S = "12345"
Output: ["12345"]
Example 4:

Input: S = "0"
Output: ["0"]


Constraints:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
from typing import List


# Runtime: 52 ms, faster than 88.03% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 14.9 MB, less than 45.99% of Python3 online submissions for Letter Case Permutation.
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []

        result.append("")
        n = len(S)
        for i in range(n):
            if str.isdigit(S[i]):
                for j in range(len(result)):
                    result[j] += S[i]
                continue
            result2 = []
            for r in result:
                u = str.upper(S[i])
                l = str.lower(S[i])
                result2.append(r + l)
                result2.append(r + u)
            result = result2

        return result


tests = [
    ("a1b2", ["a1b2","a1B2","A1b2","A1B2"]),
    ("3z4", ["3z4","3Z4"]),
    ("12345", ["12345"]),
    ("0", ["0"])
]

for test in tests:
    result = Solution().letterCasePermutation(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
