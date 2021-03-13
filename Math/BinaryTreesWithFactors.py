"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3670/
https://leetcode.com/problems/binary-trees-with-factors/

Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.



Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].


Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 109
"""
from typing import List


"""
  n0
n1  n2

F(n0) = F(n1) * F(n2) if n1 != n2 else F(n1)

a0 < a1 < a2 < ... < a(n-1)

F(a0) = 1


"""


# Runtime: 388 ms, faster than 73.04% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 14.4 MB, less than 86.09% of Python3 online submissions for Binary Trees With Factors.
# Runtime: 384 ms, faster than 74.78% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 14.4 MB, less than 73.91% of Python3 online submissions for Binary Trees With Factors.
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr = sorted(set(arr))
        n = len(arr)
        dp = {arr[i]: 1 for i in range(n)}
        for i in range(n):
            ai = arr[i]
            for j in range(i):
                if ai % arr[j] == 0:
                    d = ai // arr[j]
                    if d not in dp.keys():
                        continue
                    dp[ai] += dp[d] * dp[arr[j]]
                    dp[ai] %= MOD
        return sum(dp.values()) % MOD


tests = [
    ([2, 4, 16], 8),

    ([2, 3, 6, 8, 34, 36], 17),

    ([2, 3, 6, 8, 18, 30, 34, 36], 39),

    ([2, 3, 6, 8, 18, 30, 34, 36, 38, 43], 41),

    ([2, 3, 6, 8, 18, 26, 30, 34, 36, 38, 39, 43], 43),

    ([2, 3, 6, 8, 13, 14, 18, 21, 26, 30, 34, 36, 38, 39, 43, 49], 51),

    ([2,18,6,26,21,49,14,8,13,3,36,34,38,39,30,43], 51),

    ([2,18,6,26,21,49,31,14,19,8,13,3,36,34,38,39,30,43], 55),

    ([2,18,37,6,26,21,49,31,14,19,8,13,3,36,34,38,39,30,43], 56),

    ([2,18,23,1170,759,37,6,26,21,49,31,14,19,8,13,3,36,34,38,39,30,43], 65),

    ([2,18,23,1170,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43], 73),

    ([45,42,2,18,23,1170,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43], 99),

    ([45,42,2,18,23,1170,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43], 125),

    ([45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43], 200),

    ([45,42,2,18,23,1170,12,41,40,9,47,24,33,28,10,32,29,17,46,11,759,37,6,26,21,49,31,14,19,8,13,7,27,22,3,36,34,38,39,30,43,15,4,16,35,25,20,44,5,48], 777),

    ([15,13,22,7,11], 5),

    ([2,4], 3),
    ([2,4,5,10], 7)
]

for test in tests:
    result = Solution().numFactoredBinaryTrees(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))