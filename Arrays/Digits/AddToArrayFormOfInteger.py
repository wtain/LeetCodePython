"""
https://leetcode.com/problems/add-to-array-form-of-integer/
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.



Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000


Note：

1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0

Runtime: 256 ms, faster than 96.82% of Python3 online submissions for Add to Array-Form of Integer.
Memory Usage: 15.1 MB, less than 44.15% of Python3 online submissions for Add to Array-Form of Integer.
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        i = len(A)-1
        while K > 0 or carry:
            Ai = A[i] if i >= 0 else 0
            Ki = K % 10
            K = int(K / 10)
            result = Ai + Ki + carry
            carry = int(result / 10)
            result %= 10
            if i >= 0:
                A[i] = result
                i -= 1
            else:
                A.insert(0, result)
        return A


tests = [
    ([1,2,0,0], 34, [1,2,3,4]),
    ([2,7,4], 181, [4,5,5]),
    ([2,1,5], 806, [1,0,2,1]),
    ([9,9,9,9,9,9,9,9,9,9], 1, [1,0,0,0,0,0,0,0,0,0,0])
]

for test in tests:
    result = Solution().addToArrayForm(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))