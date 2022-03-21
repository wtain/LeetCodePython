"""
https://leetcode.com/problems/validate-stack-sequences/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3653/

Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.


Constraints:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values.
"""
from typing import List


# Runtime: 72 ms, faster than 63.35% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.2 MB, less than 95.41% of Python3 online submissions for Validate Stack Sequences.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        n = len(pushed)
        j = 0
        for i in range(n):
            st.append(pushed[i])
            while st and j < n and st[-1] == popped[j]:
                st.pop()
                j += 1
        return not st


tests = [
    [[1,2,3,4,5], [4,5,3,2,1], True],
    [[1,2,3,4,5], [4,3,5,1,2], False]
]

run_functional_tests(Solution().validateStackSequences, tests)
