"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3683/
https://leetcode.com/problems/advantage-shuffle/

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 980 ms, faster than 5.13% of Python3 online submissions for Advantage Shuffle.
# Memory Usage: 18.4 MB, less than 5.31% of Python3 online submissions for Advantage Shuffle.
# class Solution:
#     def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#         n = len(A)
#
#         def transform_arr(arr: List[int]) -> List[int]:
#             return sorted([[x, i] for (i, x) in enumerate(arr)])
#
#         At = transform_arr(A)
#         Bt = transform_arr(B)
#         result = [0] * n
#         A_used = [False] * n
#         for (b, i) in Bt:
#             j = bisect.bisect_right(At, [b+1, -1])
#             for k in range(n):
#                 if j == n:
#                     j = 0
#                 if not A_used[At[j][1]]:
#                     result[i] = At[j][0]
#                     A_used[At[j][1]] = True
#                     break
#                 j += 1
#
#         return result


# Runtime: 376 ms, faster than 41.76% of Python3 online submissions for Advantage Shuffle.
# Memory Usage: 17.6 MB, less than 34.25% of Python3 online submissions for Advantage Shuffle.
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)

        def transform_arr(arr: List[int]) -> List[List[int]]:
            return sorted([[x, i] for (i, x) in enumerate(arr)])

        Bt = transform_arr(B)
        A.sort()
        result = [0] * n
        A_used = [False] * n
        j = 0
        for i, ai in enumerate(A):
            if ai > Bt[j][0]:
                result[Bt[j][1]] = ai
                A_used[i] = True
                j += 1

        for i in range(n):
            if A_used[i]:
                continue
            result[Bt[j][1]] = A[i]
            A_used[i] = True
            j += 1

        return result


def checkAdvantage(A: List[int], B: List[int]):
    return sum([1 if ai > bi else 0 for (ai, bi) in zip(A, B)])


def customCheck(test, result) -> bool:
    B = test[1]
    expected = test[2]
    return checkAdvantage(expected, B) == checkAdvantage(result, B)


tests = [
    ([2,0,4,1,2], [1,3,0,0,2], [2,0,2,1,4]),

    ([2,7,11,15], [1,10,4,11], [2,11,7,15]),
    ([12,24,8,32], [13,25,32,11], [24,32,8,12])
]

run_functional_tests(Solution().advantageCount, tests, custom_check=customCheck)
