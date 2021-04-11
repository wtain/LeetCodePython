"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3698/
https://leetcode.com/problems/minimum-operations-to-make-array-equal/

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.



Example 1:

Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
Example 2:

Input: n = 6
Output: 9


Constraints:

1 <= n <= 10^4
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 144 ms, faster than 17.25% of Python3 online submissions for Minimum Operations to Make Array Equal.
# Memory Usage: 14.4 MB, less than 24.50% of Python3 online submissions for Minimum Operations to Make Array Equal.
# class Solution:
#     def minOperations(self, n: int) -> int:
#         # 2*i+1
#         # S = Sum(2*i+1) = n + 2*Sum(i) =
#         # n + n*(n-1) = n**2
#         # avg = n
#         return sum([abs(n-2*i-1) for i in range(n)]) // 2

# Runtime: 24 ms, faster than 97.13% of Python3 online submissions for Minimum Operations to Make Array Equal.
# Memory Usage: 14.3 MB, less than 24.50% of Python3 online submissions for Minimum Operations to Make Array Equal.
class Solution:
    def minOperations(self, n: int) -> int:
        # 2*i+1
        # S = Sum(2*i+1) = n + 2*Sum(i) =
        # n + n*(n-1) = n**2
        # avg = n
        # return sum([abs(n-2*i-1) for i in range(n)]) // 2
        # = 2 * sum(n-2*i-1)[0..n//2] = 2 * (n*n//2 - n//2 - 2 * n*(n//2-1)//2)
        # = n**2 - n - n**2 - 2*n
        return n**2 // 4



tests = [
    (3, 2),
    (6, 9)
]

run_functional_tests(Solution().minOperations, tests)