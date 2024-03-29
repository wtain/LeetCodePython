"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3697/
https://leetcode.com/problems/global-and-local-inversions/

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 328 ms, faster than 78.93% of Python3 online submissions for Global and Local Inversions.
# Memory Usage: 15.1 MB, less than 44.06% of Python3 online submissions for Global and Local Inversions.
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i, a in enumerate(A):
            if abs(a - i) > 1:
                return False
        return True


tests = [
    ([1,0,2], True),
    ([1,2,0], False)
]

run_functional_tests(Solution().isIdealPermutation, tests)