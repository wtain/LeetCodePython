"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

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


# Runtime: 144 ms, faster than 14.18% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.6 MB, less than 56.09% of Python3 online submissions for Remove All Adjacent Duplicates In String.
class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        for c in S:
            if len(st) > 0 and st[-1] == c:
                st.pop()
            else:
                st.append(c)
        return "".join(st)


tests = [
    ("abbaca", "ca")
]

for test in tests:
    result = Solution().removeDuplicates(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + result)