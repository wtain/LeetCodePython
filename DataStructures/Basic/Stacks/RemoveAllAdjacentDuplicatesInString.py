"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3794/

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.



Example 1:

Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.
"""
from functools import reduce

from Common.ObjectTestingUtils import run_functional_tests

# Runtime: 144 ms, faster than 14.18% of Python3 online submissions for Remove All Adjacent Duplicates In Strings.
# Memory Usage: 14.6 MB, less than 56.09% of Python3 online submissions for Remove All Adjacent Duplicates In Strings.
# Runtime: 80 ms, faster than 54.25% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.7 MB, less than 42.22% of Python3 online submissions for Remove All Adjacent Duplicates In String.
class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        for c in S:
            if len(st) > 0 and st[-1] == c:
                st.pop()
            else:
                st.append(c)
        return "".join(st)


# Runtime: 8520 ms, faster than 5.01% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.6 MB, less than 81.74% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         return "".join(reduce(lambda res, c: res[:-1] if len(res) > 0 and res[-1] == c else res + [c], S, []))


tests = [
    ["abbaca", "ca"]
]

run_functional_tests(Solution().removeDuplicates, tests)