"""
https://leetcode.com/problems/sort-array-by-parity-ii/
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3990/
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

Runtime: 200 ms, faster than 86.54% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 16.1 MB, less than 98.90% of Python3 online submissions for Sort Array By Parity II.
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        l = 0
        r = n - 1
        while True:
            while l < n and A[l] % 2 == 0:
                l += 2
            while 0 <= r and A[r] % 2 != 0:
                r -= 2
            if l >= n or r < 0:
                break
            A[l], A[r] = A[r], A[l]
            l += 2
            r -= 2
        return A


tests = [
    [4,2,5,7]
]


def isSortedByParity(A: List[int]) -> bool:
    n = len(A)
    for i in range(n):
        if i % 2 != A[i] % 2:
            return False
    return True


def isMadeOfSameItems(A: List[int], B: List[int]) -> bool:
    return sorted(A) == sorted(B)


for test in tests:
    result = Solution().sortArrayByParityII(test.copy())
    if isSortedByParity(result) and isMadeOfSameItems(test, result):
        print("PASS")
    else:
        print("FAIL - " + str(result))