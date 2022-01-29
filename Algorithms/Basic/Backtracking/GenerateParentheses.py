"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3781/
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


# Runtime: 28 ms, faster than 95.71% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.5 MB, less than 86.85% of Python3 online submissions for Generate Parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        targetLength = 2 * n
        result = []
        toProcess = [("(", 1, 1)]
        while toProcess:
            s, balance, totalOpen = toProcess.pop()
            if len(s) == targetLength:
                result.append(s)
            else:
                if totalOpen < n:
                    toProcess.append((s + "(", balance+1, totalOpen+1))
                if balance > 0:
                    toProcess.append((s + ")", balance - 1, totalOpen))
        return result


tests = [
    [3, ["((()))","(()())","(())()","()(())","()()()"]],
    [1, ["()"]]
]

run_functional_tests(Solution().generateParenthesis, tests, custom_check=compareSets)